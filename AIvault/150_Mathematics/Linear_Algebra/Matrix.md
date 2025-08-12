---
tags:
  - mathematics
  - linear_algebra
  - matrix
  - concept
aliases:
  - Matrices
related:
  - "[[_Linear_Algebra_MOC]]"
  - "[[Vector]]"
  - "[[Row_Vector]]"
  - "[[Column_Vector]]"
  - "[[Matrix_Operations]]"
  - "[[Matrix_Product]]"
  - "[[Transformation_Matrix]]"
  - "[[Determinant_Matrix]]"
  - "[[Matrix_Inversion]]"
  - "[[Eigenvalues_Eigenvectors]]"
worksheet:
  - WS_Math_Foundations_1
date_created: 2025-05-30
---
# Matrix

## Definition
A **matrix** is a rectangular array or table of numbers, symbols, or expressions, arranged in rows and columns. Matrices are fundamental objects in linear algebra and are used to represent linear transformations, systems of linear equations, and data, among other things.

An individual item in a matrix is called an **element** or **entry**.

## Notation and Dimensions
A matrix is typically denoted by a bold uppercase letter, such as $\mathbf{A}$. The dimensions of a matrix are given by the number of rows and the number of columns. An $m \times n$ matrix (read "m by n matrix") has $m$ rows and $n$ columns.

The element in the $i$-th row and $j$-th column of a matrix $\mathbf{A}$ is denoted by $A_{ij}$, $a_{ij}$, or $(\mathbf{A})_{ij}$.

Example of a $2 \times 3$ matrix $\mathbf{A}$:
$$ \mathbf{A} = \begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \end{pmatrix} = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix} $$
Here, $m=2$ (rows) and $n=3$ (columns). For instance, $a_{12} = 2$.

## Key Concepts & Types
[list2card|addClass(ab-col3)]
- **Dimensions (Shape)**
    - The number of rows and columns ($m \times n$).
- **Square Matrix**
    - A matrix where the number of rows equals the number of columns ($m=n$).
- **[[Row_Vector|Row Vector]]**
    - A matrix with only one row ($1 \times n$).
- **[[Column_Vector|Column Vector]]**
    - A matrix with only one column ($m \times 1$).
- **[[Scalar]]**
    - Can be considered a $1 \times 1$ matrix.
- **Main Diagonal (Principal Diagonal)**
    - In a square matrix, the elements $a_{ii}$ from the top-left corner to the bottom-right corner.
- **Identity Matrix ($\mathbf{I}$)**
    - A square matrix with ones on the main diagonal and zeros elsewhere. It acts as the multiplicative identity for [[Matrix_Product|matrix multiplication]].
    $$ \mathbf{I}_3 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} $$
- **Zero Matrix ($\mathbf{0}$)**
    - A matrix where all elements are zero. It acts as the additive identity.
- **[[Transpose_Matrix|Transpose]] ($\mathbf{A}^T$)**
    - A matrix obtained by swapping the rows and columns of $\mathbf{A}$. If $\mathbf{A}$ is $m \times n$, then $\mathbf{A}^T$ is $n \times m$, and $(\mathbf{A}^T)_{ij} = A_{ji}$.
- **Symmetric Matrix**
    - A square matrix that is equal to its transpose ($\mathbf{A} = \mathbf{A}^T$, so $a_{ij} = a_{ji}$).
- **Skew-Symmetric (Antisymmetric) Matrix**
    - A square matrix such that $\mathbf{A} = -\mathbf{A}^T$ (so $a_{ij} = -a_{ji}$, which implies $a_{ii}=0$).
- **Diagonal Matrix**
    - A square matrix where all off-diagonal elements are zero.
- **Upper/Lower Triangular Matrix**
    - A square matrix where all elements below (for upper) or above (for lower) the main diagonal are zero.
- **[[Orthogonal_Matrix|Orthogonal Matrix]]**
    - A square matrix $\mathbf{Q}$ whose transpose is also its inverse: $\mathbf{Q}^T \mathbf{Q} = \mathbf{Q} \mathbf{Q}^T = \mathbf{I}$. Its columns (and rows) form a set of orthonormal vectors.

## Basic Operations
Matrices can be subjected to various operations:
- [[Matrix_Operations|Matrix Addition and Subtraction]] (for matrices of the same dimensions)
- [[Matrix_Operations|Scalar Multiplication]]
- [[Matrix_Product|Matrix Multiplication]] (under specific dimension compatibility rules)
- [[Hadamard_Product|Element-wise Product (Hadamard Product)]]
- [[Matrix_Inversion|Matrix Inversion]] (for invertible square matrices)
- Calculating the [[Determinant_Matrix|Determinant]] (for square matrices)

## Applications in AI/ML
- **Data Representation:** Datasets are commonly represented as matrices, where rows are samples/observations and columns are features.
- **Linear Transformations:** Matrices are used to represent [[Transformation_Matrix|linear transformations]] such as rotation, scaling, and shearing.
- **Systems of Linear Equations:** $A\mathbf{x} = \mathbf{b}$ is a compact way to represent systems of equations.
- **Neural Networks:** Weights and biases in neural network layers are stored as matrices. Forward and backward propagation involve extensive matrix operations.
- **Covariance Matrices:** Used in statistics and ML to describe the relationships between different features.
- **Image Processing:** Images can be represented as matrices of pixel values.
- **Graph Theory:** Adjacency matrices and incidence matrices represent graphs.
- **Dimensionality Reduction:** Techniques like PCA involve matrix decompositions (e.g., [[Eigenvalues_Eigenvectors|eigendecomposition]] of the covariance matrix).

---