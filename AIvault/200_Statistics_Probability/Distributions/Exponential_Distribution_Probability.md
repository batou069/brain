---
tags:
  - statistics
  - probability
  - distributions
  - continuous_distribution
  - exponential_distribution
  - poisson_process
  - survival_analysis
  - pdf
  - cdf
  - concept
  - scipy
aliases:
  - Exponential Distribution
related:
  - "[[200_Statistics_Probability/Distributions/Probability_Distributions_Overview|Probability Distributions Overview]]"
  - "[[Continuous_vs_Discrete_Distributions]]"
  - "[[Poisson_Distribution]]"
  - "[[Relationships_Between_Probability_Distributions]]"
worksheet:
  - WS_StatsProb_1
date_created: 2025-08-20
---
# Exponential Distribution

## Definition
The **exponential distribution** is a [[Continuous_vs_Discrete_Distributions|continuous probability distribution]] that describes the time between events in a **[[Poisson_Distribution|Poisson process]]**, i.e., a process in which events occur continuously and independently at a constant average rate.

It is often used to model the waiting time until the next event occurs.

## Properties
-   **Random Variable ($X$):** A continuous variable representing time or distance until an event, $X \ge 0$.
-   **Parameter:**
    -   **Rate parameter ($\lambda$):** The average number of events per unit of time (or space). $\lambda > 0$.
    -   **Scale parameter ($\beta$):** The average time between events. $\beta = 1/\lambda$. `scipy.stats` often uses the scale parameter.
-   **PDF (Probability Density Function):**
    $$ f(x; \lambda) = \lambda e^{-\lambda x} \quad \text{for } x \ge 0 $$
    In terms of the scale parameter $\beta$:
    $$ f(x; \beta) = \frac{1}{\beta} e^{-x/\beta} \quad \text{for } x \ge 0 $$
-   **CDF (Cumulative Distribution Function):**
    $$ F(x; \lambda) = P(X \le x) = 1 - e^{-\lambda x} \quad \text{for } x \ge 0 $$
-   **Mean (Expected Value):**
    $$ E[X] = \frac{1}{\lambda} = \beta $$
    The average waiting time is the inverse of the rate.
-   **Variance:**
    $$ \text{Var}(X) = \frac{1}{\lambda^2} = \beta^2 $$
-   **Memoryless Property:** This is a key and unique characteristic of the exponential distribution. It means that the probability of an event occurring in the future is independent of how much time has already passed.
    $$ P(X > s+t | X > s) = P(X > t) $$
    For example, if the lifetime of a light bulb follows an exponential distribution, the probability that it will last for at least another 100 hours is the same, regardless of whether it is brand new or has already been running for 500 hours. This makes it suitable for modeling components that don't "age" but fail at a constant rate.

>[!question]- What is the relationship between the Exponential distribution and the Poisson distribution?
>The Exponential and [[Poisson_Distribution|Poisson]] distributions are closely related; they are two sides of the same coin when modeling events in a Poisson process.
>
>-   The **Poisson distribution** models the **number of events** occurring in a fixed interval of time, given a constant average rate ($\lambda$). It is a discrete distribution.
>    -   *Question:* "If a call center receives an average of 10 calls per hour, what is the probability they will receive exactly 5 calls in the next hour?"
>-   The **Exponential distribution** models the **time between** consecutive events in that same process. It is a continuous distribution.
>    -   *Question:* "If a call center receives an average of 10 calls per hour, what is the probability that the waiting time for the next call is more than 15 minutes?"
>
>If the number of events per unit time follows a Poisson distribution with rate parameter $\lambda$, then the time between those events follows an Exponential distribution with the same rate parameter $\lambda$ (and scale parameter $\beta = 1/\lambda$).

## Use Cases
-   **Reliability Engineering / Survival Analysis:** Modeling the lifetime of components that have a constant failure rate (e.g., electronic components).
-   **Queuing Theory:** Modeling the time between arrivals of customers at a service point, or the time it takes to serve a customer.
-   **Physics:** Modeling the time until a radioactive particle decays.
-   **Finance:** Modeling the time between large market movements or trades.
-   **Hydrology:** Modeling the time between floods or other extreme weather events.

## SciPy Example
In `scipy.stats`, the exponential distribution is represented by `expon`. It is parametrized using the `loc` (shift) and `scale` ($\beta = 1/\lambda$) parameters. For a standard exponential distribution, `loc=0`.

>[!question]- The life expectancy (years) of a certain car follows an exponential distribution with λ=0.1. What is the probability that the car will live more than 10 years?
>
>We need to calculate $P(X > 10)$. This is given by the survival function, $1 - CDF(10)$.
>-   Rate parameter $\lambda = 0.1$ events/year.
>-   Scale parameter $\beta = 1/\lambda = 1/0.1 = 10$ years.
>
>```python
>from scipy.stats import expon
>
># Define the parameters
>lambda_rate = 0.1
># SciPy's 'expon' uses the scale parameter, which is 1/lambda
>beta_scale = 1 / lambda_rate
>
># Probability that the car will live MORE than 10 years
># This is the survival function (sf) evaluated at x=10
>prob_gt_10 = expon.sf(x=10, scale=beta_scale)
>
># Alternatively, using the CDF: 1 - P(X <= 10)
># prob_gt_10_alt = 1 - expon.cdf(x=10, scale=beta_scale)
>
># print(f"The probability that the car will live more than 10 years is: {prob_gt_10:.4f} (or {prob_gt_10*100:.2f}%)")
># Expected output: approx. 0.3679 or 36.79%
># This is e^(-lambda*x) = e^(-0.1 * 10) = e^(-1)
>```

## Visualization
```python
# from scipy.stats import expon
# import matplotlib.pyplot as plt
# import numpy as np

# lambda_rate = 0.1
# beta_scale = 1 / lambda_rate
# x = np.linspace(0, 50, 1000)
# pdf_values = expon.pdf(x, scale=beta_scale)

# fig, ax = plt.subplots()
# ax.plot(x, pdf_values, label=f'Exponential PDF (λ={lambda_rate})')
# ax.set_title("Exponential Distribution PDF")
# ax.set_xlabel("Time (Years)")
# ax.set_ylabel("Probability Density")

# # Shade the area for P(X > 10)
# x_fill = np.linspace(10, 50, 500)
# y_fill = expon.pdf(x_fill, scale=beta_scale)
# ax.fill_between(x_fill, y_fill, color='skyblue', alpha=0.5, label='P(X > 10)')

# ax.legend()
# plt.grid(True, linestyle='--')
# plt.show()
```

---