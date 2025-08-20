---
tags: [python, functions, decorators, metaprogramming, higher_order_functions, closures, concept, example]
aliases: [Python Decorator Syntax, decorator]
related:
  - "[[100_Python/Python_Functions/_Python_Functions_MOC|_Python_Functions_MOC]]"
  - "[[Python_Higher_Order_Functions]]" # Decorators are HOFs
  - "[[Python_Nested_Functions_Closures|Python Nested Functions and Closures]]" # Decorators rely on closures
  - "[[Python_Args_Kwargs|*args and **kwargs]]" # Often used in decorator wrappers
  - "[[functools_wraps|functools.wraps]]" # Placeholder for preserving metadata
worksheet: [WS18]
date_created: 2025-08-20
---
# Python: Decorators

**Decorators** in Python are a form of metaprogramming where you can modify or enhance functions or methods in a clean and readable way. A decorator is essentially a [[Python_Higher_Order_Functions|higher-order function]] that takes another function (the decorated function) as an argument, adds some functionality to it, and returns the modified function or a new function that wraps the original.

Decorators provide a way to separate concerns and add behavior (like logging, timing, access control, caching) to functions or methods without directly altering their source code.

>[!question] What are decorators in Python?
>Decorators are a design pattern in Python that allows a user to add new functionality to an existing object (typically a function or method) without modifying its structure. They are a form of metaprogramming where part of the program tries to modify another part of the program at compile time (or, more accurately in Python, at definition time).
>
>Syntactically, decorators are usually applied using the `@decorator_name` syntax placed immediately before the function definition.

## Basic Structure of a Decorator
A typical decorator involves:
1.  An **outer function** (the decorator itself) that takes a function (`func`) as an argument.
2.  An **inner function** (often called `wrapper` or `inner`) defined inside the decorator. This inner function is where the additional functionality is added before and/or after calling the original `func`.
3.  The decorator function **returns the inner function** object.
4.  This relies on [[Python_Nested_Functions_Closures|closures]] to ensure the `wrapper` function has access to `func` even after the decorator function has finished executing.

```python
def my_simple_decorator(func_to_decorate):
    # This is the decorator function
    print("Decorator: Initializing my_simple_decorator")

    def wrapper_function(*args, **kwargs):
        # This is the wrapper function that adds functionality
        print(f"Wrapper: Before calling {func_to_decorate.__name__}")
        result = func_to_decorate(*args, **kwargs) # Call the original function
        print(f"Wrapper: After calling {func_to_decorate.__name__}, result was {result}")
        return result # Return the result of the original function
    
    print("Decorator: Returning wrapper_function")
    return wrapper_function # Decorator returns the wrapper
```

## Applying a Decorator (Using `@` Syntax)
The `@` syntax is syntactic sugar for applying a decorator.

```python
# @my_simple_decorator
# def say_hello(name):
#     message = f"Hello, {name}!"
#     print(f"say_hello: Executing with '{name}'")
#     return message

# Call the decorated function
# response = say_hello("E-commerce World")
# print(f"Final response from decorated say_hello: {response}")
```
The above is equivalent to:
```python
# def say_hello_original(name):
#     message = f"Hello, {name}!"
#     print(f"say_hello_original: Executing with '{name}'")
#     return message

# say_hello_decorated = my_simple_decorator(say_hello_original)
# response = say_hello_decorated("E-commerce World")
# print(f"Final response from decorated say_hello: {response}")
```
When `say_hello` is defined with `@my_simple_decorator`, Python automatically calls `my_simple_decorator(say_hello)` and reassigns the name `say_hello` to the returned `wrapper_function`.

**Expected Output for the `@my_simple_decorator` example:**
```
Decorator: Initializing my_simple_decorator  # Happens once when say_hello is defined
Decorator: Returning wrapper_function       # Happens once when say_hello is defined

Wrapper: Before calling say_hello           # Happens each time decorated say_hello is called
say_hello: Executing with 'E-commerce World' # Original function execution
Wrapper: After calling say_hello, result was Hello, E-commerce World!
Final response from decorated say_hello: Hello, E-commerce World!
```

## Preserving Function Metadata (`functools.wraps`)
When you decorate a function, the wrapper function replaces the original function. This means metadata of the original function (like its name `__name__`, docstring `__doc__`, etc.) is lost.
The `functools.wraps` decorator can be used inside your custom decorator to copy these attributes from the original function to the wrapper function.

```python
import functools

def timing_decorator(func):
    @functools.wraps(func) # Preserves metadata of 'func'
    def wrapper(*args, **kwargs):
        import time
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' took {end_time - start_time:.4f} seconds to execute.")
        return result
    return wrapper

# @timing_decorator
# def calculate_product_recommendations(user_id, num_recommendations=5):
#     """Simulates calculating product recommendations."""
#     print(f"Calculating {num_recommendations} recommendations for user {user_id}...")
#     # Simulate some work
#     time.sleep(0.5) 
#     return [f"Product_{i}" for i in range(num_recommendations)]

# recommendations = calculate_product_recommendations("user123", num_recommendations=3)
# print(f"Recommendations: {recommendations}")
# print(f"Decorated function name: {calculate_product_recommendations.__name__}") # Will be 'calculate_product_recommendations'
# print(f"Decorated function docstring: {calculate_product_recommendations.__doc__}") # Will be the original docstring
```

