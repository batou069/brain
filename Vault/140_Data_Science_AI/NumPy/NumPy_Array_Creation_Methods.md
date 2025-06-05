---
tags:
  - numpy
  - python
  - array_creation
  - function
  - concept
aliases:
  - Creating NumPy Arrays
  - NumPy Array Initialization
related:
  - "[[NumPy_ndarray]]"
  - "[[NumPy_Data_Types]]"
  - "[[np.array]]"
  - "[[np.zeros]]"
  - "[[np.ones]]"
  - "[[np.empty]]"
  - "[[np.arange]]"
  - "[[np.linspace]]"
  - "[[np.logspace]]"
  - "[[np.full]]"
  - "[[np.eye]]"
  - "[[np.random]]"
worksheet: [WS_NumPy]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# NumPy Array Creation Methods

## Definition

[[NumPy]] provides a wide variety of functions to create `ndarray` objects. Choosing the right creation method depends on the desired initial content, shape, and data type of the array.

## Common Creation Methods (WS_NumPy Question: List 10)

Here are more than 10 common ways, categorized:

[list2tab]
- From Existing Data
	1.  **`np.array(object, dtype=None, ...)`:**
		-   Converts input `object` (like a Python list, tuple, list of lists) into an `ndarray`.
		-   `dtype` can be specified; otherwise, NumPy infers it.
		```python
		import numpy as np
		list_data = [
		arr_from_list = np.array(list_data)
		```
	2.  **`np.asarray(a, dtype=None, ...)`:**
		-   Converts input `a` to an array.
		-   **Crucially, if `a` is already an `ndarray` with a matching `dtype`, no copy is performed (a view or the original is returned).**
		```python
		arr1 = np.arange(5)
		arr2 = np.asarray(arr1) # arr2 is arr1 (no copy)
		arr3 = np.asarray(arr1, dtype=float) # arr3 is a copy (dtype changed)
		```
- Arrays with Constant Values
	3.  **`np.zeros(shape, dtype=float, ...)`:**
		-   Creates an array of the given `shape` filled with **zeros**.
		```python
		zeros_arr = np.zeros((2, 3)) # 2x3 array of 0.0
		```
	4.  **`np.ones(shape, dtype=float, ...)`:**
		-   Creates an array of the given `shape` filled with **ones**.
		```python
		ones_arr = np.ones((3, 2), dtype=int) # 3x2 array of 1s
		```
	5.  **`np.full(shape, fill_value, dtype=None, ...)`:**
		-   Creates an array of the given `shape` filled with a specified `fill_value`.
		```python
		full_arr = np.full((2, 2), 99) # 2x2 array filled with 99
		```
	6.  **`np.empty(shape, dtype=float, ...)`:**
		-   Creates an **uninitialized** array of the given `shape`. Faster, but contains garbage values. Use only if you will fill it immediately. See [[NumPy_Empty_Array]].
		```python
		empty_arr = np.empty((2, 2))
		```
	7.  **`np.eye(N, M=None, k=0, dtype=float, ...)`:**
		-   Creates a 2D array with **ones on a diagonal** and zeros elsewhere.
		-   `N`: Number of rows.
		-   `M`: Number of columns (defaults to `N`).
		-   `k`: Index of the diagonal (0 is main, positive for upper, negative for lower).
		```python
		identity_3x3 = np.eye(3)
		diag_offset = np.eye(3, k=1)
		```
	8.  **`np.identity(n, dtype=float, ...)`:**
		-   Creates a square [[Identity_Matrix|identity matrix]] of size `n x n`. Equivalent to `np.eye(n)`.
		```python
		id_mat = np.identity(3)
		```
- Arrays with Sequences
	9.  **`np.arange([start,] stop[, step,], dtype=None, ...)`:**
		-   Similar to Python's `range()`, but returns an `ndarray`.
		-   Creates an array with evenly spaced values within a given interval.
		```python
		range_arr = np.arange(0, 10, 2) # [0 2 4 6 8]
		```
	10. **`np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, ...)`:**
		-   Creates an array with `num` evenly spaced samples, calculated over the interval [`start`, `stop`].
		-   `endpoint`: If `True`, `stop` is the last sample. If `False`, it is not included.
		```python
		linspace_arr = np.linspace(0, 1, 5) # [0.   0.25 0.5  0.75 1.  ]
		```
	11. **`np.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None, ...)`:**
		-   Creates an array with `num` samples, evenly spaced on a log scale.
		-   Values are `base ** start` to `base ** stop`.
		```python
		logspace_arr = np.logspace(0, 2, 3) # [  1.  10. 100.] (10^0, 10^1, 10^2)
		```
- Arrays from Random Sampling
	12. **`np.random.rand(d0, d1, ..., dn)`:**
		-   Creates an array of the given shape with random samples from a **uniform distribution** over `[0, 1)`.
		```python
		rand_arr = np.random.rand(2, 3)
		```
	13. **`np.random.randn(d0, d1, ..., dn)`:**
		-   Creates an array of the given shape with random samples from a **standard normal distribution** (mean 0, variance 1).
		```python
		randn_arr = np.random.randn(2, 3)
		```
	14. **`np.random.randint(low, high=None, size=None, dtype=int)`:**
		-   Creates an array of the given `size` with random integers from `low` (inclusive) to `high` (exclusive).
		```python
		randint_arr = np.random.randint(0, 10, size=(2, 4))
		```
- From Other Array-like Objects
	15. **`np.copy(a, order='K')`:**
		-   Returns an array copy of the given object. Explicitly makes a [[NumPy_Views_vs_Copies|copy]].
		```python
		arr = np.array()
		arr_copy = np.copy(arr)
		```
	16. **`np.fromfunction(function, shape, **kwargs)`:**
		-   Construct an array by executing a function over each coordinate.
		```python
		def my_func(i, j): return i + j
		from_func_arr = np.fromfunction(my_func, (3, 3), dtype=int)
		# [[0 1 2]
		#  [1 2 3]
		#  [2 3 4]]
		```
	17. **`np.diag(v, k=0)`:**
		-   If `v` is 1D, constructs a 2D array with `v` on the k-th diagonal.
		-   If `v` is 2D, extracts the k-th diagonal.
		```python
		diag_from_1d = np.diag()
		```

## Related Concepts
- [[NumPy_ndarray]], [[NumPy_Data_Types]]
- [[NumPy_Dimension_Shape_Axis]]
- [[NumPy_Views_vs_Copies]] (`np.asarray` vs `np.array` vs `np.copy`)
- [[np.random]] (Module for random number generation)

---
**Source:** Worksheet WS_NumPy, NumPy Documentation