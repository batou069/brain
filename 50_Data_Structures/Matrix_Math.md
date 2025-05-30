---
tags:
  - math
  - linear_algebra
  - concept
  - matrix
  - data_structure
aliases:
  - Matrices
related:
  - "[["[[Linear_Algebra]]"]]"
  - "[["[[Vector_Math]]"]]"
  - "[["[[Matrix_Operations]]"]]"
  - "[["[[Square_Matrix]]"]]"
  - "[["[[Identity_Matrix]]"]]"
  - "[["[[Column_Vector]]"]]"
  - "[["[[Row_Vector]]"]]"
  - "[["[[Matrix_DS]]" # Implementation DS]]"
worksheet: [WS11]
date_created: 2025-04-12
---
## Definition

A **Matrix** is a rectangular array or table of numbers, symbols, or expressions, arranged in **rows** and **columns**. Matrices are fundamental objects in [[Linear_Algebra]] used to represent linear transformations, systems of linear equations, datasets, and more.

## Representation

A matrix `A` with `m` rows and `n` columns (an `m x n` matrix) is typically written as:

```latex
A =
\begin{bmatrix}
 a_{11} & a_{12} & \cdots & a_{1n} \\
 a_{21} & a_{22} & \cdots & a_{2n} \\
 \vdots & \vdots & \ddots & \vdots \\
 a_{m1} & a_{m2} & \cdots & a_{mn}
\end{bmatrix}
```

## Key Terminology & Types

- **Dimensions:** m x n (rows x columns).
- **Elements/Entries:** The individual items a_ij within the matrix.
- **[[Square_Matrix|Square Matrix]]:** A matrix where the number of rows equals the number of columns (m = n).
- **[[Column_Vector|Column Vector]]:** A matrix with only one column (n = 1).
- **[[Row_Vector|Row Vector]]:** A matrix with only one row (m = 1).
- **[[Identity_Matrix|Identity Matrix (I)]]:** A square matrix with 1s on the main diagonal (top-left to bottom-right) and 0s elsewhere. Acts as the multiplicative identity.
- **Zero Matrix:** A matrix where all elements are 0.
- **Diagonal Matrix:** A square matrix where all off-diagonal elements are 0.
- **Transpose (A^T):** A matrix obtained by swapping the rows and columns of matrix A. If A is m x n, A^T is n x m, and (A^T)_ij = A_ji.
    

## Visualization (3x2 Matrix)

```mermaid
graph TD
    subgraph Matrix A (3x2)
        direction LR
        R1["Row 1"] --> C11(a_11);
        R1 --> C12(a_12);
        R2["Row 2"] --> C21(a_21);
        R2 --> C22(a_22);
        R3["Row 3"] --> C31(a_31);
        R3 --> C32(a_32);

        subgraph Columns
           direction TB
           Col1["Col 1"] --> C11; Col1 --> C21; Col1 --> C31;
           Col2["Col 2"] --> C12; Col2 --> C22; Col2 --> C32;
        end
    end
```
## Use Cases

- Representing and solving systems of linear equations.
- Representing linear transformations (rotation, scaling, shearing) in geometry and graphics.
- Storing data (e.g., datasets where rows are samples and columns are features).
- Representing adjacency in graphs (Adjacency Matrix).
- Quantum mechanics, economics, probability theory, computer science.
    
## Related Concepts

- [[Linear_Algebra]]
- [[Vector_Math]] (Vectors as special matrices)
- [[Matrix_Operations]] (Addition, multiplication, transpose, etc.)
- Specific types: [[Square_Matrix]], [[Identity_Matrix]], [[Column_Vector]], [[Row_Vector]]
- [[Matrix_DS]] (How matrices are often stored in code)
    

---

**Source:** Worksheet WS11