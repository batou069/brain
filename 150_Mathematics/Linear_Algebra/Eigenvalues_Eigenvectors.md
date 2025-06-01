---
tags:
  - mathematics
  - linear_algebra
  - matrix
  - eigenvalues
  - eigenvectors
  - eigendecomposition
  - concept
aliases:
  - Eigenvalue
  - Eigenvector
  - Characteristic Values
  - Characteristic Vectors
  - Eigendecomposition
related:
  - "[[Matrix]]"
  - "[[Vector]]"
  - "[[Transformation_Matrix]]"
  - "[[Matrix_Product]]"
  - "[[Determinant_Matrix]]"
  - "[[Singular_Value_Decomposition]]"
  - "[[Principal_Component_Analysis_PCA]]"
worksheet:
  - WS_Math_Foundations_1
date_created: 2025-05-30
---
# Eigenvalues and Eigenvectors

## Definition
For a given square [[Matrix|matrix]] $\mathbf{A}$ (typically $n \times n$), an **eigenvector** $\mathbf{v}$ is a non-zero [[Vector|vector]] such that when $\mathbf{A}$ acts on $\mathbf{v}$ (i.e., $\mathbf{A}\mathbf{v}$), the resulting vector is simply a scaled version of the original vector $\mathbf{v}$. The scaling factor is called the **eigenvalue**, usually denoted by $\lambda$ (lambda).

Mathematically, this relationship is expressed as:
$$ \mathbf{A}\mathbf{v} = \lambda\mathbf{v} $$
where:
- $\mathbf{A}$ is an $n \times n$ matrix.
- $\mathbf{v}$ is an $n \times 1$ non-zero column vector (the eigenvector).
- $\lambda$ is a [[Scalar|scalar]] (the eigenvalue associated with $\mathbf{v}$).

Eigenvalues can be real or complex numbers. For each eigenvalue, there can be infinitely many eigenvectors (any non-zero scalar multiple of an eigenvector is also an eigenvector for the same eigenvalue). The set of all eigenvectors corresponding to a single eigenvalue, together with the zero vector, forms a subspace called the **eigenspace**.

## Geometric Interpretation
When a [[Transformation_Matrix|linear transformation]] represented by matrix $\mathbf{A}$ is applied to one of its eigenvectors $\mathbf{v}$, the direction of $\mathbf{v}$ remains unchanged (or is exactly reversed if $\lambda < 0$). The vector is only scaled (stretched, shrunk, or flipped) by the factor $\lambda$. Eigenvectors represent the directions that are preserved (up to scaling) by the linear transformation.

- If $\lambda > 1$: $\mathbf{v}$ is stretched.
- If $0 < \lambda < 1$: $\mathbf{v}$ is shrunk.
- If $\lambda < 0$: $\mathbf{v}$ is flipped and then scaled.
- If $\lambda = 1$: $\mathbf{v}$ is unchanged by the transformation.
- If $\lambda = 0$: $\mathbf{v}$ is mapped to the zero vector (it lies in the null space of $\mathbf{A}$).

## Finding Eigenvalues and Eigenvectors

1.  **Characteristic Equation:**
    The defining equation $\mathbf{A}\mathbf{v} = \lambda\mathbf{v}$ can be rewritten as:
    $$ \mathbf{A}\mathbf{v} - \lambda\mathbf{v} = \mathbf{0} $$
    $$ \mathbf{A}\mathbf{v} - \lambda\mathbf{I}\mathbf{v} = \mathbf{0} $$
    $$ (\mathbf{A} - \lambda\mathbf{I})\mathbf{v} = \mathbf{0} $$
    where $\mathbf{I}$ is the identity matrix.
    For a non-zero vector $\mathbf{v}$ to be a solution, the matrix $(\mathbf{A} - \lambda\mathbf{I})$ must be singular (i.e., not invertible). This means its [[Determinant_Matrix|determinant]] must be zero:
    $$ \det(\mathbf{A} - \lambda\mathbf{I}) = 0 $$
    This equation is called the **characteristic equation** (or characteristic polynomial) of matrix $\mathbf{A}$. Solving this equation for $\lambda$ yields the eigenvalues.

