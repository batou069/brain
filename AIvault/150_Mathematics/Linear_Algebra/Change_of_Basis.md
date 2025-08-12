---
tags:
  - mathematics
  - linear_algebra
  - vector_space
  - basis
  - change_of_basis
  - transformation
  - concept
aliases:
  - Change of Coordinates
  - Basis Transformation
related:
  - "[[Vector]]"
  - "[[Vector_Space]]"
  - "[[Linear_Independence_Basis_Dimension]]"
  - "[[Matrix]]"
  - "[[Matrix_Inversion]]"
  - "[[Orthogonal_Matrix]]"
worksheet:
  - WS_Math_Foundations_2
date_created: 2025-08-07
---
# Change of Basis

## Definition
In linear algebra, a [[Vector|vector]]'s coordinates depend on the chosen [[Linear_Independence_Basis_Dimension|basis]] for the [[Vector_Space|vector space]]. **Change of basis** is the process of finding the coordinates of a vector with respect to a new basis, given its coordinates in the original basis.

Let $V$ be an $n$-dimensional vector space.
- Let $\mathcal{B} = \{\mathbf{b}_1, \mathbf{b}_2, \dots, \mathbf{b}_n\}$ be an "old" basis for $V$.
- Let $\mathcal{C} = \{\mathbf{c}_1, \mathbf{c}_2, \dots, \mathbf{c}_n\}$ be a "new" basis for $V$.

Any vector $\mathbf{x} \in V$ can be uniquely represented as a linear combination of basis vectors from each basis:
$$ \mathbf{x} = x_1\mathbf{b}_1 + x_2\mathbf{b}_2 + \dots + x_n\mathbf{b}_n $$
$$ \mathbf{x} = x'_1\mathbf{c}_1 + x'_2\mathbf{c}_2 + \dots + x'_n\mathbf{c}_n $$
The coordinate vectors are $[\mathbf{x}]_{\mathcal{B}} = \begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix}$ and $[\mathbf{x}]_{\mathcal{C}} = \begin{pmatrix} x'_1 \\ \vdots \\ x'_n \end{pmatrix}$.

The goal is to find a **change-of-basis matrix** $\mathbf{P}$ that relates these two coordinate representations.

## The Change-of-Basis Matrix
The change-of-basis matrix from basis $\mathcal{B}$ to basis $\mathcal{C}$, denoted $\mathbf{P}_{\mathcal{C} \leftarrow \mathcal{B}}$, is the matrix whose columns are the coordinate vectors of the old basis vectors ($\mathbf{b}_i$) expressed in the new basis ($\mathcal{C}$):
$$ \mathbf{P}_{\mathcal{C} \leftarrow \mathcal{B}} = \begin{bmatrix} [\mathbf{b}_1]_{\mathcal{C}} & [\mathbf{b}_2]_{\mathcal{C}} & \dots & [\mathbf{b}_n]_{\mathcal{C}} \end{bmatrix} $$
This matrix transforms coordinates from $\mathcal{B}$ to $\mathcal{C}$:
$$ [\mathbf{x}]_{\mathcal{C}} = \mathbf{P}_{\mathcal{C} \leftarrow \mathcal{B}} [\mathbf{x}]_{\mathcal{B}} $$
The inverse matrix transforms coordinates back from $\mathcal{C}$ to $\mathcal{B}$:
$$ [\mathbf{x}]_{\mathcal{B}} = (\mathbf{P}_{\mathcal{C} \leftarrow \mathcal{B}})^{-1} [\mathbf{x}]_{\mathcal{C}} = \mathbf{P}_{\mathcal{B} \leftarrow \mathcal{C}} [\mathbf{x}]_{\mathcal{C}} $$

## A Simpler Method (Using the Standard Basis)
Often, we work with the standard basis $\mathcal{E} = \{\mathbf{e}_1, \dots, \mathbf{e}_n\}$ (e.g., in $\mathbb{R}^2$, $\mathbf{e}_1 = (1,0)^T, \mathbf{e}_2 = (0,1)^T$).
Let's say we have a basis $\mathcal{B} = \{\mathbf{b}_1, \dots, \mathbf{b}_n\}$ where the vectors $\mathbf{b}_i$ are given in standard coordinates. The matrix $\mathbf{P}_{\mathcal{B}}$ whose columns are these vectors transforms coordinates from the $\mathcal{B}$-basis to the standard basis $\mathcal{E}$:
$$ [\mathbf{x}]_{\mathcal{E}} = \mathbf{P}_{\mathcal{B}} [\mathbf{x}]_{\mathcal{B}} \quad \text{where} \quad \mathbf{P}_{\mathcal{B}} = \begin{bmatrix} \mathbf{b}_1 & \mathbf{b}_2 & \dots & \mathbf{b}_n \end{bmatrix} $$
To go from standard coordinates to $\mathcal{B}$-coordinates, we use the inverse:
$$ [\mathbf{x}]_{\mathcal{B}} = (\mathbf{P}_{\mathcal{B}})^{-1} [\mathbf{x}]_{\mathcal{E}} $$

