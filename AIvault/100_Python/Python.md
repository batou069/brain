
`````markdown

Filename: 100_Python/Python_Data_Structures/Python_dict_get.md
````markdown
[[Python_dict_get]]
`````

`````markdown

Filename: 100_Python/Python_Data_Structures/Python_dict_keys.md
````markdown
[[Python_dict_keys]]
`````

`````markdown

Filename: 100_Python/Python_Data_Structures/Python_dict_values.md
````markdown
[[Python_dict_values]]
`````

Understood, I will create more notes per reply to make progress faster. I'll continue with the Dictionary methods, then `pop()`/`popitem()` for lists and dictionaries, and then the built-ins for WS17.

---

`````markdown

Filename: 100_Python/Python_Data_Structures/Python_dict_items.md
````markdown
[[Python_dict_items]]
`````

`````markdown

Filename: 100_Python/Python_Data_Structures/Python_dict_update.md
````markdown
[[Python_dict_update]]
`````

`````markdown

Filename: 100_Python/Python_Data_Structures/Python_dict_pop.md
````markdown
[[Python_dict_pop]]
`````

`````markdown

Filename: 100_Python/Python_Data_Structures/Python_dict_popitem.md
````markdown
[[Python_dict_popitem]]
`````

This covers the main dictionary methods from WS17. Next, I will create the notes for the Built-Ins listed in WS17: `id()`, `is`, and `slice()`.

Okay, I will create the notes for the Built-Ins from WS17 (`id()`, `is`, `slice()`) and also the requested `Catalyst_Optimizer_Spark.md` note.

---

### Python Built-Ins (WS17)

`````markdown

Filename: 100_Python/Python_Built_Ins/Built_In_Functions_Python.md
````markdown
---
tags: [python, built_in_functions, core_python, utility, concept, summary]
aliases: [Python Built-in Functions, Standard Python Functions]
related:
  - "[[100_Python/_Python_Programming_MOC|_Python_Programming_MOC]]"
  # Individual function notes will be linked here
  - "[[Built_In_Functions_Python#id()|id()]]"
  - "[[Python_Data_Structures_Identity_vs_Equality|is operator]]" # 'is' is an operator, not a function, but related to id()
  - "[[Built_In_Functions_Python#slice()|slice()]]"
  - "[[Built_In_Functions_Python#len()|len()]]"
  - "[[Built_In_Functions_Python#max()|max()]]"
  - "[[Built_In_Functions_Python#min()|min()]]"
  - "[[Built_In_Functions_Python#print()|print()]]"
  - "[[Built_In_Functions_Python#type()|type()]]"
  - "[[Built_In_Functions_Python#input()|input()]]"
  - "[[Built_In_Functions_Python#range()|range()]]"
  - "[[Built_In_Functions_Python#sum()|sum()]]"
  - "[[Built_In_Functions_Python#sorted()|sorted()]]"
  - "[[Built_In_Functions_Python#reversed()|reversed()]]"
  - "[[Built_In_Functions_Python#enumerate()|enumerate()]]"
  - "[[Built_In_Functions_Python#zip()|zip()]]"
  - "[[Built_In_Functions_Python#map_function|map()]]"
  - "[[Built_In_Functions_Python#filter_function|filter()]]"
  - "[[Built_In_Functions_Python#isinstance()|isinstance()]]"
  - "[[Built_In_Functions_Python#issubclass()|issubclass()]]"
  - "[[Built_In_Functions_Python#globals()|globals()]]"
  - "[[Built_In_Functions_Python#locals()|locals()]]"
  - "[[Built_In_Functions_Python#abs()|abs()]]"
  - "[[Built_In_Functions_Python#round()|round()]]"
  - "[[Built_In_Functions_Python#pow()|pow()]]"
  - "[[Built_In_Functions_Python#open()|open()]]"
  # ... and many more
worksheet: [WS17, WS18, WS19, WS20, WS21] # Consolidating built-ins here
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Python: Built-in Functions Summary

Python comes with a number of functions and types that are built into it and are always available without needing to `import` any module. These **built-in functions** perform a variety of common tasks, from data type conversion and mathematical operations to input/output and introspection.

This note serves as a central point for some commonly discussed built-in functions. Individual detailed notes will be created for specific functions as needed.

## Key Built-in Functions (Selection)

[list2tab|#Common Built-ins]
- `id(object)`
    -   **Purpose:** Returns the "identity" of an object. This is an integer which is guaranteed to be unique and constant for this object during its lifetime. Two objects with non-overlapping lifetimes may have the same `id()` value.
    -   **Use:** Often used to check if two variables refer to the exact same object in memory (see [[Python_Data_Structures_Identity_vs_Equality|`is` operator]]).
    -   See [[Built_In_Functions_Python#id()|id() detailed note]].
- `len(s)`
    -   **Purpose:** Returns the length (the number of items) of an object `s`.
    -   **Use:** Works on sequences (string, list, tuple), mappings (dictionary), and sets.
    -   See [[Built_In_Functions_Python#len()|len() detailed note]].
- `type(object)`
    -   **Purpose:** Returns the type of an object.
    -   **Use:** For introspection and type checking (though `isinstance()` is often preferred for checking types).
    -   See [[Built_In_Functions_Python#type()|type() detailed note]].
- `print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)`
    -   **Purpose:** Prints objects to the text stream file, separated by `sep` and followed by `end`.
    -   See [[Built_In_Functions_Python#print()|print() detailed note]].
- `input([prompt])`
    -   **Purpose:** Reads a line from input (usually user from keyboard), converts it to a string (stripping a trailing newline), and returns that.
    -   See [[Built_In_Functions_Python#input()|input() detailed note]].
- Type Conversion Functions
    -   `int(x, base=10)`, `float(x)`, `str(object)`, `bool(x)`: Convert values to integer, float, string, or boolean.
    -   `list(iterable)`, `tuple(iterable)`, `set(iterable)`, `dict(...)`: Convert iterables to collection types.
    -   See [[Python_Type_Casting]].
- `range(stop)` / `range(start, stop[, step])`
    -   **Purpose:** Returns an immutable sequence object representing a sequence of numbers. Commonly used for looping a specific number of times in `for` loops.
    -   See [[Built_In_Functions_Python#range()|range() detailed note]].
- `max(...)` / `min(...)`
    -   **Purpose:** Return the largest/smallest item in an iterable or the largest/smallest of two or more arguments.
    -   See [[Built_In_Functions_Python#max()|max()]] and [[Built_In_Functions_Python#min()|min() detailed notes]].
- `sum(iterable, /, start=0)`
    -   **Purpose:** Sums `start` and the items of an `iterable` from left to right and returns the total. Items are usually numbers.
    -   See [[Built_In_Functions_Python#sum()|sum() detailed note]].
- `sorted(iterable, *, key=None, reverse=False)`
    -   **Purpose:** Returns a new sorted list from the items in `iterable`.
    -   See [[Built_In_Functions_Python#sorted()|sorted() detailed note]].
- `reversed(seq)`
    -   **Purpose:** Returns a reverse iterator. `seq` must be an object which has a `__reversed__()` method or supports the sequence protocol.
    -   See [[Built_In_Functions_Python#reversed()|reversed() detailed note]].
- `enumerate(iterable, start=0)`
    -   **Purpose:** Returns an enumerate object. `iterable` must be a sequence, an iterator, or some other object which supports iteration. Yields pairs of (count, value).
    -   See [[Built_In_Functions_Python#enumerate()|enumerate() detailed note]].
- `zip(*iterables, strict=False)`
    -   **Purpose:** Iterate over several iterables in parallel, producing tuples with an item from each one.
    -   See [[Built_In_Functions_Python#zip()|zip() detailed note]].
- `map(function, iterable, ...)`
    -   **Purpose:** Returns an iterator that applies `function` to every item of `iterable`, yielding the results.
    -   See [[Built_In_Functions_Python#map_function|map() detailed note]].
- `filter(function, iterable)`
    -   **Purpose:** Constructs an iterator from elements of `iterable` for which `function` returns true.
    -   See [[Built_In_Functions_Python#filter_function|filter() detailed note]].
- `isinstance(object, classinfo)`
    -   **Purpose:** Returns `True` if the `object` argument is an instance of the `classinfo` argument, or of a (direct, indirect or virtual) subclass thereof.
    -   See [[Built_In_Functions_Python#isinstance()|isinstance() detailed note]].
- `issubclass(class, classinfo)`
    -   **Purpose:** Returns `True` if `class` is a subclass (direct, indirect or virtual) of `classinfo`.
    -   See [[Built_In_Functions_Python#issubclass()|issubclass() detailed note]].
- `globals()`
    -   **Purpose:** Returns a dictionary representing the current global symbol table.
    -   See [[Built_In_Functions_Python#globals()|globals() detailed note]].
- `locals()`
    -   **Purpose:** Returns a dictionary representing the current local symbol table.
    -   See [[Built_In_Functions_Python#locals()|locals() detailed note]].
- `abs(x)`
    -   **Purpose:** Returns the absolute value of a number.
    -   See [[Built_In_Functions_Python#abs()|abs() detailed note]].
- `round(number[, ndigits])`
    -   **Purpose:** Returns `number` rounded to `ndigits` precision after the decimal point.
    -   See [[Built_In_Functions_Python#round()|round() detailed note]].
- `pow(base, exp[, mod])`
    -   **Purpose:** Returns `base` to the power `exp`; if `mod` is present, returns `base` to the power `exp`, modulo `mod`.
    -   See [[Built_In_Functions_Python#pow()|pow() detailed note]].
- `open(file, mode='r', ...)`
    -   **Purpose:** Opens a file and returns a corresponding file object.
    -   See [[Built_In_Functions_Python#open()|open() detailed note]] and [[100_Python/Python_Files_Context_Managers/_Python_Files_Context_Managers_MOC|Files & Context Managers]].
- `slice(stop)` / `slice(start, stop[, step])`
    -   **Purpose:** Returns a slice object representing the set of indices specified by `range(start, stop, step)`.
    -   See [[Built_In_Functions_Python#slice()|slice() detailed note]].

This list is not exhaustive but covers many of the most frequently used built-in functions. The official Python documentation provides a complete list and detailed descriptions.

---
`````

`````markdown

Filename: 100_Python/Python_Built_Ins/id_function.md
````markdown
---
tags: [python, built_in_function, id, identity, memory, object, concept]
aliases: [id(), object identity python]
related:
  - "[[Built_In_Functions_Python]]"
  - "[[Python_References_Variables]]"
  - "[[Python_Data_Structures_Identity_vs_Equality|is operator]]" # 'is' compares ids
  - "[[Python_Memory_Management]]"
worksheet: [WS17]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
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
`````

`````markdown

Filename: 100_Python/Python_Data_Structures/Python_is_vs_equality.md
````markdown
---
tags: [python, operators, identity, equality, is_operator, equality_operator, object, value, concept_comparison]
aliases: [is vs ==, Python Identity vs Equality, Object Identity, Value Equality]
related:
  - "[[Built_In_Functions_Python#id()|id() Built-in Function]]"
  - "[[Python_References_Variables]]"
  - "[[Python_Mutability_Immutability|Mutability and Immutability in Python]]"
worksheet: [WS17]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
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
`````

`````markdown

Filename: 100_Python/Python_Built_Ins/slice_function.md
````markdown
---
tags: [python, built_in_function, slice, sequence, slicing, indexing, concept, example]
aliases: [slice(), Python Slice Object]
related:
  - "[[Built_In_Functions_Python]]"
  - "[[Python_Slicing]]" # Main note on slicing notation
  - "[[Python_List]]"
  - "[[Python_Tuple]]"
  - "[[Python_Primitive_Types|String (str)]]"
worksheet: [WS17]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Python: `slice()` Built-in Function

The `slice()` built-in function returns a **slice object** representing a set of indices specified by `range(start, stop, step)`. This slice object can then be used to [[Python_Slicing|slice]] sequences like lists, tuples, and strings.

While direct slicing notation (e.g., `my_list[start:stop:step]`) is far more common and generally more readable for most use cases, the `slice()` function can be useful in situations where slice parameters need to be passed around programmatically or stored.

## Syntax
`slice(stop)`
`slice(start, stop, step=None)`

-   `stop`: The index before which the slicing stops (exclusive).
-   `start` (optional): The starting index of the slice. Defaults to `None` (beginning of the sequence).
-   `step` (optional): The step of the slice. Defaults to `None` (which means a step of 1).

## Return Value
-   A **slice object**.

## Behavior
-   The `slice()` function itself doesn't perform the slicing. It creates a slice object that *describes* how to slice a sequence.
-   This slice object can then be used inside square brackets `[]` with a sequence.

>[!question] Explain slicing in Python. How many arguments does slicing need? How many arguments can it receive?
>
>[[Python_Slicing|Slicing]] is a feature in Python that allows you to access a subsequence (a "slice") of an ordered sequence type (like lists, tuples, strings, and even NumPy arrays).
>
>**Standard Slicing Notation `sequence[start:stop:step]`:**
>-   This is the most common way to perform slicing.
>-   `start`: The index where the slice begins (inclusive). If omitted, defaults to the beginning of the sequence (index 0).
>-   `stop`: The index where the slice ends (exclusive). If omitted, defaults to the end of the sequence.
>-   `step`: The amount to increment the index by. If omitted, defaults to 1. A negative step reverses the slice.
>
>**`slice()` Function Arguments:**
>The `slice()` function itself can be called in a few ways to create a slice object:
>1.  **`slice(stop)`:**
>    -   Takes **one argument**.
>    -   Creates a slice object equivalent to `[None:stop:None]` or `[:stop]`.
>2.  **`slice(start, stop, step=None)`:**
>    -   Takes **two or three arguments**.
>    -   `start` and `stop` are required if providing more than one argument.
>    -   `step` is optional and defaults to `None` (which means a step of 1 when used in slicing).
>    -   Creates a slice object equivalent to `[start:stop:step]`.
>
>So, the `slice()` function can receive **one, two, or three** arguments.
>
>The slicing operation itself (using `[]` with a sequence) conceptually "needs" up to three parameters (`start`, `stop`, `step`), but all are optional and have defaults.

## Examples

**1. Creating and using slice objects:**
```python
product_ids = ["P001", "P002", "P003", "P004", "P005", "P006"]

# Equivalent to product_ids[0:3:1] or product_ids[:3]
s1 = slice(3) 
print(f"Slice object s1: {s1}")
print(f"product_ids[s1]: {product_ids[s1]}") # Output: ['P001', 'P002', 'P003']

# Equivalent to product_ids[1:5:1] or product_ids[1:5]
s2 = slice(1, 5)
print(f"Slice object s2: {s2}")
print(f"product_ids[s2]: {product_ids[s2]}") # Output: ['P002', 'P003', 'P004', 'P005']

# Equivalent to product_ids[0:len(product_ids):2] or product_ids[::2]
s3 = slice(None, None, 2) # None for start/stop means full range
print(f"Slice object s3: {s3}")
print(f"product_ids[s3]: {product_ids[s3]}") # Output: ['P001', 'P003', 'P005']

# Equivalent to product_ids[::-1] (reverse)
s4 = slice(None, None, -1)
print(f"Slice object s4: {s4}")
print(f"product_ids[s4]: {product_ids[s4]}")
```

**2. Storing and reusing slice objects:**
This can be useful if you need to apply the same slicing logic multiple times or pass slicing parameters around.
```python
# Define slice parameters for different parts of a report
header_slice = slice(0, 1)
body_slice = slice(1, -1) # All but first and last
footer_slice = slice(-1, None) # Only the last item

data_report_lines = [
    "Report Title: Q3 Sales",
    "Data point 1: ...",
    "Data point 2: ...",
    "Data point 3: ...",
    "Summary: Sales increased."
]

print(f"\nHeader: {data_report_lines[header_slice]}")
print(f"Body:   {data_report_lines[body_slice]}")
print(f"Footer: {data_report_lines[footer_slice]}")
```

## Slice Object Attributes
A slice object has attributes `start`, `stop`, and `step` which can be inspected:
```python
my_slice = slice(10, 20, 2)
print(f"\nSlice object: {my_slice}")
print(f"my_slice.start: {my_slice.start}") # Output: 10
print(f"my_slice.stop: {my_slice.stop}")   # Output: 20
print(f"my_slice.step: {my_slice.step}")   # Output: 2

# Slice object with default start and step
another_slice = slice(5)
print(f"another_slice.start: {another_slice.start}") # Output: None
print(f"another_slice.stop: {another_slice.stop}")   # Output: 5
print(f"another_slice.step: {another_slice.step}")   # Output: None
```

While the direct slicing notation `seq[start:stop:step]` is more common for immediate use, the `slice()` function provides a way to create reusable slice objects, which can be beneficial in more programmatic or dynamic slicing scenarios, such as when slice parameters are determined at runtime or passed as arguments to functions.

---
`````

