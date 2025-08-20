---
tags:
  - python
  - built_in_function
  - slice
  - sequence
  - slicing
  - indexing
  - concept
  - example
aliases:
  - slice()
  - Python Slice Object
related:
  - "[[Built_In_Functions_Python]]"
  - "[[Python_Slicing]]"
  - "[[Python_List]]"
  - "[[Python_Tuple]]"
  - "[[Python_Primitive_Types|String (str)]]"
worksheet:
  - WS17
date_created: 2025-08-20
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