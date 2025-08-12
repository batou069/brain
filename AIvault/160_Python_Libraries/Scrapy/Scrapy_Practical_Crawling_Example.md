---
tags:
  - python
  - scrapy
  - web_scraping
  - web_crawling
  - spider
  - items
  - pipelines
  - example
  - practical_use_case
aliases:
  - Scrapy Crawling Example
  - E-commerce Scraping Scrapy
related:
  - "[[160_Python_Libraries/Scrapy/_Scrapy_MOC|_Scrapy_MOC]]"
  - "[[Scrapy_Project_Structure]]"
  - "[[Scrapy_Spiders]]"
  - "[[Scrapy_Items]]"
  - "[[Scrapy_Selectors]]"
  - "[[Scrapy_Item_Pipelines]]"
  - "[[Scrapy_Settings]]"
worksheet:
  - WS_WebScraping_1
date_created: 2025-06-11
---
# Scrapy: Practical Crawling Example (Conceptual E-commerce Site)

This note outlines a more complete, albeit conceptual, example of a Scrapy project designed to scrape product information from a mock e-commerce website. It will touch upon defining items, creating a spider to crawl category and product pages, extracting data, and a simple item pipeline.

**Target Scenario:** Scrape product name, price, description, and image URL from an e-commerce site that has category pages linking to individual product pages.

## 1. Project Setup
First, create a Scrapy project (if not already done):
```bash
scrapy startproject ecom_scraper
cd ecom_scraper
```

## 2. Define Items (`ecom_scraper/items.py`)
Define the structure for the product data we want to extract.

```python
# ecom_scraper/items.py
import scrapy

class ProductItem(scrapy.Item):
    product_name = scrapy.Field()
    price = scrapy.Field()
    description = scrapy.Field()
    image_url = scrapy.Field()
    product_url = scrapy.Field() # URL of the product page
    category = scrapy.Field()    # Category it belongs to
```

## 3. Create the Spider (`ecom_scraper/spiders/product_spider.py`)
This spider will start from a main category page, find links to individual product pages, follow them, and then scrape data from each product page.

```python
# ecom_scraper/spiders/product_spider.py
import scrapy
from ..items import ProductItem # Import ProductItem from items.py

class EcomProductSpider(scrapy.Spider):
    name = "ecom_products"
    allowed_domains = ["conceptual-ecommerce.com"] # Restrict to this domain
    
    # Start with a few category pages
    start_urls = [
        "http://conceptual-ecommerce.com/category/electronics",
        "http://conceptual-ecommerce.com/category/books",
    ]

    # Callback for processing category pages
    def parse_category(self, response):
        self.logger.info(f"Crawling category page: {response.url}")
        
        # Extract current category name (example: from a breadcrumb or title)
        # current_category = response.xpath('//h1[@class="category-title"]/text()').get()
        # For simplicity, let's derive from URL or pass via meta
        current_category = response.url.split("/")[-1] if response.url.split("/")[-1] else "Unknown"


        # Selector for links to individual product pages
        # This will depend heavily on the actual website structure
        # product_links = response.css('div.product-listing-item a.product-page-link::attr(href)').getall()
        
        # Conceptual: Assume product links are found
        # In a real scenario, replace these with actual selectors
        if "electronics" in response.url:
            product_links = ["/product/item101", "/product/item102"]
        elif "books" in response.url:
            product_links = ["/product/book201", "/product/book202"]
        else:
            product_links = []

        for product_link_relative in product_links:
            product_url_absolute = response.urljoin(product_link_relative)
            # Yield a request to follow the product link, passing category via meta
            yield scrapy.Request(
                url=product_url_absolute,
                callback=self.parse_product_page,
                meta={'category': current_category} # Pass category to next callback
            )

        # Conceptual: Follow pagination links on category page (if any)
        # next_page_selector = 'a.pagination-next::attr(href)'
        # next_page_relative = response.css(next_page_selector).get()
        # if next_page_relative:
        #     next_page_absolute = response.urljoin(next_page_relative)
        #     yield scrapy.Request(url=next_page_absolute, callback=self.parse_category)

    # Callback for processing individual product pages
    def parse_product_page(self, response):
        self.logger.info(f"Scraping product page: {response.url}")
        
        # Retrieve category from meta
        category = response.meta.get('category', 'N/A')

        # Create an Item instance
        product = ProductItem()
        product['product_url'] = response.url
        product['category'] = category
        
        # Extract data using selectors (these are placeholders)
        # Replace with actual selectors for the target website
        # product['product_name'] = response.xpath('//h1[@itemprop="name"]/text()').get()
        # product['price'] = response.xpath('//span[@itemprop="price"]/text()').get()
        # description_lines = response.css('div.product-description ::text').getall()
        # product['description'] = " ".join([line.strip() for line in description_lines if line.strip()])
        # product['image_url'] = response.urljoin(response.css('img.main-product-image::attr(src)').get())

        # Conceptual data extraction for this example
        product['product_name'] = response.css('title::text').get().split('-').strip() if response.css('title::text').get() else "Sample " + category + " Product"
        product['price'] = f"${np.random.randint(10,500)}.99" # Random price
        product['description'] = f"A high-quality {product['product_name']} from the {category} section."
        product['image_url'] = response.urljoin(f"/images/{response.url.split('/')[-1]}.jpg")
        
        yield product

    # Default parse method if start_urls don't have specific callbacks
    # For this spider, we want parse_category to handle start_urls
    def parse(self, response):
        # Delegate to parse_category for start_urls
        return self.parse_category(response)

# For the conceptual part to run without actual web requests,
# you would need a mock server or local HTML files.
# For this example, we assume the selectors will find something if the HTML structure matches.
import numpy as np # For random price generation in conceptual example
```

