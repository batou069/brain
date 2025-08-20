---
tags:
  - statistics
  - probability
  - distributions
  - pmf
  - pdf
  - cdf
  - concept
aliases:
  - Probability Mass Function
  - Probability Density Function
  - Cumulative Distribution Function
related:
  - "[[200_Statistics_Probability/Distributions/Probability_Distributions_Overview|Probability Distributions Overview]]"
  - "[[Discrete_vs_Continuous_Distributions]]"
worksheet:
  - WS_StatsProb_1
date_created: 2025-08-20
---
# PMF, PDF, and CDF

These three functions are fundamental ways to describe and work with probability distributions.

## PMF (Probability Mass Function)
-   **Applies to:** [[Discrete_vs_Continuous_Distributions|Discrete Random Variables]].
-   **Definition:** A function that gives the probability that a discrete random variable is exactly equal to some value.
-   **Notation:** $p(x) = P(X=x)$.
-   **Properties:**
    1.  $0 \le p(x) \le 1$ for any value $x$.
    2.  The sum of the probabilities over all possible values must equal 1: $\sum_{\text{all } x} p(x) = 1$.
-   **Example (Fair Die Roll):**
    -   The random variable $X$ is the outcome of the roll. Possible values are $\{1, 2, 3, 4, 5, 6\}$.
    -   The PMF is $P(X=k) = 1/6$ for $k \in \{1, 2, 3, 4, 5, 6\}$, and $P(X=k) = 0$ otherwise.
-   **Visualization:** A bar chart or stick plot.

## PDF (Probability Density Function)
-   **Applies to:** [[Discrete_vs_Continuous_Distributions|Continuous Random Variables]].
-   **Definition:** A function whose value at any given sample (or point) in the sample space can be interpreted as providing a *relative likelihood* that the value of the random variable would be close to that sample.
-   **Notation:** $f(x)$ or $p(x)$.
-   **Properties:**
    1.  $f(x) \ge 0$ for all $x$.
    2.  The total area under the curve of the function must equal 1: $\int_{-\infty}^{\infty} f(x) \,dx = 1$.
-   **Important Note:** For a continuous variable, the value of the PDF at a specific point, $f(x)$, is **not a probability**. The probability of a continuous random variable taking on any single specific value is zero, i.e., $P(X=x) = 0$.
-   **Calculating Probability:** Probability is found by integrating the PDF over an interval. The probability that $X$ falls between $a$ and $b$ is $P(a \le X \le b) = \int_{a}^{b} f(x) \,dx$.
-   **Example ([[Normal_Gaussian_Distribution|Normal Distribution]]):** The classic "bell curve" is a PDF.
-   **Visualization:** A smooth curve.

## CDF (Cumulative Distribution Function)
-   **Applies to:** Both Discrete and Continuous Random Variables.
-   **Definition:** A function that gives the probability that a random variable $X$ will take a value **less than or equal to** a specific value $x$.
-   **Notation:** $F(x) = P(X \le x)$.
-   **Properties:**
    1.  $0 \le F(x) \le 1$.
    2.  It is a non-decreasing function (i.e., if $a < b$, then $F(a) \le F(b)$).
    3.  $\lim_{x \to -\infty} F(x) = 0$.
    4.  $\lim_{x \to \infty} F(x) = 1$.
-   **Relationship to PMF/PDF:**
    -   For a discrete variable: $F(x) = \sum_{k \le x} P(X=k)$. The CDF is a step function.
    -   For a continuous variable: $F(x) = \int_{-\infty}^{x} f(t) \,dt$. The PDF is the derivative of the CDF: $f(x) = \frac{d}{dx}F(x)$.
-   **Usefulness:** The CDF is often very useful for calculating probabilities over ranges:
    -   $P(X > x) = 1 - P(X \le x) = 1 - F(x)$. (This is also called the Survival Function, `sf` in `scipy.stats`).
    -   $P(a < X \le b) = F(b) - F(a)$.

## Summary Table

[list2mdtable|#Function Comparison]
- Function
    - Applies To
        - Output Interpretation
            - Key Property
- **PMF**
    - Discrete RVs
        - $P(X=x)$, the probability of an exact outcome.
            - $\sum p(x) = 1$
- **PDF**
    - Continuous RVs
        - $f(x)$, the probability density (relative likelihood). Not a probability.
            - $\int f(x) \,dx = 1$
- **CDF**
    - Both Discrete and Continuous RVs
        - $P(X \le x)$, the cumulative probability up to a point.
            - Non-decreasing from 0 to 1.

## SciPy Example
The [[160_Python_Libraries/SciPy_Stats_Module|`scipy.stats`]] module provides these functions for its distribution objects.

```python
from scipy.stats import binom, norm

# --- Discrete Example: Binomial Distribution ---
# PMF: Probability of getting exactly 7 successes in 10 trials if p=0.8
prob_7_successes = binom.pmf(k=7, n=10, p=0.8)
# print(f"Binomial PMF P(X=7): {prob_7_successes:.4f}")

# CDF: Probability of getting 7 or fewer successes
prob_lte_7 = binom.cdf(k=7, n=10, p=0.8)
# print(f"Binomial CDF P(X<=7): {prob_lte_7:.4f}")


# --- Continuous Example: Normal Distribution ---
# PDF: Density at the mean (x=100) for a distribution with mean=100, std=15
density_at_mean = norm.pdf(x=100, loc=100, scale=15)
# print(f"\nNormal PDF at x=100: {density_at_mean:.4f}")

# CDF: Probability of observing a value of 115 or less
prob_lte_115 = norm.cdf(x=115, loc=100, scale=15)
# print(f"Normal CDF P(X<=115): {prob_lte_115:.4f}") # Corresponds to one std dev above mean

# Probability of being between 85 and 115
prob_between = norm.cdf(x=115, loc=100, scale=15) - norm.cdf(x=85, loc=100, scale=15)
# print(f"Normal P(85 < X <= 115): {prob_between:.4f}") # Should be ~68%
```

---