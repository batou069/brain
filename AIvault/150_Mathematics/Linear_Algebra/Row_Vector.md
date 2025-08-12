---
tags:
  - mathematics
  - linear_algebra
  - vector
  - row_vector
  - matrix
  - concept
aliases:
  - Row Vectors
related:
  - "[[Vector]]"
  - "[[Column_Vector]]"
  - "[[Matrix]]"
  - "[[Vector_Operations]]"
worksheet:
  - WS_Math_Foundations_1
date_created: 2025-05-30
---
# Row Vector

## Definition
A **row vector** is a [[Vector|vector]] whose components are arranged in a single row. If a row vector has $n$ components, it can be considered as a $1 \times n$ [[Matrix|matrix]] (a matrix with 1 row and $n$ columns).

## Representation
A row vector $\mathbf{r}$ with $n$ components $r_1, r_2, \dots, r_n$ is typically written as:
$$ \mathbf{r} = \begin{bmatrix} r_1 & r_2 & \dots & r_n \end{bmatrix} $$
or sometimes using parentheses or commas:
$$ \mathbf{r} = (r_1, r_2, \dots, r_n) $$
The latter notation can sometimes be ambiguous as it's also used for points or general coordinate vectors, but in the context of matrix operations, the $1 \times n$ matrix interpretation is key.

## Relationship to Column Vectors
A row vector can be obtained by taking the [[Transpose_Matrix|transpose]] of a [[Column_Vector|column vector]], and vice versa.
If $\mathbf{c}$ is a column vector:
$$ \mathbf{c} = \begin{pmatrix} c_1 \\ c_2 \\ \vdots \\ c_n \end{pmatrix} $$
Then its transpose, $\mathbf{c}^T$, is a row vector:
$$ \mathbf{c}^T = \begin{bmatrix} c_1 & c_2 & \dots & c_n \end{bmatrix} $$

## Operations
Row vectors follow the rules of [[Vector_Operations|vector operations]] and [[Matrix_Operations|matrix operations]].
- **Addition:** Two row vectors of the same dimension can be added component-wise.
- **Scalar Multiplication:** A row vector can be multiplied by a [[Scalar|scalar]], which multiplies each component.
- **Matrix Multiplication:**
    - A $1 \times m$ row vector can be post-multiplied by an $m \times n$ matrix to produce a $1 \times n$ row vector.
    - The [[Dot_Product|dot product]] of two vectors $\mathbf{u}$ and $\mathbf{v}$ (of the same dimension $n$) can be expressed as the matrix product of $\mathbf{u}$ (as a $1 \times n$ row vector) and $\mathbf{v}$ (as an $n \times 1$ column vector): $\mathbf{u} \cdot \mathbf{v} = \mathbf{u} \mathbf{v}_{\text{col}}$.

## Usage
- **Representing Linear Functionals:** Row vectors can represent linear functionals, which are linear maps from a vector space to its field of scalars.
- **Coefficients in Linear Equations:** In a system of linear equations, the coefficients of a single equation can form a row vector.
- **Data Representation:** In some contexts, data points (samples) in a dataset are represented as row vectors, where each column in the larger data matrix corresponds to a feature. This is a common convention in many data science libraries like Pandas and Scikit-learn.

>[!note] Convention
>While both row and column vectors are fundamental, in many mathematical texts and theoretical discussions (especially in physics and some areas of linear algebra), [[Column_Vector|column vectors]] are often the default representation for vectors. However, [[Row_Vector|row vectors]] are prevalent in data representation in software. It's important to be aware of the convention being used in any given context.

---