---
tags:
  - html
  - web_development
  - web_scraping
  - html_attributes
  - selectors
  - concept
aliases:
  - Common HTML Attributes
  - HTML Attributes for Selection
related:
  - "[[190_Web_Scraping_Crawling/HTML_Elements/_HTML_Elements_MOC|_HTML_Elements_MOC]]"
  - "[[HTML_Basics]]"
  - "[[HTML_Common_Tags]]"
  - "[[CSS_Selectors]]"
  - "[[XPath_Selectors]]"
worksheet:
  - WS_WebScraping_1
date_created: 2025-06-18
---
# Common HTML Attributes Relevant for Selection

HTML attributes provide additional information about HTML elements and are crucial for web scraping as they are often used to uniquely identify or group elements for data extraction. [[CSS_Selectors|CSS selectors]] and [[XPath_Selectors|XPath expressions]] heavily rely on attributes.

[list2tab|#Common HTML Attributes]
- Core Identification
    - **`id`**
        -   **Purpose:** Specifies a **unique identifier** for an HTML element within a document. Should be unique per page.
        -   **Scraping Relevance:** Excellent for targeting a specific element because it's supposed to be unique.
        -   **Selector Example:** CSS: `#myElementId`, XPath: `//*[@id="myElementId"]`
    - **`class`**
        -   **Purpose:** Specifies one or more class names for an HTML element. An element can have multiple classes, separated by spaces. Used to style elements with CSS or select them with JavaScript/scrapers. Multiple elements can share the same class.
        -   **Scraping Relevance:** Very common for targeting groups of similar elements (e.g., all product listings, all review containers).
        -   **Selector Example:** CSS: `.myClassName`, `.class1.class2` (element with both classes), XPath: `//*[@class="myClassName"]`, `//*[contains(@class, "myClassName")]` (more robust for multiple classes).
- Styling & Presentation (Less direct for data, but can help locate)
    - **`style`**
        -   **Purpose:** Specifies inline CSS styling for an element.
        -   **Scraping Relevance:** Less common for direct data extraction, but sometimes specific styles might indicate a certain type of data or state (e.g., `<span style="color:red;">Error</span>`). Can be used in selectors: `[style*="color:red"]`.
- Links & Resources
    - **`href` (Hypertext Reference)**
        -   **Purpose:** Specifies the URL of the page the link goes to (for `<a>` anchor tags) or the location of a linked resource (for `<link>` tags, e.g., CSS files).
        -   **Scraping Relevance:** Essential for [[Crawling|crawling]] (extracting URLs to follow) and for getting the destination of links.
        -   **Selector Example:** `a[href]`, `a[href="https://example.com"]`, `a[href*="product"]` (href contains "product").
    - **`src` (Source)**
        -   **Purpose:** Specifies the URL of an external resource, typically for `<img>` (image source), `<script>` (JavaScript file), `<iframe>` (embedded frame source).
        -   **Scraping Relevance:** Crucial for extracting image URLs, or sometimes identifying external scripts that might load data.
        -   **Selector Example:** `img[src]`, `script[src*="api.js"]`.
- Textual & Semantic
    - **`alt` (Alternative Text)**
        -   **Purpose:** Provides alternative text for an image if the image cannot be displayed. Important for accessibility and SEO.
        -   **Scraping Relevance:** Can provide a textual description of an image, which might be the data you want if the image itself is hard to process.
    - **`title`**
        -   **Purpose:** Provides advisory information about an element, often shown as a tooltip when the mouse hovers over the element.
        -   **Scraping Relevance:** Can contain supplementary information or a longer description not visible directly on the page.
- Forms & Input
    - **`value`**
        -   **Purpose:** For `<input>`, `<button>`, `<option>`, `<li>` (ordered lists), `<meter>`, `<progress>`, `<param>` elements, it specifies the initial value or the value associated with the element.
        -   **Scraping Relevance:** Extracting pre-filled form data, selected option values, or values from hidden input fields which can be important session identifiers or tokens.
    - **`placeholder`**
        -   **Purpose:** Provides a short hint that describes the expected value of an input field (e.g., "Enter your email").
        -   **Scraping Relevance:** Usually not the data itself, but can help identify the purpose of an input field.
    - **`name`**
        -   **Purpose:** Used to identify form data after it has been submitted to the server, or to reference the element in JavaScript.
        -   **Scraping Relevance:** Important for understanding form submission or identifying specific input fields if IDs or classes are not available/reliable.
    - **`type` (for `<input>`)**
        -   **Purpose:** Defines the type of input field (e.g., `text`, `password`, `checkbox`, `radio`, `submit`, `hidden`, `date`, `email`).
        -   **Scraping Relevance:** Helps identify the nature of input fields. Hidden inputs (`type="hidden"`) can contain important data or tokens.
    - **`required`**
        -   **Purpose:** A boolean attribute specifying that an input field must be filled out before submitting the form.
        -   **Scraping Relevance:** Indicates mandatory fields if simulating form submissions.
    - **`novalidate` (for `<form>`)**
        -   **Purpose:** A boolean attribute indicating that the form should not be validated when submitted.
    - **`target` (for `<a>` and `<form>`)**
        -   **Purpose:** Specifies where to display the response after submitting the form or clicking a link (e.g., `_blank` for new tab, `_self`).
        -   **Scraping Relevance:** Usually less relevant for data extraction itself, but good to be aware of for understanding link behavior.
- Custom Data Attributes
    - **`data-*` (e.g., `data-product-id`, `data-price`)**
        -   **Purpose:** Custom data attributes are intended to store custom data private to the page or application. Attribute names must start with `data-`.
        -   **Scraping Relevance:** **Very useful for scraping.** Websites often store clean, machine-readable data (like IDs, prices, JSON strings) in `data-*` attributes, which can be more stable and easier to parse than trying to extract it from visible text or complex HTML structures.
        -   **Selector Example:** CSS: `[data-product-id]`, `div[data-price="29.99"]`, XPath: `//*[@data-product-id]`.
- Interactive (Less common for direct data extraction, more for interaction simulation)
    - **`draggable`**
        -   **Purpose:** Specifies whether an element is draggable.
    - **Event Handler Attributes (e.g., `onclick`, `onsubmit`)**
        -   **Purpose:** Define JavaScript code to run when an event occurs.
        -   **Scraping Relevance:** Indicates that [[JavaScript_Basics_for_Scraping|JavaScript]] is involved. Scrapers might need to trigger these events using [[Web_Drivers_for_Scraping|browser automation]] or analyze the JS code to understand what data is loaded/action performed.

Understanding these attributes and how to use them in selectors is key to robustly locating the specific data you want to extract from a web page. Always inspect the HTML structure of your target website to identify the most reliable attributes for selection.

---