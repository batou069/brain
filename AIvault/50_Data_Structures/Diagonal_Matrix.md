---
tags:
  - math
  - linear_algebra
  - concept
  - matrix
  - square_matrix
aliases: []
related:
  - "[[Matrix_Math]]"
  - "[[Square_Matrix]]"
  - "[[Identity_Matrix]]"
  - "[[Matrix_Operations]]"
  - "[[Eigenvalue]]" # Diagonalization relates to eigenvalues
worksheet: [WS11] # Implied concept
date_created: 2025-04-21
---
# Diagonal Matrix

## Definition

A **Diagonal Matrix** is a [[Square_Matrix|square matrix]] in which all the entries **outside the main diagonal** are zero. The entries on the main diagonal can be any value, including zero.

## Representation

An `n x n` matrix `D` is diagonal if `D_ij = 0` for all `i ≠ j`.

```latex
D =
\begin{bmatrix}
 d_{11} & 0      & \cdots & 0 \\
 0      & d_{22} & \cdots & 0 \\
 \vdots & \vdots & \ddots & \vdots \\
 0      & 0      & \cdots & d_{nn}
\end{bmatrix}
```

## Key Properties

- **Easy Operations:** Matrix operations involving diagonal matrices are often very simple:
    - **Addition/Subtraction:** `D1 + D2` is diagonal, performed element-wise on the diagonal.
    - **Multiplication:** `D1 * D2` is diagonal, with `(D1*D2)_ii = (D1)_ii * (D2)_ii`. Multiplication *is* commutative for diagonal matrices of the same size.
    - **Inverse:** If all diagonal entries `d_ii` are non-zero, the inverse `D^-1` is a diagonal matrix with entries `1 / d_ii`. If any `d_ii` is zero, the matrix is singular (non-invertible).
    - **Determinant:** The [[Matrix_Determinant|determinant]] is simply the product of the diagonal entries: `det(D) = d_11 * d_22 * ... * d_nn`.
    - **Trace:** The [[Matrix_Trace|trace]] is the sum of the diagonal entries (same as any square matrix).
- **[[Identity_Matrix|Identity Matrix]]:** A special case of a diagonal matrix where all diagonal entries are 1.
- **Scalar Matrix:** A diagonal matrix where all diagonal entries are equal (`d_11 = d_22 = ...`). Equivalent to a scalar multiplied by the identity matrix (`c * I`).
- **Diagonalization:** Many important square matrices can be "diagonalized," meaning they are similar to a diagonal matrix (`A = P * D * P^-1`, where D is diagonal). The diagonal entries of `D` are the eigenvalues of `A`.

## Use Cases

- Representing scaling transformations along coordinate axes.
- Simplifying matrix calculations (e.g., powers of diagonal matrices are easy: `D^k` has diagonal entries `(d_ii)^k`).
- Appear in matrix decompositions like Singular Value Decomposition (SVD) and eigenvalue decomposition.
- Representing covariance matrices for uncorrelated variables in statistics.

## Related Concepts
- [[Matrix_Math]], [[Square_Matrix]], [[Linear_Algebra]]
- [[Identity_Matrix]] (Special case)
- [[Matrix_Operations]] (Simplified for diagonal matrices)
- [[Matrix_Determinant]], [[Matrix_Inverse]], [[Matrix_Trace]]
- Eigenvalues, Diagonalization

---
**Source:** Worksheet WS11 (Implied)