## Decorators with Arguments
Decorators themselves can also accept arguments. This requires an extra level of nesting. The decorator with arguments must be a function that returns the actual decorator function.

```python
# def repeat_decorator(num_times): # Outer function takes decorator arguments
#     def actual_decorator(func):   # This is the actual decorator
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs): # This is the wrapper for the original func
#             results = []
#             for _ in range(num_times):
#                 results.append(func(*args, **kwargs))
#             return results
#         return wrapper
#     return actual_decorator

# @repeat_decorator(num_times=3)
# def get_product_id(base_id):
#     import random
#     return f"{base_id}-{random.randint(100,999)}"

# product_ids = get_product_id("PROD")
# print(f"Generated Product IDs (repeated 3 times): {product_ids}")
```

## Class-based Decorators
Decorators can also be implemented as classes by defining `__init__` and `__call__` methods.

## Common Use Cases for Decorators
-   **Logging:** Adding logging statements before/after function calls.
-   **Timing/Profiling:** Measuring the execution time of functions.
-   **Access Control/Authorization:** Checking permissions before executing a function (common in web frameworks like Flask, Django).
-   **Caching/Memoization:** Storing results of expensive function calls and returning cached result for same inputs.
-   **Input Validation/Transformation:** Validating or transforming function arguments.
-   **Registering Functions:** Registering functions with a central registry (e.g., for plugins, event handlers).
-   **Adding Attributes to Functions.**

Decorators are a powerful and Pythonic way to add functionality to functions and methods in a reusable and non-intrusive manner.

---

# Same?

---
tags: [python, programming_concept, decorators, functions, metaprogramming, functional_programming, concept, example]
aliases: [Decorators in Python, Python Decorator Syntax]
related:
  - "[[100_Python/_Python_MOC|Python MOC]]" # Assuming a Python MOC exists
  - "[[Python_Functions_as_First_Class_Objects]]" # Placeholder for a prerequisite concept
worksheet: [WS_Python_Advanced_1] # New worksheet identifier
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Python Decorators

## Definition
A **decorator** in Python is a design pattern that allows a user to add new functionality to an existing object (like a function or a class) without modifying its structure. Decorators are a form of metaprogramming; they take another function as an argument, add some functionality, and then return another function.

This is possible because in Python, functions are [[Python_Functions_as_First_Class_Objects|first-class objects]], meaning they can be passed as arguments, returned from other functions, and assigned to variables.

## Core Concept: A Function that Wraps Another Function
At its core, a decorator is "syntactic sugar" for a common pattern. The following two code snippets are equivalent:

**1. The "Syntactic Sugar" `@` Syntax (Preferred):**
```python
@my_decorator
def say_hello():
    print("Hello!")
```

**2. The Manual Wrapping Equivalent:**
```python
def say_hello():
    print("Hello!")

say_hello = my_decorator(say_hello)
```
In both cases, `my_decorator` is a function that takes the `say_hello` function as an argument and returns a new function (or a modified version of the original) which is then assigned back to the name `say_hello`.

## Creating a Simple Decorator
A decorator is a callable (usually a function) that returns a callable. The inner function, often called `wrapper`, is where the "decoration" happens.

```python
def simple_decorator(func):
    """A simple decorator that prints before and after the wrapped function."""
    def wrapper():
        print("Something is happening before the function is called.")
        func()  # Call the original function
        print("Something is happening after the function is called.")
    return wrapper

@simple_decorator
def greet():
    print("Whee! I am the original function.")

# Calling the decorated function
# greet()
```
**Output of `greet()`:**
```
Something is happening before the function is called.
Whee! I am the original function.
Something is happening after the function is called.
```

## Decorators with Arguments
What if the function we want to decorate takes arguments? The `wrapper` function needs to accept those arguments and pass them along. We use `*args` and `**kwargs` to handle any combination of positional and keyword arguments.

```python
def decorator_with_args(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}' with arguments:")
        print(f"  Positional args: {args}")
        print(f"  Keyword args: {kwargs}")
        result = func(*args, **kwargs) # Pass arguments to the original function
        print(f"Function '{func.__name__}' returned: {result}")
        return result
    return wrapper

@decorator_with_args
def add(a, b):
    return a + b

@decorator_with_args
def say_something(message, to="World"):
    return f"{message}, {to}!"

# Calling the decorated functions
# sum_result = add(5, 3)
# message_result = say_something("Hello", to="Python")
```

## Decorators That Accept Arguments
Sometimes, you want to pass arguments to the decorator itself. This requires an extra layer of nesting. The outer function takes the decorator's arguments and returns the actual decorator function.

```python
def repeat(num_times):
    """A decorator that repeats the execution of a function a given number of times."""
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result # Return the result of the last call
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def say_whee():
    print("Whee!")

# Calling the decorated function
# say_whee()
```
**Output of `say_whee()`:**
```
Whee!
Whee!
Whee!
```

