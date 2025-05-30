---
tags: [math, linear_algebra, concept, matrix, property, matrix_operations]
aliases: [Matrix Commutativity]
related: [Linear_Algebra, Matrix_Math, Matrix_Operations, Matrix_Addition, Matrix_Multiplication, Distributive_Law_Matrix, Associativity_Matrix]
worksheet: WS11
date_created: 2025-04-12
---
# Commutativity (Matrices)

## Definition

**Commutativity** is a property of binary operations where changing the order of the operands does not change the result (i.e., `a op b = b op a`). In the context of matrices:

-   **Matrix Addition IS Commutative:** For any two matrices `A` and `B` of the same dimensions:
    `A + B = B + A`

-   **Matrix Multiplication IS *NOT* Generally Commutative:** For two matrices `A` and `B` where the product `A * B` is defined, the product `B * A` may not even be defined (if dimensions don't match appropriately). Even if both `A * B` and `B * A` are defined (e.g., if `A` and `B` are [[Square_Matrix|square matrices]] of the same order), it is generally **not true** that `A * B = B * A`.

## Example (Non-Commutativity of Multiplication)

Let:
```latex
$$
A =
\begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}
\quad
B =
\begin{bmatrix}
0 & 1 \\
1 & 0
\end{bmatrix}
$$
```

Then:
```latex
$$
A * B =
\begin{bmatrix}
(1*0 + 2*1) & (1*1 + 2*0) \\
(3*0 + 4*1) & (3*1 + 4*0)
\end{bmatrix}
=
\begin{bmatrix}
2 & 1 \\
4 & 3
\end{bmatrix}
$$
```

```latex
$$
B * A =
\begin{bmatrix}
(0*1 + 1*3) & (0*2 + 1*4) \\
(1*1 + 0*3) & (1*2 + 0*4)
\end{bmatrix}
=
\begin{bmatrix}
3 & 4 \\
1 & 2
\end{bmatrix}
$$
```
Clearly, `A * B ≠ B * A`.

## Special Cases for Multiplication Commutativity

Matrix multiplication *can* commute in specific cases:
- If one matrix is the [[Identity_Matrix]] (`A * I = I * A = A`).
- If one matrix is the [[Matrix_Inverse|Inverse Matrix]] of the other (`A * A^-1 = A^-1 * A = I`).
- If one matrix is a scalar multiple of the other (`A * (c*A) = (c*A) * A`).
- If both matrices are diagonal matrices of the same order.

## Related Concepts
- [[Linear_Algebra]], [[Matrix_Math]]
- [[Matrix_Operations]], [[Matrix_Addition]], [[Matrix_Multiplication]]
- [[Distributive_Law_Matrix]]
- [[Associativity_Matrix]]

## Questions / Further Study
>[!question] Describe the distributive, commutative and associative properties of matrix operations. (WS11)
> - **[[Distributive_Law_Matrix|Distributive]]:** Matrix multiplication distributes over matrix addition: `A(B+C) = AB + AC` and `(A+B)C = AC + BC`.
> - **Commutative:**
>     - Matrix *addition* IS commutative: `A + B = B + A`.
>     - Matrix *multiplication* IS **NOT** generally commutative: `A * B ≠ B * A`.
> - **[[Associativity_Matrix|Associative]]:**
>     - Matrix *addition* IS associative: `(A + B) + C = A + (B + C)`.
>     - Matrix *multiplication* IS associative: `(A * B) * C = A * (B * C)`.

---
**Source:** Worksheet WS11