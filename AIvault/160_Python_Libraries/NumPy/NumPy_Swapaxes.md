---
tags:
  - numpy
  - python
  - array_manipulation
  - concept
  - axes
aliases:
  - np.swapaxes
related:
  - "[[NumPy_ndarray]]"
  - "[[NumPy_Dimension_Shape_Axis]]"
  - "[[NumPy_Transpose]]"
  - "[[NumPy_Views_vs_Copies]]"
worksheet: [WS_NumPy]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# NumPy `swapaxes()`

## Definition

The `numpy.swapaxes(array, axis1, axis2)` function in [[NumPy]] interchanges (swaps) two specified **axes** of an `ndarray`. It returns a **[[NumPy_Views_vs_Copies|view]]** of the input array with the specified axes swapped; the underlying data is not copied.

## Syntax

```python
numpy.swapaxes(array, axis1, axis2)
```

- **`array`**: The input `ndarray`.
- **`axis1`**: First axis to be swapped.
- **`axis2`**: Second axis to be swapped.

## Key Aspects

- **Swaps Two Axes:** Specifically interchanges the positions and lengths of `axis1` and `axis2` in the array's shape. Other axes remain in their original relative order.
- **Returns a View:** Modifying the returned array will modify the original array's data, as they share the same data buffer.
- **Difference from Transpose:**
    - `ndarray.T` (or `np.transpose(array)`) without an `axes` argument reverses *all* axes.
    - `np.transpose(array, axes=tuple_of_axes)` provides a general permutation of axes.
    - `np.swapaxes` is a specialized permutation that only swaps two given axes.

## Example

```python
import numpy as np

# Create a 3D array
arr = np.arange(24).reshape((2, 3, 4))
# Shape: (2 layers, 3 rows, 4 columns)
# arr =
# [[[ 0  1  2  3]
#   [ 4  5  6  7]
#   [ 8  9 10 11]]
#
#  [[12 13 14 15]
#   [16 17 18 19]
#   [20 21 22 23]]]

print(f"Original array shape: {arr.shape}")

# Swap axis 0 (layers) and axis 1 (rows)
arr_swapped_01 = np.swapaxes(arr, 0, 1)
print(f"\nShape after swapping axes 0 and 1: {arr_swapped_01.shape}") # (3, 2, 4)
# Now has 3 layers, each being a 2x4 matrix
# arr_swapped_01[0,0,0] would be original arr[0,0,0] = 0
# arr_swapped_01[1,0,0] would be original arr[0,1,0] = 4 (Original row 1 became new layer 1)

# Swap axis 0 (layers) and axis 2 (columns)
arr_swapped_02 = np.swapaxes(arr, 0, 2)
print(f"\nShape after swapping axes 0 and 2: {arr_swapped_02.shape}") # (4, 3, 2)
# Now has 4 layers, each being a 3x2 matrix
# arr_swapped_02[0,0,0] would be original arr[0,0,0] = 0
# arr_swapped_02[1,0,0] would be original arr[0,0,1] = 1 (Original column 1 became new layer 1)

# Swap axis 1 (rows) and axis 2 (columns) - like transposing each 2D matrix layer
arr_swapped_12 = np.swapaxes(arr, 1, 2)
print(f"\nShape after swapping axes 1 and 2: {arr_swapped_12.shape}") # (2, 4, 3)
# Still 2 layers, but each is now a 4x3 matrix
# arr_swapped_12[0,0,0] would be original arr[0,0,0] = 0
# arr_swapped_12[0,0,1] would be original arr[0,1,0] = 4

print("\nOriginal array element arr[0,1,2]:", arr[0,1,2]) # Output: 6
print("arr_swapped_01[1,0,2]:", arr_swapped_01[1,0,2]) # Output: 6 (0->1, 1->0, 2->2)
print("arr_swapped_02[2,1,0]:", arr_swapped_02[2,1,0]) # Output: 6 (0->2, 1->1, 2->0)
print("arr_swapped_12[0,2,1]:", arr_swapped_12[0,2,1]) # Output: 6 (0->0, 1->2, 2->1)

# Check if it's a view
print(f"\narr_swapped_01 is a view: {arr_swapped_01.base is arr}") # True
arr_swapped_01[0,0,0] = 99
print(f"Original arr[0,0,0] after modifying view: {arr[0,0,0]}") # Output: 99
```

## Related Concepts
- [[NumPy_ndarray]], [[NumPy_Dimension_Shape_Axis]]
- [[NumPy_Transpose]] (`.T`, `np.transpose()`) (More general axis permutation or full reversal)
- [[NumPy_Views_vs_Copies]] (Returns a view)
- Array Strides (Internal mechanism that allows views for such operations)

## Questions / Further Study
>[!question] How are `swapaxes` and `transpose` different? (WS_NumPy)
> - **`np.swapaxes(arr, axis1, axis2)`:** Interchanges exactly **two** specified axes. Other axes remain in their original relative positions.
> - **`arr.T` or `np.transpose(arr)` (without `axes` argument):** Reverses the order of **all** axes. For a 3D array `(d0, d1, d2)`, `.T` gives shape `(d2, d1, d0)`.
> - **`np.transpose(arr, axes=(p0, p1, ..., pk))`:** Provides a **general permutation** of all axes according to the `axes` tuple. `swapaxes` is a special case of this general permutation.
>
> **Example (3D array with shape (2,3,4)):**
> - `arr.T` or `np.transpose(arr)` -> shape `(4,3,2)`
> - `np.swapaxes(arr, 0, 1)` -> shape `(3,2,4)` (axes 0 and 1 swapped, axis 2 unchanged relative to new axis 0,1)
> - `np.swapaxes(arr, 0, 2)` -> shape `(4,3,2)` (same as `.T` in this specific 3D case because it's a full reversal if you swap first and last)
> - `np.transpose(arr, axes=(1,2,0))` -> shape `(3,4,2)` (axis 0 becomes axis 2, axis 1 becomes axis 0, axis 2 becomes axis 1)

---
**Source:** Worksheet WS_NumPy, NumPy Documentation