This completes the built-in functions from WS17 (`id()`, `is` (as `Python_is_vs_equality.md`), `slice()`). The functions `max()`, `min()`, `len()` were covered in `Python_list_max_min_len.md` in the context of lists, but they are general built-ins, so I've also created placeholders for them in `Built_In_Functions_Python.md` and will link them there.

Next, I will address the remaining questions from WS17 that might not have been fully covered yet, primarily focusing on:
-   "Can you delete an element inside a data structure?" (will create `Python_Data_Structures_Deleting_Elements.md`)
-   "Can you mix all types of elements in all data structures?" (will create `Python_Data_Structures_Type_Mixing.md`)
-   "List the ordered and the unordered data structures." (will create `Python_Data_Structures_Ordered_Unordered.md`)

Then I will move to WS18 - Functions.

---

`````markdown

Filename: 100_Python/Python_Data_Structures/Python_Data_Structures_Deleting_Elements.md
````markdown
---
tags: [python, data_structures, list, dictionary, set, delete, remove, pop, mutable, concept]
aliases: [Deleting from Python Data Structures, Removing Elements Python]
related:
  - "[[100_Python/Python_Data_Structures/_Python_Data_Structures_MOC|_Python_Data_Structures_MOC]]"
  - "[[Python_List_Methods]]"
  - "[[Python_Dictionary_Methods]]"
  - "[[Python_Set_Methods]]" # Placeholder for Set methods summary
  - "[[Python_Mutability_Immutability|Mutability and Immutability in Python]]"
worksheet: [WS17]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Python: Deleting Elements from Data Structures

Python's built-in [[Python_Mutability_Immutability|mutable data structures]] (lists, dictionaries, sets) provide various ways to remove or delete elements. Immutable data structures (tuples, frozensets, strings, numbers) cannot have elements removed from them in-place; any operation that "removes" an element from an immutable structure actually creates a new object without that element.

>[!question] Can you delete an element inside a data structure?
>Yes, you can delete elements from **mutable** data structures like lists, dictionaries, and sets. You cannot directly delete elements from immutable data structures like tuples or strings in-place; instead, you would create a new object excluding the desired element(s).

## Deleting from Lists (`list`)
Lists offer several ways to remove elements:

[list2tab|#List Deletion Methods]
- `list.remove(value)`
    -   **How:** Removes the **first occurrence** of the specified `value`.
    -   **Raises:** `ValueError` if the value is not found.
    -   **Example:**
        ```python
        product_cart = ["apple", "banana", "cherry", "banana"]
        product_cart.remove("banana") # Removes the first "banana"
        print(product_cart) # Output: ['apple', 'cherry', 'banana']
        ```
    -   See [[Python_list_remove]].
- `list.pop(index=-1)`
    -   **How:** Removes and returns the element at the specified `index`. If no index is given, it removes and returns the last element (LIFO behavior).
    -   **Raises:** `IndexError` if the list is empty or the index is out of range.
    -   **Example:**
        ```python
        product_cart = ["apple", "banana", "cherry"]
        removed_item = product_cart.pop(0) # Removes "apple"
        print(f"Removed: {removed_item}, Cart: {product_cart}") # Output: Removed: apple, Cart: ['banana', 'cherry']
        last_item = product_cart.pop() # Removes "cherry"
        print(f"Removed: {last_item}, Cart: {product_cart}") # Output: Removed: cherry, Cart: ['banana']
        ```
    -   See [[Python_list_pop]].
- `del list[index]`
    -   **How:** The `del` statement removes the element at the specified `index`.
    -   **Raises:** `IndexError` if the index is out of range.
    -   **Example:**
        ```python
        product_cart = ["apple", "banana", "cherry"]
        del product_cart[1] # Removes "banana"
        print(product_cart) # Output: ['apple', 'cherry']
        ```
- `del list[start:stop:step]` (Slice Deletion)
    -   **How:** The `del` statement can remove a slice of elements.
    -   **Example:**
        ```python
        numbers = [10, 20, 30, 40, 50, 60]
        del numbers[1:4] # Removes elements at index 1, 2, 3 (i.e., 20, 30, 40)
        print(numbers) # Output: [10, 50, 60]
        ```
- `list.clear()`
    -   **How:** Removes all elements from the list, making it empty.
    -   **Example:**
        ```python
        product_cart = ["apple", "banana"]
        product_cart.clear()
        print(product_cart) # Output: []
        ```
    -   See [[Python_list_clear]].

## Deleting from Dictionaries (`dict`)
Dictionaries store key-value pairs. Deletion is typically done by key.

[list2tab|#Dictionary Deletion Methods]
- `dict.pop(key, default=RAISE_ERROR)`
    -   **How:** Removes the item with the specified `key` and returns its value.
    -   **Raises/Returns:** If `key` is not found, it returns `default` if provided, otherwise raises `KeyError`.
    -   **Example:**
        ```python
        product_info = {"name": "Laptop", "price": 1200, "stock": 50}
        price_value = product_info.pop("price")
        print(f"Removed price: {price_value}, Info: {product_info}") 
        # Output: Removed price: 1200, Info: {'name': 'Laptop', 'stock': 50}
        
        color = product_info.pop("color", "Not Available") # Key "color" doesn't exist
        print(f"Removed color: {color}, Info: {product_info}")
        # Output: Removed color: Not Available, Info: {'name': 'Laptop', 'stock': 50}
        ```
    -   See [[Python_dict_pop]].
- `dict.popitem()`
    -   **How:** Removes and returns an arbitrary (key, value) pair. In Python 3.7+, this is LIFO (Last-In, First-Out).
    -   **Raises:** `KeyError` if the dictionary is empty.
    -   **Example:**
        ```python
        product_info = {"name": "Laptop", "price": 1200, "stock": 50}
        key, value = product_info.popitem() # Removes ('stock', 50) in Python 3.7+
        print(f"Popped item: ({key}, {value}), Info: {product_info}")
        ```
    -   See [[Python_dict_popitem]].
- `del dict[key]`
    -   **How:** The `del` statement removes the item with the specified `key`.
    -   **Raises:** `KeyError` if the key is not found.
    -   **Example:**
        ```python
        product_info = {"name": "Laptop", "price": 1200, "stock": 50}
        if "stock" in product_info:
            del product_info["stock"]
        print(f"Info after del 'stock': {product_info}") # Output: {'name': 'Laptop', 'price': 1200}
        ```
- `dict.clear()`
    -   **How:** Removes all items from the dictionary, making it empty.
    -   **Example:**
        ```python
        product_info = {"name": "Laptop", "price": 1200}
        product_info.clear()
        print(f"Info after clear: {product_info}") # Output: {}
        ```

## Deleting from Sets (`set`)
Sets store unique, unordered elements.

[list2tab|#Set Deletion Methods]
- `set.remove(element)`
    -   **How:** Removes the specified `element` from the set.
    -   **Raises:** `KeyError` if the element is not found.
    -   **Example:**
        ```python
        product_tags = {"electronics", "sale", "new", "gadget"}
        product_tags.remove("sale")
        print(product_tags) # Output example: {'new', 'gadget', 'electronics'}
        ```
- `set.discard(element)`
    -   **How:** Removes the specified `element` from the set if it is present.
    -   **Raises:** Does **not** raise an error if the element is not found.
    -   **Example:**
        ```python
        product_tags = {"electronics", "new", "gadget"}
        product_tags.discard("new")
        print(product_tags) # Output example: {'gadget', 'electronics'}
        product_tags.discard("obsolete") # "obsolete" is not in the set, no error
        print(product_tags) # Output example: {'gadget', 'electronics'}
        ```
- `set.pop()`
    -   **How:** Removes and returns an **arbitrary** element from the set. Since sets are unordered, you cannot predict which element will be removed.
    -   **Raises:** `KeyError` if the set is empty.
    -   **Example:**
        ```python
        product_tags = {"electronics", "new", "gadget"}
        removed_tag = product_tags.pop()
        print(f"Removed tag: {removed_tag}, Remaining tags: {product_tags}")
        ```
- `set.clear()`
    -   **How:** Removes all elements from the set, making it empty.
    -   **Example:**
        ```python
        product_tags = {"electronics", "new"}
        product_tags.clear()
        print(product_tags) # Output: set()
        ```

## Immutable Structures (Tuples, Strings, Frozensets)
You cannot directly delete elements from immutable structures in-place. To achieve a similar effect, you typically create a new object by slicing or filtering out the unwanted elements.

**Example (Tuple):**
```python
my_tuple = (10, 20, 30, 40, 50)
# To "remove" 30, create a new tuple without it:
new_tuple = my_tuple[:2] + my_tuple[3:] # Concatenate slices
print(f"New tuple after 'removing' 30: {new_tuple}") # Output: (10, 20, 40, 50)
```

Understanding how to delete elements is crucial for managing the state of mutable data structures in Python.

---
`````

`````markdown

Filename: 100_Python/Python_Data_Structures/Python_Data_Structures_Type_Mixing.md
````markdown
---
tags: [python, data_structures, list, tuple, set, dictionary, data_types, heterogeneous, concept]
aliases: [Mixed Types in Python Collections, Heterogeneous Data Structures Python]
related:
  - "[[100_Python/Python_Data_Structures/_Python_Data_Structures_MOC|_Python_Data_Structures_MOC]]"
  - "[[Python_List]]"
  - "[[Python_Tuple]]"
  - "[[Python_Set_Frozenset|Python Set and Frozenset]]"
  - "[[Python_Dictionary]]"
  - "[[Python_Primitive_Types]]"
worksheet: [WS17]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Python: Mixing Element Types in Data Structures

A key feature of Python's built-in collection types like lists, tuples, sets, and dictionaries is their ability to hold elements of different data types. This makes them very flexible for representing diverse data.

>[!question] Can you mix all types of elements in all data structures?

**General Answer:** Yes, for the most part, Python's primary built-in data structures (`list`, `tuple`, `dict` values, `set` elements) allow you to store items of mixed data types. However, there are important caveats, especially concerning mutability for dictionary keys and set elements.

[list2tab|#Type Mixing by Data Structure]
- [[Python_List|Lists (`list`)]]
    -   **Can Mix Types?** Yes, absolutely.
    -   **Explanation:** Lists are ordered sequences and can store any combination of Python objects, regardless of their type.
    -   **Example (Product details with mixed types):**
        ```python
        product_A_details = [
            "SuperWidget X1000",  # str (name)
            "SWX1000",            # str (SKU)
            49.99,                # float (price)
            150,                  # int (stock_count)
            True,                 # bool (is_available)
            ["electronics", "gadget", "new"] # list (tags)
        ]
        print(f"Product A details list: {product_A_details}")
        for item in product_A_details:
            print(f"- Item: {item}, Type: {type(item)}")
        ```
- [[Python_Tuple|Tuples (`tuple`)]]
    -   **Can Mix Types?** Yes, absolutely.
    -   **Explanation:** Tuples are ordered, immutable sequences. Like lists, they can store elements of any data type.
    -   **Example (Customer record):**
        ```python
        customer_record = (
            1025,                     # int (customer_id)
            "Alice Wonderland",       # str (name)
            30,                       # int (age)
            "alice@example.com",      # str (email)
            ("123 Main St", "Anytown") # tuple (address components)
        )
        print(f"\nCustomer record tuple: {customer_record}")
        ```
- [[Python_Dictionary|Dictionaries (`dict`)]]
    -   **Keys:**
        -   **Can Mix Types?** Yes, keys can be of different immutable types within the same dictionary.
        -   **Constraint:** Dictionary keys **must be of an immutable (hashable) type**. This includes numbers, strings, tuples (if all their elements are immutable), and frozensets. You cannot use mutable types like lists or other dictionaries as keys.
    -   **Values:**
        -   **Can Mix Types?** Yes, absolutely. Values associated with keys can be of any data type, and different keys can have values of different types.
    -   **Example (E-commerce order information):**
        ```python
        order_info = {
            "order_id": "ORD789",           # str key, str value
            123: "Customer Account",      # int key, str value
            "total_amount": 127.50,         # str key, float value
            "items_ordered": ["P101", "P203"], # str key, list value
            "is_shipped": False,            # str key, bool value
            ("ship_to_country", "ship_to_zip"): ("USA", "90210") # tuple key, tuple value
        }
        print(f"\nOrder info dictionary: {order_info}")
        # print(f"Key 'order_id' type: {type('order_id')}, Value type: {type(order_info['order_id'])}")
        # print(f"Key 123 type: {type(123)}, Value type: {type(order_info)}")
        ```
- [[Python_Set_Frozenset|Sets (`set`)]]
    -   **Can Mix Types?** Yes, elements in a set can be of different immutable types.
    -   **Constraint:** Like dictionary keys, elements of a set **must be of an immutable (hashable) type**. You cannot add a list or another (mutable) set as an element to a set. You can add tuples (if all their elements are immutable) or frozensets.
    -   **Example (Collection of unique identifiers and properties):**
        ```python
        mixed_set = {
            101,                      # int
            "product_sku_abc",        # str
            3.14,                     # float
            True,                     # bool
            ("user_id", 1001),        # tuple
            frozenset({"tag1", "tag2"}) # frozenset
        }
        # mixed_set.add([]) # This would raise TypeError: unhashable type: 'list'
        print(f"\nMixed set: {mixed_set}")
        ```
- [[Python_Set_Frozenset|Frozen Sets (`frozenset`)]]
    -   **Can Mix Types?** Yes, same rules as `set`: elements can be of different immutable types.
    -   **Constraint:** Elements must be immutable. The `frozenset` itself is immutable after creation.
    -   **Example:**
        ```python
        mixed_frozenset = frozenset([1, "config_value", (True, None)])
        print(f"\nMixed frozenset: {mixed_frozenset}")
        ```

## Implications of Type Mixing
-   **Flexibility:** The ability to mix types makes Python's data structures very adaptable for representing real-world data which is often heterogeneous.
-   **Type Checking:** When iterating or accessing elements, you might need to check the type of an element using `isinstance()` if your processing logic depends on the type.
    ```python
    # mixed_data_list = [1, "hello",, {"a":5}, 3.14]
    # for item in mixed_data_list:
    #     if isinstance(item, int):
    #         print(f"Integer: {item * 2}")
    #     elif isinstance(item, str):
    #         print(f"String: {item.upper()}")
    #     else:
    #         print(f"Other type ({type(item)}): {item}")
    ```
-   **Operations:** Not all operations are valid for all types within a mixed collection. For example, you can't sum a list of mixed strings and numbers directly without conversion. Sorting a list of mixed, incomparable types will raise a `TypeError`.

While Python allows mixing types in its collections, it's often good practice to have collections with homogeneous types (all elements of the same type) if the subsequent processing expects uniformity, as this can simplify code and reduce the need for type checking. However, the flexibility to mix types is a powerful feature when needed.

---
`````

