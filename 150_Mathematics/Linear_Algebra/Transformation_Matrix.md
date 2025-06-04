---
tags:
  - mathematics
  - linear_algebra
  - matrix
  - transformation
  - linear_transformation
  - geometry
  - concept
aliases:
  - Linear Transformation Matrix
  - Geometric Transformation Matrix
related:
  - "[[Matrix]]"
  - "[[Vector]]"
  - "[[Column_Vector]]"
  - "[[Matrix_Product]]"
  - "[[Eigenvalues_Eigenvectors]]"
  - "[[Matrix_Transformations_and_Distance]]"
worksheet:
  - WS_Math_Foundations_1
date_created: 2025-05-30
---
# Transformation Matrix

## Definition
A **transformation matrix** is a [[Matrix|matrix]] whose [[Matrix_Product|product]] with a [[Vector|vector]] (typically a [[Column_Vector|column vector]] representing coordinates) results in a new vector representing the transformed coordinates. Matrices are a fundamental tool for representing and performing linear transformations in geometry and linear algebra.

A linear transformation $T: \mathbb{R}^n \to \mathbb{R}^m$ is a function that maps vectors from an $n$-dimensional space to an $m$-dimensional space and satisfies two properties:
1.  $T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})$ (additivity)
2.  $T(c\mathbf{u}) = cT(\mathbf{u})$ (homogeneity of degree 1), for any scalar $c$.

Any such linear transformation can be represented by an $m \times n$ matrix $\mathbf{A}$, such that $T(\mathbf{x}) = \mathbf{A}\mathbf{x}$. The columns of the matrix $\mathbf{A}$ are the images of the standard basis vectors under the transformation $T$.

## Common 2D Linear Transformations
Let $\mathbf{x} = \begin{pmatrix} x \\ y \end{pmatrix}$ be a 2D column vector.

[list2tab|#2D Transformations]
- Scaling
    - Scales coordinates by factors $s_x$ along the x-axis and $s_y$ along the y-axis.
    - Matrix: $\mathbf{S} = \begin{pmatrix} s_x & 0 \\ 0 & s_y \end{pmatrix}$
    - Transformed vector: $\mathbf{x}' = \mathbf{S}\mathbf{x} = \begin{pmatrix} s_x x \\ s_y y \end{pmatrix}$
- Rotation
    - Rotates points by an angle $\theta$ *counter-clockwise*  around the origin.
    - Matrix: $\mathbf{R} = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix}$
    - Transformed vector: $\mathbf{x}' = \mathbf{R}\mathbf{x}$
- Shearing
    - Slants the shape of an object.
    - Shear parallel to x-axis by factor $k$: $\mathbf{H}_x = \begin{pmatrix} 1 & k \\ 0 & 1 \end{pmatrix}$
      $\mathbf{x}' = \mathbf{H}_x\mathbf{x} = \begin{pmatrix} x + ky \\ y \end{pmatrix}$
    - Shear parallel to y-axis by factor $m$: $\mathbf{H}_y = \begin{pmatrix} 1 & 0 \\ m & 1 \end{pmatrix}$
      $\mathbf{x}' = \mathbf{H}_y\mathbf{x} = \begin{pmatrix} x \\ mx + y \end{pmatrix}$
- Reflection
    - Reflection across x-axis: $\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$
    - Reflection across y-axis: $\begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix}$
    - Reflection across origin: $\begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}$ (equivalent to rotation by $180^\circ$)
    - Reflection across line $y=x$: $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$

## Homogeneous Coordinates for Affine Transformations
Linear transformations (like scaling, rotation, shear) always map the origin to the origin. To represent **affine transformations**, which include translations (shifting the origin), **homogeneous coordinates** are used.

In 2D, a point $(x, y)$ is represented as $(x, y, 1)$ in homogeneous coordinates. 2D affine transformations can then be represented by $3 \times 3$ matrices.
For example, translation by $(t_x, t_y)$:
$$ \mathbf{T} = \begin{pmatrix} 1 & 0 & t_x \\ 0 & 1 & t_y \\ 0 & 0 & 1 \end{pmatrix} $$
Then $\mathbf{x}'_{homo} = \mathbf{T}\mathbf{x}_{homo}$:
$$ \begin{pmatrix} x' \\ y' \\ 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 & t_x \\ 0 & 1 & t_y \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} x \\ y \\ 1 \end{pmatrix} = \begin{pmatrix} x + t_x \\ y + t_y \\ 1 \end{pmatrix} $$
The transformed Cartesian coordinates are $(x+t_x, y+t_y)$.

## Composition of Transformations
Multiple transformations can be combined by multiplying their respective matrices. If transformation $T_1$ is represented by matrix $\mathbf{M}_1$ and $T_2$ by $\mathbf{M}_2$, applying $T_1$ then $T_2$ to a vector $\mathbf{x}$ is:
$$ \mathbf{x}' = \mathbf{M}_2 (\mathbf{M}_1 \mathbf{x}) = (\mathbf{M}_2 \mathbf{M}_1) \mathbf{x} $$
The combined transformation is represented by the matrix product $\mathbf{M}_{\text{combined}} = \mathbf{M}_2 \mathbf{M}_1$.
>[!warning] Order Matters
>Matrix multiplication is generally not commutative, so the order of applying transformations (and thus multiplying matrices) is crucial. $\mathbf{M}_2 \mathbf{M}_1$ is usually different from $\mathbf{M}_1 \mathbf{M}_2$.

## 3D Transformations
Similar concepts apply to 3D transformations, using $3 \times 3$ matrices for linear transformations and $4 \times 4$ matrices with homogeneous coordinates for affine transformations.

## Applications
- **Computer Graphics:** Fundamental for rendering 2D and 3D scenes, animating objects, and camera movements.
- **Robotics:** Describing the position and orientation of robot parts and manipulating them.
- **Computer Vision:** Image warping, alignment, and geometric corrections.
- **Data Augmentation in ML:** Applying geometric transformations (rotation, scaling, shearing) to training images to increase dataset size and improve model robustness.
- **Physics and Engineering:** Describing changes in coordinate systems or physical states.

## Effect on Distances
See [[Matrix_Transformations_and_Distance]] for how matrix transformations affect distances between points.

---