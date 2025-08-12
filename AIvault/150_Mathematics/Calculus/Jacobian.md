---
tags:
  - mathematics
  - calculus
  - matrix_calculus
  - jacobian
  - vector_calculus
  - derivative
  - concept
aliases:
  - Jacobian Matrix
  - Jacobian Determinant
related:
  - "[[Matrix_Calculus]]"
  - "[[Gradient]]"
  - "[[Hessian]]"
  - "[[Calculus_Derivatives]]"
  - "[[Determinant_Matrix]]"
  - "[[Change_of_Variables_Integration]]"
worksheet:
  - WS_Math_Foundations_1
date_created: 2025-05-30
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