---
tags:
  - numpy
  - python
  - linear_algebra
  - function
  - vector_operations
  - matrix_operations
aliases:
  - np.linalg.norm
  - NumPy Vector Norm
  - NumPy Matrix Norm
related:
  - "[[NumPy_linalg_Module]]"
  - "[[Vector_Math]]" # Magnitude
  - "[[Matrix_Math]]"
  - "[[Norm]]" # Mathematical concept
  - "[[Unit_Vector]]" # Placeholder
worksheet: [WS_NumPy]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# `np.linalg.norm()`

## Definition

`numpy.linalg.norm(x, ord=None, axis=None, keepdims=False)` computes the **[[Norm|norm]]** of a vector or a matrix. A norm is a function that assigns a strictly positive length or size to each vector in a vector space (except for the zero vector, which has zero length). For matrices, norms measure their "magnitude" or "size" in various ways.

## Syntax

```python
numpy.linalg.norm(x, ord=None, axis=None, keepdims=False)
```

- **`x`**: Input array (vector or matrix).
- **`ord`**: Order of the norm. Default is `None`.
    - **For Vectors (1D arrays):**
        - `None` or `2`: L2 norm (Euclidean norm, default) - `sqrt(sum(abs(x_i)**2))`.
        - `1`: L1 norm (Manhattan norm) - `sum(abs(x_i))`.
        - `np.inf`: Max norm (infinity norm) - `max(abs(x_i))`.
        - `-np.inf`: Min norm - `min(abs(x_i))`.
        - Other integers `p`: L_p norm - `sum(abs(x_i)**p)**(1/p)`.
    - **For Matrices (2D arrays):**
        - `None` or `'fro'`: Frobenius norm (default) - `sqrt(sum(abs(a_ij)**2))`.
        - `1`: Max absolute column sum.
        - `-1`: Min absolute column sum.
        - `np.inf`: Max absolute row sum.
        - `-np.inf`: Min absolute row sum.
        - `2`: Largest singular value (spectral norm).
        - `-2`: Smallest singular value.
        - `'nuc'`: Nuclear norm.
- **`axis`**: If `x` is an N-D array, specifies the axis or axes along which the norms are computed.
    - If `axis` is an `int`, norms are computed for 1D slices along that axis.
    - If `axis` is a 2-tuple `(ax1, ax2)`, norms are computed on the 2D slices specified by these axes.
    - If `axis` is `None` (default), vector norm is computed if `x` is 1D, matrix norm if `x` is 2D. If `x` is N-D with N>2, it is treated as a stack of matrices if `ord` is a matrix norm, or flattened if `ord` is a vector norm.
- **`keepdims`**: If `True`, the axes which are normed over are left in the result as dimensions with size one.

## Return Value

-   An `ndarray` or `float` containing the norm(s).

## Examples

[list2tab]
- Vector Norms
	```python
	import numpy as np
	v = np.array()

	# L2 norm (Euclidean, default)
	norm_l2 = np.linalg.norm(v) # sqrt(1^2 + (-2)^2 + 3^2) = sqrt(1+4+9) = sqrt(14)
	print(f"Vector v: {v}")
	print(f"L2 norm of v: {norm_l2:.4f}") # Approx 3.7417

	# L1 norm (Manhattan)
	norm_l1 = np.linalg.norm(v, ord=1) # |1| + |-2| + |3| = 1 + 2 + 3 = 6
	print(f"L1 norm of v: {norm_l1}")

	# Max norm (Infinity norm)
	norm_inf = np.linalg.norm(v, ord=np.inf) # max(|1|, |-2|, |3|) = 3
	print(f"Max norm of v: {norm_inf}")
	```
