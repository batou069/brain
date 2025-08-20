---
tags:
  - statistics
  - probability
  - distributions
  - discrete_distribution
  - continuous_distribution
  - random_variable
  - concept_comparison
aliases:
  - Discrete and Continuous Probability Distributions
related:
  - "[[200_Statistics_Probability/Distributions/Probability_Distributions_Overview|Probability Distributions Overview]]"
  - "[[PMF_PDF_CDF]]"
  - "[[Random_Variable]]"
worksheet:
  - WS_StatsProb_1
date_created: 2025-08-20
---
# Discrete vs. Continuous Probability Distributions

The fundamental difference between discrete and continuous probability distributions lies in the nature of the outcomes (the values that the random variable can take).

>[!question]- When would you consider a discrete distribution and when would you consider a continuous distribution?
>You choose the type of distribution based on the nature of the random variable you are trying to model:
>
>**Consider a Discrete Distribution when:**
>-   The variable represents **countable outcomes**.
>-   The outcomes are distinct and separate values (often integers).
>-   You are interested in the probability of an *exact* outcome (e.g., "What is the probability of getting *exactly* 3 heads?").
>-   **Examples of Scenarios:**
>    -   The number of defective items in a batch ([[Binomial_Distribution|Binomial]]).
>    -   The number of customer support calls received in an hour ([[Poisson_Distribution|Poisson]]).
>    -   The outcome of a single success/failure trial (e.g., a customer churns or not) ([[Bernoulli_Distribution|Bernoulli]]).
>    -   The outcome of rolling a die ([[Uniform_Distribution_Discrete|Discrete Uniform]]).
>
>**Consider a Continuous Distribution when:**
>-   The variable can take **any value within a given range or interval**.
>-   The outcomes are measurements that are not restricted to specific, separate values.
>-   You are interested in the probability of an outcome falling *within a range* (e.g., "What is the probability that a person's height is *between* 170cm and 180cm?").
>-   **Examples of Scenarios:**
>    -   Measurements of height, weight, temperature, or time ([[Normal_Gaussian_Distribution|Normal]] is common).
>    -   The time until the next event occurs (e.g., time until the next customer arrives) ([[Exponential_Distribution_Probability|Exponential]]).
>    -   Any outcome within a fixed range having an equal chance of occurring ([[Uniform_Distribution_Continuous|Continuous Uniform]]).
>    -   Modeling phenomena where many small factors contribute to the final value, often leading to a normal distribution due to the [[Central_Limit_Theorem_CLT|Central Limit Theorem]].

## Comparison of Properties

[list2mdtable|#Discrete vs. Continuous]
- Feature
    - Discrete Distribution
        - Continuous Distribution
- **Random Variable**
    - Countable (e.g., 0, 1, 2, 3, ...)
        - Uncountable, can take any value in an interval (e.g., 1.25, 3.14159, ...)
- **Probability Function**
    - **PMF (Probability Mass Function)**, $P(X=k)$
        - **PDF (Probability Density Function)**, $f(x)$
- **Probability Interpretation**
    - $P(X=k)$ gives the probability of the exact value $k$.
        - $f(x)$ is **not** a probability. The probability of an exact value is zero, $P(X=x)=0$. Probability is the area under the PDF curve.
- **Key Condition**
    - $\sum_{\text{all } k} P(X=k) = 1$
        - $\int_{-\infty}^{\infty} f(x) \,dx = 1$
- **Calculating Probability**
    - $P(a \le X \le b) = \sum_{k=a}^{b} P(X=k)$
        - $P(a \le X \le b) = \int_{a}^{b} f(x) \,dx$
- **CDF (Cumulative Distribution Function)**
    - A step function (jumps at each possible value).
        - A continuous, non-decreasing function.
- **Example Distributions**
    - Bernoulli, Binomial, Poisson, Geometric, Discrete Uniform.
        - Normal (Gaussian), Exponential, Continuous Uniform, Beta, Gamma.

## Visualization
-   A **discrete distribution** is typically visualized with a **bar chart** or stick plot, where the height of each bar at value $k$ represents $P(X=k)$.
-   A **continuous distribution** is visualized with a **smooth curve**, where the area under the curve between two points represents the probability of an outcome falling in that range.

Understanding whether your data is discrete or continuous is the first and most critical step in choosing an appropriate probability distribution to model it.

---