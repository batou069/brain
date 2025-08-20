---
tags:
  - python
  - functions
  - comprehensions
  - list_comprehension
  - dict_comprehension
  - set_comprehension
  - generator_expression
  - concise_code
  - functional_programming
  - concept
  - example
aliases:
  - Python Comprehensions
  - List Comprehensions
  - Dictionary Comprehensions
  - Set Comprehensions
  - Generator Expressions
related:
  - "[[100_Python/Python_Functions/_Python_Functions_MOC|_Python_Functions_MOC]]"
  - "[[Python_List]]"
  - "[[Python_Dictionary]]"
  - "[[Python_Set_Frozenset|Python Set]]"
  - "[[Python_Loops_Iteration|Looping and Iteration]]"
  - "[[Python_Lambda_Functions]]"
worksheet:
  - WS18
date_created: 2025-08-20
---
# Python: Comprehensions (List, Dict, Set) and Generator Expressions

**Comprehensions** in Python provide a concise and readable way to create lists, dictionaries, or sets from existing iterables. They are often more compact and sometimes more efficient than using explicit `for` loops and `append()` calls or conditional logic to build these collections.

**Generator Expressions** use a similar syntax but create an iterator instead of a fully realized collection in memory immediately.

>[!question] What is the benefit of using comprehensions?
>The primary benefits of using comprehensions are:
>1.  **Conciseness and Readability:** They allow you to create collections in a single, often more readable line of code compared to multi-line `for` loops. The intent of creating a new collection based on an existing one is very clear.
>2.  **Expressiveness:** They elegantly express common patterns like mapping (applying an operation to each element) and filtering (selecting elements based on a condition).
>3.  **Performance (Often):** List comprehensions, in particular, can be faster than equivalent `for` loops with `append()` calls because the list construction is optimized at a lower level in CPython.
>4.  **Pythonic Style:** Using comprehensions is considered a more "Pythonic" way to create collections from iterables for many common use cases.

## 1. List Comprehensions
-   **Purpose:** Create a new [[Python_List|list]] by applying an expression to each item in an iterable, optionally filtering items.
-   >[!question] What is the syntax of list comprehension?
    >```python
    >[expression for item in iterable if condition]
    >```
    >-   `expression`: The operation to apply to each `item` (e.g., `item * 2`, `item.upper()`). This becomes an element in the new list.
    >-   `item`: A variable representing each element from the `iterable`.
    -   `iterable`: The existing sequence or iterable to process (e.g., a list, tuple, string, range).
    -   `if condition` (optional): A filter. Only items for which the `condition` is `True` will be processed by the `expression` and included in the new list.

**Examples (E-commerce context):**
```python
# a. Square of product quantities
quantities =
squared_quantities = [q**2 for q in quantities]
print(f"Squared quantities: {squared_quantities}") # Output:

# b. Uppercase product category names
categories = ["electronics", "books", "apparel"]
uppercase_categories = [cat.upper() for cat in categories]
print(f"Uppercase categories: {uppercase_categories}") # Output: ['ELECTRONICS', 'BOOKS', 'APPAREL']

# c. Filter for product prices above a threshold and apply a discount
prices = [99.99, 150.00, 25.50, 200.00, 10.00]
min_price_for_discount = 50.00
discount_rate = 0.10 # 10%
discounted_high_prices = [
    price * (1 - discount_rate) 
    for price in prices 
    if price > min_price_for_discount
]
print(f"Discounted high prices: {[f'{p:.2f}' for p in discounted_high_prices]}") 
# Output: ['135.00', '180.00'] (for 150.00 and 200.00)
```

