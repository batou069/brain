---
tags:
  - math
  - linear_algebra
  - concept
  - vector
  - matrix
aliases:
  - Row Matrix
related:
  - "[[Vector_Math]]"
  - "[[Matrix_Math]]"
  - "[[Linear_Algebra]]"
  - "[[Column_Vector]]"
  - "[[Matrix_Operations]]"
worksheet: [WS11] # Implied concept
date_created: 2025-04-21
---
# Row Vector

## Definition

A **Row Vector** (or Row Matrix) is a [[Matrix_Math|matrix]] consisting of a **single row**. A `1 × n` matrix is a row vector with `n` elements (columns).

## Representation

A row vector `v` with `n` elements is written as:

`v = [ v1 v2 ... vn ]`

## Significance

- **Alternative Vector Representation:** While [[Column_Vector|column vectors]] are often the default in many linear algebra contexts, row vectors are also used.
- **Vector-Matrix Multiplication:** When multiplying a vector `v` by a matrix `A` such that the vector comes first (`vA`), `v` must typically be treated as a row vector (`1 x m`) and `A` must be `m x n` for the multiplication to be defined. The result `vA` is another row vector (`1 x n`).
```
v * A = w
(1 x m) * (m x n) = (1 x n)
```
- **Linear Systems:** Sometimes used in representing linear combinations or parts of linear systems.

## Contrast with Column Vector

- **[[Column_Vector|Column Vector]]:** A matrix with a single column (`m x 1`).
- **Transpose Relationship:** The transpose (`^T`) of a row vector is a column vector, and vice-versa.
  `[ v1 v2 ... vn ]^T = [ v1 ]`
  `                    [ v2 ]`
  `                    [ .. ]`
  `                    [ vn ]`

## Visualization

Using LaTeX:
```latex
\mathbf{v} =
\begin{bmatrix}
 v_1 & v_2 & \cdots & v_n
\end{bmatrix}
```

## Related Concepts
- [[Linear_Algebra]], [[Vector_Math]], [[Matrix_Math]]
- [[Column_Vector]] (Contrasting concept)
- Matrix Transpose
- [[Matrix_Operations]] (Especially vector-matrix multiplication)

---
**Source:** Worksheet WS11 (Implied)