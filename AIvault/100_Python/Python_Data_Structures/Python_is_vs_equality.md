---
tags:
  - python
  - operators
  - identity
  - equality
  - is_operator
  - equality_operator
  - object
  - value
  - concept_comparison
aliases:
  - is vs ==
  - Python Identity vs Equality
  - Object Identity
  - Value Equality
related:
  - "[[Built_In_Functions_Python#id()|id() Built-in Function]]"
  - "[[Python_References_Variables]]"
  - "[[Python_Mutability_Immutability|Mutability and Immutability in Python]]"
worksheet:
  - WS17
date_created: 2025-08-20
---
# Python: `is` (Identity) vs. `==` (Equality)

In Python, it's crucial to understand the distinction between the `is` operator and the `==` operator, as they test for different kinds of "sameness."

>[!question] What is the difference between `==` and `is`?

## `==` (Equality Operator)
-   **Purpose:** Tests for **value equality**. It checks if the values of the two objects being compared are the same.
-   **How it Works:** When you use `a == b`, Python calls the `__eq__()` dunder method of the object `a` (i.e., `a.__eq__(b)`).
    -   For built-in types, `__eq__()` is implemented to compare their contents or numerical values.
    -   For user-defined classes, you can override `__eq__()` to define what it means for instances of your class to be considered equal in value. If not overridden, the default `__eq__()` (inherited from `object`) behaves like `is` (checks for identity).
-   **Return Value:** `True` if the values are considered equal, `False` otherwise.

**Example:**
```python
list1 = [1, 2, 3]
list2 = [1, 2, 3] # A different list object, but with the same content
list3 = list1     # list3 refers to the same object as list1

print(f"list1 value: {list1}")
print(f"list2 value: {list2}")
print(f"list3 value: {list3}")

# Value equality
print(f"list1 == list2: {list1 == list2}") # True, because their contents are the same
print(f"list1 == list3: {list1 == list3}") # True, because their contents are the same

str1 = "hello"
str2 = "hello"
print(f"str1 == str2: {str1 == str2}") # True
```

## `is` (Identity Operator)
-   **Purpose:** Tests for **object identity**. It checks if two variable names refer to the **exact same object** in memory.
-   **How it Works:** `a is b` is equivalent to `id(a) == id(b)`. It compares the memory addresses (or unique IDs) of the objects.
-   **Return Value:** `True` if both variables point to the same object, `False` otherwise.

**Example (Continuing from above):**
```python
list1 = [1, 2, 3]
list2 = [1, 2, 3] 
list3 = list1     

print(f"id(list1): {id(list1)}")
print(f"id(list2): {id(list2)}") # Different from id(list1)
print(f"id(list3): {id(list3)}") # Same as id(list1)

# Identity
print(f"list1 is list2: {list1 is list2}") # False, because they are different objects in memory
print(f"list1 is list3: {list1 is list3}") # True, because they refer to the same object

# For immutable types like small integers or short strings, Python may intern them
# (reuse the same object for identical values) for optimization.
a = 256
b = 256
print(f"a is b (for 256): {a is b}") # Often True due to interning

c = 257
d = 257
print(f"c is d (for 257): {c is d}") # Often False for larger integers (implementation dependent)

# None is a singleton object, so all references to None point to the same object
val1 = None
val2 = None
print(f"val1 is None: {val1 is None}") # True
print(f"val1 is val2: {val1 is val2}") # True
```

## Key Differences Summarized

[list2mdtable|#is vs. ==]
- Feature
    - `==` (Equality)
        - `is` (Identity)
- **What it checks**
    - Values of the objects are equal.
        - Variables refer to the exact same object in memory.
- **How it works**
    - Calls `obj1.__eq__(obj2)`.
        - Compares `id(obj1)` and `id(obj2)`.
- **Mutability**
    - Two different mutable objects (e.g., two lists) can be `==` if their contents are the same.
        - Two different mutable objects will never be `is` each other.
- **Immutability & Interning**
    - Compares values.
        - For small integers and some strings, Python's interning can make `is` return `True` even if they seem separately defined, because they point to the same pre-existing object. This should not be relied upon for correctness for arbitrary values.
- **Usage with `None`**
    - `x == None` works.
        - `x is None` is the **idiomatic and preferred** way to check for `None`. It's faster and more reliable because `None` is a singleton.

## When to Use Which
-   **Use `==` (and `!=`) when you want to compare the *values* or *contents* of objects.** This is the most common type of comparison.
    ```python
    # if user_input == "yes":
    # if my_list_of_products == expected_products:
    ```
-   **Use `is` (and `is not`) when you specifically want to check if two variables refer to the *exact same object instance*.**
    -   The most common and recommended use case for `is` is checking for **`None`**:
        ```python
        # if my_variable is None:
        #     print("Variable is not yet assigned a meaningful value.")
        # if my_variable is not None:
        #     # proceed
        ```
    -   Use with caution when comparing other immutable types like numbers or strings, as interning behavior can be implementation-dependent and might lead to unexpected results if you rely on `is` for value comparison. For value comparison of numbers and strings, always use `==`.
    -   Useful when dealing with mutable objects to see if changes to one variable will affect another (aliasing).

Understanding the difference between identity (`is`) and equality (`==`) is fundamental for writing correct Python code, especially when working with [[Python_References_Variables|references]] and [[Python_Mutability_Immutability|mutable objects]].

---