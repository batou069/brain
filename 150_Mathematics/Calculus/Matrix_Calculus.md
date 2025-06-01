---
tags:
  - mathematics
  - calculus
  - linear_algebra
  - matrix_calculus
  - derivatives
  - gradient
  - jacobian
  - hessian
  - concept
aliases:
  - Matrix Derivatives
  - Vector Calculus
  - Tensor Calculus (basics)
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
  - "[[Calculus_Optimization]]"
worksheet:
  - WS_Math_Foundations_1
date_created: 2025-05-30
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