

### The New Architecture: A Pipeline

The data will now flow through a series of dedicated workers and queues:

1.  **Producer (`producer.py`)**: Seeds the initial URLs.
    *   Publishes to: `urls_to_fetch` queue.

2.  **Fetcher Worker (`fetcher.py`)**: Handles all network fetching and pre-validation.
    *   Consumes from: `urls_to_fetch` queue.
    *   **Tasks**:
        *   Checks `robots.txt`.
        *   Checks Redis to see if the URL has already been visited.
        *   If checks pass, it fetches the raw HTML.
    *   Publishes `(URL, HTML_content)` to: `pages_to_parse` queue.

3.  **Parser Worker (`parser.py`)**: Handles CPU-intensive parsing and link extraction.
    *   Consumes from: `pages_to_parse` queue.
    *   **Tasks**:
        *   Parses the HTML.
        *   Extracts the title and all valid, normalized links.
        *   **Closes the loop**: Publishes the newly found links back to the `urls_to_fetch` queue for the fetchers to process.
    *   Publishes `(URL, Title, Links)` to: `data_to_save` queue.

4.  **Saver Worker (`saver.py`)**: Handles all database writes.
    *   Consumes from: `data_to_save` queue.
    *   **Tasks**:
        *   Saves the page data to MongoDB.
        *   Saves the graph structure (nodes and relationships) to Neo4j.

This creates a clean, unidirectional data flow with a feedback loop for new links.

---

### 1. Updated Code Files

The `shared_utils.py` file remains the same. We will create three new worker files and update the producer. We'll also use `json` to pass structured data through RabbitMQ.

#### `producer.py` (Slightly Modified)

The only change is the queue name to match the new pipeline.

```python
# producer.py
import pika
import json
from shared_utils import normalize_url

def send_seed_url():
    """Connects to RabbitMQ and sends a normalized seed URL."""
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        # The first queue in our pipeline
        queue_name = 'urls_to_fetch'
        channel.queue_declare(queue=queue_name, durable=True)

        seed_urls = [
            'https://en.wikipedia.org/wiki/Python_(programming_language)',
        ]

        for url in seed_urls:
            normalized = normalize_url(url)
            channel.basic_publish(
                exchange='',
                routing_key=queue_name,
                body=normalized,
                properties=pika.BasicProperties(
                    delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
                ))
            print(f" [x] Sent seed URL: '{normalized}' to queue '{queue_name}'")

        connection.close()
    except pika.exceptions.AMQPConnectionError as e:
        print(f"Error: Could not connect to RabbitMQ. Is the service running? Details: {e}")

if __name__ == '__main__':
    send_seed_url()
```

#### `fetcher.py` (New Worker)

```python
# fetcher.py
import pika
import redis
import requests
import time
import json
from shared_utils import can_fetch

# --- Configuration ---
RABBITMQ_HOST = 'localhost'
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
CRAWL_DELAY = 1
USER_AGENT = "MyWikipediaCrawler/1.0"
HEADERS = {'User-Agent': USER_AGENT}
VISITED_URLS_KEY = 'visited_urls'

# --- Connections ---
redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0, decode_responses=True)
connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
channel = connection.channel()

# --- Queue Declarations ---
channel.queue_declare(queue='urls_to_fetch', durable=True)
channel.queue_declare(queue='pages_to_parse', durable=True)

def fetch_url(url):
    """Fetches the content of a URL after performing checks."""
    # 1. Check if URL is allowed by robots.txt
    if not can_fetch(url, USER_AGENT):
        print(f"[Fetcher] Skipping (disallowed by robots.txt): {url}")
        return None

    # 2. Check Redis BEFORE fetching to save bandwidth
    if redis_client.sismember(VISITED_URLS_KEY, url):
        print(f"[Fetcher] Skipping (already visited): {url}")
        return None

    # 3. Mark as visited *immediately* to prevent other fetchers from grabbing it
    redis_client.sadd(VISITED_URLS_KEY, url)
    print(f"[Fetcher] Processing: {url}")

    try:
        time.sleep(CRAWL_DELAY)
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"[Fetcher] ERROR fetching {url}: {e}")
        # If fetching fails, remove from visited set so it can be retried later
        redis_client.srem(VISITED_URLS_KEY, url)
        return None

def callback(ch, method, properties, body):
    url = body.decode()
    html_content = fetch_url(url)

    if html_content:
        message = {'url': url, 'html': html_content}
        ch.basic_publish(
            exchange='',
            routing_key='pages_to_parse',
            body=json.dumps(message),
            properties=pika.BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE)
        )
        print(f"[Fetcher] Sent page content for {url} to be parsed.")

    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='urls_to_fetch', on_message_callback=callback)

print('[Fetcher] Waiting for URLs. To exit press CTRL+C')
try:
    channel.start_consuming()
except KeyboardInterrupt:
    print("Fetcher shutting down.")
    connection.close()
```

