---
tags:
  - python
  - data_types
  - data_structures
  - mutable
  - immutable
  - concept
  - fundamental
aliases:
  - Mutable Objects Python
  - Immutable Objects Python
  - Python Mutability
related:
  - "[[100_Python/Python_Data_Structures/_Python_Data_Structures_MOC|_Python_Data_Structures_MOC]]"
  - "[[Python_References_Variables]]"
  - "[[Python_List]]"
  - "[[Python_Tuple]]"
  - "[[Python_Set_Frozenset|Python Set]]"
  - "[[Python_Dictionary]]"
  - "[[Python_Primitive_Types|Python Primitive Types (str, int, float, bool are immutable)]]"
worksheet:
  - WS17
date_created: 2025-06-11
---
# Python: Mutability and Immutability

In Python, objects can be broadly classified as either **mutable** or **immutable**. This distinction refers to whether an object's state (its value or contents) can be changed after it has been created. Understanding this is crucial for predicting how variables and data structures behave.

## Immutable Objects
-   **Definition:** An object whose internal state **cannot be changed** after it is created.
-   If you perform an operation that appears to "modify" an immutable object, Python actually creates a **new object** in memory with the new value, and the variable name (if reassigned) will then refer to this new object. The original object remains unchanged (and might be garbage collected if no other references point to it).
-   **Advantages:**
    -   **Predictability:** Since their value never changes, they are safer to use in situations where you don't want accidental modifications (e.g., as dictionary keys, elements in a set).
    -   **Hashing:** Immutable objects can be hashed, which is necessary for them to be used as keys in dictionaries or elements in sets.
    -   **Performance (Potentially):** Python can sometimes optimize operations or reuse immutable objects (e.g., string interning, small integer interning).

>[!question] List mutable and immutable objects in Python.

**Common Immutable Types in Python:**
-   **Numbers:** `int`, `float`, `complex`, `bool` (Booleans are a subclass of integers).
-   **Strings (`str`):** Sequences of characters.
-   **Tuples (`tuple`):** Ordered, fixed-size sequences.
-   **Frozen Sets (`frozenset`):** Immutable version of a set.
-   `None` (the `NoneType` object).
-   Bytes (`bytes`).

**Example (Immutable - String):**
```python
my_string = "hello"
print(f"Initial string: '{my_string}', ID: {id(my_string)}")

my_string = my_string + " world" # This creates a NEW string object
print(f"Modified string: '{my_string}', ID: {id(my_string)}") # ID will be different
```
The name `my_string` is rebound to a new string object "hello world". The original "hello" object might still exist if other references point to it or will be garbage collected.

## Mutable Objects
-   **Definition:** An object whose internal state **can be changed** in-place after it is created.
-   Modifying a mutable object does not create a new object; the same object in memory is altered.
-   If multiple variables refer to the same mutable object, changes made through one variable will be visible through all other variables referencing that object.
-   **Advantages:**
    -   **Efficiency for In-Place Changes:** Modifying large mutable objects in place can be more memory and computationally efficient than creating new objects for every change.
    -   **Flexibility:** Useful for data structures that need to grow, shrink, or have their contents altered dynamically.
-   **Caution:** Can lead to unexpected behavior if multiple parts of a program share and modify the same mutable object without awareness (aliasing issues).

**Common Mutable Types in Python:**
-   **Lists (`list`):** Ordered, dynamic sequences.
-   **Dictionaries (`dict`):** Collections of key-value pairs.
-   **Sets (`set`):** Unordered collections of unique items.
-   Most user-defined classes (objects) are mutable by default unless specifically designed to be immutable.
-   Byte Arrays (`bytearray`).

**Example (Mutable - List):**
```python
my_list =
print(f"Initial list: {my_list}, ID: {id(my_list)}")

alias_list = my_list # Both names refer to the same list object

my_list.append(4) # Modifies the list object in-place
print(f"Modified my_list: {my_list}, ID: {id(my_list)}") # ID remains the same
print(f"alias_list after modification: {alias_list}")   # Shows the same change
```
Here, `my_list` and `alias_list` point to the same object in memory. Modifying it via `my_list.append()` changes the object that `alias_list` also references.

## Implications
-   **Function Arguments:**
    -   When you pass an immutable object to a function, the function cannot change the original object outside its scope (unless it returns a new object and the caller reassigns).
    -   When you pass a mutable object to a function, the function can modify the object's contents in-place, and these changes will be visible outside the function.
-   **Default Arguments in Functions:** Using mutable default arguments (like `def func(my_list=[]):`) can lead to unexpected behavior because the default list object is created only once when the function is defined and is reused across calls.
-   **Copying:**
    -   For mutable objects, simple assignment (`new_list = old_list`) creates a new reference to the same object (shallow copy of the reference).
    -   To create a true independent copy, you need to perform a shallow copy (e.g., `new_list = old_list.copy()` or `new_list = old_list[:]`) or a deep copy (`import copy; new_list = copy.deepcopy(old_list)`) if the mutable object contains other mutable objects.

Understanding mutability is fundamental for writing correct and predictable Python code, especially when dealing with shared data and complex data structures.

---