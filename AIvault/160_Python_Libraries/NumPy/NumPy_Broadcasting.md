---
tags:
  - numpy
  - python
  - array_manipulation
  - concept
  - core
  - performance
aliases:
  - Broadcasting (NumPy)
  - NumPy Broadcast Rules
related:
  - "[[NumPy_ndarray]]"
  - "[[NumPy_Dimension_Shape_Axis]]"
  - "[[NumPy_Vectorization]]"
  - "[[NumPy_Universal_Functions]]"
worksheet: [WS_NumPy]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# NumPy Broadcasting

## Definition

**Broadcasting** is a powerful mechanism in [[NumPy]] that allows arithmetic operations to be performed on `ndarray`s of **different shapes**, provided they meet certain compatibility rules. It describes how NumPy treats arrays with different shapes during element-wise operations, "broadcasting" the smaller array across the larger array so that they have compatible shapes. This is done without actually making copies of the data, leading to efficient computation.

## Broadcasting Rules

NumPy compares the shapes of the two arrays element-wise, starting from the trailing (rightmost) dimensions and working inwards. Two dimensions are compatible if:

1.  They are **equal**, or
2.  One of them is **1**.

If these conditions are not met for any dimension, a `ValueError` is raised, indicating the arrays are not compatible for broadcasting. Arrays do not need to have the same number of dimensions. If one array has fewer dimensions, it is conceptually padded with dimensions of size 1 on its left side until its `ndim` matches the other array.

Once the shapes are compatible, the smaller array is "broadcast" across the larger array:
- If a dimension has size 1, the values from that dimension are conceptually "stretched" or "copied" along that dimension to match the size of the corresponding dimension in the other array.
- The resulting array has a shape where each dimension is the maximum of the sizes of the input arrays' corresponding dimensions.

## Visualization with AnyBlock Tabs

[list2tab]
- Scalar and 1D Array
	```python
	import numpy as np
	a = np.array()  # Shape: (4,)
	b = 5                  # Scalar (conceptually shape (1,) or just treated specially)
	result = a + b         # b is broadcast to [5, 5, 5, 5]
	# result is [6, 7, 8, 9]
	```
	```mermaid
	graph TD
    subgraph Array_A_1D_Shape_4
        A0(1)---A1(2)---A2(3)---A3(4)
    end
    ScalarB(Scalar B = 5)
    subgraph Result_1D_Shape_4
        R0("1+5=6")---R1("2+5=7")---R2("3+5=8")---R3("4+5=9")
    end
    ScalarB -->|Broadcasts to each element| Array_A_1D_Shape_4
    Array_A_1D_Shape_4 -->|Element-wise Op| Result_1D_Shape_4
	```
- 1D Array and 2D Array
	```python
	import numpy as np
	matrix = np.array([, # Shape: (2, 3)
	                         , ])
	vector = np.array()           # Shape: (3,)
	result = matrix + vector         # vector is broadcast across rows of matrix
	# vector becomes [[10, 20, 30], [10, 20, 30]] conceptually
	# result:
	# [[11, 22, 33],
	#  [14, 25, 36]]
	```
	%% 
	1. `vector` (shape `(3,)`) compared with `matrix` (shape `(2,3)`).
	2. `vector` padded to `(1,3)` conceptually.
	3. Trailing dimensions: `3` and `3` are equal.
	4. Leading dimensions: `1` and `2`. `1` is compatible with `2`.
	5. `vector` is broadcast along `axis=0`. Result shape: `(2,3)`.
	%%
- 2D Array and Column Vector
	```python
	import numpy as np
	matrix = np.array([,]) # Shape: (2,3)
	col_vec = np.array([).reshape(2,1) # Shape: (2,1)
	# col_vec: [[10], [20]]
	result = matrix + col_vec
	# col_vec becomes [[10, 10, 10], [20, 20, 20]] conceptually
	# result:
	# [[11, 12, 13],
	#  [24, 25, 26]]
	```
	%%
	1. `col_vec` (shape `(2,1)`) compared with `matrix` (shape `(2,3)`).
	2. Trailing dimensions: `1` and `3`. `1` is compatible with `3`.
	3. Leading dimensions: `2` and `2` are equal.
	4. `col_vec` is broadcast along `axis=1`. Result shape: `(2,3)`.
	%%
- Incompatible Shapes (Error)
	```python
	import numpy as np
	a = np.array([,]) # Shape (2,3)
	b = np.array()        # Shape (4,)
	# result = a + b # ValueError: operands could not be broadcast together
	```
	%%
	1. `b` (shape `(4,)`) padded to `(1,4)`.
	2. `a` (shape `(2,3)`) and `b` (shape `(1,4)`).
	3. Trailing dimensions: `3` and `4` are **not** equal and neither is `1`. Incompatible.
	%%

## Advantages

- **Code Conciseness:** Allows writing cleaner and more compact code for array operations.
- **Memory Efficiency:** Avoids creating unnecessary copies of data in memory. The "stretching" is conceptual; NumPy performs the operations efficiently using the original data and strides.
- **Performance:** Operations are often executed by underlying C code, making them fast.

## Related Concepts
- [[NumPy_ndarray]], [[NumPy_Dimension_Shape_Axis]]
- [[NumPy_Vectorization]] (Broadcasting is a key part of how vectorization works with different shapes)
- [[NumPy_Universal_Functions]] (Ufuncs leverage broadcasting)

## Questions / Further Study
>[!question] When does broadcasting occur? (WS_NumPy)
> Broadcasting occurs during arithmetic operations (and other universal functions) between NumPy arrays of **different shapes** when their shapes are **compatible** according to the broadcasting rules (dimensions are equal, or one of them is 1, compared element-wise from trailing dimensions).

>[!question] When is it a problem? (WS_NumPy)
> Broadcasting itself is not inherently a problem; it's a feature. A problem (a `ValueError`) occurs when:
> 1.  The arrays' shapes are **not compatible** according to the rules (i.e., for a given dimension, they are different and neither is 1).
> 2.  **Unintended Broadcasting:** If the programmer expects arrays to have the same shape but one has a singleton dimension (size 1) that causes unintended broadcasting, the calculation might proceed without error but produce a logically incorrect result. This can be subtle to debug. Explicitly reshaping or checking shapes can prevent this. For example, adding a row vector of shape `(1, N)` to a matrix of shape `(M, N)` will broadcast the row vector to each row of the matrix. If the intent was to add a column vector, it must first be shaped to `(M, 1)`.

---
**Source:** Worksheet WS_NumPy, NumPy Documentation