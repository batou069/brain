---
tags:
  - python
  - scrapy
  - web_scraping
  - middleware
  - downloader_middleware
  - spider_middleware
  - customization
  - concept
  - example
aliases:
  - Scrapy Middlewares
  - Downloader Middleware
  - Spider Middleware
related:
  - "[[160_Python_Libraries/Scrapy/_Scrapy_MOC|_Scrapy_MOC]]"
  - "[[Scrapy_Settings]]"
worksheet:
  - WS_WebScraping_1
date_created: 2025-06-11
---
# Scrapy: Middleware (Downloader and Spider Middleware)

Scrapy Middleware are hooks into Scrapy’s request/response processing framework. They provide a way to plug custom code to modify how Scrapy handles requests and responses globally across your project or for specific spiders.

There are two main types of middleware:
1.  **Downloader Middleware:** Sits between the Scrapy Engine and the Downloader. It processes requests just before they are sent to the website and responses just after they are received from the website.
2.  **Spider Middleware:** Sits between the Scrapy Engine and the Spiders. It processes spider output (requests and items) and can modify initial requests sent from the spider.

## 1. Downloader Middleware
Downloader middleware components are processed sequentially for each request and response.

**Key Methods to Implement in a Downloader Middleware Class:**
-   **`process_request(self, request, spider)`:**
    -   Called for each request that passes through the downloader middleware.
    -   Must either:
        -   Return `None`: Scrapy continues processing this request, executing other middleware’s `process_request` and then the downloader.
        -   Return a `Response` object: Scrapy won’t call any other `process_request` or the downloader; it returns this response directly. Other middleware's `process_response` will be called.
        -   Return a `Request` object: Scrapy stops `process_request` chain and reschedules the returned request.
        -   Raise `IgnoreRequest`: The request is ignored, and other middleware's `process_exception` is called.
    -   **Use Cases:** Modifying request headers (e.g., User-Agent, cookies), adding proxies, handling HTTP authentication, filtering out requests to certain domains.
-   **`process_response(self, request, response, spider)`:**
    -   Called with the response returned from the Downloader (or another `process_request` that returned a Response).
    -   Must either:
        -   Return a `Response` object: Passed to the next middleware's `process_response` or to the spider.
        -   Return a `Request` object: Stops `process_response` chain, original request is rescheduled. The new request goes through `process_request` again.
        -   Raise `IgnoreRequest`: The spider's `errback` for the original request is called.
    -   **Use Cases:** Modifying response content (e.g., decompressing, decoding), handling specific HTTP status codes (e.g., retrying on 503), scraping data that is common to all pages.
-   **`process_exception(self, request, exception, spider)`:**
    -   Called when the downloader or a `process_request` method from a previous middleware raises an exception (including `IgnoreRequest`).
    -   Must either:
        -   Return `None`: Scrapy continues processing the exception with subsequent middleware.
        -   Return a `Response` object: Stops exception processing, starts `process_response` chain.
        -   Return a `Request` object: Stops exception processing, reschedules the new request.
    -   **Use Cases:** Custom retry logic, logging specific errors.

**Example: Custom User-Agent Downloader Middleware**
```python
# myproject/middlewares.py
import random

class RandomUserAgentMiddleware:
    def __init__(self, user_agents):
        self.user_agents = user_agents

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        # You can get settings from crawler.settings
        user_agents_list = crawler.settings.getlist('MY_USER_AGENTS', [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ...', # A default if not set
            'Another User Agent String...'
        ])
        return cls(user_agents_list)

    def process_request(self, request, spider):
        # Randomly select a User-Agent for the request
        user_agent = random.choice(self.user_agents)
        if user_agent:
            request.headers.setdefault('User-Agent', user_agent)
            spider.logger.debug(f"Using User-Agent: {user_agent} for {request.url}")
        return None # Continue processing

# To enable in settings.py:
# DOWNLOADER_MIDDLEWARES = {
#    'myproject.middlewares.RandomUserAgentMiddleware': 543, # Order matters
# }
# MY_USER_AGENTS = [
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ... Chrome/90...",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 ... Safari/15...",
#     # ... more user agents ...
# ]
```

## 2. Spider Middleware
Spider middleware components are processed for requests sent from the spider and for items/requests yielded by the spider.

**Key Methods to Implement in a Spider Middleware Class:**
-   **`process_spider_input(self, response, spider)`:**
    -   Called for each response that passes through the spider middleware and is processed by the spider.
    -   Should return `None` or raise an exception.
    -   **Use Cases:** Logging, modifying response before spider sees it (rare).
-   **`process_spider_output(self, response, result, spider)`:**
    -   Called with the results (requests or items) returned by the Spider, after it has processed the response.
    -   Must return an iterable of `Request` objects, dictionaries, or `Item` objects.
    -   **Use Cases:** Filtering items, modifying items (e.g., adding a timestamp), generating new requests based on item content.
-   **`process_spider_exception(self, response, exception, spider)`:**
    -   Called when a spider or `process_spider_input()` method (from a previous spider middleware) raises an exception.
    -   Should return either `None` (to continue processing the exception with subsequent middleware) or an iterable of `Request`, `dict` or `Item` objects.
-   **`process_start_requests(self, start_requests, spider)`:**
    -   Called with the start requests of the spider. Works like `process_spider_output` but for initial requests.
    -   Must return an iterable of `Request` objects.
    -   **Use Cases:** Modifying the initial set of requests (e.g., filtering URLs, adding cookies).

**Example: Spider Middleware to Add a Timestamp to Items**
```python
# myproject/middlewares.py
import datetime

class AddTimestampSpiderMiddleware:
    def process_spider_output(self, response, result, spider):
        for i in result: # result is an iterable of Requests or Items
            if isinstance(i, scrapy.Item) or isinstance(i, dict): # Check if it's an item-like object
                # Assuming your item has a 'scraped_at' field
                i['scraped_at_timestamp'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
            yield i # Must yield all results (requests or items)

# To enable in settings.py:
# SPIDER_MIDDLEWARES = {
#    'myproject.middlewares.AddTimestampSpiderMiddleware': 543,
# }
```

## Enabling Middleware
Middleware are enabled and ordered in the `settings.py` file using the `DOWNLOADER_MIDDLEWARES` and `SPIDER_MIDDLEWARES` dictionaries. The integer values determine the order of execution (lower values are processed closer to the Engine for requests, and closer to the Downloader/Spider for responses).

Scrapy comes with several built-in middleware (e.g., for handling cookies, HTTP compression, retries, `robots.txt`). Custom middleware are merged with these based on their order.

Middleware provide a powerful mechanism to extend and customize Scrapy's functionality at various points in the crawling process.

---