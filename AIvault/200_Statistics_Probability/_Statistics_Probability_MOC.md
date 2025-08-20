---
tags:
  - statistics
  - probability
  - data_analysis
  - inference
  - distributions
  - moc
  - concept
aliases:
  - Statistics and Probability MOC
  - Stats & Prob MOC
related:
  - "[[_Data_Science_AI_MOC]]"
  - "[[_Mathematics_MOC]]"
  - "[[160_Python_Libraries/SciPy_Library|SciPy Library]]"
  - "[[160_Python_Libraries/Statsmodels_Library|Statsmodels Library]]"
worksheet:
  - WS_StatsProb_1
date_created: 2025-08-20
---
# Statistics and Probability MOC 🎲📈

This section covers the fundamental concepts of statistics and probability, which form the mathematical foundation for data analysis, machine learning, and making decisions under uncertainty.

## Core Concepts
-   [[Descriptive_vs_Inferential_Statistics|Descriptive vs. Inferential Statistics]]
-   [[Probability_vs_Likelihood|Probability vs. Likelihood]]
-   [[Bayes_Rule_Bayesian_Inference|Bayes' Rule and Bayesian Inference]]
-   [[Central_Limit_Theorem_CLT|Central Limit Theorem (CLT)]]
-   [[Correlation_vs_Covariance|Correlation and Covariance]]
-   [[Descriptive_Statistics_Features|Essential Descriptive Statistics for Understanding Data]]

## Probability Distributions
-   [[Probability_Distributions_Overview|Overview of Probability Distributions]]
    -   [[Discrete_vs_Continuous_Distributions|Discrete vs. Continuous Distributions]]
    -   [[PMF_PDF_CDF|PMF, PDF, and CDF]]
-   **Common Discrete Distributions:**
    -   [[Uniform_Distribution_Discrete|Uniform Distribution (Discrete)]]
    -   [[Bernoulli_Distribution|Bernoulli Distribution]]
    -   [[Binomial_Distribution|Binomial Distribution]]
    -   [[Poisson_Distribution|Poisson Distribution]]
-   **Common Continuous Distributions:**
    -   [[Uniform_Distribution_Continuous|Uniform Distribution (Continuous)]]
    -   [[Normal_Gaussian_Distribution|Normal (Gaussian) Distribution]]
    -   [[Exponential_Distribution_Probability|Exponential Distribution]]
    -   [[Power_Law_Distribution|Power-Law Distribution]]
-   **Relationships Between Distributions:**
    -   [[Relationships_Between_Probability_Distributions|Relationships Between Distributions]] (e.g., Binomial-Poisson, Gaussian-Student-Chi2, Exponential-Poisson)

## Estimation Theory
-   [[Estimators_in_Statistics|Estimators in Statistics]]
-   [[Bias_Variance_Tradeoff|Bias-Variance Tradeoff]]

## Notes in this Section
```dataview
LIST
FROM "200_Statistics_Probability"
WHERE file.folder = this.file.folder AND file.name != this.file.name AND !contains(file.name, "MOC") AND !contains(file.folder, "Distributions")
SORT file.name ASC
```

### Probability Distributions Sub-Section
```dataview
LIST
FROM "200_Statistics_Probability/Distributions"
WHERE file.folder = this.file.folder AND file.name != this.file.name AND !contains(file.name, "MOC")
SORT file.name ASC
```

---