---
tags:
  - python
  - built_in_functions
  - core_python
  - utility
  - concept
  - summary
aliases:
  - Python Built-in Functions
  - Standard Python Functions
related:
  - "[[100_Python/_Python_Programming_MOC|_Python_Programming_MOC]]"
  - "[[Built_In_Functions_Python#id()|id()]]"
  - "[[Python_Data_Structures_Identity_vs_Equality|is operator]]"
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
worksheet:
  - WS17
  - WS18
  - WS19
  - WS20
  - WS21
date_created: 2025-08-20
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