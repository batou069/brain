---
tags:
  - numpy
  - python
  - array_creation
  - concept
  - memory
aliases:
  - np.empty
  - Empty NumPy Array
related:
  - "[[NumPy_ndarray]]"
  - "[[NumPy_Data_Types]]"
  - "[[np.zeros]]"
  - "[[np.ones]]"
  - "[[Memory_Initialization]]" # Placeholder
worksheet: [WS_NumPy]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# NumPy Empty Array (`np.empty`)

## Definition

In NumPy, an **empty array** created using `numpy.empty(shape, dtype=float, order='C')` is an array whose initial content is **random and uninitialized**. Unlike `np.zeros()` or `np.ones()`, `np.empty()` does **not** set the array values to any particular value (like zero or one). It simply allocates a block of memory of the specified shape and data type, and the values in that memory block are whatever happened to be there before allocation (garbage values).

## Purpose

- **Performance (Marginal):** The main reason to use `np.empty()` is for a slight performance gain when creating very large arrays if you intend to fill all elements immediately afterwards. By skipping the initialization step (to zeros or ones), `np.empty()` can be marginally faster for allocation.
- **When Overwriting:** If you are sure that every element of the array will be explicitly assigned a value before being read, then the initial garbage values don't matter, and `np.empty()` avoids the unnecessary work of initializing.

## Syntax

```python
import numpy as np

# Create an empty array of shape (2, 3) with default dtype (float64)
empty_arr = np.empty((2, 3))

# Create an empty array with a specific dtype
empty_int_arr = np.empty((3, 4), dtype=np.int32)
```

## Key Characteristics

- **Uninitialized Values:** Contains arbitrary "garbage" data from the allocated memory locations. **Do not assume it contains zeros or any predictable pattern.**
- **Shape and Dtype:** The shape and data type are defined correctly as specified.
- **Use with Caution:** Should only be used if you are certain that you will populate every element of the array before reading from it. Using uninitialized values can lead to unpredictable behavior and bugs.

## Example

```python
import numpy as np

# Create an empty array
# Its contents are unpredictable!
arr = np.empty((2, 3))
print("Uninitialized 'empty' array:")
print(arr)

# Example of filling it immediately
arr_filled = np.empty((2, 2), dtype=int)
for i in range(2):
    for j in range(2):
        arr_filled[i, j] = i + j
print("\n'empty' array after filling:")
print(arr_filled)

# Contrast with np.zeros
arr_zeros = np.zeros((2,3))
print("\n'zeros' array:")
print(arr_zeros)
```
**Example Output (for `print(arr)` the values will vary each run):**
```
Uninitialized 'empty' array:
[[6.95320418e-310  6.95320418e-310  6.95320418e-310]
 [6.95320418e-310  6.95320418e-310  0.00000000e+000]]  # Example garbage

'empty' array after filling:
[[0 1]
 [1 2]]

'zeros' array:
[[0. 0. 0.]
 [0. 0. 0.]]
```

## Related Concepts
- [[NumPy_ndarray]], [[NumPy_Data_Types]]
- [[np.zeros]] (Creates an array initialized with zeros)
- [[np.ones]] (Creates an array initialized with ones)
- [[Memory_Initialization]]
- [[Performance]] (Minor benefit in specific cases)

>[!warning] Uninitialized Data
> Never rely on the initial content of an array created with `np.empty()`. Always ensure all elements are assigned values before they are read or used in computations.

---
**Source:** Worksheet WS_NumPy, NumPy Documentation