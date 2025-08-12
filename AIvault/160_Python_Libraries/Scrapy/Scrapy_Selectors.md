---
tags:
  - python
  - scrapy
  - web_scraping
  - selectors
  - xpath
  - css
  - parsing
  - concept
  - example
aliases:
  - Scrapy Selectors
  - XPath Selectors Scrapy
  - CSS Selectors Scrapy
related:
  - "[[160_Python_Libraries/Scrapy/_Scrapy_MOC|_Scrapy_MOC]]"
  - "[[Scrapy_Spiders]]"
  - "[[HTML_Basics]]"
  - "[[XML_Basics]]"
  - "[[XPath_Selectors]]"
  - "[[CSS_Selectors]]"
  - "[[Beautiful_Soup_MOC|_Beautiful_Soup_MOC]]"
worksheet:
  - WS_WebScraping_1
date_created: 2025-06-09
---
# Scrapy: Selectors (XPath and CSS)

Scrapy comes with its own powerful mechanism for extracting data from HTML and XML responses, called **Selectors**. Scrapy Selectors are built upon the `parsel` library, which itself builds on `lxml`, allowing you to extract data using **XPath** expressions or **CSS selectors**.

When a [[Scrapy_Spiders|spider]]'s callback method receives a `response` object, you can use `response.xpath()` or `response.css()` to query the document.

## `response.css()` (CSS Selectors)
This method uses CSS selectors to find elements in the HTML/XML document. CSS selectors are often more concise and easier to read for common selection tasks. See [[CSS_Selectors]] for more on syntax.

-   `response.css('some_css_selector')`: Returns a `SelectorList` (a list-like object containing `Selector` objects).
-   Each `Selector` object in the list represents an HTML/XML element that matched the selector.
-   To extract data from a `Selector` object:
    -   `selector.get()`: Returns the first matched element's string content (for text nodes) or the full tag (for element nodes). Alias for `selector.extract_first()`.
    -   `selector.getall()`: Returns a list of all matched elements' string contents or full tags. Alias for `selector.extract()`.
    -   `selector.attrib['attribute_name']`: Accesses an attribute of the selected tag.
    -   `selector.css('further_css_selector')`: Apply another CSS selector relative to the current selector.
    -   `selector.xpath('further_xpath_selector')`: Apply an XPath selector relative to the current selector.

**Common CSS Selector patterns:**
-   Tag name: `p`, `div`, `a`
-   Class: `.my-class`
-   ID: `#my-id`
-   Attribute: `img[src]`, `a[href="..."]`
-   Descendant: `div p` (a `p` anywhere inside a `div`)
-   Direct child: `ul > li` (an `li` that is a direct child of `ul`)
-   Pseudo-classes: `a:first-child`, `p::text` (Scrapy extension for text content), `img::attr(src)` (Scrapy extension for attribute value).

**Example (using conceptual product page HTML):**
```python
# Assuming 'response' is a Scrapy Response object for a product page:
# html_content = """
# <html><body>
#     <h1 id="product-title" class="main-title">Awesome Widget</h1>
#     <div class="details">
#         <p>Price: <span class="price-value">$29.99</span></p>
#         <p class="description">A truly great widget.</p>
#         <ul class="features"><li>Feature 1</li><li>Feature 2</li></ul>
#         <a href="/reviews" class="reviews-link">Read Reviews</a>
#     </div>
# </body></html>
# """
# from scrapy.http import HtmlResponse
# response = HtmlResponse(url="http://example.com", body=html_content, encoding='utf-8')

# Extract product name (text content of h1 with id 'product-title')
# product_name = response.css('#product-title::text').get()
# print(f"Product Name: {product_name}") # Output: Awesome Widget

# Extract price (text content of span with class 'price-value')
# price = response.css('span.price-value::text').get()
# print(f"Price: {price}") # Output: $29.99

# Extract all feature list items (text content)
# features = response.css('ul.features li::text').getall()
# print(f"Features: {features}") # Output: ['Feature 1', 'Feature 2']

# Extract reviews link URL (href attribute of <a> with class 'reviews-link')
# reviews_url = response.css('a.reviews-link::attr(href)').get()
# print(f"Reviews URL: {reviews_url}") # Output: /reviews
```

