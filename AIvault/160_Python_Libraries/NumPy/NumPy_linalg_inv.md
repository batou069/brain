---
tags:
  - numpy
  - python
  - linear_algebra
  - function
  - matrix_operations
aliases:
  - np.linalg.inv
  - NumPy Matrix Inverse
related:
  - "[[NumPy_linalg_Module]]"
  - "[[Matrix_Inverse]]"
  - "[[Square_Matrix]]"
  - "[[Identity_Matrix]]"
  - "[[Matrix_Determinant]]" # Related to invertibility
  - "[[NumPy_linalg_solve]]" # Often preferred for solving Ax=b
  - "[[LinAlgError]]" # Placeholder for NumPy's linalg error
worksheet: [WS_NumPy] # Implied by "useful functions in np.linalg"
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# `np.linalg.inv()`

## Definition

`numpy.linalg.inv(a)` computes the multiplicative **[[Matrix_Inverse|inverse]]** of a given square matrix `a`. If `a` is a matrix, its inverse `a_inv` is such that `a @ a_inv` (or `a_inv @ a`) results in the [[Identity_Matrix]] (within floating-point precision).

## Syntax

```python
numpy.linalg.inv(a)
```

- **`a`**: Input array. Must be a square matrix (or a stack of square matrices). If `a` is a stack of matrices, the inverse is computed for each matrix in the stack.

## Return Value

-   An `ndarray` containing the inverse of `a`.
-   The `dtype` of the returned array is usually `float64` or `complex128`, even if the input array `a` has an integer `dtype`, because inverses often involve fractions.

## Raises

-   **`LinAlgError`**: If matrix `a` is singular (non-invertible, i.e., its [[Matrix_Determinant|determinant]] is zero or very close to zero) or not square.

## Key Aspects

- **Square Matrices Only:** The input must be a square 2D array or a stack of square 2D arrays (where the last two dimensions are square).
- **Invertibility:** The matrix must be non-singular for the inverse to exist.
- **Numerical Stability:** For solving systems of linear equations `Ax = b`, using `np.linalg.solve(A, b)` is generally preferred over `x = np.linalg.inv(A) @ b` because `solve()` is often more numerically stable and can be faster.
- **Floating-Point Precision:** Due to floating-point arithmetic, `A @ inv(A)` might result in an identity matrix with very small non-zero off-diagonal elements or diagonal elements slightly off from 1.0. Use `np.allclose(A @ np.linalg.inv(A), np.eye(N))` to check.

## Example

```python
import numpy as np

# Define a square, invertible matrix
A = np.array([
    ,
    
])
print("Matrix A:\n", A)

# Compute the inverse
try:
    A_inv = np.linalg.inv(A)
    print("\nInverse of A (A_inv):\n", A_inv)

    # Verify: A @ A_inv should be close to the identity matrix
    identity_check = A @ A_inv
    print("\nA @ A_inv:\n", identity_check)

    # Check if it's close to identity
    identity_matrix = np.eye(A.shape[0])
    print(f"\nIs A @ A_inv close to identity? {np.allclose(identity_check, identity_matrix)}")

except np.linalg.LinAlgError as e:
    print(f"\nError inverting matrix A: {e}")

# Example of a singular matrix
B = np.array([
    ,  # Rows are linearly dependent
    
])
print("\nMatrix B (singular):\n", B)
try:
    B_inv = np.linalg.inv(B)
    print("Inverse of B:\n", B_inv) # This part likely won't be reached
except np.linalg.LinAlgError as e:
    print(f"Error inverting matrix B: {e}") # Expected: Singular matrix

# Example with a stack of matrices
C_stack = np.array([
    [ ,  ],
    [ ,  ], # Matrix 1
    [ ,  ],
    [ ,  ]  # Matrix 2
])
print("\nMatrix C_stack (shape 2,2,2):\n", C_stack)
try:
    C_stack_inv = np.linalg.inv(C_stack)
    print("\nInverse of C_stack:\n", C_stack_inv)
    print("\nC_stack[0] @ C_stack_inv[0]:\n", C_stack[0] @ C_stack_inv[0])
except np.linalg.LinAlgError as e:
    print(f"Error inverting matrix C_stack: {e}")
```

## Related Concepts
- [[NumPy_linalg_Module]]
- [[Matrix_Inverse]] (Mathematical concept)
- [[Square_Matrix]], [[Identity_Matrix]]
- [[Matrix_Determinant]] (Non-zero determinant implies invertibility)
- [[NumPy_linalg_solve]] (Often preferred for solving linear systems)
- [[LinAlgError]] (NumPy exception for linear algebra errors)
- `@` operator (matrix multiplication)
- `np.allclose()` (For comparing floating-point arrays)

---
**Source:** Worksheet WS_NumPy, NumPy Documentation