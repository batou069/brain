---
tags:
  - python
  - functions
  - def_statement
  - parameters
  - arguments
  - return_statement
  - docstrings
  - syntax
  - concept
aliases:
  - Defining Python Functions
  - Python def
  - Function Parameters Python
  - Function Return Values
related:
  - "[[100_Python/Python_Functions/_Python_Functions_MOC|_Python_Functions_MOC]]"
worksheet:
  - WS18
date_created: 2025-08-20
---
# Python: Function Definition Syntax (`def`)

Functions in Python are defined using the `def` keyword, followed by the function name, parentheses `()` containing zero or more parameters, and a colon `:`. The indented block of code following the colon is the function body.

## Basic Syntax
```python
def function_name(parameter1, parameter2, ...):
    """
    Optional docstring: explains what the function does, its parameters, and what it returns.
    """
    # Function body: statements to be executed
    statement1
    statement2
    # ...
    return some_value # Optional return statement
```

[list2tab|#Function Components]
- `def` Keyword
    -   Signals the start of a function definition.
- Function Name
    -   A valid Python identifier (starts with a letter or underscore, followed by letters, numbers, or underscores).
    -   Conventionally, function names are lowercase with words separated by underscores (snake_case).
- Parameters (in parentheses `()`)
    -   Variables listed inside the parentheses in the function definition. They act as placeholders for the values that will be passed into the function when it is called.
    -   A function can have zero or more parameters.
    -   Parameters can have default values: `def greet(name, greeting="Hello"): ...`
    -   Can also include variable-length arguments: [[Python_Args_Kwargs|`*args` and `**kwargs`]].
- Colon (`:`)
    -   Marks the end of the function header.
- Docstring (Optional)
    -   A string literal (often a multi-line triple-quoted string) that is the first statement in the function body.
    -   Used to document the function's purpose, arguments, return value, etc.
    -   Accessible via `function_name.__doc__` or `help(function_name)`.
- Function Body
    -   One or more indented Python statements that make up the function's logic.
    -   Indentation (typically 4 spaces) is crucial in Python to define the scope of the function body.
- `return` Statement (Optional)
    -   Used to exit the function and optionally pass back a value (or multiple values as a tuple) to the caller.
    -   If there is no `return` statement, or a `return` statement without an expression, the function implicitly returns `None`.

    >[!question] What is the return value of this Function?
    >```python
    >def foo(num):
    >    print(num)
    >```
    >The function `foo(num)` will print the value of `num` to the console. Since there is no explicit `return` statement with a value, the function will implicitly **return `None`**.
    >```python
    >def foo(num):
    >    print(num)
    >
    >result = foo(10) # foo(10) will print 10
    >print(f"The result of foo(10) is: {result}") # Output: The result of foo(10) is: None
    >```

## Parameters vs. Arguments
-   **Parameters:** Variables defined in the function signature (e.g., `name` in `def greet(name):`).
-   **Arguments:** Actual values passed to the function when it is called (e.g., `"Alice"` in `greet("Alice")`).

## Example: E-commerce Price Calculator
```python
def calculate_total_price(item_price: float, quantity: int, discount_percentage: float = 0.0) -> float:
    """
    Calculates the total price for a quantity of items after applying a discount.

    Args:
        item_price (float): The price of a single item.
        quantity (int): The number of items.
        discount_percentage (float, optional): Discount as a decimal (e.g., 0.1 for 10%). 
                                               Defaults to 0.0 (no discount).

    Returns:
        float: The calculated total price after discount.
               Returns -1.0 if inputs are invalid (e.g., negative price or quantity).
    """
    if item_price < 0 or quantity < 0:
        return -1.0 # Indicate an error or invalid input
    
    subtotal = item_price * quantity
    discount_amount = subtotal * discount_percentage
    total_price = subtotal - discount_amount
    return total_price

# Calling the function
price1 = calculate_total_price(item_price=29.99, quantity=2)
price2 = calculate_total_price(item_price=100.00, quantity=3, discount_percentage=0.15) # 15% discount
price_invalid = calculate_total_price(item_price=-10, quantity=1)

print(f"Price for 2 items at $29.99: ${price1:.2f}")
print(f"Price for 3 items at $100.00 with 15% discount: ${price2:.2f}")
print(f"Price for invalid input: ${price_invalid:.2f}")
```
This example demonstrates:
-   Function definition with `def`.
-   Type hints for parameters (`item_price: float`) and return value (`-> float`).
-   A default value for `discount_percentage`.
-   A docstring explaining the function.
-   A `return` statement.
-   Calling the function with positional and keyword arguments.

Functions are a cornerstone of writing modular, reusable, and organized Python code.

---