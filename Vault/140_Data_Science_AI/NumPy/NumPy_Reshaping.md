---
tags:
  - numpy
  - python
  - array_manipulation
  - concept
aliases:
  - Reshaping NumPy Arrays
  - np.reshape
  - ndarray.reshape
related:
  - "[[NumPy_ndarray]]"
  - "[[NumPy_Dimension_Shape_Axis]]"
  - "[[NumPy_Views_vs_Copies]]"
worksheet: [WS_NumPy]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# NumPy Reshaping

## Definition

**Reshaping** in NumPy refers to changing the [[NumPy_Dimension_Shape_Axis|shape]] (number of elements along each axis/dimension) of an `ndarray` **without changing its data**. The total number of elements in the reshaped array must remain the same as the original array.

## Key Methods for Reshaping

1.  **`ndarray.reshape(new_shape)` method:**
    -   Called on an existing `ndarray` object.
    -   Returns a **new `ndarray` object** (often a [[NumPy_Views_vs_Copies|view]] if possible, otherwise a copy) with the specified `new_shape`. The original array's shape is unchanged.
    -   The `new_shape` is a tuple of integers.
    -   One dimension in `new_shape` can be `-1`. In this case, the value for that dimension is inferred from the length of the array and the remaining dimensions.

2.  **`numpy.reshape(array, new_shape)` function:**
    -   A function from the NumPy module that takes the array to be reshaped as its first argument.
    -   Similar behavior to the method version.

3.  **`ndarray.shape = new_shape` (In-place assignment):**
    -   Modifies the shape of the array **in-place**, if possible.
    -   This is only possible if the array's data is contiguous in memory and the new shape is compatible with the total number of elements.
    -   If not possible (e.g., data is not contiguous due to certain slicing operations, or total elements don't match), it will raise an error.
    -   Generally, using the `reshape()` method/function is safer and preferred as it returns a new view or copy, and handles potential memory layout issues more gracefully.

4.  **`ndarray.resize(new_shape)` method:**
    -   **Modifies the array in-place.**
    -   Unlike `reshape` or `shape` assignment, `resize` **can change the total number of elements**.
    -   If the new size is larger, new elements are added (uninitialized or filled with zeros if `refcheck=False` is used cautiously).
    -   If the new size is smaller, elements are discarded.
    -   Use with caution, especially if other variables reference the same array data, as it can lead to unexpected behavior.

## Visualization with AnyBlock Cards

[list2card|addClass(ab-col3)]
- `Original Array`
	```python
	import numpy as np
	original = np.arange(12) # [ 0  1  2  3  4  5  6  7  8  9 10 11]
	# original.shape is (12,)
	```
	Original Data (Conceptual Memory):
	`[0|1|2|3|4|5|6|7|8|9|10|11]`
- `arr.reshape((3, 4))`
	```python
	reshaped_3x4 = original.reshape((3, 4))
	# Output:
	# [[ 0  1  2  3]
	#  [ 4  5  6  7]
	#  [ 8  9 10 11]]
	# reshaped_3x4.shape is (3, 4)
	# original.shape is still (12,)
	```
	This usually returns a *view* if data is C-contiguous.
- `arr.reshape((2, -1))` (Infer Dimension)
	```python
	reshaped_2x_auto = original.reshape((2, -1)) # -1 infers 6 columns
	# Output:
	# [[ 0  1  2  3  4  5]
	#  [ 6  7  8  9 10 11]]
	# reshaped_2x_auto.shape is (2, 6)
	```
- `arr.shape = (4, 3)` (In-place)
	```python
	# Be careful, modifies 'original' if possible
	# original_copy = original.copy()
	# original_copy.shape = (4, 3)
	# Output (for original_copy):
	# [[ 0  1  2]
	#  [ 3  4  5]
	#  [ 6  7  8]
	#  [ 9 10 11]]
	# original_copy.shape is now (4, 3)
	```
	This modifies the array directly.
- `arr.resize((2, 5))` (In-place, changes size)
	```python
	# Modifies 'original' AND changes its total size
	original_resized = np.arange(12) # Start fresh
	original_resized.resize((2, 5)) # Total elements becomes 10
	# Output (original_resized):
	# [[0 1 2 3 4]
	#  [5 6 7 8 9]]
	# original_resized.shape is (2, 5)
	# original_resized.size is 10
	```
	If new size > old size, new values are often zeros (depending on `refcheck`). If new size < old, data is lost.

## Related Concepts
- [[NumPy_ndarray]], [[NumPy_Dimension_Shape_Axis]]
- [[NumPy_Views_vs_Copies]] (Important to understand if reshape returns a view or copy)
- `ravel()`, `flatten()` (Methods to convert multi-dimensional arrays to 1D)
- `transpose()`, `.T` (Permutes axes, which is different from reshaping)

## Questions / Further Study
>[!question] Why would you need to reshape an `ndarray`? (WS_NumPy)
> 1.  **Algorithm Requirements:** Many machine learning algorithms or mathematical operations expect input data in a specific shape (e.g., a 2D matrix for linear algebra, a specific tensor shape for neural network layers).
> 2.  **Data Interpretation:** Reshaping can help interpret 1D data as a multi-dimensional structure (e.g., loading a flat list of pixel values and reshaping it into a 2D image matrix).
> 3.  **Broadcasting:** To make arrays compatible for [[NumPy_Broadcasting|broadcasting]] operations.
> 4.  **Feature Engineering:** Transforming features into a shape suitable for a model.

>[!question] Why use `reshape`; can't you simply assign a new shape? (WS_NumPy)
> - **`reshape()` method/function:** Is generally **safer** and more flexible. It returns a new array (often a view if possible, or a copy if necessary to maintain contiguity for the new shape). The original array remains unchanged. It also allows the `-1` inferring for one dimension.
> - **`ndarray.shape = new_shape` assignment:** Modifies the array **in-place**. This is only allowed if the new shape is compatible with the total number of elements AND the array's data is stored contiguously in memory in a way that supports the new shape. If the data isn't C-contiguous (e.g., after certain transpose or slicing operations), direct shape assignment might fail with an error. `reshape()` can often handle non-contiguous data by making a copy.
>
> **Conclusion:** `reshape()` is generally preferred for its safety, ability to return views efficiently, and flexibility with dimension inference. Direct shape assignment is more restrictive.

---
**Source:** Worksheet WS_NumPy, NumPy Documentation