---
tags:
  - statistics
  - probability
  - distributions
  - continuous_distribution
  - power_law
  - pareto
  - scale_free
  - concept
  - scipy
aliases:
  - Power Law
  - Scale-Free Distribution
  - Pareto Distribution
related:
  - "[[200_Statistics_Probability/Distributions/Probability_Distributions_Overview|Probability Distributions Overview]]"
  - "[[Continuous_vs_Discrete_Distributions]]"
  - "[[Logarithmic_Function]]"
worksheet:
  - WS_StatsProb_1
date_created: 2025-08-20
---
# Power-Law Distribution

## Definition
A **power-law distribution** is a probability distribution where the frequency of an event varies as a power of some attribute of that event. In other words, a quantity $x$ is said to be power-law distributed if its probability density function (PDF) (for continuous variables) or probability mass function (PMF) (for discrete variables) has the form:
$$ p(x) \propto x^{-\alpha} $$
where:
-   $x$ is the quantity of interest.
-   $\alpha$ is a constant parameter of the distribution known as the **exponent** or **scaling parameter**.
-   $\propto$ means "is proportional to."

The key characteristic is that a small number of items are ranked "high" (have a high value of $x$) and occur with low frequency, while a large number of items are ranked "low" (have a low value of $x$) and occur with high frequency. This leads to a very long or "heavy" tail in the distribution.

## Key Characteristics
-   **Scale-Free:** Power-law distributions are "scale-free" or "scale-invariant." This means there is no characteristic scale or "typical" size for an event. If you "zoom in" on a portion of the distribution, its shape remains statistically similar.
-   **Heavy/Fat Tails:** The tail of the distribution decays much more slowly than that of an exponential or normal distribution. This means that extremely large events, while rare, are much more probable than they would be under a normal distribution.
-   **Mean and Variance:** Depending on the value of the exponent $\alpha$, the mean and variance of a power-law distribution can be infinite (undefined).
    -   If $\alpha \le 2$, the variance is infinite.
    -   If $\alpha \le 1$, the mean is also infinite.
-   **80/20 Rule (Pareto Principle):** The Pareto distribution, a specific type of power-law distribution, is often associated with the "80/20 rule," where roughly 80% of the effects come from 20% of the causes (e.g., 80% of wealth is held by 20% of the population).

>[!question]- How can you visually see exponential and power-law relationships in your data?
>A standard linear-scale plot can be misleading for these distributions. The best way to visually identify them is by using **log-log** or **semi-log** plots.
>
>1.  **[[Exponential_Distribution_Probability|Exponential Distribution]]:**
>    -   An exponential relationship of the form $y = Ae^{-\lambda x}$ becomes linear on a **semi-log plot** (logarithmic y-axis, linear x-axis).
>    -   Taking the log of both sides: $\ln(y) = \ln(A) - \lambda x$. This is the equation of a straight line ($Y = C - \lambda x$) where $Y = \ln(y)$.
>    -   **Visual Test:** If you plot your data's frequency or probability density on a log scale against the value on a linear scale and it forms a straight line, the distribution is likely exponential.
>
>2.  **Power-Law Distribution:**
>    -   A power-law relationship of the form $p(x) = C x^{-\alpha}$ becomes linear on a **log-log plot** (both axes are logarithmic).
>    -   Taking the log of both sides: $\ln(p(x)) = \ln(C) - \alpha \ln(x)$. This is the equation of a straight line ($Y = C' - \alpha X$) where $Y = \ln(p(x))$ and $X = \ln(x)$.
>    -   **Visual Test:** If you plot your data's frequency or probability density against the value on log-log axes and it forms a straight line, the distribution is likely a power-law. The slope of this line corresponds to the negative exponent, $-\alpha$.

## Use Cases (Where Power-Laws Appear)
Power-law distributions are found in a surprisingly large number of natural and man-made phenomena:
-   **Economics:** Distribution of wealth (Pareto distribution).
-   **Linguistics:** Frequency of words in a language (Zipf's law).
-   **Urban Studies:** Population of cities.
-   **Social Networks:** The number of connections (degree) of nodes in many real-world networks. A few nodes (hubs) have a huge number of connections, while most have very few.
-   **Internet:** Number of links pointing to a web page, size of web files.
-   **Geophysics:** Magnitude of earthquakes (Gutenberg-Richter law).
-   **Biology:** Number of species per genus.
-   **Finance:** Size of price fluctuations in financial markets.

## SciPy Example (Pareto Distribution)
The Pareto distribution is a classic power-law distribution. In `scipy.stats`, it's represented by `pareto`. The parameter `b` in `scipy.stats.pareto` corresponds to the exponent $\alpha$.

```python
from scipy.stats import pareto
import matplotlib.pyplot as plt
import numpy as np

# Pareto distribution with exponent b=2.62 (often used for wealth)
# The 'scale' parameter here sets the minimum value xm.
b_exponent = 2.62
scale_min_val = 1.0 # Minimum value (e.g., $1)
pareto_dist = pareto(b=b_exponent, scale=scale_min_val)

# Generate 1000 random samples
samples = pareto_dist.rvs(size=1000)

# Visualize on linear and log-log scales
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# 1. Linear Scale Plot (Histogram)
# ax1.hist(samples, bins=100, range=) # Limit range to see detail, as tail is long
# ax1.set_title("Histogram of Pareto Data (Linear Scale)")
# ax1.set_xlabel("Value")
# ax1.set_ylabel("Frequency")

# 2. Log-Log Scale Plot
# To create a log-log plot of the PDF, we need to bin the data logarithmically
# or plot the survival function (1 - CDF), which also follows a power law.
# Plotting the survival function (P(X > x)) is often clearer.
# sorted_samples = np.sort(samples)
# survival_prob = 1 - np.arange(1, len(sorted_samples) + 1) / len(sorted_samples)

# ax2.plot(sorted_samples, survival_prob)
# ax2.set_xscale('log')
# ax2.set_yscale('log')
# ax2.set_title("Survival Function (Log-Log Scale)")
# ax2.set_xlabel("Value (log scale)")
# ax2.set_ylabel("P(X > x) (log scale)")
# ax2.grid(True, which="both", ls="--")

# plt.tight_layout()
# plt.show()
```
> The log-log plot of the survival function (or a log-binned histogram) will appear as a straight line, confirming the power-law nature of the data.

---