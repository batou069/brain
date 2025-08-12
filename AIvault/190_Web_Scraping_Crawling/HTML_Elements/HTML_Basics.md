---
tags:
  - html
  - web_development
  - structure
  - web_scraping
  - concept
aliases:
  - HTML Fundamentals
  - HyperText Markup Language Basics
related:
  - "[[190_Web_Scraping_Crawling/HTML_Elements/_HTML_Elements_MOC|_HTML_Elements_MOC]]"
  - "[[DOM_Document_Object_Model]]"
  - "[[HTML_Common_Tags]]"
  - "[[HTML_Common_Attributes]]"
worksheet:
  - WS_WebScraping_1
date_created: 2025-06-18
---
# HTML Basics for Web Scraping

**HTML (HyperText Markup Language)** is the standard markup language for creating web pages and web applications. Web browsers receive HTML documents from a web server or from local storage and render them into multimedia web pages. HTML describes the structure of a web page semantically and originally included cues for the appearance of the document.

For web scraping, understanding the basic structure and common elements of HTML is essential to locate and extract the desired data.

## Basic Document Structure
A typical HTML document has the following structure:

```html
<!DOCTYPE html> <!-- Document type declaration -->
<html> <!-- Root element -->
  <head>
    <!-- Meta-information about the HTML document (not displayed on the page itself) -->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Title</title> <!-- Appears in the browser tab or window title bar -->
    <link rel="stylesheet" href="style.css"> <!-- Link to external CSS file -->
    <script src="script.js"></script> <!-- Link to external JavaScript file -->
  </head>
  <body>
    <!-- The actual content of the page, visible to the user -->
    <header>
      <h1>Main Heading of the Page</h1>
      <nav>...</nav>
    </header>
    <main>
      <article>
        <p>This is a paragraph of text.</p>
        <a href="https://example.com">This is a link</a>
        <img src="image.jpg" alt="Description of image">
      </article>
    </main>
    <footer>
      <p>&copy; 2023 My Website</p>
    </footer>
  </body>
</html>
```

Key parts:
-   **`<!DOCTYPE html>`:** Declares the document type to be HTML5.
-   **`<html>`:** The root element that encloses all other content on the page.
-   **`<head>`:** Contains meta-information about the HTML document, such as the character set, viewport settings, page title, links to CSS stylesheets, and scripts. This content is not displayed directly on the rendered page (except for the `<title>`).
    -   **`<title>`:** Defines the title of the document, shown in the browser's title bar or tab. Often a good piece of data to scrape.
    -   **`<meta>`:** Provides metadata like character set, page description, keywords, author.
    -   **`<link>`:** Links to external resources, most commonly CSS files.
    -   **`<script>`:** Embeds or links to JavaScript code.
-   **`<body>`:** Contains the visible page content that is displayed in the browser window. This is where most of the data targeted by scrapers resides.

## Elements (Tags)
HTML documents are made up of **HTML elements**. Elements are usually defined by a **start tag** (e.g., `<p>`), some **content**, and an **end tag** (e.g., `</p>`).
-   Example: `<p>This is a paragraph.</p>`
-   Some elements are **empty elements** (or void elements) and do not have an end tag or content, e.g., `<img>`, `<br>`, `<hr>`, `<input>`. They are often written with a self-closing slash: `<img src="path.jpg" />`.

See [[HTML_Common_Tags|Common HTML Tags for Scraping]] for a list of tags frequently targeted.

## Attributes
HTML elements can have **attributes**, which provide additional information about an element or modify its behavior. Attributes are always specified in the start tag and usually come in name/value pairs like `name="value"`.
-   Example: `<a href="https://example.com" class="external-link">Visit Example</a>`
    -   `href` and `class` are attribute names.
    -   `"https://example.com"` and `"external-link"` are attribute values.

See [[HTML_Common_Attributes|Common HTML Attributes for Selection]] for attributes often used to locate elements.

## Nesting
HTML elements can be nested inside other elements, forming a hierarchical structure. This structure is represented by the [[DOM_Document_Object_Model|Document Object Model (DOM)]].
```html
<div> <!-- Parent -->
  <p> <!-- Child of div, parent of span -->
    This is <strong>important</strong> text. <!-- strong is child of p -->
  </p>
</div>
```

## Comments
HTML comments are ignored by the browser and are not displayed. They are written as:
`<!-- This is a comment -->`
Sometimes comments might contain useful metadata or hints, but usually, they are not a primary target for scraping data meant for users.

Understanding these basics allows a scraper to interpret the raw HTML fetched from a server and provides the foundation for using tools like [[160_Python_Libraries/Beautiful_Soup/_Beautiful_Soup_MOC|Beautiful Soup]] or [[160_Python_Libraries/Scrapy/_Scrapy_MOC|Scrapy selectors]] to navigate and extract specific pieces of information.

---