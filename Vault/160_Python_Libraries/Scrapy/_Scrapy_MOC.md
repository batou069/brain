---
tags:
  - python
  - framework
  - scrapy
  - web_scraping
  - web_crawling
  - moc
  - concept
aliases:
  - Scrapy Framework MOC
related:
  - "[[_Python_Libraries_MOC]]"
  - "[[Requests_Library]]"
  - "[[Beautiful_Soup_MOC|_Beautiful_Soup_MOC]]"
  - "[[XPath_Selectors]]"
  - "[[CSS_Selectors]]"
worksheet:
  - WS_WebScraping_1
date_created: 2025-06-09
---
# Scrapy Framework MOC 🕷️🕸️

**Scrapy** is an open-source and collaborative web crawling framework for Python. It is designed for extracting data from websites (web scraping) in a fast, simple, yet extensible way. Scrapy handles many common web crawling complexities like asynchronous requests, following links, managing sessions, and processing scraped data.

It's more than just a parser or an HTTP client; it's a complete framework for building and running web spiders (bots that crawl websites).

## Core Philosophy & Features
-   **Asynchronous Networking:** Built on Twisted, an event-driven networking engine, allowing for high concurrency and non-blocking I/O. This means Scrapy can handle many requests simultaneously without waiting for each one to complete.
-   **Spider-Based Architecture:** Users define "spiders," which are Python classes that specify how to crawl a website (starting URLs, how to follow links) and how to extract data from the pages.
-   **Selectors (XPath & CSS):** Built-in support for extracting data using XPath and CSS selectors, making it powerful for targeting specific HTML/XML elements. Can also integrate with libraries like [[Beautiful_Soup_MOC|_Beautiful_Soup_MOC]] for parsing if preferred.
-   **Item Pipelines:** Scraped data is typically processed through a series of "item pipelines" for cleaning, validation, storing in databases, or writing to files.
-   **Middleware:** Extensible middleware system for customizing request/response handling, cookie management, user-agent spoofing, proxy rotation, etc.
-   **Built-in Services:** Includes features like `robots.txt` respect, crawl depth limitation, link filtering, caching, and more.
-   **Extensibility:** Highly extensible through custom middleware, pipelines, and extensions.
-   **Portability:** Written in Python, runs on Linux, Windows, Mac OSX.

## Key Components of a Scrapy Project
-   [[Scrapy_Project_Structure|Project Structure]]
-   [[Scrapy_Spiders|Spiders]]
    -   Defining how to crawl and parse pages.
    -   `start_requests()` or `start_urls`.
    -   `parse()` method for processing responses.
    -   Yielding `Request` objects to follow links and `Item` objects (or dicts) for scraped data.
-   [[Scrapy_Items|Items]]
    -   Structured containers for scraped data (similar to dictionaries or custom objects).
-   [[Scrapy_Selectors|Selectors (XPath & CSS)]]
    -   Used within spiders to extract data from HTML/XML responses.
-   [[Scrapy_Item_Pipelines|Item Pipelines]]
    -   Processing scraped items (cleaning, validation, storage).
-   [[Scrapy_Settings|Settings (`settings.py`)]]
    -   Configuring spider behavior, middleware, pipelines, concurrency, etc.
-   [[Scrapy_Middleware|Middleware (Downloader & Spider Middleware)]]
    -   Hooks for modifying requests and responses.

## Typical Workflow
1.  **Create a Scrapy Project:** `scrapy startproject myproject`
2.  **Define Items:** In `items.py`, define the structure of the data you want to scrape.
3.  **Create a Spider:** In the `spiders/` directory, create a Python file for your spider class, inheriting from `scrapy.Spider`.
    -   Define `name`, `allowed_domains`, `start_urls`.
    -   Implement the `parse()` method to process responses, extract data using selectors, and yield items or new requests.
4.  **Configure Item Pipelines (Optional):** In `pipelines.py`, define classes to process and store items. Enable them in `settings.py`.
5.  **Configure Settings:** In `settings.py`, adjust settings like `ROBOTSTXT_OBEY`, `CONCURRENT_REQUESTS_PER_DOMAIN`, user-agent, etc.
6.  **Run the Spider:** From the project's root directory, `scrapy crawl myspidername`.

## Notes in this Scrapy Section
```dataview
LIST
FROM "160_Python_Libraries/Scrapy"
WHERE file.folder = this.file.folder AND file.name != this.file.name AND !contains(file.name, "MOC")
SORT file.name ASC
```

---