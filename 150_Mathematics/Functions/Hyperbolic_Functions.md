---
tags:
  - mathematics
  - functions
  - hyperbolic
  - sinh
  - cosh
  - tanh
  - exponential
  - concept
aliases:
  - Hyperbolic Trig Functions
  - sinh(x)
  - cosh(x)
  - tanh(x)
related:
  - "[[_Functions_MOC]]"
  - "[[Exponential_Function]]"
  - "[[Trigonometric_Functions]]"
  - "[[Unit_Hyperbola]]"
  - "[[Calculus_Derivatives]]"
  - "[[Calculus_Integrals]]"
  - "[[Sigmoid_Function]]"
worksheet:
  - WS_Math_Foundations_1
date_created: 2025-05-30
---
# Hyperbolic Functions

## Definition
**Hyperbolic functions** are analogues of the ordinary [[Trigonometric_Functions|trigonometric (circular) functions]], but defined using the [[Exponential_Function|natural exponential function $e^x$]] instead of a circle. Just as points $(\cos t, \sin t)$ form a circle with unit radius, points $(\cosh t, \sinh t)$ form the right half of the [[Unit_Hyperbola|unit hyperbola]] $x^2 - y^2 = 1$.

The basic hyperbolic functions are:
- **Hyperbolic Sine ($\sinh x$):**
  $$ \sinh x = \frac{e^x - e^{-x}}{2} $$
- **Hyperbolic Cosine ($\cosh x$):**
  $$ \cosh x = \frac{e^x + e^{-x}}{2} $$
- **Hyperbolic Tangent ($\tanh x$):**
  $$ \tanh x = \frac{\sinh x}{\cosh x} = \frac{e^x - e^{-x}}{e^x + e^{-x}} = \frac{e^{2x} - 1}{e^{2x} + 1} $$

Other hyperbolic functions are defined analogously to trigonometric functions:
- **Hyperbolic Cosecant ($\text{csch } x$):** $\text{csch } x = \frac{1}{\sinh x} = \frac{2}{e^x - e^{-x}}$ (for $x \neq 0$)
- **Hyperbolic Secant ($\text{sech } x$):** $\text{sech } x = \frac{1}{\cosh x} = \frac{2}{e^x + e^{-x}}$
- **Hyperbolic Cotangent ($\coth x$):** $\coth x = \frac{1}{\tanh x} = \frac{\cosh x}{\sinh x} = \frac{e^x + e^{-x}}{e^x - e^{-x}}$ (for $x \neq 0$)

## Properties

