---
tags:
  - math
  - linear_algebra
  - concept
  - matrix
  - property
  - matrix_operations
aliases:
  - Matrix Associativity
related:
  - "[[Linear_Algebra]]"
  - "[[Matrix_Math]]"
  - "[[Matrix_Operations]]"
  - "[[Matrix_Addition]]"
  - "[[Matrix_Multiplication]]"
  - "[[Distributive_Law_Matrix]]"
  - "[[Commutativity_Matrix]]"
worksheet:
  - WS11
date_created: 2025-04-12
---
# Associativity (Matrices)

## Definition

**Associativity** is a property of binary operations where rearranging the parentheses in an expression involving only that operation does not change the result (i.e., `(a op b) op c = a op (b op c)`). In the context of matrices:

-   **Matrix Addition IS Associative:** For any three matrices `A`, `B`, and `C` of the same dimensions:
    `(A + B) + C = A + (B + C)`

-   **Matrix Multiplication IS Associative:** For any three matrices `A`, `B`, and `C` where the dimensions are compatible for the multiplications involved:
    `(A * B) * C = A * (B * C)`

## Importance

- **Addition:** Associativity means we can sum multiple matrices without worrying about the order of pairwise additions (`A + B + C`).
- **Multiplication:** Associativity is crucial. It means we can multiply a chain of matrices `A * B * C * D` by grouping the multiplications in any way (e.g., `(AB)(CD)`, `A(BC)D`, `((AB)C)D`), and the final result will be the same. This is important because the *cost* of matrix multiplication depends heavily on the dimensions, and choosing an optimal multiplication order (though yielding the same result) can significantly impact performance (e.g., matrix chain multiplication problem).

## Note on Commutativity

While matrix multiplication is associative, it is **not** generally [[Commutativity_Matrix|commutative]]. The order of matrices matters (`A * B ≠ B * A`), but the grouping for a sequence of multiplications does not (`(A * B) * C = A * (B * C)`).

## Related Concepts
- [[Linear_Algebra]], [[Matrix_Math]]
- [[Matrix_Operations]], [[Matrix_Addition]], [[Matrix_Multiplication]]
- [[Distributive_Law_Matrix]]
- [[Commutativity_Matrix]]

## Questions / Further Study
>[!question] Describe the distributive, commutative and associative properties of matrix operations. (WS11)
> - **[[Distributive_Law_Matrix|Distributive]]:** Matrix multiplication distributes over matrix addition: `A(B+C) = AB + AC` and `(A+B)C = AC + BC`.
> - **[[Commutativity_Matrix|Commutative]]:**
>     - Matrix *addition* IS commutative: `A + B = B + A`.
>     - Matrix *multiplication* IS **NOT** generally commutative: `A * B ≠ B * A`.
> - **Associative:**
>     - Matrix *addition* IS associative: `(A + B) + C = A + (B + C)`.
>     - Matrix *multiplication* IS associative: `(A * B) * C = A * (B * C)`.

---
**Source:** Worksheet WS11