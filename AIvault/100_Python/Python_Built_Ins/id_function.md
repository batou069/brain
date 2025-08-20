---
tags:
  - python
  - built_in_function
  - id
  - identity
  - memory
  - object
  - concept
aliases:
  - id()
  - object identity python
related:
  - "[[Built_In_Functions_Python]]"
  - "[[Python_References_Variables]]"
  - "[[Python_Data_Structures_Identity_vs_Equality|is operator]]"
  - "[[Python_Memory_Management]]"
worksheet:
  - WS17
date_created: 2025-08-20
---
# Python: `id(object)` Built-in Function

The `id()` built-in function returns the **"identity"** of an object. This identity is an integer which is guaranteed to be **unique and constant for this object during its lifetime**.

## Syntax```python
id(object)```
-   `object`: Any Python object.

## Return Value
-   An integer representing the unique identity of the object.

## Behavior and Interpretation
-   **Uniqueness:** No two objects that exist simultaneously will have the same `id()`.
-   **Constancy:** Once an object is created, its `id()` will not change as long as the object exists.
-   **Memory Address (CPython):** In CPython (the standard Python implementation), `id(object)` typically returns the memory address of the object. However, this is an implementation detail and should not be relied upon as being the memory address in other Python implementations or future CPython versions. The key guarantee is uniqueness and constancy during the object's lifetime.
-   **Object Lifetime:** If an object is destroyed (e.g., its reference count drops to zero and it's garbage collected), its `id()` value may be reused by a new object created later.

## Use Cases
1.  **Checking Object Identity (with `is` operator):**
    The primary use of `id()` is often indirect, through the `is` operator. The expression `a is b` is equivalent to `id(a) == id(b)`. It checks if `a` and `b` refer to the exact same object in memory.
    ```python
    list_a =
    list_b = list_a       # list_b now refers to the same object as list_a
    list_c =    # list_c refers to a new, separate list object with the same content

    print(f"id(list_a): {id(list_a)}")
    print(f"id(list_b): {id(list_b)}") # Same as id(list_a)
    print(f"id(list_c): {id(list_c)}") # Different from id(list_a)

    print(f"list_a is list_b: {list_a is list_b}") # True
    print(f"list_a == list_b: {list_a == list_b}") # True (values are equal)

    print(f"list_a is list_c: {list_a is list_c}") # False (different objects)
    print(f"list_a == list_c: {list_a == list_c}") # True (values are equal)
    ```

2.  **Understanding Variable Assignment and Mutability:**
    `id()` can be used to observe how [[Python_References_Variables|variable assignments]] and operations on [[Python_Mutability_Immutability|mutable vs. immutable objects]] affect object identities.
    ```python
    # Immutable type (integer)
    x = 10
    print(f"x = {x}, id(x) = {id(x)}")
    x = x + 1 # Creates a new integer object for 11, x is rebound
    print(f"x = {x}, id(x) = {id(x)}") # id(x) will likely change

    # Mutable type (list)
    my_list =
    print(f"my_list = {my_list}, id(my_list) = {id(my_list)}")
    my_list.append(30) # Modifies the list in-place
    print(f"my_list = {my_list}, id(my_list) = {id(my_list)}") # id(my_list) remains the same
    ```

3.  **Debugging:**
    In some debugging scenarios, checking `id()` values can help determine if different variables are unexpectedly pointing to the same mutable object, leading to unintended side effects.

## CPython Interning
For certain immutable objects, CPython may "intern" them, meaning it reuses existing objects with the same value to save memory and speed up comparisons.
-   **Small Integers:** Integers between -5 and 256 (inclusive) are typically interned.
    ```python
    a = 256
    b = 256
    print(f"a = {a}, id(a) = {id(a)}")
    print(f"b = {b}, id(b) = {id(b)}")
    print(f"a is b (for 256): {a is b}") # Often True due to interning

    c = 257
    d = 257
    print(f"c = {c}, id(c) = {id(c)}")
    print(f"d = {d}, id(d) = {id(d)}")
    print(f"c is d (for 257): {c is d}") # Often False (unless explicitly interned or specific interpreter behavior)
    ```
-   **Short Strings:** Some short strings may also be interned.

This interning behavior is an implementation detail and should not be relied upon for program correctness, but it can explain why `is` sometimes returns `True` for seemingly different immutable objects with the same value.

The `id()` function is a low-level tool that provides insight into Python's object model and memory management.

---