## 4. Define an Item Pipeline (`ecom_scraper/pipelines.py`)
A simple pipeline to clean data and print it (or save to JSON).

```python
# ecom_scraper/pipelines.py
import json
from itemadapter import ItemAdapter # For working with Items or dicts

class PriceCleanerPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter.get('price'):
            price_str = str(adapter['price']).replace('$', '').replace(',', '').strip()
            try:
                adapter['price'] = float(price_str)
            except ValueError:
                spider.logger.warning(f"Could not convert price to float: {adapter['price']} for {adapter.get('product_url')}")
                # adapter['price'] = None # Or handle as invalid
        return item

class SimpleJsonWriterPipeline:
    def open_spider(self, spider):
        self.file = open(f'{spider.name}_output.jl', 'w') # JSON Lines format

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(ItemAdapter(item).asdict()) + "\n"
        self.file.write(line)
        spider.logger.info(f"Saved item: {item.get('product_name')}")
        return item
```

## 5. Configure Settings (`ecom_scraper/settings.py`)
Enable the pipelines and set a polite User-Agent and download delay.

```python
# ecom_scraper/settings.py

BOT_NAME = 'ecom_scraper'

SPIDER_MODULES = ['ecom_scraper.spiders']
NEWSPIDER_MODULE = 'ecom_scraper.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure a delay for requests for the same website (default: 0)
DOWNLOAD_DELAY = 1 # 1 second delay
# CONCURRENT_REQUESTS_PER_DOMAIN = 8

USER_AGENT = 'ECommerceProductScraper/1.0 (+http://www.example.com/botinfo)'

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'ecom_scraper.pipelines.PriceCleanerPipeline': 300,
   'ecom_scraper.pipelines.SimpleJsonWriterPipeline': 800,
}

# Optional: Configure HTTP Caching for development
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0 # Cache forever during dev
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
```

## 6. Running the Spider
Navigate to the outer `ecom_scraper` directory in your terminal:
```bash
scrapy crawl ecom_products
```
This command will:
1.  Look for a spider named "ecom_products".
2.  Start making requests from `start_urls`.
3.  Call `parse_category` for category page responses.
4.  Yield `Request` objects for product pages, which will then be processed by `parse_product_page`.
5.  Yield `ProductItem` objects from `parse_product_page`.
6.  Pass these items through the `PriceCleanerPipeline` and then `SimpleJsonWriterPipeline`.
7.  A file named `ecom_products_output.jl` will be created containing the scraped data in JSON Lines format.

**Important Notes for Real-World Scenario:**
-   **Website Structure:** The CSS/XPath selectors (`response.css(...)`, `response.xpath(...)`) are highly dependent on the target website's HTML structure and will need to be carefully identified using browser developer tools. The selectors in this example are placeholders.
-   **Politeness:** Always respect `robots.txt` (`ROBOTSTXT_OBEY = True`). Set appropriate `DOWNLOAD_DELAY` and `CONCURRENT_REQUESTS_PER_DOMAIN` to avoid overloading the server. Identify your bot with a clear `USER_AGENT`.
-   **Error Handling:** Real spiders need robust error handling (e.g., for missing elements, network issues, changes in website structure).
-   **Dynamic Content:** If the website loads data using JavaScript, Scrapy alone might not be enough. You might need to use tools like Selenium, Playwright, or Scrapy Splash to render JavaScript.
-   **Legality and Ethics:** Always ensure you have permission to scrape a website and comply with its terms of service.

This example provides a foundational structure for a multi-page scraping project using Scrapy.

---