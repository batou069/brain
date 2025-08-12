---
tags:
  - mathematics
  - functions
  - softmax
  - activation_function
  - machine_learning
  - probability
  - concept
aliases:
  - Normalized Exponential Function
related:
  - "[[_Functions_MOC]]"
  - "[[Exponential_Function]]"
  - "[[Sigmoid_Function]]"
  - "[[Vector]]"
  - "[[Probability_Distribution]]"
  - "[[Multi_Class_Classification]]"
  - "[[Neural_Networks]]"
worksheet:
  - WS_Math_Foundations_1
date_created: 2025-05-30
---
# Softmax Function

## Definition
The **softmax function**, also known as the **normalized exponential function**, is a generalization of the [[Sigmoid_Function|logistic (sigmoid) function]] to multiple dimensions. It takes a [[Vector|vector]] $\mathbf{z}$ of $K$ real numbers as input and transforms it into a probability distribution consisting of $K$ probabilities proportional to the exponentials of the input numbers.

For an input vector $\mathbf{z} = (z_1, z_2, \dots, z_K)$, the softmax function computes a vector $\mathbf{p} = \text{softmax}(\mathbf{z})$ where the $i$-th component $p_i$ is:
$$ p_i = \text{softmax}(\mathbf{z})_i = \frac{e^{z_i}}{\sum_{j=1}^{K} e^{z_j}} \quad \text{for } i = 1, \dots, K $$
where $e$ is [[Euler_Number_e|Euler's number]].

## Properties
- **Output Range:** Each output component $p_i$ is in the range $(0, 1)$.
  Since $e^{z_i} > 0$ and $\sum_{j=1}^{K} e^{z_j} > 0$, it follows that $p_i > 0$.
  Also, since $e^{z_i} < \sum_{j=1}^{K} e^{z_j}$ (unless $K=1$), $p_i < 1$.
- **Sum to One:** The sum of all output components is 1:
  $$ \sum_{i=1}^{K} p_i = \sum_{i=1}^{K} \frac{e^{z_i}}{\sum_{j=1}^{K} e^{z_j}} = \frac{\sum_{i=1}^{K} e^{z_i}}{\sum_{j=1}^{K} e^{z_j}} = 1 $$
  This makes the output a valid [[Probability_Distribution|probability distribution]].
- **Monotonicity:** The softmax function is monotonic with respect to its inputs. If $z_i$ increases while other $z_j$ ($j \neq i$) remain constant, then $p_i$ will increase, and all other $p_j$ will decrease (while maintaining the sum to 1).
- **Not Element-wise:** Unlike sigmoid or tanh, the softmax function is not applied element-wise independently. The calculation of each $p_i$ depends on all elements $z_j$ in the input vector due to the normalization term in the denominator.
- **Effect of Exponentiation:** The [[Exponential_Function|exponentiation]] $e^{z_i}$ serves to:
    - Make all values positive.
    - Amplify differences between input values. Larger input values $z_i$ will result in disproportionately larger $e^{z_i}$ and thus larger probabilities $p_i$. This "winner-takes-more" effect is a key characteristic.
- **Shift Invariance:** Adding a constant $C$ to all input components $z_i$ does not change the output probabilities:
  $$ \text{softmax}(z_1+C, \dots, z_K+C)_i = \frac{e^{z_i+C}}{\sum_j e^{z_j+C}} = \frac{e^{z_i}e^C}{e^C \sum_j e^{z_j}} = \frac{e^{z_i}}{\sum_j e^{z_j}} = \text{softmax}(\mathbf{z})_i $$
  This property is often used for numerical stability by subtracting the maximum value of $\mathbf{z}$ from all components before exponentiation to prevent overflow with large $z_i$: $\text{softmax}(\mathbf{z}) = \text{softmax}(\mathbf{z} - \max(\mathbf{z}))$.

## Relationship to Sigmoid
If $K=2$, the softmax function for the first component $z_1$ (with input vector $(z_1, z_2)$) can be shown to be equivalent to the logistic sigmoid function of the difference $z_1 - z_2$.
Let $z_1' = z_1 - C$ and $z_2' = z_2 - C$.
If we set $C = z_2$, then $z_1' = z_1 - z_2$ and $z_2' = 0$.
$$ p_1 = \frac{e^{z_1'}}{e^{z_1'} + e^{z_2'}} = \frac{e^{z_1-z_2}}{e^{z_1-z_2} + e^0} = \frac{e^{z_1-z_2}}{e^{z_1-z_2} + 1} = \frac{1}{1 + e^{-(z_1-z_2)}} = \sigma(z_1-z_2) $$
So, for binary classification, using a single output neuron with a sigmoid activation on its raw output $z$ is equivalent to using two output neurons with raw outputs $(z, 0)$ (or $(z_1, z_2)$ with $z=z_1-z_2$) and applying softmax.

## Applications
- **[[Multi_Class_Classification|Multi-Class Classification]] in [[Neural_Networks|Neural Networks]]:**
    - The softmax function is predominantly used as the activation function in the output layer of a neural network when the task is to classify an input into one of $K$ mutually exclusive classes.
    - The input vector $\mathbf{z}$ typically represents the raw scores (logits) computed by the network for each class.
    - The output vector $\mathbf{p}$ provides a probability distribution over the $K$ classes, where $p_i$ is interpreted as the probability that the input belongs to class $i$.
    - Example: Classifying an image as a cat, dog, or bird ($K=3$). The network outputs logits $(z_{cat}, z_{dog}, z_{bird})$. Softmax converts these into $(p_{cat}, p_{dog}, p_{bird})$ where $p_{cat}+p_{dog}+p_{bird}=1$.
- **Reinforcement Learning:**
    - Used in policy gradient methods to represent a policy, where the probabilities correspond to the likelihood of choosing each action in a given state.
    - A "softmax policy" (or Boltzmann policy) often includes a temperature parameter $\tau$:
      $$ p_i = \frac{e^{z_i/\tau}}{\sum_j e^{z_j/\tau}} $$
      - High $\tau$: Probabilities become more uniform (more exploration).
      - Low $\tau$: Probabilities become more concentrated on the action with the highest score (more exploitation, approaches [[argmax_argmin|argmax]]).
- **Attention Mechanisms (e.g., in Transformers):**
    - Softmax is used to convert raw attention scores (e.g., dot products between query and key vectors) into attention weights, which sum to 1 and indicate how much "attention" to pay to different parts of an input sequence.

## Numerical Stability
Directly computing $e^{z_i}$ can lead to numerical overflow if some $z_i$ are very large, or underflow if $z_i$ are very negative (leading to $e^{z_i} \approx 0$ and potential division by zero if all are very negative).
A common trick is to use the shift invariance property:
Let $C = \max_j(z_j)$. Then compute:
$$ p_i = \frac{e^{z_i - C}}{\sum_{j=1}^{K} e^{z_j - C}} $$
This ensures that the largest exponent is $e^0 = 1$, preventing overflow. The terms $e^{z_j-C}$ where $z_j$ is much smaller than $C$ might underflow to zero, which is generally acceptable as they contribute negligibly to the sum.

## Example Calculation
Let input logits be $\mathbf{z} = (1.0, 2.0, 0.5)$.
1.  Exponentiate:
    $e^{1.0} \approx 2.718$
    $e^{2.0} \approx 7.389$
    $e^{0.5} \approx 1.649$
2.  Sum of exponentials:
    $\sum e^{z_j} = 2.718 + 7.389 + 1.649 = 11.756$
3.  Normalize:
    $p_1 = \frac{2.718}{11.756} \approx 0.231$
    $p_2 = \frac{7.389}{11.756} \approx 0.629$
    $p_3 = \frac{1.649}{11.756} \approx 0.140$
Output probabilities: $\mathbf{p} \approx (0.231, 0.629, 0.140)$. Sum $\approx 1.0$.

>[!question] Does the softmax function return a distribution?
>Yes, the output of the softmax function is a [[Probability_Distribution|discrete probability distribution]] over $K$ categories because:
>1. Each output component $p_i$ is non-negative (in fact, $p_i > 0$).
>2. The sum of all output components $\sum_{i=1}^{K} p_i = 1$.

---