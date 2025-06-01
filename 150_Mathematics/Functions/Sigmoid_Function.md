---
tags:
  - mathematics
  - functions
  - sigmoid
  - logistic_function
  - activation_function
  - machine_learning
  - concept
aliases:
  - Logistic Function
  - Sigmoid Curve
  - Standard Sigmoid
related:
  - "[[_Functions_MOC]]"
  - "[[Exponential_Function]]"
  - "[[Logarithmic_Function]]"
  - "[[Logit_Function]]"
  - "[[Hyperbolic_Functions]]"
  - "[[Softmax_Function]]"
  - "[[Binary_Classification]]"
  - "[[Neural_Networks]]"
worksheet:
  - WS_Math_Foundations_1
date_created: 2025-05-30
---
# Sigmoid Function (Logistic Function)

## Definition
The **sigmoid function**, often specifically referring to the **logistic function**, is a mathematical function having a characteristic "S"-shaped curve or sigmoid curve. It maps any real-valued number into a value between 0 and 1.

The standard logistic sigmoid function is defined as:
$$ \sigma(x) = \frac{1}{1 + e^{-x}} = \frac{e^x}{e^x + 1} $$
where $e$ is [[Euler_Number_e|Euler's number]].

## Properties
- **Domain:** $(-\infty, \infty)$ (all real numbers)
- **Range:** $(0, 1)$ (outputs are strictly between 0 and 1, never reaching 0 or 1)
- **Value at $x=0$:** $\sigma(0) = \frac{1}{1 + e^0} = \frac{1}{1+1} = 0.5$
- **Monotonically Increasing:** The function is always increasing.
- **Asymptotes:**
    - As $x \to \infty$, $e^{-x} \to 0$, so $\sigma(x) \to \frac{1}{1+0} = 1$. (Horizontal asymptote $y=1$)
    - As $x \to -\infty$, $e^{-x} \to \infty$, so $\sigma(x) \to \frac{1}{\text{large number}} \to 0$. (Horizontal asymptote $y=0$)
- **Symmetry:** The curve is symmetric about the point $(0, 0.5)$. Specifically, $\sigma(-x) = 1 - \sigma(x)$.
- **Derivative:**
  $$ \frac{d}{dx} \sigma(x) = \sigma(x)(1 - \sigma(x)) $$
  The derivative is bell-shaped, with a maximum value of $0.25$ at $x=0$. It is always non-negative.
- **Inverse Function:** The inverse of the sigmoid function is the **[[Logit_Function|logit function]]**. If $y = \sigma(x)$, then $x = \text{logit}(y) = \ln\left(\frac{y}{1-y}\right)$.

## Graph of $y = \sigma(x)$

```mermaid
graph TD
    subgraph SigmoidGraph["Graph of y = σ(x)"]
        XAxis["x (-5 to 5)"] --- YAxis["y (0 to 1)"]
        P0((0, 0.5))
        Pneg5((-5, "$σ(-5) \approx 0.0067$"))
        Ppos5((5, "$σ(5) \approx 0.9933$"))
        
        Asymptote0["y=0"] -.-> Pneg5
        Pneg5 --- P0 --- Ppos5 % Curve path
        Asymptote1["y=1"] -.-> Ppos5
    end
    P0 -->|Inflection Point (0, 0.5)| P0
    
    style P0 fill:#afa,stroke:#333,stroke-width:2px
    style Pneg5 fill:#aaf,stroke:#333,stroke-width:2px
    style Ppos5 fill:#aaf,stroke:#333,stroke-width:2px
    linkStyle 3 stroke-width:2px,fill:none,stroke:blue;
    linkStyle 4 stroke-width:2px,fill:none,stroke:blue,stroke-dasharray: 5 5;
    linkStyle 6 stroke-width:2px,fill:none,stroke:blue,stroke-dasharray: 5 5;
```

## Applications
- **Machine Learning / [[Neural_Networks|Neural Networks]]:**
    - **Activation Function:** Historically, it was a popular choice for activation functions in hidden layers of neural networks to introduce non-linearity. However, it suffers from the vanishing gradient problem for large positive or negative inputs, which can slow down learning. [[Hyperbolic_Functions|Tanh]] (which is zero-centered) or [[Rectified_Linear_Unit_ReLU|ReLU]] and its variants are often preferred in hidden layers now.
    - **Output Layer for [[Binary_Classification|Binary Classification]]:** The sigmoid function is commonly used in the output layer of a neural network for binary classification problems. The output (between 0 and 1) can be interpreted as the probability of the positive class.
      Example: If the network outputs a raw score $z$, $P(\text{class}=1 | \text{input}) = \sigma(z)$.
- **Logistic Regression:** The sigmoid function is the core of logistic regression, linking a linear combination of features to a probability.
- **Statistics:** The logistic function is the cumulative distribution function (CDF) of the logistic distribution.
- **Artificial Neuron Models:** Simulates the activation rate of a neuron.

## Relationship to Tanh
The sigmoid function is closely related to the [[Hyperbolic_Functions|hyperbolic tangent ($\tanh$) function]]:
$$ \tanh(x) = 2\sigma(2x) - 1 $$
$$ \sigma(x) = \frac{\tanh(x/2) + 1}{2} $$
$\tanh(x)$ has a range of $(-1, 1)$, while $\sigma(x)$ has a range of $(0, 1)$.

## The "Relaxation" of the Step Function

>[!question] One may say that the sigmoid function is the relaxation of the step function.
>    - What does that mean?
>    - How can we make it closer to a step function? How close can we get?
>    - What if we want the step to happen around $x \neq 0$ rather than $x=0$?

1.  **What does "relaxation" mean?**
    A **[[Step_Function|step function]]** (e.g., Heaviside step function $H(x)$ which is 0 for $x<0$ and 1 for $x \ge 0$) is discontinuous and non-differentiable at the step. "Relaxation" in this context means replacing this hard, discontinuous jump with a smooth, continuous, and differentiable transition. The sigmoid function provides this smooth approximation:
    - It transitions from (approximately) 0 to (approximately) 1.
    - The transition is gradual rather than instantaneous.
    - It is differentiable everywhere, which is crucial for gradient-based optimization methods used in training machine learning models.

2.  **How can we make it closer to a step function? How close can we get?**
    We can make the sigmoid function $\sigma(kx) = \frac{1}{1 + e^{-kx}}$ approximate a step function more closely by increasing the magnitude of the scaling factor $k$ (often called temperature or gain).
    - As $k \to \infty$:
        - For $x > 0$, $kx \to \infty$, $e^{-kx} \to 0$, so $\sigma(kx) \to 1$.
        - For $x < 0$, $kx \to -\infty$, $e^{-kx} \to \infty$, so $\sigma(kx) \to 0$.
        - At $x=0$, $\sigma(k \cdot 0) = 0.5$.
    - So, as $|k|$ increases, the transition of the sigmoid function becomes steeper and more closely resembles a step function.
    - **How close?** We can get arbitrarily close to a step function by making $k$ sufficiently large, but it will always remain a continuous and differentiable function, never perfectly replicating the discontinuity of a true step function. The transition region around $x=0$ will shrink but never disappear.

    ```python
    # Example of k effect:
    # import numpy as np
    # import matplotlib.pyplot as plt
    # def sigmoid(x, k=1): return 1 / (1 + np.exp(-k*x))
    # x = np.linspace(-5, 5, 100)
    # plt.plot(x, sigmoid(x, k=0.5), label='k=0.5')
    # plt.plot(x, sigmoid(x, k=1), label='k=1 (standard)')
    # plt.plot(x, sigmoid(x, k=5), label='k=5')
    # plt.plot(x, sigmoid(x, k=20), label='k=20 (steeper)')
    # plt.title("Sigmoid with varying k (steepness)")
    # plt.legend(); plt.grid(); plt.show()
    ```

3.  **What if we want the step to happen around $x_0 \neq 0$ rather than $x=0$?**
    We can shift the sigmoid function horizontally by introducing a bias or offset term. If we want the "step" (the point where the sigmoid is 0.5) to occur at $x = x_0$, we modify the argument of the exponential:
    $$ \sigma(k(x - x_0)) = \frac{1}{1 + e^{-k(x - x_0)}} $$
    Here:
    - $x_0$ controls the horizontal shift (center of the sigmoid).
    - $k$ still controls the steepness of the transition.
    When $x = x_0$, the exponent is $e^0 = 1$, and $\sigma(k(x_0 - x_0)) = \frac{1}{1+1} = 0.5$.

---