#### `parser.py` (New Worker)

```python
# parser.py
import pika
import json
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from shared_utils import normalize_url

# --- Configuration ---
RABBITMQ_HOST = 'localhost'

# --- Connections ---
connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
channel = connection.channel()

# --- Queue Declarations ---
channel.queue_declare(queue='pages_to_parse', durable=True)
channel.queue_declare(queue='data_to_save', durable=True)
channel.queue_declare(queue='urls_to_fetch', durable=True) # To close the loop

def parse_content(url, html):
    """Parses HTML to extract title and valid links."""
    print(f"[Parser] Parsing {url}")
    soup = BeautifulSoup(html, 'lxml')
    title = soup.find('h1', id='firstHeading').text if soup.find('h1', id='firstHeading') else "No Title Found"
    content_div = soup.find('div', id='mw-content-text')
    
    found_links = set()
    if content_div:
        base_netloc = urlparse(url).netloc
        for a in content_div.find_all('a', href=True):
            href = a['href']
            if href.startswith('/wiki/') and ':' not in href and not href.endswith(('.png', '.jpg', '.svg')):
                normalized_link = normalize_url(href, base_domain=base_netloc)
                if urlparse(normalized_link).netloc.endswith('.wikipedia.org'):
                    found_links.add(normalized_link)
    
    print(f"[Parser] Found {len(found_links)} links in {url}")
    return title, list(found_links)

def callback(ch, method, properties, body):
    message = json.loads(body)
    url, html = message['url'], message['html']
    
    title, links = parse_content(url, html)
    
    # 1. Send the parsed data onward to the saver
    data_to_save = {'url': url, 'title': title, 'links': links}
    ch.basic_publish(
        exchange='',
        routing_key='data_to_save',
        body=json.dumps(data_to_save),
        properties=pika.BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE)
    )
    
    # 2. Feed the newly found links back into the fetch queue (close the loop)
    for link in links:
        ch.basic_publish(
            exchange='',
            routing_key='urls_to_fetch',
            body=link,
            properties=pika.BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE)
        )
        
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='pages_to_parse', on_message_callback=callback)

print('[Parser] Waiting for pages to parse. To exit press CTRL+C')
try:
    channel.start_consuming()
except KeyboardInterrupt:
    print("Parser shutting down.")
    connection.close()
```

#### `saver.py` (New Worker)

