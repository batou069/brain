---
tags:
  - web_scraping
  - html
  - parsing
  - beautifulsoup
  - lxml
  - html_parser
  - concept
aliases:
  - Parsing HTML
  - HTML Document Parsing
related:
  - "[[_Web_Scraping_Crawling_MOC]]"
  - "[[HTML_Basics]]"
  - "[[DOM_Document_Object_Model]]"
  - "[[160_Python_Libraries/Beautiful_Soup/_Beautiful_Soup_MOC|Beautiful Soup]]"
  - "[[160_Python_Libraries/Scrapy/_Scrapy_MOC|Scrapy Selectors]]"
worksheet:
  - WS_WebScraping_1
date_created: 2025-06-18
---
# HTML Parsing

## Definition
**HTML Parsing** is the process of taking raw HTML (HyperText Markup Language) code as input and transforming it into a structured representation, typically a tree-like structure such as the [[DOM_Document_Object_Model|Document Object Model (DOM)]]. This structured representation allows programs to easily navigate, search, and manipulate the content and structure of the HTML document.

HTML parsing is a fundamental step in web scraping, web browsing (how browsers render pages), and any application that needs to understand or extract information from web pages.

## The Need for Parsing
Raw HTML is just a string of text. While humans can read it, computers need a structured way to access specific parts of it (e.g., "find all links," "get the text of the main heading," "extract product prices"). Parsing provides this structure.

**Challenges in HTML Parsing:**
-   **Malformed HTML ("Tag Soup"):** Real-world HTML is often not perfectly well-formed or valid according to strict standards. Parsers need to be lenient and capable of handling common errors, missing tags, or improperly nested elements, much like web browsers do.
-   **Complexity:** HTML documents can be large and have deeply nested structures.
-   **Dynamic Content:** Some content might be loaded or modified by [[JavaScript_Basics_for_Scraping|JavaScript]] after the initial HTML is parsed (see [[Static_vs_Dynamic_Web_Pages]]). Basic HTML parsers typically only see the initial HTML source.

## How HTML Parsers Work (General Idea)
1.  **Tokenization (Lexical Analysis):** The parser reads the HTML string character by character and breaks it down into a sequence of "tokens." Tokens represent basic units like start tags (`<p>`), end tags (`</p>`), attributes (`class="foo"`), text content, comments, etc.
2.  **Tree Construction (Syntactic Analysis):** The tokenizer feeds these tokens to a tree builder, which constructs the parse tree (e.g., DOM tree) according to HTML grammar rules. It handles tag nesting, resolves errors (e.g., by implicitly adding missing tags or correcting mis-nesting), and builds the hierarchical structure.

## Common Python Libraries for HTML Parsing

[list2tab|#Python HTML Parsers]
- [[160_Python_Libraries/Beautiful_Soup/_Beautiful_Soup_MOC|Beautiful Soup (bs4)]]
    -   **Role:** Not a parser itself, but a library that sits on top of different underlying parsers and provides a convenient, Pythonic API for navigating and searching the parse tree.
    -   **Supported Parsers:**
        -   **`html.parser`:** Python's built-in HTML parser. Good default, no external dependencies. Reasonably fast and lenient.
        -   **`lxml`:** A very fast and robust C-based parser for both HTML and XML. Often the preferred choice for speed and handling messy HTML. Requires `lxml` to be installed.
        -   **`html5lib`:** Parses HTML in the same way a web browser does, meaning it's extremely lenient and aims to produce a perfectly valid HTML5 DOM tree. It's slower than `lxml` but very good for extremely broken HTML. Requires `html5lib` to be installed.
    -   **Example (with Beautiful Soup):**
        ```python
        from bs4 import BeautifulSoup
        html_doc = "<html><head><title>Test Page</title></head><body><p class='info'>Hello!</p></body></html>"
        
        # Using html.parser
        soup_std = BeautifulSoup(html_doc, 'html.parser')
        print("Title (html.parser):", soup_std.title.string)

        # Using lxml (if installed)
        try:
            soup_lxml = BeautifulSoup(html_doc, 'lxml')
            print("Paragraph text (lxml):", soup_lxml.find('p', class_='info').string)
        except ImportError:
            print("lxml not installed.")
        ```
- `lxml`
    -   **Role:** A powerful and fast library for processing XML and HTML in Python. Can be used directly for parsing and then navigating/querying using XPath or CSS selectors (via its `cssselect` integration).
    -   **Example (direct lxml parsing):**
        ```python
        from lxml import html # For HTML parsing
        from lxml import etree # For XML parsing

        html_doc = "<html><body><h1>Title</h1><p>Content</p></body></html>"
        tree = html.fromstring(html_doc) # Parse the HTML string

        # Using XPath to find elements
        title_elements = tree.xpath('//h1/text()')
        if title_elements:
            print("Title (lxml XPath):", title_elements)
        
        paragraph_elements = tree.cssselect('p') # Using CSS selectors
        if paragraph_elements:
            print("Paragraph text (lxml CSS):", paragraph_elements.text_content())
        ```
- `html.parser` (Python's built-in)
    -   **Role:** Provides basic HTML parsing capabilities as part of Python's standard library. It's what `BeautifulSoup` uses if you specify `'html.parser'`. Can be used directly, but its API is lower-level and less convenient for scraping than Beautiful Soup's.

## Role in Web Scraping
1.  **Fetch HTML:** First, a tool like [[160_Python_Libraries/Requests_Library|Requests]] (for static pages) or a browser automation tool like Selenium/Playwright (for dynamic pages) fetches the raw HTML content of a web page.
2.  **Parse HTML:** The fetched HTML string is then passed to an HTML parser (e.g., via Beautiful Soup or Scrapy's internal selectors which use `parsel`).
3.  **Create Parse Tree:** The parser constructs a tree representation (DOM-like structure).
4.  **Extract Data:** The scraper then uses methods provided by the parsing library (e.g., `find_all()`, `select()`, XPath queries) to navigate this tree and extract the desired information (text, links, image URLs, etc.). See [[Data_Extraction_Web]].

Effective HTML parsing is the foundation upon which successful web scraping is built, allowing structured access to unstructured web content.

---