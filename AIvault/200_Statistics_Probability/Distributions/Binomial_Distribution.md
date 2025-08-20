---
tags:
  - statistics
  - probability
  - distributions
  - discrete_distribution
  - binomial
  - pmf
  - cdf
  - concept
  - scipy
aliases:
  - Binomial Distribution
related:
  - "[[200_Statistics_Probability/Distributions/Probability_Distributions_Overview|Probability Distributions Overview]]"
  - "[[Discrete_vs_Continuous_Distributions]]"
  - "[[Bernoulli_Distribution]]"
  - "[[Poisson_Distribution]]"
  - "[[Normal_Gaussian_Distribution]]"
  - "[[Relationships_Between_Probability_Distributions]]"
worksheet:
  - WS_StatsProb_1
date_created: 2025-08-20
---
# Binomial Distribution

## Definition
The **binomial distribution** is a [[Discrete_vs_Continuous_Distributions|discrete probability distribution]] that describes the number of successes in a sequence of $n$ independent experiments, each asking a yes–no question. Each experiment is a [[Bernoulli_Distribution|Bernoulli trial]] with a constant probability of success, $p$.

A random variable $X$ follows a binomial distribution if it meets the following four conditions:
1.  **Fixed number of trials ($n$):** The experiment consists of a fixed number of trials.
2.  **Independent trials:** The outcome of each trial is independent of the others.
3.  **Two possible outcomes:** Each trial has only two possible outcomes, labeled "success" and "failure."
4.  **Constant probability of success ($p$):** The probability of success is the same for each trial.

## Properties
-   **Random Variable ($X$):** The number of successes $k$ in $n$ trials. Possible values are $k \in \{0, 1, 2, \dots, n\}$.
-   **Parameters:**
    -   $n$: The number of trials (an integer $\ge 0$).
    -   $p$: The probability of success on a single trial ($0 \le p \le 1$).
-   **PMF (Probability Mass Function):** The probability of getting exactly $k$ successes in $n$ trials is given by:
    $$ P(X=k) = \binom{n}{k} p^k (1-p)^{n-k} $$
    where $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ is the binomial coefficient, representing the number of ways to choose $k$ successes from $n$ trials.
-   **Mean (Expected Value):**
    $$ E[X] = np $$
-   **Variance:**
    $$ \text{Var}(X) = np(1-p) $$

## Use Cases
-   **Quality Control:** The number of defective items in a batch of $n$ items, where each item has a probability $p$ of being defective.
-   **Marketing:** The number of people who click on an ad out of $n$ people who see it.
-   **Medicine:** The number of patients who respond to a treatment out of $n$ patients treated.
-   **Games of Chance:** The number of heads in $n$ coin flips.

## Relationship to Other Distributions
>[!question]- What is the relationship between the Poisson and the Binomial distributions?
>The [[Poisson_Distribution|Poisson distribution]] can be used as an **approximation to the Binomial distribution** under specific conditions:
>-   When the number of trials $n$ is **very large**.
>-   When the probability of success $p$ is **very small**.
>-   When the product $np = \lambda$ (the expected number of successes) is a **finite, moderate value**.
>
>A common rule of thumb is that the approximation is good if $n \ge 20$ and $p \le 0.05$, or if $n \ge 100$ and $np \le 10$.
>
>**Why?** The Poisson distribution models the number of events in a fixed interval of time or space, which can be thought of as the limit of a binomial process where the number of trials $n$ goes to infinity and the success probability $p$ goes to zero, while their product $np$ remains constant ($\lambda$). This makes calculations easier, as the binomial PMF with large $n$ can be computationally intensive due to the factorial term.

The [[Normal_Gaussian_Distribution|Normal distribution]] can also be used to approximate the binomial distribution when $n$ is large and $p$ is not too close to 0 or 1 (typically when $np > 5$ and $n(1-p) > 5$).

## SciPy Example
In `scipy.stats`, the binomial distribution is represented by `binom`.

```python
from scipy.stats import binom
import matplotlib.pyplot as plt
import numpy as np

# Example: A factory produces light bulbs. The probability of a bulb being defective is 5% (p=0.05).
# We inspect a batch of 50 bulbs (n=50).
n = 50
p = 0.05
bulb_dist = binom(n, p)

# 1. PMF: What is the probability of finding exactly 3 defective bulbs?
prob_of_3_defective = bulb_dist.pmf(k=3)
# print(f"Probability of exactly 3 defective bulbs: {prob_of_3_defective:.4f}")

# 2. CDF: What is the probability of finding 2 or fewer defective bulbs?
prob_lte_2 = bulb_dist.cdf(k=2)
# print(f"Probability of 2 or fewer defective bulbs: {prob_lte_2:.4f}")

# 3. Survival Function (SF): What is the probability of finding more than 5 defective bulbs?
# P(X > 5) = 1 - P(X <= 5)
prob_gt_5 = bulb_dist.sf(k=5)
# print(f"Probability of more than 5 defective bulbs: {prob_gt_5:.4f}")

# 4. Mean and Variance
# expected_defective = bulb_dist.mean()
# variance_defective = bulb_dist.var()
# print(f"\nExpected number of defective bulbs: {expected_defective:.2f} (np)")
# print(f"Variance: {variance_defective:.2f} (np(1-p))")

# 5. Visualize the PMF
# k_values = np.arange(0, 11) # Plot for 0 to 10 defective bulbs
# probabilities = bulb_dist.pmf(k_values)

# fig, ax = plt.subplots()
# ax.bar(k_values, probabilities, width=0.1)
# ax.set_title(f"Binomial PMF (n={n}, p={p})")
# ax.set_xlabel("Number of Defective Bulbs (k)")
# ax.set_ylabel("Probability P(X=k)")
# ax.set_xticks(k_values)
# plt.grid(axis='y', linestyle='--')
# plt.show()
```

---