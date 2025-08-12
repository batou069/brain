---
tags: [mathematics, linear_algebra, matrix, orthogonal_matrix, orthonormal_basis, concept]
aliases: [Orthonormal Matrix] # Technically, columns/rows are orthonormal
related:
  - "[[Matrix]]"
  - "[[Vector]]"
  - "[[Dot_Product]]"
  - "[[p-norm]]" # L2 norm
  - "[[Transpose_Matrix]]"
  - "[[Matrix_Inversion]]"
  - "[[Transformation_Matrix]]" # Represents rotations, reflections
  - "[[Singular_Value_Decomposition]]" # U and V are orthogonal
  - "[[Eigenvalues_Eigenvectors]]" # Eigenvectors of symmetric matrices can form an orthogonal matrix
worksheet: [WS_Math_Foundations_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Orthogonal Matrix

## Definition
A square [[Matrix|matrix]] $\mathbf{Q}$ with real entries is called an **orthogonal matrix** if its columns (and rows) form an orthonormal set of vectors. An orthonormal set consists of vectors that are mutually [[Orthogonal_Vectors|orthogonal]] and each have a unit length (L2 [[p-norm|norm]] of 1).

The defining property of an orthogonal matrix is that its [[Transpose_Matrix|transpose]] is equal to its [[Matrix_Inversion|inverse]]:
$$ \mathbf{Q}^T = \mathbf{Q}^{-1} $$
This leads to the equivalent and more common verification condition:
$$ \mathbf{Q}^T \mathbf{Q} = \mathbf{Q} \mathbf{Q}^T = \mathbf{I} $$
where $\mathbf{I}$ is the identity matrix.

## Properties
[list2tab|#Orthogonal Matrix Properties]
- Inverse
    - The inverse is trivial to compute: $\mathbf{Q}^{-1} = \mathbf{Q}^T$. This is computationally very efficient compared to standard [[Matrix_Inversion|matrix inversion]].
- Determinant
    - The [[Determinant_Matrix|determinant]] of an orthogonal matrix is always $\pm 1$.
    - $\det(\mathbf{Q}) = 1$ corresponds to a **rotation** (a proper orthogonal transformation).
    - $\det(\mathbf{Q}) = -1$ corresponds to a **reflection** or an improper rotation.
- Eigenvalues
    - The [[Eigenvalues_Eigenvectors|eigenvalues]] of an orthogonal matrix all have a complex modulus (absolute value) of 1.
    - In LaTeX: $|\lambda| = 1$ for any eigenvalue $\lambda$.
- Preservation
    - Orthogonal transformations are isometries; they preserve lengths (L2 norms) and angles.
    - **Length Preservation:** $\|\mathbf{Q}\mathbf{x}\|_2 = \|\mathbf{x}\|_2$
    - **Angle/Dot Product Preservation:** $(\mathbf{Q}\mathbf{x}) \cdot (\mathbf{Q}\mathbf{y}) = \mathbf{x} \cdot \mathbf{y}$
- Products
    - The product of two orthogonal matrices is also an orthogonal matrix. If $\mathbf{Q}_1$ and $\mathbf{Q}_2$ are orthogonal, then so is $\mathbf{Q}_1\mathbf{Q}_2$.

## Examples and Python Code
[list2tab|#Examples]
- 2D Rotation
    - A 2D rotation matrix is a classic example of an orthogonal matrix. It rotates vectors counter-clockwise by an angle $\theta$.
    - $$ \mathbf{R}(\theta) = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix} $$
    - Let's create one for $\theta = 45^\circ = \pi/4$ radians.
    - ```python
      import numpy as np
      
      # Define the angle in radians (pi/4 = 45 degrees)
      theta = np.pi / 4
      
      # Create the 2D rotation matrix
      Q_rot = np.array([
          [np.cos(theta), -np.sin(theta)],
          [np.sin(theta),  np.cos(theta)]
      ])
      
      print("2D Rotation Matrix (theta=pi/4):\n", Q_rot)
      
      # Expected Output:
      # 2D Rotation Matrix (theta=pi/4):
      # [[ 0.70710678 -0.70710678]
      #  [ 0.70710678  0.70710678]]
      ```
- Verification
    - We can verify the property $\mathbf{Q}^T \mathbf{Q} = \mathbf{I}$ using Python. Due to floating-point precision, we check if the result is "close" to the identity matrix.
    - ```python
      # Q_rot is from the previous example
      
      # Get the transpose of Q_rot
      Q_rot_T = Q_rot.T
      
      # Multiply the transpose by the original matrix
      # The @ operator is used for matrix multiplication in NumPy
      identity_check = Q_rot_T @ Q_rot
      
      print("Q_T @ Q:\n", identity_check)
      
      # Check if the result is close to the 2x2 identity matrix
      is_orthogonal = np.allclose(identity_check, np.identity(2))
      
      print("\nIs the matrix orthogonal?", is_orthogonal)
      
      # Expected Output:
      # Q_T @ Q:
      # [[1. 0.]
      #  [0. 1.]]
      #
      # Is the matrix orthogonal? True
      ```
- Preservation
    - Let's demonstrate that an orthogonal transformation preserves the L2 norm (length) of a vector.
    - $$ \|\mathbf{Q}\mathbf{x}\|_2 = \|\mathbf{x}\|_2 $$
    - ```python
      # Q_rot is from the first example
      
      # Create a sample vector
      v = np.array()
      
      # Transform the vector using the orthogonal matrix
      w = Q_rot @ v
      
      # Calculate the L2 norm (Euclidean length) of the original and transformed vectors
      norm_v = np.linalg.norm(v)
      norm_w = np.linalg.norm(w)
      
      print("Original vector v:", v)
      print("Transformed vector w:", w)
      print("\nL2 norm of original vector v:", norm_v)
      print("L2 norm of transformed vector w:", norm_w)
      print("Are the norms equal?", np.isclose(norm_v, norm_w))
      
      # Expected Output:
      # Original vector v: [3 1]
      # Transformed vector w: [1.41421356 2.82842712]
      #
      # L2 norm of original vector v: 3.1622776601683795
      # L2 norm of transformed vector w: 3.1622776601683795
      # Are the norms equal? True
      ```

## Applications
- **[[Transformation_Matrix|Geometric Transformations]]:** Representing rotations and reflections in computer graphics, robotics, and physics.
- **[[Singular_Value_Decomposition|Singular Value Decomposition (SVD)]]:** The matrices $\mathbf{U}$ and $\mathbf{V}$ in the decomposition $\mathbf{A} = \mathbf{U} \mathbf{\Sigma} \mathbf{V}^T$ are orthogonal.
- **QR Decomposition:** Any real square matrix $\mathbf{A}$ can be decomposed as $\mathbf{A} = \mathbf{Q}\mathbf{R}$, where $\mathbf{Q}$ is an orthogonal matrix and $\mathbf{R}$ is an upper triangular matrix. This is used in solving linear systems and eigenvalue problems.
- **Change of Basis:** Orthogonal matrices are used to change from one orthonormal basis to another, which simplifies many calculations.
- **[[Principal_Component_Analysis_PCA|Principal Component Analysis (PCA)]]:** The transformation matrix in PCA, which projects data onto principal components, is an orthogonal matrix.
- **Numerical Stability:** Orthogonal transformations are numerically stable because they do not amplify floating-point errors (since they preserve norms). This makes them highly desirable in numerical algorithms.

---