---
tags:
  - statistics
  - probability
  - distributions
  - continuous_distribution
  - normal_distribution
  - gaussian
  - bell_curve
  - clt
  - pdf
  - cdf
  - concept
  - scipy
aliases:
  - Normal Distribution
  - Gaussian Distribution
  - Bell Curve
related:
  - "[[200_Statistics_Probability/Distributions/Probability_Distributions_Overview|Probability Distributions Overview]]"
  - "[[Continuous_vs_Discrete_Distributions]]"
  - "[[Central_Limit_Theorem_CLT]]"
  - "[[Standard_Normal_Distribution_Z_Score]]"
  - "[[Relationships_Between_Probability_Distributions]]"
worksheet:
  - WS_StatsProb_1
date_created: 2025-08-20
---
# Normal (Gaussian) Distribution

## Definition
The **Normal distribution**, also known as the **Gaussian distribution** or the **bell curve**, is a [[Continuous_vs_Discrete_Distributions|continuous probability distribution]] that is symmetric about its mean. It is one of the most important distributions in statistics and probability theory.

Its importance stems largely from the [[Central_Limit_Theorem_CLT|Central Limit Theorem (CLT)]], which states that the sum (or average) of a large number of independent, identically distributed random variables will be approximately normally distributed, regardless of the underlying distribution.

## Properties
-   **Random Variable ($X$):** A continuous variable over the entire real line $(-\infty, \infty)$.
-   **Parameters:**
    -   **Mean ($\mu$):** The center of the distribution (also its median and mode). It determines the location of the peak.
    -   **Standard Deviation ($\sigma$):** A measure of the spread or width of the distribution. A larger $\sigma$ results in a wider, flatter curve. The variance is $\sigma^2$.
-   **PDF (Probability Density Function):**
    $$ f(x | \mu, \sigma) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2} $$
-   **Shape:** Symmetrical, unimodal, and bell-shaped.
-   **Empirical Rule (68-95-99.7 Rule):** For a normal distribution:
    -   Approximately **68%** of the data falls within 1 standard deviation of the mean ($\mu \pm \sigma$).
    -   Approximately **95%** of the data falls within 2 standard deviations of the mean ($\mu \pm 2\sigma$).
    -   Approximately **99.7%** of the data falls within 3 standard deviations of the mean ($\mu \pm 3\sigma$).
-   **[[Standard_Normal_Distribution_Z_Score|Standard Normal Distribution]]:** A special case where $\mu=0$ and $\sigma=1$. Any normal distribution can be converted to a standard normal distribution using the Z-score transformation: $Z = \frac{X-\mu}{\sigma}$.

>[!question]- If the height (cm) of a certain human population follows a Gaussian distribution with μ=170 and σ=10, then p(height < 0) > 0. How can it be?
>This is an excellent question that highlights the difference between a **mathematical model** and **physical reality**.
>
>1.  **The Model's Domain:** The mathematical formula for the normal distribution is defined for all real numbers, from $-\infty$ to $+\infty$. The tails of the bell curve never truly touch the x-axis, so for any normal distribution, there is a non-zero (though often infinitesimally small) probability density for any value, including negative values.
>2.  **Physical Impossibility:** We know that height cannot be negative. A person's height must be greater than zero.
>3.  **The Resolution:** The normal distribution is being used as a **model** to approximate the real-world distribution of heights. For the given parameters ($\mu=170, \sigma=10$):
>    -   A height of 0 is 17 standard deviations below the mean ($Z = (0-170)/10 = -17$).
>    -   The probability of observing a value more than 17 standard deviations away from the mean is astronomically small. Using `scipy.stats.norm.cdf(0, loc=170, scale=10)`, the probability is approximately $1.12 \times 10^{-64}$.
>
>So, while the mathematical model assigns a tiny, non-zero probability to negative heights, this probability is so close to zero that it is practically and physically negligible. The normal distribution is still an excellent and useful model for height because its density in the physically impossible range (height < 0) is effectively zero. It's a case where the model is "wrong" in a way that doesn't matter for any practical purpose.

## Use Cases
-   **Natural Phenomena:** Many natural measurements tend to follow a normal distribution (e.g., height, weight, blood pressure, measurement errors).
-   **Statistical Inference:** It is the foundation for many hypothesis tests (t-tests, Z-tests, ANOVA) and for constructing confidence intervals, thanks to the CLT.
-   **Machine Learning:**
    -   Assumption for some models (e.g., Linear Discriminant Analysis, Gaussian Naive Bayes).
    -   Errors (residuals) in linear regression are often assumed to be normally distributed.
    -   Used in Gaussian Mixture Models for clustering.
    -   Used for weight initialization in neural networks.
-   **Finance:** Modeling asset returns (though often with "fat tails" not perfectly captured by a normal distribution).

## SciPy Example
In `scipy.stats`, the normal distribution is represented by `norm`.

>[!question]- The height (cm) of a certain human population follows a Gaussian distribution with μ=170 and σ=10. What is the probability that one randomly picked person measures between 190 and 200?
>
>We need to calculate $P(190 < X \le 200)$. This can be found using the CDF: $P(190 < X \le 200) = P(X \le 200) - P(X \le 190) = F(200) - F(190)$.
>
>```python
>from scipy.stats import norm
>
>mu = 170
>sigma = 10
>
># Probability of being between 190 and 200 cm
>prob_le_200 = norm.cdf(200, loc=mu, scale=sigma) # P(X <= 200)
>prob_le_190 = norm.cdf(190, loc=mu, scale=sigma) # P(X <= 190)
>
>prob_between_190_200 = prob_le_200 - prob_le_190
>
># print(f"P(X <= 200) = {prob_le_200:.4f}")
># print(f"P(X <= 190) = {prob_le_190:.4f}")
># print(f"The probability of a person's height being between 190cm and 200cm is: {prob_between_190_200:.4f} (or {prob_between_190_200*100:.2f}%)")
># Expected output: approx. 0.0214 or 2.14%
>```

## Visualization
```python
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

mu = 170
sigma = 10
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
pdf_values = norm.pdf(x, loc=mu, scale=sigma)

fig, ax = plt.subplots()
ax.plot(x, pdf_values, label=f'N(μ={mu}, σ={sigma})')
ax.set_title("Normal Distribution PDF")
ax.set_xlabel("Height (cm)")
ax.set_ylabel("Probability Density")

# Shade the area for the question P(190 < X < 200)
x_fill = np.linspace(190, 200, 100)
y_fill = norm.pdf(x_fill, loc=mu, scale=sigma)
ax.fill_between(x_fill, y_fill, color='skyblue', alpha=0.5, label='P(190 < X < 200)')

ax.legend()
plt.grid(True, linestyle='--')
plt.show()
```

---