---
tags:
  - python
  - functions
  - nested_functions
  - closures
  - nonlocal
  - scope
  - functional_programming
  - concept
  - example
aliases:
  - Nested Functions Python
  - Python Closures
  - Nonlocal Keyword Python
  - Enclosing Scope
related:
  - "[[100_Python/Python_Functions/_Python_Functions_MOC|_Python_Functions_MOC]]"
  - "[[Python_Scopes_Modules_MOC|Python Scopes (LEGB Rule)]]"
  - "[[Python_Decorators]]"
  - "[[Python_Higher_Order_Functions]]"
worksheet:
  - WS18
date_created: 2025-08-20
---
# Python: Nested Functions, Closures, and `nonlocal`

Python allows functions to be defined inside other functions. These are called **nested functions** or inner functions. Nested functions can lead to a powerful concept called **closures**.

## Nested Functions

A nested function is a function defined within another function (the enclosing function).
-   The nested function has access to variables in its own local scope as well as variables in the scope of its enclosing function (the **enclosing scope** or **nonlocal scope**).
-   The nested function is only directly accessible from within the enclosing function unless it is returned by the enclosing function.

**Example: Simple Nested Function**
```python
def outer_function(text_prefix):
    # text_prefix is in the enclosing scope of inner_function
    
    def inner_function(name):
        # name is local to inner_function
        print(f"{text_prefix}: {name}")

    inner_function("Alice")
    inner_function("Bob")

outer_function("Customer")
# Output:
# Customer: Alice
# Customer: Bob

# inner_function("Charlie") # This would raise NameError: name 'inner_function' is not defined
                          # because inner_function is local to outer_function
```

## Closures
A **closure** occurs when a nested function "remembers" and has access to the variables from its enclosing scope, even after the enclosing function has finished executing and returned. The nested function, along with its remembered enclosing scope, forms the closure.

This happens when the enclosing function returns the nested function object itself.

>[!question] What are the criteria that must be met to create closure in Python?
>To create a closure in Python, the following conditions must be met:
>1.  **Nested Function:** There must be a function defined inside another function (an outer function enclosing an inner function).
>2.  **Reference to Enclosing Scope:** The inner (nested) function must refer to one or more variables defined in the scope of its enclosing (outer) function. These are called "free variables" for the inner function.
>3.  **Outer Function Returns Inner Function:** The enclosing function must return the nested function object itself (not the result of calling the nested function).

**Example: Creating a Closure (Multiplier Factory)**
```python
def create_multiplier(factor): # Enclosing function
    # 'factor' is a free variable for the 'multiplier' function
    print(f"Creating multiplier with factor: {factor}")

    def multiplier(number): # Nested function
        # This function "remembers" the 'factor' from its enclosing scope
        return number * factor
    
    return multiplier # Return the nested function object

# Create specific multiplier functions (closures)
double = create_multiplier(2) # 'double' is a closure, remembers factor=2
triple = create_multiplier(3) # 'triple' is a closure, remembers factor=3

# Even though create_multiplier() has finished executing,
# 'double' and 'triple' still have access to their respective 'factor' values.
print(f"double(5): {double(5)}")   # Output: 10
print(f"triple(5): {triple(5)}")   # Output: 15

print(f"double(10): {double(10)}") # Output: 20
print(f"triple(10): {triple(10)}") # Output: 30

# Inspecting the closure (for advanced understanding)
# print(double.__closure__) 
# print(triple.__closure__)
# Each cell in __closure__ contains the remembered free variables.
```
In this example, `double` and `triple` are closures. Each instance of the `multiplier` function created by `create_multiplier` carries its own "memory" of the `factor` variable from the specific call to `create_multiplier` that created it.

## The `nonlocal` Keyword
By default, if you assign a value to a name inside a nested function, Python creates a new local variable within that nested function's scope. If you want to modify a variable that is in an enclosing function's scope (but not global), you must use the `nonlocal` keyword.

-   The `nonlocal` statement causes the listed identifiers to refer to previously bound variables in the nearest enclosing scope excluding globals.
-   Without `nonlocal`, assignment creates a new local variable, shadowing the enclosing scope's variable.

