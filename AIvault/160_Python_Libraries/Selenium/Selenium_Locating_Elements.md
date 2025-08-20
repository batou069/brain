---
tags:
  - python
  - selenium
  - webdriver
  - locators
  - find_element
  - css_selector
  - xpath
  - concept
  - example
aliases:
  - Selenium Locators
  - Finding Elements with Selenium
  - By Class
related:
  - "[[160_Python_Libraries/Selenium/_Selenium_MOC|_Selenium_MOC]]"
  - "[[Selenium_WebDriver_Basics]]"
  - "[[Selenium_Interacting_Elements]]"
  - "[[CSS_Selectors]]"
  - "[[XPath_Selectors]]"
worksheet:
  - WS_WebScraping_1
  - WS_Automation_1
date_created: 2025-08-20
---
# Selenium: Locating HTML Elements

After navigating to a page, the next step is to locate the specific HTML elements you want to interact with or extract data from. Selenium WebDriver provides the `find_element()` (to find a single element) and `find_elements()` (to find all matching elements) methods, which use different locator strategies defined in the `By` class.

## The `By` Class
To specify a locator strategy, you import the `By` class:
```python
from selenium.webdriver.common.by import By
```

## Common Locator Strategies
The `By` class provides the following strategies:

[list2tab|#Locator Strategies]
- `By.ID`
    -   **Description:** Locates an element by its unique `id` attribute. This is usually the fastest and most reliable locator if available.
    -   **Example:** `driver.find_element(By.ID, "product-title")`
- `By.NAME`
    -   **Description:** Locates an element by its `name` attribute. Often used for form elements.
    -   **Example:** `driver.find_element(By.NAME, "username")`
- `By.CLASS_NAME`
    -   **Description:** Locates elements that have a specific CSS class name. If an element has multiple classes, you must use one of them.
    -   **Example:** `driver.find_elements(By.CLASS_NAME, "product-card")`
- `By.TAG_NAME`
    -   **Description:** Locates elements by their HTML tag name.
    -   **Example:** `driver.find_elements(By.TAG_NAME, "a")` (finds all links)
- `By.LINK_TEXT`
    -   **Description:** Locates an anchor element (`<a>`) by its exact visible text.
    -   **Example:** `driver.find_element(By.LINK_TEXT, "Read More")`
- `By.PARTIAL_LINK_TEXT`
    -   **Description:** Locates an anchor element (`<a>`) whose visible text contains the given substring.
    -   **Example:** `driver.find_element(By.PARTIAL_LINK_TEXT, "More Info")`
- `By.CSS_SELECTOR`
    -   **Description:** Locates elements using a [[CSS_Selectors|CSS selector]]. This is a very powerful and versatile strategy.
    -   **Example:** `driver.find_element(By.CSS_SELECTOR, "div#main-content p.intro")`
- `By.XPATH`
    -   **Description:** Locates elements using an [[XPath_Selectors|XPath expression]]. This is the most powerful and flexible locator, allowing complex navigation of the DOM tree.
    -   **Example:** `driver.find_element(By.XPATH, '//button[contains(text(), "Submit")]')`

## `find_element()` vs. `find_elements()`
-   **`driver.find_element(By.STRATEGY, "value")`**:
    -   Finds the **first** web element that matches the locator.
    -   Returns a single `WebElement` object.
    -   If no element is found, it raises a `NoSuchElementException`.
-   **`driver.find_elements(By.STRATEGY, "value")`**:
    -   Finds **all** web elements that match the locator.
    -   Returns a **list** of `WebElement` objects.
    -   If no elements are found, it returns an empty list.

## Example: Locating Elements on a Conceptual Product Page
```python
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# try:
#     # Assume we navigate to a product page
#     # driver.get("http://example-ecommerce.com/product/123")

#     # --- Using find_element (for unique elements) ---
#     # Find the product title by its ID
#     # product_title_element = driver.find_element(By.ID, "product-name")

#     # Find the price using a CSS selector
#     # price_element = driver.find_element(By.CSS_SELECTOR, "span.current-price")

#     # Find the "Add to Cart" button using XPath based on its text
#     # add_to_cart_button = driver.find_element(By.XPATH, '//button[text()="Add to Cart"]')

#     # --- Using find_elements (for multiple elements) ---
#     # Find all feature list items
#     # feature_elements = driver.find_elements(By.CSS_SELECTOR, "ul.features li")

#     # Find all review containers
#     # review_elements = driver.find_elements(By.CLASS_NAME, "review-card")

#     # print(f"Found {len(feature_elements)} features.")
#     # print(f"Found {len(review_elements)} reviews.")

# except Exception as e:
#     print(f"An error occurred: {e}")
# finally:
#     if 'driver' in locals():
#         driver.quit()
```

## Best Practices for Locators
-   **Prefer unique and stable locators:** `ID` is usually the best choice if available and unique.
-   **Use descriptive `class` names or `data-*` attributes:** These are often more stable than the HTML structure itself. `[data-testid="..."]` is a common pattern for stable test/automation hooks.
-   **Use CSS selectors for most cases:** They are readable and powerful enough for most common selection tasks.
-   **Use XPath for complex scenarios:** Use XPath when you need to select based on text content or navigate complex relationships (e.g., finding a parent or sibling based on a child's content).
-   **Avoid brittle locators:** Avoid relying on auto-generated IDs or class names (e.g., `class="css-1dbjc4n r-13awgt0"`), as they can change on every page load. Also, avoid long, absolute XPath paths (e.g., `/html/body/div/div[2]/div/p[3]`) as they break easily with minor layout changes.
-   **Use [[Selenium_Waits|Waits]]:** Before locating an element, especially on dynamic pages, use explicit waits to ensure the element is present and interactive.

Choosing the right locator strategy is key to creating robust and maintainable browser automation scripts.

---