---
tags:
  - python
  - list
  - built_in_function
  - max
  - min
  - len
  - sequence
  - data_structures
  - function
aliases:
  - max() on list
  - min() on list
  - len() of list
related:
  - "[[Python_List]]"
  - "[[Python_List_Methods]]"
  - "[[Built_In_Functions_Python]]"
worksheet:
  - WS17
date_created: 2025-06-11
---
# Python: `max()`, `min()`, and `len()` with Lists

While not methods of the list object itself (i.e., not called as `my_list.func()`), `max()`, `min()`, and `len()` are built-in Python functions that are commonly used with [[Python_List|lists]] (and other sequence/collection types).

## `len(s)`
-   **Purpose:** Returns the number of items in a container `s`. For a list, it returns the number of elements in the list.
-   **Syntax:** `len(list_object)`
-   **Return Value:** An integer representing the length of the list.
-   **Example (Number of products in a cart):**
    ```python
    shopping_cart = ["Laptop", "Mouse", "Keyboard", "Webcam"]
    number_of_items = len(shopping_cart)
    print(f"Number of items in cart: {number_of_items}") # Output: 4

    empty_cart = []
    print(f"Number of items in empty cart: {len(empty_cart)}") # Output: 0
    ```

## `max(iterable, *[, key, default])` or `max(arg1, arg2, *args[, key])`
-   **Purpose:**
    -   With a single iterable argument: Returns the largest item in an iterable or the largest of two or more arguments.
    -   With multiple arguments: Returns the largest of the arguments.
-   **Behavior with Lists:** When applied to a list, `max()` finds the largest element in the list.
    -   The elements in the list must be comparable (e.g., all numbers, or all strings). Mixing types like numbers and strings will raise a `TypeError`.
    -   For strings, comparison is lexicographical (alphabetical order).
-   **Optional `key` argument:** A function to be called on each list element prior to making comparisons. For example, `max(list_of_strings, key=len)` would find the longest string.
-   **Optional `default` argument (with iterable):** If the iterable is empty and `default` is provided, it's returned. Otherwise, `ValueError` is raised for an empty iterable.
-   **Syntax:** `max(list_object, key=None, default=...)`
-   **Return Value:** The largest item in the list.
-   **Example (Highest product price, longest product name):**
    ```python
    product_prices = [19.99, 120.50, 49.75, 250.00, 89.90]
    highest_price = max(product_prices)
    print(f"Highest product price: ${highest_price}") # Output: $250.0

    product_names = ["Laptop Pro", "Wireless Mouse", "Mechanical Keyboard Extended Edition", "Webcam HD"]
    longest_name = max(product_names, key=len) # Find the string with the maximum length
    print(f"Longest product name: '{longest_name}'") # Output: 'Mechanical Keyboard Extended Edition'

    empty_prices = []
    # max_empty = max(empty_prices) # This would raise ValueError
    max_empty_with_default = max(empty_prices, default=0.0)
    print(f"Max of empty list with default: {max_empty_with_default}") # Output: 0.0
    ```

## `min(iterable, *[, key, default])` or `min(arg1, arg2, *args[, key])`
-   **Purpose:** Similar to `max()`, but returns the smallest item in an iterable or the smallest of two or more arguments.
-   **Behavior with Lists:** When applied to a list, `min()` finds the smallest element in the list.
    -   Elements must be comparable.
    -   The `key` and `default` arguments work the same way as in `max()`.
-   **Syntax:** `min(list_object, key=None, default=...)`
-   **Return Value:** The smallest item in the list.
-   **Example (Lowest product rating, shortest product SKU):**
    ```python
    customer_ratings = [4.5, 3.0, 4.8, 2.5, 4.0, 5.0]
    lowest_rating = min(customer_ratings)
    print(f"Lowest customer rating: {lowest_rating}") # Output: 2.5

    product_skus = ["SKU10234", "SKU501", "SKU8"] # String comparison is lexicographical
    # For SKUs, lexicographical min might not be what's desired if numbers are involved without padding.
    # If SKUs were numbers, min would work as expected for numbers.
    # Example: if SKUs were based on an ID
    # product_skus_as_ids =
    # shortest_sku_id = min(product_skus_as_ids) -> 8

    # To find the SKU string with the shortest length:
    shortest_sku_by_length = min(product_skus, key=len)
    print(f"Shortest SKU by length: '{shortest_sku_by_length}'") # Output: 'SKU8'
    ```

These built-in functions provide convenient ways to get fundamental information about lists, such as their size and extreme values, without needing to write explicit loops.

---