>[!question] What is nested list comprehension?
>A nested list comprehension involves one or more `for` clauses (and optional `if` clauses) within another list comprehension, allowing you to work with nested iterables or create lists of lists (like matrices).
>
>**Syntax (conceptual for two levels):**
>```python
>[expression for outer_item in outer_iterable for inner_item in inner_iterable if condition]
>```
>The `for` clauses are nested from left to right.
>
>**Example: Flattening a list of product tags**
>```python
>product_tags_nested = [
#    ["electronics", "new", "sale"],
#    ["books", "bestseller"],
#    ["apparel", "sale", "cotton"]
#]
#
#all_tags_flat = [tag for sublist in product_tags_nested for tag in sublist]
#print(f"Flattened tags: {all_tags_flat}")
## Output: ['electronics', 'new', 'sale', 'books', 'bestseller', 'apparel', 'sale', 'cotton']
#
# Get unique flattened tags
# unique_tags_flat = list(set([tag.lower() for sublist in product_tags_nested for tag in sublist]))
# print(f"Unique flattened tags (lowercase): {unique_tags_flat}")
>```
>**Example: Creating a matrix (list of lists)**
>```python
#matrix = [[row * col for col in range(1, 4)] for row in range(1, 4)]
## matrix will be [1*1, 1*2, 1*3] ->
## matrix will be [2*1, 2*2, 2*3] ->
## matrix will be [3*1, 3*2, 3*3] ->
#print(f"Generated matrix:\n{matrix}")
>```
>While powerful, deeply nested list comprehensions can sometimes become hard to read. For very complex nesting, traditional `for` loops might be clearer.

## 2. Dictionary Comprehensions
-   **Purpose:** Create a new [[Python_Dictionary|dictionary]] from an iterable.
-   **Syntax:**
    ```python
    {key_expression: value_expression for item in iterable if condition}
    ```
**Example: Create a dictionary of product names and their lengths**
```python
#product_names = ["Laptop", "Mouse", "Keyboard", "Monitor"]
#name_lengths = {name: len(name) for name in product_names}
#print(f"Product name lengths: {name_lengths}")
## Output: {'Laptop': 6, 'Mouse': 5, 'Keyboard': 8, 'Monitor': 7}

# Create a dictionary of products with price > 50
#product_prices = {"Laptop": 1200, "Mouse": 25, "Keyboard": 75, "Webcam": 45}
#expensive_products = {name: price for name, price in product_prices.items() if price > 50}
#print(f"Expensive products: {expensive_products}")
## Output: {'Laptop': 1200, 'Keyboard': 75}
```

## 3. Set Comprehensions
-   **Purpose:** Create a new [[Python_Set_Frozenset|set]] (containing unique elements) from an iterable.
-   **Syntax:**
    ```python
    {expression for item in iterable if condition}
    ```
    Note the use of curly braces `{}` but without key-value pairs like dictionaries.

**Example: Get unique uppercase first letters of product categories**
```python
#product_categories_list = ["electronics", "books", "apparel", "electronics", "home goods", "books"]
#unique_first_letters_upper = {category.upper() for category in product_categories_list}
#print(f"Unique uppercase first letters: {unique_first_letters_upper}")
## Output (order may vary): {'APPAREL', 'BOOKS', 'ELECTRONICS', 'HOME GOODS'}
```

## 4. Generator Expressions
-   **Purpose:** Create a **generator object**, which is an iterator that produces items on demand (lazily).
-   **Syntax:** Similar to list comprehension but uses parentheses `()` instead of square brackets `[]`.
    ```python
    (expression for item in iterable if condition)
    ```
-   **Benefits:**
    -   **Memory Efficient:** Does not create the entire collection in memory at once. Values are generated one by one as needed. This is very useful for large datasets.
    -   **Lazy Evaluation:** Computation is deferred until the generator is iterated over.
-   **Use Cases:** When you need to iterate over a sequence once (e.g., in a `for` loop, or as an argument to functions like `sum()`, `min()`, `max()`) and don't need to store the entire sequence in memory.

**Example: Sum of squares of numbers without creating a full list**
```python
#large_number_range = range(1, 1000001) # Represents a large sequence

# Generator expression for squares
#squares_generator = (x**2 for x in large_number_range)
#print(f"Generator object: {squares_generator}")

# Summing the squares using the generator (efficient)
#total_sum_of_squares = sum(squares_generator)
#print(f"Sum of squares (1 to 1,000,000): {total_sum_of_squares}") 
# This avoids creating a list of a million squared numbers in memory.

# If you did:
# squares_list = [x**2 for x in large_number_range] # Creates a very large list in memory
# total_sum_from_list = sum(squares_list)
```

Comprehensions and generator expressions are powerful tools in Python for creating collections and iterators in a concise, readable, and often efficient manner.

---