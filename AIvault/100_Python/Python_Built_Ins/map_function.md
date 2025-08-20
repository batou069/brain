---
tags:
  - python
  - built_in_function
  - map
  - higher_order_function
  - functional_programming
  - iterator
  - concept
  - example
aliases:
  - map()
  - Python map function
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
# Python: `map(function, iterable, ...)` Built-in Function

The `map()` function is a built-in [[Python_Higher_Order_Functions|higher-order function]] that applies a given `function` to each item of one or more `iterable`(s) (e.g., list, tuple, string) and returns an **iterator** that yields the results.

## Syntax
```python
map(function, iterable1, iterable2, ...)
```
-   `function`: A function that takes as many arguments as there are iterables passed. This function will be called for each item from the iterable(s).
-   `iterable1, iterable2, ...`: One or more iterable objects.
    -   If multiple iterables are provided, `function` must take that many arguments, and it will be called with corresponding items from each iterable in parallel. The iteration stops when the shortest iterable is exhausted.

## Behavior
-   `map()` does not execute the function immediately for all items. It returns an **iterator** (a `map` object).
-   The actual computation (calling `function` on items) happens lazily, as you iterate over the `map` object (e.g., in a `for` loop, or by converting it to a list using `list()`).
-   It does not modify the original iterable(s).

## Return Value
-   An **iterator** that yields the results of applying `function` to each item of the input iterable(s).

## Examples

**1. Applying a function to a single iterable (e.g., product prices):**
```python
# Product prices in USD
prices_usd = 
# Function to convert USD to EUR (conceptual rate)
def usd_to_eur(price_usd):
    return round(price_usd * 0.92, 2)

prices_eur_iterator = map(usd_to_eur, prices_usd)

print(f"Map object: {prices_eur_iterator}")
# To see the results, convert the iterator to a list or iterate over it:
prices_eur_list = list(prices_eur_iterator)
print(f"Prices in EUR: {prices_eur_list}")
# Output:
# Map object: <map object at 0x...>
# Prices in EUR: [18.39, 45.54, 110.4, 23.46, 69.0]
```

**2. Using a [[Python_Lambda_Functions|lambda function]] with `map()`:**
This is very common for simple, one-off operations.
```python
# Product names
product_names = ["SuperWidget", "MegaGadget", "BasicTool"]

# Convert all product names to uppercase
uppercase_names_iterator = map(lambda name: name.upper(), product_names)
print(f"Uppercase names: {list(uppercase_names_iterator)}")
# Output: ['SUPERWIDGET', 'MEGAGADGET', 'BASICTOOL']
```

**3. Using `map()` with multiple iterables:**
The function must accept a corresponding number of arguments.
```python
# Product quantities and per-item prices
quantities = 
unit_prices = 
# Function to calculate total cost for each product type
def calculate_item_total(qty, price):
    return qty * price

total_costs_iterator = map(calculate_item_total, quantities, unit_prices)
print(f"Total costs for each item type: {list(total_costs_iterator)}")
# Output: [200, 750, 2400] (10*20, 15*50, 30*80)
```
If iterables are of different lengths, `map()` stops when the shortest iterable is exhausted.
```python
list_a = [1, 2, 3, 4]
list_b = [10, 20]
# 'sum_corresponding' will be called for (1,10) and (2,20)
sum_iterator = map(lambda x, y: x + y, list_a, list_b)
print(f"Sum of corresponding elements (shortest iterable limits): {list(sum_iterator)}")
# Output: [11, 22]
```

## `map()` vs. [[Python_Comprehensions|List Comprehensions]]
For many common use cases, list comprehensions can achieve the same result as `map()` and are often considered more Pythonic and readable by some.
-   **`map()` with lambda:** `list(map(lambda x: x * 2, numbers))`
-   **List Comprehension:** `[x * 2 for x in numbers]`

**Advantages of List Comprehensions over `map()` for simple cases:**
-   Often more concise and easier to read for straightforward transformations.
-   Can directly include filtering logic (`[x*2 for x in numbers if x > 0]`). With `map()`, you'd typically chain it with `filter()`.

**When `map()` might be preferred:**
-   When the transformation function is already defined (a named function) and you want to apply it directly.
-   When working with multiple iterables in parallel.
-   When an iterator is explicitly desired for memory efficiency with very large datasets, though generator expressions `(x * 2 for x in numbers)` also provide this.

The `map()` function is a powerful tool from functional programming paradigms, useful for applying a transformation to every element of an iterable.

---