---
tags:
  - python
  - variables
  - references
  - memory_model
  - objects
  - assignment
  - concept
aliases:
  - Python Variables
  - Python Object References
  - Python Assignment
related:
  - "[[100_Python/Python_Intro/_Python_Intro_MOC|_Python_Intro_MOC]]"
  - "[[Python_Memory_Management]]"
  - "[[Python_Data_Structures_MOC#Mutable and Immutable Objects|Mutable and Immutable Objects]]"
  - "[[Built_In_Functions_Python#id()|id() Built-in Function]]"
worksheet:
  - WS16
date_created: 2025-06-11
---
# Python: Variables and References

In Python, variables are not containers that hold values directly (like in C++ or Java for primitive types). Instead, **variables in Python are names (or identifiers) that act as references (or pointers) to objects stored in memory.**

Understanding this reference model is key to understanding how Python handles assignments, data sharing, and mutability.

## Objects, Names, and References
-   **Objects:** Everything in Python is an object (integers, floats, strings, lists, functions, classes, etc.). Each object has:
    -   An **identity** (a unique ID, accessible via `id()`, often related to its memory address).
    -   A **type** (e.g., `int`, `str`, `list`).
    -   A **value**.
-   **Names (Variables):** When you assign a value to a variable, you are essentially binding a name to an object.
    ```python
    x = 100 
    ```
    Here, `100` is an integer object created in memory. The name `x` is now a reference pointing to this integer object.
-   **References:** Variables store references to objects. Multiple names can refer to the same object.

    ```python
    a = [1, 2, 3] # 'a' refers to a list object
    b = a         # 'b' now refers to the *same* list object as 'a'

    print(f"id(a): {id(a)}")
    print(f"id(b): {id(b)}") # Will be the same as id(a)
    
    b.append(4)
    print(f"a after b.append(4): {a}") # Output: [1, 2, 3, 4]
    print(f"b after b.append(4): {b}") # Output: [1, 2, 3, 4]
    ```
    In the example above, modifying the list through `b` also affects `a` because both names point to the exact same list object in memory.

## Assignment
-   Assignment (`=`) in Python **binds a name to an object**.
-   If the object on the right-hand side already exists, the name on the left-hand side is made to refer to it.
-   If the object on the right-hand side is a new object (e.g., a literal like `200` or the result of an expression like `x + y`), that new object is created, and the name refers to it.

**Rebinding a Name:**
When you reassign a variable, you are changing which object the name refers to. The original object might still exist if other names refer to it, or it might become eligible for [[Python_Memory_Management|garbage collection]] if no names refer to it anymore.

```python
x = 10
print(f"x = {x}, id(x) = {id(x)}")

x = 20 # 'x' is now rebound to a new integer object '20'
print(f"x = {x}, id(x) = {id(x)}") # id(x) will be different

y = 10
print(f"y = {y}, id(y) = {id(y)}") # For small integers, Python often reuses objects (interning)
                                 # so id(y) might be the same as the original id(x) if x was 10.
```

## Impact on Mutable vs. Immutable Objects
The reference model has different implications for [[Python_Data_Structures_MOC#Mutable and Immutable Objects|mutable and immutable objects]]:

-   **Immutable Objects (e.g., numbers, strings, tuples):**
    -   Their value cannot be changed after creation.
    -   Operations that appear to modify an immutable object actually create a *new* object and rebind the name (if assigned).
    ```python
    s = "hello"
    original_id_s = id(s)
    s = s + " world" # Creates a NEW string object "hello world"
    print(f"s: '{s}', id(s): {id(s)}")
    print(f"original_id_s: {original_id_s}") # id(s) will be different from original_id_s
    
    num = 5
    original_id_num = id(num)
    num = num + 1 # Creates a NEW integer object 6
    print(f"num: {num}, id(num): {id(num)}")
    print(f"original_id_num: {original_id_num}")
    ```

    >[!question] What happens when you increment an `int`? Investigate with `id`.
    >When you increment an integer (which is immutable), Python typically creates a **new integer object** with the incremented value, and the variable name is rebound to this new object. The `id()` of the variable will change.
    >```python
    >my_int = 10
    >print(f"Initial my_int: {my_int}, id: {id(my_int)}")
    >
    >my_int = my_int + 1 # or my_int += 1
    >print(f"Incremented my_int: {my_int}, id: {id(my_int)}") # id will likely be different
    >
    >my_int_alias = my_int
    >print(f"my_int_alias: {my_int_alias}, id: {id(my_int_alias)}") # Same id as current my_int
    >
    >my_int += 1
    >print(f"Incremented my_int again: {my_int}, id: {id(my_int)}") # id likely changes again
    >print(f"my_int_alias after my_int changed: {my_int_alias}, id: {id(my_int_alias)}") # my_int_alias still points to the *previous* int object (11)
    >```
    >   **Note on Integer Interning:** For small integers (typically -5 to 256), Python often reuses existing objects in memory (interning) for efficiency. So, for these small integers, the `id()` might appear to be the same even after operations if the result falls within this pre-allocated range. However, the conceptual model of creating a new object for an immutable type upon "modification" still holds.

-   **Mutable Objects (e.g., lists, dictionaries, sets):**
    -   Their content can be changed in place after creation without creating a new object.
    -   If multiple names refer to the same mutable object, changes made through one name will be visible through all other names referring to that object.
    ```python
    list1 = [10, 20, 30]
    list2 = list1 # list2 refers to the same object as list1
    original_id_list1 = id(list1)

    list2.append(40) # Modifies the object in-place
    print(f"list1: {list1}") # Output: [10, 20, 30, 40]
    print(f"list2: {list2}") # Output: [10, 20, 30, 40]
    print(f"id(list1) after append: {id(list1)}") # id(list1) remains original_id_list1
    print(f"id(list2) after append: {id(list2)}") # Same as id(list1)
    ```

## Passing Arguments to Functions
When you pass variables to functions, you are passing their references (references to the objects they point to).
-   If an **immutable object** (like a number or string) is passed, the function receives a reference to it. If the function reassigns its local parameter name to a new object, this does not affect the original variable outside the function. If the function performs an operation that creates a new immutable object (e.g., `x = x + 1`), it's working with a new object.
-   If a **mutable object** (like a list) is passed, the function receives a reference to the *same object*. If the function modifies this object in-place (e.g., `my_list.append(item)`), the changes will be visible outside the function.

## `is` vs. `==`
This reference model is also key to understanding the difference between `is` and `==` (covered in more detail in [[Python_Data_Structures_MOC#is vs. == (Identity vs. Equality)|`is` vs. `==`]]).
-   `is` checks if two names refer to the **same object** (i.e., have the same identity/memory address).
-   `==` checks if the **values** of the objects the names refer to are equal.

Understanding Python's variable and reference model is fundamental for writing correct and predictable Python code, especially when dealing with mutable data structures and function arguments.

---