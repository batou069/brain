---
tags:
  - python
  - built_in_function
  - filter
  - higher_order_function
  - functional_programming
  - iterator
  - concept
  - example
aliases:
  - filter()
  - Python filter function
related:
  - "[[Built_In_Functions_Python]]"
  - "[[Python_Higher_Order_Functions]]"
  - "[[Python_Lambda_Functions]]"
  - "[[Python_List_Comprehensions|List Comprehensions]]"
  - "[[Python_Iterators_Generators|Iterators and Generators]]"
worksheet:
  - WS18
date_created: 2025-08-20
---
# Python: `filter(function, iterable)` Built-in Function

The `filter()` function is a built-in [[Python_Higher_Order_Functions|higher-order function]] that constructs an **iterator** from elements of an `iterable` for which a given `function` returns true.

## Syntax
```python
filter(function, iterable)```
-   `function`: A function that takes one argument (an element from the `iterable`) and returns a boolean value (`True` or `False`). If `function` is `None`, `filter()` removes items from the iterable that are "falsey" (e.g., `0`, `False`, `None`, empty sequences/mappings).
-   `iterable`: An iterable object (e.g., list, tuple, string, set, dictionary keys/values) whose elements will be tested by `function`.

## Behavior
-   `filter()` does not execute the `function` immediately for all items. It returns an **iterator** (a `filter` object).
-   The actual filtering (calling `function` on items) happens lazily, as you iterate over the `filter` object (e.g., in a `for` loop, or by converting it to a list using `list()`).
-   It does not modify the original iterable.

## Return Value
-   An **iterator** that yields only those elements from `iterable` for which `function(element)` is true.

## Examples

>[!question] Give examples of `filter()` Function usage.

**1. Filtering even numbers from a list of product quantities:**
```python
product_quantities = 
# Function to check if a number is even
def is_even(number):
    return number % 2 == 0

even_quantities_iterator = filter(is_even, product_quantities)

print(f"Filter object: {even_quantities_iterator}")
# To see the results, convert the iterator to a list or iterate over it:
even_quantities_list = list(even_quantities_iterator)
print(f"Even quantities: {even_quantities_list}")
# Output:
# Filter object: <filter object at 0x...>
# Even quantities:
```

**2. Using a [[Python_Lambda_Functions|lambda function]] with `filter()`:**
This is very common for simple, one-off filtering conditions.
```python
# E-commerce product ratings
product_ratings = [4.5, 2.8, 3.9, 5.0, 1.2, 4.1, 4.8]

# Filter for high ratings (e.g., rating >= 4.0)
high_ratings_iterator = filter(lambda rating: rating >= 4.0, product_ratings)
print(f"High ratings: {list(high_ratings_iterator)}")
# Output: [4.5, 5.0, 4.1, 4.8]
```

**3. Filtering strings (e.g., product names starting with 'Super'):**
```python
product_names = ["SuperWidget", "MegaGadget", "BasicTool", "SuperCharger", "Accessory"]

super_products_iterator = filter(lambda name: name.startswith("Super"), product_names)
print(f"Super products: {list(super_products_iterator)}")
# Output: ['SuperWidget', 'SuperCharger']
```

**4. Using `None` as the function to filter out "falsey" values:**
If `function` is `None`, items are filtered if they are "falsey" in a boolean context (e.g., `0`, `False`, `None`, empty strings, empty lists).
```python
# Mixed data, some representing stock availability (0 means out of stock)
stock_levels = [10, 0, 25, None, 50, False, "In Stock"] # "In Stock" is truthy

# Filter for items considered "in stock" (non-falsey values)
# This is a bit of a conceptual stretch for stock_levels, better to filter explicitly
# but demonstrates the None behavior.
truthy_values_iterator = filter(None, stock_levels)
print(f"Truthy stock levels: {list(truthy_values_iterator)}")
# Output: [10, 25, 50, 'In Stock']
```

## `filter()` vs. [[Python_Comprehensions|List Comprehensions]] with an `if` clause
For many common use cases, list comprehensions (or generator expressions) with an `if` clause can achieve the same result as `filter()` and are often considered more Pythonic and readable.
-   **`filter()` with lambda:** `list(filter(lambda x: x > 0, numbers))`
-   **List Comprehension:** `[x for x in numbers if x > 0]`
-   **Generator Expression (returns iterator):** `(x for x in numbers if x > 0)`

**Advantages of List Comprehensions/Generator Expressions over `filter()`:**
-   Often more concise and directly expresses the intent of creating a new filtered collection or iterator.
-   Can combine filtering and mapping in one expression: `[x*2 for x in numbers if x > 0]`. With `filter()` and `map()`, this would require chaining them.

**When `filter()` might be preferred:**
-   When the filtering logic is complex and already defined in a named function.
-   In some functional programming styles or when working with existing code that uses it.

The `filter()` function is a classic tool from functional programming for selectively extracting elements from an iterable based on a condition.

---