`````markdown

Filename: 100_Python/Python_Data_Structures/Python_Data_Structures_Ordered_Unordered.md
````markdown
---
tags: [python, data_structures, list, tuple, set, dictionary, order, sequence, concept_comparison]
aliases: [Ordered Data Structures Python, Unordered Data Structures Python, Python Collection Order]
related:
  - "[[100_Python/Python_Data_Structures/_Python_Data_Structures_MOC|_Python_Data_Structures_MOC]]"
  - "[[Python_List]]"
  - "[[Python_Tuple]]"
  - "[[Python_Set_Frozenset|Python Set and Frozenset]]"
  - "[[Python_Dictionary]]"
worksheet: [WS17]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Python: Ordered vs. Unordered Data Structures

Python's built-in data structures can be categorized based on whether they maintain the order of their elements.

>[!question] List the ordered and the unordered data structures.

## Ordered Data Structures
**Ordered data structures** preserve the order in which items were inserted. When you iterate over them or access elements by index (if applicable), you get them back in that same defined sequence.

1.  **[[Python_List|Lists (`list`)]]**
    -   **Definition:** `my_list = `
    -   **Order:** Inherently ordered. Elements are stored in a sequence, and this sequence is maintained. You can access elements by their numerical index (e.g., `my_list`, `my_list`).
    -   **Example:**
        ```python
        product_order = ["Laptop", "Mouse", "Keyboard"]
        # Iterating will always give "Laptop", then "Mouse", then "Keyboard"
        # for item in product_order:
        #     print(item)
        # print(product_order[0]) # Always "Laptop"
        ```

2.  **[[Python_Tuple|Tuples (`tuple`)]]**
    -   **Definition:** `my_tuple = ("alpha", "beta", "gamma")`
    -   **Order:** Inherently ordered, just like lists. Elements are stored in a sequence and accessed by index.
    -   **Example:**
        ```python
        coordinates = (10.5, 20.3, 5.0) # x, y, z
        # print(coordinates[1]) # Always 20.3
        ```

3.  **[[Python_Primitive_Types|Strings (`str`)]]**
    -   **Definition:** `my_string = "hello"`
    -   **Order:** Strings are sequences of characters, and their order is fundamental.
    -   **Example:**
        ```python
        # print(my_string[0]) # Always 'h'
        ```

4.  **[[Python_Dictionary|Dictionaries (`dict`)]] (Python 3.7+ and CPython 3.6+)**
    -   **Definition:** `my_dict = {"name": "Alice", "age": 30}`
    -   **Order:**
        -   **Python 3.7+:** Dictionaries are guaranteed to preserve insertion order. When you iterate over a dictionary (e.g., its keys, values, or items), they will appear in the order they were added.
        -   **CPython 3.6:** This version also implemented insertion order preservation as an implementation detail, which became official in 3.7.
        -   **Python < 3.6:** Dictionaries were unordered. The order of items could be arbitrary and might change during operations. For ordered dictionaries in older Python, `collections.OrderedDict` was used.
    -   **Example (Python 3.7+):**
        ```python
        # product_config = {"color": "blue", "size": "M", "material": "cotton"}
        # product_config["in_stock"] = True # Added last

        # print("Keys in insertion order (Python 3.7+):")
        # for key in product_config:
        #     print(key)
        # Output:
        # color
        # size
        # material
        # in_stock
        ```

## Unordered Data Structures
**Unordered data structures** do not maintain any specific order for their elements. The concept of a "first" or "second" element is not well-defined, and iterating over them might yield elements in a different sequence each time or in an order based on internal hashing mechanisms rather than insertion.

1.  **[[Python_Set_Frozenset|Sets (`set`)]]**
    -   **Definition:** `my_set = {1, "apple", 3.14}` or `my_set = set()`
    -   **Order:** Inherently unordered. Sets are implemented using hash tables, and the internal storage order is optimized for efficient membership testing and uniqueness, not for preserving insertion sequence.
    -   You cannot access elements by index.
    -   **Example:**
        ```python
        # customer_tags = {"vip", "new_customer", "newsletter_subscriber"}
        # print(f"Customer tags set: {customer_tags}")
        # The output order might be different each time or across Python versions/runs, e.g.:
        # {'newsletter_subscriber', 'vip', 'new_customer'} or
        # {'vip', 'new_customer', 'newsletter_subscriber'}

        # print("\nIterating over the set (order not guaranteed):")
        # for tag in customer_tags:
        #     print(tag)
        ```

2.  **[[Python_Set_Frozenset|Frozen Sets (`frozenset`)]]**
    -   **Definition:** `my_fset = frozenset([1, "apple", 3.14])`
    -   **Order:** Inherently unordered, just like regular sets.

3.  **[[Python_Dictionary|Dictionaries (`dict`)]] (Python < 3.6, or non-CPython 3.6 implementations)**
    -   As mentioned above, dictionaries were unordered before Python 3.7 (officially). If working with older Python versions, you should assume dictionaries are unordered.

## Summary Table

[list2mdtable|#Order in Python Data Structures]
- Data Structure
    - Ordered?
        - Notes
- `list`
    - Yes
        - Order of insertion is preserved. Indexable.
- `tuple`
    - Yes
        - Order of insertion is preserved. Indexable.
- `str`
    - Yes
        - Sequence of characters. Indexable.
- `dict`
    - Yes (Python 3.7+)
        - Preserves insertion order.
    - No (Python < 3.6 generally)
        - Use `collections.OrderedDict` for guaranteed order in older Python.
- `set`
    - No
        - Elements are unique; order is not guaranteed and not indexable.
- `frozenset`
    - No
        - Immutable version of set; order is not guaranteed and not indexable.

Understanding whether a data structure is ordered or unordered is important for predicting its behavior during iteration, indexing (if applicable), and for operations where sequence matters.

---
`````

This completes the notes for the remaining questions from WS17. Next, I will move to **WS18 - Functions**, starting with its MOC and then the keyword/question notes.

Okay, let's move on to **WS18 - Python Functions**. I'll start by creating the MOC for this section and then create notes for the keywords, built-in functions, and questions.

---

### Python Functions (WS18) - Folder and MOC

`````markdown

Filename: 100_Python/Python_Functions/_Python_Functions_MOC.md
````markdown
---
tags: [python, functions, programming_paradigms, scope, arguments, lambda, higher_order_functions, moc, concept]
aliases: [Python Functions MOC, Defining Functions Python]
related:
  - "[[100_Python/_Python_Programming_MOC|_Python_Programming_MOC]]"
  - "[[Python_Function_Definition_Syntax]]" # Placeholder
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
worksheet: [WS18]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
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
`````

Now, creating notes for the keywords, built-ins, and questions from WS18.

`````markdown

Filename: 100_Python/Python_Functions/Python_Function_Definition_Syntax.md
````markdown
---
tags: [python, functions, def_statement, parameters, arguments, return_statement, docstrings, syntax, concept]
aliases: [Defining Python Functions, Python def, Function Parameters Python, Function Return Values]
related:
  - "[[100_Python/Python_Functions/_Python_Functions_MOC|_Python_Functions_MOC]]"
worksheet: [WS18] # Implied as foundational for functions
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
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
`````

`````markdown

Filename: 100_Python/Python_Functions/Python_Pure_Functions.md
````markdown
---
tags: [python, functions, pure_functions, functional_programming, side_effects, determinism, concept, example]
aliases: [Pure Function Python]
related:
  - "[[100_Python/Python_Functions/_Python_Functions_MOC|_Python_Functions_MOC]]"
  - "[[Python_Higher_Order_Functions]]" # Pure functions are often good candidates for HOFs
  - "[[Python_Mutability_Immutability|Mutability and Immutability in Python]]"
worksheet: [WS18]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Python: Pure Functions

A **pure function** is a concept from functional programming that describes a function with two main properties:

1.  **Deterministic:** Given the same input arguments, the function will **always return the same output value**. It does not depend on any hidden state or external factors that might change between calls.
2.  **No Side Effects:** The function's execution does **not cause any observable changes outside its local scope**. This means it doesn't modify global variables, mutable arguments passed by reference, perform I/O operations (like printing to console, reading/writing files, network requests), or call other non-pure functions that have side effects.

## Characteristics of Pure Functions
-   **Predictable:** Their behavior is entirely determined by their input values.
-   **Testable:** Easy to test because you only need to check if the output is correct for a given input, without worrying about external state or side effects.
-   **Referential Transparency:** An expression involving a pure function call can be replaced by its return value without changing the program's behavior.
-   **Concurrency-Friendly:** Since they don't modify shared state, pure functions are inherently easier to parallelize and use in concurrent environments without race conditions.
-   **Cacheable/Memoizable:** The results of pure functions can be cached (memoized) because they always produce the same output for the same input.

>[!question] What is "Pure function" and "Higher-order Function"? Give 3 examples For each of them.

## Pure Functions
(Definition above)

**Examples of Pure Functions in Python:**
1.  **Simple Arithmetic Function:**
    ```python
    def add_numbers(x: float, y: float) -> float:
        """Returns the sum of x and y. Pure function."""
        return x + y
    
    print(add_numbers(2, 3))    # Always 5
    print(add_numbers(2, 3))    # Still 5, no side effects
    print(add_numbers(-1, 10))  # Always 9
    ```
    -   *Deterministic:* `add_numbers(2, 3)` will always return `5`.
    -   *No Side Effects:* It doesn't print anything, modify global variables, or change its input arguments (numbers are immutable).

2.  **String Manipulation Function:**
    ```python
    def create_greeting(name: str) -> str:
        """Returns a greeting string for the given name. Pure function."""
        return f"Hello, {name}!"
    
    print(create_greeting("Alice")) # Always "Hello, Alice!"
    print(create_greeting("Bob"))   # Always "Hello, Bob!"
    ```    -   *Deterministic:* Output depends only on the `name` argument.
    -   *No Side Effects:* Strings are immutable; a new string is created and returned.

3.  **List Transformation (returning a new list):**
    ```python
    def square_elements(numbers: list[int]) -> list[int]:
        """Returns a NEW list with each element squared. Pure function."""
        return [x**2 for x in numbers]

    original_list = 
    squared_list1 = square_elements(original_list)
    squared_list2 = square_elements(original_list) # original_list is unchanged
    
    print(f"Original: {original_list}")
    print(f"Squared 1: {squared_list1}") # [1, 4, 9, 16]
    print(f"Squared 2: {squared_list2}") # [1, 4, 9, 16] (same result)
    print(f"Original still unchanged: {original_list}")
    ```
    -   *Deterministic:* Given the same input list content, it always produces the same new list of squared numbers.
    -   *No Side Effects:* It does not modify the original `numbers` list. It creates and returns a *new* list. If it modified `numbers` in-place, it would not be pure.

## Impure Functions (Examples for Contrast)

1.  **Modifies Global State:**
    ```python
    # total_calls = 0
    # def count_function_calls():
    #     """Impure: Modifies a global variable."""
    #     global total_calls
    #     total_calls += 1
    #     return total_calls
    ```
2.  **Performs I/O (Printing):**
    ```python
    # def greet_with_print(name):
    #     """Impure: Has a side effect (printing to console)."""
    #     message = f"Hello, {name}!"
    #     print(message) # Side effect
    #     return message
    ```
3.  **Modifies Mutable Arguments In-Place:**
    ```python
    # def append_to_list_impure(item, target_list):
    #     """Impure: Modifies its mutable argument 'target_list'."""
    #     target_list.append(item)
    #     return target_list # Returning it doesn't make it pure if it was modified
    ```
4.  **Depends on External State (e.g., current time, random numbers):**
    ```python
    # import datetime
    # def get_current_time_string():
    #     """Impure: Output depends on external state (current time)."""
    #     return str(datetime.datetime.now())

    # import random
    # def get_random_number():
    #     """Impure: Output is not deterministic."""
    #     return random.randint(1, 100)
    ```

While not all functions can or should be pure (e.g., functions dealing with I/O inherently have side effects), striving to write pure functions for computational logic can lead to more robust, testable, and maintainable code. Pure functions are easier to reason about because their behavior is self-contained.

The concept of [[Python_Higher_Order_Functions|Higher-Order Functions]] is distinct but often benefits from using pure functions as arguments or return values.

---
`````

`````markdown

Filename: 100_Python/Python_Functions/Python_Higher_Order_Functions.md
````markdown
---
tags: [python, functions, higher_order_functions, functional_programming, map, filter, reduce, decorators, concept, example]
aliases: [Higher Order Functions Python, HOFs]
related:
  - "[[100_Python/Python_Functions/_Python_Functions_MOC|_Python_Functions_MOC]]"
  - "[[Python_Pure_Functions]]"
  - "[[Python_Lambda_Functions]]"
  - "[[Python_Decorators]]"
  - "[[Built_In_Functions_Python#map_function|map() built-in]]"
  - "[[Built_In_Functions_Python#filter_function|filter() built-in]]"
  - "[[Built_In_Functions_Python#reduce_function|functools.reduce()]]"
worksheet: [WS18]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
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
`````

This covers Pure Functions and Higher-Order Functions. Next, I'll create notes for Recursion, Nested Functions/Closures/Nonlocal, *args/**kwargs, Lambdas, Comprehensions, and Decorators.

Okay, continuing with the notes for Python Functions (WS18).

---

`````markdown

Filename: 100_Python/Python_Functions/Python_Recursion.md
````markdown
---
tags: [python, functions, recursion, algorithm, base_case, recursive_step, concept, example]
aliases: [Recursive Functions Python, Python Recursive Call]
related:
  - "[[100_Python/Python_Functions/_Python_Functions_MOC|_Python_Functions_MOC]]"
  - "[[Stack_Overflow_Error]]" # Placeholder, relevant to deep recursion
worksheet: [WS18]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Python: Recursion

**Recursion** is a programming technique where a function calls itself in order to solve a problem. A recursive function breaks a problem down into smaller, self-similar subproblems until it reaches a simple enough case that can be solved directly (the base case).

## Key Components of a Recursive Function
1.  **Base Case(s):**
    -   One or more conditions under which the function does not call itself again.
    -   This is crucial to prevent infinite recursion and a [[Stack_Overflow_Error|stack overflow error]].
    -   The base case provides a direct solution for the simplest instance of the problem.
2.  **Recursive Step (Recursive Call):**
    -   The part of the function where it calls itself, but with modified arguments that move it closer to a base case.
    -   The problem is broken down into a smaller or simpler version of the same problem.

## How Recursion Works
When a function calls itself, a new frame is added to the call stack to store the local variables and state of that particular call. When the recursive call returns, its frame is popped from the stack, and execution resumes in the calling frame. This continues until the base case is reached and the chain of calls unwinds.

## Example: Factorial Calculation
The factorial of a non-negative integer $n$, denoted by $n!$, is the product of all positive integers less than or equal to $n$.
-   $0! = 1$ (base case)
-   $n! = n \times (n-1)!$ for $n > 0$ (recursive step)

```python
def factorial_recursive(n: int) -> int:
    """Calculates factorial of n using recursion."""
    # Base case: factorial of 0 or 1 is 1
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif n == 0 or n == 1:
        return 1
    # Recursive step: n * (n-1)!
    else:
        return n * factorial_recursive(n - 1)

# Test the function
# print(f"Factorial of 5: {factorial_recursive(5)}")  # Output: 120 (5*4*3*2*1)
# print(f"Factorial of 0: {factorial_recursive(0)}")  # Output: 1
# print(f"Factorial of 1: {factorial_recursive(1)}")  # Output: 1
# try:
#     factorial_recursive(-2)
# except ValueError as e:
#     print(f"Error: {e}")
```

## Example: Sum of Elements in a List (Conceptual E-commerce Order Total)
Imagine an RDD-like structure or list of item prices from an order.
```python
def sum_list_recursive(data_list: list) -> float:
    """Calculates the sum of elements in a list using recursion."""
    # Base case: if the list is empty, sum is 0
    if not data_list: # or len(data_list) == 0
        return 0
    # Recursive step: first element + sum of the rest of the list
    else:
        return data_list[0] + sum_list_recursive(data_list[1:])

# Test the function
# item_prices = 
# total_order_value = sum_list_recursive(item_prices)
# print(f"Item prices: {item_prices}")
# print(f"Total order value: ${total_order_value:.2f}") # Output: $185.94

# empty_order = []
# print(f"Total for empty order: ${sum_list_recursive(empty_order):.2f}") # Output: $0.00
```

## Advantages of Recursion
-   **Elegance and Readability:** For problems that are naturally recursive (e.g., tree traversals, fractals, some mathematical functions like factorial or Fibonacci), recursive solutions can be very concise, elegant, and easier to understand than iterative solutions.
-   **Problem Decomposition:** Matches well with divide-and-conquer strategies.

## Disadvantages of Recursion
-   **Performance Overhead:** Each function call adds a new frame to the call stack, consuming memory and time. For deep recursion, this can be less efficient than an iterative solution.
-   **Stack Overflow Risk:** If the recursion is too deep (i.e., too many nested function calls without reaching a base case quickly enough), it can exhaust the call stack memory, leading to a [[Stack_Overflow_Error|stack overflow error]]. Python has a default recursion limit (often around 1000-3000 calls), which can be changed with `sys.setrecursionlimit()`, but this is generally not recommended as a primary solution.
-   **Debugging:** Tracing the flow of execution in recursive functions can sometimes be more challenging than in iterative ones.
-   **Not Always Intuitive:** For problems that are not inherently recursive, forcing a recursive solution can make the code harder to understand.

## Recursion vs. Iteration
Many problems that can be solved recursively can also be solved iteratively (using loops like `for` or `while`).
-   Iterative solutions often use less memory (no deep call stack) and can be faster due to less function call overhead.
-   Recursive solutions can be more intuitive for certain problems.

**Tail Recursion:**
Some programming languages perform **tail call optimization (TCO)**, where a recursive call that is the very last operation in a function (a tail call) can be optimized to not consume additional stack space, effectively behaving like an iteration. **Python does NOT perform tail call optimization.** Therefore, deep tail-recursive functions in Python can still lead to stack overflows.

When deciding whether to use recursion:
-   Consider if the problem has a natural recursive structure.
-   Be mindful of the potential depth of recursion and the risk of stack overflow.
-   If performance is critical for very deep call chains, an iterative solution might be preferable in Python.

Recursion is a powerful conceptual tool and a practical technique for solving certain types of problems elegantly.

---
````

`````markdown

Filename: 100_Python/Python_Functions/Python_Nested_Functions_Closures.md
````markdown
---
tags: [python, functions, nested_functions, closures, nonlocal, scope, functional_programming, concept, example]
aliases: [Nested Functions Python, Python Closures, Nonlocal Keyword Python, Enclosing Scope]
related:
  - "[[100_Python/Python_Functions/_Python_Functions_MOC|_Python_Functions_MOC]]"
  - "[[Python_Scopes_Modules_MOC|Python Scopes (LEGB Rule)]]"
  - "[[Python_Decorators]]" # Closures are fundamental to how decorators work
  - "[[Python_Higher_Order_Functions]]" # Functions returning functions often create closures
worksheet: [WS18]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
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
````

