---
tags:
  - python
  - functions
  - programming_paradigms
  - scope
  - arguments
  - lambda
  - higher_order_functions
  - moc
  - concept
aliases:
  - Python Functions MOC
  - Defining Functions Python
related:
  - "[[100_Python/_Python_Programming_MOC|_Python_Programming_MOC]]"
  - "[[Python_Function_Definition_Syntax]]"
  - "[[Python_Pure_Functions]]"
  - "[[Python_Higher_Order_Functions]]"
  - "[[Python_Recursion]]"
  - "[[Python_Nested_Functions_Closures|Python Nested Functions, Closures, Nonlocal]]"
  - "[[Python_Args_Kwargs|Python *args and **kwargs]]"
  - "[[Python_Lambda_Functions]]"
  - "[[Python_Comprehensions]]"
  - "[[Python_Decorators]]"
  - "[[Built_In_Functions_Python#map_function|map() built-in]]"
  - "[[Built_In_Functions_Python#filter_function|filter() built-in]]"
  - "[[Built_In_Functions_Python#reduce_function|functools.reduce()]]"
worksheet:
  - WS18
date_created: 2025-08-20
---
# Python Functions MOC ⚙️

Functions are fundamental building blocks in Python, allowing you to encapsulate reusable blocks of code, improve modularity, and organize your programs effectively. This section explores various aspects of defining and using functions in Python.

## Core Concepts
-   [[Python_Function_Definition_Syntax|Defining Functions (`def` statement)]]
    -   Parameters and Arguments
    -   Return Values (`return` statement)
    -   Docstrings
-   [[Python_Pure_Functions|Pure Functions]]
-   [[Python_Higher_Order_Functions|Higher-Order Functions]]
-   [[Python_Recursion|Recursion]]
-   [[Python_Nested_Functions_Closures|Nested Functions, Closures, and Nonlocal Variables]]
    -   Enclosing scope
    -   `nonlocal` keyword
-   [[Python_Args_Kwargs|Variable Arguments (`*args` and `**kwargs`)]]
    -   Argument unpacking
-   [[Python_Lambda_Functions|Lambda Functions (Anonymous Functions)]]
-   [[Python_Comprehensions|Comprehensions (List, Dict, Set, Generator)]]
    -   Syntax and benefits
    -   Nested comprehensions
-   [[Python_Decorators|Decorators]]
-   [[Python_Expression_vs_Statement|Expressions vs. Statements]]

## Built-in Functions Related to Functional Programming
-   [[Built_In_Functions_Python#map_function|`map(function, iterable, ...)`]]
-   [[Built_In_Functions_Python#filter_function|`filter(function, iterable)`]]
-   [[Built_In_Functions_Python#reduce_function|`functools.reduce(function, iterable[, initializer])`]] (Note: `reduce` is in the `functools` module)

## Notes in this Section
```dataview
LIST
FROM "100_Python/Python_Functions"
WHERE file.folder = this.file.folder AND file.name != this.file.name AND !contains(file.name, "MOC")
SORT file.name ASC
```

---