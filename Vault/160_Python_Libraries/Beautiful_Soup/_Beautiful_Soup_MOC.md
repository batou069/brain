---
tags:
  - python
  - library
  - beautifulsoup
  - bs4
  - web_scraping
  - html_parser
  - xml_parser
  - moc
  - concept
aliases:
  - Beautiful Soup MOC
  - BS4 MOC
related:
  - "[[_Python_Libraries_MOC]]"
  - "[[Requests_Library]]"
  - "[[HTML_Basics]]"
  - "[[CSS_Selectors]]"
  - "[[Scrapy_Framework]]"
worksheet:
  - WS_WebScraping_1
date_created: 2025-06-09
---
# Beautiful Soup MOC 🍲📄

**Beautiful Soup** is a Python library designed for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. It commonly saves programmers hours or days of work on web scraping tasks.

It does **not** fetch web pages itself; for that, it's typically used in conjunction with libraries like [[Requests_Library|Requests]] or `urllib`.

## Core Philosophy & Features
-   **Ease of Use:** Provides a simple, Pythonic interface for navigating and searching a parsed HTML/XML document.
-   **Parser Flexibility:** Works with different parsers, including Python's built-in `html.parser`, as well as faster and more robust parsers like `lxml` and `html5lib`.
    -   `lxml`: Very fast, lenient.
    -   `html5lib`: Extremely lenient, parses HTML like a web browser, creates valid HTML5. Slower.
    -   `html.parser`: Built-in, decent speed, reasonably lenient.
-   **Robustness:** Handles poorly-formed markup gracefully.
-   **Powerful Navigation & Searching:**
    -   Navigating the tree structure (parent, children, siblings, next/previous element).
    -   Searching by tag name, attributes, CSS classes, string content, regular expressions.
-   **Modification of Parse Tree:** Allows for modifying the HTML/XML structure (though less common for pure scraping).

## Key Concepts & Usage
-   [[BS4_Installation_Setup|Installation and Setup]]
-   [[BS4_Parsing_Documents|Parsing HTML/XML Documents]]
    -   Creating a `BeautifulSoup` object from a string or file handle.
-   [[BS4_Navigating_Tree|Navigating the Parse Tree]]
    -   Accessing tags by name (e.g., `soup.title`, `soup.p`).
    -   `.contents`, `.children`, `.descendants`.
    -   `.parent`, `.parents`.
    -   `.next_sibling`, `.previous_sibling`, `.next_element`, `.previous_element`.
-   [[BS4_Searching_Tree|Searching the Parse Tree]]
    -   `find(name, attrs, string, ...)`: Returns the first matching tag.
    -   `find_all(name, attrs, string, limit, ...)`: Returns a list of all matching tags.
    -   Searching by CSS selectors (`soup.select()`).
    -   Searching by string content or regular expressions.
-   [[BS4_Accessing_Attributes_Text|Accessing Tag Attributes and Text]]
    -   `tag['attribute_name']` (e.g., `link['href']`).
    -   `tag.get('attribute_name')`.
    -   `tag.string`, `tag.get_text()`, `tag.strings`, `tag.stripped_strings`.
-   [[BS4_Practical_Scraping_Examples|Practical Scraping Examples]]
    -   Extracting product information from e-commerce sites.
    -   Scraping article titles and content from news sites.

## Typical Workflow (with Requests)
1.  Fetch web page content using [[Requests_Library|`requests.get(url)`]].
2.  Parse the content using `BeautifulSoup(response.content, 'html.parser')` (or another parser).
3.  Navigate and search the `BeautifulSoup` object to find the desired data elements.
4.  Extract text, attributes, or other information.
5.  Store or process the extracted data.

## Notes in this Beautiful Soup Section
```dataview
LIST
FROM "160_Python_Libraries/Beautiful_Soup"
WHERE file.folder = this.file.folder AND file.name != this.file.name AND !contains(file.name, "MOC")
SORT file.name ASC
```

---