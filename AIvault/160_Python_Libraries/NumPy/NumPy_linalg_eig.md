---
tags:
  - numpy
  - python
  - linear_algebra
  - function
  - matrix_operations
  - decomposition
aliases:
  - np.linalg.eig
  - NumPy Eigenvalues
  - NumPy Eigenvectors
related:
  - "[[NumPy_linalg_Module]]"
  - "[[Eigenvalue]]"
  - "[[Eigenvector]]" # Placeholder
  - "[[Square_Matrix]]"
  - "[[Linear_Transformation]]"
  - "[[Principal_Component_Analysis]]" # Placeholder (uses eigendecomposition)
worksheet: [WS_NumPy]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# `np.linalg.eig()`

## Definition

`numpy.linalg.eig(a)` computes the **[[Eigenvalue|eigenvalues]]** and right **[[Eigenvector|eigenvectors]]** of a square matrix `a`. For a square matrix `A`, a non-zero vector `v` is an eigenvector if `Av = λv`, where `λ` (lambda) is a scalar known as the eigenvalue corresponding to `v`.

## Syntax

```python
numpy.linalg.eig(a)
```

- **`a`**: Input array. Must be a square matrix (shape `(..., M, M)`).

## Return Value

A tuple `(w, v)` where:
-   **`w`**: An `ndarray` containing the eigenvalues.
    -   Shape `(..., M)`. Each entry `w[i]` is an eigenvalue.
    -   The eigenvalues are **not necessarily ordered**.
    -   For real matrices, eigenvalues can be complex (if the matrix is not symmetric). The `dtype` of `w` will be complex in such cases.
-   **`v`**: An `ndarray` containing the normalized (unit length) right eigenvectors.
    -   Shape `(..., M, M)`.
    -   The column `v[:, i]` is the eigenvector corresponding to the eigenvalue `w[i]`.

## Key Aspects

- **Square Matrices Only:** Input `a` must be square.
- **Right Eigenvectors:** Calculates right eigenvectors (`Av = λv`). Left eigenvectors (`v^H A = λ v^H`) can be found by `eig(A.T)`.
- **Normalization:** Eigenvectors are normalized to have a Euclidean length (L2 norm) of 1.
- **Non-Uniqueness of Eigenvectors:** Eigenvectors are unique only up to a non-zero scalar multiple. The sign of an eigenvector returned by `eig` might vary.
- **Complex Eigenvalues/Eigenvectors:** For real non-symmetric matrices, eigenvalues and eigenvectors can be complex. NumPy will return complex `dtype` arrays in this case.
- **Symmetric/Hermitian Matrices:** For real symmetric or complex Hermitian matrices, eigenvalues are always real. Use `np.linalg.eigh()` for these cases as it's more efficient and numerically stable, and guarantees real eigenvalues.
- **Repeated Eigenvalues:** If eigenvalues are repeated, the set of corresponding eigenvectors might not be uniquely determined or might not span a full eigenspace in some degenerate cases (though for distinct eigenvalues, eigenvectors are linearly independent).

## Eigendecomposition Relationship

If `v` is the matrix of eigenvectors (columns are eigenvectors) and `w` is a diagonal matrix of eigenvalues, then `A @ v = v @ np.diag(w)`.
This can be rewritten as `A = v @ np.diag(w) @ np.linalg.inv(v)` if `v` is invertible (i.e., if `A` has a full set of linearly independent eigenvectors, which is true for matrices with distinct eigenvalues or symmetric matrices). This is the eigendecomposition of `A`.

## Example

```python
import numpy as np

# Define a square matrix
A = np.array([
    ,
    
])
print("Matrix A:\n", A)

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("\nEigenvalues (w):\n", eigenvalues)
print("\nEigenvectors (v) (columns are eigenvectors):\n", eigenvectors)

# Verify: A @ v[:,i] should be close to w[i] * v[:,i]
print("\nVerification (A @ v[:,i] vs w[i] * v[:,i]):")
for i in range(len(eigenvalues)):
    Av = A @ eigenvectors[:, i]
    lambda_v = eigenvalues[i] * eigenvectors[:, i]
    print(f"For eigenvalue {eigenvalues[i]:.2f}:")
    print(f"  A @ v_{i}: {Av}")
    print(f"  λ * v_{i}: {lambda_v}")
    print(f"  Close? {np.allclose(Av, lambda_v)}")

# Example with complex eigenvalues/vectors from a real matrix
B = np.array([
    ,  # Rotation matrix scaled
    
])
print("\nMatrix B:\n", B)
eigvals_B, eigvecs_B = np.linalg.eig(B)
print("\nEigenvalues of B:\n", eigvals_B)       # Will be complex
print("\nEigenvectors of B:\n", eigvecs_B)     # Will be complex
```

## Related Concepts
- [[NumPy_linalg_Module]]
- [[Eigenvalue]], [[Eigenvector]] (Mathematical concepts)
- [[Square_Matrix]]
- [[Linear_Transformation]] (Eigenvectors show directions unchanged by the transformation)
- [[Eigendecomposition]]
- `np.linalg.eigh()` (For Hermitian/symmetric matrices)
- [[Principal_Component_Analysis]] (Relies on eigendecomposition of covariance matrix)

---
**Source:** Worksheet WS_NumPy, NumPy Documentation