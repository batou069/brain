Filename: 150_Mathematics/_Mathematics_MOC.md
````markdown
[[_Mathematics_MOC]]
````

Filename: 150_Mathematics/Calculus/_Calculus_MOC.md
````markdown
[[_Calculus_MOC]]
````

Filename: 150_Mathematics/Linear_Algebra/_Linear_Algebra_MOC.md
````markdown
[[_Linear_Algebra_MOC]]
````

Filename: 150_Mathematics/Functions/_Functions_MOC.md
````markdown
[[_Functions_MOC]]
````

Now, let's start with the Calculus topics.

Filename: 150_Mathematics/Calculus/Calculus_Derivatives.md
````markdown
[[Calculus_Derivatives]]
````

Filename: 150_Mathematics/Calculus/Calculus_Integrals
````markdown
[[Calculus_Integrals]]
````

Filename: 150_Mathematics/Calculus/Calculus_Optimization
````markdown
[[Calculus_Optimization]]
````

Next, the core Linear Algebra concepts.


Filename: 150_Mathematics/Linear_Algebra/Vector.md
````markdown
[[Vector]]
````

Filename: 150_Mathematics/Linear_Algebra/Row_Vector.md
````markdown
[[150_Mathematics/Linear_Algebra/Row_Vector]]
````

Filename: 150_Mathematics/Linear_Algebra/Column_Vector.md
````markdown
[[150_Mathematics/Linear_Algebra/Column_Vector]]
````

Filename: 150_Mathematics/Linear_Algebra/Dot_Product.md
````markdown
[[150_Mathematics/Linear_Algebra/Dot_Product]]
````

Filename: 150_Mathematics/Linear_Algebra/Cosine_Similarity.md
````markdown
[[Cosine_Similarity]]
````


Filename: 150_Mathematics/Linear_Algebra/Matrix.md
````markdown
[[Matrix]]
````

Filename: 150_Mathematics/Linear_Algebra/Matrix_Product.md
````markdown
[[Matrix_Product]]
````

Filename: 150_Mathematics/Linear_Algebra/Transformation_Matrix.md
````markdown
[[Transformation_Matrix]]
````

Filename: 150_Mathematics/Linear_Algebra/Element_wise_Matrix_Operations.md
````markdown
[[Element_wise_Matrix_Operations]]
````

Filename: 150_Mathematics/Linear_Algebra/Eigenvalues_Eigenvectors.md
````markdown
[[Eigenvalues_Eigenvectors]]
````

Filename: 150_Mathematics/Linear_Algebra/Singular_Values.md
````markdown
[[Singular_Values]]
````

Filename: 150_Mathematics/Linear_Algebra/p-norm.md
````markdown
---
tags: [mathematics, linear_algebra, vector, norm, p_norm, L1_norm, L2_norm, manhattan_distance, euclidean_distance, concept]
aliases: [Vector Norm, Lp Norm, L1 Norm, L2 Norm, L-infinity Norm, Manhattan Norm, Euclidean Norm, Max Norm]
related:
  - "[[Vector]]"
  - "[[Dot_Product]]" # L2 norm is related
  - "[[Distance_Metrics]]"
