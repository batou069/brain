---
tags:
  - math
  - linear_algebra
  - concept
  - matrix
  - determinant
  - inverse_matrix
aliases:
  - Matrix Minors
  - Matrix Cofactors
  - Adjugate Matrix
  - Adjoint Matrix (Classical)
related:
  - "[[Matrix_Determinant]]"
  - "[[Matrix_Inverse]]"
  - "[[Square_Matrix]]"
  - "[[Linear_Algebra]]"
worksheet: [WS11] # Related to research link
date_created: 2025-04-21
---
# Minors, Cofactors, and Adjugate Matrix

## Definition

These concepts are used in [[Linear_Algebra]], primarily for calculating the [[Matrix_Determinant|determinant]] and the [[Matrix_Inverse|inverse]] of a [[Square_Matrix]] using the cofactor expansion method.

1.  **Minor (M<sub>ij</sub>):**
    -   The minor of an element `a_ij` (in row `i`, column `j`) of a square matrix `A` is the determinant of the submatrix obtained by deleting the `i`-th row and `j`-th column from `A`.

2.  **Cofactor (C<sub>ij</sub>):**
    -   The cofactor of an element `a_ij` is its minor multiplied by `(-1)^(i+j)`.
    -   `C_ij = (-1)^(i+j) * M_ij`
    -   The `(-1)^(i+j)` term creates a "checkerboard" pattern of signs (+, -, +, -...) starting with + in the top-left position.

3.  **Matrix of Cofactors:**
    -   A matrix formed by replacing each element `a_ij` of the original matrix `A` with its corresponding cofactor `C_ij`.

4.  **Adjugate Matrix (adj(A)):**
    -   The **transpose** of the Matrix of Cofactors.
    -   `adj(A) = [C_ij]^T` (Transpose of the cofactor matrix).
    -   Also known as the Adjoint Matrix or Classical Adjoint (distinct from the Hermitian adjoint).

## Usage

- **Determinant Calculation (Cofactor Expansion):**
  The determinant of `A` can be calculated by expanding along any row `i` or any column `j`:
  - Along row `i`: `det(A) = Σ (a_ik * C_ik)` (sum over column `k`)
  - Along column `j`: `det(A) = Σ (a_kj * C_kj)` (sum over row `k`)
  Example (along first row): `det(A) = a_11*C_11 + a_12*C_12 + ... + a_1n*C_1n`

- **Matrix Inverse Calculation:**
  If `det(A) ≠ 0`, the inverse of `A` can be calculated using the adjugate:
  `A^-1 = (1 / det(A)) * adj(A)`

## Example (2x2 Matrix)

Let `A = [ [a, b], [c, d] ]`

-   Minors:
    -   `M_11` (delete row 1, col 1) = `det([d]) = d`
    -   `M_12` (delete row 1, col 2) = `det([c]) = c`
    -   `M_21` (delete row 2, col 1) = `det([b]) = b`
    -   `M_22` (delete row 2, col 2) = `det([a]) = a`
-   Cofactors:
    -   `C_11 = (-1)^(1+1) * M_11 = +d`
    -   `C_12 = (-1)^(1+2) * M_12 = -c`
    -   `C_21 = (-1)^(2+1) * M_21 = -b`
    -   `C_22 = (-1)^(2+2) * M_22 = +a`
-   Matrix of Cofactors: `[ [d, -c], [-b, a] ]`
-   Adjugate Matrix `adj(A)` (Transpose of Cofactor Matrix): `[ [d, -b], [-c, a] ]`
-   Determinant: `det(A) = ad - bc`
-   Inverse: `A^-1 = (1 / (ad - bc)) * [ [d, -b], [-c, a] ]` (Matches the known 2x2 inverse formula).

## Notes

- Calculating determinants and inverses using cofactor expansion and adjugates becomes computationally very expensive for matrices larger than 3x3 or 4x4. [[Gaussian_Elimination]] based methods are generally much more efficient in practice.
- These concepts are important for theoretical understanding.

## Related Concepts
- [[Matrix_Determinant]] (Calculated using cofactors)
- [[Matrix_Inverse]] (Calculated using adjugate and determinant)
- [[Square_Matrix]]
- [[Linear_Algebra]]
- Transpose

---
**Source:** Worksheet WS11 (Research Link Implied)