`````markdown

Filename: 100_Python/Python_Functions/Python_Args_Kwargs.md
````markdown
---
tags: [python, functions, arguments, parameters, args, kwargs, variable_arguments, unpacking, concept, example]
aliases: [*args, **kwargs, Arbitrary Arguments Python, Keyword Arguments Python]
related:
  - "[[100_Python/Python_Functions/_Python_Functions_MOC|_Python_Functions_MOC]]"
  - "[[Python_Function_Definition_Syntax]]"
worksheet: [WS18]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Python: `*args` and `**kwargs` (Variable Arguments)

Python functions can be defined to accept a variable number of arguments using special syntax: `*args` for positional arguments and `**kwargs` for keyword arguments.

>[!question] What is the definition of "args" and the definition of "kwargs"? Are we required to use these specific names?
>
>-   **`*args` (Arbitrary Positional Arguments):**
>    -   **Definition:** When used in a function definition, `*args` allows the function to accept an **arbitrary number of positional arguments**. These arguments are collected into a **tuple** named `args` (or whatever name follows the `*`).
>    -   **Required Name?** No, `args` is just a convention. You could use `*my_numbers` or `*params`, but `*args` is widely understood. The single asterisk `*` is the important part of the syntax.
>
>-   **`**kwargs` (Arbitrary Keyword Arguments):**
>    -   **Definition:** When used in a function definition, `**kwargs` allows the function to accept an **arbitrary number of keyword arguments** (arguments passed in the form `key=value`). These arguments are collected into a **dictionary** named `kwargs` (or whatever name follows the `**`).
>    -   **Required Name?** No, `kwargs` is just a convention. You could use `**options` or `**attributes`, but `**kwargs` is standard. The double asterisk `**` is the important part.

## Using `*args`
To accept a variable number of positional arguments.

```python
def calculate_product_sum(*numbers): # 'numbers' will be a tuple
    """Calculates the sum of all numbers passed as arguments."""
    print(f"Received numbers as a tuple: {numbers}")
    total = 0
    for num in numbers:
        total += num
    return total

# print(calculate_product_sum(10, 20))          # Output: Received numbers... (10, 20) -> 30
# print(calculate_product_sum(5, 15, 25, 5))    # Output: Received numbers... (5, 15, 25, 5) -> 50
# print(calculate_product_sum())                # Output: Received numbers... () -> 0
```
Inside `calculate_product_sum`, `numbers` is a tuple containing all the positional arguments passed.

## Using `**kwargs`
To accept a variable number of keyword arguments.

```python
def display_product_info(**details): # 'details' will be a dictionary
    """Displays product information passed as keyword arguments."""
    print("Product Details:")
    if not details:
        print("  No details provided.")
        return
    for key, value in details.items():
        print(f"  {key.replace('_', ' ').title()}: {value}")

# display_product_info(name="Super Laptop", price=1299.99, category="Electronics")
# display_product_info(item_id="XYZ001", in_stock=True, color="Silver", warranty_years=2)
# display_product_info()
```
Inside `display_product_info`, `details` is a dictionary containing all the keyword arguments passed.

## Combining `*args`, `**kwargs` with Standard Arguments

>[!question] If you want to use standard arguments along with `*args` and `**kwargs`, what is the correct order?
>The correct order for parameters in a function definition is:
>1.  **Standard positional arguments.**
>2.  `*args` (for arbitrary positional arguments).
>3.  **Keyword-only arguments** (arguments that can *only* be passed by keyword, appear after `*args` or a bare `*`).
>4.  `**kwargs` (for arbitrary keyword arguments).
>
>```python
>def example_function(pos_arg1, pos_arg2, default_arg="default", *args, kw_only_arg1, kw_only_arg2="val2", **kwargs):
>    print(f"pos_arg1: {pos_arg1}")
>    print(f"pos_arg2: {pos_arg2}")
>    print(f"default_arg: {default_arg}")
>    print(f"args: {args}")
>    print(f"kw_only_arg1: {kw_only_arg1}")
>    print(f"kw_only_arg2: {kw_only_arg2}")
>    print(f"kwargs: {kwargs}")

# Calling it:
# example_function(1, 2, "custom_default", 10, 20, 30, 
#                  kw_only_arg1="hello", option1="A", option2="B")
# Output:
# pos_arg1: 1
# pos_arg2: 2
# default_arg: custom_default
# args: (10, 20, 30)
# kw_only_arg1: hello
# kw_only_arg2: val2
# kwargs: {'option1': 'A', 'option2': 'B'}

# example_function(1, 2, kw_only_arg1="world") # Also valid
```

## Unpacking Arguments (`*` and `**` in function calls)

>[!question] What is an "unpacking operator"? Why do we use a single asterisk in "args" and double in "kwargs"?
>The `*` and `**` symbols when used in *function calls* (not definitions) are **unpacking operators**.
>
>-   **`*iterable` (Unpacking Positional Arguments):**
>    -   When calling a function, `*` unpacks an iterable (like a list or tuple) into individual positional arguments.
>    -   **Why single asterisk for `*args` in definition?** In the function definition, `*args` *collects* multiple positional arguments into a single tuple named `args`. The single asterisk signifies "collect all remaining positional arguments."
>
>-   **`**dictionary` (Unpacking Keyword Arguments):**
>    -   When calling a function, `**` unpacks a dictionary into individual keyword arguments, where dictionary keys become argument names and dictionary values become argument values.
>    -   **Why double asterisk for `**kwargs` in definition?** In the function definition, `**kwargs` *collects* multiple keyword arguments into a single dictionary named `kwargs`. The double asterisk signifies "collect all remaining keyword arguments."

**Example of Unpacking in Function Calls:**
```python
def describe_item(item_id, name, price=0.0, category="General"):
    print(f"ID: {item_id}, Name: {name}, Price: ${price:.2f}, Category: {category}")

# Using * to unpack a list/tuple for positional arguments
product_data_list = ["P456", "Deluxe Coffee Grinder"]
# describe_item(*product_data_list, price=89.99, category="Appliances")
# Equivalent to: describe_item("P456", "Deluxe Coffee Grinder", price=89.99, category="Appliances")

# Using ** to unpack a dictionary for keyword arguments
product_details_dict = {
    "name": "Ergonomic Keyboard",
    "price": 75.50,
    "category": "Accessories"
}
# describe_item("K789", **product_details_dict)
# Equivalent to: describe_item("K789", name="Ergonomic Keyboard", price=75.50, category="Accessories")

# Combining them
# required_args = ("S001", "Premium Subscription")
# optional_attrs = {"price": 19.99, "category": "Service"}
# describe_item(*required_args, **optional_attrs)
```

`*args` and `**kwargs` provide great flexibility in designing functions that can handle a varying number of inputs or pass arguments through to other functions.

---
`````

