---
tags:
  - numpy
  - python
  - array_manipulation
  - linear_algebra
  - concept
aliases:
  - NumPy Transpose
  - np.transpose
  - ndarray.T
related:
  - "[[NumPy_ndarray]]"
  - "[[NumPy_Dimension_Shape_Axis]]"
  - "[[Matrix_Math]]" # Matrix Transpose
  - "[[NumPy_Swapaxes]]"
  - "[[NumPy_Views_vs_Copies]]"
worksheet: [WS_NumPy]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# NumPy Transpose (`.T`, `np.transpose()`)

## Definition

In NumPy, **transposing** an `ndarray` means permuting (rearranging) its axes. For a 2D array (matrix), this is the standard matrix transpose operation where rows become columns and columns become rows. For N-dimensional arrays, the `transpose()` function allows specifying the new order of axes. The `.T` attribute is a shortcut for `transpose()` with reversed axes order.

## Methods

1.  **`ndarray.T` attribute:**
    -   A convenient attribute of an `ndarray` object.
    -   For a 2D array, `arr.T` is its matrix transpose.
    -   For a 1D array, `arr.T` returns the original array unchanged (as the transpose of a vector is conceptually itself in 1D context, or a row/column vector if promoted to 2D).
    -   For N-D arrays (N > 2), `arr.T` reverses the order of axes (equivalent to `arr.transpose(N-1, N-2, ..., 1, 0)`).
    -   Often returns a **[[NumPy_Views_vs_Copies|view]]** of the original array (data is not copied).

2.  **`numpy.transpose(array, axes=None)` function:**
    -   More general function for permuting axes.
    -   `array`: The input `ndarray`.
    -   `axes` (optional): A tuple or list of integers specifying the new order of axes. If `None` (default), it reverses the order of axes (like `.T`).
    -   Example: If `arr` has shape `(2,3,4)`, `np.transpose(arr, axes=(1,2,0))` will result in an array with shape `(3,4,2)`.
    -   Also often returns a view.

## Visualization (2D Transpose)

[list2tab]
- Original Array
	```python
	import numpy as np
	A = np.array([
	    ,
	    
	])
	# A:
	# [[1 2 3]
	#  [4 5 6]]
	# A.shape is (2, 3)
	```
	```d2
	A_original: {
	  shape: "2x3 Matrix"
	  row0: "1 | 2 | 3"
	  row1: "4 | 5 | 6"
	}
	```
- "A.T (Transpose)"
	```python
	AT = A.T
	# AT:
	# [[1 4]
	#  [2 5]
	#  [3 6]]
	# AT.shape is (3, 2)
	```
	```d2
	AT_transposed: {
	  shape: "3x2 Matrix"
	  row0: "1 | 4"
	  row1: "2 | 5"
	  row2: "3 | 6"
	}
	```
```

## Related Concepts
- [[NumPy_ndarray]], [[NumPy_Dimension_Shape_Axis]]
- [[Matrix_Math]] (Matrix transpose is a core linear algebra operation)
- [[NumPy_Swapaxes]] (Swaps only two specified axes)
- [[NumPy_Views_vs_Copies]] (Transpose often returns a view)
- Permutation of Axes

## Questions / Further Study
>[!question] Why is `.T` an attribute and not a method? (WS_NumPy)
> In NumPy, `arr.T` is implemented as a **property** (an attribute that has getter/setter logic behind it). It behaves like an attribute syntactically (no parentheses `()`).
> - **Convenience:** It provides a very concise and common mathematical notation for transpose.
> - **View (Usually):** For simple transposition (like reversing axes for N-D arrays or standard 2D matrix transpose), NumPy can often return a [[NumPy_Views_vs_Copies|view]] of the original data without copying it. This is achieved by changing the array's strides (how many bytes to step in memory to get to the next element along each axis) rather than moving data. An attribute access is a natural fit for an operation that primarily changes metadata and returns a view.
> - **No Arguments Needed for Default:** The most common transpose (reversing all axes, or 2D transpose) requires no arguments, fitting the attribute access style. The more general `np.transpose()` *function* takes arguments for custom axis permutations.
>
> While it could have been a method `arr.transpose()`, using `.T` aligns well with mathematical notation and the efficient view-based implementation for the common case.

>[!question] How are `swapaxes` and `transpose` different? (WS_NumPy)
> - **`ndarray.T` / `np.transpose(arr)` (no `axes` argument):** Reverses the order of *all* axes. For a 2D array, this is the standard matrix transpose. For a 3D array with shape `(a,b,c)`, `arr.T` has shape `(c,b,a)`.
> - **`np.transpose(arr, axes=(p0, p1, ..., pk))`:** Permutes the axes according to the specified tuple `axes`. For example, if `arr` has shape `(a,b,c)` and `axes=(1,2,0)`, the new shape will be `(b,c,a)`.
> - **[[NumPy_Swapaxes|`np.swapaxes(arr, axis1, axis2)`]]:** Specifically interchanges (swaps) *only two* specified axes. Other axes remain in their original relative order. For example, if `arr` has shape `(a,b,c)`, `np.swapaxes(arr, 0, 2)` results in shape `(c,b,a)` (same as `.T` in this 3D case). However, `np.swapaxes(arr, 0, 1)` would result in shape `(b,a,c)`.
>
> **Summary:**
> - `.T` is a shortcut for reversing all axes.
> - `np.transpose()` is a general permutation of axes.
> - `np.swapaxes()` is a specialized permutation that swaps exactly two axes.
> All these operations usually return views.

---
**Source:** Worksheet WS_NumPy, NumPy Documentation