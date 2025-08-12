---
tags:
  - mathematics
  - linear_algebra
  - matrix
  - vector
  - element_wise_operations
  - hadamard_product
  - concept
aliases:
  - Element-wise Operations
  - Pointwise Operations
  - Hadamard Product on Matrices/Vectors
related:
  - "[[Matrix]]"
  - "[[Vector]]"
  - "[[Matrix_Operations]]"
  - "[[Hadamard_Product]]"
  - "[[NumPy_Vectorization]]"
worksheet:
  - WS_Math_Foundations_1
date_created: 2025-05-30
---
# Element-wise Matrix/Vector Operations

Element-wise operations (also called pointwise operations) are operations performed between two [[Matrix|matrices]] or two [[Vector|vectors]] of the same dimensions, or between a matrix/vector and a [[Scalar|scalar]], where the operation is applied independently to each corresponding pair of elements (or to each element in the case of scalar operations).

## Operations with a Scalar
If $\mathbf{A}$ is an $m \times n$ matrix and $k$ is a scalar, common element-wise operations include:
- **Scalar Addition/Subtraction:** $\mathbf{B} = \mathbf{A} \pm k$ where $B_{ij} = A_{ij} \pm k$.
- **Scalar Multiplication:** $\mathbf{B} = k\mathbf{A}$ (or $\mathbf{A}k$) where $B_{ij} = k A_{ij}$. (This is a standard [[Matrix_Operations|matrix operation]]).
- **Scalar Division:** $\mathbf{B} = \mathbf{A} / k$ where $B_{ij} = A_{ij} / k$ (for $k \neq 0$).
- **Scalar Exponentiation:** $\mathbf{B} = \mathbf{A}^k$ (element-wise power) where $B_{ij} = (A_{ij})^k$. (Note: This is different from matrix exponentiation $\mathbf{A}^n = \mathbf{A}\mathbf{A}...\mathbf{A}$).
- **Function Application:** Applying a scalar function $f$ to each element: $\mathbf{B} = f(\mathbf{A})$ where $B_{ij} = f(A_{ij})$. Examples include $\log(\mathbf{A})$, $\exp(\mathbf{A})$, $\sin(\mathbf{A})$.

These operations also apply analogously to vectors.

## Operations Between Two Matrices/Vectors (Element-wise)
If $\mathbf{A}$ and $\mathbf{B}$ are matrices (or vectors) of the **same dimensions** ($m \times n$), common element-wise operations include:

- **Element-wise Addition/Subtraction:** $\mathbf{C} = \mathbf{A} \pm \mathbf{B}$ where $C_{ij} = A_{ij} \pm B_{ij}$. (This is standard [[Matrix_Operations|matrix addition/subtraction]]).
- **[[Hadamard_Product|Element-wise Multiplication (Hadamard Product)]]:** $\mathbf{C} = \mathbf{A} \odot \mathbf{B}$ (or $\mathbf{A} * \mathbf{B}$ in some programming contexts like NumPy) where $C_{ij} = A_{ij} B_{ij}$.
    - This is **different** from the standard [[Matrix_Product|matrix product]].
- **Element-wise Division:** $\mathbf{C} = \mathbf{A} \oslash \mathbf{B}$ where $C_{ij} = A_{ij} / B_{ij}$ (assuming $B_{ij} \neq 0$).
- **Element-wise Exponentiation:** $\mathbf{C} = \mathbf{A}^{\odot \mathbf{B}}$ where $C_{ij} = (A_{ij})^{B_{ij}}$.
- **Element-wise Maximum/Minimum:** $\mathbf{C} = \max(\mathbf{A}, \mathbf{B})$ where $C_{ij} = \max(A_{ij}, B_{ij})$.

## Example (Hadamard Product)
Let $\mathbf{A} = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ and $\mathbf{B} = \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}$.
The Hadamard product $\mathbf{A} \odot \mathbf{B}$ is:
$$ \mathbf{A} \odot \mathbf{B} = \begin{pmatrix} 1 \cdot 5 & 2 \cdot 6 \\ 3 \cdot 7 & 4 \cdot 8 \end{pmatrix} = \begin{pmatrix} 5 & 12 \\ 21 & 32 \end{pmatrix} $$

## Element-wise Functions
This term from the prompt "Element-wise functions" specifically refers to applying a mathematical function to each element of a matrix or vector independently.
Examples:
- If $\mathbf{A} = \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix}$
- Then $\sin(\mathbf{A}) = \begin{pmatrix} \sin(a_{11}) & \sin(a_{12}) \\ \sin(a_{21}) & \sin(a_{22}) \end{pmatrix}$
- And $\exp(\mathbf{A}) = \begin{pmatrix} e^{a_{11}} & e^{a_{12}} \\ e^{a_{21}} & e^{a_{22}} \end{pmatrix}$ (This is different from the matrix exponential $e^{\mathbf{A}}$ which involves a power series of matrices).

These are common in numerical computing libraries like [[NumPy]], where universal functions (ufuncs) operate element-wise on arrays. For example, `numpy.exp(array)`, `numpy.log(array)`, `numpy.sin(array)`.

## Applications
- **Image Processing:** Modifying pixel intensities (e.g., brightness adjustment by scalar addition/multiplication, contrast enhancement, applying filters via Hadamard product with a kernel).
- **Neural Networks:**
    - Applying activation functions (like [[Sigmoid_Function|Sigmoid]], [[Rectified_Linear_Unit_ReLU|ReLU]], [[Hyperbolic_Functions|tanh]]) element-wise to the weighted sum of inputs.
    - Element-wise multiplication is used in attention mechanisms, gating mechanisms (like in LSTMs/GRUs).
    - Bias addition is an element-wise operation.
- **Data Preprocessing:** Scaling features, applying transformations like log or exponentiation.
- **Numerical Algorithms:** Many algorithms involve updating arrays or matrices element by element.
- **Broadcasting:** Libraries like NumPy extend element-wise operations to arrays of compatible but not necessarily identical shapes through a mechanism called broadcasting. For example, adding a row vector to each row of a matrix.

>[!note] Notation
>The symbol $\odot$ is standard for the Hadamard product. For other element-wise operations, explicit description or context (like in programming libraries) is often used, as there isn't always a unique mathematical symbol. Python libraries like NumPy use standard operators (`+`, `-`, `*`, `/`, `**`) for element-wise operations on their array objects by default.

---