- Matrix Norms
	```python
	import numpy as np
	M = np.array([
	    ,
	    
	])
	print(f"Matrix M:\n{M}")

	# Frobenius norm (default for matrices)
	norm_fro = np.linalg.norm(M) # sqrt(1^2+2^2+3^2+4^2) = sqrt(1+4+9+16) = sqrt(30)
	print(f"Frobenius norm of M: {norm_fro:.4f}") # Approx 5.4772

	# Max absolute column sum (ord=1)
	# Col0 sum = |1|+|3|=4, Col1 sum = |2|+|4|=6. Max is 6.
	norm_m1 = np.linalg.norm(M, ord=1)
	print(f"Matrix norm (ord=1) of M: {norm_m1}")

	# Max absolute row sum (ord=np.inf)
	# Row0 sum = |1|+|2|=3, Row1 sum = |3|+|4|=7. Max is 7.
	norm_minf = np.linalg.norm(M, ord=np.inf)
	print(f"Matrix norm (ord=np.inf) of M: {norm_minf}")
	```
- Norm along an Axis
	```python
	import numpy as np
	A = np.array([
	    ,
	    
	])
	print(f"Matrix A:\n{A}")

	# L2 norm of each column vector
	col_norms = np.linalg.norm(A, axis=0) # Norm along axis 0 (down columns)
	# Col0: sqrt(1^2+3^2)=sqrt(10), Col1: sqrt(2^2+4^2)=sqrt(20)
	print(f"L2 norm of columns: {col_norms}") # [3.16227766 4.47213595]

	# L2 norm of each row vector
	row_norms = np.linalg.norm(A, axis=1) # Norm along axis 1 (across rows)
	# Row0: sqrt(1^2+2^2)=sqrt(5), Row1: sqrt(3^2+4^2)=sqrt(25)=5
	print(f"L2 norm of rows: {row_norms}") # [2.23606798 5.        ]
	```

## Use Cases

- **[[Vector_Math|Vector Magnitude]]:** Calculating the length or magnitude of a vector.
- **Normalization:** Scaling a vector to have unit length (dividing a vector by its norm). See `NumPy_Vector_Normalization` exercise.
- **Distance Calculation:** The Euclidean distance between two vectors `u` and `v` is `np.linalg.norm(u - v)`.
- **Regularization (Machine Learning):** L1 and L2 norms are used in regularization terms to prevent overfitting.
- **Condition Number:** Matrix norms are used in calculating the condition number of a matrix.
- **Error Measurement:** Can be used to measure the "size" of an error vector or matrix.

## Related Concepts
- [[NumPy_linalg_Module]]
- [[Vector_Math]] (Vector magnitude)
- [[Matrix_Math]]
- [[Norm]] (Mathematical concept)
- [[Unit_Vector]] (A vector with norm 1)
- Euclidean Distance, Manhattan Distance

## Questions / Further Study
>[!question] Exercise: Calculate the magnitude of each vector in a collection of vectors. Normalize a collection of vectors so that each vector is of unit length.
> ```python
> import numpy as np
>
> # Collection of vectors (e.g., a 2D array where each row is a vector)
> vectors = np.array([
>     ,
>     ,
>     
> ])
> print("Original vectors:\n", vectors)
>
> # 1. Calculate the magnitude (L2 norm) of each vector
> # axis=1 to calculate norm along each row
> magnitudes = np.linalg.norm(vectors, axis=1, keepdims=True)
> print("\nMagnitudes of each vector:\n", magnitudes)
>
> # 2. Normalize each vector to unit length
> # Avoid division by zero if a vector has zero magnitude
> # (np.finfo(float).eps is a very small float to prevent division by zero warnings for actual zero vectors)
> normalized_vectors = vectors / (magnitudes + np.finfo(float).eps)
> print("\nNormalized vectors (unit length):\n", normalized_vectors)
>
> # Verify norms of normalized vectors (should be close to 1)
> normalized_magnitudes = np.linalg.norm(normalized_vectors, axis=1)
> print("\nMagnitudes of normalized vectors:\n", normalized_magnitudes)
> ```

---
**Source:** Worksheet WS_NumPy, NumPy Documentation