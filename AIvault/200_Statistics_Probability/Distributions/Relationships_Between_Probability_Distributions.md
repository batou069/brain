---
tags:
  - statistics
  - probability
  - distributions
  - relationships
  - binomial
  - poisson
  - normal
  - exponential
  - student_t
  - chi_squared
  - concept
aliases:
  - Distribution Relationships
  - Binomial-Poisson Approximation
  - Gaussian-Student-Chi2 Link
related:
  - "[[Binomial_Distribution]]"
  - "[[Poisson_Distribution]]"
  - "[[Normal_Gaussian_Distribution]]"
  - "[[Exponential_Distribution_Probability]]"
  - "[[Student_t_Distribution]]"
  - "[[Chi_Squared_Distribution]]"
worksheet:
  - WS_StatsProb_1
date_created: 2025-08-20
---
# Relationships Between Probability Distributions

Many probability distributions are not isolated concepts; they are often related to each other as special cases, approximations, or through transformations of random variables. Understanding these relationships provides deeper insight into statistical theory and practice.

[list2tab|#Distribution Relationships]
- Binomial, Poisson, and Normal
    -   >[!question]- What is the relationship between the Poisson and the Binomial distributions?
        >The **Poisson distribution is a limiting case of the Binomial distribution**.
        >
        >-   **Conditions:** When the number of trials $n$ in a [[Binomial_Distribution|Binomial distribution]] is very large ($n \to \infty$), and the probability of success $p$ is very small ($p \to 0$), such that their product $np = \lambda$ remains a finite, constant value.
        >-   **Intuition:** Imagine you have a very large number of opportunities for an event to happen, but each opportunity has a very small chance of success. The total number of successes in this scenario can be modeled by a Poisson distribution with mean $\lambda = np$.
        >-   **Use Case:** This approximation is useful because calculating the binomial PMF with a very large $n$ can be computationally difficult due to the $n!$ term. For example, modeling the number of typos in a 500-page book. Here, $n$ is the total number of characters (very large), and $p$ is the probability of any single character being a typo (very small).
    -   **Normal Approximation to Binomial:**
        -   **Conditions:** When the number of trials $n$ is large, and the probability $p$ is not too close to 0 or 1. A common rule of thumb is that the approximation is good if both $np > 5$ and $n(1-p) > 5$.
        -   **Approximation:** A Binomial distribution $B(n, p)$ can be approximated by a [[Normal_Gaussian_Distribution|Normal distribution]] with mean $\mu = np$ and variance $\sigma^2 = np(1-p)$.
        -   **Use Case:** Simplifies probability calculations for large $n$ by allowing the use of the continuous normal distribution (often with a continuity correction).
- Exponential and Poisson
    -   >[!question]- What is the relationship between the Exponential distribution and the Poisson distribution?
        >They describe the same underlying random process, a **Poisson process**, from two different perspectives. A Poisson process models events occurring independently at a constant average rate.
        >
        >-   The **[[Poisson_Distribution|Poisson distribution]]** models the **count of events** in a fixed interval of time or space. It is a discrete distribution.
        >    -   *Example:* The number of emails arriving at a server per hour.
        >-   The **[[Exponential_Distribution_Probability|Exponential distribution]]** models the **waiting time** between consecutive events. It is a continuous distribution.
        >    -   *Example:* The time until the next email arrives at the server.
        >
        >If the number of events per unit of time follows a Poisson distribution with rate $\lambda$, then the time between those events follows an Exponential distribution with the same rate parameter $\lambda$.
- Gaussian (Normal), Student's t, and Chi-Squared ($\chi^2$)
    -   >[!question]- What is the link between Gaussian, Student, and Chi2 distributions?
        >These three distributions are fundamental to inferential statistics and are deeply interconnected, especially through sampling from a [[Normal_Gaussian_Distribution|Normal distribution]].
        >
        >1.  **Chi-Squared ($\chi^2$) Distribution:**
        >    -   **Derivation:** If you take $k$ independent random variables $Z_1, Z_2, \dots, Z_k$ from a **standard normal distribution** (mean=0, std=1), and you square them and sum them up, the resulting distribution is a Chi-Squared distribution with $k$ degrees of freedom.
        >        $$ \sum_{i=1}^{k} Z_i^2 \sim \chi^2_k $$
        >    -   **Use Case:** It is used in hypothesis tests for goodness of fit (Chi-squared test) and for making inferences about the variance of a normally distributed population. It is also a component in defining the t-distribution and F-distribution.
        >
        >2.  **Student's t-distribution:**
        >    -   **Derivation:** The t-distribution arises when you are estimating the mean of a normally distributed population from a small sample size and the population standard deviation is **unknown**. It is the distribution of the quantity:
        >        $$ t = \frac{\bar{x} - \mu}{s / \sqrt{n}} $$
        >        where $\bar{x}$ is the sample mean, $\mu$ is the population mean, $s$ is the *sample* standard deviation, and $n$ is the sample size.
        >    -   **Formal Link:** A t-distribution with $k$ degrees of freedom can be defined as the distribution of the ratio of a standard normal variable $Z$ to the square root of a Chi-Squared variable $V$ (divided by its degrees of freedom $k$):
        >        $$ T = \frac{Z}{\sqrt{V/k}} \sim t_k $$
        >    -   **Shape:** It is bell-shaped and symmetric like the normal distribution, but has "heavier" tails, meaning it allows for more variability and extreme values. As the degrees of freedom ($n-1$) increase, the t-distribution **approaches the standard normal distribution**.
        >    -   **Use Case:** Used for confidence intervals and hypothesis testing for the mean when the sample size is small and/or the population variance is unknown (t-tests).
        >
        >3.  **Summary of the Link:**
        >    -   Start with a **Normal** population.
        >    -   The sum of squares of samples from a standard normal gives a **Chi-Squared** distribution.
        >    -   The ratio of a sample mean (normalized) to the sample standard deviation (which is related to the Chi-Squared distribution) gives a **Student's t-distribution**.
        >    -   As sample sizes get large, the t-distribution converges to the **Normal** distribution.
- Bernoulli and Binomial
    -   The **[[Bernoulli_Distribution|Bernoulli distribution]]** is the distribution of a single trial with two outcomes (success/failure).
    -   The **[[Binomial_Distribution|Binomial distribution]]** is the distribution of the **sum of $n$ independent and identically distributed Bernoulli trials**. A Binomial distribution with $n=1$ is a Bernoulli distribution.

Understanding these relationships is key to knowing when to use certain statistical tests and how different statistical concepts are derived from one another.