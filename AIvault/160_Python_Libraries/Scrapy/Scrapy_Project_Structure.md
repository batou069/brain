---
tags:
  - python
  - scrapy
  - web_scraping
  - project_structure
  - organization
  - concept
aliases:
  - Scrapy Project Layout
  - Scrapy Directory Structure
related:
  - "[[160_Python_Libraries/Scrapy/_Scrapy_MOC|_Scrapy_MOC]]"
  - "[[Scrapy_Spiders]]"
  - "[[Scrapy_Items]]"
  - "[[Scrapy_Item_Pipelines]]"
  - "[[Scrapy_Settings]]"
  - "[[Scrapy_Middleware]]"
worksheet:
  - WS_WebScraping_1
date_created: 2025-06-11
---
# Scrapy: Project Structure

When you start a new Scrapy project using the command `scrapy startproject myprojectname`, Scrapy automatically generates a directory structure with several key files and folders. Understanding this structure is important for organizing your web scraping code.

## Typical Project Layout
After running `scrapy startproject ecommerce_scraper`, you would typically see a structure like this:

```
ecommerce_scraper/  <-- Outer directory (can be renamed)
├── scrapy.cfg      <-- Deploy configuration file
└── ecommerce_scraper/  <-- Inner Python package for your project (project module)
    ├── __init__.py
    ├── items.py    <-- Project items definition file
    ├── middlewares.py <-- Project middlewares file
    ├── pipelines.py   <-- Project pipelines file
    ├── settings.py    <-- Project settings file
    └── spiders/       <-- Directory for your spider modules
        ├── __init__.py
        └── # (e.g., product_spider.py, category_spider.py)
```

[list2tab|#Project Components]
- `scrapy.cfg`
    -   **Location:** Outer project directory.
    -   **Purpose:** This is the project configuration file. It mainly specifies settings for deploying your Scrapy project (e.g., using Scrapyd) and points to the project's settings module.
    -   You typically don't modify this file much for local development and running spiders from the command line.
    -   Example content:
        ```ini
        [settings]
        default = ecommerce_scraper.settings

        [deploy]
        #url = http://localhost:6800/
        project = ecommerce_scraper
        ```
- Inner Project Directory (e.g., `ecommerce_scraper/`)
    -   **Location:** Inside the outer project directory. This is the actual Python package for your Scrapy project.
    -   **Purpose:** Contains all the core code for your spiders, items, pipelines, etc. You'll do most of your work here.
    -   `__init__.py`: Makes this directory a Python package.
    -   **[[Scrapy_Items|`items.py`]]**:
        -   Defines the structure of the data you want to scrape using `scrapy.Item` classes. This acts as a schema for your scraped data.
    -   **[[Scrapy_Middleware|`middlewares.py`]]**:
        -   Defines custom spider middleware and downloader middleware. Middleware are hooks into Scrapy’s request/response processing for advanced customization.
    -   **[[Scrapy_Item_Pipelines|`pipelines.py`]]**:
        -   Defines item pipelines for processing scraped items (e.g., cleaning, validating, storing data in databases or files).
    -   **[[Scrapy_Settings|`settings.py`]]**:
        -   Contains project-specific settings that override Scrapy's default settings. You configure things like concurrency, user-agent, enabled pipelines, middleware, download delays, `robots.txt` obedience, etc., here.
    -   **`spiders/` directory**:
        -   This is where you place your spider modules (Python files containing your [[Scrapy_Spiders|spider classes]]). Each file can contain one or more spiders.
        -   `spiders/__init__.py`: Makes the `spiders` directory a Python package.

## How Scrapy Uses This Structure
-   When you run a Scrapy command like `scrapy crawl myspider` from the outer project directory, Scrapy uses `scrapy.cfg` to locate your project's settings and module.
-   It then loads the settings from `ecommerce_scraper/settings.py`.
-   It discovers spiders defined in Python files within the `ecommerce_scraper/spiders/` directory.
-   If items are yielded by spiders, they are instances of classes defined in `ecommerce_scraper/items.py`.
-   These items are then passed through the item pipelines enabled in `settings.py` and defined in `ecommerce_scraper/pipelines.py`.
-   Middleware defined in `middlewares.py` and enabled in `settings.py` can intercept and modify requests and responses.

## Best Practices
-   **Keep Spiders in `spiders/`:** This is the standard location and helps Scrapy discover them automatically.
-   **Define Data Structure in `items.py`:** Use `scrapy.Item` for clarity and consistency, especially for larger projects.
-   **Modularize Pipelines and Middleware:** Implement distinct processing steps in separate pipeline components or middleware classes.
-   **Configure via `settings.py`:** Avoid hardcoding settings directly in spiders or pipelines where possible. Use `settings.py` for project-wide configurations.
-   **Utilities:** You can create additional Python modules within your project's inner directory (e.g., `ecommerce_scraper/utils.py`) for helper functions or shared code.

Understanding and adhering to this project structure makes your Scrapy projects organized, maintainable, and aligned with the framework's conventions.

---