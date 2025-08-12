---
tags:
  - html
  - web_development
  - web_scraping
  - tags
  - attributes
  - moc
  - concept
aliases:
  - HTML Elements MOC
  - HTML Tags and Attributes
related:
  - "[[_Web_Scraping_Crawling_MOC]]"
  - "[[HTML_Basics]]"
  - "[[DOM_Document_Object_Model]]"
  - "[[CSS_Selectors]]"
  - "[[XPath_Selectors]]"
worksheet:
  - WS_WebScraping_1
date_created: 2025-06-18
---
# HTML Elements MOC: Tags & Attributes for Scraping

Understanding common **HTML (HyperText Markup Language)** elements (tags) and their attributes is fundamental for effective web scraping. Scrapers target these elements to extract specific pieces of data.

This section provides an overview of frequently encountered HTML tags and attributes that are often key targets or aids in locating data.

## Core Concepts
-   **[[HTML_Basics|HTML Document Structure]]:** The basic layout (`<html>`, `<head>`, `<body>`).
-   **[[HTML_Tags_Overview|HTML Tags]]:** Define the structure and semantics of web content.
-   **[[HTML_Attributes_Overview|HTML Attributes]]:** Provide additional information about HTML elements (e.g., `id`, `class`, `href`, `src`).
-   **[[DOM_Document_Object_Model|DOM Tree]]:** How these elements are represented hierarchically.

## Common HTML Tags Relevant to Scraping
A detailed list and description of common tags:
-   [[HTML_Common_Tags|Common HTML Tags for Scraping]]
    -   Includes notes on `<div>`, `<span>`, `<p>`, `<a>`, `<h1>`-`<h6>`, `<li>`, `<ol>`, `<ul>`, `<table>` (and its children `<tr>`, `<td>`, `<th>`), `<img>`, `<form>`, `<input>`, `<button>`, `<head>`, `<body>`, `<main>`, `<nav>`, `<menu>`, `<map>` (less common for scraping data directly but for image maps).

## Common HTML Attributes Relevant to Scraping
A detailed list and description of common attributes used for selecting elements:
-   [[HTML_Common_Attributes|Common HTML Attributes for Selection]]
    -   Includes notes on `id`, `class`, `style`, `href`, `src`, `alt`, `title`, `value`, `placeholder`, `data-*` attributes, `target`, `required`, `draggable`, `novalidate`.

## Using Tags and Attributes for Selection
-   **[[CSS_Selectors|CSS Selectors]]:** Use tag names, IDs (`#my-id`), classes (`.my-class`), and attribute selectors (`[attribute="value"]`) to target elements.
-   **[[XPath_Selectors|XPath]]:** Use paths like `//div[@class="content"]/p` to select elements based on tag names, attributes, and their position in the DOM tree.

## Notes in this HTML Elements Section
```dataview
LIST
FROM "190_Web_Scraping_Crawling/HTML_Elements"
WHERE file.folder = this.file.folder AND file.name != this.file.name AND !contains(file.name, "MOC")
SORT file.name ASC
```

---