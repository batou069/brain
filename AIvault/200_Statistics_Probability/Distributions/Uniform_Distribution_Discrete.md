---
tags:
  - statistics
  - probability
  - distributions
  - discrete_distribution
  - uniform_distribution
  - pmf
  - cdf
  - concept
  - scipy
aliases:
  - Discrete Uniform Distribution
related:
  - "[[200_Statistics_Probability/Distributions/Probability_Distributions_Overview|Probability Distributions Overview]]"
  - "[[Discrete_vs_Continuous_Distributions]]"
  - "[[Uniform_Distribution_Continuous]]"
worksheet:
  - WS_StatsProb_1
date_created: 2025-08-20
---
# Uniform Distribution (Discrete)

## Definition
The **discrete uniform distribution** is a probability distribution where a finite number of values are equally likely to be observed. Every one of the $n$ values has an equal probability of $1/n$.

A simple example is a fair six-sided die roll, where the possible outcomes are $\{1, 2, 3, 4, 5, 6\}$, and each outcome has a probability of $1/6$.

## Properties
-   **Random Variable ($X$):** Can take on $n$ distinct values, say $\{x_1, x_2, \dots, x_n\}$.
-   **Parameters:** The set of possible values. Often, for integers, it's defined by a lower bound $a$ and an upper bound $b$. The number of values is $n = b - a + 1$.
-   **PMF (Probability Mass Function):**
    $$ P(X=k) = \frac{1}{n} $$
    for each of the $n$ possible values $k$.
-   **Mean (Expected Value):**
    $$ E[X] = \frac{a+b}{2} $$
    (For integer range $[a,b]$)
-   **Variance:**
    $$ \text{Var}(X) = \frac{n^2 - 1}{12} = \frac{(b-a+1)^2 - 1}{12} $$
    (For integer range $[a,b]$)

>[!question]- Why does the uniform distribution have both a PMF and a PDF?
>This is a common point of confusion. A single "uniform distribution" does not have both a PMF and a PDF. Rather, there are **two different types** of uniform distributions:
>1.  **[[Uniform_Distribution_Discrete|Discrete Uniform Distribution]]:** Applies to [[Discrete_vs_Continuous_Distributions|discrete random variables]] (countable outcomes). It is described by a **PMF**. Example: Rolling a die.
>2.  **[[Uniform_Distribution_Continuous|Continuous Uniform Distribution]]:** Applies to [[Discrete_vs_Continuous_Distributions|continuous random variables]] (outcomes in a range). It is described by a **PDF**. Example: A random number generator producing a float between 0.0 and 1.0.
>
>So, the concept of "uniformity" (all outcomes being equally likely) can be applied to both discrete and continuous cases, resulting in two distinct distributions, each with its appropriate probability function (PMF for discrete, PDF for continuous).

## Use Cases
-   **Modeling Equiprobable Outcomes:** Ideal for situations where all possible outcomes are assumed to be equally likely (e.g., fair coin flips, die rolls, lottery draws, card games).
-   **Generating Random Integers:** Computer programs often use this distribution to generate random integers within a specified range.
-   **Default Prior in Bayesian Statistics:** When there is no prior knowledge to favor any particular parameter value, a discrete uniform distribution might be used as an uninformative prior.
-   **Sampling:** Used as a basis for simple random sampling.

## SciPy Example
In `scipy.stats`, the discrete uniform distribution is represented by `randint`.

```python
from scipy.stats import randint
import matplotlib.pyplot as plt
import numpy as np

# A discrete uniform distribution for a fair six-sided die
# The range is [low, high), so for 1-6 we use low=1, high=7.
low = 1
high = 7
n = high - low
die_dist = randint(low, high)

# 1. PMF: Probability of rolling a specific number (e.g., 3)
prob_of_3 = die_dist.pmf(k=3)
# print(f"Probability of rolling a 3: {prob_of_3:.4f} (Expected: {1/n:.4f})")

# 2. CDF: Probability of rolling a 4 or less
prob_lte_4 = die_dist.cdf(k=4)
# print(f"Probability of rolling <= 4: {prob_lte_4:.4f} (Expected: 4/6)")

# 3. RVS: Generate 20 random die rolls
random_rolls = die_dist.rvs(size=20)
# print(f"\n20 random die rolls: {random_rolls}")

# 4. Visualize the PMF
# possible_outcomes = np.arange(low, high)
# probabilities = die_dist.pmf(possible_outcomes)

# fig, ax = plt.subplots()
# ax.bar(possible_outcomes, probabilities, width=0.1)
# ax.set_title(f"PMF of a Discrete Uniform Distribution (n={n})")
# ax.set_xlabel("Outcome (Die Roll)")
# ax.set_ylabel("Probability P(X=k)")
# ax.set_ylim(0, 0.2)
# ax.set_xticks(possible_outcomes)
# plt.grid(axis='y', linestyle='--')
# plt.show()
```

---