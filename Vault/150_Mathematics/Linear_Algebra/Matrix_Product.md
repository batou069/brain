---
tags:
  - mathematics
  - linear_algebra
  - matrix
  - matrix_multiplication
  - concept
aliases:
  - Matrix Multiplication
  - Product of Matrices
related:
  - "[[Matrix]]"
  - "[[Row_Vector]]"
  - "[[Column_Vector]]"
  - "[[Dot_Product]]"
  - "[[Matrix_Operations]]"
  - "[[Transformation_Matrix]]"
  - "[[Matrix_Multiplication_Associativity]]"
  - "[[Matrix_Multiplication_Complexity]]"
worksheet:
  - WS_Math_Foundations_1
date_created: 2025-05-30
---
# Matrix Product (Matrix Multiplication)

## Definition
The **matrix product**, or **matrix multiplication**, is a binary operation that produces a [[Matrix|matrix]] from two matrices. For matrix multiplication to be defined, the number of columns in the first matrix must be equal to the number of rows in the second matrix.

If $\mathbf{A}$ is an $m \times n$ matrix and $\mathbf{B}$ is an $n \times p$ matrix, their product $\mathbf{C} = \mathbf{A}\mathbf{B}$ is an $m \times p$ matrix. The element $C_{ij}$ (in the $i$-th row and $j$-th column of $\mathbf{C}$) is calculated by taking the [[Dot_Product|dot product]] of the $i$-th [[Row_Vector|row vector]] of $\mathbf{A}$ with the $j$-th [[Column_Vector|column vector]] of $\mathbf{B}$.

$$ C_{ij} = (\mathbf{A}\mathbf{B})_{ij} = \sum_{k=1}^{n} A_{ik} B_{kj} $$
This means:
$$ C_{ij} = A_{i1}B_{1j} + A_{i2}B_{2j} + \dots + A_{in}B_{nj} $$

## Dimension Compatibility
- To multiply $\mathbf{A}$ by $\mathbf{B}$ (i.e., $\mathbf{A}\mathbf{B}$):
    - Number of columns in $\mathbf{A}$ must equal number of rows in $\mathbf{B}$.
    - If $\mathbf{A}$ is $m \times \mathbf{n}$ and $\mathbf{B}$ is $\mathbf{n} \times p$, then $\mathbf{A}\mathbf{B}$ is $m \times p$.
    - Schematically: $(m \times \underline{n}) \cdot (\underline{n} \times p) \rightarrow (m \times p)$. The "inner" dimensions must match.

## Example
Let $\mathbf{A} = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ (a $2 \times 2$ matrix) and $\mathbf{B} = \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}$ (a $2 \times 2$ matrix).
Then $\mathbf{C} = \mathbf{A}\mathbf{B}$ is a $2 \times 2$ matrix:
$$
\begin{aligned}
C_{11} &= (1 \cdot 5) + (2 \cdot 7) = 5 + 14 = 19 \\
C_{12} &= (1 \cdot 6) + (2 \cdot 8) = 6 + 16 = 22 \\
C_{21} &= (3 \cdot 5) + (4 \cdot 7) = 15 + 28 = 43 \\
C_{22} &= (3 \cdot 6) + (4 \cdot 8) = 18 + 32 = 50
\end{aligned}
$$
So, $\mathbf{C} = \begin{pmatrix} 19 & 22 \\ 43 & 50 \end{pmatrix}$.

Let $\mathbf{D} = \begin{pmatrix} 1 & 0 & 2 \\ -1 & 3 & 1 \end{pmatrix}$ ($2 \times 3$) and $\mathbf{E} = \begin{pmatrix} 3 & 1 \\ 2 & 1 \\ 1 & 0 \end{pmatrix}$ ($3 \times 2$).
Then $\mathbf{F} = \mathbf{D}\mathbf{E}$ is a $2 \times 2$ matrix.
$$
\begin{aligned}
F_{11} &= (1 \cdot 3) + (0 \cdot 2) + (2 \cdot 1) = 3 + 0 + 2 = 5 \\
F_{12} &= (1 \cdot 1) + (0 \cdot 1) + (2 \cdot 0) = 1 + 0 + 0 = 1 \\
F_{21} &= (-1 \cdot 3) + (3 \cdot 2) + (1 \cdot 1) = -3 + 6 + 1 = 4 \\
F_{22} &= (-1 \cdot 1) + (3 \cdot 1) + (1 \cdot 0) = -1 + 3 + 0 = 2
\end{aligned}
$$
So, $\mathbf{F} = \begin{pmatrix} 5 & 1 \\ 4 & 2 \end{pmatrix}$.

## Properties
[list2table|#Matrix Product Properties]
- Not Commutative (Generally): 
	- $\mathbf{A}\mathbf{B} \neq \mathbf{B}\mathbf{A}$ in most cases.
    Even if both products are defined, they might have different dimensions or different values.
- Associative: 
	- $(\mathbf{A}\mathbf{B})\mathbf{C} = \mathbf{A}(\mathbf{B}\mathbf{C})$. 
	This property is crucial for [[Matrix_Multiplication_Associativity|optimizing the order of multiplications]].
- Distributive over Matrix Addition:
    - $\mathbf{A}(\mathbf{B} + \mathbf{C}) = \mathbf{A}\mathbf{B} + \mathbf{A}\mathbf{C}$ (left distributivity)
    - $(\mathbf{A} + \mathbf{B})\mathbf{C} = \mathbf{A}\mathbf{C} + \mathbf{B}\mathbf{C}$ (right distributivity)
- Scalar Multiplication: 
	- $k(\mathbf{A}\mathbf{B}) = (k\mathbf{A})\mathbf{B} = \mathbf{A}(k\mathbf{B})$, where $k$ is a scalar.
- Identity Element: 
	- If $\mathbf{I}$ is the identity matrix of appropriate size, then
	$\mathbf{A}\mathbf{I} = \mathbf{A}$ and $\mathbf{I}\mathbf{A} = \mathbf{A}$.
- Transpose of a Product: 
	- $(\mathbf{A}\mathbf{B})^T = \mathbf{B}^T \mathbf{A}^T$
	The order is reversed.

## Applications
- **Representing Linear Transformations:** If a vector $\mathbf{x}$ is transformed by a linear map represented by matrix $\mathbf{B}$, and then the result is transformed by another linear map represented by matrix $\mathbf{A}$, the combined transformation is represented by the matrix product $\mathbf{A}\mathbf{B}$. The transformed vector is $(\mathbf{A}\mathbf{B})\mathbf{x} = \mathbf{A}(\mathbf{B}\mathbf{x})$. (See [[Transformation_Matrix]])
- **Solving Systems of Linear Equations:** Used in various algorithms.
- **Neural Networks:** Core operation in calculating weighted sums in layers.
- **Graph Theory:** Powers of an adjacency matrix can give information about paths of certain lengths.
- **Computer Graphics:** Used extensively for transformations (rotation, scaling, translation via homogeneous coordinates).

## Computational Complexity
See [[Matrix_Multiplication_Complexity]].

---