---
tags:
  - html
  - web_development
  - web_scraping
  - html_tags
  - elements
  - concept
aliases:
  - Common HTML Tags
  - HTML Tags for Scraping
related:
  - "[[190_Web_Scraping_Crawling/HTML_Elements/_HTML_Elements_MOC|_HTML_Elements_MOC]]"
  - "[[HTML_Basics]]"
  - "[[HTML_Common_Attributes]]"
worksheet:
  - WS_WebScraping_1
date_created: 2025-06-18
---
# Common HTML Tags Relevant for Web Scraping

When scraping web pages, certain HTML tags are more frequently targeted because they typically contain the data of interest or help structure the content in a way that aids navigation. Here's a list of common tags and why they are relevant:

[list2tab|#Common HTML Tags]
- Structure & Layout
    - **`<div>` (Division)**
        -   **Purpose:** A generic container for flow content. It has no effect on the content or layout until styled using CSS. Extensively used for grouping content sections, creating layouts (e.g., headers, footers, sidebars, main content areas, product cards).
        -   **Scraping Relevance:** Often targeted using its `class` or `id` attributes to isolate specific sections of a page (e.g., `<div class="product-details">`, `<div id="main-article">`).
    - **`<span>`**
        -   **Purpose:** A generic inline container for phrasing content, used to group inline-elements for styling or scripting.
        -   **Scraping Relevance:** Often used to wrap small pieces of text that need specific styling or identification, like prices (`<span class="price">$29.99</span>`), labels, or icons. Can be targeted by class/id or its position within a larger element.
    - **`<main>`**
        -   **Purpose:** Specifies the main content of a document. The content inside `<main>` should be unique to the document, excluding sidebars, navigation links, copyright information, site logos, and search forms (unless the search form is the main function of the page).
        -   **Scraping Relevance:** A good starting point to narrow down the search for the primary content of a page.
    - **`<nav>` (Navigation)**
        -   **Purpose:** Represents a section of a page whose purpose is to provide navigation links, either within the current document or to other documents.
        -   **Scraping Relevance:** Useful for finding main site navigation menus, often to [[Crawling|crawl]] to other relevant pages.
    - **`<header>`, `<footer>`, `<article>`, `<section>`, `<aside>` (Semantic Tags)**
        -   **Purpose:** Provide semantic meaning to different parts of a web page.
        -   **Scraping Relevance:** Can be useful for identifying specific content blocks if the website uses semantic HTML properly. For example, `<article>` often encloses a blog post or news item.
- Headings & Text
    - **`<h1>` to `<h6>` (Headings)**
        -   **Purpose:** Define HTML headings, with `<h1>` being the most important (main title) and `<h6>` the least.
        -   **Scraping Relevance:** Frequently contain titles of articles, products, sections, or other key textual information.
    - **`<p>` (Paragraph)**
        -   **Purpose:** Defines a paragraph of text.
        -   **Scraping Relevance:** The primary container for textual content like descriptions, articles, comments, reviews.
    - **`<a>` (Anchor/Hyperlink)**
        -   **Purpose:** Creates hyperlinks to other web pages, files, locations within the same page, or email addresses.
        -   **Scraping Relevance:** Crucial for [[Crawling|crawling]] (extracting URLs from the `href` attribute to visit other pages) and for extracting link text.
    - **`<span>` (already mentioned)**
        -   Often contains specific pieces of data within larger text blocks, like prices, dates, or labels.
- Lists
    - **`<ul>` (Unordered List)**
        -   **Purpose:** Defines an unordered (bulleted) list.
    - **`<ol>` (Ordered List)**
        -   **Purpose:** Defines an ordered (numbered/lettered) list.
    - **`<li>` (List Item)**
        -   **Purpose:** Defines an item within a `<ul>` or `<ol>`.
        -   **Scraping Relevance:** Lists are commonly used for product features, navigation menus, comment threads, search results. Scrapers often iterate through `<li>` elements within a list to extract individual items.
    - **`<dl>`, `<dt>`, `<dd>` (Description List)**
        -   **Purpose:** Used for creating lists of terms and their descriptions (like a dictionary or metadata). `<dt>` is the term, `<dd>` is the description.
        -   **Scraping Relevance:** Often used for product specifications, key-value pairs of information.
- Tables
    - **`<table>`**
        -   **Purpose:** Defines an HTML table.
    - **`<thead>`, `<tbody>`, `<tfoot>`**
        -   **Purpose:** Group header, body, and footer content within a table.
    - **`<tr>` (Table Row)**
        -   **Purpose:** Defines a row in a table.
    - **`<th>` (Table Header Cell)**
        -   **Purpose:** Defines a header cell in a table. Often contains column titles.
    - **`<td>` (Table Data Cell)**
        -   **Purpose:** Defines a standard data cell in a table.
        -   **Scraping Relevance:** Tables are a common way to present structured data (e.g., product comparisons, financial data, schedules). Scrapers iterate through rows and cells to extract tabular information.
- Media & Forms
    - **`<img>` (Image)**
        -   **Purpose:** Embeds an image in an HTML page.
        -   **Scraping Relevance:** Extracting image URLs (from the `src` attribute) or alternative text (`alt` attribute).
    - **`<form>`**
        -   **Purpose:** Defines an HTML form for user input.
        -   **Scraping Relevance:** Understanding form structure can be necessary if you need to simulate form submissions to access data or trigger actions (often requires tools like Selenium or direct POST requests).
    - **`<input>`**
        -   **Purpose:** Defines an input field where the user can enter data. Types include `text`, `password`, `checkbox`, `radio`, `submit`, `hidden`, etc.
        -   **Scraping Relevance:** Identifying input fields for form submission, or sometimes extracting default values or hidden data.
    - **`<button>`**
        -   **Purpose:** Defines a clickable button.
        -   **Scraping Relevance:** Identifying buttons that might trigger JavaScript events to load more content or submit forms.
    - **`<textarea>`**
        -   **Purpose:** Defines a multi-line text input control.
    - **`<select>` and `<option>`**
        -   **Purpose:** Creates a drop-down list. `<select>` is the container, `<option>` are the items.
        -   **Scraping Relevance:** Extracting available options or selecting options to trigger dynamic content changes.
- Meta & Scripting
    - **`<head>` (already mentioned)**
        -   Contains `<title>`, `<meta>` tags (which might have descriptions or keywords useful for scraping context).
    - **`<script>`**
        -   **Purpose:** Embeds or refers to executable JavaScript code.
        -   **Scraping Relevance:** JavaScript within `<script>` tags can sometimes contain data directly (e.g., as JSON within the script) or provide clues about how data is fetched via APIs. This is more advanced scraping.
    - **`<meta>`**
        -   **Purpose:** Provides metadata about the HTML document.
        -   **Scraping Relevance:** Can contain useful information like page description (`<meta name="description" content="...">`), keywords, character set, or Open Graph data (e.g., `og:title`, `og:image`).

Understanding these common tags and their typical uses helps in forming effective [[CSS_Selectors|CSS selectors]] or [[XPath_Selectors|XPath expressions]] to target the desired data during web scraping.

---