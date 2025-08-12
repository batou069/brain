---
tags:
  - python
  - beautifulsoup
  - bs4
  - web_scraping
  - html_parser
  - attributes
  - text_extraction
  - concept
  - example
aliases:
  - BeautifulSoup Attributes
  - BS4 Get Text
  - BS4 Tag Attributes
related:
  - "[[160_Python_Libraries/Beautiful_Soup/_Beautiful_Soup_MOC|_Beautiful_Soup_MOC]]"
  - "[[BS4_Parsing_Documents]]"
  - "[[BS4_Navigating_Tree]]"
  - "[[BS4_Searching_Tree]]"
worksheet:
  - WS_WebScraping_1
date_created: 2025-06-11
---
# Beautiful Soup: Accessing Tag Attributes and Text Content

Once you have located a `Tag` object in a parsed Beautiful Soup document (using [[BS4_Navigating_Tree|navigation]] or [[BS4_Searching_Tree|searching]] methods), you'll often need to extract its attributes (like `href` from an `<a>` tag or `class` from a `<div>`) and its textual content.

## Accessing Attributes
A `Tag` object in Beautiful Soup behaves much like a Python dictionary when it comes to accessing its attributes.

[list2tab|#Attribute Access]
- Dictionary-like Access
    -   You can get the value of an attribute by treating the tag like a dictionary:
        ```python
        from bs4 import BeautifulSoup
        html_doc = """
        <a href="http://example.com/product" class="product-link item" id="link123" data-sku="WIDGET-X">Product Page</a>
        <img src="image.jpg" alt="Product Image"/>
        """
        soup = BeautifulSoup(html_doc, 'html.parser')

        # link_tag = soup.find('a')
        # if link_tag:
        #     href_value = link_tag['href'] # Access 'href' attribute
        #     class_value = link_tag['class'] # Access 'class' attribute
        #     id_value = link_tag['id']
        #     data_sku_value = link_tag['data-sku']

        #     print(f"Href: {href_value}")         # Output: http://example.com/product
        #     print(f"Class: {class_value}")       # Output: ['product-link', 'item'] (class can have multiple values, returns a list)
        #     print(f"ID: {id_value}")           # Output: link123
        #     print(f"Data-SKU: {data_sku_value}") # Output: WIDGET-X

            # If an attribute doesn't exist, accessing it like a dict raises a KeyError
            # try:
            #     non_existent_attr = link_tag['style']
            # except KeyError as e:
            #     print(f"KeyError for 'style': {e}")
        ```
- Using `.get()` Method
    -   Similar to Python dictionaries, you can use the `.get()` method, which allows specifying a default value if the attribute is not found (preventing `KeyError`).
        ```python
        # img_tag = soup.find('img')
        # if img_tag:
        #     src_value = img_tag.get('src')
        #     alt_value = img_tag.get('alt')
        #     style_value = img_tag.get('style', 'default-style') # Provide a default

        #     print(f"\nImg Src: {src_value}")       # Output: image.jpg
        #     print(f"Img Alt: {alt_value}")       # Output: Product Image
        #     print(f"Img Style: {style_value}")   # Output: default-style
        ```
- `.attrs` Attribute
    -   You can get a Python dictionary of all a tag's attributes using `tag.attrs`.
        ```python
        # link_tag = soup.find('a')
        # if link_tag:
        #     all_attributes = link_tag.attrs
        #     print("\nAll attributes of <a> tag:", all_attributes)
        #     # Output: {'href': 'http://example.com/product', 'class': ['product-link', 'item'], 'id': 'link123', 'data-sku': 'WIDGET-X'}
        ```
- Multi-valued Attributes
    -   HTML5 allows some attributes (like `class`) to have multiple values. Beautiful Soup usually returns these as a list of strings.
    -   Other attributes that look multi-valued (like `style` in CSS syntax) are typically returned as a single string by Beautiful Soup, as that's how they are represented in the HTML.

## Accessing Text Content
Beautiful Soup provides several ways to get the text content within a tag, excluding the markup itself.

[list2tab|#Text Extraction]
- `.string` Attribute
    -   If a tag has only one child and that child is a `NavigableString` (i.e., just text, no other tags), then `tag.string` will give you that string.
    -   If a tag contains other tags, or multiple strings, or no string content, `tag.string` will be `None`.
    -   Useful for tags that are guaranteed to contain only simple text (e.g., `<title>`, often `<h1>` or simple `<p>`).
    -   **Example:**
        ```python
        html_text_doc = """
        <p>This is <b>bold</b> text.</p>
        <title>Simple Title</title>
        <div>Just text here</div>
        """
        soup_text = BeautifulSoup(html_text_doc, 'html.parser')

        # p_tag = soup_text.find('p')
        # print(f"\n.string of <p>: {p_tag.string}") # Output: None (because it contains a <b> tag)

        # title_tag_text = soup_text.title
        # print(f".string of <title>: {title_tag_text.string}") # Output: Simple Title

        # div_tag_text = soup_text.find('div')
        # print(f".string of <div>: {div_tag_text.string}") # Output: Just text here
        ```- `.strings` Generator
    -   Returns a generator that yields all the strings within a tag, recursively (including strings in child tags).
    -   Preserves whitespace, including newlines.
    -   **Example:**
        ```python
        # p_tag = soup_text.find('p') # <p>This is <b>bold</b> text.</p>
        # print("\n.strings from <p>:")
        # for s in p_tag.strings:
        #     print(repr(s))
        # # Output:
        # # 'This is '
        # # 'bold'
        # # ' text.'
        ```
- `.stripped_strings` Generator
    -   Similar to `.strings`, but it strips leading and trailing whitespace from each string.
    -   It also ignores strings that consist entirely of whitespace.
    -   Often more useful for extracting clean text.
    -   **Example:**
        ```python
        html_whitespace_doc = "<p>  Some \n text with  <b> extra \t space </b>. </p>"
        # soup_whitespace = BeautifulSoup(html_whitespace_doc, 'html.parser')
        # p_whitespace_tag = soup_whitespace.p
        # print("\n.stripped_strings from <p> with extra whitespace:")
        # for s in p_whitespace_tag.stripped_strings:
        #     print(repr(s))
        # # Output:
        # # 'Some'
        # # 'text with'
        # # 'extra \t space' # Note: internal whitespace like \t is kept by default
        # # '.'
        ```
- `.get_text(separator="", strip=False, types=(<NavigableString types>, <CData types>))` Method
    -   This is often the most convenient method for getting all human-readable text from a tag and its children, concatenated into a single Unicode string.
    -   `separator`: A string used to join the different pieces of text found. Default is an empty string (text runs together). A common choice is `" "`.
    -   `strip`: If `True`, whitespace at the beginning and end of each string is stripped before concatenation.
    -   `types`: Allows specifying which types of `NavigableString` elements to include.
    -   **Example (Extracting product description):**
        ```python
        html_product_desc = """
        <div class="description">
            <p>This is an <strong>awesome</strong> e-commerce product. It has many features:</p>
            <ul><li>Feature 1</li><li>Feature 2</li></ul>
            Check it out!
        </div>
        """
        # soup_desc = BeautifulSoup(html_product_desc, 'html.parser')
        # description_div = soup_desc.find('div', class_='description')

        # if description_div:
        #     text_no_sep = description_div.get_text()
        #     print("\nDescription text (no separator):\n", repr(text_no_sep))
            
        #     text_with_space_sep = description_div.get_text(separator=" ", strip=True)
        #     print("\nDescription text (space separator, stripped):\n", repr(text_with_space_sep))
        # # Output (space separator, stripped):
        # # 'This is an awesome e-commerce product. It has many features: Feature 1 Feature 2 Check it out!'
        ```

Choosing the right method for text extraction depends on whether you need a single string, an iterator of strings, and how you want to handle whitespace and nested tags. `.get_text(strip=True, separator=" ")` is often a good starting point for clean, readable text.

---