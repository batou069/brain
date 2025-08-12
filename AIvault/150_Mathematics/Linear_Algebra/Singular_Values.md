---
tags:
  - mathematics
  - linear_algebra
  - matrix
  - singular_values
  - svd
  - concept
aliases:
  - Singular Value
  - Singular Value Decomposition
related:
  - "[[Matrix]]"
  - "[[Eigenvalues_Eigenvectors]]"
  - "[[Singular_Value_Decomposition]]"
  - "[[p-norm]]"
  - "[[Principal_Component_Analysis_PCA]]"
worksheet:
  - WS_Math_Foundations_1
date_created: 2025-05-30
---
# Singular Values

## Definition
**Singular values** are a concept in linear algebra associated with any rectangular (or square) [[Matrix|matrix]], whether real or complex. They are the non-negative square roots of the [[Eigenvalues_Eigenvectors|eigenvalues]] of $\mathbf{A}^T\mathbf{A}$ (or $\mathbf{A}\mathbf{A}^T$). Singular values are a key component of **[[Singular_Value_Decomposition|Singular Value Decomposition (SVD)]]**.

For an $m \times n$ matrix $\mathbf{A}$:
1.  Consider the $n \times n$ matrix $\mathbf{A}^T\mathbf{A}$. This matrix is symmetric and positive semi-definite, so its eigenvalues are real and non-negative.
2.  Let $\lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_n \ge 0$ be the eigenvalues of $\mathbf{A}^T\mathbf{A}$.
3.  The **singular values** of $\mathbf{A}$, denoted $\sigma_i$, are defined as the square roots of these eigenvalues:
    $$ \sigma_i = \sqrt{\lambda_i} $$
    By convention, singular values are ordered in descending order: $\sigma_1 \ge \sigma_2 \ge \dots \ge \sigma_r > 0$, where $r$ is the rank of the matrix $\mathbf{A}$. If $n > r$, the remaining singular values $\sigma_{r+1}, \dots, \sigma_n$ are zero.

Alternatively, singular values can also be defined as the square roots of the eigenvalues of the $m \times m$ matrix $\mathbf{A}\mathbf{A}^T$. The non-zero singular values obtained from $\mathbf{A}^T\mathbf{A}$ and $\mathbf{A}\mathbf{A}^T$ are the same.

## Geometric Interpretation
Singular values represent the "strengths" or "magnitudes" of the principal axes of the linear transformation defined by the matrix $\mathbf{A}$.
If we consider the action of $\mathbf{A}$ on the unit sphere in $\mathbb{R}^n$, it transforms the unit sphere into an ellipsoid (or hyperellipsoid) in $\mathbb{R}^m$. The singular values are the lengths of the semi-axes of this resulting ellipsoid.
- $\sigma_1$ (the largest singular value) is the length of the longest semi-axis.
- $\sigma_2$ is the length of the second longest semi-axis, and so on.

## Relation to Eigenvalues
- For a symmetric positive semi-definite matrix $\mathbf{A}$ (i.e., $\mathbf{A} = \mathbf{A}^T$ and all its eigenvalues are $\ge 0$), its singular values are equal to its eigenvalues.
- For a general square matrix $\mathbf{A}$, its singular values are not the same as its eigenvalues, unless $\mathbf{A}$ is symmetric positive semi-definite. Eigenvalues can be negative or complex, while singular values are always real and non-negative.

## Key Properties
- Singular values are always real and non-negative.
- The number of non-zero singular values of a matrix is equal to its **rank**.
- The largest singular value, $\sigma_1$, is equal to the spectral norm (or L2-norm) of the matrix $\mathbf{A}$: $\|\mathbf{A}\|_2 = \sigma_1$.
- The condition number of a matrix (with respect to L2-norm) can be defined using singular values: $\kappa(\mathbf{A}) = \frac{\sigma_1}{\sigma_r}$ (where $\sigma_r$ is the smallest non-zero singular value). A large condition number indicates an ill-conditioned matrix.

## Singular Value Decomposition (SVD)
Singular values are central to the [[Singular_Value_Decomposition|Singular Value Decomposition (SVD)]] of a matrix $\mathbf{A}$ ($m \times n$):
$$ \mathbf{A} = \mathbf{U} \mathbf{\Sigma} \mathbf{V}^T $$
where:
- $\mathbf{U}$ is an $m \times m$ orthogonal matrix whose columns are the left-singular vectors of $\mathbf{A}$.
- $\mathbf{\Sigma}$ is an $m \times n$ diagonal matrix with the singular values $\sigma_i$ on its diagonal (in descending order). The rest of the entries are zero.
- $\mathbf{V}$ is an $n \times n$ orthogonal matrix whose columns are the right-singular vectors of $\mathbf{A}$ (these are the eigenvectors of $\mathbf{A}^T\mathbf{A}$).

## Applications
Singular values and SVD have numerous applications:
- **Dimensionality Reduction / [[Principal_Component_Analysis_PCA|Principal Component Analysis (PCA)]]:** Singular values indicate the importance of each dimension. Small singular values correspond to dimensions with less variance and can be discarded for dimensionality reduction.
- **Low-Rank Matrix Approximation:** The SVD provides the best low-rank approximation of a matrix (Eckart-Young theorem). This is used in image compression, noise reduction, and recommendation systems.
- **Solving Linear Systems / Least Squares:** SVD can be used to solve linear systems $A\mathbf{x}=\mathbf{b}$ and find least-squares solutions, especially for ill-conditioned or singular matrices (via pseudoinverse).
- **Determining Matrix Rank:** The number of non-zero singular values gives the rank.
- **Numerical Stability:** SVD is a numerically stable decomposition.
- **Recommendation Systems (Collaborative Filtering):** Used in matrix factorization techniques.
- **Natural Language Processing (NLP):** Latent Semantic Analysis (LSA) uses SVD.

The magnitude of singular values provides insight into the "energy" or "importance" of different directions in the data or transformation.

---