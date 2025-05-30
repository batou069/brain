---
tags:
  - math
  - linear_algebra
  - concept
  - matrix
  - square_matrix
  - operation
aliases:
  - Determinant
  - det(A)
  - "|A|"
related:
  - "[[Matrix_Math]]"
  - "[[Square_Matrix]]"
  - "[[Matrix_Inverse]]"
  - "[[Linear_Equations]]"
  - "[[Linear_Algebra]]"
  - "[[Cofactor_Expansion]]"
  - "[[Bitmap_DS]]"
worksheet:
  - WS11
date_created: 2025-04-12
---



# Matrix Determinant

## Definition

The **Determinant** is a scalar value that can be computed from the elements of a [[Square_Matrix|square matrix]]. It encodes certain properties of the matrix and the linear transformation it represents. The determinant of a matrix `A` is denoted as `det(A)`, `det A`, or `|A|`.

## Calculation

- **1x1 Matrix:** `A = [a]`, `det(A) = a`.
- **2x2 Matrix:**
  ```latex
  $$  
  A =
  \begin{bmatrix}
  a & b \\
  c & d
  \end{bmatrix}
  \quad \implies \quad
  \det(A) = ad - bc
    $$
  ```
- **3x3 Matrix (Sarrus' Rule or Cofactor Expansion):**
```latex
$$
A =
\begin{bmatrix}
a & b & c \\
d & e & f \\
g & h & i
\end{bmatrix}
\implies
\det(A) = a(ei - fh) - b(di - fg) + c(dh - eg)
$$
```
- **NxN Matrix (General):** Typically calculated using **Cofactor Expansion** (Laplace expansion) along any row or column, or more efficiently using methods derived from Gaussian elimination (row reduction to triangular form; determinant is product of diagonal entries, adjusted for row swaps and scaling). See [[Minors_Cofactors_Adjugate]].

## Key Properties and Significance

- **Invertibility:** A square matrix `A` has an [[Matrix_Inverse|inverse]] (is invertible or nonsingular) **if and only if** `det(A) ≠ 0`. If `det(A) = 0`, the matrix is singular (non-invertible).
- **Geometric Interpretation:**
    - In 2D, `|det(A)|` represents the **area scaling factor** of the linear transformation represented by `A`.
    - In 3D, `|det(A)|` represents the **volume scaling factor**.
    - A zero determinant implies the transformation collapses space onto a lower dimension.
- **Linear Equations:** Indicates if a system `Ax = b` has a unique solution (`det(A) != 0`). Used in Cramer's rule.
- **Properties:**
    - `det(I) = 1`
    - `det(A * B) = det(A) * det(B)`
    - `det(A^T) = det(A)`
    - `det(A^-1) = 1 / det(A)`
    - `det(k * A) = k^n * det(A)` (for `n x n` matrix `A`)

## Related Concepts
- [[Linear_Algebra]], [[Matrix_Math]], [[Square_Matrix]]
- [[Matrix_Inverse]], Singularity
- [[Minors_Cofactors_Adjugate]] (Used in calculation - *to be created*)
- Geometric Transformations (Scaling factor interpretation)

## Questions / Further Study
>[!question] What is a determinant, and how does it relate to the properties of a matrix? (WS11)
> A **Determinant** is a scalar value calculated from a [[Square_Matrix]]. It relates to key properties:
> 1.  **Invertibility:** `det(A) != 0` iff `A` is invertible ([[Matrix_Inverse]] exists).
> 2.  **Linear Independence:** `det(A) != 0` iff rows/columns are linearly independent.
> 3.  **Geometric Scaling:** `|det(A)|` is the area/volume scaling factor of the transformation `A`.
> 4.  **System of Equations:** `det(A) != 0` implies a unique solution for `Ax=b`.

---
**Source:** Worksheet WS11