---
tags:
  - statistics
  - probability
  - distributions
  - discrete_distribution
  - bernoulli
  - pmf
  - cdf
  - concept
  - scipy
aliases:
  - Bernoulli Trial
  - Bernoulli Distribution
related:
  - "[[200_Statistics_Probability/Distributions/Probability_Distributions_Overview|Probability Distributions Overview]]"
  - "[[Discrete_vs_Continuous_Distributions]]"
  - "[[Binomial_Distribution]]"
worksheet:
  - WS_StatsProb_1
date_created: 2025-08-20
---
# Bernoulli Distribution

## Definition
The **Bernoulli distribution** is a [[Discrete_vs_Continuous_Distributions|discrete probability distribution]] for a random variable which takes the value 1 with probability $p$ and the value 0 with probability $q = 1-p$. It represents the outcome of a single **Bernoulli trial**, which is a random experiment with exactly two possible outcomes: "success" and "failure".

-   Success is typically coded as 1.
-   Failure is typically coded as 0.

## Properties
-   **Random Variable ($X$):** Can take on two values, $\{0, 1\}$.
-   **Parameter:** $p$, the probability of success, where $0 \le p \le 1$.
-   **PMF (Probability Mass Function):**
    $$
    P(X=k) =
    \begin{cases}
    p & \text{if } k=1 \text{ (success)} \\
    1-p & \text{if } k=0 \text{ (failure)}
    \end{cases}
    $$
    This can be written compactly as:
    $$ P(X=k) = p^k (1-p)^{1-k} \quad \text{for } k \in \{0, 1\} $$
-   **Mean (Expected Value):**
    $$ E[X] = 1 \cdot p + 0 \cdot (1-p) = p $$
-   **Variance:**
    $$ \text{Var}(X) = p(1-p) $$

## Use Cases
The Bernoulli distribution is the fundamental building block for more complex discrete distributions.
-   **Modeling Single Binary Events:**
    -   A single coin flip (Heads/Tails).
    -   Whether a single customer clicks on an ad (Click/No Click).
    -   Whether a single product from an assembly line is defective or not.
    -   Whether a single email is spam or not spam.
-   **Foundation for Other Distributions:**
    -   The [[Binomial_Distribution|Binomial distribution]] models the number of successes in a fixed number of independent Bernoulli trials.
    -   The Geometric distribution models the number of Bernoulli trials needed to get one success.
    -   The Negative Binomial distribution models the number of Bernoulli trials needed to get a specified number of successes.

## SciPy Example
In `scipy.stats`, the Bernoulli distribution is represented by `bernoulli`.

```python
from scipy.stats import bernoulli
import matplotlib.pyplot as plt
import numpy as np

# A Bernoulli trial representing a biased coin flip
# p = probability of success (e.g., Heads, coded as 1)
p_success = 0.7
coin_flip_dist = bernoulli(p_success)

# 1. PMF: Probability of getting a success (1) or failure (0)
prob_of_success = coin_flip_dist.pmf(k=1)
prob_of_failure = coin_flip_dist.pmf(k=0)
# print(f"Probability of Success (k=1): {prob_of_success:.2f}")
# print(f"Probability of Failure (k=0): {prob_of_failure:.2f}")

# 2. RVS: Generate 20 random outcomes from this distribution
random_flips = coin_flip_dist.rvs(size=20)
# print(f"\n20 random trials (1=Success, 0=Failure): {random_flips}")
# num_successes = np.sum(random_flips)
# print(f"Total successes in 20 trials: {num_successes}")

# 3. Mean and Variance
# theoretical_mean = coin_flip_dist.mean()
# theoretical_variance = coin_flip_dist.var()
# print(f"\nTheoretical Mean: {theoretical_mean:.2f} (p)")
# print(f"Theoretical Variance: {theoretical_variance:.2f} (p*(1-p))")

# 4. Visualize the PMF
# outcomes =
# probabilities = [coin_flip_dist.pmf(k=0), coin_flip_dist.pmf(k=1)]

# fig, ax = plt.subplots()
# ax.bar(outcomes, probabilities, width=0.1, tick_label=["Failure (0)", "Success (1)"])
# ax.set_title(f"PMF of a Bernoulli Distribution (p={p_success})")
# ax.set_xlabel("Outcome")
# ax.set_ylabel("Probability P(X=k)")
# ax.set_ylim(0, 1)
# plt.grid(axis='y', linestyle='--')
# plt.show()
```

---