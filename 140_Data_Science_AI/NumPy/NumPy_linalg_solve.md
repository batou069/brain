---
tags:
  - numpy
  - python
  - linear_algebra
  - function
  - matrix_operations
  - system_of_equations
aliases:
  - np.linalg.solve
  - NumPy Solve Linear System
related:
  - "[[NumPy_linalg_Module]]"
  - "[[Linear_Equations]]" # Placeholder
  - "[[Matrix_Math]]"
  - "[[Vector_Math]]"
  - "[[NumPy_linalg_inv]]" # Can be used but solve is often better
  - "[[LinAlgError]]"
worksheet: [WS_NumPy]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# `np.linalg.solve()`

## Definition

`numpy.linalg.solve(a, b)` computes the **exact solution `x`** to a system of linear scalar equations represented by `ax = b`, where `a` is a square coefficient matrix and `b` is a 1D or 2D array (representing one or more constant vectors).

## Syntax

```python
numpy.linalg.solve(a, b)
```

- **`a`**: Coefficient matrix. Must be square and non-singular (invertible). Shape `(..., M, M)`.
- **`b`**: Ordinate or "dependent variable" values. Shape `(..., M)` or `(..., M, K)`.

## Return Value

-   An `ndarray` `x` representing the solution.
-   Shape matches `b`. If `b` is `(M,)`, `x` is `(M,)`. If `b` is `(M, K)`, `x` is `(M, K)`, where each column of `x` is the solution for the corresponding column of `b`.

## Raises

-   **`LinAlgError`**: If `a` is singular (non-invertible) or not square.

## Key Aspects

- **Solves `ax = b`:** Finds the vector `x` that satisfies the matrix equation.
- **Requires Invertible `a`:** The coefficient matrix `a` must be square and have a non-zero [[Matrix_Determinant|determinant]] for a unique solution to exist.
- **Numerical Stability & Efficiency:** `np.linalg.solve(a, b)` is generally **preferred over** calculating `x = np.linalg.inv(a) @ b` for solving linear systems. `solve()` often uses more numerically stable algorithms (like LU decomposition) and can be more efficient as it avoids explicitly computing the inverse, which can be prone to larger errors.
- **Multiple Right-Hand Sides:** If `b` is a 2D array (a stack of vectors), `solve` will efficiently solve the system for each column vector in `b`.

## Example

Solve the system:
`x + 2y = 1`
`3x + 4y = -1`

This can be written as `Ax = B`:
`A = [[1, 2], [3, 4]]`
`x_vec = [x, y]`
`B = [1, -1]`

```python
import numpy as np

# Coefficient matrix A
A = np.array([
    ,
    
])

# Constant vector B
B = np.array()

print(f"Matrix A:\n{A}")
print(f"Vector B: {B}")

try:
    # Solve for x_vec (which is [x, y])
    solution_x_vec = np.linalg.solve(A, B)
    print(f"\nSolution [x, y]: {solution_x_vec}") # Expected: [-3.  2.]

    # Verify the solution: A @ x_vec should be close to B
    verification = A @ solution_x_vec
    print(f"Verification A @ solution: {verification}")
    print(f"Is solution correct? {np.allclose(verification, B)}")

except np.linalg.LinAlgError as e:
    print(f"\nError solving system: {e}")

# Example with multiple right-hand sides
# Solve A * X = B_multi
# where X = [x1, x2] and B_multi = [b1, b2]
# b1 = [1, -1] (from above)
# b2 = [5, 6]
B_multi = np.array([, ]).T # Shape (2,2)
print(f"\nMatrix B_multi:\n{B_multi}")
try:
    solution_X_multi = np.linalg.solve(A, B_multi)
    print(f"\nSolution X for multiple RHS:\n{solution_X_multi}")
    # Column 0 of solution_X_multi is solution for B_multi[:,0]
    # Column 1 of solution_X_multi is solution for B_multi[:,1]
    # Expected:
    # [[-3.  -4.]
    #  [ 2.   4.5]]
except np.linalg.LinAlgError as e:
    print(f"\nError solving multi-RHS system: {e}")
```

## Related Concepts
- [[NumPy_linalg_Module]]
- [[Linear_Equations]] (The type of problem being solved)
- [[Matrix_Math]], [[Vector_Math]]
- [[NumPy_linalg_inv]] (Alternative, but often less preferred for solving)
- [[Gaussian_Elimination]], LU Decomposition (Underlying algorithms often used by `solve`)
- [[LinAlgError]]

---
**Source:** Worksheet WS_NumPy, NumPy Documentation