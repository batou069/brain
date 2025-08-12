---
tags:
  - python
  - scrapy
  - web_scraping
  - item_pipeline
  - data_processing
  - data_storage
  - concept
  - example
aliases:
  - Scrapy Pipelines
  - Item Processing Pipeline
related:
  - "[[160_Python_Libraries/Scrapy/_Scrapy_MOC|_Scrapy_MOC]]"
  - "[[Scrapy_Items]]"
  - "[[Scrapy_Spiders]]"
  - "[[Scrapy_Settings]]"
worksheet:
  - WS_WebScraping_1
date_created: 2025-06-09
---
# Scrapy: Item Pipelines

After a [[Scrapy_Items|Scrapy Item]] has been scraped by a [[Scrapy_Spiders|Spider]], it is sent to the **Item Pipeline**. The Item Pipeline is a sequence of custom components that process these items. Each component (called an "item pipeline") is a Python class that implements a simple interface.

Item pipelines are commonly used for:
-   Cleaning HTML data (e.g., removing unwanted tags, normalizing whitespace).
-   Validating scraped data (e.g., checking if required fields are present, if data types are correct).
-   Checking for and dropping duplicate items.
-   Storing the scraped item in a database (e.g., SQLite, MySQL, PostgreSQL, MongoDB).
-   Writing the scraped item to a file (e.g., JSON, CSV, XML).
-   Sending items to an external API or message queue.

## Structure of an Item Pipeline
An item pipeline is a Python class that must implement one or more of the following methods:

1.  **`process_item(self, item, spider)`:**
    -   This method is called for every item yielded by a spider.
    -   It must either:
        -   Return the item (either the original or a modified version) to continue processing by subsequent pipelines.
        -   Return a `Deferred` for asynchronous operations (less common for simple pipelines).
        -   Raise a `DropItem` exception to discard the item and stop its processing by further pipelines.
    -   `item`: The scraped item object (or dictionary).
    -   `spider`: The spider that scraped the item.

2.  **`open_spider(self, spider)` (Optional):**
    -   Called when the spider is opened (starts crawling).
    -   Useful for initializing resources (e.g., opening a database connection, opening a file).
    -   `spider`: The spider that was opened.

3.  **`close_spider(self, spider)` (Optional):**
    -   Called when the spider is closed (finishes crawling or is stopped).
    -   Useful for cleaning up resources (e.g., closing a database connection, closing a file).
    -   `spider`: The spider that was closed.

4.  **`from_crawler(cls, crawler)` (Optional, Class Method):**
    -   A class method used by Scrapy to create an instance of your pipeline.
    -   It can access Scrapy settings and signals via the `crawler` object.
    -   Useful for initializing the pipeline with settings-dependent parameters.

## Enabling an Item Pipeline
Pipelines are defined in the `pipelines.py` file of your Scrapy project. To enable a pipeline, you must add its class path to the `ITEM_PIPELINES` setting in your project's `settings.py` file. The order is defined by an integer value (lower values are processed first, typically 0-1000).

**Example: `settings.py`**
```python
# settings.py
# ... other settings ...

ITEM_PIPELINES = {
   'myproject.pipelines.PriceValidationPipeline': 300, # Lower number = earlier execution
   'myproject.pipelines.DuplicatesPipeline': 400,
   'myproject.pipelines.JsonWriterPipeline': 800,
   # 'myproject.pipelines.MongoPipeline': 850, # Example for MongoDB
}
```

## Example Pipelines

### 1. Price Validation and Conversion Pipeline
This pipeline checks if a price field exists, converts it to a float, and drops items without a valid price.

```python
# myproject/pipelines.py
import re
from scrapy.exceptions import DropItem

class PriceValidationPipeline:
    def process_item(self, item, spider):
        # Assuming item has a 'price' field which is a string like "$29.99" or "Contact us"
        if 'price' in item and item['price']:
            price_str = str(item['price']).strip()
            # Try to extract numeric part
            match = re.search(r'[\d\.]+', price_str.replace(',', ''))
            if match:
                try:
                    item['price'] = float(match.group(0))
                    return item
                except ValueError:
                    raise DropItem(f"Invalid price format after regex: {price_str} in {item['product_url']}")
            else:
                # If no numeric part found, consider it invalid for this example
                raise DropItem(f"Price not found or invalid format: {price_str} in {item['product_url']}")
        else:
            raise DropItem(f"Missing price in {item.get('product_url', 'Unknown URL')}")
```

### 2. Duplicate Product URL Pipeline
This pipeline drops items that have already been scraped (based on product URL).

```python
# myproject/pipelines.py
from scrapy.exceptions import DropItem

class DuplicatesPipeline:
    def __init__(self):
        self.urls_seen = set() # Set to store URLs encountered so far

    def process_item(self, item, spider):
        if 'product_url' in item:
            if item['product_url'] in self.urls_seen:
                raise DropItem(f"Duplicate item found: {item['product_url']}")
            else:
                self.urls_seen.add(item['product_url'])
                return item
        else:
            # If no URL, pass it through or handle as per requirements
            return item 
```

### 3. JSON Writer Pipeline
This pipeline writes each scraped item to a JSON Lines file.

```python
# myproject/pipelines.py
import json

class JsonWriterPipeline:
    def open_spider(self, spider):
        # Open file in append mode, one JSON object per line
        self.file = open(f'{spider.name}_items.jl', 'a')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n" # Convert Scrapy Item to dict for json.dumps
        self.file.write(line)
        return item # Return item for further processing if any
```
> **Note:** Scrapy has built-in Feed Exporters (`-o output.json`, `-o output.csv`) which are often simpler for basic file output and can handle JSON Lines format automatically. Custom pipelines like this offer more control.

### 4. Storing to SQLite Database (Example)
```python
# myproject/pipelines.py
import sqlite3

class SQLitePipeline:
    def __init__(self, sqlite_file, sqlite_table):
        self.sqlite_file = sqlite_file
        self.sqlite_table = sqlite_table
        self.conn = None
        self.cur = None

    @classmethod
    def from_crawler(cls, crawler):
        # Get database settings from Scrapy settings.py
        return cls(
            sqlite_file=crawler.settings.get('SQLITE_FILE', 'scraped_data.db'),
            sqlite_table=crawler.settings.get('SQLITE_TABLE', 'products')
        )

    def open_spider(self, spider):
        self.conn = sqlite3.connect(self.sqlite_file)
        self.cur = self.conn.cursor()
        # Create table if it doesn't exist (adapt columns to your Item)
        self.cur.execute(f"""
        CREATE TABLE IF NOT EXISTS {self.sqlite_table} (
            product_url TEXT PRIMARY KEY,
            product_name TEXT,
            price REAL,
            description TEXT,
            category TEXT
        )
        """)
        self.conn.commit()

    def close_spider(self, spider):
        if self.conn:
            self.conn.close()

    def process_item(self, item, spider):
        # Adapt SQL query and item fields to your specific Item structure
        try:
            self.cur.execute(f"""
                INSERT INTO {self.sqlite_table} (product_url, product_name, price, description, category)
                VALUES (?, ?, ?, ?, ?)
            """, (
                item.get('product_url'),
                item.get('product_name'),
                item.get('price'), # Assumes price is already float from a previous pipeline
                item.get('description'),
                item.get('category')
            ))
            self.conn.commit()
        except sqlite3.IntegrityError:
            spider.logger.warning(f"Duplicate URL found (SQLite constraint): {item.get('product_url')}")
        except Exception as e:
            spider.logger.error(f"Error inserting item into SQLite: {e} - Item: {item}")
            # Potentially raise DropItem or handle differently
        return item
```