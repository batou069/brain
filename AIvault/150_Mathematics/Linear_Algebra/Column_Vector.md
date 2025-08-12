---
tags:
  - mathematics
  - linear_algebra
  - vector
  - column_vector
  - matrix
  - concept
aliases:
  - Column Vectors
related:
  - "[[Vector]]"
  - "[[Row_Vector]]"
  - "[[Matrix]]"
  - "[[Vector_Operations]]"
worksheet:
  - WS_Math_Foundations_1
date_created: 2025-05-30
---
# Column Vector

## Definition
A **column vector** is a [[Vector|vector]] whose components are arranged in a single column. If a column vector has $n$ components, it can be considered as an $n \times 1$ [[Matrix|matrix]] (a matrix with $n$ rows and 1 column).

## Representation
A column vector $\mathbf{c}$ with $n$ components $c_1, c_2, \dots, c_n$ is typically written as:
$$ \mathbf{c} = \begin{pmatrix} c_1 \\ c_2 \\ \vdots \\ c_n \end{pmatrix} $$
or sometimes as $\mathbf{c} = [c_1, c_2, \dots, c_n]^T$, where the $T$ denotes the [[Transpose_Matrix|transpose]], indicating it's the transpose of a [[Row_Vector|row vector]] representation.

## Relationship to Row Vectors
A column vector can be obtained by taking the [[Transpose_Matrix|transpose]] of a [[Row_Vector|row vector]], and vice versa.
If $\mathbf{r}$ is a row vector:
$$ \mathbf{r} = \begin{bmatrix} r_1 & r_2 & \dots & r_n \end{bmatrix} $$
Then its transpose, $\mathbf{r}^T$, is a column vector:
$$ \mathbf{r}^T = \begin{pmatrix} r_1 \\ r_2 \\ \vdots \\ r_n \end{pmatrix} $$

## Operations
Column vectors follow the rules of [[Vector_Operations|vector operations]] and [[Matrix_Operations|matrix operations]].
- **Addition:** Two column vectors of the same dimension can be added component-wise.
- **Scalar Multiplication:** A column vector can be multiplied by a [[Scalar|scalar]], which multiplies each component.
- **Matrix Multiplication:**
    - An $m \times n$ matrix can be pre-multiplied by a column vector of dimension $n \times 1$ (by first transposing the column vector to a $1 \times n$ row vector if standard matrix multiplication rules are strictly followed for $A \mathbf{x}$, or more directly, an $m \times n$ matrix $A$ times an $n \times 1$ column vector $\mathbf{x}$ results in an $m \times 1$ column vector $A\mathbf{x}$).
    - A common operation is $A\mathbf{x}$, where $A$ is an $m \times n$ matrix and $\mathbf{x}$ is an $n \times 1$ column vector. The result is an $m \times 1$ column vector. This represents the application of a linear transformation $A$ to the vector $\mathbf{x}$.
    - The [[Dot_Product|dot product]] of two vectors $\mathbf{u}$ and $\mathbf{v}$ (of the same dimension $n$) can be expressed as the matrix product of $\mathbf{u}^T$ (a $1 \times n$ row vector) and $\mathbf{v}$ (an $n \times 1$ column vector): $\mathbf{u} \cdot \mathbf{v} = \mathbf{u}^T \mathbf{v}$.

## Usage
- **Default Vector Representation:** In many mathematical and physics texts, column vectors are often the default or standard representation for vectors.
- **Linear Transformations:** When a [[Matrix|matrix]] $A$ represents a linear transformation, it acts on column vectors $\mathbf{x}$ to produce transformed column vectors $A\mathbf{x}$.
- **Systems of Linear Equations:** A system of linear equations $A\mathbf{x} = \mathbf{b}$ typically involves $\mathbf{x}$ and $\mathbf{b}$ as column vectors.
- **Coordinates:** Points in space can be represented by column vectors (position vectors).
- **Gradients:** The [[Gradient|gradient]] of a scalar-valued function is typically represented as a column vector.

>[!note] Convention
>Column vectors are a very common convention in linear algebra, particularly when discussing matrix transformations $A\mathbf{x}$. While [[Row_Vector|row vectors]] are also used (especially in data representation), understanding operations with column vectors is crucial for much of the theory.

---