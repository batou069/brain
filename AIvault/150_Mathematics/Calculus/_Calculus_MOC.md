---
tags:
  - mathematics
  - calculus
  - moc
aliases:
  - Calculus MOC
related:
  - "[[_Mathematics_MOC]]"
  - "[[Calculus_Derivatives]]"
  - "[[Calculus_Integrals]]"
  - "[[Calculus_Optimization]]"
  - "[[Matrix_Calculus]]"
  - "[[Gradient]]"
  - "[[Jacobian]]"
  - "[[Hessian]]"
worksheet:
  - WS_Math_Foundations_1
date_created: 2025-05-30
---
# Calculus MOC

Calculus is a branch of mathematics focused on limits, functions, [[Calculus_Derivatives|derivatives]], [[Calculus_Integrals|integrals]], and infinite series. It is fundamental to understanding change and motion, and plays a critical role in [[Calculus_Optimization|optimization]], which is at the heart of training many machine learning models.

## Core Concepts

[list2card|addClass(ab-col3)]
- **[[Limits]]**
  - The value that a function or sequence "approaches" as the input or index approaches some value. Fundamental to defining derivatives and integrals.
- **[[Calculus_Derivatives|Derivatives]]**
  - Measure the instantaneous rate of change of a function. Geometrically, the slope of the tangent line to the function's graph.
- **[[Calculus_Integrals|Integrals]]**
  - Represent the accumulation of quantities, such as the area under a curve. The inverse operation of differentiation (Fundamental Theorem of Calculus).
- **[[Calculus_Optimization|Optimization]]**
  - Finding the input values (e.g., model parameters) that result in the minimum or maximum output of a function (e.g., minimizing a loss function). Heavily relies on derivatives.
- **[[Matrix_Calculus|Matrix Calculus]]**
  - Extends concepts of calculus to functions involving [[Vector|vectors]] and [[Matrix|matrices]].
  - Includes:
    - [[Gradient]] (derivative of a scalar function with respect to a vector)
    - [[Jacobian]] (derivative of a vector function with respect to a vector)
    - [[Hessian]] (second-order partial derivatives of a scalar function)

## Applications in AI/ML
- **Gradient Descent:** An optimization algorithm that uses gradients (derivatives) to iteratively find the minimum of a loss function.
- **Backpropagation:** The algorithm used to train artificial neural networks, which relies heavily on the chain rule for derivatives.
- **Probability Density Functions:** Integrals are used to calculate probabilities from continuous probability distributions.
- **Model Formulation:** Many models are defined using functions whose properties are analyzed using calculus.

## Notes in this Section
```dataview
LIST
FROM "150_Mathematics/Calculus"
WHERE file.folder = this.file.folder AND file.name != this.file.name AND !contains(file.name, "MOC")
SORT file.name ASC
```

---