---
tags:
  - python
  - scrapy
  - web_scraping
  - web_crawling
  - spider
  - concept
  - example
aliases:
  - Scrapy Spider
  - Creating Scrapy Spiders
related:
  - "[[160_Python_Libraries/Scrapy/_Scrapy_MOC|_Scrapy_MOC]]"
  - "[[Scrapy_Items]]"
  - "[[Scrapy_Selectors]]"
  - "[[Requests_Library]]"
worksheet:
  - WS_WebScraping_1
date_created: 2025-06-09
---
# Scrapy: Spiders

**Spiders** are the core of Scrapy. They are Python classes that you define to crawl websites and extract structured data (items) from their pages. Each spider is responsible for:
1.  Defining the initial requests to make.
2.  Optionally, how to follow links on pages.
3.  How to parse the content of downloaded pages to extract data.

## Basic Structure of a Spider
A Scrapy spider is a class that inherits from `scrapy.Spider`.

```python
import scrapy
# from ..items import MyProjectItem # Assuming items are defined in items.py

class ProductSpider(scrapy.Spider):
    # 1. Identity
    name = "product_scraper"  # Unique name for the spider
    
    # Optional: Restrict crawling to specific domains
    # allowed_domains = ["example-ecommerce.com"] 

    # 2. Initial Requests
    # Option A: List of URLs to start crawling from
    start_urls = [
        "http://example-ecommerce.com/category/electronics",
        "http://example-ecommerce.com/category/books"
    ]

    # Option B: Override start_requests() for more complex initial requests
    # def start_requests(self):
    #     urls = [
    #         "http://example-ecommerce.com/category/electronics",
    #         "http://example-ecommerce.com/category/books"
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse_category)

    # 3. Parsing Responses (Main callback)
    # Default callback for requests made from start_urls or start_requests (if no callback specified)
    def parse(self, response):
        # 'response' is a scrapy.http.Response object containing the page content

        # Example: Extract product links from a category page
        # product_links = response.css('div.product-item a.product-link::attr(href)').getall()
        # for link in product_links:
        #     # Ensure the link is absolute
        #     product_page_url = response.urljoin(link)
        #     # Follow the link to the product page, and use parse_product as callback
        #     yield scrapy.Request(product_page_url, callback=self.parse_product)

        # Example: Pagination - find the "next page" link
        # next_page_path = response.css('a.next-page::attr(href)').get()
        # if next_page_path:
        #     next_page_url = response.urljoin(next_page_path)
        #     yield scrapy.Request(next_page_url, callback=self.parse) # Recursive call to parse for next category page

        # Placeholder for conceptual example
        self.logger.info(f"Parsing category page: {response.url}")
        # Simulate finding product links and yielding requests
        # For a real site, replace with actual CSS/XPath selectors
        if "electronics" in response.url:
            product_links_on_page = ["/product/tv123", "/product/phone456"]
            for plink in product_links_on_page:
                yield response.follow(plink, callback=self.parse_product)
        
        next_page_example = response.meta.get('next_page_num', 1)
        if next_page_example < 3 and "electronics" in response.url: # Simulate 2 pages for electronics
             yield response.follow(f"/category/electronics?page={next_page_example + 1}", 
                                   callback=self.parse, 
                                   meta={'next_page_num': next_page_example + 1})


    # 4. Callback for Parsing Individual Product Pages
    def parse_product(self, response):
        self.logger.info(f"Parsing product page: {response.url}")

        # Extract data using Scrapy Selectors (XPath or CSS)
        # product_name = response.css('h1#product-name::text').get()
        # price_str = response.xpath('//span[@class="price-amount"]/text()').get()
        # description = response.css('div.product-description p::text').getall()
        # description_joined = "".join(description).strip()

        # Conceptual data extraction
        product_name = "Sample Product " + response.url.split("/")[-1]
        price_str = "$19.99"
        description_joined = "A fantastic sample product."

        # Clean data (e.g., convert price string to float)
        # price_float = None
        # if price_str:
        #     price_float = float(price_str.replace('$', '').replace(',', ''))
        
        # Yield the scraped data as a dictionary or a Scrapy Item
        # Using a dictionary here for simplicity
        scraped_item = {
            'url': response.url,
            'name': product_name,
            'price': price_str, # or price_float
            'description': description_joined
        }
        yield scraped_item
        
        # If there are reviews to scrape on this page, you might yield another request
        # review_section_url = response.urljoin(response.css('a#reviews-link::attr(href)').get())
        # if review_section_url:
        #     yield scrapy.Request(review_section_url, callback=self.parse_reviews, meta={'product_name': product_name})

    # def parse_reviews(self, response):
    #     product_name = response.meta['product_name']
    #     # Logic to extract reviews for 'product_name'
    #     pass
```

## Key Components of a Spider Class
-   **`name`**: A string that uniquely identifies the spider. Used when running the spider (e.g., `scrapy crawl product_scraper`).
-   **`allowed_domains` (Optional)**: A list of strings containing domains that this spider is allowed to crawl. Requests for URLs not belonging to these domains will not be followed.
-   **`start_urls` (Attribute)**: A list of URLs where the spider will begin to crawl from. The first pages downloaded will be those listed here. The `parse` method will be called to handle the response for these URLs by default.
-   **`start_requests()` (Method)**: An alternative to `start_urls`. This method can be overridden to generate the initial `scrapy.Request` objects, allowing for more complex starting logic (e.g., reading URLs from a file, making POST requests). It must return an iterable of `Request` objects.
-   **`parse(self, response)` (Method)**: This is the default callback method called by Scrapy to process responses downloaded for the requests generated from `start_urls` or `start_requests` (if no specific callback is assigned to the request).
    -   The `response` argument is an instance of `scrapy.http.Response` and contains the page content and other metadata.
    -   This method is responsible for:
        -   Extracting scraped data (as dictionaries or [[Scrapy_Items|Scrapy Items]]).
        -   Identifying new URLs to follow and creating new `scrapy.Request` objects for them.
    -   It must return an iterable of `Request` objects, dictionaries, or `Item` objects.
-   **Custom Callback Methods (e.g., `parse_product`, `parse_category`):**
    -   You can define other methods to handle responses for specific types of pages.
    -   When creating a `scrapy.Request`, you can specify which method should be called to process its response using the `callback` argument: `yield scrapy.Request(url, callback=self.my_custom_parser)`.
-   **`response.follow(url, callback, ...)` or `response.urljoin(url_fragment)`:**
    -   Convenience methods for creating new `Request` objects from relative URLs found on the page.

## Yielding Data and Requests
Spiders yield two main types of objects from their callback methods:
1.  **Dictionaries or `scrapy.Item` objects:** These represent the structured data extracted from a page. These items are then typically processed by [[Scrapy_Item_Pipelines|Item Pipelines]].
2.  **`scrapy.Request` objects:** These represent new URLs to be downloaded and processed. They can specify a callback method for their response.

By yielding requests, spiders can recursively crawl through a website.

## Running a Spider
From the root directory of your Scrapy project:
```bash
scrapy crawl <spider_name>
# Example: scrapy crawl product_scraper -o products.json
```
This command will execute the spider named `product_scraper` and, with the `-o products.json` flag, save the scraped items to a JSON file.

Spiders are the heart of any Scrapy project, defining the logic for navigating websites and extracting the desired information.

---