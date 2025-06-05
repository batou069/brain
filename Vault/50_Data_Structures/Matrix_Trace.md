---
tags:
  - math
  - linear_algebra
  - concept
  - matrix
  - square_matrix
  - operation
aliases:
  - Trace of a Matrix
  - tr(A)
related:
  - "[[Matrix_Math]]"
  - "[[Square_Matrix]]"
  - "[[Linear_Algebra]]"
  - "[[Matrix_Operations]]"
  - "[[Eigenvalue]]"
worksheet:
  - WS11
date_created: 2025-04-12
---
# Matrix Trace

## Definition

The **Trace** of a [[Square_Matrix|square matrix]] `A`, denoted as `tr(A)`, is the **sum of the elements on the main diagonal** (the diagonal from the upper left to the lower right).

## Formula

For an `n x n` square matrix `A` with elements `a_ij`:

`tr(A) = Σ (a_ii) = a_11 + a_22 + ... + a_nn`

## Calculation Example

```latex
$$
A =
\begin{bmatrix}
\mathbf{5} & 2 & 9 \\
-1 & \mathbf{0} & 6 \\
7 & 3 & \mathbf{-4}
\end{bmatrix}
$$
`tr(A) = 5 + 0 + (-4) = 1`
```

## Key Properties

- **Defined only for Square Matrices.**
- **Linearity:** `tr(A + B) = tr(A) + tr(B)`; `tr(c * A) = c * tr(A)`.
- **Cyclic Property:** `tr(ABC) = tr(BCA) = tr(CAB)`.
- **Transpose:** `tr(A^T) = tr(A)`.
- **Similarity Invariance:** `tr(P^-1 * A * P) = tr(A)`.
- **Relation to Eigenvalues:** The trace equals the sum of the matrix's eigenvalues.

## Use Cases

- Invariant under change of basis.
- Theoretical insights via eigenvalue relation.
- Used in some physics, engineering, and ML formulas (e.g., Frobenius norm).

## Related Concepts
- [[Matrix_Math]], [[Square_Matrix]], [[Linear_Algebra]]
- Main Diagonal
- Eigenvalues
- [[Matrix_Operations]]

---
**Source:** Worksheet WS11