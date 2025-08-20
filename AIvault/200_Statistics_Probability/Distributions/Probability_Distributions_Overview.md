---
tags:
  - statistics
  - probability
  - distributions
  - pmf
  - pdf
  - cdf
  - random_variable
  - concept
aliases:
  - Overview of Probability Distributions
related:
  - "[[200_Statistics_Probability/_Statistics_Probability_MOC|_Statistics_Probability_MOC]]"
  - "[[Discrete_vs_Continuous_Distributions]]"
  - "[[PMF_PDF_CDF]]"
  - "[[160_Python_Libraries/SciPy_Stats_Module|scipy.stats]]"
worksheet:
  - WS_StatsProb_1
date_created: 2025-08-20
---
# Overview of Probability Distributions

A **probability distribution** is a mathematical function that describes the likelihood of different possible outcomes for a [[Random_Variable|random variable]]. It's a fundamental concept in probability and statistics that provides a framework for modeling random phenomena.

>[!question]- What is the point of applying a distribution to your data?
>Applying or fitting a probability distribution to your data serves several key purposes:
>1.  **Summarization and Understanding:** A distribution provides a compact mathematical summary of the data's behavior. Instead of looking at thousands of data points, you can describe them with a distribution name and a few parameters (e.g., "The customer heights follow a Normal distribution with mean 170cm and standard deviation 10cm"). This simplifies understanding and communication.
>2.  **Inference and Prediction:** Once you have a fitted distribution, you can make inferences about the underlying population. You can calculate the probability of observing future events, even values that weren't in your original sample. For example, you can estimate the probability of a car lasting more than 10 years, even if your sample didn't have that exact data point.
>3.  **Foundation for Statistical Modeling:** Many statistical tests and models (like t-tests, ANOVA, linear regression) are based on assumptions about the underlying distribution of the data or errors (often assuming normality). Fitting a distribution helps you check if these assumptions are met.
>4.  **Simulation (Monte Carlo Methods):** If you can model a real-world process with a probability distribution, you can use a computer to generate random samples from that distribution to simulate the process thousands or millions of times. This is useful for risk analysis, performance testing, and understanding complex systems.
>5.  **Data Generation:** In machine learning, distributions are used to generate synthetic data for testing or to initialize model parameters.
>
>In essence, applying a distribution moves you from just describing your observed data (descriptive statistics) to modeling the underlying process that generated the data, which enables prediction and inference.

>[!question]- Can any function be a probability distribution?
>No, not any function can be a probability distribution function. To be a valid probability distribution (specifically, a PMF or PDF), a function $f(x)$ must satisfy certain conditions:
>
>6.  **Non-negativity:** The function must be non-negative for all possible outcomes $x$.
>    -   $f(x) \ge 0$ for all $x$.
>    -   It doesn't make sense to have a negative probability or probability density.
>7.  **Normalization (Sum/Integral to One):** The sum (for discrete distributions) or integral (for continuous distributions) of the function over all possible outcomes in the sample space must be equal to 1.
>    -   **For a Discrete PMF:** $\sum_{\text{all } x} P(X=x) = 1$. This means the probabilities of all possible outcomes must add up to 100%.
>    -   **For a Continuous PDF:** $\int_{-\infty}^{\infty} f(x) \,dx = 1$. This means the total area under the curve of the density function must be 1.
>
>Any function that meets these two criteria can be considered a valid probability distribution function.

## Key Components for Describing a Distribution
-   **[[Discrete_vs_Continuous_Distributions|Type]]:** Is the underlying random variable discrete or continuous?
-   **[[PMF_PDF_CDF|Defining Function]]:**
    -   **PMF (Probability Mass Function):** For discrete distributions. Gives the probability $P(X=k)$ for a specific outcome $k$.
    -   **PDF (Probability Density Function):** For continuous distributions. The area under the PDF curve over an interval gives the probability for that interval.
    -   **CDF (Cumulative Distribution Function):** For all distributions. Gives the probability $P(X \le x)$.
-   **Parameters:** Values that define the specific shape, location, and scale of a distribution within its family (e.g., mean $\mu$ and standard deviation $\sigma$ for the Normal distribution).
-   **Moments:** Descriptive statistics like mean (expected value), variance, skewness, and kurtosis that characterize the distribution.

The [[160_Python_Libraries/SciPy_Stats_Module|`scipy.stats`]] module provides a powerful and consistent interface for working with a vast number of these distributions in Python.

---