[list2tab|#Hyperbolic Function Properties]
- **Hyperbolic Sine ($\sinh x$)**
    - **Domain:** $(-\infty, \infty)$
    - **Range:** $(-\infty, \infty)$
    - **Odd function:** $\sinh(-x) = -\sinh x$
    - **Derivative:** $\frac{d}{dx} \sinh x = \cosh x$
    - **Integral:** $\int \sinh x \,dx = \cosh x + C$

- **Hyperbolic Cosine ($\cosh x$)**
    - **Domain:** $(-\infty, \infty)$
    - **Range:** $[1, \infty)$ (Note: $\cosh x \ge 1$ for all $x$, with $\cosh 0 = 1$)
    - **Even function:** $\cosh(-x) = \cosh x$
    - **Derivative:** $\frac{d}{dx} \cosh x = \sinh x$
    - **Integral:** $\int \cosh x \,dx = \sinh x + C$
    - The graph $y=\cosh x$ is the shape of a **catenary**, the curve formed by a flexible chain hanging under its own weight.

- **Hyperbolic Tangent ($\tanh x$)**
    - **Domain:** $(-\infty, \infty)$
    - **Range:** $(-1, 1)$
    - **Odd function:** $\tanh(-x) = -\tanh x$
    - **Derivative:** $\frac{d}{dx} \tanh x = \text{sech}^2 x = 1 - \tanh^2 x$
    - **Integral:** $\int \tanh x \,dx = \ln(\cosh x) + C$
    - **Asymptotes:** $y=1$ as $x \to \infty$, and $y=-1$ as $x \to -\infty$.
    - It is a sigmoidal (S-shaped) curve, similar to the [[Sigmoid_Function|logistic sigmoid function]].

## Fundamental Identities
Analogous to trigonometric identities:
- **Hyperbolic Pythagorean Identity:** $\cosh^2 x - \sinh^2 x = 1$
    (Compare to $\cos^2 x + \sin^2 x = 1$)
- **Other Identities:**
    - $1 - \tanh^2 x = \text{sech}^2 x$
    - $\coth^2 x - 1 = \text{csch}^2 x$
- **Sum/Difference Formulas:**
    - $\sinh(x \pm y) = \sinh x \cosh y \pm \cosh x \sinh y$
    - $\cosh(x \pm y) = \cosh x \cosh y \pm \sinh x \sinh y$
- **Osborn's Rule:** Trigonometric identities can often be converted to hyperbolic identities by changing $\sin$ to $\sinh$, $\cos$ to $\cosh$, but changing the sign of any term that is a product of two sines (e.g., $\sin^2 A$, $\sin A \sin B$).

## Graphs of $\sinh x$, $\cosh x$, $\tanh x$

```mermaid
graph TD
    subgraph HyperbolicGraphs["Graphs of sinh(x), cosh(x), tanh(x)"]
        XAxis["x (-3 to 3)"] --- YAxis["y (-3 to 3 for sinh/tanh, 0 to 5 for cosh)"]

        %% sinh(x) - blue
        Psinh_neg2((-2, -3.62)) --- Psinh_neg1((-1, -1.17)) --- Psinh0((0,0)) --- Psinh1((1, 1.17)) --- Psinh2((2, 3.62))
        
        %% cosh(x) - red
        Pcosh_neg2((-2, 3.76)) --- Pcosh_neg1((-1, 1.54)) --- Pcosh0((0,1)) --- Pcosh1((1, 1.54)) --- Pcosh2((2, 3.76))

        %% tanh(x) - green
        Ptanh_negInf(["x → -∞, y → -1"]) -.-> Ptanh_neg2((-2, -0.96)) --- Ptanh_neg1((-1, -0.76)) --- Ptanh0((0,0)) --- Ptanh1((1, 0.76)) --- Ptanh2((2, 0.96)) -.-> Ptanh_posInf(["x → +∞, y → 1"])

        note right of Psinh2 : sinh(x)
        note right of Pcosh2 : cosh(x)
        note right of Ptanh2 : tanh(x)
    end
    
    linkStyle 1 stroke:blue,stroke-width:2px,interpolate:basis; % sinh
    linkStyle 2 stroke:blue,stroke-width:2px,interpolate:basis;
    linkStyle 3 stroke:blue,stroke-width:2px,interpolate:basis;
    linkStyle 4 stroke:blue,stroke-width:2px,interpolate:basis;
    
    linkStyle 5 stroke:red,stroke-width:2px,interpolate:basis; % cosh
    linkStyle 6 stroke:red,stroke-width:2px,interpolate:basis;
    linkStyle 7 stroke:red,stroke-width:2px,interpolate:basis;
    linkStyle 8 stroke:red,stroke-width:2px,interpolate:basis;

    linkStyle 9 stroke:green,stroke-width:2px,interpolate:basis; % tanh
    linkStyle 10 stroke:green,stroke-width:2px,interpolate:basis;
    linkStyle 11 stroke:green,stroke-width:2px,interpolate:basis;
    linkStyle 12 stroke:green,stroke-width:2px,interpolate:basis;
    linkStyle 13 stroke:green,stroke-width:2px,interpolate:basis,stroke-dasharray: 5 5;
    linkStyle 14 stroke:green,stroke-width:2px,interpolate:basis,stroke-dasharray: 5 5;

    style Psinh0 fill:#fff,stroke:blue
    style Pcosh0 fill:#fff,stroke:red
    style Ptanh0 fill:#fff,stroke:green
```

## Applications
- **Physics and Engineering:**
    - **Catenary Curve ($\cosh x$):** Describes the shape of hanging cables, chains, or arches supporting only their own weight.
    - **Special Relativity:** Lorentz transformations involve hyperbolic functions (hyperbolic angle or rapidity).
    - Solutions to certain linear differential equations (e.g., Laplace's equation in specific coordinate systems).
    - Describing motion where acceleration is proportional to distance (e.g., an object falling through a resisting medium).
- **Machine Learning:**
    - **Activation Functions:** $\tanh x$ is widely used as an activation function in neural networks. It squashes input values to the range $(-1, 1)$, which can be beneficial for centering data for subsequent layers.
      >[!question] If tanh can be expressed as a sigmoid - why do we need both of them?
      >The standard [[Sigmoid_Function|logistic sigmoid function]] is $\sigma(x) = \frac{1}{1 + e^{-x}}$, which has a range $(0, 1)$.
      >The hyperbolic tangent function is $\tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}$.
      >
      >Indeed, $\tanh(x)$ can be expressed as a scaled and shifted version of the logistic sigmoid:
      >$$ \tanh(x) = 2 \sigma(2x) - 1 $$
      >Proof: $2 \sigma(2x) - 1 = 2 \frac{1}{1+e^{-2x}} - 1 = \frac{2 - (1+e^{-2x})}{1+e^{-2x}} = \frac{1 - e^{-2x}}{1+e^{-2x}} = \frac{e^{2x}(1 - e^{-2x})}{e^{2x}(1+e^{-2x})} = \frac{e^{2x}-1}{e^{2x}+1} = \tanh(x)$.
      >
      >Why use both?
      >1.  **Output Range:**
      >    - **Sigmoid $\sigma(x)$:** Range $(0, 1)$. Useful for representing probabilities or binary classification outputs.
      >    - **Tanh $\tanh(x)$:** Range $(-1, 1)$. Its output is zero-centered, which can sometimes lead to faster convergence during training of neural networks because the average activation is closer to zero, helping with the gradient flow (gradients are less likely to be all positive or all negative).
      >2.  **Gradient:**
      >    - The derivative of $\tanh(x)$ is $1 - \tanh^2(x)$. The maximum gradient is 1 (at $x=0$).
      >    - The derivative of $\sigma(x)$ is $\sigma(x)(1-\sigma(x))$. The maximum gradient is 0.25 (at $x=0$).
      >    - $\tanh(x)$ has a steeper gradient than $\sigma(x)$ around $x=0$, which can sometimes lead to stronger gradients and faster learning, but also potentially more issues with vanishing/exploding gradients if not managed.
      >3.  **Historical and Empirical Reasons:** Both have been used historically, and their performance can be task-dependent. $\tanh$ was often preferred in older neural network architectures before [[Rectified_Linear_Unit_ReLU|ReLU]] and its variants became popular, partly due to its zero-centered nature.
      >
      >In summary, while mathematically related, their different output ranges and gradient characteristics make them suitable for slightly different scenarios or lead to different empirical performance. $\tanh$ is often a good default choice for hidden layers if a sigmoidal activation is desired due to its zero-centered output.

- **Calculus:** Hyperbolic functions often simplify integrals that would be more complex with trigonometric substitutions.

---