This covers Recursion, Nested Functions/Closures/Nonlocal, and *args/**kwargs. Next will be Lambda Functions, Comprehensions, and Decorators from WS18.

Okay, continuing with the Python Functions (WS18) notes, focusing on Lambda Functions, Comprehensions, and Decorators.

---

`````markdown

Filename: 100_Python/Python_Functions/Python_Lambda_Functions.md
````markdown
---
tags: [python, functions, lambda, anonymous_function, functional_programming, concept, example]
aliases: [Lambda Expressions Python, Anonymous Functions Python, Python Lambda]
related:
  - "[[100_Python/Python_Functions/_Python_Functions_MOC|_Python_Functions_MOC]]"
  - "[[Python_Higher_Order_Functions]]" # Lambdas are often used with HOFs like map, filter, sorted
worksheet: [WS18]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Python: Lambda Functions (Anonymous Functions)

A **lambda function** in Python is a small, anonymous function defined with the `lambda` keyword. Lambda functions are restricted to a single expression and are often used when you need a simple function for a short period and don't want to formally define it using `def`.

>[!question] What is a lambda Function?
>A lambda function is a small, anonymous (unnamed) function defined using the `lambda` keyword. It can take any number of arguments but can only have **one expression**. The expression is evaluated and returned. Lambda functions are syntactically restricted and cannot contain multiple statements or complex logic that would require multiple lines in a regular `def` function.

## Syntax
```python
lambda arguments: expression
```
-   `lambda`: Keyword indicating the start of a lambda function definition.
-   `arguments`: A comma-separated list of arguments (parameters) the function accepts, similar to a regular function's parameter list.
-   `:`: Separates the arguments from the expression.
-   `expression`: A single expression that is evaluated and whose result is returned by the lambda function. This expression cannot contain multiple statements or complex control flow like multi-line `if/else` or `for/while` loops (though conditional expressions are allowed).

## Key Characteristics
-   **Anonymous:** They don't have a formal name defined with `def` (though you can assign a lambda function to a variable, it's generally not the primary use case for complex lambdas).
-   **Single Expression:** The body of a lambda function is limited to a single expression. The result of this expression is implicitly returned.
-   **Concise:** Useful for creating simple, one-off functions without the boilerplate of a `def` statement.
-   **Often Used with Higher-Order Functions:** Frequently used as arguments to [[Python_Higher_Order_Functions|higher-order functions]] like `map()`, `filter()`, `sorted()`, or in GUI callbacks.

>[!question] Can we use more than one expression in the Lambda Function?
>No, a lambda function is restricted to a **single expression**. It cannot contain multiple statements or a block of statements like a regular function defined with `def`. The result of this single expression is what the lambda function returns.

>[!question] Can you create a lambda function that receives more than one parameter?
>Yes, a lambda function can accept multiple parameters, just like a regular function.
>```python
># Lambda with two parameters
>add_product_prices = lambda price1, price2: price1 + price2
>print(add_product_prices(10.99, 5.50)) # Output: 16.49
>
># Lambda with three parameters
>format_product_info = lambda name, category, stock: f"Product: {name} (Category: {category}) - Stock: {stock}"
>print(format_product_info("Smartwatch", "Electronics", 50))
>```

## Examples

**1. Simple arithmetic:**
```python
# Add 10 to an argument
add_ten = lambda x: x + 10
print(f"add_ten(5): {add_ten(5)}") # Output: 15

# Multiply two numbers
multiply = lambda x, y: x * y
print(f"multiply(6, 7): {multiply(6, 7)}") # Output: 42
```

**2. Using with `map()`:**
To apply a simple operation to all items in an iterable.
```python
# E-commerce: List of product prices
prices = 
# Apply a 5% discount to all prices
discounted_prices_iterator = map(lambda p: p * 0.95, prices)
print(f"Discounted prices: {list(discounted_prices_iterator)}")
# Output: [18.9905, 47.025, 114.0, 23.75, 72.1905]
```

**3. Using with `filter()`:**
To select items from an iterable based on a condition.
```python
# E-commerce: Product ratings
ratings = [4.5, 2.0, 3.8, 5.0, 1.5, 4.2, 4.9]
# Filter for high ratings (>= 4.0)
high_ratings_iterator = filter(lambda r: r >= 4.0, ratings)
print(f"High ratings: {list(high_ratings_iterator)}") # Output: [4.5, 5.0, 4.2, 4.9]
```

**4. Using with `sorted()` (or `list.sort()`) for custom sort keys:**
To sort an iterable based on a computed key.
```python
# List of product tuples: (product_name, price, stock_quantity)
products = [
    ("Laptop", 1200.00, 10),
    ("Mouse", 25.00, 150),
    ("Keyboard", 75.00, 75),
    ("Monitor", 300.00, 25)
]

# Sort products by price (the second element of each tuple)
sorted_by_price = sorted(products, key=lambda product: product[1])
print(f"Products sorted by price:\n{sorted_by_price}")

# Sort products by stock quantity (descending)
sorted_by_stock_desc = sorted(products, key=lambda product: product[2], reverse=True)
print(f"\nProducts sorted by stock (desc):\n{sorted_by_stock_desc}")
```

## When to Use Lambda Functions (and When Not To)

>[!question] When should you use Lambda Functions and when should you not?
>
>**When to Use Lambda Functions:**
>1.  **Short, Simple, One-Off Functions:** When you need a small, throwaway function for a specific, localized purpose, and defining a full `def` function would be overly verbose.
>2.  **Arguments to Higher-Order Functions:** They are very commonly used as arguments for functions like `map()`, `filter()`, `sorted()`, or as callbacks in GUI programming or event handling, where a simple function is needed to define a behavior.
>3.  **Improving Readability for Simple Operations:** For very simple operations, a lambda can sometimes make the code more concise and readable by keeping the logic inline. Example: `sorted(items, key=lambda x: x)` is often clearer than defining a separate one-line function just to extract `x`.
>
>**When NOT to Use (or Use with Caution):**
>4.  **Complex Logic:** If the function requires multiple expressions, statements, or complex control flow (multi-line if/else, loops), a lambda function is not appropriate. Use a regular `def` function instead for readability and maintainability.
>5.  **Readability Suffers:** If the lambda expression becomes too long or convoluted, it harms readability. A named `def` function is better in such cases. A good rule of thumb: if it's hard to understand the lambda at a glance, use `def`.
>6.  **Reusability:** If you need to use the same function logic in multiple places, define it once with `def` and give it a descriptive name. While you *can* assign a lambda to a variable (e.g., `my_adder = lambda x, y: x + y`), linters like PEP 8 often discourage this, suggesting `def my_adder(x, y): return x + y` instead for better clarity and debuggability (named functions show up better in tracebacks).
>7.  **Docstrings and Type Hints:** Lambda functions cannot have docstrings in the standard way, and adding type hints can make them look clunky (though possible with type-comment syntax or by assigning to a typed variable). Regular functions are better for documentation and explicit typing.

Lambda functions are a convenient tool for writing concise functional code in Python, but they should be used judiciously to maintain code clarity.

---
`````

`````markdown

Filename: 100_Python/Python_Functions/Python_Comprehensions.md
````markdown
---
tags: [python, functions, comprehensions, list_comprehension, dict_comprehension, set_comprehension, generator_expression, concise_code, functional_programming, concept, example]
aliases: [Python Comprehensions, List Comprehensions, Dictionary Comprehensions, Set Comprehensions, Generator Expressions]
related:
  - "[[100_Python/Python_Functions/_Python_Functions_MOC|_Python_Functions_MOC]]"
  - "[[Python_List]]"
  - "[[Python_Dictionary]]"
  - "[[Python_Set_Frozenset|Python Set]]"
  - "[[Python_Loops_Iteration|Looping and Iteration]]" # Comprehensions are concise loops
  - "[[Python_Lambda_Functions]]" # Often used with or as alternative to comprehensions for simple maps/filters
worksheet: [WS18]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Python: Comprehensions (List, Dict, Set) and Generator Expressions

**Comprehensions** in Python provide a concise and readable way to create lists, dictionaries, or sets from existing iterables. They are often more compact and sometimes more efficient than using explicit `for` loops and `append()` calls or conditional logic to build these collections.

**Generator Expressions** use a similar syntax but create an iterator instead of a fully realized collection in memory immediately.

>[!question] What is the benefit of using comprehensions?
>The primary benefits of using comprehensions are:
>1.  **Conciseness and Readability:** They allow you to create collections in a single, often more readable line of code compared to multi-line `for` loops. The intent of creating a new collection based on an existing one is very clear.
>2.  **Expressiveness:** They elegantly express common patterns like mapping (applying an operation to each element) and filtering (selecting elements based on a condition).
>3.  **Performance (Often):** List comprehensions, in particular, can be faster than equivalent `for` loops with `append()` calls because the list construction is optimized at a lower level in CPython.
>4.  **Pythonic Style:** Using comprehensions is considered a more "Pythonic" way to create collections from iterables for many common use cases.

## 1. List Comprehensions
-   **Purpose:** Create a new [[Python_List|list]] by applying an expression to each item in an iterable, optionally filtering items.
-   >[!question] What is the syntax of list comprehension?
    >```python
    >[expression for item in iterable if condition]
    >```
    >-   `expression`: The operation to apply to each `item` (e.g., `item * 2`, `item.upper()`). This becomes an element in the new list.
    >-   `item`: A variable representing each element from the `iterable`.
    -   `iterable`: The existing sequence or iterable to process (e.g., a list, tuple, string, range).
    -   `if condition` (optional): A filter. Only items for which the `condition` is `True` will be processed by the `expression` and included in the new list.

**Examples (E-commerce context):**
```python
# a. Square of product quantities
quantities =
squared_quantities = [q**2 for q in quantities]
print(f"Squared quantities: {squared_quantities}") # Output:

# b. Uppercase product category names
categories = ["electronics", "books", "apparel"]
uppercase_categories = [cat.upper() for cat in categories]
print(f"Uppercase categories: {uppercase_categories}") # Output: ['ELECTRONICS', 'BOOKS', 'APPAREL']

# c. Filter for product prices above a threshold and apply a discount
prices = [99.99, 150.00, 25.50, 200.00, 10.00]
min_price_for_discount = 50.00
discount_rate = 0.10 # 10%
discounted_high_prices = [
    price * (1 - discount_rate) 
    for price in prices 
    if price > min_price_for_discount
]
print(f"Discounted high prices: {[f'{p:.2f}' for p in discounted_high_prices]}") 
# Output: ['135.00', '180.00'] (for 150.00 and 200.00)
```

>[!question] What is nested list comprehension?
>A nested list comprehension involves one or more `for` clauses (and optional `if` clauses) within another list comprehension, allowing you to work with nested iterables or create lists of lists (like matrices).
>
>**Syntax (conceptual for two levels):**
>```python
>[expression for outer_item in outer_iterable for inner_item in inner_iterable if condition]
>```
>The `for` clauses are nested from left to right.
>
>**Example: Flattening a list of product tags**
>```python
>product_tags_nested = [
#    ["electronics", "new", "sale"],
#    ["books", "bestseller"],
#    ["apparel", "sale", "cotton"]
#]
#
#all_tags_flat = [tag for sublist in product_tags_nested for tag in sublist]
#print(f"Flattened tags: {all_tags_flat}")
## Output: ['electronics', 'new', 'sale', 'books', 'bestseller', 'apparel', 'sale', 'cotton']
#
# Get unique flattened tags
# unique_tags_flat = list(set([tag.lower() for sublist in product_tags_nested for tag in sublist]))
# print(f"Unique flattened tags (lowercase): {unique_tags_flat}")
>```
>**Example: Creating a matrix (list of lists)**
>```python
#matrix = [[row * col for col in range(1, 4)] for row in range(1, 4)]
## matrix will be [1*1, 1*2, 1*3] ->
## matrix will be [2*1, 2*2, 2*3] ->
## matrix will be [3*1, 3*2, 3*3] ->
#print(f"Generated matrix:\n{matrix}")
>```
>While powerful, deeply nested list comprehensions can sometimes become hard to read. For very complex nesting, traditional `for` loops might be clearer.

## 2. Dictionary Comprehensions
-   **Purpose:** Create a new [[Python_Dictionary|dictionary]] from an iterable.
-   **Syntax:**
    ```python
    {key_expression: value_expression for item in iterable if condition}
    ```
**Example: Create a dictionary of product names and their lengths**
```python
#product_names = ["Laptop", "Mouse", "Keyboard", "Monitor"]
#name_lengths = {name: len(name) for name in product_names}
#print(f"Product name lengths: {name_lengths}")
## Output: {'Laptop': 6, 'Mouse': 5, 'Keyboard': 8, 'Monitor': 7}

# Create a dictionary of products with price > 50
#product_prices = {"Laptop": 1200, "Mouse": 25, "Keyboard": 75, "Webcam": 45}
#expensive_products = {name: price for name, price in product_prices.items() if price > 50}
#print(f"Expensive products: {expensive_products}")
## Output: {'Laptop': 1200, 'Keyboard': 75}
```

## 3. Set Comprehensions
-   **Purpose:** Create a new [[Python_Set_Frozenset|set]] (containing unique elements) from an iterable.
-   **Syntax:**
    ```python
    {expression for item in iterable if condition}
    ```
    Note the use of curly braces `{}` but without key-value pairs like dictionaries.

**Example: Get unique uppercase first letters of product categories**
```python
#product_categories_list = ["electronics", "books", "apparel", "electronics", "home goods", "books"]
#unique_first_letters_upper = {category.upper() for category in product_categories_list}
#print(f"Unique uppercase first letters: {unique_first_letters_upper}")
## Output (order may vary): {'APPAREL', 'BOOKS', 'ELECTRONICS', 'HOME GOODS'}
```

## 4. Generator Expressions
-   **Purpose:** Create a **generator object**, which is an iterator that produces items on demand (lazily).
-   **Syntax:** Similar to list comprehension but uses parentheses `()` instead of square brackets `[]`.
    ```python
    (expression for item in iterable if condition)
    ```
-   **Benefits:**
    -   **Memory Efficient:** Does not create the entire collection in memory at once. Values are generated one by one as needed. This is very useful for large datasets.
    -   **Lazy Evaluation:** Computation is deferred until the generator is iterated over.
-   **Use Cases:** When you need to iterate over a sequence once (e.g., in a `for` loop, or as an argument to functions like `sum()`, `min()`, `max()`) and don't need to store the entire sequence in memory.

**Example: Sum of squares of numbers without creating a full list**
```python
#large_number_range = range(1, 1000001) # Represents a large sequence

# Generator expression for squares
#squares_generator = (x**2 for x in large_number_range)
#print(f"Generator object: {squares_generator}")

# Summing the squares using the generator (efficient)
#total_sum_of_squares = sum(squares_generator)
#print(f"Sum of squares (1 to 1,000,000): {total_sum_of_squares}") 
# This avoids creating a list of a million squared numbers in memory.

# If you did:
# squares_list = [x**2 for x in large_number_range] # Creates a very large list in memory
# total_sum_from_list = sum(squares_list)
```

Comprehensions and generator expressions are powerful tools in Python for creating collections and iterators in a concise, readable, and often efficient manner.

---
````

`````markdown

Filename: 100_Python/Python_Functions/Python_Decorators.md
````markdown
---
tags: [python, functions, decorators, metaprogramming, higher_order_functions, closures, concept, example]
aliases: [Python Decorator Syntax, @decorator]
related:
  - "[[100_Python/Python_Functions/_Python_Functions_MOC|_Python_Functions_MOC]]"
  - "[[Python_Higher_Order_Functions]]" # Decorators are HOFs
  - "[[Python_Nested_Functions_Closures|Python Nested Functions and Closures]]" # Decorators rely on closures
  - "[[Python_Args_Kwargs|*args and **kwargs]]" # Often used in decorator wrappers
  - "[[functools_wraps|functools.wraps]]" # Placeholder for preserving metadata
worksheet: [WS18]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
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
`````

This covers Lambda Functions, Comprehensions, and Decorators from WS18. Next, I will address the built-in functions `map()`, `filter()`, and `reduce()` and the remaining questions from WS18.

Okay, continuing with the Python Functions (WS18) section, focusing on the built-in functions `map()`, `filter()`, `reduce()`, and the remaining questions.

---

`````markdown

Filename: 100_Python/Python_Built_Ins/map_function.md
````markdown
---
tags: [python, built_in_function, map, higher_order_function, functional_programming, iterator, concept, example]
aliases: [map(), Python map function]
related:
  - "[[Built_In_Functions_Python]]"
  - "[[Python_Higher_Order_Functions]]" # map is a HOF
  - "[[Python_Lambda_Functions]]" # Often used with map
  - "[[Python_List_Comprehensions|List Comprehensions]]" # Often an alternative to map
  - "[[Python_Iterators_Generators|Iterators and Generators]]" # map returns an iterator
worksheet: [WS18]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Python: `map(function, iterable, ...)` Built-in Function

The `map()` function is a built-in [[Python_Higher_Order_Functions|higher-order function]] that applies a given `function` to each item of one or more `iterable`(s) (e.g., list, tuple, string) and returns an **iterator** that yields the results.

## Syntax
```python
map(function, iterable1, iterable2, ...)
```
-   `function`: A function that takes as many arguments as there are iterables passed. This function will be called for each item from the iterable(s).
-   `iterable1, iterable2, ...`: One or more iterable objects.
    -   If multiple iterables are provided, `function` must take that many arguments, and it will be called with corresponding items from each iterable in parallel. The iteration stops when the shortest iterable is exhausted.

## Behavior
-   `map()` does not execute the function immediately for all items. It returns an **iterator** (a `map` object).
-   The actual computation (calling `function` on items) happens lazily, as you iterate over the `map` object (e.g., in a `for` loop, or by converting it to a list using `list()`).
-   It does not modify the original iterable(s).

## Return Value
-   An **iterator** that yields the results of applying `function` to each item of the input iterable(s).

## Examples

**1. Applying a function to a single iterable (e.g., product prices):**
```python
# Product prices in USD
prices_usd = 
# Function to convert USD to EUR (conceptual rate)
def usd_to_eur(price_usd):
    return round(price_usd * 0.92, 2)

prices_eur_iterator = map(usd_to_eur, prices_usd)

print(f"Map object: {prices_eur_iterator}")
# To see the results, convert the iterator to a list or iterate over it:
prices_eur_list = list(prices_eur_iterator)
print(f"Prices in EUR: {prices_eur_list}")
# Output:
# Map object: <map object at 0x...>
# Prices in EUR: [18.39, 45.54, 110.4, 23.46, 69.0]
```

**2. Using a [[Python_Lambda_Functions|lambda function]] with `map()`:**
This is very common for simple, one-off operations.
```python
# Product names
product_names = ["SuperWidget", "MegaGadget", "BasicTool"]

# Convert all product names to uppercase
uppercase_names_iterator = map(lambda name: name.upper(), product_names)
print(f"Uppercase names: {list(uppercase_names_iterator)}")
# Output: ['SUPERWIDGET', 'MEGAGADGET', 'BASICTOOL']
```

**3. Using `map()` with multiple iterables:**
The function must accept a corresponding number of arguments.
```python
# Product quantities and per-item prices
quantities = 
unit_prices = 
# Function to calculate total cost for each product type
def calculate_item_total(qty, price):
    return qty * price

total_costs_iterator = map(calculate_item_total, quantities, unit_prices)
print(f"Total costs for each item type: {list(total_costs_iterator)}")
# Output: [200, 750, 2400] (10*20, 15*50, 30*80)
```
If iterables are of different lengths, `map()` stops when the shortest iterable is exhausted.
```python
list_a = [1, 2, 3, 4]
list_b = [10, 20]
# 'sum_corresponding' will be called for (1,10) and (2,20)
sum_iterator = map(lambda x, y: x + y, list_a, list_b)
print(f"Sum of corresponding elements (shortest iterable limits): {list(sum_iterator)}")
# Output: [11, 22]
```

## `map()` vs. [[Python_Comprehensions|List Comprehensions]]
For many common use cases, list comprehensions can achieve the same result as `map()` and are often considered more Pythonic and readable by some.
-   **`map()` with lambda:** `list(map(lambda x: x * 2, numbers))`
-   **List Comprehension:** `[x * 2 for x in numbers]`

**Advantages of List Comprehensions over `map()` for simple cases:**
-   Often more concise and easier to read for straightforward transformations.
-   Can directly include filtering logic (`[x*2 for x in numbers if x > 0]`). With `map()`, you'd typically chain it with `filter()`.

**When `map()` might be preferred:**
-   When the transformation function is already defined (a named function) and you want to apply it directly.
-   When working with multiple iterables in parallel.
-   When an iterator is explicitly desired for memory efficiency with very large datasets, though generator expressions `(x * 2 for x in numbers)` also provide this.

The `map()` function is a powerful tool from functional programming paradigms, useful for applying a transformation to every element of an iterable.

---````

`````markdown

Filename: 100_Python/Python_Functions/Python_filter_function.md
````markdown
---
tags: [python, built_in_function, filter, higher_order_function, functional_programming, iterator, concept, example]
aliases: [filter(), Python filter function]
related:
  - "[[Built_In_Functions_Python]]"
  - "[[Python_Higher_Order_Functions]]" # filter is a HOF
  - "[[Python_Lambda_Functions]]" # Often used with filter
  - "[[Python_List_Comprehensions|List Comprehensions]]" # Often an alternative to filter
  - "[[Python_Iterators_Generators|Iterators and Generators]]" # filter returns an iterator
worksheet: [WS18]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Python: `filter(function, iterable)` Built-in Function

The `filter()` function is a built-in [[Python_Higher_Order_Functions|higher-order function]] that constructs an **iterator** from elements of an `iterable` for which a given `function` returns true.

## Syntax
```python
filter(function, iterable)```
-   `function`: A function that takes one argument (an element from the `iterable`) and returns a boolean value (`True` or `False`). If `function` is `None`, `filter()` removes items from the iterable that are "falsey" (e.g., `0`, `False`, `None`, empty sequences/mappings).
-   `iterable`: An iterable object (e.g., list, tuple, string, set, dictionary keys/values) whose elements will be tested by `function`.

## Behavior
-   `filter()` does not execute the `function` immediately for all items. It returns an **iterator** (a `filter` object).
-   The actual filtering (calling `function` on items) happens lazily, as you iterate over the `filter` object (e.g., in a `for` loop, or by converting it to a list using `list()`).
-   It does not modify the original iterable.

## Return Value
-   An **iterator** that yields only those elements from `iterable` for which `function(element)` is true.

## Examples

>[!question] Give examples of `filter()` Function usage.

**1. Filtering even numbers from a list of product quantities:**
```python
product_quantities = 
# Function to check if a number is even
def is_even(number):
    return number % 2 == 0

even_quantities_iterator = filter(is_even, product_quantities)

print(f"Filter object: {even_quantities_iterator}")
# To see the results, convert the iterator to a list or iterate over it:
even_quantities_list = list(even_quantities_iterator)
print(f"Even quantities: {even_quantities_list}")
# Output:
# Filter object: <filter object at 0x...>
# Even quantities:
```

**2. Using a [[Python_Lambda_Functions|lambda function]] with `filter()`:**
This is very common for simple, one-off filtering conditions.
```python
# E-commerce product ratings
product_ratings = [4.5, 2.8, 3.9, 5.0, 1.2, 4.1, 4.8]

# Filter for high ratings (e.g., rating >= 4.0)
high_ratings_iterator = filter(lambda rating: rating >= 4.0, product_ratings)
print(f"High ratings: {list(high_ratings_iterator)}")
# Output: [4.5, 5.0, 4.1, 4.8]
```

**3. Filtering strings (e.g., product names starting with 'Super'):**
```python
product_names = ["SuperWidget", "MegaGadget", "BasicTool", "SuperCharger", "Accessory"]

super_products_iterator = filter(lambda name: name.startswith("Super"), product_names)
print(f"Super products: {list(super_products_iterator)}")
# Output: ['SuperWidget', 'SuperCharger']
```

**4. Using `None` as the function to filter out "falsey" values:**
If `function` is `None`, items are filtered if they are "falsey" in a boolean context (e.g., `0`, `False`, `None`, empty strings, empty lists).
```python
# Mixed data, some representing stock availability (0 means out of stock)
stock_levels = [10, 0, 25, None, 50, False, "In Stock"] # "In Stock" is truthy

# Filter for items considered "in stock" (non-falsey values)
# This is a bit of a conceptual stretch for stock_levels, better to filter explicitly
# but demonstrates the None behavior.
truthy_values_iterator = filter(None, stock_levels)
print(f"Truthy stock levels: {list(truthy_values_iterator)}")
# Output: [10, 25, 50, 'In Stock']
```

## `filter()` vs. [[Python_Comprehensions|List Comprehensions]] with an `if` clause
For many common use cases, list comprehensions (or generator expressions) with an `if` clause can achieve the same result as `filter()` and are often considered more Pythonic and readable.
-   **`filter()` with lambda:** `list(filter(lambda x: x > 0, numbers))`
-   **List Comprehension:** `[x for x in numbers if x > 0]`
-   **Generator Expression (returns iterator):** `(x for x in numbers if x > 0)`

**Advantages of List Comprehensions/Generator Expressions over `filter()`:**
-   Often more concise and directly expresses the intent of creating a new filtered collection or iterator.
-   Can combine filtering and mapping in one expression: `[x*2 for x in numbers if x > 0]`. With `filter()` and `map()`, this would require chaining them.

**When `filter()` might be preferred:**
-   When the filtering logic is complex and already defined in a named function.
-   In some functional programming styles or when working with existing code that uses it.

The `filter()` function is a classic tool from functional programming for selectively extracting elements from an iterable based on a condition.

---
````

`````markdown

Filename: 100_Python/Python_Built_Ins/reduce_function.md
````markdown
---
tags: [python, functools, reduce, higher_order_function, functional_programming, aggregation, iterator, concept, example]
aliases: [functools.reduce(), Python reduce function]
related:
  - "[[Built_In_Functions_Python]]"
  - "[[Python_Higher_Order_Functions]]" # reduce is a HOF
  - "[[Python_Lambda_Functions]]" # Often used with reduce
  - "[[Python_Loops_Iteration|Looping and Iteration]]" # reduce can often be replaced by a loop
worksheet: [WS18]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Python: `functools.reduce(function, iterable[, initializer])`

The `reduce()` function is part of the `functools` module in Python's standard library. It is a [[Python_Higher_Order_Functions|higher-order function]] that applies a binary `function` (a function taking two arguments) cumulatively to the items of an `iterable`, from left to right, so as to reduce the iterable to a single accumulated value.

**Note:** `reduce()` was a built-in function in Python 2. In Python 3, it was moved to the `functools` module, so you need to import it: `from functools import reduce`.

## Syntax
```python
from functools import reduce

reduce(function, iterable, initializer=None)
```
-   `function`: A function that takes two arguments and returns a single value. This function will be applied cumulatively.
-   `iterable`: An iterable object (e.g., list, tuple) whose elements will be reduced.
-   `initializer` (optional): If provided, it is placed before the items of the iterable in the calculation and serves as a default when the iterable is empty.

## Behavior
1.  If `initializer` is **not** provided:
    -   The `function` is first applied to the first two items of the `iterable`.
    -   The result of this call then becomes the first argument to `function`, and the third item from `iterable` becomes the second argument.
    -   This process continues until all items in `iterable` have been processed.
    -   If `iterable` is empty, a `TypeError` is raised.
    -   If `iterable` has only one item, that item is returned without calling `function`.
2.  If `initializer` **is** provided:
    -   The `function` is first applied to `initializer` and the first item of `iterable`.
    -   The result of this call then becomes the first argument to `function`, and the second item from `iterable` becomes the second argument.
    -   This continues until all items in `iterable` have been processed.
    -   If `iterable` is empty, the `initializer` is returned.

## Return Value
-   The single, accumulated result of applying `function` cumulatively to the items of `iterable`.

## Examples

**1. Summing all numbers in a list (e.g., total quantity of products sold):**
```python
from functools import reduce
import operator # For common operator functions like operator.add

daily_units_sold = 
# Using a lambda function
total_units_lambda = reduce(lambda x, y: x + y, daily_units_sold)
print(f"Total units sold (lambda): {total_units_lambda}") # Output: 125

# Using operator.add for clarity and potential minor efficiency
total_units_operator = reduce(operator.add, daily_units_sold)
print(f"Total units sold (operator.add): {total_units_operator}") # Output: 125

# With an initializer (e.g., starting sum from 100)
total_units_with_initial = reduce(lambda x, y: x + y, daily_units_sold, 100)
print(f"Total units with initial 100: {total_units_with_initial}") # Output: 225
```

**2. Finding the maximum value in a list (e.g., peak daily sales):**
```python
from functools import reduce

# daily_sales_figures = 
# Using a lambda
# peak_sale_lambda = reduce(lambda x, y: x if x > y else y, daily_sales_figures)
# print(f"Peak daily sale (lambda): {peak_sale_lambda}") # Output: 150

# A more direct way for max is the built-in max() function
# print(f"Peak daily sale (built-in max()): {max(daily_sales_figures)}")
```
While `reduce` can do this, `max()` is more direct and readable for finding the maximum.

**3. Concatenating a list of strings (e.g., product tags):**
```python
from functools import reduce

product_tags_list = ["electronics", "wearable", "smartwatch", "fitness"]
concatenated_tags = reduce(lambda x, y: x + " | " + y, product_tags_list)
print(f"Concatenated tags: '{concatenated_tags}'")
# Output: 'electronics | wearable | smartwatch | fitness'
```
For string concatenation, `' | '.join(product_tags_list)` is usually more Pythonic and efficient.

## `reduce()` vs. `map()` vs. `filter()`

>[!question] What is the difference between the `map()` and `reduce()` functions?
>
>[list2mdtable|#map vs reduce vs filter]
>- Feature
>    - [[Built_In_Functions_Python#map_function|`map(func, iter)`]]
>        - `reduce(func, iter)`
>            - [[Built_In_Functions_Python#filter_function|`filter(func, iter)`]]
>- **Purpose**
>    - Applies `func` to each element of `iter` independently. Transforms each element.
>        - Cumulatively applies a binary `func` to the elements of `iter` to reduce it to a single value.
>            - Selects elements from `iter` for which `func` returns `True`.
>- **Input `func`**
>    - Takes one argument (or more if multiple iterables).
>        - Takes two arguments (accumulator, current_element).
>            - Takes one argument, returns a boolean.
>- **Output**
>    - Returns an iterator of the same length as the input iterable (or shortest if multiple). Each element is transformed.
>        - Returns a single accumulated value.
>            - Returns an iterator containing a subset of the original iterable's elements.
>- **Common Use**
>    - Element-wise transformation (e.g., squaring numbers, converting strings to uppercase).
>        - Aggregation (e.g., sum, product, finding min/max by accumulation).
>            - Selection/Filtering (e.g., getting all even numbers, filtering out None values).
>
>**Analogy (E-commerce Order Processing):**
>-   `map()`: Applying a 10% discount to the price of *each item* in an order.
>-   `filter()`: Selecting only the *items that are currently in stock* from an order.
>-   `reduce()`: Calculating the *total sum* of prices for all items in an order.

## Readability and Alternatives
Guido van Rossum (creator of Python) has mentioned that `reduce()` can be less readable than an explicit `for` loop for many common use cases like summing or finding a product, which is why it was moved to `functools`.
-   For summing: `sum(iterable)` is preferred.
-   For product: `math.prod(iterable)` (Python 3.8+).
-   For many other reductions, an explicit `for` loop might be clearer:
    ```python
    # total = 0
    # for x in my_list:
    #     total += x
    # is often clearer than reduce(lambda x, y: x + y, my_list) for simple summation.
    ```

However, `reduce()` remains a powerful tool for certain complex cumulative operations or when adhering to a more functional programming style.

---
````

`````markdown

Filename: 100_Python/Python_Functions/Python_Expression_vs_Statement.md
````markdown
---
tags: [python, programming_fundamentals, expression, statement, syntax, concept_comparison]
aliases: [Python Expressions, Python Statements, Expression vs Statement]
related:
  - "[[100_Python/Python_Functions/_Python_Functions_MOC|_Python_Functions_MOC]]"
  - "[[Python_Lambda_Functions]]" # Lambdas can only contain expressions
worksheet: [WS18]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
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
`````

This completes the notes for WS18 (Functions). Next, I will move to **WS19 - Scopes and Modules**.

Okay, let's move on to **WS19 - Python Scopes and Modules**. I'll start by creating the MOC for this section and then the detailed notes for the keywords, built-in functions, and questions.

---

### Python Scopes and Modules (WS19) - Folder and MOC

`````markdown

Filename: 100_Python/Python_Scopes_Modules/_Python_Scopes_Modules_MOC.md
````markdown
---
tags: [python, scope, namespace, module, import, legb, concept, moc]
aliases: [Python Scopes MOC, Python Modules MOC, Python Namespaces MOC]
related:
  - "[[100_Python/_Python_Programming_MOC|_Python_Programming_MOC]]"
  - "[[Python_LEGB_Rule|LEGB Rule (Scope Resolution)]]"
  - "[[Python_Namespaces|Namespaces]]"
  - "[[Python_Modules_Packages|Modules and Packages]]"
  - "[[Python_Import_System|The `import` System (`import`, `from ... import`)]]"
  - "[[Python_global_Keyword|`global` Keyword]]"
  - "[[Python_nonlocal_Keyword|`nonlocal` Keyword (from Functions MOC)]]"
  - "[[Python_dunder_name|`__name__` Special Variable]]"
  - "[[Python_Script_vs_Module|Executing Modules as Scripts (`if __name__ == '__main__':`)]]"
  - "[[Python_Built_In_Modules_OS|OS Module]]"
  - "[[Python_Built_In_Modules_Sys|sys Module]]"
worksheet: [WS19]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Python Scopes and Modules MOC 📦🔍

This section delves into how Python manages names (variables, functions, classes) using **scopes** and **namespaces**, and how code is organized into reusable units called **modules** and packages. Understanding these concepts is crucial for writing well-structured, maintainable, and conflict-free Python programs.

## Core Concepts
-   [[Python_Scopes_Visibility|Scopes and Visibility]]
    -   What is a scope? How does it define the visibility of a name?
-   [[Python_Namespaces|Namespaces]]
    -   What are namespaces? How Python uses them to avoid name collisions.
    -   Operations in Python that create names in namespaces.
-   [[Python_LEGB_Rule|LEGB Rule (Scope Resolution)]]
    -   The order Python follows to look up names: Local, Enclosing function locals, Global, Built-in.
-   [[Python_global_Keyword|The `global` Keyword]]
    -   Accessing and modifying global variables from within a function.
    -   Why modifying globals is often discouraged.
-   [[Python_Nested_Functions_Closures#The nonlocal Keyword|The `nonlocal` Keyword]] (Covered in Functions)
    -   Modifying variables in an enclosing function's scope.
-   [[Python_Modules_Packages|Modules and Packages]]
    -   Organizing code into reusable files (modules) and directories (packages).
    -   Advantages of modularizing code.
-   [[Python_Import_System|The `import` System]]
    -   `import module_name`
    -   `from module_name import specific_name`
    -   `from module_name import *` (and its dangers)
    -   Absolute vs. Relative imports.
-   [[Python_dunder_name|The `__name__` Special Variable]]
-   [[Python_Script_vs_Module|Executing Modules as Scripts (`if __name__ == '__main__':`)]]
    -   How to make a module runnable as a script.
-   [[Python_reload_function|`importlib.reload()` (formerly `reload()`)]]

## Built-in Functions & Modules Related to Scope/Modules
-   [[Built_In_Functions_Python#globals()|`globals()`]]
-   [[Built_In_Functions_Python#locals()|`locals()`]]
-   [[Python_Built_In_Modules_OS|`os` Module]] (Overview)
-   [[Python_Built_In_Modules_Sys|`sys` Module]] (Overview, including `sys.argv`, `sys.path`)

## Notes in this Section
```dataview
LIST
FROM "100_Python/Python_Scopes_Modules"
WHERE file.folder = this.file.folder AND file.name != this.file.name AND !contains(file.name, "MOC")
SORT file.name ASC
```

---
````

Now, creating notes for the keywords, built-ins, and questions from WS19.

`````markdown

Filename: 100_Python/Python_Scopes_Modules/Python_Scopes_Visibility.md
````markdown
---
tags: [python, scope, visibility, namespace, legb, concept, programming_fundamentals]
aliases: [Python Scope, Name Visibility Python]
related:
  - "[[100_Python/Python_Scopes_Modules/_Python_Scopes_Modules_MOC|_Python_Scopes_Modules_MOC]]"
  - "[[Python_Namespaces]]"
  - "[[Python_LEGB_Rule]]"
  - "[[Python_global_Keyword]]"
  - "[[Python_Nested_Functions_Closures|nonlocal Keyword]]"
worksheet: [WS19]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Python: Scopes and Visibility

## What is a Scope?
In Python, a **scope** is a region of a program where a particular [[Python_Namespaces|namespace]] is directly accessible. A namespace is a mapping from names (identifiers like variable names, function names, class names) to objects. Scopes define the "visibility" or "accessibility" of these names.

When you refer to a name (e.g., use a variable `x`), Python searches through a sequence of scopes to find the object that name refers to. This search order is defined by the [[Python_LEGB_Rule|LEGB rule]].

## Types of Scopes in Python
Python has primarily four types of scopes:

1.  **Local (L):**
    -   The innermost scope, containing names defined **inside the current function**.
    -   When a function is called, a new local scope is created for that call.
    -   Parameters passed to the function are also in its local scope.
    -   Names assigned within the function (that are not declared `global` or `nonlocal`) belong to this local scope.
    -   This scope is destroyed when the function returns.

2.  **Enclosing function locals (E):**
    -   This scope exists for **[[Python_Nested_Functions_Closures|nested functions]]**.
    -   If a function is defined inside another function (the enclosing function), the nested function has access to the names in the local scope of its enclosing function(s).
    -   Python searches these enclosing scopes from the innermost enclosing scope outwards.

3.  **Global (G):**
    -   The scope of the **module** in which the code is currently running.
    -   Names defined at the top level of a module (outside any function or class) are in the global scope of that module.
    -   Each module has its own global scope.

4.  **Built-in (B):**
    -   The outermost scope, containing pre-defined names that are always available in Python without needing to be imported.
    -   Examples: `len()`, `print()`, `str()`, `list()`, `Exception` types like `ValueError`, `TypeError`.

## Visibility of Names

>[!question] How do you define the scope or visibility of a name?
>The scope or visibility of a name in Python is determined by **where that name is assigned or defined** within the code structure.
>
>1.  **Assignment within a function (`def` or `lambda`):** If a name is assigned a value inside a function (and not declared `global` or `nonlocal`), it becomes a **local** name to that function. Its visibility is limited to that function's body.
>    ```python
>    def my_func():
>        local_var = 10 # local_var is local to my_func
>        print(local_var)
>    # print(local_var) # This would cause a NameError
>    ```
>2.  **Parameters of a function:** Function parameters are also **local** to that function.
>    ```python
>    def another_func(param): # param is local to another_func
>        print(param)
>    ```
>3.  **Assignment within a nested function:** If a name is assigned within a nested function without `nonlocal` or `global`, it's local to that nested function. If `nonlocal` is used, it refers to a name in an enclosing function's scope. If `global` is used, it refers to a name in the module's global scope.
>4.  **Assignment at the top level of a module:** If a name is assigned outside of any function or class definition within a module file, it becomes a **global** name within that module. It's visible throughout that module and can be imported by other modules.
>    ```python
>    # my_module.py
>    global_module_var = 100 # global within my_module
>    def some_func():
>        print(global_module_var) # Accesses the module's global
>    ```
>5.  **Class definitions (`class`):** Names assigned inside a class definition (but outside methods) are class attributes. Names assigned inside methods (using `self.name = ...`) are instance attributes. These have their own scoping rules related to classes and instances.
>6.  **Import statements:** `import module_name` makes the `module_name` itself available in the current scope. `from module_name import name` brings `name` directly into the current scope.
>
>The [[Python_LEGB_Rule|LEGB rule]] then dictates how Python searches for these names when they are accessed (read).

## Scope Resolution (LEGB Rule)
When Python encounters a name, it tries to resolve it by searching the scopes in the following order:
1.  **L**ocal: The current function's local scope.
2.  **E**nclosing function locals: Scopes of any enclosing functions, from innermost to outermost.
3.  **G**lobal: The global scope of the current module.
4.  **B**uilt-in: The scope containing built-in functions and constants.

If the name is not found after searching all these scopes, a `NameError` exception is raised.

**Example Illustrating LEGB:**
```python
# Built-in scope
# print("This is from built-in scope:", len) 

# Global scope
x_global = "I am global"

def outer_function():
    # Enclosing function local scope for inner_function
    x_enclosing = "I am enclosing"
    
    def inner_function():
        # Local scope
        x_local = "I am local"
        print(x_local)       # Accesses L
        print(x_enclosing)   # Accesses E
        print(x_global)      # Accesses G
        print(len("test"))   # Accesses B (len is built-in)
    
    inner_function()
    # print(x_local) # NameError: x_local not defined in outer_function's scope

# outer_function()
# print(x_enclosing) # NameError: x_enclosing not defined in global scope
```

Understanding scopes is fundamental for writing correct Python code, avoiding `NameError` exceptions, and managing where variables are accessible and how they might be shadowed or modified.

---
````

`````markdown

Filename: 100_Python/Python_Scopes_Modules/Python_Namespaces.md
````markdown
---
tags: [python, namespace, scope, identifier, mapping, concept, programming_fundamentals]
aliases: [Python Namespace, Name Binding Python]
related:
  - "[[Python_Scopes_Visibility]]"
  - "[[Python_LEGB_Rule]]"
  - "[[Python_Modules_Packages|Modules (each module has its own namespace)]]"
  - "[[Python_OOP_MOC|Classes and Objects (each instance has its own namespace)]]" # Placeholder
worksheet: [WS19]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Python: Namespaces

A **namespace** in Python is a system that ensures that all names (identifiers like variable names, function names, class names) in a program are unique and can be used without conflict. Think of it as a dictionary where keys are the names and values are the objects those names refer to.

Different namespaces can coexist at the same time, and names in one namespace do not clash with identical names in another namespace.

## Concept of Namespaces
-   **Mapping:** A namespace is essentially a mapping from names to objects.
-   **Context:** Each namespace provides a context for names. The same name can exist in different namespaces and refer to different objects. For example, a function might have a local variable `x`, and there might also be a global variable `x` in the module; these are distinct.
-   **Lifetime:** Namespaces are created at different moments and have different lifetimes:
    -   The **built-in namespace** (containing functions like `len()`, `print()`, and built-in exception names) is created when the Python interpreter starts and is never deleted.
    -   The **global namespace** for a module is created when the module definition is read in; normally, module namespaces also last until the interpreter quits.
    -   The **local namespace** for a function is created when the function is called, and deleted when the function returns or raises an unhandled exception.

## When are Namespaces Created?
-   When the Python interpreter starts (built-in namespace).
-   When a module is imported or run (global namespace for that module).
-   When a function is called (local namespace for that function call).
    -   [[Python_Nested_Functions_Closures|Nested functions]] create nested local namespaces.
-   When a class is defined (local namespace within the class definition, attributes become part of class/instance namespace).
-   When an object instance is created (instance attributes form a namespace for that object).

>[!question] What operations in Python create names in namespaces?
>Names are introduced into namespaces through various operations:
>
>1.  **Assignments:**
>    -   Direct assignment: `x = 10` (creates or rebinds `x` in the current local or global scope).
>    -   Augmented assignment: `x += 1` (if `x` doesn't exist, it might create it, depending on context, or raise `NameError`).
>2.  **Function Definitions (`def`):**
>    -   `def my_function(param1, param2): ...` creates the name `my_function` in the current scope (usually global or enclosing function local).
>    -   Function parameters (`param1`, `param2`) are bound to names in the function's local namespace when the function is called.
>3.  **Class Definitions (`class`):**
>    -   `class MyClass: ...` creates the name `MyClass` in the current scope.
>    -   Names assigned within the class body (but outside methods) become class attributes.
>    -   Names assigned to `self` within methods (e.g., `self.instance_var = value`) create instance attributes in the instance's namespace.
>4.  **`import` Statements:**
>    -   `import my_module`: Creates the name `my_module` in the current namespace, referring to the module object.
>    -   `from my_module import some_name`: Creates `some_name` directly in the current namespace, referring to the object `some_name` from `my_module`.
>    -   `from my_module import another_name as alias_name`: Creates `alias_name` in the current namespace.
>5.  **`for` Loop Variables:**
>    -   `for item in iterable: ...` assigns each element of `iterable` to the name `item` in the current scope (often local to a function, or global if the loop is at module level).
>6.  **`with ... as name:` (Context Managers):**
>    -   `with open('file.txt') as f: ...` binds the name `f` to the file object within the `with` block's scope.
>7.  **`except ... as name:` (Exception Handling):**
>    -   `try: ... except ValueError as e: ...` binds the name `e` to the exception instance within the `except` block.
>8.  **List/Set/Dictionary Comprehensions and Generator Expressions (Variables within them):**
>    -   In Python 3.x, variables used in comprehensions (e.g., `x` in `[x*x for x in range(5)]`) have their own scope and do not "leak" into the surrounding scope. In Python 2.x, they did leak.

These operations are how names get associated with objects within specific namespaces. The [[Python_Scopes_Visibility|scope]] then determines where these names are accessible.

## Relationship with Scopes
-   A **scope** is a textual region of a Python program where a namespace is directly accessible.
-   At any point in execution, there are at least three nested scopes whose namespaces are directly accessible:
    1.  The innermost scope, which is searched first, contains the local names.
    2.  The scopes of any enclosing functions, which are searched starting with the nearest enclosing scope.
    3.  The next-to-last scope contains the current module’s global names.
    4.  The outermost scope (searched last) is the namespace containing built-in names.
    (This is the [[Python_LEGB_Rule|LEGB rule]]).

**Example:**
```python
# Module's global namespace
global_var = "I am global in this module"

def outer_func():
    # Enclosing namespace for inner_func
    enclosing_var = "I am in outer_func's local (enclosing for inner) namespace"
    
    def inner_func():
        # Local namespace for inner_func
        local_var = "I am local to inner_func"
        print(local_var)         # Accesses inner_func's local namespace
        print(enclosing_var)     # Accesses outer_func's local namespace
        print(global_var)        # Accesses module's global namespace
        print(len("hello"))      # Accesses built-in namespace for 'len'
    
    inner_func()

# outer_func()
```
Each call to `outer_func` creates a new local namespace for it, and each call to `inner_func` (within `outer_func`) creates its own local namespace.

Namespaces are a fundamental concept for organizing code and preventing name conflicts in Python, allowing for modular and maintainable programs.

---
````

`````markdown

Filename: 100_Python/Python_Scopes_Modules/Python_LEGB_Rule.md
````markdown
---
tags: [python, scope, namespace, legb, name_resolution, concept, programming_fundamentals]
aliases: [LEGB Rule, Python Scope Resolution, Name Lookup Python]
related:
  - "[[Python_Scopes_Visibility]]"
  - "[[Python_Namespaces]]"
  - "[[Python_global_Keyword]]"
  - "[[Python_Nested_Functions_Closures|nonlocal Keyword]]"
worksheet: [WS19]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Python: LEGB Rule (Scope Resolution)

When Python encounters a name (variable, function, class) in your code, it needs to determine what object that name refers to. The **LEGB rule** is the sequence of [[Python_Namespaces|namespaces]] Python searches to find this object. LEGB stands for:

1.  **L**ocal
2.  **E**nclosing function locals
3.  **G**lobal
4.  **B**uilt-in

Python searches these scopes in this specific order. The first place a name is found is the one that is used. If the name is not found in any of these scopes, a `NameError` exception is raised.

>[!question] What is the order of lookup For names?
>The order of lookup for names in Python follows the LEGB rule:
>1.  **Local (L):** This is the current scope. If inside a function, it's the function's local namespace (including its parameters). If in a class definition, it's the class's local namespace.
>2.  **Enclosing function locals (E):** If the current scope is a nested function, Python searches the local scopes of all enclosing functions, from the innermost enclosing function outwards. This is how [[Python_Nested_Functions_Closures|closures]] work. This scope is skipped if not in a nested function.
>3.  **Global (G):** This is the namespace of the module containing the current code. Names defined at the top level of a module are global to that module.
>4.  **Built-in (B):** This namespace contains all of Python's built-in functions (`len()`, `print()`, `str()`, etc.) and built-in exception names. It's always available and searched last.

## Detailed Explanation of LEGB Scopes

[list2tab|#LEGB Scopes]
- L: Local Scope
    -   The names assigned within the currently executing function (including its parameters).
    -   This is the first place Python looks.
    -   When a function call ends, its local scope is typically destroyed.
    -   **Example:**
        ```python
        # def my_function(product_price):
        #     discount = 0.1 # 'discount' is local to my_function
        #     final_price = product_price * (1 - discount)
        #     print(final_price) # Looks for product_price, discount, final_price locally first
        ```
- E: Enclosing Function Locals Scope
    -   If a function is nested inside another function, the inner function can access names from the outer (enclosing) function's local scope.
    -   Python searches these enclosing scopes from the nearest one outwards until it reaches the module's global scope.
    -   This is what enables closures.
    -   **Example:**
        ```python
        # def outer_checkout(customer_type):
        #     # customer_type is in the enclosing scope for apply_special_discount
        #     base_discount = 0.05 

        #     def apply_special_discount(price):
        #         # price is local to apply_special_discount
        #         if customer_type == "VIP":
        #             # Accesses customer_type and base_discount from enclosing scope
        #             return price * (1 - (base_discount + 0.10)) 
        #         return price * (1 - base_discount)
            
        #     return apply_special_discount # Returns the inner function

        # vip_discounter = outer_checkout("VIP")
        # print(vip_discounter(100)) # vip_discounter "remembers" customer_type and base_discount
        ```
- G: Global Scope
    -   The namespace of the module from which the code is currently executing.
    -   Names defined at the top level of a `.py` file (outside any function or class) are in this global scope.
    -   Each module has its own distinct global scope.
    -   To modify a global variable from within a function, you must use the [[Python_global_Keyword|`global` keyword]].
    -   **Example:**
        ```python
        # tax_rate = 0.07 # tax_rate is global to this module

        # def calculate_total_with_tax(subtotal):
        #     total = subtotal * (1 + tax_rate) # Accesses global tax_rate
        #     return total
        
        # print(calculate_total_with_tax(100))
        ```
- B: Built-in Scope
    -   The outermost scope, containing names that are always available in Python without needing any imports.
    -   Includes functions like `len()`, `print()`, `int()`, `str()`, `list()`, `dict()`, `range()`, `type()`, built-in exceptions like `ValueError`, `TypeError`, and constants like `True`, `False`, `None`.
    -   This is the last scope searched.
    -   It's possible (though generally bad practice) to shadow a built-in name by defining a global or local variable with the same name.
    -   **Example:**
        ```python
        # my_items = ["apple", "banana"]
        # print(len(my_items)) # 'len' is found in the built-in scope
        
        # Bad practice: shadowing a built-in
        # str = "This is now a variable, not the str() function"
        # print(str(123)) # Would raise TypeError: 'str' object is not callable
        ```

## How the LEGB Rule Works
When a name is encountered:
1.  Python checks the **Local** scope. If found, it's used.
2.  If not in Local, and if inside a nested function, it checks the **Enclosing function local** scopes, from innermost to outermost. If found, it's used.
3.  If not found in Local or Enclosing, it checks the **Global** (module) scope. If found, it's used.
4.  If not found in Global, it checks the **Built-in** scope. If found, it's used.
5.  If the name is not found in any of these scopes, a `NameError` is raised.

**Example Illustrating Full LEGB Search:**
```python
# B: Built-in (print, len)
# G: Global
global_api_key = "XYZ123_GLOBAL"

def configure_api(api_version="v2"):
    # E: Enclosing for process_data
    enclosing_service_url = f"http://api.example.com/{api_version}"
    
    def process_data(data_payload):
        # L: Local
        local_batch_id = "BATCH001"
        print(f"Processing batch: {local_batch_id}") # L
        print(f"Service URL: {enclosing_service_url}") # E
        print(f"Using API Key: {global_api_key}") # G
        print(f"Payload length: {len(data_payload)}") # B (len is built-in)
        return True

    return process_data

# processor_v2 = configure_api()
# sample_payload = {"item_id": "P789", "quantity": 5}
# processor_v2(sample_payload)

# processor_v3 = configure_api(api_version="v3") # Creates a new closure
# processor_v3(sample_payload)
```

The LEGB rule is a fundamental concept that governs how Python resolves names, ensuring that variables and functions are accessed from the correct context.

---
`````

This covers Scopes, Namespaces, and the LEGB rule. Next, I'll create notes for the `global` keyword, `__name__`, modules/packages, the import system, and then the `os` and `sys` modules, integrating the remaining questions from WS19.

Okay, continuing with the Python Scopes and Modules (WS19) section.

---

`````markdown

Filename: 100_Python/Python_Scopes_Modules/Python_global_Keyword.md
````markdown
---
tags: [python, scope, global_keyword, variable_scope, namespace, concept, example]
aliases: [global statement python]
related:
  - "[[Python_Scopes_Visibility]]"
  - "[[Python_LEGB_Rule]]"
  - "[[Python_Namespaces]]"
  - "[[Python_Nested_Functions_Closures|nonlocal Keyword]]" # For modifying enclosing (non-global) scope
worksheet: [WS19]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Python: `global` Keyword

The `global` keyword in Python is used to declare that a variable inside a function refers to a variable in the **global scope** (i.e., the module-level scope), rather than creating a new local variable with the same name.

## Purpose
Normally, if you assign a value to a variable inside a function, Python creates that variable in the function's local scope. If you want to *modify* a global variable from within a function, you must explicitly tell Python that you are referring to the global variable using the `global` keyword.

-   **Reading Globals:** You can *read* the value of a global variable from within a function without the `global` keyword, as Python will find it via the [[Python_LEGB_Rule|LEGB rule]] if it's not found locally or in enclosing scopes.
-   **Modifying Globals:** To *assign to* or *change* a global variable from within a function, you **must** use `global variable_name` before the assignment.

## Syntax
```python
global variable_name1, variable_name2, ...
```
This statement is typically placed at the beginning of the function body.

## Behavior
-   The `global` statement tells Python that any assignments to the specified variable names within that function should affect the global variable of that name, not create a new local one.
-   If the global variable does not exist when `global` is declared and then an assignment is made, a new global variable is created.

## Examples

**1. Reading a global variable (no `global` keyword needed):**
```python
# Global variable for an e-commerce site's default currency
default_currency = "USD"

def display_product_price(price):
    # Reads the global 'default_currency'
    print(f"Price: {price} {default_currency}")

# display_product_price(29.99) # Output: Price: 29.99 USD
```

**2. Modifying a global variable (requires `global` keyword):**
```python
# Global counter for total items processed
total_items_processed = 0

def process_order(items_in_order):
    global total_items_processed # Declare intent to modify the global variable
    
    print(f"Processing {items_in_order} items...")
    total_items_processed += items_in_order # Modifies the global variable
    print(f"Current total items processed: {total_items_processed}")

# print(f"Initial total items: {total_items_processed}")
# process_order(5)
# process_order(3)
# print(f"Final total items: {total_items_processed}")
```
Output:```
Initial total items: 0
Processing 5 items...
Current total items processed: 5
Processing 3 items...
Current total items processed: 8
Final total items: 8
```

**3. What happens without `global` when trying to modify:**
If you try to assign to a variable inside a function that has the same name as a global variable *without* using the `global` keyword, Python creates a new *local* variable. If you try to read it before this local assignment, you might get an `UnboundLocalError`.

```python
# Global variable for site status
site_status = "Online"

def attempt_to_update_status_locally(new_status):
    # This creates a NEW LOCAL variable 'site_status', shadowing the global one.
    # It does NOT modify the global 'site_status'.
    site_status = new_status 
    print(f"Inside function, local site_status: {site_status}")

def problematic_update_status():
    # This will cause UnboundLocalError if site_status is not yet assigned locally
    # because Python sees an assignment to site_status later in the function,
    # so it treats site_status as local throughout this function.
    # print(f"Trying to read site_status before local assignment: {site_status}") # This line would error
    site_status = "Maintenance" # This makes site_status local
    print(f"Inside problematic_update_status, local site_status: {site_status}")


# print(f"Initial global site_status: {site_status}")
# attempt_to_update_status_locally("Maintenance Mode")
# print(f"Global site_status after local attempt: {site_status}") # Still "Online"

# try:
#     problematic_update_status()
# except UnboundLocalError as e:
#     print(f"Error in problematic_update_status: {e}") 
# print(f"Global site_status after problematic attempt: {site_status}") # Still "Online"
```

>[!question] Why is using and modifying global names generally considered to be bad programming practice?
>Modifying global variables from within functions is generally discouraged for several reasons:
>1.  **Reduced Readability and Maintainability:** It makes it harder to understand the flow of data and the state of the program. When a function modifies global state, its effects are not self-contained, and you have to look outside the function to understand its full impact. This can lead to "spaghetti code" where changes in one part of the code unexpectedly affect other parts.
>2.  **Increased Complexity:** Global variables create hidden dependencies between functions and modules. Changes to a global variable can have far-reaching and often unintended consequences, making debugging difficult.
>3.  **Testing Difficulties:** Functions that rely on or modify global state are harder to test in isolation. You need to set up the global state correctly before each test and potentially clean it up afterwards. Pure functions (that don't rely on or modify external state) are much easier to test.
>4.  **Namespace Pollution:** Overuse of global variables can clutter the global namespace, increasing the risk of name collisions, especially in larger projects or when integrating multiple modules.
>5.  **Reduced Reusability:** Functions that depend on specific global variables are less reusable in different contexts or projects where those globals might not exist or have different meanings.
>
>**Alternatives to Modifying Globals:**
>-   **Pass variables as arguments:** If a function needs some data, pass it as an argument.
>-   **Return values from functions:** If a function computes a value that needs to be used elsewhere, return it.
>-   **Use Classes and Objects:** For managing state that needs to be shared and modified by multiple methods, encapsulate it within a class using instance attributes. This provides better organization and control.
>-   **Configuration Objects/Modules:** For application-wide settings, use dedicated configuration objects or modules that can be imported and accessed in a controlled manner.
>
>While there might be rare, specific cases where modifying a global variable is a pragmatic solution (e.g., simple scripts, some caching mechanisms), it should generally be avoided in favor of more explicit and encapsulated ways of managing state.

The `global` keyword is a necessary tool if you *must* modify a global variable from within a function, but its use should be carefully considered due to the potential downsides to code clarity and maintainability.

---
`````

`````markdown

Filename: 100_Python/Python_Scopes_Modules/Python_Modules_Packages.md
````markdown
---
tags: [python, module, package, import, organization, code_reuse, namespace, concept]
aliases: [Python Modules, Python Packages, Code Organization Python]
related:
  - "[[100_Python/Python_Scopes_Modules/_Python_Scopes_Modules_MOC|_Python_Scopes_Modules_MOC]]"
  - "[[Python_Import_System]]"
  - "[[Python_Namespaces]]" # Each module has its own namespace
  - "[[Python_Script_vs_Module|Executing Modules as Scripts]]"
worksheet: [WS19]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Python: Modules and Packages

As Python programs grow larger and more complex, organizing code into manageable and reusable units becomes essential. Python uses **modules** and **packages** for this purpose.

## Modules
-   **Definition:** A **module** is simply a file containing Python definitions and statements. The file name is the module name with the suffix `.py` appended.
-   **Purpose:**
    -   **Code Organization:** Group related functions, classes, and variables together.
    -   **Reusability:** Code defined in a module can be used in other Python scripts or modules by [[Python_Import_System|importing]] it.
    -   **[[Python_Namespaces|Namespace Isolation]]:** Each module has its own private namespace (global scope). This prevents names defined in one module from conflicting with identical names in another module or in the main script.
-   **Example:**
    Let's say you have a file named `ecommerce_utils.py` with some utility functions for an e-commerce application:

    ```python
    # ecommerce_utils.py
    
    PI = 3.14159 # A global variable within this module
    
    def calculate_tax(price, tax_rate=0.05):
        """Calculates sales tax for a given price."""
        return price * tax_rate

    def format_price(price, currency_symbol="$"):
        """Formats a price with a currency symbol."""
        return f"{currency_symbol}{price:.2f}"

    class Product:
        def __init__(self, name, price):
            self.name = name
            self.price = price
        
        def display(self):
            print(f"Product: {self.name}, Price: {format_price(self.price)}")
    ```
    This `ecommerce_utils.py` file is a module named `ecommerce_utils`.

-   **Using a Module:** You use the `import` statement to access definitions from a module.
    ```python
    # main_script.py
    import ecommerce_utils # Imports the entire module

    subtotal = 100.00
    tax = ecommerce_utils.calculate_tax(subtotal, tax_rate=0.07)
    formatted_subtotal = ecommerce_utils.format_price(subtotal)
    
    print(f"Subtotal: {formatted_subtotal}, Tax: {ecommerce_utils.format_price(tax)}")
    
    my_product = ecommerce_utils.Product("Super TV", 799.99)
    my_product.display()
    print(f"Value of PI from module: {ecommerce_utils.PI}")
    ```
    When `import ecommerce_utils` is executed, Python runs the code in `ecommerce_utils.py` (if not already imported in the session) and creates a module object. Names defined at the top level in `ecommerce_utils.py` become attributes of this module object.

## Packages
-   **Definition:** A **package** is a way of structuring Python's module namespace by using "dotted module names". A package is essentially a collection of modules organized in a directory hierarchy.
-   **Structure:** A directory containing Python modules and a special file named `__init__.py` (which can be empty) is treated as a package. The `__init__.py` file indicates that the directory should be considered a package and can also contain initialization code for the package or specify modules to be exported.
-   **Purpose:**
    -   **Hierarchical Organization:** Allows organizing a large number of modules into a logical structure, preventing a flat and cluttered module namespace.
    -   **Further Namespace Isolation:** e.g., `mypackage.subpackage.module`.
-   **Example Structure:**
    ```
    my_app/
    ├── main.py
    └── ecommerce_system/             <-- Package directory
        ├── __init__.py
        ├── products/                 <-- Sub-package directory
        │   ├── __init__.py
        │   ├── inventory.py
        │   └── pricing.py
        ├── users/                    <-- Sub-package directory
        │   ├── __init__.py
        │   └── profiles.py
        └── utils.py                  <-- Module directly in ecommerce_system
    ```
-   **Importing from Packages:**
    ```python
    # In main.py

    # Option 1: Import specific module from package
    # import ecommerce_system.products.inventory
    # stock_level = ecommerce_system.products.inventory.get_stock("P123")

    # Option 2: Import module with an alias
    # import ecommerce_system.products.pricing as product_pricing
    # final_price = product_pricing.apply_discount(100, 0.1)

    # Option 3: Import specific names from a module within a package
    # from ecommerce_system.users.profiles import UserProfile
    # user = UserProfile("user001")

    # Option 4: If __init__.py in 'products' imports 'inventory' (e.g., from . import inventory)
    # import ecommerce_system.products
    # stock_level = ecommerce_system.products.inventory.get_stock("P123") 
    ```

>[!question] What are the advantages of modularizing a code?
>Modularizing code (breaking it down into modules and packages) offers several significant advantages:
>1.  **Organization:** Code becomes better organized and structured. Related functionalities are grouped together, making the codebase easier to navigate and understand.
>2.  **Reusability:** Modules and packages can be reused across different parts of a project or even in entirely different projects. This "Don't Repeat Yourself" (DRY) principle saves development time and effort.
>3.  **Maintainability:** Changes or bug fixes in one module are less likely to impact other unrelated parts of the application, assuming well-defined interfaces. This makes maintenance easier and reduces the risk of introducing new bugs.
>4.  **[[Python_Namespaces|Namespace Isolation]]:** Each module has its own global namespace. This prevents naming conflicts between identifiers (variables, functions, classes) defined in different modules. You can have a function named `calculate()` in `module_a` and another function named `calculate()` in `module_b` without issues (`module_a.calculate()` vs. `module_b.calculate()`).
>5.  **Collaboration:** Different developers or teams can work on different modules independently, reducing conflicts and improving development speed in larger projects.
>6.  **Testability:** Smaller, well-defined modules are generally easier to test in isolation (unit testing).
>7.  **Readability:** A well-modularized codebase is often easier to read and comprehend because concerns are separated.
>8.  **Scalability of Development:** As projects grow, modularity helps manage complexity and allows the system to scale in terms of features and codebase size.

Modules and packages are fundamental to writing clean, organized, and maintainable Python applications, especially as projects increase in size and complexity.

---
`````

`````markdown

Filename: 100_Python/Python_Scopes_Modules/Python_Import_System.md
````markdown
---
tags: [python, module, package, import, from_import, namespace, concept, syntax]
aliases: [Python Import Statement, from ... import, Python Module Importing]
related:
  - "[[Python_Modules_Packages]]"
  - "[[Python_Namespaces]]"
  - "[[Python_Script_vs_Module|Executing Modules as Scripts (`if __name__ == '__main__':`)]]"
  - "[[sys_module_python|sys.path]]" # Placeholder, where Python looks for modules
worksheet: [WS19]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Python: The `import` System

Python's `import` system allows you to bring definitions (functions, classes, variables) from one module or package into another module or into the interactive interpreter's scope. This is the primary mechanism for code reuse and modularization.

## Basic `import module_name`
-   **Syntax:** `import module_name` or `import package_name.module_name`
-   **Behavior:**
    1.  Python searches for `module_name.py` (or the package directory) in a list of directories defined by `sys.path` (which includes the directory of the input script, `PYTHONPATH` environment variable, and installation-dependent default paths).
    2.  If found, the code in the module is executed (if it's the first time being imported in the session).
    3.  A **module object** is created.
    4.  The name `module_name` (or the last part of a dotted package path) is bound in the current [[Python_Namespaces|namespace]] to this module object.
    5.  To access definitions within the imported module, you must use the module name as a prefix (attribute access): `module_name.definition_name`.
-   **Example:**
    ```python
    # Assume ecommerce_utils.py exists with:
    # def calculate_shipping(weight): return weight * 0.5

    import math # Built-in module
    import ecommerce_utils # Custom module

    # print(math.sqrt(16)) # Access sqrt via math.
    # shipping_cost = ecommerce_utils.calculate_shipping(10)
    # print(f"Shipping cost: {shipping_cost}")
    ```

## `from module_name import name1, name2, ...`
-   **Syntax:** `from module_name import name1`, `from module_name import name1 as alias1, name2`
-   **Behavior:**
    1.  The module `module_name` is loaded and executed (if not already).
    2.  The specified names (`name1`, `name2`, etc.) are directly bound into the current [[Python_Namespaces|namespace]].
    3.  You can then use `name1` directly without prefixing it with `module_name.`.
    4.  The module object itself is *not* bound to `module_name` in the current namespace (unless you also do a separate `import module_name`).
-   **Example:**
    ```python
    # from math import sqrt, pi
    # from ecommerce_utils import calculate_tax, Product

    # print(sqrt(25)) # Use sqrt directly
    # print(f"Value of pi: {pi}")
    # tax = calculate_tax(100)
    # my_item = Product("Widget", 19.99)
    ```

>[!question] Explain the difference between `import module` and `from <module name> import *`. Why is it dangerous to use a second Form of importing?
>
>[list2tab|#import vs from import *]
>- `import module_name`
>    -   **What it does:** Imports the module `module_name`. You must use `module_name.attribute` to access its contents.
>    -   **Namespace:** Introduces only one name (`module_name`) into the current namespace.
>    -   **Clarity:** Very clear where names are coming from (e.g., `math.pi` clearly indicates `pi` is from the `math` module).
>    -   **Name Clashes:** Less prone to name clashes, as attributes are accessed via the module's namespace.
>    -   **Example:**
>        ```python
>        # import math
>        # print(math.pi)
>        # print(math.sqrt(4))
>        ```
>- `from module_name import *`
>    -   **What it does:** Imports **all public names** (those not starting with an underscore `_`, or all names if the module defines `__all__`) from `module_name` directly into the current namespace. You can use these names directly without the module prefix.
>    -   **Namespace:** Can introduce many names into the current namespace, potentially overwriting existing names.
>    -   **Clarity:** Can make it unclear where a specific name originated, especially if multiple modules are imported this way. This reduces code readability and maintainability.
>    -   **Name Clashes:** High risk of name clashes. If the imported module defines a name that already exists in your current scope, the existing name will be overwritten silently. This can lead to subtle bugs that are hard to trace.
>    -   **Example:**
>        ```python
>        # from math import * # Imports pi, sqrt, sin, cos, etc., directly
>        # print(pi)
>        # print(sqrt(4))
>        #
>        # def sqrt(x): # This would overwrite the imported math.sqrt if defined after the import!
>        #     print("My custom sqrt!")
>        #     return x**0.5 
>        ```>
>**Why is `from module_name import *` dangerous (and generally discouraged by PEP 8)?**
>1.  **Namespace Pollution:** It dumps all imported names into your current namespace, making it crowded and harder to manage.
>2.  **Name Clashes:** It can silently overwrite names that already exist in your namespace or that are imported from other modules, leading to unexpected behavior and bugs.
>3.  **Reduced Readability:** It becomes difficult to tell where a particular name (function, variable, class) came from without looking at all the `import *` statements. This makes code harder to understand and maintain, especially for others (or your future self).
>4.  **Tooling Issues:** Static analysis tools (linters, type checkers) may have a harder time analyzing code that uses `import *`.
>
>**When might it be (cautiously) acceptable?**
>-   In the interactive interpreter (`>>>`) for convenience during exploration.
>-   Sometimes within a module's `__init__.py` to re-export names from submodules to make the package API flatter (though explicit re-exporting `from .submodule import name` is often preferred).
>-   Very rarely, for specific modules designed to be used this way (e.g., some parts of `tkinter`).
>
>In general, prefer `import module_name` or `from module_name import specific_name1, specific_name2` for clarity and to avoid namespace issues.

## Absolute vs. Relative Imports

>[!question] What is the difference between *absolute* import and *relative* import? When will you use each?
>
>[list2tab|#Absolute vs Relative Imports]
>- Absolute Imports
>    -   **Definition:** Specify the full path to the module from the project's root directory (or a directory in `sys.path`). They are "absolute" because they don't depend on the location of the current file.
>    -   **Syntax:** `import package.subpackage.module` or `from package.subpackage import name`.
>    -   **When to Use:**
>        -   This is the **recommended default** for most imports, especially for modules outside the current package or for top-level scripts.
>        -   They are clear, unambiguous, and make it easy to understand where a module is coming from regardless of the current file's location.
>        -   More robust to refactoring if you move files around (as long as the top-level package structure relative to `sys.path` remains).
>    -   **Example:**
>        Assuming a project structure:
>        ```
>        my_project/
>            main.py
>            ecommerce/
>                __init__.py
>                utils.py
>                products/
>                    __init__.py
>                    catalog.py
>        ```
>        In `main.py` or `ecommerce/products/catalog.py`, to import `utils.py`:
>        ```python
>        # Absolute import
>        import ecommerce.utils
>        from ecommerce.utils import helper_function
>        ```
>- Relative Imports
>    -   **Definition:** Specify the module to be imported *relative* to the location of the current module. They use leading dots (`.` or `..`) to indicate current and parent directories.
>    -   **Syntax:**
>        -   `from . import sibling_module` (imports `sibling_module` from the same package as the current module)
>        -   `from .sibling_module import name`
>        -   `from .. import parent_package_module` (imports `parent_package_module` from the parent package)
>        -   `from ..parent_package_module import name`
>    -   **When to Use:**
>        -   Primarily used for imports **within the same package**. They make it easier to reorganize the internal structure of a package without having to update import statements that refer to modules within that package.
>        -   They help avoid hardcoding the top-level package name within the package itself, making the package more self-contained and easier to rename or move.
>    -   **Cannot be used in top-level scripts:** Relative imports are meant for modules within packages. Trying to use them in a script that is run directly (i.e., when `__name__ == "__main__"`) will result in an `ImportError` because the notion of "current package" is not well-defined for top-level scripts.
>    -   **Example (inside `ecommerce/products/catalog.py`):**
>        To import `inventory.py` (assuming it's in the same `products` sub-package):
>        ```python
>        # In ecommerce/products/catalog.py
>        from . import inventory # Relative import for a sibling module
>        from .inventory import check_stock
>        
>        # To import utils.py from the parent 'ecommerce' package:
>        from ..utils import format_price 
>        ```
>
>**PEP 8 Recommendation:** Absolute imports are generally recommended for clarity and explicitness. However, relative imports are acceptable and often preferred for intra-package imports to make packages more self-contained and easier to refactor. Avoid complex relative imports like `from ...some_other_branch import name`.

## The Module Search Path (`sys.path`)
When an `import` statement is encountered, Python searches for the module in a list of directories specified by `sys.path`. This list typically includes:
1.  The directory containing the input script (or the current directory if running interactively).
2.  Directories listed in the `PYTHONPATH` environment variable (if set).
3.  Installation-dependent default paths (e.g., where standard library modules and site-packages are installed).

You can inspect `sys.path` to see where Python is looking:
```python
import sys
# print(sys.path)
```

The import system is a powerful feature that allows Python programs to be structured logically and to leverage a vast ecosystem of libraries.

---
``````

`````markdown

Filename: 100_Python/Python_Scopes_Modules/Python_dunder_name.md
````markdown
---
tags: [python, module, script, dunder_name, __name__, __main__, execution_context, concept]
aliases: [__name__ variable, Python __name__, if __name__ == "__main__"]
related:
  - "[[Python_Modules_Packages]]"
  - "[[Python_Import_System]]"
  - "[[Python_Script_vs_Module|Executing Modules as Scripts]]"
worksheet: [WS19]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Python: The `__name__` Special Variable

`__name__` (pronounced "dunder name," for double underscore name) is a special built-in variable in Python that is automatically set in every module. Its value depends on how the module is being used.

## Value of `__name__`

1.  **When a Module is Run Directly (as a Script):**
    -   If you execute a Python file directly (e.g., `python my_script.py`), the `__name__` variable within that script is set to the string `__main__`.
    -   This indicates that the script is the main program being run.

2.  **When a Module is Imported:**
    -   If a Python file is imported as a module into another script (e.g., `import my_module`), the `__name__` variable within `my_module.py` is set to the **name of the module itself** (as a string, e.g., `'my_module'`).

## The `if __name__ == "__main__":` Idiom

This common Python idiom leverages the behavior of the `__name__` variable to control code execution.

```python
# my_module.py

def helper_function():
    print("Helper function from my_module is called.")

def main_logic():
    print("Main logic of my_module is executing.")
    helper_function()

print(f"In my_module.py, __name__ is set to: {__name__}")

if __name__ == "__main__":
    # This block of code will ONLY execute if this script is run directly.
    # It will NOT execute if this module is imported by another script.
    print("my_module.py is being run directly.")
    main_logic()
else:
    # This block executes if the module is being imported.
    print("my_module.py is being imported into another module.")
```

**Scenario 1: Running `my_module.py` directly**
```bash
$ python my_module.py
```
Output:
```
In my_module.py, __name__ is set to: __main__
my_module.py is being run directly.
Main logic of my_module is executing.
Helper function from my_module is called.
```
Here, `__name__` inside `my_module.py` is `__main__`, so the code inside the `if` block executes.

**Scenario 2: Importing `my_module.py` into another script**
Let's say we have `another_script.py`:
```python
# another_script.py
import my_module # This will execute the top-level code in my_module.py

print("\nIn another_script.py, now using my_module:")
my_module.helper_function()
# my_module.main_logic() # We can still call it if we want
```
Output when running `python another_script.py`:
```
In my_module.py, __name__ is set to: my_module  <-- Note this!
my_module.py is being imported into another module.

In another_script.py, now using my_module:
Helper function from my_module is called.
```
Here, when `my_module` is imported, `__name__` inside `my_module.py` is `'my_module'`, so the `else` block executes, and the code inside `if __name__ == "__main__":` in `my_module.py` does *not* execute automatically upon import.

## Purpose and Advantages of `if __name__ == "__main__":`
1.  **Reusability:** Allows a Python file to serve a dual purpose:
    -   It can be **imported as a module** by other scripts, providing its functions and classes for reuse without automatically running example code or a main script logic.
    -   It can also be **executed as a standalone script**, typically to run tests, demonstrations, or a main application flow defined within the `if` block.
2.  **Preventing Unintended Execution:** Code that is intended only for when the file is the main program (like test calls, example usage, or application startup logic) is placed inside this block. This prevents it from running automatically every time the module is imported elsewhere.
3.  **Clarity and Convention:** It's a standard Python idiom that clearly signals the entry point for script execution.

>[!question] Can we execute a module as a script?
>Yes, any Python file (`.py`) can be executed as a script by passing its name to the Python interpreter (e.g., `python my_module.py`). When executed this way, its `__name__` variable is set to `__main__`. The `if __name__ == "__main__":` block allows you to define specific behavior for when the module is run as the main script.

The `__name__` variable and the `if __name__ == "__main__":` construct are fundamental for creating reusable Python modules that can also be run independently for testing or as top-level programs.

---
`````

This covers `global`, `__name__`, modules/packages, and the import system. Next, I'll create notes for the `os` and `sys` modules and address the remaining questions for WS19.