## `response.xpath()` (XPath Selectors)
This method uses XPath expressions to find elements. XPath is more powerful and flexible than CSS selectors, especially for navigating complex XML structures or when needing to select based on text content or relationships like parent/sibling in more complex ways. See [[XPath_Selectors]] for more on syntax.

-   `response.xpath('some_xpath_expression')`: Returns a `SelectorList`.
-   Similar methods for extracting data: `.get()`, `.getall()`, `.attrib['attribute_name']`, `.xpath()`, `.css()`.

**Common XPath patterns:**
-   Select by tag name: `//p`, `//div`, `//a` (selects all such tags anywhere in document)
-   Select by attribute: `//img[@src]`, `//a[@href="..."]`, `//div[@class="my-class"]`
-   Select text content: `//h1/text()`, `//p[@class="description"]/text()`
-   Select attribute value: `//a/@href`
-   Navigating axes: `parent::*`, `child::p`, `following-sibling::div`

**Example (using the same conceptual HTML):**
```python
# (Using the same 'response' object as above)

# Extract product name
# product_name_xpath = response.xpath('//h1[@id="product-title"]/text()').get()
# print(f"Product Name (XPath): {product_name_xpath}")

# Extract price
# price_xpath = response.xpath('//span[@class="price-value"]/text()').get()
# print(f"Price (XPath): {price_xpath}")

# Extract all feature list items
# features_xpath = response.xpath('//ul[@class="features"]/li/text()').getall()
# print(f"Features (XPath): {features_xpath}")

# Extract reviews link URL
# reviews_url_xpath = response.xpath('//a[@class="reviews-link"]/@href').get()
# print(f"Reviews URL (XPath): {reviews_url_xpath}")
```

## Chaining Selectors
Both `response.css()` and `response.xpath()` return `SelectorList` objects. You can call `.css()` or `.xpath()` on individual `Selector` objects within these lists to perform selections relative to that element.

```python
# product_details_div = response.css('div.details').get() # Gets the first div.details
# if product_details_div: # This is not a Selector object, but a string if .get() is used
#     # Better:
#     product_details_selector = response.css('div.details') # This is a SelectorList
#     if product_details_selector:
#         # price_relative = product_details_selector.css('span.price-value::text').get()
#         # print(f"Price (relative CSS): {price_relative}")
#         description_relative = product_details_selector.xpath('.//p[@class="description"]/text()').get() # Note the .// for relative XPath
#         print(f"Description (relative XPath): {description_relative}")
```
Using `.` at the start of an XPath expression (e.g., `.//p`) makes it relative to the current selector's context node.

## Extracting Data
-   `get()` or `extract_first()`: Returns the first matched element/text/attribute. Returns `None` if no match. Useful when you expect only one result. You can provide a `default` value: `response.css('...').get(default='Not found')`.
-   `getall()` or `extract()`: Returns a list of all matched elements/texts/attributes. Returns an empty list if no matches.

## Regular Expressions with Selectors
You can use the `.re()` method on a `SelectorList` to extract data using regular expressions from the selected content.
-   `selector_list.re(r'some_regex_pattern')`: Returns a list of strings that match the regex. If the regex has a capturing group, it returns the content of the first group.

```python
# price_text = response.css('span.price-value::text').get() # "$29.99"
# if price_text:
#     # Extract only the number part using regex
#     price_numeric_list = response.css('span.price-value::text').re(r'\$(\d+\.\d+)')
#     if price_numeric_list:
#         price_numeric = price_numeric_list
#         print(f"Price Numeric (regex): {price_numeric}") # Output: 29.99
```

## Choosing Between CSS and XPath
-   **CSS Selectors:** Generally more readable and concise for common tasks like selecting by ID, class, or simple tag hierarchies. Preferred by many for HTML parsing due to familiarity from web development.
-   **XPath:** More powerful and expressive. Better for complex navigation (e.g., selecting parent or sibling elements based on conditions), selecting elements based on their text content directly, or working with XML documents where CSS selectors might be less natural.

Scrapy's selectors provide a flexible and efficient way to pinpoint and extract the exact data you need from web pages.

---