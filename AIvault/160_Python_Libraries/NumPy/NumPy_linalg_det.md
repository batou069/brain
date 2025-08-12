---
tags:
  - numpy
  - python
  - linear_algebra
  - function
  - matrix_operations
aliases:
  - np.linalg.det
  - NumPy Matrix Determinant
related:
  - "[[NumPy_linalg_Module]]"
  - "[[Matrix_Determinant]]"
  - "[[Square_Matrix]]"
  - "[[Matrix_Inverse]]" # Invertibility depends on determinant
  - "[[LinAlgError]]"
worksheet: [WS_NumPy]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# `np.linalg.det()`

## Definition

`numpy.linalg.det(a)` computes the **[[Matrix_Determinant|determinant]]** of a square matrix `a` or a stack of square matrices. The determinant is a scalar value that can provide information about the matrix, such as its invertibility.

## Syntax

```python
numpy.linalg.det(a)
```

- **`a`**: Input array. Must be a square matrix (shape `(..., M, M)`), meaning the last two dimensions must be equal.

## Return Value

-   A `float` or `complex` `ndarray` (or scalar if input is 2D) containing the determinant(s).
-   If `a` is a stack of matrices, the determinants are computed for each matrix in the stack.

## Key Aspects

- **Square Matrices Only:** The input array's last two dimensions must be square.
- **Invertibility:** A matrix is invertible if and only if its determinant is non-zero. Due to floating-point inaccuracies, a computed determinant might be very small (e.g., `1e-18`) instead of exactly zero for a theoretically singular matrix. It's often better to check for singularity using other methods like matrix rank or condition number in practice, or by attempting inversion and catching `LinAlgError`.
- **Geometric Interpretation:** For a 2x2 matrix, the absolute value of the determinant is the area of the parallelogram spanned by its column (or row) vectors. For a 3x3 matrix, it's the volume of the parallelepiped.

## Example

```python
import numpy as np

# 2x2 Matrix
A = np.array([
    ,
    
])
det_A = np.linalg.det(A)
print(f"Matrix A:\n{A}")
print(f"Determinant of A: {det_A}") # Expected: 1*4 - 2*3 = 4 - 6 = -2.0

# 3x3 Matrix
B = np.array([
    ,
    ,
    
])
det_B = np.linalg.det(B)
print(f"\nMatrix B:\n{B}")
print(f"Determinant of B: {det_B}") # Expected: 0.0 (Singular matrix)

# Singular Matrix Example
C = np.array([
    , # Row 2 is 2*Row 1
    
])
det_C = np.linalg.det(C)
print(f"\nMatrix C (singular):\n{C}")
print(f"Determinant of C: {det_C}") # Expected: close to 0.0

# Stack of matrices
D_stack = np.array([
    [ ,  ], # Matrix 1
    [ ,  ],
    [ ,  ], # Matrix 2
    [ ,  ]
])
det_D_stack = np.linalg.det(D_stack)
print(f"\nMatrix D_stack:\n{D_stack}")
print(f"Determinants of D_stack matrices: {det_D_stack}") # Expected: array([-2., -2.])
```

## Related Concepts
- [[NumPy_linalg_Module]]
- [[Matrix_Determinant]] (Mathematical concept)
- [[Square_Matrix]]
- [[Matrix_Inverse]] (Invertible if determinant is non-zero)
- Singularity (A matrix is singular if its determinant is 0)
- [[LinAlgError]] (Can be raised by `np.linalg.inv` for singular matrices)

---
**Source:** Worksheet WS_NumPy, NumPy Documentation