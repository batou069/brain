---
tags:
  - numpy
  - python
  - array_manipulation
  - concept
  - memory
  - core
aliases:
  - NumPy View
  - NumPy Copy
  - ndarray View vs Copy
related:
  - "[[NumPy_ndarray]]"
  - "[[NumPy_Indexing_Slicing]]"
  - "[[NumPy_Reshaping]]"
  - "[[Memory_Management]]"
  - "[[Shallow_Copy_vs_Deep_Copy]]" # General concept
worksheet: [WS_NumPy]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# NumPy: Views vs. Copies

## Definition

When manipulating NumPy `ndarray`s (e.g., through slicing, reshaping, or certain functions), it's crucial to understand whether the operation returns a **view** of the original array or a **copy**.

1.  **View (Shallow Copy):**
    -   A **view** is a new `ndarray` object that looks at the **same underlying data buffer** as the original array.
    -   Changes made to the data through the view **will affect** the original array.
    -   Changes made to the data through the original array **will affect** the view.
    -   Views are memory-efficient as they don't duplicate data.
    -   The view can have a different shape, strides, and `dtype` (if reinterpreted) than the original, but it shares the same data.
    -   Created by operations like basic slicing, `reshape()` (often), `transpose()`/`.T`, `swapaxes()`, or methods like `ndarray.view()`.

2.  **Copy (Deep Copy):**
    -   A **copy** is a completely new `ndarray` object with its **own separate data buffer**, containing a duplicate of the original array's data.
    -   Changes made to the copy **will not affect** the original array.
    -   Changes made to the original array **will not affect** the copy.
    -   Created by operations like explicit `ndarray.copy()` method, fancy indexing, boolean indexing (when selecting elements into a new array), or when an operation cannot produce a view due to memory layout constraints (e.g., some `reshape()` cases).

## Determining if an Array is a View or Owns its Data

- **`ndarray.base` attribute:**
    - If `arr.base` is `None`, then `arr` owns its own data (it's not a view of another array).
    - If `arr.base` is another `ndarray` object, then `arr` is a view of that base array.
- **`ndarray.flags.owndata` attribute:**
    - `arr.flags.owndata` is `True` if the array owns its data.
    - `arr.flags.owndata` is `False` if it is a view or borrows data from another object.

## AnyBlock Tabs: View vs. Copy Examples

[list2tab]
- Basic Slicing (View)
	```python
	import numpy as np
	original = np.arange(10)
	print(f"Original: {original}")

	# Slicing creates a view
	view_slice = original[2:5]
	print(f"View Slice: {view_slice}")
	print(f"Does view_slice own its data? {view_slice.flags.owndata}") # False
	print(f"Base of view_slice is original? {view_slice.base is original}") # True

	# Modify the view
	view_slice[0] = 99
	print(f"View Slice after modification: {view_slice}")
	print(f"Original after modifying view: {original}") # Original is changed!
	```
- Reshape (Often a View)
	```python
	import numpy as np
	original = np.arange(6)
	reshaped_view = original.reshape((2, 3))
	print(f"Original: {original}")
	print(f"Reshaped View:\n{reshaped_view}")
	print(f"Does reshaped_view own data? {reshaped_view.flags.owndata}") # False

	reshaped_view[0, 0] = 100
	print(f"Original after modifying reshaped_view: {original}") # Original changed
	```
- Explicit Copy (`.copy()`)
	```python
	import numpy as np
	original = np.arange(5)
	print(f"Original: {original}")

	# Explicit copy
	copied_arr = original.copy()
	print(f"Copied Array: {copied_arr}")
	print(f"Does copied_arr own its data? {copied_arr.flags.owndata}") # True
	print(f"Base of copied_arr: {copied_arr.base}") # None

	# Modify the copy
	copied_arr[0] = 77
	print(f"Copied Array after modification: {copied_arr}")
	print(f"Original after modifying copy: {original}") # Original is UNCHANGED
	```
- Fancy Indexing / Boolean Indexing (Copy)
	```python
	import numpy as np
	original = np.array()

	# Fancy indexing creates a copy
	fancy_indexed = original[]
	print(f"Fancy Indexed: {fancy_indexed}")
	print(f"Does fancy_indexed own data? {fancy_indexed.flags.owndata}") # True
	fancy_indexed[0] = 111
	print(f"Original after fancy mod: {original}") # Unchanged

	# Boolean indexing creates a copy when selecting elements
	bool_indexed = original[original > 2]
	print(f"Boolean Indexed: {bool_indexed}")
	print(f"Does bool_indexed own data? {bool_indexed.flags.owndata}") # True
	if bool_indexed.size > 0:
	    bool_indexed[0] = 222
	print(f"Original after bool mod: {original}") # Unchanged
	```

## Importance

- **Memory Efficiency:** Views avoid unnecessary data duplication, saving memory, especially for large arrays.
- **Performance:** Operations on views can be faster as no data copying is involved.
- **Unintended Side Effects:** Crucial to understand if modifications to a derived array will affect the original. If a view is modified unintentionally, it can lead to subtle bugs. If independent modification is needed, an explicit `.copy()` should be made.

## Related Concepts
- [[NumPy_ndarray]]
- [[NumPy_Indexing_Slicing]], [[NumPy_Reshaping]], Transposing (Operations that may return views)
- [[Memory_Management]]
- [[Shallow_Copy_vs_Deep_Copy]] (General programming concept)
- `ndarray.base`, `ndarray.flags.owndata` (Attributes for checking)

## Questions / Further Study
>[!question] What is a view of an `np.array`? (WS_NumPy)
> A view of a NumPy array is a new `ndarray` object that shares the **same underlying data buffer** as the original array. It provides a different "view" or perspective on that data (e.g., different shape, strides, or a subset of elements via slicing). Changes made to the data through the view will affect the original array, and vice-versa. Views are memory-efficient because they don't duplicate the data. Operations like basic slicing or `reshape()` often return views. You can check if an array `v` is a view of another array `b` by checking if `v.base is b` or if `v.flags.owndata` is `False`.

---
**Source:** Worksheet WS_NumPy, NumPy Documentation