>[!question] How can you change the value of a non-local variable?
>You can change the value of a non-local variable (a variable in an enclosing function's scope, but not global) from within a nested function by declaring that variable as `nonlocal` inside the nested function.

**Example: Using `nonlocal` to modify an enclosing scope variable**
```python
def outer_counter():
    count = 0 # Variable in enclosing scope

    def increment():
        nonlocal count # Declare that we want to modify the 'count' from outer_counter
        count += 1
        print(f"Inner increment: count = {count}")
        return count
    
    def get_count():
        return count

    return increment, get_count # Return both functions as a tuple

# inc1, get1 = outer_counter()
# inc2, get2 = outer_counter() # Creates a SEPARATE counter instance

# inc1() # Modifies count within the first closure
# inc1()
# print(f"Count from first counter (get1): {get1()}") # Output: 2

# inc2() # Modifies count within the second, independent closure
# print(f"Count from second counter (get2): {get2()}") # Output: 1
# print(f"Count from first counter again (get1): {get1()}") # Still 2
```
If `nonlocal count` was omitted in `increment()`, assigning to `count` (e.g., `count = count + 1`) would create a new local variable `count` within `increment()`, and the `count` in `outer_counter` would remain unchanged, likely leading to an `UnboundLocalError` if `count` was read before this local assignment.

## Use Cases for Nested Functions and Closures
-   **Data Hiding and Encapsulation:** Closures can be used to create functions with persistent private state, similar to how instance variables work in classes, but more lightweight.
-   **Factory Functions:** Functions that generate and return other specialized functions (like `create_multiplier` or `power_generator` in [[Python_Higher_Order_Functions]]).
-   **[[Python_Decorators|Decorators]]:** Decorators extensively use nested functions and closures to wrap or modify the behavior of other functions.
-   **Callback Functions:** Creating callback functions that "remember" some context from where they were created.
-   **Implementing Delayed Evaluation or Currying (Partial Application):**
    ```python
    # def add_n(n):
    #     def adder(x):
    #         return x + n
    #     return adder
    # add_5 = add_n(5)
    # print(add_5(10)) # Output: 15
    ```

Nested functions and closures are powerful tools in Python that enable more sophisticated and elegant programming patterns, particularly in functional programming and for creating flexible, reusable code.

---

>[!question] What will the Following programs print? Explain:
>```python
>def multiply (num1): 
>  def inner (num2): 
>    return num1 * num2 
>  return inner
>
>m1 = multiply(1)
>print(m1(10))
>
>m2 = multiply(2)
>print(m2(10))
>
>m3 = multiply(3)
>print(m3(10))
>```
>
>**Explanation:**
>This code demonstrates the concept of **closures**.
>1.  The `multiply(num1)` function is a higher-order function. When called, it defines a nested function `inner(num2)` and then **returns the `inner` function object itself**.
>2.  The `inner` function forms a closure: it "remembers" the value of `num1` from the enclosing `multiply` function's scope at the time `inner` was created.
>
>-   **`m1 = multiply(1)`:**
>    -   `multiply` is called with `num1 = 1`.
>    -   The `inner` function is created, and it captures `num1 = 1` in its closure.
>    -   `m1` now refers to this specific instance of `inner` that "knows" `num1` is 1.
>    -   `print(m1(10))`: This calls `m1` (which is the `inner` function with `num1=1`) with `num2 = 10`. It returns `1 * 10 = 10`.
>-   **`m2 = multiply(2)`:**
>    -   `multiply` is called with `num1 = 2`.
>    -   A *new* `inner` function instance is created, capturing `num1 = 2`.
>    -   `m2` refers to this new `inner` function.
>    -   `print(m2(10))`: This calls `m2` (with `num1=2`) with `num2 = 10`. It returns `2 * 10 = 20`.
>-   **`m3 = multiply(3)`:**
>    -   `multiply` is called with `num1 = 3`.
>    -   Another *new* `inner` function instance is created, capturing `num1 = 3`.
>    -   `m3` refers to this third `inner` function.
>    -   `print(m3(10))`: This calls `m3` (with `num1=3`) with `num2 = 10`. It returns `3 * 10 = 30`.
>
>**Output:**
>```
>10
>20
>30
>```
>Each call to `multiply()` creates a new, independent closure for the `inner` function, each with its own remembered value of `num1`.

---