2.  **Finding Eigenvectors:**
    Once an eigenvalue $\lambda$ is found, substitute it back into the equation $(\mathbf{A} - \lambda\mathbf{I})\mathbf{v} = \mathbf{0}$. This becomes a system of linear equations for the components of the eigenvector $\mathbf{v}$. Solve this system to find the non-zero vector(s) $\mathbf{v}$.

## Eigendecomposition
If an $n \times n$ matrix $\mathbf{A}$ has $n$ linearly independent eigenvectors $\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n$ with corresponding eigenvalues $\lambda_1, \lambda_2, \dots, \lambda_n$, then $\mathbf{A}$ can be decomposed as:
$$ \mathbf{A} = \mathbf{P} \mathbf{D} \mathbf{P}^{-1} $$
where:
- $\mathbf{P}$ is an $n \times n$ matrix whose columns are the eigenvectors of $\mathbf{A}$: $\mathbf{P} = [\mathbf{v}_1 | \mathbf{v}_2 | \dots | \mathbf{v}_n]$.
- $\mathbf{D}$ is an $n \times n$ diagonal matrix whose diagonal entries are the corresponding eigenvalues:
  $$ \mathbf{D} = \begin{pmatrix} \lambda_1 & 0 & \dots & 0 \\ 0 & \lambda_2 & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & \lambda_n \end{pmatrix} $$
This is known as **eigendecomposition** or **spectral decomposition**. Not all matrices are diagonalizable (i.e., have a full set of linearly independent eigenvectors). Symmetric matrices are always diagonalizable, and their eigenvectors corresponding to distinct eigenvalues are orthogonal.

## Properties
- An $n \times n$ matrix has at most $n$ distinct eigenvalues. Counting multiplicities, it has exactly $n$ eigenvalues (possibly complex).
- The sum of the eigenvalues (trace) is equal to the trace of the matrix (sum of diagonal elements): $\sum \lambda_i = \text{tr}(\mathbf{A})$.
- The product of the eigenvalues is equal to the determinant of the matrix: $\prod \lambda_i = \det(\mathbf{A})$.
- If a matrix is triangular (upper or lower), its eigenvalues are the entries on its main diagonal.
- Symmetric matrices have real eigenvalues and their eigenvectors can be chosen to be orthonormal.

## Applications
- **[[Principal_Component_Analysis_PCA|Principal Component Analysis (PCA)]]:** Eigenvectors of the covariance matrix (or correlation matrix) define the principal components (directions of maximum variance), and eigenvalues indicate the amount of variance along these components.
- **Stability Analysis of Dynamic Systems:** Eigenvalues determine the stability of linear systems (e.g., in control theory, differential equations).
- **Vibrational Analysis:** In physics and engineering, eigenvalues and eigenvectors describe the natural frequencies and modes of vibration of a system.
- **Graph Theory:** Eigenvalues of graph matrices (like adjacency or Laplacian matrices) reveal properties of the graph structure (e.g., connectivity, spectral clustering).
- **Quantum Mechanics:** Eigenvalues represent measurable quantities (observables) and eigenvectors represent the states of the system.
- **Recommendation Systems:** Can be used in some matrix factorization approaches.
- **Understanding Matrix Powers:** If $\mathbf{A} = \mathbf{P} \mathbf{D} \mathbf{P}^{-1}$, then $\mathbf{A}^k = \mathbf{P} \mathbf{D}^k \mathbf{P}^{-1}$, where $\mathbf{D}^k$ is easy to compute (just raise diagonal elements to power $k$).

See also [[Singular_Value_Decomposition|Singular Values]], which are related but more general.

---