worksheet: [WS_Math_Foundations_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# p-norm (Vector Norms)

## Definition
In linear algebra, a **norm** is a function that assigns a strictly positive length or size to each [[Vector|vector]] in a vector space—except for the zero vector, which is assigned a length of zero. A norm on a vector space $V$ is a function $\| \cdot \|: V \to \mathbb{R}$ that satisfies the following properties for all scalars $k$ and all vectors $\mathbf{u}, \mathbf{v} \in V$:
1.  $\|\mathbf{v}\| \ge 0$ (Non-negativity)
2.  $\|\mathbf{v}\| = 0$ if and only if $\mathbf{v} = \mathbf{0}$ (zero vector) (Definiteness)
3.  $\|k\mathbf{v}\| = |k| \|\mathbf{v}\|$ (Absolute homogeneity or Absolute scalability)
4.  $\|\mathbf{u} + \mathbf{v}\| \le \|\mathbf{u}\| + \|\mathbf{v}\|$ (Triangle inequality or Subadditivity)

The **$L_p$-norm** (or **p-norm**) of a vector $\mathbf{x} = (x_1, x_2, \dots, x_n)$ is a specific class of vector norms defined as:
$$ \|\mathbf{x}\|_p = \left( \sum_{i=1}^{n} |x_i|^p \right)^{1/p} $$
for a real number $p \ge 1$.

## Common p-norms

>[!question] What are the common names for the 1-norm, 2-norm, and ∞-norm? Why are they called like that?

[list2tab|#Common p-norms]
- **L1-norm ($p=1$)**
    - **Formula:** $\|\mathbf{x}\|_1 = \sum_{i=1}^{n} |x_i| = |x_1| + |x_2| + \dots + |x_n|$
    - **Common Names:**
        - **Manhattan Norm:** This name comes from the grid-like path a taxi would take in Manhattan (where streets are often in a grid). The L1 distance between two points $(x_1, y_1)$ and $(x_2, y_2)$ is $|x_1-x_2| + |y_1-y_2|$, which is the distance traveled along grid lines.
        - **Taxicab Norm:** Similar to Manhattan norm.
        - Sum Absolute Deviations (SAD) is related when comparing to a zero vector or between two vectors.
    - **Why these names?** They reflect the idea of summing absolute differences along axes, akin to moving along a city grid.
    - **Use Cases:** Promotes sparsity in machine learning (e.g., L1 regularization like Lasso), robust to outliers in some contexts, feature selection.

- **L2-norm ($p=2$)**
    - **Formula:** $\|\mathbf{x}\|_2 = \sqrt{\sum_{i=1}^{n} |x_i|^2} = \sqrt{x_1^2 + x_2^2 + \dots + x_n^2}$
    - **Common Names:**
        - **Euclidean Norm:** This is the ordinary "straight-line" distance from the origin to the point represented by the vector in Euclidean space. It's derived from the Pythagorean theorem.
        - (Sometimes just called "the norm" or "magnitude" if context is clear).
    - **Why these names?** It corresponds to our intuitive notion of distance in Euclidean geometry. It's also related to the [[Dot_Product|dot product]]: $\|\mathbf{x}\|_2 = \sqrt{\mathbf{x} \cdot \mathbf{x}}$.
    - **Use Cases:** Most common norm, used in many geometric calculations, distance measurements (Euclidean distance), L2 regularization (Ridge regression, weight decay), least squares.

- **L$\infty$-norm ($p \to \infty$)**
    - **Formula:** $\|\mathbf{x}\|_\infty = \max_{i} |x_i| = \max(|x_1|, |x_2|, \dots, |x_n|)$
    - **Common Names:**
        - **Maximum Norm (Max Norm):** This name directly describes what it calculates – the maximum absolute value among the vector's components.
        - **Uniform Norm:** Related to the concept of uniform convergence.
        - Chebyshev Norm (related to Chebyshev distance).
    - **Why these names?** As $p$ approaches infinity in the $L_p$ formula, the term with the largest absolute value $|x_i|$ dominates the sum, leading to the maximum absolute component.
      Consider $(\sum |x_i|^p)^{1/p}$. Let $|x_k|$ be $\max_i |x_i|$. Then $\|\mathbf{x}\|_p = |x_k| (\sum (|x_i|/|x_k|)^p)^{1/p}$. As $p \to \infty$, $(|x_i|/|x_k|)^p \to 0$ if $|x_i| < |x_k|$, and $\to 1$ if $|x_i| = |x_k|$. If there's a unique maximum, the sum inside parenthesis approaches 1.
    - **Use Cases:** Useful when the largest component is of primary interest, error analysis (maximum error), some types of regularization, feature scaling to a max value.

- **L0-norm (Pseudo-norm)**
    - **Definition:** Although not strictly a norm (it violates the homogeneity property $\|k\mathbf{v}\| = |k| \|\mathbf{v}\|$ for $k \neq \pm 1$), the "L0-norm" is often used to denote the number of non-zero elements in a vector.
    - **Formula:** $\|\mathbf{x}\|_0 = \sum_{i=1}^{n} \mathbb{I}(x_i \neq 0)$, where $\mathbb{I}$ is the indicator function.
    - **Use Cases:** Sparsity measure in compressed sensing and feature selection. Computationally hard to optimize directly, often approximated by L1-norm.

## Geometric Interpretation (Unit Circles in 2D)
The set of all vectors $\mathbf{x}$ such that $\|\mathbf{x}\|_p = 1$ forms the "unit circle" for that norm.
- **L1-norm:** A diamond (rotated square).
- **L2-norm:** A standard circle.
- **L$\infty$-norm:** A square aligned with axes.

```mermaid
graph TD
    subgraph L1_Norm_Unit_Circle ["L1 Unit Circle: ||x||_1 = 1"]
        P1((1,0)) --- P2((0,1)) --- P3((-1,0)) --- P4((0,-1)) --- P1
    end
    subgraph L2_Norm_Unit_Circle ["L2 Unit Circle: ||x||_2 = 1"]
        C[Circle center 0,0 radius 1]
    end
    subgraph Linf_Norm_Unit_Circle ["L-inf Unit Circle: ||x||_inf = 1"]
        S1((1,1)) --- S2((-1,1)) --- S3((-1,-1)) --- S4((1,-1)) --- S1
    end

    style P1 fill:#afa
    style P2 fill:#afa
    style P3 fill:#afa
    style P4 fill:#afa
    style C fill:#aaf,stroke:#333,stroke-width:4px,r:50
    style S1 fill:#faa
    style S2 fill:#faa
    style S3 fill:#faa
    style S4 fill:#faa
```

## Applications
- **Distance Metrics:** The norm of the difference between two vectors, $\|\mathbf{a} - \mathbf{b}\|_p$, defines the $L_p$ distance.
- **Regularization in Machine Learning:**
    - L1 regularization (Lasso) adds $\|\mathbf{w}\|_1$ to the loss function, promoting sparse weight vectors (feature selection).
    - L2 regularization (Ridge/Weight Decay) adds $\|\mathbf{w}\|_2^2$ to the loss function, penalizing large weights and preventing overfitting.
- **Error Measurement:** Different norms can be used to measure the error between a predicted vector and a true vector.
- **Signal Processing & Image Analysis:** Various norms are used for noise reduction and feature extraction.

---
````

Filename: 150_Mathematics/Linear_Algebra/Hadamard_Product.md
````markdown
---
tags: [mathematics, linear_algebra, matrix, vector, hadamard_product, element_wise_product, schur_product, concept]
aliases: [Element-wise Matrix Product, Schur Product, Pointwise Matrix Product]
related:
  - "[[Matrix]]"
  - "[[Vector]]"
  - "[[Element_wise_Matrix_Operations]]"
  - "[[Matrix_Product]]" # Contrast with standard matrix product
worksheet: [WS_Math_Foundations_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
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
````

Filename: 150_Mathematics/Calculus/Matrix_Calculus.md
````markdown
---
tags: [mathematics, calculus, linear_algebra, matrix_calculus, derivatives, gradient, jacobian, hessian, concept]
aliases: [Matrix Derivatives, Vector Calculus, Tensor Calculus (basics)]
related:
  - "[[_Calculus_MOC]]"
  - "[[_Linear_Algebra_MOC]]"
  - "[[Calculus_Derivatives]]"
  - "[[Matrix]]"
  - "[[Vector]]"
  - "[[Scalar]]"
  - "[[Gradient]]"
  - "[[Jacobian]]"
  - "[[Hessian]]"
  - "[[Calculus_Optimization]]" # Core application
worksheet: [WS_Math_Foundations_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Matrix Calculus

## Definition
**Matrix calculus** (also known as matrix differential calculus or vector calculus in this context) is a specialized notation and collection of rules for differentiating functions whose arguments or values (or both) are [[Matrix|matrices]] or [[Vector|vectors]]. It extends the concepts of single-variable [[Calculus_Derivatives|calculus]] to higher dimensions.

The core idea is to define how a function's output (which can be a [[Scalar|scalar]], vector, or matrix) changes with respect to changes in its input (which can also be a scalar, vector, or matrix).

## Key Combinations of Derivatives
The derivative can be of a scalar, vector, or matrix, and *by* a scalar, vector, or matrix. The layout (shape) of the resulting derivative (e.g., whether a derivative of a scalar by a vector is a row or column vector) depends on notational conventions (numerator layout vs. denominator layout). We will generally describe common conventions.

[list2tab|#Derivative Combinations (Output by Input)]
- **Scalar by Scalar: $\frac{df}{dx}$**
    - **Input:** Scalar $x$
    - **Output Function:** Scalar $f(x)$
    - **Derivative:** Scalar. This is the standard derivative from single-variable calculus.
    - **Example:** If $f(x) = x^2$, then $\frac{df}{dx} = 2x$.

- **Vector by Scalar: $\frac{d\mathbf{y}}{dx}$**
    - **Input:** Scalar $x$
    - **Output Function:** Vector $\mathbf{y}(x) = \begin{pmatrix} y_1(x) \\ \vdots \\ y_m(x) \end{pmatrix}$
    - **Derivative:** Vector (same dimension as $\mathbf{y}$). Each component of the derivative vector is the derivative of the corresponding component of $\mathbf{y}$ with respect to $x$.
    - $$ \frac{d\mathbf{y}}{dx} = \begin{pmatrix} \frac{dy_1}{dx} \\ \vdots \\ \frac{dy_m}{dx} \end{pmatrix} $$
    - **Example:** If $\mathbf{y}(x) = \begin{pmatrix} x^2 \\ \sin(x) \end{pmatrix}$, then $\frac{d\mathbf{y}}{dx} = \begin{pmatrix} 2x \\ \cos(x) \end{pmatrix}$.

- **Matrix by Scalar: $\frac{d\mathbf{Y}}{dx}$**
    - **Input:** Scalar $x$
    - **Output Function:** Matrix $\mathbf{Y}(x)$ (e.g., $m \times p$)
    - **Derivative:** Matrix (same dimensions as $\mathbf{Y}$). Each element of the derivative matrix is the derivative of the corresponding element of $\mathbf{Y}$ with respect to $x$.
    - $$ \left(\frac{d\mathbf{Y}}{dx}\right)_{ij} = \frac{dY_{ij}}{dx} $$

- **Scalar by Vector: $\frac{df}{d\mathbf{x}}$ (This is the [[Gradient|Gradient]])**
    - **Input:** Vector $\mathbf{x} = \begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix}$
    - **Output Function:** Scalar $f(\mathbf{x})$
    - **Derivative:** Vector (typically a column vector by numerator layout convention, or row vector by denominator layout). It's called the **[[Gradient|gradient]]** of $f$ with respect to $\mathbf{x}$, denoted $\nabla_{\mathbf{x}} f$ or $\nabla f$.
    - $$ \nabla_{\mathbf{x}} f = \frac{df}{d\mathbf{x}} = \begin{pmatrix} \frac{\partial f}{\partial x_1} \\ \frac{\partial f}{\partial x_2} \\ \vdots \\ \frac{\partial f}{\partial x_n} \end{pmatrix} $$
      (This is the numerator layout, resulting in a column vector of the same shape as $\mathbf{x}$).
    - **Example:** If $f(\mathbf{x}) = x_1^2 + x_2^3$ for $\mathbf{x} = (x_1, x_2)^T$, then $\nabla f = \begin{pmatrix} 2x_1 \\ 3x_2^2 \end{pmatrix}$.

- **Vector by Vector: $\frac{d\mathbf{y}}{d\mathbf{x}}$ (This is the [[Jacobian|Jacobian Matrix]])**
    - **Input:** Vector $\mathbf{x} = \begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix}$
    - **Output Function:** Vector $\mathbf{y}(\mathbf{x}) = \begin{pmatrix} y_1(\mathbf{x}) \\ \vdots \\ y_m(\mathbf{x}) \end{pmatrix}$
    - **Derivative:** Matrix, called the **[[Jacobian|Jacobian matrix]]** $\mathbf{J}$. Its dimensions depend on the layout convention.
    - Using numerator layout for $\mathbf{y}$ (column) and denominator layout for $\mathbf{x}$ (meaning derivative of $y_i$ by $x_j$ is $J_{ij}$), the Jacobian is an $m \times n$ matrix:
    - $$ \mathbf{J} = \frac{d\mathbf{y}}{d\mathbf{x}^T} = \begin{pmatrix}
        \frac{\partial y_1}{\partial x_1} & \frac{\partial y_1}{\partial x_2} & \dots & \frac{\partial y_1}{\partial x_n} \\
        \frac{\partial y_2}{\partial x_1} & \frac{\partial y_2}{\partial x_2} & \dots & \frac{\partial y_2}{\partial x_n} \\
        \vdots & \vdots & \ddots & \vdots \\
        \frac{\partial y_m}{\partial x_1} & \frac{\partial y_m}{\partial x_2} & \dots & \frac{\partial y_m}{\partial x_n}
        \end{pmatrix} $$
      (Here, $d\mathbf{x}^T$ indicates that $x_j$ varies along columns).
    - If both are treated as column vectors (numerator layout for both), the result might be defined differently, e.g., as a tensor or a collection of gradients. The $m \times n$ matrix above is the most common representation for the Jacobian of $\mathbf{y}: \mathbb{R}^n \to \mathbb{R}^m$.
    - If $m=1$ (scalar output), the Jacobian becomes a row vector (transpose of the gradient if using column vector gradient convention).
    - If $n=1$ (scalar input), the Jacobian becomes a column vector (derivative of vector by scalar).

- **Scalar by Matrix: $\frac{df}{d\mathbf{X}}$**
    - **Input:** Matrix $\mathbf{X}$ (e.g., $p \times q$)
    - **Output Function:** Scalar $f(\mathbf{X})$
    - **Derivative:** Matrix (same dimensions as $\mathbf{X}$). Each element $(\frac{df}{d\mathbf{X}})_{ij}$ is $\frac{\partial f}{\partial X_{ij}}$.
    - **Example:** If $f(\mathbf{X}) = \text{tr}(\mathbf{X}) = \sum X_{ii}$ (for a square matrix), then $\frac{df}{d\mathbf{X}} = \mathbf{I}$ (identity matrix).
    - For $f(\mathbf{X}) = \mathbf{a}^T \mathbf{X} \mathbf{b}$ (scalar), $\frac{df}{d\mathbf{X}} = \mathbf{a} \mathbf{b}^T$.

- **Other Combinations (More Advanced / Tensor Notation):**
    - **Matrix by Vector:** $\frac{d\mathbf{Y}}{d\mathbf{x}}$
    - **Vector by Matrix:** $\frac{d\mathbf{y}}{d\mathbf{X}}$
    - **Matrix by Matrix:** $\frac{d\mathbf{Y}}{d\mathbf{X}}$
    - These often result in higher-order tensors or require careful definition of layout and operations (e.g., using Kronecker products or vectorization).

## Focus Areas in Machine Learning
In ML, the most commonly encountered matrix calculus derivatives are:
1.  **[[Gradient|Scalar by Vector ($\nabla_{\mathbf{x}} f$)]]:** Essential for optimizing loss functions with respect to model parameters (weights, biases) which are often represented as vectors.
2.  **[[Jacobian|Vector by Vector ($\frac{d\mathbf{y}}{d\mathbf{x}}$)]]:** Used in backpropagation for vector-valued functions, change of variables in probability, and sensitivity analysis.
3.  **[[Hessian|Scalar by Vector (Second Derivative - $\nabla^2_{\mathbf{x}} f$)]]:** The Hessian matrix is the Jacobian of the Gradient. It's a matrix of second-order partial derivatives, crucial for second-order optimization methods (like Newton's method) and analyzing the curvature of a function (convexity/concavity).
4.  **Scalar by Matrix ($\frac{df}{d\mathbf{X}}$):** Important when optimizing with respect to matrix parameters, like weight matrices in neural networks.

## Chain Rule
The chain rule extends to matrix calculus, but its form can be complex depending on the functions involved. For example, if $f$ is a scalar, $\mathbf{y}$ is a vector function of $\mathbf{x}$ (vector), and $z = f(\mathbf{y}(\mathbf{x}))$, then:
$$ \frac{dz}{d\mathbf{x}} = \left(\frac{d\mathbf{y}}{d\mathbf{x}}\right)^T \frac{df}{d\mathbf{y}} $$
(This uses specific layout conventions: gradient as column, Jacobian $J_{ij} = \partial y_i / \partial x_j$). The exact form depends on layout choices.

## Importance
Matrix calculus provides a compact and powerful way to:
- Derive update rules for optimization algorithms (e.g., [[Gradient_Descent]]).
- Analyze the sensitivity of functions to changes in multiple variables.
- Perform backpropagation in neural networks efficiently.
- Work with multivariate probability distributions.

 Mastering matrix calculus requires careful attention to the dimensions of inputs, outputs, and the resulting derivatives, as well as consistent use of layout conventions. Key resources include "The Matrix Cookbook" and "Matrix Differential Calculus with Applications in Statistics and Econometrics".

---
````

Filename: 150_Mathematics/Calculus/Hessian.md
````markdown
---
tags: [mathematics, calculus, matrix_calculus, hessian, second_derivative, optimization, concept]
aliases: [Hessian Matrix]
related:
  - "[[Matrix_Calculus]]"
  - "[[Gradient]]"
  - "[[Jacobian]]"
  - "[[Calculus_Derivatives]]" # Second-order partial derivatives
  - "[[Calculus_Optimization]]" # Used in second-order optimization methods
  - "[[Convex_Optimization]]" # Hessian used to check convexity
worksheet: [WS_Math_Foundations_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Hessian Matrix

## Definition
In multivariable calculus, the **Hessian matrix** (or simply the **Hessian**) of a scalar-valued function $f(\mathbf{x})$ of $n$ variables $\mathbf{x} = (x_1, x_2, \dots, x_n)$ is the square $n \times n$ [[Matrix|matrix]] of its second-order partial [[Calculus_Derivatives|derivatives]].

If all second partial derivatives of $f$ exist and are continuous, the Hessian matrix $\mathbf{H}$ (or $\nabla^2 f$) is defined as:
$$ \mathbf{H}_{ij} = \frac{\partial^2 f}{\partial x_i \partial x_j} $$
So, the Hessian matrix looks like this:
$$ \mathbf{H} = \nabla^2 f(\mathbf{x}) =
\begin{pmatrix}
\frac{\partial^2 f}{\partial x_1^2} & \frac{\partial^2 f}{\partial x_1 \partial x_2} & \dots & \frac{\partial^2 f}{\partial x_1 \partial x_n} \\
\frac{\partial^2 f}{\partial x_2 \partial x_1} & \frac{\partial^2 f}{\partial x_2^2} & \dots & \frac{\partial^2 f}{\partial x_2 \partial x_n} \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial^2 f}{\partial x_n \partial x_1} & \frac{\partial^2 f}{\partial x_n \partial x_2} & \dots & \frac{\partial^2 f}{\partial x_n^2}
\end{pmatrix}
$$

Under the condition of continuity of second partial derivatives (Clairaut's theorem on equality of mixed partials), the Hessian matrix is a **symmetric matrix**, i.e., $\frac{\partial^2 f}{\partial x_i \partial x_j} = \frac{\partial^2 f}{\partial x_j \partial x_i}$, so $\mathbf{H} = \mathbf{H}^T$.

The Hessian can also be seen as the [[Jacobian|Jacobian matrix]] of the [[Gradient|gradient]] vector $\nabla f$:
$$ \mathbf{H}(f)(\mathbf{x}) = \mathbf{J}(\nabla f)(\mathbf{x}) $$
(Assuming gradient is a column vector, and Jacobian $J_{ij} = \frac{\partial (\nabla f)_i}{\partial x_j}$).

## Role in Optimization
The Hessian matrix plays a crucial role in [[Calculus_Optimization|optimization]] problems for multivariable functions, similar to how the second derivative is used in single-variable calculus:

1.  **Second-Order Test for Local Extrema:**
    Let $\mathbf{x}_0$ be a critical point of $f$ (i.e., $\nabla f(\mathbf{x}_0) = \mathbf{0}$). Let $\mathbf{H}_0$ be the Hessian evaluated at $\mathbf{x}_0$.
    - If $\mathbf{H}_0$ is **positive definite** (all its [[Eigenvalues_Eigenvectors|eigenvalues]] are positive), then $f$ has a local minimum at $\mathbf{x}_0$.
    - If $\mathbf{H}_0$ is **negative definite** (all its eigenvalues are negative), then $f$ has a local maximum at $\mathbf{x}_0$.
    - If $\mathbf{H}_0$ has both positive and negative eigenvalues (indefinite), then $\mathbf{x}_0$ is a **saddle point**.
    - If $\mathbf{H}_0$ is singular (at least one eigenvalue is zero) and semi-definite (but not definite), the test is inconclusive.

2.  **Convexity:**
    For a twice-differentiable function $f$ defined on a convex set:
    - $f$ is a [[Convex_Optimization|convex function]] if and only if its Hessian matrix $\mathbf{H}$ is positive semi-definite for all $\mathbf{x}$ in the domain.
    - $f$ is a strictly convex function if its Hessian matrix $\mathbf{H}$ is positive definite for all $\mathbf{x}$ in the domain.
    - Similar conditions apply for concave functions (Hessian being negative semi-definite or negative definite).
    Convexity is highly desirable in optimization because any local minimum of a convex function is also a global minimum.

3.  **Newton's Method for Optimization:**
    Newton's method is a second-order optimization algorithm that uses the Hessian matrix to find the minimum (or maximum) of a function. The update rule is:
    $$ \mathbf{x}_{k+1} = \mathbf{x}_k - [\mathbf{H}(f)(\mathbf{x}_k)]^{-1} \nabla f(\mathbf{x}_k) $$
    This method converges quickly near the optimum if the function is well-behaved and the Hessian is positive definite, but computing and inverting the Hessian can be computationally expensive for high-dimensional problems.

## Example
Let $f(x, y) = x^2 + y^2 + xy$.
Partial derivatives:
- $\frac{\partial f}{\partial x} = 2x + y$
- $\frac{\partial f}{\partial y} = 2y + x$

Second-order partial derivatives:
- $\frac{\partial^2 f}{\partial x^2} = 2$
- $\frac{\partial^2 f}{\partial y^2} = 2$
- $\frac{\partial^2 f}{\partial x \partial y} = 1$
- $\frac{\partial^2 f}{\partial y \partial x} = 1$

The Hessian matrix is:
$$ \mathbf{H} = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix} $$
To check for definiteness, we can look at eigenvalues or leading principal minors.
Determinant: $(2)(2) - (1)(1) = 4 - 1 = 3 > 0$.
Trace (sum of diagonal elements, also sum of eigenvalues): $2+2 = 4 > 0$.
Since the determinant is positive and the first leading principal minor ($H_{11}=2$) is positive, the matrix is positive definite.
Thus, $f(x,y)$ is a convex function.
The critical point is where $\nabla f = \mathbf{0}$:
$2x+y=0$ and $x+2y=0$. Solving this system gives $x=0, y=0$.
Since the Hessian is positive definite everywhere, the point $(0,0)$ is a local (and global) minimum.

## Computational Cost
For a function of $n$ variables, the Hessian matrix has $n^2$ elements. Computing all these second derivatives can be expensive. For very high-dimensional problems (common in deep learning where $n$ can be millions or billions), explicitly forming and storing the Hessian is often infeasible. Quasi-Newton methods (like L-BFGS) approximate the Hessian or its inverse.

---
````

Filename: 150_Mathematics/Calculus/Jacobian.md
````markdown
---
tags: [mathematics, calculus, matrix_calculus, jacobian, vector_calculus, derivative, concept]
aliases: [Jacobian Matrix, Jacobian Determinant]
related:
  - "[[Matrix_Calculus]]"
  - "[[Gradient]]"
  - "[[Hessian]]"
  - "[[Calculus_Derivatives]]" # Partial derivatives
  - "[[Determinant_Matrix]]" # Jacobian determinant
  - "[[Change_of_Variables_Integration]]"
worksheet: [WS_Math_Foundations_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Jacobian Matrix

## Definition
In vector calculus, the **Jacobian matrix** (or simply the **Jacobian**) of a vector-valued function of several variables is the [[Matrix|matrix]] of all its first-order partial [[Calculus_Derivatives|derivatives]]. It generalizes the concept of the derivative of a single-variable function to multivariable vector-valued functions.

Let $\mathbf{f}: \mathbb{R}^n \to \mathbb{R}^m$ be a function that takes as input a [[Vector|vector]] $\mathbf{x} \in \mathbb{R}^n$ and produces an output vector $\mathbf{f}(\mathbf{x}) \in \mathbb{R}^m$.
$$ \mathbf{x} = \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix}, \quad \mathbf{f}(\mathbf{x}) = \begin{pmatrix} f_1(\mathbf{x}) \\ f_2(\mathbf{x}) \\ \vdots \\ f_m(\mathbf{x}) \end{pmatrix} $$
The Jacobian matrix $\mathbf{J}$ of $\mathbf{f}$ (or $\mathbf{J}_{\mathbf{f}}$, or $\frac{d\mathbf{f}}{d\mathbf{x}^T}$) is an $m \times n$ matrix, defined as:
$$ \mathbf{J} =
\begin{pmatrix}
\frac{\partial f_1}{\partial x_1} & \frac{\partial f_1}{\partial x_2} & \dots & \frac{\partial f_1}{\partial x_n} \\
\frac{\partial f_2}{\partial x_1} & \frac{\partial f_2}{\partial x_2} & \dots & \frac{\partial f_2}{\partial x_n} \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial f_m}{\partial x_1} & \frac{\partial f_m}{\partial x_2} & \dots & \frac{\partial f_m}{\partial x_n}
\end{pmatrix}
$$
Each row $i$ of $\mathbf{J}$ is the transpose of the [[Gradient|gradient]] of the $i$-th component function $f_i$: $(\nabla f_i)^T$.
The element $(i,j)$ of the Jacobian matrix is $J_{ij} = \frac{\partial f_i}{\partial x_j}$.

## Interpretation
- **Best Linear Approximation:** If the function $\mathbf{f}$ is differentiable at a point $\mathbf{x}_0$, its Jacobian matrix $\mathbf{J}(\mathbf{x}_0)$ represents the best linear approximation of the function $\mathbf{f}$ near $\mathbf{x}_0$.
  $$ \mathbf{f}(\mathbf{x}) \approx \mathbf{f}(\mathbf{x}_0) + \mathbf{J}(\mathbf{x}_0)(\mathbf{x} - \mathbf{x}_0) $$
  This means the Jacobian describes how a small change in the input vector $\mathbf{x}$ leads to a change in the output vector $\mathbf{f}(\mathbf{x})$.
- **Transformation of Volume/Area:** The absolute value of the [[Determinant_Matrix|determinant]] of the Jacobian matrix (if $m=n$, i.e., a square Jacobian) gives the factor by which the function locally stretches or shrinks volumes (or areas in 2D) when transforming coordinates. This is crucial for the [[Change_of_Variables_Integration|change of variables technique in multiple integrals]].

## Special Cases
- **If $m=1$ (scalar-valued function $f: \mathbb{R}^n \to \mathbb{R}$):**
    The Jacobian matrix becomes a $1 \times n$ row vector. This row vector is the transpose of the [[Gradient|gradient]] of $f$:
    $$ \mathbf{J}_f = (\nabla f)^T = \begin{bmatrix} \frac{\partial f}{\partial x_1} & \frac{\partial f}{\partial x_2} & \dots & \frac{\partial f}{\partial x_n} \end{bmatrix} $$
- **If $n=1$ (vector-valued function of a single variable $\mathbf{f}: \mathbb{R} \to \mathbb{R}^m$):**
    The Jacobian matrix becomes an $m \times 1$ column vector, which is simply the derivative of the vector function with respect to the single variable:
    $$ \mathbf{J}_{\mathbf{f}} = \begin{pmatrix} \frac{df_1}{dx} \\ \frac{df_2}{dx} \\ \vdots \\ \frac{df_m}{dx} \end{pmatrix} $$
- **If $m=n$ (function from $\mathbb{R}^n \to \mathbb{R}^n$):**
    The Jacobian matrix is a square $n \times n$ matrix. Its determinant, $\det(\mathbf{J})$, is called the **Jacobian determinant** (or simply "the Jacobian" in some contexts).

## Jacobian Determinant
If $m=n$, the determinant of the Jacobian matrix, $\det(\mathbf{J})$, is of particular importance:
- **Local Invertibility:** If $\det(\mathbf{J})(\mathbf{x}_0) \neq 0$ at a point $\mathbf{x}_0$, then the function $\mathbf{f}$ is locally invertible near $\mathbf{x}_0$ (Inverse Function Theorem). The Jacobian of the inverse function $\mathbf{f}^{-1}$ at $\mathbf{f}(\mathbf{x}_0)$ is the inverse of the Jacobian of $\mathbf{f}$ at $\mathbf{x}_0$: $\mathbf{J}_{\mathbf{f}^{-1}}(\mathbf{f}(\mathbf{x}_0)) = [\mathbf{J}_{\mathbf{f}}(\mathbf{x}_0)]^{-1}$.
- **Change of Variables in Multiple Integrals:** When changing variables in a multiple integral, the differential volume element $dx_1 dx_2 \dots dx_n$ transforms to $|\det(\mathbf{J})| du_1 du_2 \dots du_n$, where $\mathbf{J}$ is the Jacobian of the transformation from $u$-coordinates to $x$-coordinates.

## Example
Consider a transformation from polar coordinates $(r, \theta)$ to Cartesian coordinates $(x, y)$:
$x = r \cos \theta$
$y = r \sin \theta$
Here, $\mathbf{f}(r, \theta) = \begin{pmatrix} x(r, \theta) \\ y(r, \theta) \end{pmatrix}$.
The Jacobian matrix $\mathbf{J} = \frac{\partial(x,y)}{\partial(r,\theta)}$ is:
$$ \mathbf{J} =
\begin{pmatrix}
\frac{\partial x}{\partial r} & \frac{\partial x}{\partial \theta} \\
\frac{\partial y}{\partial r} & \frac{\partial y}{\partial \theta}
\end{pmatrix}
=
\begin{pmatrix}
\cos \theta & -r \sin \theta \\
\sin \theta & r \cos \theta
\end{pmatrix}
$$
The Jacobian determinant is:
$$ \det(\mathbf{J}) = (\cos \theta)(r \cos \theta) - (-r \sin \theta)(\sin \theta) = r \cos^2 \theta + r \sin^2 \theta = r(\cos^2 \theta + \sin^2 \theta) = r $$
This $r$ is the factor used when converting an area element $dA = dx dy$ to polar coordinates: $dA = r dr d\theta$.

## Applications
- **Optimization:** Used in some variations of Newton's method for systems of equations or vector-valued functions.
- **Sensitivity Analysis:** Shows how sensitive the output components are to changes in input components.
- **Robotics:** Relates joint velocities to end-effector velocities.
- **Continuum Mechanics:** Describes deformation gradients.
- **Probability Theory:** Used in transformations of random variables to find the PDF of the transformed variable.
- **Neural Networks (Backpropagation):** The chain rule for Jacobians is implicitly used in backpropagation when dealing with vector-valued activation functions or layers. The [[Hessian]] matrix is the Jacobian of the [[Gradient]].

---
````