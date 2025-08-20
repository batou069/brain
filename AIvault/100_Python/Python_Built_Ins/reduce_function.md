---
tags:
  - python
  - functools
  - reduce
  - higher_order_function
  - functional_programming
  - aggregation
  - iterator
  - concept
  - example
aliases:
  - functools.reduce()
  - Python reduce function
related:
  - "[[Built_In_Functions_Python]]"
  - "[[Python_Higher_Order_Functions]]"
  - "[[Python_Lambda_Functions]]"
  - "[[Python_Loops_Iteration|Looping and Iteration]]"
worksheet:
  - WS18
date_created: 2025-08-20
---
# Python: `functools.reduce(function, iterable[, initializer])`

The `reduce()` function is part of the `functools` module in Python's standard library. It is a [[Python_Higher_Order_Functions|higher-order function]] that applies a binary `function` (a function taking two arguments) cumulatively to the items of an `iterable`, from left to right, so as to reduce the iterable to a single accumulated value.

**Note:** `reduce()` was a built-in function in Python 2. In Python 3, it was moved to the `functools` module, so you need to import it: `from functools import reduce`.

## Syntax
```python
from functools import reduce

reduce(function, iterable, initializer=None)
```
-   `function`: A function that takes two arguments and returns a single value. This function will be applied cumulatively.
-   `iterable`: An iterable object (e.g., list, tuple) whose elements will be reduced.
-   `initializer` (optional): If provided, it is placed before the items of the iterable in the calculation and serves as a default when the iterable is empty.

## Behavior
1.  If `initializer` is **not** provided:
    -   The `function` is first applied to the first two items of the `iterable`.
    -   The result of this call then becomes the first argument to `function`, and the third item from `iterable` becomes the second argument.
    -   This process continues until all items in `iterable` have been processed.
    -   If `iterable` is empty, a `TypeError` is raised.
    -   If `iterable` has only one item, that item is returned without calling `function`.
2.  If `initializer` **is** provided:
    -   The `function` is first applied to `initializer` and the first item of `iterable`.
    -   The result of this call then becomes the first argument to `function`, and the second item from `iterable` becomes the second argument.
    -   This continues until all items in `iterable` have been processed.
    -   If `iterable` is empty, the `initializer` is returned.

## Return Value
-   The single, accumulated result of applying `function` cumulatively to the items of `iterable`.

## Examples

**1. Summing all numbers in a list (e.g., total quantity of products sold):**
```python
from functools import reduce
import operator # For common operator functions like operator.add

daily_units_sold = 
# Using a lambda function
total_units_lambda = reduce(lambda x, y: x + y, daily_units_sold)
print(f"Total units sold (lambda): {total_units_lambda}") # Output: 125

# Using operator.add for clarity and potential minor efficiency
total_units_operator = reduce(operator.add, daily_units_sold)
print(f"Total units sold (operator.add): {total_units_operator}") # Output: 125

# With an initializer (e.g., starting sum from 100)
total_units_with_initial = reduce(lambda x, y: x + y, daily_units_sold, 100)
print(f"Total units with initial 100: {total_units_with_initial}") # Output: 225
```

**2. Finding the maximum value in a list (e.g., peak daily sales):**
```python
from functools import reduce

# daily_sales_figures = 
# Using a lambda
# peak_sale_lambda = reduce(lambda x, y: x if x > y else y, daily_sales_figures)
# print(f"Peak daily sale (lambda): {peak_sale_lambda}") # Output: 150

# A more direct way for max is the built-in max() function
# print(f"Peak daily sale (built-in max()): {max(daily_sales_figures)}")
```
While `reduce` can do this, `max()` is more direct and readable for finding the maximum.

**3. Concatenating a list of strings (e.g., product tags):**
```python
from functools import reduce

product_tags_list = ["electronics", "wearable", "smartwatch", "fitness"]
concatenated_tags = reduce(lambda x, y: x + " | " + y, product_tags_list)
print(f"Concatenated tags: '{concatenated_tags}'")
# Output: 'electronics | wearable | smartwatch | fitness'
```
For string concatenation, `' | '.join(product_tags_list)` is usually more Pythonic and efficient.

## `reduce()` vs. `map()` vs. `filter()`

>[!question] What is the difference between the `map()` and `reduce()` functions?
>
>[list2mdtable|#map vs reduce vs filter]
>- Feature
>    - [[Built_In_Functions_Python#map_function|`map(func, iter)`]]
>        - `reduce(func, iter)`
>            - [[Built_In_Functions_Python#filter_function|`filter(func, iter)`]]
>- **Purpose**
>    - Applies `func` to each element of `iter` independently. Transforms each element.
>        - Cumulatively applies a binary `func` to the elements of `iter` to reduce it to a single value.
>            - Selects elements from `iter` for which `func` returns `True`.
>- **Input `func`**
>    - Takes one argument (or more if multiple iterables).
>        - Takes two arguments (accumulator, current_element).
>            - Takes one argument, returns a boolean.
>- **Output**
>    - Returns an iterator of the same length as the input iterable (or shortest if multiple). Each element is transformed.
>        - Returns a single accumulated value.
>            - Returns an iterator containing a subset of the original iterable's elements.
>- **Common Use**
>    - Element-wise transformation (e.g., squaring numbers, converting strings to uppercase).
>        - Aggregation (e.g., sum, product, finding min/max by accumulation).
>            - Selection/Filtering (e.g., getting all even numbers, filtering out None values).
>
>**Analogy (E-commerce Order Processing):**
>-   `map()`: Applying a 10% discount to the price of *each item* in an order.
>-   `filter()`: Selecting only the *items that are currently in stock* from an order.
>-   `reduce()`: Calculating the *total sum* of prices for all items in an order.

## Readability and Alternatives
Guido van Rossum (creator of Python) has mentioned that `reduce()` can be less readable than an explicit `for` loop for many common use cases like summing or finding a product, which is why it was moved to `functools`.
-   For summing: `sum(iterable)` is preferred.
-   For product: `math.prod(iterable)` (Python 3.8+).
-   For many other reductions, an explicit `for` loop might be clearer:
    ```python
    # total = 0
    # for x in my_list:
    #     total += x
    # is often clearer than reduce(lambda x, y: x + y, my_list) for simple summation.
    ```

However, `reduce()` remains a powerful tool for certain complex cumulative operations or when adhering to a more functional programming style.

---