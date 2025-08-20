---
tags:
  - python
  - functions
  - higher_order_functions
  - functional_programming
  - map
  - filter
  - reduce
  - decorators
  - concept
  - example
aliases:
  - Higher Order Functions Python
  - HOFs
related:
  - "[[100_Python/Python_Functions/_Python_Functions_MOC|_Python_Functions_MOC]]"
  - "[[Python_Pure_Functions]]"
  - "[[Python_Lambda_Functions]]"
  - "[[Python_Decorators]]"
  - "[[Built_In_Functions_Python#map_function|map() built-in]]"
  - "[[Built_In_Functions_Python#filter_function|filter() built-in]]"
  - "[[Built_In_Functions_Python#reduce_function|functools.reduce()]]"
worksheet:
  - WS18
date_created: 2025-08-20
---
# Python: Higher-Order Functions

A **higher-order function (HOF)** is a function that does at least one of the following:
1.  Takes one or more functions as **arguments**.
2.  **Returns a function** as its result.

In Python, functions are "first-class citizens," meaning they can be treated like any other object (e.g., assigned to variables, passed as arguments, returned from other functions). This property enables the use of higher-order functions.

## Characteristics and Benefits
-   **Abstraction:** HOFs allow for abstracting common patterns of computation. Instead of writing similar loops or logic repeatedly, you can pass different functions to a HOF to achieve varied behavior.
-   **Code Reusability:** Generic HOFs can be reused with different specific functions.
-   **Modularity:** Helps in breaking down problems into smaller, more manageable functional pieces.
-   **Readability (often):** Can lead to more concise and expressive code, especially when combined with [[Python_Lambda_Functions|lambda functions]] or [[Python_Pure_Functions|pure functions]].
-   **Foundation for Functional Programming:** HOFs are a core concept in functional programming paradigms.

>[!question] What is "Pure function" and "Higher-order Function"? Give 3 examples For each of them.

*(Pure functions are covered in [[Python_Pure_Functions]]. This note focuses on Higher-Order Functions.)*

## Examples of Higher-Order Functions in Python

**1. Functions that Take Other Functions as Arguments:**

   a.  **`map(function, iterable, ...)` (Built-in):**
       -   Applies `function` to every item of `iterable` (or iterables) and returns an iterator of the results.
       ```python
       # Example: Square all numbers in a list of product quantities
       # product_quantities =
       # def square(x):
       #     return x * x
       # squared_quantities_iterator = map(square, product_quantities)
       # print(list(squared_quantities_iterator)) # Output:

       # Using a lambda function with map
       # prices = 
       # discounted_prices = map(lambda p: p * 0.9, prices) # 10% discount
       # print(list(discounted_prices))
       ```
       Here, `map` is a HOF because it takes the `square` function (or a lambda function) as an argument.

   b.  **`filter(function, iterable)` (Built-in):**
       -   Constructs an iterator from elements of `iterable` for which `function` returns true.
       ```python
       # Example: Filter out low product ratings
       # ratings = [4.5, 2.0, 3.8, 5.0, 1.5, 4.2]
       # def is_high_rating(rating):
       #     return rating >= 4.0
       # high_ratings_iterator = filter(is_high_rating, ratings)
       # print(list(high_ratings_iterator)) # Output: [4.5, 5.0, 4.2]

       # Using a lambda function with filter
       # product_names = ["Laptop X1", "Mouse Pad", "Keyboard Pro", "USB Cable"]
       # long_product_names = filter(lambda name: len(name) > 10, product_names)
       # print(list(long_product_names)) # Output: ['Keyboard Pro', 'Webcam Adapter'] (if Webcam Adapter was there)
       ```
       `filter` is a HOF because it takes `is_high_rating` (or a lambda) as an argument.

   c.  **Custom HOF for applying an operation:**
       ```python
       # def apply_operation_to_list(data_list, operation_func):
       #     """Applies a given operation_func to each element of data_list."""
       #     result = []
       #     for item in data_list:
       #         result.append(operation_func(item))
       #     return result

       # def double(x): return x * 2
       # def to_uppercase(s): return s.upper()

       # numbers = 
       # product_names = ["widget", "gadget"]
       
       # doubled_numbers = apply_operation_to_list(numbers, double)
       # print(f"Doubled numbers: {doubled_numbers}") # Output:
       # uppercased_names = apply_operation_to_list(product_names, to_uppercase)
       # print(f"Uppercased names: {uppercased_names}") # Output: ['WIDGET', 'GADGET']
       ```
       `apply_operation_to_list` is a HOF because it takes `operation_func` as an argument.

**2. Functions that Return Other Functions:**

   a.  **Creating a Multiplier Function (Factory Function):**
       ```python
       # def create_multiplier(factor):
       #     """Returns a new function that multiplies its argument by 'factor'."""
       #     def multiplier(number):
       #         return number * factor
       #     return multiplier # Returns the inner 'multiplier' function

       # doubler = create_multiplier(2) # doubler is now a function: lambda x: x * 2
       # tripler = create_multiplier(3) # tripler is now a function: lambda x: x * 3

       # print(f"doubler(5): {doubler(5)}")   # Output: 10
       # print(f"tripler(5): {tripler(5)}")   # Output: 15
       # print(f"doubler(10): {doubler(10)}") # Output: 20
       ```
       `create_multiplier` is a HOF because it returns the `multiplier` function. This also demonstrates a [[Python_Nested_Functions_Closures|closure]].

   b.  **Creating a Power Function Generator:**
       ```python
       # def power_generator(exponent):
       #     """Returns a function that raises its argument to the given exponent."""
       #     def to_the_power_of(base):
       #         return base ** exponent
       #     return to_the_power_of

       # square_func = power_generator(2)
       # cube_func = power_generator(3)

       # print(f"square_func(4): {square_func(4)}") # Output: 16
       # print(f"cube_func(3): {cube_func(3)}")   # Output: 27
       ```
       `power_generator` is a HOF.

   c.  **[[Python_Decorators|Decorators]]:** Decorators are a common application of HOFs in Python. A decorator is a function that takes another function as an argument, adds some functionality to it (without explicitly modifying the original function's code), and returns the modified function or a new function.
       ```python
       # def simple_decorator(func_to_decorate):
       #     def wrapper_around_func():
       #         print("Something is happening before the function is called.")
       #         func_to_decorate()
       #         print("Something is happening after the function is called.")
       #     return wrapper_around_func

       # @simple_decorator # This is syntactic sugar for: say_whee = simple_decorator(say_whee)
       # def say_whee():
       #     print("Whee!")

       # say_whee()
       # Output:
       # Something is happening before the function is called.
       # Whee!
       # Something is happening after the function is called.
       ```
       `simple_decorator` is a HOF because it takes `func_to_decorate` as an argument and returns the `wrapper_around_func`.

Other built-in HOFs include `functools.reduce()`, and `sorted()` (when used with its `key` argument, which takes a function).

Higher-order functions are a powerful feature that enables more abstract, flexible, and expressive programming styles in Python.

---