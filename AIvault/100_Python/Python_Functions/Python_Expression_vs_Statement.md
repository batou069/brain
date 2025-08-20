---
tags:
  - python
  - programming_fundamentals
  - expression
  - statement
  - syntax
  - concept_comparison
aliases:
  - Python Expressions
  - Python Statements
  - Expression vs Statement
related:
  - "[[100_Python/Python_Functions/_Python_Functions_MOC|_Python_Functions_MOC]]"
  - "[[Python_Lambda_Functions]]"
worksheet:
  - WS18
date_created: 2025-08-20
---
# Python: Expression vs. Statement

In Python, like in many programming languages, it's important to distinguish between **expressions** and **statements**.

>[!question] What is the difference between "Expression" and "Statement"?

## Statement
-   **Definition:** A **statement** is a complete unit of execution that performs some action. Statements are the fundamental building blocks of a Python program. They represent an instruction or a command that the Python interpreter can execute.
-   **Characteristics:**
    -   They *do* something (e.g., assign a value, print output, define a function, control flow).
    -   They may or may not produce or evaluate to a value.
    -   A Python script is a sequence of statements.
-   **Examples of Statements:**
    -   **Assignment statement:** `product_price = 29.99`
    -   **Function definition statement:** `def calculate_discount(price): ...`
    -   **`if/elif/else` statements (Conditional statements):**
        ```python
        # if product_price > 100:
        #     print("Expensive item")
        # else:
        #     print("Affordable item")
        ```
    -   **`for` / `while` loop statements (Iteration statements):**
        ```python
        # for item in product_list:
        #     print(item)
        ```
    -   **`import` statement:** `import math`
    -   **`return` statement:** `return total_price`
    -   **`print()` call (in Python 3, `print` is a function, so `print(...)` is an expression statement):** `print("Hello")`
    -   **Expression statement:** An expression can also be a statement if it stands on its own line (though often it's for side effects like a function call that prints). `x + 5` on its own line is an expression statement; its value is computed and discarded unless it's part of a larger context like the REPL.

## Expression
-   **Definition:** An **expression** is a piece of code that **evaluates to a value**. It represents a computation.
-   **Characteristics:**
    -   They *produce* or *compute* a value.
    -   They can be made up of literals, variables, operators, and function calls that return values.
    -   Expressions can be part of statements (e.g., the right-hand side of an assignment, the condition in an `if` statement).
-   **Examples of Expressions:**
    -   **Literals:** `100` (evaluates to the integer 100), `"hello"` (evaluates to the string "hello"), `True`
    -   **Variable names:** `product_price` (evaluates to the value stored in `product_price`)
    -   **Arithmetic operations:** `price * quantity`, `5 + (3 / 2)`
    -   **Function calls that return a value:** `len(my_list)`, `math.sqrt(16)`, `my_function(arg)`
    -   **Comparisons:** `x > 10`, `name == "Alice"` (these evaluate to `True` or `False`)
    -   **Logical operations:** `is_in_stock and price < 50`
    -   **List/dict/set comprehensions:** `[x*x for x in range(5)]` (evaluates to a new list)
    -   **[[Python_Lambda_Functions|Lambda functions]]:** `lambda x: x * 2` (evaluates to a function object)
    -   **Conditional expressions (ternary operator):** `discount_price if is_member else regular_price`

## Key Differences Summarized

[list2mdtable|#Expression vs Statement]
- Feature
    - Statement
        - Expression
- **Primary Role**
    - Performs an action, an instruction.
        - Evaluates to a value, represents a computation.
- **Produces a Value?**
    - May or may not.
        - Always produces/evaluates to a value.
- **Composition**
    - Can contain expressions.
        - Can be part of statements or other larger expressions.
- **Examples**
    - `x = 5` (assignment), `if x > 0: ...`, `def foo(): ...`, `import os`
        - `5`, `x`, `x + 5`, `my_func()`, `x > 0`

**Analogy:**
-   Think of **statements** like complete sentences in English that convey an action or a declaration (e.g., "John ate an apple." or "Define a variable named 'age'.").
-   Think of **expressions** like phrases or clauses that have a value but might not be a complete sentence on their own (e.g., "an apple", "John's age", "5 plus 3").

## Expression Statements
An expression can also be a statement if it forms a line of code by itself. This is called an **expression statement**.
```python
# Expression statements
# "Hello World"  # A string literal, evaluates to itself, then discarded
# x + y            # Computes sum, result discarded (unless in REPL)
# my_function()    # Calls a function, its return value is discarded (if any, and not assigned)
```
In such cases, the expression is evaluated, but its result is discarded unless the expression has a side effect (like a function call that prints something or modifies a global variable). In the Python REPL, the result of an expression statement is automatically printed.

Understanding this distinction is helpful for grasping Python syntax, especially when working with constructs like lambda functions (which can only contain expressions) or list comprehensions.

---