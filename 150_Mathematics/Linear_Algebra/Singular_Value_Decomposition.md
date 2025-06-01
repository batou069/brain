---
tags:
  - mathematics
  - linear_algebra
  - matrix
  - svd
  - matrix_decomposition
  - dimensionality_reduction
  - concept
aliases:
  - SVD
  - Matrix SVD
related:
  - "[[Matrix]]"
  - "[[Singular_Values]]"
  - "[[Eigenvalues_Eigenvectors]]"
  - "[[Orthogonal_Matrix]]"
  - "[[Diagonal_Matrix]]"
  - "[[Principal_Component_Analysis_PCA]]"
  - "[[Low_Rank_Matrix_Approximation]]"
worksheet:
  - WS_Math_Foundations_1
date_created: 2025-05-30
---
# Singular Value Decomposition (SVD)

## Definition
The **Singular Value Decomposition (SVD)** is a fundamental factorization of a real or complex [[Matrix|matrix]]. It generalizes the [[Eigenvalues_Eigenvectors|eigendecomposition]] of a square symmetric matrix to any $m \times n$ matrix. The SVD states that any $m \times n$ matrix $\mathbf{A}$ can be factored as:

$$ \mathbf{A} = \mathbf{U} \mathbf{\Sigma} \mathbf{V}^T $$

where:
- **$\mathbf{U}$**: An $m \times m$ [[Orthogonal_Matrix|orthogonal matrix]]. Its columns are the **left-singular vectors** of $\mathbf{A}$. These are the eigenvectors of $\mathbf{A}\mathbf{A}^T$.
- **$\mathbf{\Sigma}$**: An $m \times n$ [[Diagonal_Matrix|rectangular diagonal matrix]]. Its diagonal entries $\Sigma_{ii} = \sigma_i$ are the **[[Singular_Values|singular values]]** of $\mathbf{A}$, arranged in descending order ($\sigma_1 \ge \sigma_2 \ge \dots \ge \sigma_r > 0$, where $r$ is the rank of $\mathbf{A}$). All other entries of $\mathbf{\Sigma}$ are zero.
  If $m > n$, $\mathbf{\Sigma}$ has the form $\begin{pmatrix} \mathbf{D} \\ \mathbf{0} \end{pmatrix}$ where $\mathbf{D}$ is $n \times n$ diagonal.
  If $m < n$, $\mathbf{\Sigma}$ has the form $\begin{pmatrix} \mathbf{D} & \mathbf{0} \end{pmatrix}$ where $\mathbf{D}$ is $m \times m$ diagonal.
  If $m = n$, $\mathbf{\Sigma}$ is an $n \times n$ diagonal matrix.
