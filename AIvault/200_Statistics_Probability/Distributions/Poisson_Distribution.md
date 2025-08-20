---
tags:
  - statistics
  - probability
  - distributions
  - discrete_distribution
  - poisson
  - pmf
  - cdf
  - concept
  - scipy
aliases:
  - Poisson Distribution
related:
  - "[[200_Statistics_Probability/Distributions/Probability_Distributions_Overview|Probability Distributions Overview]]"
  - "[[Discrete_vs_Continuous_Distributions]]"
  - "[[Binomial_Distribution]]"
  - "[[Exponential_Distribution_Probability]]"
  - "[[Relationships_Between_Probability_Distributions]]"
worksheet:
  - WS_StatsProb_1
date_created: 2025-08-20
---
# Poisson Distribution

## Definition
The **Poisson distribution** is a [[Discrete_vs_Continuous_Distributions|discrete probability distribution]] that expresses the probability of a given number of events occurring in a fixed interval of time or space, if these events occur with a known constant mean rate and independently of the time since the last event.

It is often used to model **count data**.

## Conditions for a Poisson Process
A random variable follows a Poisson distribution if the underlying process meets these conditions:
1.  Events occur independently. The occurrence of one event does not affect the probability of another event occurring.
2.  The average rate at which events occur is constant for the interval of interest.
3.  Two events cannot occur at exactly the same instant in time or point in space.
4.  The probability of an event occurring in a very small interval is proportional to the length of the interval.

## Properties
-   **Random Variable ($X$):** The number of events $k$ in a given interval. Possible values are $k \in \{0, 1, 2, \dots, \infty\}$.
-   **Parameter:**
    -   **Rate parameter ($\lambda$ or $\mu$):** The average number of events in the given interval. $\lambda > 0$.
-   **PMF (Probability Mass Function):** The probability of observing exactly $k$ events in an interval is given by:
    $$ P(X=k) = \frac{\lambda^k e^{-\lambda}}{k!} $$
    where $e$ is [[Euler_Number_e|Euler's number]] and $k!$ is the factorial of $k$.
-   **Mean (Expected Value):**
    $$ E[X] = \lambda $$
-   **Variance:**
    $$ \text{Var}(X) = \lambda $$
    A key property of the Poisson distribution is that its mean and variance are equal.

## Use Cases
-   **Queuing Theory:** The number of customers arriving at a service center in an hour.
-   **Telecommunications:** The number of phone calls received by a call center per minute.
-   **Biology:** The number of mutations on a strand of DNA per unit length.
-   **Physics:** The number of radioactive particles decaying in a given time interval.
-   **Insurance:** The number of insurance claims filed per month.
-   **Web Analytics:** The number of visitors to a website in a given hour.

## Relationship to Other Distributions
>[!question]- What is the relationship between the Poisson and the Binomial distributions?
>The Poisson distribution is the limiting case of the [[Binomial_Distribution|Binomial distribution]] when the number of trials $n$ is very large, the probability of success $p$ is very small, and the product $np = \lambda$ is a finite constant. See [[Binomial_Distribution]] for more details.

>[!question]- What is the relationship between the Exponential distribution and the Poisson distribution?
>They describe the same underlying process (a Poisson process) from different perspectives. If the number of events in an interval follows a Poisson distribution with rate $\lambda$, then the waiting time between those events follows an [[Exponential_Distribution_Probability|Exponential distribution]] with the same rate $\lambda$.

## SciPy Example
In `scipy.stats`, the Poisson distribution is represented by `poisson`. The main parameter is `mu` (which corresponds to $\lambda$).

```python
from scipy.stats import poisson
import matplotlib.pyplot as plt
import numpy as np

# Example: A customer support center receives an average of 5 emails per hour (mu=5).
mu_rate = 5
email_dist = poisson(mu=mu_rate)

# 1. PMF: What is the probability of receiving exactly 3 emails in the next hour?
prob_of_3_emails = email_dist.pmf(k=3)
# print(f"Probability of exactly 3 emails: {prob_of_3_emails:.4f}")

# 2. CDF: What is the probability of receiving 2 or fewer emails?
prob_lte_2 = email_dist.cdf(k=2)
# print(f"Probability of 2 or fewer emails: {prob_lte_2:.4f}")

# 3. Survival Function (SF): What is the probability of receiving more than 7 emails?
# P(X > 7) = 1 - P(X <= 7)
prob_gt_7 = email_dist.sf(k=7)
# print(f"Probability of more than 7 emails: {prob_gt_7:.4f}")

# 4. Mean and Variance
# theoretical_mean = email_dist.mean()
# theoretical_variance = email_dist.var()
# print(f"\nTheoretical Mean: {theoretical_mean:.2f} (mu)")
# print(f"Theoretical Variance: {theoretical_variance:.2f} (mu)")

# 5. Visualize the PMF
# k_values = np.arange(0, 15) # Plot for 0 to 14 emails
# probabilities = email_dist.pmf(k_values)

# fig, ax = plt.subplots()
# ax.bar(k_values, probabilities, width=0.1)
# ax.set_title(f"Poisson PMF (μ={mu_rate})")
# ax.set_xlabel("Number of Emails Received (k)")
# ax.set_ylabel("Probability P(X=k)")
# ax.set_xticks(k_values)
# plt.grid(axis='y', linestyle='--')
# plt.show()
```

---