---
tags:
  - python
  - beautifulsoup
  - bs4
  - web_scraping
  - html_parser
  - example
  - practical_use_case
aliases:
  - BeautifulSoup Scraping Examples
  - BS4 Use Cases
related:
  - "[[160_Python_Libraries/Beautiful_Soup/_Beautiful_Soup_MOC|_Beautiful_Soup_MOC]]"
  - "[[BS4_Parsing_Documents]]"
  - "[[BS4_Navigating_Tree]]"
  - "[[BS4_Searching_Tree]]"
  - "[[BS4_Accessing_Attributes_Text]]"
  - "[[Requests_Library]]"
worksheet:
  - WS_WebScraping_1
date_created: 2025-06-11
---
# Beautiful Soup: Practical Scraping Examples

This note demonstrates how to combine [[BS4_Parsing_Documents|parsing]], [[BS4_Navigating_Tree|navigation]], [[BS4_Searching_Tree|searching]], and [[BS4_Accessing_Attributes_Text|attribute/text extraction]] with Beautiful Soup to scrape data from a conceptual e-commerce product page.

**Assumed HTML Structure (Conceptual `product_page.html`):**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>SuperWidget X1000 - Awesome Products Inc.</title>
</head>
<body>
    <header>
        <img src="/logo.png" alt="Awesome Products Inc. Logo">
        <nav>
            <a href="/">Home</a> | <a href="/products">Products</a> | <a href="/contact">Contact</a>
        </nav>
    </header>
    <main>
        <article class="product-listing" data-product-id="SWX1000">
            <h1 id="product-name">SuperWidget X1000</h1>
            <img class="product-image" src="/images/widget_x1000.jpg" alt="Image of SuperWidget X1000">
            
            <section class="pricing">
                <span class="price-label">Price:</span>
                <span class="current-price">$49.99</span>
                <span class="original-price">$59.99</span>
                <span class="discount-badge">Save 17%</span>
            </section>
            
            <section id="description">
                <h2>Product Description</h2>
                <p>The <strong>SuperWidget X1000</strong> is our latest innovation in widget technology. 
                It offers unparalleled performance and durability. <em>Perfect for all your widgeting needs!</em></p>
                <p>Comes in three exciting colors: Red, Blue, and Green.</p>
            </section>
            
            <section class="features">
                <h2>Key Features</h2>
                <ul>
                    <li>Durable Titanium Alloy</li>
                    <li>Water-Resistant (IP68)</li>
                    <li>Bluetooth 5.2 Connectivity</li>
                    <li>Long-lasting Battery</li>
                </ul>
            </section>
            
            <section class="reviews">
                <h2>Customer Reviews (<span id="review-count">352</span>)</h2>
                <div class="review-item" data-review-id="r001">
                    <p class="reviewer-name">Jane D.</p>
                    <p class="review-rating">Rating: <span>5</span>/5 Stars</p>
                    <p class="review-text">Absolutely love it! Best widget ever.</p>
                </div>
                <div class="review-item" data-review-id="r002">
                    <p class="reviewer-name">John S.</p>
                    <p class="review-rating">Rating: <span>4</span>/5 Stars</p>
                    <p class="review-text">Pretty good, but battery could be better.</p>
                </div>
                <!-- More reviews... -->
                <a href="#more-reviews" class="load-more">Load More Reviews</a>
            </section>
        </article>
    </main>
    <footer>
        <p>&copy; 2024 Awesome Products Inc. All rights reserved.</p>
    </footer>
</body>
</html>
```

**Python Scraping Script:**
```python
import requests # To fetch HTML (conceptually, actual fetching might be blocked)
from bs4 import BeautifulSoup
import pandas as pd # To store scraped data

# --- Step 1: Fetch HTML Content (Conceptual) ---
# In a real scenario, you'd fetch this from a URL.
# For this example, we'll use the HTML string defined above.
# url = "http://example-ecommerce.com/product/SWX1000"
# try:
#     response = requests.get(url, timeout=10)
#     response.raise_for_status() # Check for HTTP errors
#     html_content = response.text
# except requests.exceptions.RequestException as e:
#     print(f"Could not fetch URL {url}: {e}")
#     # Using the sample HTML directly for this example if fetch fails
html_content_from_above = """... [Copy the HTML from above here for a runnable script] ..."""
# For a script to run, replace the line above with the actual HTML content string.
# For this note, assume html_content_from_above is populated.
if not html_content_from_above.startswith("<!DOCTYPE html>"): # Quick check if it's not populated
    html_content_from_above = """
    <html><head><title>SuperWidget X1000</title></head><body>
    <article class="product-listing" data-product-id="SWX1000">
        <h1 id="product-name">SuperWidget X1000</h1>
        <img class="product-image" src="/images/widget_x1000.jpg" alt="Image of SuperWidget X1000">
        <section class="pricing"><span class="current-price">$49.99</span><span class="original-price">$59.99</span></section>
        <section id="description"><p>The <strong>SuperWidget X1000</strong> is great.</p></section>
        <section class="features"><ul><li>Titanium Alloy</li><li>Water-Resistant</li></ul></section>
        <section class="reviews"><span id="review-count">352</span>
            <div class="review-item" data-review-id="r001"><p class="reviewer-name">Jane D.</p><p class="review-rating">Rating: <span>5</span>/5</p><p class="review-text">Love it!</p></div>
            <div class="review-item" data-review-id="r002"><p class="reviewer-name">John S.</p><p class="review-rating">Rating: <span>4</span>/5</p><p class="review-text">Good.</p></div>
        </section>
    </article></body></html>""" # Minimal fallback

