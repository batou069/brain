---
tags:
  - numpy
  - python
  - data_structure
  - core
aliases:
  - ndarray
  - N-dimensional array (NumPy)
related:
  - "[[NumPy]]"
  - "[[NumPy_Data_Types]]"
  - "[[NumPy_Dimension_Shape_Axis]]"
  - "[[NumPy_Indexing_Slicing]]"
  - "[[NumPy_Array_vs_List]]"
  - "[[Memory_Management]]" # NumPy arrays are contiguous
worksheet: [WS_NumPy]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# NumPy `ndarray` (N-dimensional Array)

## Definition

The **`ndarray`** (N-dimensional array) is the fundamental data structure provided by the [[NumPy]] library. It is a **grid of values, all of the same type ([[NumPy_Data_Types|dtype]])**, indexed by a tuple of non-negative integers. The number of dimensions is the **rank** of the array; the **shape** of an array is a tuple of integers giving the size of the array along each dimension.

## Key Attributes

- **`ndarray.ndim`:** The number of axes (dimensions) of the array (its rank).
- **`ndarray.shape`:** A tuple of integers indicating the size of the array in each dimension. For a matrix with `n` rows and `m` columns, `shape` will be `(n, m)`.
- **`ndarray.size`:** The total number of elements in the array. Equal to the product of the elements of `shape`.
- **`ndarray.dtype`:** An object describing the data type of the elements in the array (e.g., `numpy.int32`, `numpy.float64`). All elements in an `ndarray` must have the same `dtype`.
- **`ndarray.itemsize`:** The size in bytes of each element of the array.
- **`ndarray.data`:** The buffer containing the actual elements of the array. Usually, we don't need to use this attribute directly, as we access the elements through indexing.
- **`ndarray.flags`:** Information about the memory layout of the array (e.g., C-contiguous, F-contiguous, writeable).

## Characteristics

- **Homogeneous:** All elements must be of the same data type. This allows for efficient storage and computation.
- **Fixed Size at Creation:** Once an `ndarray` is created, its size (number of elements) cannot be changed directly. Operations that appear to change the size (like `np.append`) actually create a new array and deallocate the old one.
- **Contiguous Memory (Usually):** NumPy arrays are typically stored in a contiguous block of memory. This is crucial for performance, allowing efficient access and operations by optimized C/Fortran code.
- **Efficient Operations:** Supports [[NumPy_Vectorization|vectorized]] arithmetic and other operations, which are much faster than element-by-element loops in Python.
- **Multi-dimensional:** Can represent vectors (1D), matrices (2D), and higher-dimensional tensors.

## Creating `ndarray`s

```python
import numpy as np

# From Python list
arr1d = np.array()
arr2d = np.array([,])

# Using creation functions
zeros_arr = np.zeros((2, 3))       # Array of zeros
ones_arr = np.ones((3, 2), dtype=np.int16) # Array of ones, specified dtype
arange_arr = np.arange(0, 10, 2)   # Like Python's range
linspace_arr = np.linspace(0, 1, 5) # 5 evenly spaced numbers from 0 to 1

print(f"arr2d:\n{arr2d}")
print(f"arr2d.ndim: {arr2d.ndim}")
print(f"arr2d.shape: {arr2d.shape}")
print(f"arr2d.size: {arr2d.size}")
print(f"arr2d.dtype: {arr2d.dtype}")
print(f"ones_arr.dtype: {ones_arr.dtype}")
print(f"ones_arr.itemsize: {ones_arr.itemsize}")
```

## Related Concepts
- [[NumPy]] (The library providing `ndarray`)
- [[NumPy_Data_Types]] (Defines the type of elements)
- [[NumPy_Dimension_Shape_Axis]] (Describes the structure)
- [[NumPy_Indexing_Slicing]], [[NumPy_Boolean_Indexing]] (Accessing elements)
- [[NumPy_Views_vs_Copies]] (Important for understanding memory sharing)
- [[NumPy_Array_vs_List]] (Key differences)

## Questions / Further Study
>[!question] When we talk about dimension, are we referring to matrix dimension or the dimension of the ndarray ? (WS_NumPy)
> In NumPy, when we refer to the **dimension** of an `ndarray` (often given by `ndarray.ndim`), we are talking about the **number of axes** or the **rank** of the array.
> - A 1D array (vector) has `ndim = 1`. Shape: `(n,)`
> - A 2D array (matrix) has `ndim = 2`. Shape: `(rows, cols)`
> - A 3D array (tensor) has `ndim = 3`. Shape: `(depth, rows, cols)`
> This is consistent with the mathematical concept of the dimension of a tensor.
> A **matrix dimension** (like "2x3 matrix") directly corresponds to the `shape` of a 2D `ndarray` (e.g., `(2, 3)` for 2 rows, 3 columns). So, "matrix dimension" refers to the *size along each axis* for a 2D array, while `ndarray.ndim` refers to the *number of axes*.

---
**Source:** Worksheet WS_NumPy, NumPy Documentation