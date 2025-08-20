---
tags:
  - python
  - library
  - scipy
  - scipy_stats
  - statistics
  - probability
  - distributions
  - hypothesis_testing
  - concept
  - example
aliases:
  - scipy.stats
  - SciPy Statistics
related:
  - "[[160_Python_Libraries/SciPy_Library|SciPy Library]]"
  - "[[200_Statistics_Probability/_Statistics_Probability_MOC|_Statistics_Probability_MOC]]"
  - "[[Probability_Distributions_Overview]]"
  - "[[Hypothesis_Testing]]"
worksheet:
  - WS_StatsProb_1
date_created: 2025-08-20
---
# SciPy: Statistical Functions (`scipy.stats`)

The `scipy.stats` module is a comprehensive sub-package of the [[SciPy_Library|SciPy library]] containing a large number of probability distributions and a growing library of statistical functions. It is an essential tool for data scientists and researchers working with Python.

## Core Functionality
-   **Probability Distributions:** Provides objects for a vast array of continuous and discrete probability distributions (e.g., normal, uniform, binomial, poisson).
-   **Descriptive Statistics:** Functions for calculating summary statistics (e.g., mean, variance, skewness, kurtosis).
-   **Statistical Tests (Inferential Statistics):** A wide range of hypothesis tests (e.g., t-tests, ANOVA, Kolmogorov-Smirnov test, Chi-squared test).
-   **Correlation Functions:** Functions to calculate correlation coefficients.
-   **Parameter Estimation:** Includes tools like `fit()` to estimate distribution parameters from data.

## Working with Probability Distributions
A key feature of `scipy.stats` is its consistent API for working with probability distributions. For a given distribution object (e.g., `scipy.stats.norm`), you have access to several common methods:

[list2tab|#Distribution Methods]
- `rvs()` (Random Variates)
    -   **Purpose:** Generate random samples from the distribution.
    -   **Syntax:** `dist.rvs(param1, param2, ..., size=N)`
    -   **Example:** `norm.rvs(loc=170, scale=10, size=100)` generates 100 random samples from a normal distribution with mean 170 and std dev 10.
- `pdf()` (Probability Density Function)
    -   **Purpose:** For **continuous** distributions, evaluates the probability density at a given point. The value is not a probability itself, but represents relative likelihood.
    -   **Syntax:** `dist.pdf(x, param1, param2, ...)`
    -   **Example:** `norm.pdf(170, loc=170, scale=10)` gives the height of the bell curve at its peak.
- `pmf()` (Probability Mass Function)
    -   **Purpose:** For **discrete** distributions, gives the probability of observing a specific value.
    -   **Syntax:** `dist.pmf(k, param1, param2, ...)`
    -   **Example:** `poisson.pmf(k=3, mu=5)` gives the probability of observing exactly 3 events if the average rate is 5.
- `cdf()` (Cumulative Distribution Function)
    -   **Purpose:** For any distribution, gives the probability of observing a value **less than or equal to** a given point, $P(X \le x)$.
    -   **Syntax:** `dist.cdf(x, param1, param2, ...)`
    -   **Example:** `norm.cdf(170, loc=170, scale=10)` returns 0.5, as 50% of the distribution is less than or equal to the mean.
- `sf()` (Survival Function)
    -   **Purpose:** Gives the probability of observing a value **greater than** a given point, $P(X > x)$. It is equivalent to `1 - cdf(x)`.
    -   **Syntax:** `dist.sf(x, param1, param2, ...)`
    -   **Example:** `norm.sf(170, loc=170, scale=10)` returns 0.5.
- `ppf()` (Percent Point Function)
    -   **Purpose:** The inverse of the CDF. Given a probability (quantile) $q$, it returns the value $x$ such that $P(X \le x) = q$.
    -   **Syntax:** `dist.ppf(q, param1, param2, ...)`
    -   **Example:** `norm.ppf(0.95, loc=0, scale=1)` returns approx. 1.645, the z-score for the 95th percentile.
- `fit()`
    -   **Purpose:** Estimates the distribution's parameters (e.g., mean, standard deviation) from a given dataset.
    -   **Syntax:** `dist.fit(data)`
    -   **Example:** `loc, scale = norm.fit(my_data_array)` estimates the mean and standard deviation from `my_data_array`.
- `mean()`, `median()`, `var()`, `std()`
    -   **Purpose:** Returns the theoretical mean, median, variance, or standard deviation of the distribution given its parameters.

## Example: Using the Normal Distribution (`scipy.stats.norm`)
```python
from scipy.stats import norm
import numpy as np

# Define a normal distribution for human heights: mean=170cm, std=10cm
mu = 170
sigma = 10
height_dist = norm(loc=mu, scale=sigma)

# 1. Generate 5 random heights from this distribution
random_heights = height_dist.rvs(size=5)
# print(f"Random heights: {np.round(random_heights, 2)}")

# 2. What is the probability density at 175cm?
# pdf_at_175 = height_dist.pdf(175)
# print(f"PDF at 175cm: {pdf_at_175:.4f}")

# 3. What is the probability a person is shorter than or equal to 180cm? (CDF)
prob_shorter_than_180 = height_dist.cdf(180)
# print(f"P(height <= 180cm): {prob_shorter_than_180:.4f}")

# 4. What is the probability a person is taller than 190cm? (Survival Function)
prob_taller_than_190 = height_dist.sf(190)
# print(f"P(height > 190cm): {prob_taller_than_190:.4f}")

# 5. What height corresponds to the 90th percentile? (PPF)
height_90th_percentile = height_dist.ppf(0.90)
# print(f"90th percentile height: {height_90th_percentile:.2f} cm")

# 6. Fit parameters from a sample dataset
# sample_data = norm.rvs(loc=172, scale=12, size=1000) # Generate some sample data
# estimated_mu, estimated_sigma = norm.fit(sample_data)
# print(f"Estimated mean from data: {estimated_mu:.2f} (True was 172)")
# print(f"Estimated std dev from data: {estimated_sigma:.2f} (True was 12)")
```

## Example: Statistical Test (`ttest_ind`)
```python
from scipy.stats import ttest_ind, norm

# Create two samples of product ratings
# Group A used the old product design, Group B used the new one
group_a_ratings = norm.rvs(loc=3.5, scale=0.8, size=50, random_state=42)
group_b_ratings = norm.rvs(loc=3.9, scale=0.8, size=50, random_state=101)

# Perform an independent t-test to see if the means are significantly different
# t_statistic, p_value = ttest_ind(group_a_ratings, group_b_ratings)

# print(f"T-test results:")
# print(f"  T-statistic: {t_statistic:.4f}")
# print(f"  P-value: {p_value:.4f}")

# if p_value < 0.05:
#     print("The difference in mean ratings is statistically significant (p < 0.05).")
# else:
#     print("The difference in mean ratings is not statistically significant (p >= 0.05).")
```

The `scipy.stats` module is an indispensable tool for performing statistical analysis, working with probability distributions, and conducting hypothesis tests in Python.

---