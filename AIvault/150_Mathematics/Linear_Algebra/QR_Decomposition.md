---
tags: [mathematics, linear_algebra, matrix, matrix_decomposition, qr_decomposition, concept]
aliases: [QR Factorization]
related:
  - "[[Matrix]]"
  - "[[Orthogonal_Matrix]]"
  - "[[Upper_Triangular_Matrix]]"
  - "[[Gram_Schmidt_Process]]" # A method to compute QR
  - "[[Linear_Least_Squares]]"
worksheet: [WS_Math_Foundations_2]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# QR Decomposition

## Definition
The **QR decomposition** (or QR factorization) is a decomposition of a [[Matrix|matrix]] $\mathbf{A}$ into a product of an [[Orthogonal_Matrix|orthogonal matrix]] $\mathbf{Q}$ and an [[Upper_Triangular_Matrix|upper triangular matrix]] $\mathbf{R}$.

For any real square matrix $\mathbf{A}$, the decomposition is:
$$ \mathbf{A} = \mathbf{Q}\mathbf{R} $$
For a general $m \times n$ matrix $\mathbf{A}$ with linearly independent columns:
- $\mathbf{Q}$ is an $m \times n$ matrix with orthonormal columns (i.e., $\mathbf{Q}^T\mathbf{Q} = \mathbf{I}_n$).
- $\mathbf{R}$ is an $n \times n$ invertible upper triangular matrix.

The decomposition is unique up to the signs of the diagonal elements of $\mathbf{R}$ and the corresponding columns of $\mathbf{Q}$.

## How it Works (Conceptual)
The QR decomposition can be thought of as the result of applying the [[Gram_Schmidt_Process|Gram-Schmidt process]] to the columns of matrix $\mathbf{A}$.
- The columns of $\mathbf{A}$ form a basis for a vector space.
- The Gram-Schmidt process transforms this basis into an orthonormal basis. The matrix $\mathbf{Q}$ is formed by taking these orthonormal vectors as its columns.
- The matrix $\mathbf{R}$ contains the coefficients that express the original column vectors of $\mathbf{A}$ as linear combinations of the new orthonormal basis vectors in $\mathbf{Q}$. Since the $k$-th original vector only depends on the first $k$ orthonormal vectors, $\mathbf{R}$ is upper triangular.
$$ \mathbf{a}_k = r_{1k}\mathbf{q}_1 + r_{2k}\mathbf{q}_2 + \dots + r_{kk}\mathbf{q}_k $$

## Python Example
The `numpy.linalg.qr` function in NumPy can be used to compute the QR decomposition.

[list2tab|#QR Decomposition in Python]
- Calculation
    - Let's decompose a sample $3 \times 3$ matrix $\mathbf{A}$.
    - ```python
      import numpy as np
      
      # Define a matrix A
      A = np.array([
          [12, -51, 4],
          [6, 167, -68],
          [-4, 24, -41]
      ])
      
      # Perform QR decomposition
      Q, R = np.linalg.qr(A)
      
      print("Original Matrix A:\n", A)
      print("\nOrthogonal Matrix Q:\n", Q)
      print("\nUpper Triangular Matrix R:\n", R)
      
      # Expected Output:
      # Original Matrix A:
      # [[ 12 -51   4]
      #  [  6 167 -68]
      #  [ -4  24 -41]]
      #
      # Orthogonal Matrix Q:
      # [[-0.85714286  0.39428571 -0.33142857]
      #  [-0.42857143 -0.90285714  0.03428571]
      #  [ 0.28571429 -0.17142857 -0.94285714]]
      #
      # Upper Triangular Matrix R:
      # [[-14.   -21.    14.  ]
      #  [  0.  -175.    70.  ]
      #  [  0.     0.    35.  ]]
      ```
- Verification
    - We can verify that $\mathbf{Q}$ is orthogonal ($\mathbf{Q}^T\mathbf{Q} \approx \mathbf{I}$) and that the product $\mathbf{Q}\mathbf{R}$ reconstructs the original matrix $\mathbf{A}$.
    - ```python
      # Q and R are from the previous example
      
      # 1. Verify Q is orthogonal
      # np.allclose is used to handle floating point inaccuracies
      is_Q_orthogonal = np.allclose(Q.T @ Q, np.identity(3))
      print(f"Is Q orthogonal? {is_Q_orthogonal}")
      
      # 2. Verify A = QR
      A_reconstructed = Q @ R
      is_reconstruction_correct = np.allclose(A, A_reconstructed)
      print(f"\nIs A reconstructed correctly from QR? {is_reconstruction_correct}")
      print("\nReconstructed A:\n", A_reconstructed)
      
      # Expected Output:
      # Is Q orthogonal? True
      #
      # Is A reconstructed correctly from QR? True
      #
      # Reconstructed A:
      # [[ 12. -51.   4.]
      #  [  6. 167. -68.]
      #  [ -4.  24. -41.]]
      ```

## Applications
- **Solving [[Linear_Least_Squares|Linear Least Squares]] Problems:**
    - To solve the overdetermined system $\mathbf{A}\mathbf{x} = \mathbf{b}$, we want to minimize $\|\mathbf{A}\mathbf{x} - \mathbf{b}\|_2$.
    - Substituting $\mathbf{A} = \mathbf{Q}\mathbf{R}$, we get $\|\mathbf{Q}\mathbf{R}\mathbf{x} - \mathbf{b}\|_2$. Since $\mathbf{Q}$ is orthogonal, it preserves norms, so this is equivalent to minimizing $\|\mathbf{R}\mathbf{x} - \mathbf{Q}^T\mathbf{b}\|_2$.
    - This transforms the problem into solving the upper triangular system $\mathbf{R}\mathbf{x} = \mathbf{Q}^T\mathbf{b}$, which is easily solved using back substitution. This is a numerically stable method.
- **Eigenvalue Calculation (QR Algorithm):**
    - The QR algorithm is one of the most important methods for computing the [[Eigenvalues_Eigenvectors|eigenvalues]] of a matrix. It iteratively applies QR decomposition to a sequence of matrices that converge to a form from which eigenvalues can be easily read.
- **Finding an Orthonormal Basis:**
    - The columns of $\mathbf{Q}$ provide an orthonormal basis for the column space of $\mathbf{A}$.

QR decomposition is a cornerstone of numerical linear algebra due to its excellent [[Numerical_Stability|numerical stability]] and wide range of applications.

---