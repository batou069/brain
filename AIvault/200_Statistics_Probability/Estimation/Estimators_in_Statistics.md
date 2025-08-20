---
tags:
  - statistics
  - inferential_statistics
  - estimation
  - estimator
  - point_estimate
  - interval_estimate
  - concept
aliases:
  - Estimator
  - Point Estimate
  - Interval Estimate
  - Statistical Estimator
related:
  - "[[200_Statistics_Probability/_Statistics_Probability_MOC|_Statistics_Probability_MOC]]"
  - "[[Descriptive_vs_Inferential_Statistics]]"
  - "[[Bias_Variance_Tradeoff]]"
  - "[[Maximum_Likelihood_Estimation_MLE]]"
worksheet:
  - WS_StatsProb_1
date_created: 2025-08-20
---
# Estimators in Statistics

## Definition
In statistics, an **estimator** is a rule or formula that is used to calculate an estimate of a given quantity based on observed data. The quantity being estimated is called the **estimand**, which is typically a parameter of the underlying population distribution (e.g., the population mean $\mu$, the population variance $\sigma^2$).

-   **Estimator:** The rule or function itself (e.g., the formula for the sample mean, $\bar{X} = \frac{1}{n}\sum X_i$). It is a random variable because its value depends on the particular random sample drawn.
-   **Estimate:** The specific numerical value obtained by applying the estimator to a particular sample of data (e.g., $\bar{x} = 5.2$).

Estimation is a core part of [[Inferential_Statistics|inferential statistics]], where we use sample data to make educated guesses about population parameters.

## Types of Estimates

[list2tab|#Estimate Types]
- Point Estimate
    -   **Definition:** A single value that is our "best guess" for the population parameter.
    -   **Examples:**
        -   The sample mean ($\bar{x}$) is a point estimate of the population mean ($\mu$).
        -   The sample proportion ($\hat{p}$) is a point estimate of the population proportion ($p$).
        -   The sample variance ($s^2$) is a point estimate of the population variance ($\sigma^2$).
    -   **Limitation:** A point estimate by itself provides no information about its precision or how much it might vary from sample to sample. It's almost certain that the point estimate is not *exactly* equal to the true population parameter.
- Interval Estimate (Confidence Interval)
    -   **Definition:** A range of values within which the true population parameter is likely to lie, with a certain level of confidence.
    -   **Example:** "We are 95% confident that the true population mean $\mu$ lies between 4.8 and 5.6."
    -   **Components:**
        -   **Confidence Level:** The probability (e.g., 90%, 95%, 99%) that the interval estimation procedure will produce an interval containing the true parameter value.
        -   **Margin of Error:** The range on either side of the point estimate that defines the interval. It depends on the variability of the data and the sample size.
    -   **Advantage:** Provides a measure of uncertainty associated with the estimate, which is more informative than a single point estimate.

## Properties of Good Estimators
Statisticians evaluate estimators based on several desirable properties. The goal is to find estimators that are, on average, close to the true value and consistent.

1.  **Unbiasedness:**
    -   An estimator is **unbiased** if its expected value is equal to the true value of the population parameter it is estimating.
    -   Mathematically, an estimator $\hat{\theta}$ for a parameter $\theta$ is unbiased if $E[\hat{\theta}] = \theta$.
    -   **Example:** The sample mean ($\bar{X}$) is an unbiased estimator of the population mean ($\mu$). The sample variance calculated with a denominator of $n-1$ ($s^2 = \frac{\sum(x_i-\bar{x})^2}{n-1}$) is an unbiased estimator of the population variance ($\sigma^2$).
    -   See [[Bias_Variance_Tradeoff|Bias]].

2.  **Efficiency (Minimum Variance):**
    -   Among all unbiased estimators for a parameter, the one with the smallest variance is called the most **efficient**.
    -   A more efficient estimator is more likely to produce an estimate close to the true parameter value.
    -   See [[Bias_Variance_Tradeoff|Variance]].

3.  **Consistency:**
    -   An estimator is **consistent** if its value gets closer to the true value of the population parameter as the sample size ($n$) increases.
    -   Formally, as $n \to \infty$, the probability that the estimate is arbitrarily close to the true parameter value approaches 1.
    -   The sample mean is a consistent estimator.

## Example: Estimating Mean Product Rating
-   **Population:** All ratings for a specific product. The true mean rating $\mu$ is unknown.
-   **Sample:** We collect 100 customer ratings.
-   **Estimator:** The formula for the sample mean, $\bar{X} = \frac{1}{100}\sum_{i=1}^{100} X_i$.
-   **Estimate:** We calculate the sample mean from our data and find it to be $\bar{x} = 4.3$ stars. This is our **point estimate** for $\mu$.
-   **Interval Estimate:** After further calculation, we might determine a 95% confidence interval of $[4.1, 4.5]$. We can then state that we are 95% confident that the true average rating for this product across all customers is between 4.1 and 4.5 stars.

In machine learning, the process of training a model is essentially an estimation problem. The model's learned parameters (e.g., the coefficients in a linear regression) are estimates of the "true" parameters that would best describe the underlying relationship in the entire population.

---