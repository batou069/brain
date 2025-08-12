---
tags:
  - python
  - scrapy
  - web_scraping
  - configuration
  - settings
  - concept
aliases:
  - Scrapy Configuration
  - settings.py Scrapy
related:
  - "[[160_Python_Libraries/Scrapy/_Scrapy_MOC|_Scrapy_MOC]]"
  - "[[Scrapy_Project_Structure]]"
  - "[[Scrapy_Item_Pipelines]]"
  - "[[Scrapy_Middleware]]"
worksheet:
  - WS_WebScraping_1
date_created: 2025-06-11
---
# Scrapy: Settings (`settings.py`)

The `settings.py` file in a Scrapy project is crucial for configuring the behavior of your web crawlers (spiders) and other Scrapy components. When Scrapy runs, it first loads default settings, then overrides them with the settings defined in your project's `settings.py` file.

This file allows you to customize various aspects of the crawling process without modifying the core Scrapy framework or your spider code directly.

## Location
The `settings.py` file is located within your project's inner Python package directory (e.g., `myproject/myproject/settings.py`).

## Common Settings to Configure

[list2tab|#Scrapy Settings]
- Basic Spider Configuration
    -   **`BOT_NAME`**: (String) The name of the bot implemented by this Scrapy project (also known as the project name). Default: `'myproject'`.
    -   **`SPIDER_MODULES`**: (List of strings) A list of modules where Scrapy will look for spiders. Default: `['myproject.spiders']`.
    -   **`NEWSPIDER_MODULE`**: (String) Module where new spiders are created using `scrapy genspider`. Default: `'myproject.spiders'`.
- Crawl Behavior & Politeness
    -   **`ROBOTSTXT_OBEY`**: (Boolean) If `True` (default), Scrapy will respect `robots.txt` rules of websites. It's good practice to keep this `True`.
    -   **`USER_AGENT`**: (String) The default User-Agent string to use for requests, unless overridden per spider or request. Default is `Scrapy/VERSION (+http://scrapy.org)`. It's often recommended to set this to a common browser user-agent or a custom one identifying your bot respectfully.
        ```python
        # USER_AGENT = 'MyECommerceScraper (+http://www.mywebsite.com/botinfo)'
        ```
    -   **`CONCURRENT_REQUESTS`**: (Integer) The maximum number of concurrent (i.e. simultaneous) requests that will be performed by the Scrapy downloader. Default: 16.
    -   **`DOWNLOAD_DELAY`**: (Float) The amount of time (in seconds) that the downloader should wait before downloading consecutive pages from the same website. Helps to avoid overloading servers. Default: 0.
        ```python
        # DOWNLOAD_DELAY = 1 # Wait 1 second between requests to the same domain
        ```
    -   **`CONCURRENT_REQUESTS_PER_DOMAIN`**: (Integer) Maximum number of concurrent requests that will be performed to any single domain. Default: 8.
    -   **`CONCURRENT_REQUESTS_PER_IP`**: (Integer) Maximum number of concurrent requests that will be performed to any single IP. If non-zero, `CONCURRENT_REQUESTS_PER_DOMAIN` is ignored. Default: 0.
    -   **`AUTOTHROTTLE_ENABLED`**: (Boolean) Enables the AutoThrottle extension, which dynamically adjusts download delays based on server load. Default: `False`.
    -   **`AUTOTHROTTLE_START_DELAY`**: (Float) Initial download delay for AutoThrottle. Default: 5.0.
    -   **`AUTOTHROTTLE_MAX_DELAY`**: (Float) Maximum download delay for AutoThrottle. Default: 60.0.
    -   **`AUTOTHROTTLE_TARGET_CONCURRENCY`**: (Float) Average number of parallel requests Scrapy should try to maintain to each remote server. Default: 1.0.
- Item Pipelines (`ITEM_PIPELINES`)
    -   A dictionary specifying the [[Scrapy_Item_Pipelines|item pipelines]] to use and their order of execution (lower integer means earlier execution).
    -   Keys are pipeline class paths, values are integers from 0 to 1000.
        ```python
        # ITEM_PIPELINES = {
        #    'myproject.pipelines.PriceCleanerPipeline': 300,
        #    'myproject.pipelines.DatabaseStoragePipeline': 800,
        # }
        ```
- Middleware (`DOWNLOADER_MIDDLEWARES`, `SPIDER_MIDDLEWARES`)
    -   Dictionaries to enable and order [[Scrapy_Middleware|downloader and spider middleware]].
    -   Keys are middleware class paths, values are integers for order.
        ```python
        # DOWNLOADER_MIDDLEWARES = {
        #    'myproject.middlewares.CustomUserAgentMiddleware': 543,
        #    # 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 750, # Example
        # }
        ```
- Extensions (`EXTENSIONS`)
    -   A dictionary to enable and order Scrapy extensions.
- Request Headers (`DEFAULT_REQUEST_HEADERS`)
    -   A dictionary containing default headers to be sent with each request.
        ```python
        # DEFAULT_REQUEST_HEADERS = {
        #   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        #   'Accept-Language': 'en-US,en;q=0.5',
        # }
        ```
- Cookies (`COOKIES_ENABLED`, `COOKIES_DEBUG`)
    -   `COOKIES_ENABLED`: (Boolean) Whether cookies are enabled. Default: `True`.
    -   `COOKIES_DEBUG`: (Boolean) Log cookies sent in requests and received in responses. Default: `False`.
- Feed Exports (for `-o` command line option)
    -   **`FEEDS`**: A dictionary to configure feed exports (e.g., output format, path, encoding) if you want more control than the command line provides or want to export multiple feeds.
    -   **`FEED_EXPORT_ENCODING`**: Default encoding for feeds. Default: `'utf-8'`.
    -   **`FEED_EXPORT_FIELDS`**: A list of fields to include in the export, and their order.
- Logging (`LOG_LEVEL`, `LOG_FILE`)
    -   `LOG_LEVEL`: Minimum level of messages to log (e.g., 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'). Default: 'DEBUG'.
    -   `LOG_FILE`: Path to a file where logs will be written. If None, logs go to standard error.
- Caching (`HTTPCACHE_ENABLED`, etc.)
    -   Scrapy has a built-in HTTP caching middleware that can be enabled to speed up development by caching responses.
    -   `HTTPCACHE_ENABLED = True`
    -   `HTTPCACHE_EXPIRATION_SECS = 0` (0 means cache forever, good for dev)
    -   `HTTPCACHE_DIR = 'httpcache'`
    -   `HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'`

## Overriding Settings
-   **Project Settings (`settings.py`):** The primary place.
-   **Command-Line Options:** Many settings can be overridden using `scrapy crawl myspider -s SETTING_NAME=value`.
-   **Spider-Specific Settings (`custom_settings` attribute):** A spider class can define a `custom_settings` dictionary to override project or default settings specifically for that spider.
    ```python
    # In your spider class:
    # class MySpecialSpider(scrapy.Spider):
    #     name = "special_spider"
    #     custom_settings = {
    #         'DOWNLOAD_DELAY': 0.25,
    #         'USER_AGENT': 'SpecialBot/1.0'
    #     }
    #     # ... rest of spider ...
    ```

Properly configuring `settings.py` is essential for controlling the behavior, politeness, and data processing workflow of your Scrapy spiders. It's recommended to review the default Scrapy settings and adjust them according to the needs of your project and the websites you are crawling.

---