```python
# saver.py
import pika
import json
import time
from pymongo import MongoClient
from neo4j import GraphDatabase

# --- Configuration ---
RABBITMQ_HOST = 'localhost'
MONGODB_URI = 'mongodb://localhost:27017/'
NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "your_strong_password"

# --- Connections ---
mongo_client = MongoClient(MONGODB_URI)
db = mongo_client['wikipedia']
pages_collection = db['pages']
neo4j_driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
channel = connection.channel()

# --- Queue Declaration ---
channel.queue_declare(queue='data_to_save', durable=True)

def save_to_databases(data):
    """Saves parsed data to MongoDB and Neo4j."""
    url = data['url']
    title = data['title']
    links = data['links']
    
    print(f"[Saver] Saving data for {url}")
    
    # 1. Save to MongoDB
    mongo_doc = {'url': url, 'title': title, 'links': links, 'saved_at': time.time()}
    pages_collection.replace_one({'url': url}, mongo_doc, upsert=True)
    
    # 2. Save to Neo4j
    with neo4j_driver.session() as session:
        session.run("MERGE (p:Page {url: $url}) SET p.title = $title", url=url, title=title)
        for link in links:
            session.run("MERGE (p:Page {url: $url})", url=link)
            session.run("""
                MATCH (source:Page {url: $source_url})
                MATCH (target:Page {url: $target_url})
                MERGE (source)-[:LINKS_TO]->(target)
                """, source_url=url, target_url=link)
    
    print(f"[Saver] Successfully saved {url}")

def callback(ch, method, properties, body):
    data = json.loads(body)
    try:
        save_to_databases(data)
    except Exception as e:
        print(f"[Saver] ERROR saving data for {data['url']}: {e}")
        # Here you might want to requeue the message or send it to a dead-letter queue
    finally:
        ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='data_to_save', on_message_callback=callback)

print('[Saver] Waiting for data to save. To exit press CTRL+C')
try:
    channel.start_consuming()
except KeyboardInterrupt:
    print("Saver shutting down.")
    connection.close()
    mongo_client.close()
    neo4j_driver.close()
```

---

### 2. Updated `docker-compose.yml`

Now we define each worker as a separate service. This allows us to scale them independently.

```yaml
version: '3.8'
services:
  rabbitmq:
    image: "rabbitmq:3-management"
    ports:
      - "5672:5672"
      - "15672:15672"
    volumes:
      - rabbitmq_data:/var/lib/rabbitmq/
    networks:
      - app-network

  mongodb:
    image: "mongo:latest"
    ports:
      - "27017:27017"
    volumes:
      - mongodb_data:/data/db
    networks:
      - app-network

  redis:
    image: "redis:latest"
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    networks:
      - app-network

  fetcher:
    build: .
    command: python fetcher.py
    depends_on:
      - rabbitmq
      - redis
    networks:
      - app-network
    # To scale fetchers: add a deploy block
    deploy:
      replicas: 2 # Example: run 2 fetcher instances

  parser:
    build: .
    command: python parser.py
    depends_on:
      - rabbitmq
    networks:
      - app-network
    deploy:
      replicas: 2 # Example: run 2 parser instances

  saver:
    build: .
    command: python saver.py
    depends_on:
      - rabbitmq
      - mongodb
      - redis # Though not directly used, good to have it ready
    networks:
      - app-network
    deploy:
      replicas: 1 # Saving is often sequential, but can be scaled if needed

volumes:
  rabbitmq_data:
  mongodb_data:
  redis_data:

networks:
  app-network:
    driver: bridge
```

### How to Run the New System

1.  **Build the Image**: Since all workers use the same base image, you only need to build it once.
    ```bash
    docker-compose build
    ```

2.  **Start the Services**: Use the `up` command. Docker Compose will start one of each service by default. To use the `replicas` feature, you'd typically use Docker Swarm (`docker swarm init` and `docker stack deploy`), but for local testing, you can scale manually.
    ```bash
    # Start all services (one of each worker)
    docker-compose up -d

    # To scale a specific worker (e.g., add another fetcher)
    docker-compose up -d --scale fetcher=3
    ```
    And don't forget to start Neo4j with its separate compose file.

3.  **Seed the Queue**:
    ```bash
    python producer.py
    ```

4.  **Monitor the Flow**:
    *   Check the logs for each worker: `docker-compose logs -f fetcher`, `docker-compose logs -f parser`, etc.
    *   Open the RabbitMQ Management UI at `http://localhost:15672` (user: `guest`, pass: `guest`). You will see the three queues and can watch messages flow from one to the next.