## Preserving Function Metadata (`functools.wraps`)
When you decorate a function, you are replacing it with the `wrapper` function. This means you lose the original function's metadata (like its name `__name__`, docstring `__doc__`, etc.).

```python
# print(greet.__name__) # Without functools.wraps, this would print 'wrapper'
```

To fix this, use the `@functools.wraps` decorator inside your decorator.

```python
import functools

def decorator_that_preserves_metadata(func):
    @functools.wraps(func) # This is the key line
    def wrapper(*args, **kwargs):
        """This is the wrapper's docstring."""
        print("Wrapper is executing.")
        return func(*args, **kwargs)
    return wrapper

@decorator_that_preserves_metadata
def my_function_with_docstring():
    """This is the original function's docstring."""
    print("Original function is executing.")

# print(my_function_with_docstring.__name__) # Prints 'my_function_with_docstring'
# print(my_function_with_docstring.__doc__) # Prints "This is the original function's docstring."
```

## Common Use Cases for Decorators

[list2tab|#Decorator Use Cases]
- Logging
    -   **Use Case:** Log when a function is called, what arguments it received, and what it returned.
    -   **Example:**
        ```python
        import functools
        import logging

        # logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

        def log_function_call(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                # logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
                try:
                    result = func(*args, **kwargs)
                    # logging.info(f"{func.__name__} returned {result}")
                    return result
                except Exception as e:
                    # logging.error(f"Exception in {func.__name__}: {e}", exc_info=True)
                    raise
            return wrapper

        # @log_function_call
        # def calculate_price(base, tax_rate):
        #     return base * (1 + tax_rate)
        
        # calculate_price(100, 0.05)
        ```
- Timing / Performance Measurement
    -   **Use Case:** Measure how long a function takes to execute.
    -   **Example:**
        ```python
        import functools
        import time

        def timer(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                start_time = time.perf_counter()
                result = func(*args, **kwargs)
                end_time = time.perf_counter()
                run_time = end_time - start_time
                print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
                return result
            return wrapper

        # @timer
        # def process_large_data(size):
        #     # Simulate a time-consuming task
        #     time.sleep(size)
        #     return "Done"
        
        # process_large_data(1)
        ```
- Caching / Memoization
    -   **Use Case:** Store the results of expensive function calls and return the cached result when the same inputs occur again.
    -   **Example (using Python's built-in LRU cache):**
        ```python
        import functools
        import time

        # @functools.lru_cache(maxsize=None) # maxsize=None for unlimited cache
        # @timer # Decorators can be stacked
        # def slow_fibonacci(n):
        #     if n < 2:
        #         return n
        #     return slow_fibonacci(n-1) + slow_fibonacci(n-2)

        # print("Calculating Fibonacci(35)...")
        # slow_fibonacci(35) # First call is slow
        # print("\nCalculating Fibonacci(35) again...")
        # slow_fibonacci(35) # Second call is instantaneous due to cache
        ```
- Authorization & Access Control
    -   **Use Case:** In web frameworks (like Flask or Django), decorators are used to check if a user is logged in or has the necessary permissions before allowing them to execute the function that handles a web request.
    -   **Example (Conceptual Flask):**
        ```python
        # from functools import wraps
        # from flask import g, request, redirect, url_for

        # def login_required(f):
        #     @wraps(f)
        #     def decorated_function(*args, **kwargs):
        #         if g.user is None: # 'g' is a global context object in Flask
        #             return redirect(url_for('login', next=request.url))
        #         return f(*args, **kwargs)
        #     return decorated_function

        # @app.route('/profile')
        # @login_required
        # def user_profile():
        #     # This code only runs if the user is logged in
        #     return "This is the user profile page."
        ```
- Validation
    -   **Use Case:** Validate the arguments passed to a function before executing it.
    -   **Example (Simple type checking):**
        ```python
        import functools

        def validate_types(*type_args):
            def decorator_validate(func):
                @functools.wraps(func)
                def wrapper(*args, **kwargs):
                    for i, (arg, expected_type) in enumerate(zip(args, type_args)):
                        if not isinstance(arg, expected_type):
                            raise TypeError(f"Argument {i+1} of {func.__name__} must be {expected_type.__name__}, not {type(arg).__name__}")
                    return func(*args, **kwargs)
                return wrapper
            return decorator_validate

        # @validate_types(int, int)
        # def multiply(a, b):
        #     return a * b

        # multiply(5, 10) # OK
        # try:
        #     multiply(5, "10") # Raises TypeError
        # except TypeError as e:
        #     print(e)
        ```
- Class Decorators
    -   Decorators can also be applied to classes. They can be used to modify a class, for example, to implement the Singleton pattern or to automatically add methods.
    -   Python's `@dataclass` is a well-known class decorator that automatically generates methods like `__init__()`, `__repr__()`, etc.

Decorators are a powerful and expressive feature in Python that can help reduce code duplication and separate concerns, leading to cleaner and more maintainable code.

---
