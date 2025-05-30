---
tags:
  - numpy
  - python
  - linear_algebra
  - module
  - function
aliases:
  - np.linalg
  - NumPy Linear Algebra
related:
  - "[[NumPy]]"
  - "[[Linear_Algebra]]"
  - "[[Matrix_Math]]"
  - "[[Vector_Math]]"
  - "[[Matrix_Inverse]]"
  - "[[Matrix_Determinant]]"
  - "[[Eigenvalue]]"
  - "[[Singular_Value_Decomposition]]" # Placeholder
  - "[[NumPy_linalg_inv]]"
  - "[[NumPy_linalg_det]]"
  - "[[NumPy_linalg_solve]]"
  - "[[NumPy_linalg_eig]]"
  - "[[NumPy_linalg_norm]]"
worksheet: [WS_NumPy]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# NumPy `linalg` Module

## Definition

The `numpy.linalg` module in [[NumPy]] provides a collection of functions for performing common **linear algebra** operations. It includes functions for matrix decompositions, finding inverses and determinants, solving linear systems, calculating eigenvalues and eigenvectors, and more.

## Key Capabilities & Functions (WS_NumPy Question)

The `np.linalg` module contains many useful functions. Here are some prominent ones:

[list2tab]
- Core Matrix Operations
	- **`np.linalg.det(a)` ([[NumPy_linalg_det]]):** Computes the [[Matrix_Determinant|determinant]] of a square matrix or stack of matrices.
	  ```python
	  import numpy as np
	  A = np.array([, ])
	  det_A = np.linalg.det(A) # det_A = 1*4 - 2*3 = -2
	  ```
	- **`np.linalg.inv(a)` ([[NumPy_linalg_inv]]):** Computes the multiplicative [[Matrix_Inverse|inverse]] of a square matrix or stack of matrices. Raises `LinAlgError` if the matrix is singular.
	  ```python
	  # B = np.array([, ])
	  # B_inv = np.linalg.inv(B)
	  # print(B @ B_inv) # Should be close to identity matrix
	  ```
	- **`np.linalg.matrix_rank(M, tol=None)`:** Returns matrix rank of array using SVD method.
	- **`np.linalg.solve(a, b)` ([[NumPy_linalg_solve]]):** Solves a linear matrix equation `ax = b` for `x`. `a` must be square and non-singular. More stable and often faster than computing `inv(a) @ b`.
	  ```python
	  # Solve: x + 2y = 1; 3x + 5y = 2
	  # A_eq = np.array([, ])
	  # b_eq = np.array()
	  # x_solution = np.linalg.solve(A_eq, b_eq) # x_solution = [-1.,  1.]
	  ```
	- **`np.linalg.lstsq(a, b, rcond=...)`:** Computes the least-squares solution to `ax = b`. Useful when `a` is not square or the system is overdetermined.
- Decompositions
	- **`np.linalg.eig(a)` ([[NumPy_linalg_eig]]):** Computes the [[Eigenvalue|eigenvalues]] and right eigenvectors of a square array. Returns a tuple `(w, v)` where `w` contains eigenvalues and `v` contains eigenvectors as columns.
	- **`np.linalg.eigh(a, UPLO='L')`:** Computes eigenvalues and eigenvectors for a complex Hermitian or real symmetric matrix. More efficient and stable for these specific types.
	- **`np.linalg.svd(a, full_matrices=True, compute_uv=True, hermitian=False)`:** Computes the [[Singular_Value_Decomposition]] (SVD) of a matrix. Returns `U, s, Vh` where `a = U @ np.diag(s) @ Vh`.
	- **`np.linalg.qr(a, mode='reduced')`:** Computes the QR decomposition of a matrix.
	- **`np.linalg.cholesky(a)`:** Computes the Cholesky decomposition of a positive definite matrix.
- Norms and Other Properties
	- **`np.linalg.norm(x, ord=None, axis=None, keepdims=False)` ([[NumPy_linalg_norm]]):** Computes the matrix or vector norm.
	  - For vectors: `ord=1` (Manhattan), `ord=2` (Euclidean, default), `ord=np.inf` (max absolute value).
	  - For matrices: `ord='fro'` (Frobenius), `ord=1` (max absolute column sum), `ord=np.inf` (max absolute row sum), `ord=2` (largest singular value).
	  ```python
	  vec = np.array()
	  l2_norm = np.linalg.norm(vec) # sqrt(1^2 + 2^2 + 3^2)
	  ```
	- **`np.linalg.cond(x, p=None)`:** Computes the condition number of a matrix (indicates sensitivity to changes in input).
	- **`np.trace(a, offset=0, axis1=0, axis2=1, dtype=None, out=None)`:** (This is `np.trace`, not `np.linalg.trace`, but very related) Computes the sum along diagonals of the array. See [[Matrix_Trace]].
- Matrix Powers & Tensor Operations
	- **`np.linalg.matrix_power(a, n)`:** Raises a square matrix to the (integer) power `n`.
	- **`np.tensordot(a, b, axes=2)`:** Computes a tensor dot product along specified axes.
	- **`np.kron(a, b)`:** Computes the Kronecker product of two arrays.

## Usage Context

The `np.linalg` module is essential for:
- Solving systems of linear equations.
- Performing matrix decompositions used in various algorithms (e.g., SVD for PCA, eigendecomposition for understanding linear transformations).
- Calculating distances and norms in vector spaces.
- Many scientific and engineering computations.
- Core operations in machine learning algorithms.

## Related Concepts
- [[NumPy]], [[Linear_Algebra]], [[Matrix_Math]], [[Vector_Math]]
- Specific functions: [[NumPy_linalg_inv]], [[NumPy_linalg_det]], [[NumPy_linalg_solve]], [[NumPy_linalg_eig]], [[NumPy_linalg_norm]]
- [[Eigenvalue]], [[Singular_Value_Decomposition]]
- [[Matrix_Inverse]], [[Matrix_Determinant]]

---
**Source:** Worksheet WS_NumPy, NumPy Documentation