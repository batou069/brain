---
tags:
  - python
  - functions
  - lambda
  - anonymous_function
  - functional_programming
  - concept
  - example
aliases:
  - Lambda Expressions Python
  - Anonymous Functions Python
  - Python Lambda
related:
  - "[[100_Python/Python_Functions/_Python_Functions_MOC|_Python_Functions_MOC]]"
  - "[[Python_Higher_Order_Functions]]"
worksheet:
  - WS18
date_created: 2025-08-20
---
# Python: Lambda Functions (Anonymous Functions)

A **lambda function** in Python is a small, anonymous function defined with the `lambda` keyword. Lambda functions are restricted to a single expression and are often used when you need a simple function for a short period and don't want to formally define it using `def`.

>[!question] What is a lambda Function?
>A lambda function is a small, anonymous (unnamed) function defined using the `lambda` keyword. It can take any number of arguments but can only have **one expression**. The expression is evaluated and returned. Lambda functions are syntactically restricted and cannot contain multiple statements or complex logic that would require multiple lines in a regular `def` function.

## Syntax
```python
lambda arguments: expression
```
-   `lambda`: Keyword indicating the start of a lambda function definition.
-   `arguments`: A comma-separated list of arguments (parameters) the function accepts, similar to a regular function's parameter list.
-   `:`: Separates the arguments from the expression.
-   `expression`: A single expression that is evaluated and whose result is returned by the lambda function. This expression cannot contain multiple statements or complex control flow like multi-line `if/else` or `for/while` loops (though conditional expressions are allowed).

## Key Characteristics
-   **Anonymous:** They don't have a formal name defined with `def` (though you can assign a lambda function to a variable, it's generally not the primary use case for complex lambdas).
-   **Single Expression:** The body of a lambda function is limited to a single expression. The result of this expression is implicitly returned.
-   **Concise:** Useful for creating simple, one-off functions without the boilerplate of a `def` statement.
-   **Often Used with Higher-Order Functions:** Frequently used as arguments to [[Python_Higher_Order_Functions|higher-order functions]] like `map()`, `filter()`, `sorted()`, or in GUI callbacks.

>[!question] Can we use more than one expression in the Lambda Function?
>No, a lambda function is restricted to a **single expression**. It cannot contain multiple statements or a block of statements like a regular function defined with `def`. The result of this single expression is what the lambda function returns.

>[!question] Can you create a lambda function that receives more than one parameter?
>Yes, a lambda function can accept multiple parameters, just like a regular function.
>```python
># Lambda with two parameters
>add_product_prices = lambda price1, price2: price1 + price2
>print(add_product_prices(10.99, 5.50)) # Output: 16.49
>
># Lambda with three parameters
>format_product_info = lambda name, category, stock: f"Product: {name} (Category: {category}) - Stock: {stock}"
>print(format_product_info("Smartwatch", "Electronics", 50))
>```

## Examples

**1. Simple arithmetic:**
```python
# Add 10 to an argument
add_ten = lambda x: x + 10
print(f"add_ten(5): {add_ten(5)}") # Output: 15

# Multiply two numbers
multiply = lambda x, y: x * y
print(f"multiply(6, 7): {multiply(6, 7)}") # Output: 42
```

**2. Using with `map()`:**
To apply a simple operation to all items in an iterable.
```python
# E-commerce: List of product prices
prices = 
# Apply a 5% discount to all prices
discounted_prices_iterator = map(lambda p: p * 0.95, prices)
print(f"Discounted prices: {list(discounted_prices_iterator)}")
# Output: [18.9905, 47.025, 114.0, 23.75, 72.1905]
```

**3. Using with `filter()`:**
To select items from an iterable based on a condition.
```python
# E-commerce: Product ratings
ratings = [4.5, 2.0, 3.8, 5.0, 1.5, 4.2, 4.9]
# Filter for high ratings (>= 4.0)
high_ratings_iterator = filter(lambda r: r >= 4.0, ratings)
print(f"High ratings: {list(high_ratings_iterator)}") # Output: [4.5, 5.0, 4.2, 4.9]
```

**4. Using with `sorted()` (or `list.sort()`) for custom sort keys:**
To sort an iterable based on a computed key.
```python
# List of product tuples: (product_name, price, stock_quantity)
products = [
    ("Laptop", 1200.00, 10),
    ("Mouse", 25.00, 150),
    ("Keyboard", 75.00, 75),
    ("Monitor", 300.00, 25)
]

# Sort products by price (the second element of each tuple)
sorted_by_price = sorted(products, key=lambda product: product[1])
print(f"Products sorted by price:\n{sorted_by_price}")

# Sort products by stock quantity (descending)
sorted_by_stock_desc = sorted(products, key=lambda product: product[2], reverse=True)
print(f"\nProducts sorted by stock (desc):\n{sorted_by_stock_desc}")
```

## When to Use Lambda Functions (and When Not To)

>[!question] When should you use Lambda Functions and when should you not?
>
>**When to Use Lambda Functions:**
>1.  **Short, Simple, One-Off Functions:** When you need a small, throwaway function for a specific, localized purpose, and defining a full `def` function would be overly verbose.
>2.  **Arguments to Higher-Order Functions:** They are very commonly used as arguments for functions like `map()`, `filter()`, `sorted()`, or as callbacks in GUI programming or event handling, where a simple function is needed to define a behavior.
>3.  **Improving Readability for Simple Operations:** For very simple operations, a lambda can sometimes make the code more concise and readable by keeping the logic inline. Example: `sorted(items, key=lambda x: x)` is often clearer than defining a separate one-line function just to extract `x`.
>
>**When NOT to Use (or Use with Caution):**
>4.  **Complex Logic:** If the function requires multiple expressions, statements, or complex control flow (multi-line if/else, loops), a lambda function is not appropriate. Use a regular `def` function instead for readability and maintainability.
>5.  **Readability Suffers:** If the lambda expression becomes too long or convoluted, it harms readability. A named `def` function is better in such cases. A good rule of thumb: if it's hard to understand the lambda at a glance, use `def`.
>6.  **Reusability:** If you need to use the same function logic in multiple places, define it once with `def` and give it a descriptive name. While you *can* assign a lambda to a variable (e.g., `my_adder = lambda x, y: x + y`), linters like PEP 8 often discourage this, suggesting `def my_adder(x, y): return x + y` instead for better clarity and debuggability (named functions show up better in tracebacks).
>7.  **Docstrings and Type Hints:** Lambda functions cannot have docstrings in the standard way, and adding type hints can make them look clunky (though possible with type-comment syntax or by assigning to a typed variable). Regular functions are better for documentation and explicit typing.

Lambda functions are a convenient tool for writing concise functional code in Python, but they should be used judiciously to maintain code clarity.

---