- **$\mathbf{V}^T$**: An $n \times n$ orthogonal matrix. Its rows are the transposes of the **right-singular vectors** of $\mathbf{A}$ (so $\mathbf{V}$'s columns are the right-singular vectors). These are the eigenvectors of $\mathbf{A}^T\mathbf{A}$.

The singular values $\sigma_i$ are the square roots of the non-zero eigenvalues of both $\mathbf{A}\mathbf{A}^T$ and $\mathbf{A}^T\mathbf{A}$.

## Geometric Interpretation
The SVD provides a geometric understanding of how a linear transformation represented by matrix $\mathbf{A}$ acts on vectors:
1.  **Rotation/Reflection ($\mathbf{V}^T$)**: The input vector space ($\mathbb{R}^n$) is rotated/reflected by $\mathbf{V}^T$ so that the new axes (the columns of $\mathbf{V}$, i.e., right-singular vectors) align with the principal directions of stretching/shrinking.
2.  **Scaling ($\mathbf{\Sigma}$)**: The space is scaled along these new axes by the [[Singular_Values|singular values]] $\sigma_i$. Some dimensions might be scaled to zero if their corresponding singular values are zero (effectively reducing dimensionality).
3.  **Rotation/Reflection ($\mathbf{U}$)**: The scaled space is then rotated/reflected by $\mathbf{U}$ into the output vector space ($\mathbb{R}^m$). The columns of $\mathbf{U}$ (left-singular vectors) form an orthonormal basis for the output space, aligned with the semi-axes of the ellipsoid formed by transforming the unit sphere.

Essentially, any linear transformation can be decomposed into a rotation, a scaling, and another rotation.

## Forms of SVD
[list2tab|#SVD Forms]
- **Full SVD**
    - As defined above, with $\mathbf{U}$ being $m \times m$, $\mathbf{\Sigma}$ being $m \times n$, and $\mathbf{V}$ being $n \times n$.
- **Thin SVD (Reduced SVD)**
    - If $m > n$ (more rows than columns, "tall" matrix):
        - $\mathbf{U}$ is $m \times n$ (contains only the first $n$ columns of the full $\mathbf{U}$).
        - $\mathbf{\Sigma}$ is $n \times n$ (square diagonal matrix of singular values).
        - $\mathbf{V}^T$ is $n \times n$ (same as full SVD).
        - $\mathbf{A} = \mathbf{U}_{m \times n} \mathbf{\Sigma}_{n \times n} \mathbf{V}^T_{n \times n}$
    - If $m < n$ (more columns than rows, "wide" matrix):
        - $\mathbf{U}$ is $m \times m$ (same as full SVD).
        - $\mathbf{\Sigma}$ is $m \times m$ (square diagonal matrix of singular values).
        - $\mathbf{V}^T$ is $m \times n$ (contains only the first $m$ rows of the full $\mathbf{V}^T$, corresponding to the $m$ largest singular values).
        - $\mathbf{A} = \mathbf{U}_{m \times m} \mathbf{\Sigma}_{m \times m} \mathbf{V}^T_{m \times n}$
    - The Thin SVD is often more computationally efficient and provides the essential components for reconstruction and analysis.
- **Truncated SVD**
    - Only the $k$ largest singular values (and corresponding singular vectors) are kept, where $k < r$ (rank of $\mathbf{A}$).
    - $\mathbf{A}_k = \mathbf{U}_k \mathbf{\Sigma}_k \mathbf{V}_k^T$
    - $\mathbf{U}_k$ is $m \times k$, $\mathbf{\Sigma}_k$ is $k \times k$ diagonal, $\mathbf{V}_k^T$ is $k \times n$.
    - This gives the best rank-$k$ approximation of $\mathbf{A}$ in the least-squares sense (Eckart-Young-Mirsky theorem). See [[Low_Rank_Matrix_Approximation]].

## Calculation Example (Conceptual)
Finding the SVD manually is complex. Libraries like NumPy (`numpy.linalg.svd`) are used.
Consider $\mathbf{A} = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$.
1.  Calculate $\mathbf{A}^T\mathbf{A}$:
    $$ \mathbf{A}^T\mathbf{A} = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix} $$
2.  Find eigenvalues of $\mathbf{A}^T\mathbf{A}$:
    $\det(\mathbf{A}^T\mathbf{A} - \lambda\mathbf{I}) = \det \begin{pmatrix} 1-\lambda & 1 \\ 1 & 2-\lambda \end{pmatrix} = (1-\lambda)(2-\lambda) - 1 = \lambda^2 - 3\lambda + 1 = 0$.
    $\lambda = \frac{3 \pm \sqrt{9-4}}{2} = \frac{3 \pm \sqrt{5}}{2}$.
    $\lambda_1 = \frac{3+\sqrt{5}}{2} \approx 2.618$, $\lambda_2 = \frac{3-\sqrt{5}}{2} \approx 0.382$.
3.  Singular values are $\sigma_1 = \sqrt{\lambda_1} \approx 1.618$, $\sigma_2 = \sqrt{\lambda_2} \approx 0.618$.
    So $\mathbf{\Sigma} = \begin{pmatrix} 1.618 & 0 \\ 0 & 0.618 \end{pmatrix}$ (approx).
4.  Find eigenvectors of $\mathbf{A}^T\mathbf{A}$ to get columns of $\mathbf{V}$.
5.  Find eigenvectors of $\mathbf{A}\mathbf{A}^T$ to get columns of $\mathbf{U}$ (or use $\mathbf{u}_i = \frac{1}{\sigma_i}\mathbf{A}\mathbf{v}_i$).

## Applications
[list2card|addClass(ab-col1)|#SVD Applications]
- **[[Low_Rank_Matrix_Approximation|Low-Rank Matrix Approximation]] & Data Compression:**
    - By keeping only the top $k$ singular values and corresponding vectors (Truncated SVD), we get the best rank-$k$ approximation of the original matrix. This is used in image compression (discarding small singular values) and noise reduction.
    - Application: Image compression. An image can be represented as a matrix. SVD allows approximating this matrix with a lower-rank matrix, reducing storage.
- **[[Principal_Component_Analysis_PCA|Principal Component Analysis (PCA)]]:**
    - SVD of the (mean-centered) data matrix is directly related to PCA. The right-singular vectors ($\mathbf{V}$) give the principal component directions, and the singular values are related to the variance explained by each component.
- **Recommendation Systems (Collaborative Filtering):**
    - User-item rating matrices are often large and sparse. SVD can be used to find latent factors and predict missing ratings by approximating the original matrix.
- **Solving Linear Systems and Least Squares Problems:**
    - The pseudoinverse (Moore-Penrose inverse) of a matrix can be computed using SVD: $\mathbf{A}^+ = \mathbf{V} \mathbf{\Sigma}^+ \mathbf{U}^T$, where $\mathbf{\Sigma}^+$ is formed by taking reciprocals of non-zero singular values in $\mathbf{\Sigma}$ and transposing. This is useful for overdetermined or underdetermined systems.
- **Determining Matrix Rank:**
    - The number of non-zero singular values is the rank of the matrix.
- **Numerical Stability and Condition Number:**
    - SVD is numerically stable. The ratio $\sigma_1 / \sigma_r$ (largest to smallest non-zero singular value) is the condition number, indicating sensitivity to errors.
- **Natural Language Processing (NLP):**
    - **Latent Semantic Analysis (LSA) / Latent Semantic Indexing (LSI):** SVD is applied to term-document matrices to uncover latent semantic relationships between terms and documents.
- **Signal Processing:**
    - Noise reduction and feature extraction.
- **Control Theory:**
    - Analyzing system properties.

SVD is a powerful and versatile tool in linear algebra with broad applicability across many scientific and engineering disciplines, especially in data science and machine learning.

---