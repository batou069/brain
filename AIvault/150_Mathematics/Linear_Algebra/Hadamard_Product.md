---
tags:
  - mathematics
  - linear_algebra
  - matrix
  - vector
  - hadamard_product
  - element_wise_product
  - schur_product
  - concept
aliases:
  - Element-wise Matrix Product
  - Schur Product
  - Pointwise Matrix Product
related:
  - "[[Matrix]]"
  - "[[Vector]]"
  - "[[Element_wise_Matrix_Operations]]"
  - "[[Matrix_Product]]"
worksheet:
  - WS_Math_Foundations_1
date_created: 2025-05-30
---
# Hadamard Product (Element-wise Product)

## Definition
The **Hadamard product** (also known as the **element-wise product**, **Schur product**, or pointwise product) is a binary operation that takes two [[Matrix|matrices]] (or [[Vector|vectors]]) of the **same dimensions** and produces another matrix of the same dimension where each element $(i,j)$ is the product of the elements $(i,j)$ of the original two matrices.

For two $m \times n$ matrices $\mathbf{A}$ and $\mathbf{B}$, their Hadamard product, denoted $\mathbf{A} \odot \mathbf{B}$ (or sometimes $\mathbf{A} * \mathbf{B}$ in programming contexts like NumPy), is an $m \times n$ matrix $\mathbf{C}$ such that:
$$ C_{ij} = (\mathbf{A} \odot \mathbf{B})_{ij} = A_{ij} B_{ij} $$

This operation is distinct from the more common [[Matrix_Product|matrix product]].

## Example
Let $\mathbf{A} = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}$ and $\mathbf{B} = \begin{pmatrix} 7 & 8 & 9 \\ 10 & 11 & 12 \end{pmatrix}$.
Both are $2 \times 3$ matrices. Their Hadamard product $\mathbf{A} \odot \mathbf{B}$ is:
$$
\mathbf{A} \odot \mathbf{B} = \begin{pmatrix}
1 \cdot 7 & 2 \cdot 8 & 3 \cdot 9 \\
4 \cdot 10 & 5 \cdot 11 & 6 \cdot 12
\end{pmatrix}
= \begin{pmatrix}
7 & 16 & 27 \\
40 & 55 & 72
\end{pmatrix}
$$

The same principle applies to vectors of the same dimension.
If $\mathbf{u} = (u_1, u_2, u_3)$ and $\mathbf{v} = (v_1, v_2, v_3)$, then:
$$ \mathbf{u} \odot \mathbf{v} = (u_1 v_1, u_2 v_2, u_3 v_3) $$

## Properties
- **Commutative:** $\mathbf{A} \odot \mathbf{B} = \mathbf{B} \odot \mathbf{A}$
- **Associative:** $(\mathbf{A} \odot \mathbf{B}) \odot \mathbf{C} = \mathbf{A} \odot (\mathbf{B} \odot \mathbf{C})$
- **Distributive over matrix addition:** $\mathbf{A} \odot (\mathbf{B} + \mathbf{C}) = (\mathbf{A} \odot \mathbf{B}) + (\mathbf{A} \odot \mathbf{C})$
- **Identity Element:** If $\mathbf{J}$ is a matrix of all ones (of the same dimensions as $\mathbf{A}$), then $\mathbf{A} \odot \mathbf{J} = \mathbf{A}$. (Note: This is different from the identity matrix for standard matrix multiplication).
- **Zero Element:** If $\mathbf{0}$ is a zero matrix (of the same dimensions as $\mathbf{A}$), then $\mathbf{A} \odot \mathbf{0} = \mathbf{0}$.
- **Relationship with Diagonal Matrices:** If $\mathbf{D}_1$ and $\mathbf{D}_2$ are diagonal matrices, then $\mathbf{D}_1 \mathbf{D}_2 = \mathbf{D}_1 \odot \mathbf{D}_2$.
- **Schur Product Theorem:** The Hadamard product of two positive semi-definite matrices is also positive semi-definite.

## Applications
- **Image Processing:**
    - Applying masks to images (where the mask is a binary matrix of 0s and 1s).
    - Element-wise multiplication for blending or specific filter effects.
- **Machine Learning / Deep Learning:**
    - **Gating Mechanisms:** In Recurrent Neural Networks like LSTMs and GRUs, gates (which are vectors of values between 0 and 1) are often applied using element-wise multiplication to control information flow.
    - **Attention Mechanisms:** Attention scores can be used to element-wise scale or weight feature vectors.
    - **Activation Functions:** While activation functions themselves are applied element-wise, the Hadamard product can be used in more complex layer designs.
    - **Element-wise scaling of features.**
- **Data Analysis:** Applying weights to data points or features.
- **Statistics:** Used in the calculation of certain types of covariance matrices or in operations involving variance components.
- **Signal Processing:** Element-wise multiplication in the frequency domain corresponds to convolution in the time domain, and vice-versa (though this often involves standard multiplication with specific matrix structures like circulant matrices, the element-wise concept is related to how filter responses are applied).

## Contrast with Standard Matrix Product
It's crucial to distinguish the Hadamard product ($\odot$) from the standard [[Matrix_Product|matrix product]] (often denoted by juxtaposition, e.g., $\mathbf{A}\mathbf{B}$).
- **Dimensionality:**
    - Hadamard product: Requires matrices of the *same* dimensions. Result has the *same* dimensions.
    - Matrix product: Requires inner dimensions to match ($m \times n$ and $n \times p$). Result has outer dimensions ($m \times p$).
- **Calculation:**
    - Hadamard product: $C_{ij} = A_{ij} B_{ij}$
    - Matrix product: $C_{ij} = \sum_k A_{ik} B_{kj}$

Numerical libraries like NumPy overload the `*` operator for element-wise multiplication between arrays by default. Standard matrix multiplication in NumPy is done using the `@` operator or `numpy.matmul()`.

---