## Python Example
Let's work in $\mathbb{R}^2$.
- Standard basis $\mathcal{E} = \{\begin{pmatrix} 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \end{pmatrix}\}$.
- A new basis $\mathcal{B} = \{\mathbf{b}_1, \mathbf{b}_2\} = \{\begin{pmatrix} 2 \\ 1 \end{pmatrix}, \begin{pmatrix} -1 \\ 1 \end{pmatrix}\}$.
- A vector $\mathbf{v}$ has standard coordinates $[\mathbf{v}]_{\mathcal{E}} = \begin{pmatrix} 4 \\ 5 \end{pmatrix}$.
- We want to find its coordinates $[\mathbf{v}]_{\mathcal{B}}$ in the basis $\mathcal{B}$.

[list2tab|#Change of Basis in Python]
- Calculation
    - We need to solve $\mathbf{v} = x_1\mathbf{b}_1 + x_2\mathbf{b}_2$, which is the system $\mathbf{P}_{\mathcal{B}}[\mathbf{v}]_{\mathcal{B}} = [\mathbf{v}]_{\mathcal{E}}$.
    - The solution is $[\mathbf{v}]_{\mathcal{B}} = (\mathbf{P}_{\mathcal{B}})^{-1} [\mathbf{v}]_{\mathcal{E}}$.
    - ```python
      import numpy as np
      
      # Define the basis vectors of B as columns of a matrix P_B
      P_B = np.array([
          [2, -1],
          [1,  1]
      ])
      
      # Define the vector v in standard coordinates
      v_E = np.array()
      
      # To find the coordinates in basis B, we need the inverse of P_B
      P_B_inv = np.linalg.inv(P_B)
      
      # Calculate the coordinates of v in basis B
      v_B = P_B_inv @ v_E
      
      print("Change of basis matrix P_B (B -> E):\n", P_B)
      print("\nInverse matrix P_B_inv (E -> B):\n", P_B_inv)
      print("\nVector v in standard coordinates (E):", v_E)
      print("Vector v in basis B coordinates:", v_B)
      
      # Expected Output:
      # Change of basis matrix P_B (B -> E):
      # [[ 2 -1]
      #  [ 1  1]]
      #
      # Inverse matrix P_B_inv (E -> B):
      # [[ 0.33333333  0.33333333]
      #  [-0.33333333  0.66666667]]
      #
      # Vector v in standard coordinates (E): [4 5]
      # Vector v in basis B coordinates: [3. 1.]
      ```
- Verification
    - We can verify that $3\mathbf{b}_1 + 1\mathbf{b}_2$ gives us back the original vector $\mathbf{v}$ in standard coordinates.
    - $$ [\mathbf{v}]_{\mathcal{E}} = \mathbf{P}_{\mathcal{B}} [\mathbf{v}]_{\mathcal{B}} $$
    - ```python
      # P_B and v_B are from the previous example
      b1 = P_B[:, 0] # First column
      b2 = P_B[:, 1] # Second column
      
      # Reconstruct v in standard coordinates from its B-coordinates
      v_reconstructed_E = v_B * b1 + v_B * b2
      
      # Alternatively, using matrix multiplication
      v_reconstructed_E_mat = P_B @ v_B
      
      print("Coordinates in B:", v_B)
      print("Reconstructed vector in E (manual):", v_reconstructed_E)
      print("Reconstructed vector in E (matrix):", v_reconstructed_E_mat)
      
      # Expected Output:
      # Coordinates in B: [3. 1.]
      # Reconstructed vector in E (manual): [4. 5.]
      # Reconstructed vector in E (matrix): [4. 5.]
      ```

## Orthonormal Bases
If the new basis $\mathcal{B}$ is an orthonormal basis, then the change-of-basis matrix $\mathbf{P}_{\mathcal{B}}$ is an [[Orthogonal_Matrix|orthogonal matrix]]. In this case, its inverse is simply its transpose: $(\mathbf{P}_{\mathcal{B}})^{-1} = (\mathbf{P}_{\mathcal{B}})^T$. This makes changing to and from an orthonormal basis computationally very efficient.

## Applications
- **[[Principal_Component_Analysis_PCA|Principal Component Analysis (PCA)]]:** PCA finds a new orthonormal basis (the principal components) for the data that aligns with the directions of maximum variance. The data is then projected onto this new basis, which is a change of basis operation.
- **Computer Graphics:** Objects are often defined in their own local coordinate system (model space). To place them in a scene (world space) and view them from a camera (view space), a series of change-of-basis transformations are applied.
- **Diagonalization:** In [[Eigenvalues_Eigenvectors|eigendecomposition]], a matrix $\mathbf{A}$ is diagonalized by changing to a basis of its eigenvectors. In this new basis, the transformation $\mathbf{A}$ acts simply by scaling along the basis vectors.
- **Signal Processing:** The Fourier transform can be viewed as a change of basis from the time domain to the frequency domain, where the basis vectors are sinusoids.

---