# --- Step 2: Parse HTML with Beautiful Soup ---
soup = BeautifulSoup(html_content_from_above, 'lxml') # Using lxml, or 'html.parser'

# --- Step 3: Extract Product Information ---
product_info = {}

# Product Name
product_name_tag = soup.find('h1', id='product-name')
product_info['name'] = product_name_tag.string.strip() if product_name_tag else None

# Product ID (from data attribute)
product_article_tag = soup.find('article', class_='product-listing')
product_info['id'] = product_article_tag['data-product-id'] if product_article_tag and 'data-product-id' in product_article_tag.attrs else None

# Image URL
product_image_tag = soup.find('img', class_='product-image')
product_info['image_url'] = product_image_tag['src'] if product_image_tag and 'src' in product_image_tag.attrs else None

# Pricing
current_price_tag = soup.select_one('section.pricing span.current-price')
product_info['current_price'] = current_price_tag.string.strip() if current_price_tag else None

original_price_tag = soup.select_one('section.pricing span.original-price')
product_info['original_price'] = original_price_tag.string.strip() if original_price_tag else None

# Description (get all text within the description section)
description_section = soup.find('section', id='description')
if description_section:
    # Find the first <p> tag directly under description_section, or all <p> tags
    # For this example, let's take all text content, stripped
    product_info['description'] = description_section.get_text(separator=" ", strip=True)
else:
    product_info['description'] = None

# Key Features (as a list)
features_list = []
features_section = soup.find('section', class_='features')
if features_section:
    feature_items = features_section.find_all('li')
    for item in feature_items:
        if item.string:
            features_list.append(item.string.strip())
product_info['features'] = features_list if features_list else None

# Review Count
review_count_tag = soup.find('span', id='review-count')
try:
    product_info['review_count'] = int(review_count_tag.string) if review_count_tag and review_count_tag.string else 0
except ValueError:
    product_info['review_count'] = 0


# --- Step 4: Extract Individual Reviews (first few) ---
reviews_data = []
review_item_tags = soup.select('section.reviews div.review-item', limit=5) # Limit to 5 reviews for example

for review_tag in review_item_tags:
    review = {}
    review['review_id'] = review_tag.get('data-review-id')
    
    reviewer_name_tag = review_tag.find('p', class_='reviewer-name')
    review['reviewer_name'] = reviewer_name_tag.string.strip() if reviewer_name_tag and reviewer_name_tag.string else None
    
    rating_tag = review_tag.select_one('p.review-rating span') # Get the span inside p.review-rating
    try:
        review['rating_value'] = int(rating_tag.string) if rating_tag and rating_tag.string else None
    except ValueError:
        review['rating_value'] = None
        
    review_text_tag = review_tag.find('p', class_='review-text')
    review['review_text'] = review_text_tag.string.strip() if review_text_tag and review_text_tag.string else None
    
    reviews_data.append(review)

# --- Step 5: Display or Store Scraped Data ---
# print("--- Product Information ---")
# for key, value in product_info.items():
#     print(f"{key.replace('_', ' ').title()}: {value}")

# print("\n--- Extracted Reviews (First Few) ---")
# for rev in reviews_data:
#     print(rev)

# Optional: Store in a Pandas DataFrame
# product_df = pd.DataFrame([product_info])
# reviews_df = pd.DataFrame(reviews_data)
# print("\n--- Product DataFrame ---")
# print(product_df)
# print("\n--- Reviews DataFrame ---")
# print(reviews_df)
```

**Explanation of Techniques Used:**
-   **`soup.find('tag_name', id='some_id')`**: Finds the first tag with the given name and ID.
-   **`soup.find('tag_name', class_='some_class')`**: Finds the first tag with the given name and CSS class. Note `class_` due to `class` being a Python keyword.
-   **`tag['attribute_name']`**: Accesses the value of an attribute.
-   **`tag.string`**: Gets the text content if the tag has only one string child.
-   **`soup.select('css_selector')`**: Finds all tags matching a CSS selector, returns a list.
-   **`soup.select_one('css_selector')`**: Finds the first tag matching a CSS selector.
-   **`tag.get_text(separator=" ", strip=True)`**: Gets all text from a tag and its children, stripped of whitespace and joined by the separator.
-   **Error Handling (Conceptual):** The `if tag else None` pattern is a simple way to handle cases where an element might not be found. More robust error handling (try-except blocks) would be needed for production scrapers.
-   **Data Cleaning:** The example includes basic `.strip()` for text. Real-world scraping often requires more extensive cleaning (e.g., removing currency symbols, converting types, handling inconsistent formatting).

This example showcases a typical workflow for extracting structured data from an HTML page using Beautiful Soup's searching and data access capabilities. The specific selectors and logic would need to be adapted for different website structures.

---