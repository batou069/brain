---
tags:
  - numpy
  - python
  - data_structure
  - concept
  - core
aliases:
  - NumPy Dimensions
  - NumPy Shape
  - NumPy Axes
  - ndarray Rank
related:
  - "[[NumPy_ndarray]]"
  - "[[NumPy_Reshaping]]"
  - "[[NumPy_Indexing_Slicing]]"
  - "[[Matrix_Math]]" # Matrix dimensions
worksheet: [WS_NumPy]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# NumPy: Dimension, Shape, and Axis

## Definitions

In [[NumPy]], the terms **dimension**, **shape**, and **axis** are fundamental to describing the structure of an `ndarray`.

1.  **Dimension (or Rank / `ndim`):**
    -   Refers to the **number of axes** an array has.
    -   A scalar (single number) can be considered 0-dimensional.
    -   A vector (1D array) has 1 dimension (`ndim=1`).
    -   A matrix (2D array) has 2 dimensions (`ndim=2`).
    -   Higher-dimensional arrays (tensors) have 3 or more dimensions.
    -   Accessed via the `ndarray.ndim` attribute.

2.  **Shape (`shape`):**
    -   A **tuple of integers** indicating the size of the array along each dimension (axis).
    -   The length of the `shape` tuple is equal to `ndarray.ndim`.
    -   Example:
        -   A 1D array (vector) of length 5 has `shape = (5,)`.
        -   A 2D array (matrix) with 3 rows and 4 columns has `shape = (3, 4)`.
        -   A 3D array with 2 layers, 3 rows, and 4 columns has `shape = (2, 3, 4)`.
    -   Accessed via the `ndarray.shape` attribute.

3.  **Axis (plural: Axes):**
    -   Refers to a specific **dimension** of the array.
    -   Axes are numbered starting from 0.
    -   For a 2D array (matrix):
        -   `axis=0` refers to the **rows** (iterating *down* the rows). Operations along `axis=0` often collapse rows.
        -   `axis=1` refers to the **columns** (iterating *across* the columns). Operations along `axis=1` often collapse columns.
    -   For a 3D array:
        -   `axis=0` refers to the "depth" or layers.
        -   `axis=1` refers to the rows within each layer.
        -   `axis=2` refers to the columns within each layer.
    -   Many NumPy functions take an `axis` parameter to specify along which dimension the operation should be performed (e.g., `np.sum(arr, axis=0)` sums elements down each column).

## Visualization with AnyBlock Tabs

[list2tab]
- 1D Array (Vector)
	```python
	import numpy as np
	arr1d = np.array()
	print(f"arr1d: {arr1d}")
	print(f"arr1d.ndim: {arr1d.ndim}")   # Output: 1
	print(f"arr1d.shape: {arr1d.shape}") # Output: (4,)
	print(f"arr1d.size: {arr1d.size}")   # Output: 4
	```
	```mermaid
	graph LR
    subgraph arr1d_Shape_4
        Idx0((0: 1)) --- Idx1((1: 2)) --- Idx2((2: 3)) --- Idx3((3: 4))
    end
    Note[Axis 0 Length 4] --> arr1d_Shape_4
    style Note fill:#f9f,stroke:#333,stroke-width:2px
	```
	- 2D Array (Matrix)
	```python
	import numpy as np
	arr2d = np.array([,])
	print(f"arr2d:\n{arr2d}")
	print(f"arr2d.ndim: {arr2d.ndim}")   # Output: 2
	print(f"arr2d.shape: {arr2d.shape}") # Output: (2, 3)
	print(f"arr2d.size: {arr2d.size}")   # Output: 6
	```
	```mermaid
	graph TD
    subgraph arr2d_Shape_2_3
        subgraph Axis0_Rows_Len2[Axis 0 Rows Length 2]
            R0["Row 0"] --> C00((0,0: 1))
            R0 --> C01((0,1: 2))
            R0 --> C02((0,2: 3))
            R1["Row 1"] --> C10((1,0: 4))
            R1 --> C11((1,1: 5))
            R1 --> C12((1,2: 6))
        end
        subgraph Axis1_Cols_Len3[Axis 1 Columns Length 3]
            direction LR
            C0((Col 0)) --- C1((Col 1)) --- C2((Col 2))
        end
        R0 --- R1
    end
	```
	-   `axis=0` refers to movement "down" the rows. `arr2d[0,:]` is the first row ``.
	-   `axis=1` refers to movement "across" the columns. `arr2d[:,0]` is the first column ``.
- 3D Array (Tensor)
	```python
	import numpy as np
	arr3d = np.array([
	    [ # Layer 0
	        ,
	        
	    ],
	    [ # Layer 1
	        ,
	        
	    ]
	])
	print(f"arr3d:\n{arr3d}")
	print(f"arr3d.ndim: {arr3d.ndim}")   # Output: 3
	print(f"arr3d.shape: {arr3d.shape}") # Output: (2, 2, 3) (2 layers, 2 rows, 3 columns)
	print(f"arr3d.size: {arr3d.size}")   # Output: 12
	```
	```d2
	# arr3d: shape(2, 2, 3)
	arr3d: {
	  layer0: {
	    row0: {1; 2; 3}
	    row1: {4; 5; 6}
	  }
	  layer1: {
	    row0: {7; 8; 9}
	    row1: {10; 11; 12}
	  }
	}
	# Axis 0: Layers (layer0, layer1)
	# Axis 1: Rows (within each layer)
	# Axis 2: Columns (within each row)
	```

## Related Concepts
- [[NumPy_ndarray]] (The object these attributes describe)
- [[NumPy_Reshaping]] (Changing the shape of an array)
- [[NumPy_Indexing_Slicing]] (Uses axes and shape for access)
- [[Matrix_Math]] (Matrix dimensions correspond to shape of 2D array)
- Tensors (Higher-dimensional arrays)

## Questions / Further Study
>[!question] When we talk about dimension, are we referring to matrix dimension or the dimension of the ndarray? (WS_NumPy)
> In NumPy:
> - **`ndarray.ndim`** (dimension of the ndarray, or rank): This refers to the **number of axes**. A vector is 1D, a matrix is 2D, etc.
> - **Matrix dimension** (e.g., a "2x3 matrix"): This refers to the *size along each axis* for a 2D array, which corresponds to the `ndarray.shape` attribute (e.g., `(2, 3)`).
> So, a 2x3 matrix is a 2-dimensional `ndarray` with a shape of `(2, 3)`.

---
**Source:** Worksheet WS_NumPy, NumPy Documentation