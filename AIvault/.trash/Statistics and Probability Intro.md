`Excellent! Let's move on to this new chapter on statistics and probability. Here are the explanations for the concepts in your screenshots.

### **Keywords**

**1. Descriptive Statistics**

*   **Definition:** Methods for organizing, summarizing, and presenting data in an informative way. It describes the basic features of the data in a study.
*   **Illustrative Example:** Calculating the average height (mean), the middle height value (median), and the most common height (mode) for a group of students.
*   **Methodologies:** Includes measures of central tendency (mean, median, mode), measures of variability/dispersion (variance, standard deviation, range), and visualizations (histograms, box plots).
*   **Purpose:** To simplify large amounts of data into a sensible summary. It does *not* allow us to make conclusions beyond the data we have analyzed.
*   **Syntax (Python - pandas):** `df['column'].mean()`, `df['column'].median()`, `df['column'].std()`, `df.describe()`

**2. Inferential Statistics**

*   **Definition:** Methods that use data from a sample to make inferences, predictions, or conclusions about a larger population from which the sample was drawn.
*   **Illustrative Example:** Testing a new drug on a sample of 1,000 patients to infer its effectiveness on the entire population of patients with the disease.
*   **Methodologies:** Includes hypothesis testing (e.g., t-tests, chi-squared tests), confidence intervals, and regression analysis.
*   **Purpose:** To generalize from a sample to a population and quantify the uncertainty of that generalization.
*   **Key Concept:** It relies heavily on probability theory to determine the likelihood that the observed results are not just due to random chance.

**3. Probability Distributions**

*   **Definition:** A mathematical function that describes the likelihood of obtaining the possible values that a random variable can take.
*   **Illustrative Example:** A normal distribution (bell curve) can describe the distribution of human heights, showing that most people are of average height, with fewer people being very tall or very short.
*   **Types:**
    *   **Discrete:** For variables that can only take on a finite number of values (e.g., number of heads in 3 coin flips). Described by a Probability Mass Function (PMF).
    *   **Continuous:** For variables that can take on any value within a given range (e.g., height). Described by a Probability Density Function (PDF).
*   **Purpose:** To model real-world phenomena and provide a framework for calculating probabilities of different outcomes.

**4. Probability**

*   **Definition:** A measure of the likelihood that an event will occur, quantified as a number between 0 (impossibility) and 1 (certainty).
*   **Illustrative Example:** The probability of a single roll of a fair six-sided die landing on '4' is 1/6.
*   **Formula (Simple Case):** P(Event) = (Number of favorable outcomes) / (Total number of possible outcomes).
*   **Interpretation:**
    *   **Frequentist:** The long-run frequency of an event over many repeated trials.
    *   **Bayesian:** A degree of belief or confidence in an event occurring, which can be updated with new evidence.

**5. Likelihood**

*   **Definition:** A function that measures the goodness of fit of a statistical model to a sample of data for different values of the model's parameters. It's the probability of the observed data, given a specific parameter value.
*   **Illustrative Example:** If we flip a coin 10 times and get 7 heads (data), the *likelihood* of this data is higher for a model where the probability of heads (parameter) is 0.7 than for a model where the parameter is 0.5.
*   **Distinction from Probability:** Probability asks "Given a known parameter (e.g., a fair coin), what is the chance of seeing this data?". Likelihood asks "Given this observed data, how plausible are different parameter values?". The data is fixed; the parameter varies.
*   **Usage:** Central to many statistical inference methods, particularly Maximum Likelihood Estimation (MLE), where we find the parameter value that maximizes the likelihood function.
*   **Formula:** L(θ | x) = P(x | θ), where θ is the parameter and x is the observed data.

**6. Bayes' Rule**

*   **Definition:** A mathematical formula for determining conditional probability. It describes how to update the probability of a hypothesis based on new evidence.
*   **Illustrative Example:** The initial probability of a patient having a disease is low (prior). If they test positive on a test that isn't 100% accurate (evidence), Bayes' rule calculates the updated, higher probability that they actually have the disease (posterior).
*   **Formula:** P(A|B) = [P(B|A) * P(A)] / P(B)
    *   P(A|B): Posterior probability (probability of hypothesis A given evidence B).
    *   P(A): Prior probability (initial belief in hypothesis A).
    *   P(B|A): Likelihood (probability of seeing evidence B if hypothesis A is true).
    *   P(B): Marginal probability of the evidence.
*   **Application:** The foundation of Bayesian statistics. Used in spam filters, medical diagnosis, A/B testing, and machine learning models like Naive Bayes.

**7. Central Limit Theorem (CLT)**

*   **Definition:** A fundamental theorem stating that the distribution of sample means from a population (regardless of the population's original distribution) will be approximately normally distributed (a bell curve), provided the sample size is sufficiently large (usually n > 30).
*   **Illustrative Example:** If you repeatedly take samples of 50 people and calculate their average height, the distribution of these *average heights* will form a bell curve, even if the original population's height distribution was slightly skewed.
*   **Significance:** It allows us to use normal distribution probabilities to make inferences about population means, even when we don't know the shape of the population's distribution. This is the cornerstone of many hypothesis tests.
*   **Key Result:** The mean of the sampling distribution will be equal to the population mean (μ), and its standard deviation (called the standard error) will be σ/√n, where σ is the population standard deviation and n is the sample size.

**8. Correlation**

*   **Definition:** A statistical measure that expresses the extent to which two variables are linearly related, meaning they change together at a constant rate.
*   **Illustrative Example:** The correlation between height and weight is positive; as height increases, weight tends to increase. The correlation between study time and number of errors is negative; as study time increases, errors tend to decrease.
*   **Metric (Pearson Correlation Coefficient, 'r'):** A value between -1 and +1.
    *   +1: Perfect positive linear correlation.
    *   -1: Perfect negative linear correlation.
    *   0: No linear correlation.
*   **Important Caveat:** **Correlation does not imply causation!** Just because two variables are correlated does not mean one causes the other. There could be a third, confounding variable at play (e.g., ice cream sales and shark attacks are correlated, but both are caused by warm weather).
*   **Syntax (Python - pandas):** `df['col1'].corr(df['col2'])` or `df.corr()` for a full correlation matrix.

---

### **Probability Distributions**

**1. Uniform Distribution**

*   **Domain:** For a continuous variable, a range `[a, b]`. For a discrete variable, a set of `n` outcomes.
*   **PDF (Continuous):** `f(x) = 1 / (b - a)` for `x` in `[a, b]`, and 0 otherwise.
*   **CDF (Continuous):** `F(x) = (x - a) / (b - a)` for `x` in `[a, b]`.
*   **Expected Value:** `E[X] = (a + b) / 2`
*   **Standard Deviation:** `σ = sqrt((b - a)² / 12)`
*   **Real-world Examples:**
    1.  Rolling a single fair die (discrete uniform).
    2.  A random number generator producing numbers between 0 and 1 (continuous uniform).
    3.  The arrival time of a bus that is known to arrive at some point within a 10-minute interval, with no minute being more likely than another.

**2. Bernoulli Distribution**

*   **Domain:** `{0, 1}` (a single trial resulting in failure or success).
*   **PMF:** `P(X=k) = p^k * (1-p)^(1-k)` for `k` in `{0, 1}`. (i.e., `P(1) = p`, `P(0) = 1-p`).
*   **CDF:** `F(k) = 0` for `k < 0`, `1-p` for `0 ≤ k < 1`, and `1` for `k ≥ 1`.
*   **Expected Value:** `E[X] = p`
*   **Standard Deviation:** `σ = sqrt(p * (1-p))`
*   **Real-world Examples:**
    1.  The outcome of a single coin flip (Heads=1, Tails=0).
    2.  Whether a single email is spam (1) or not spam (0).
    3.  Whether a single manufactured part passes (1) or fails (0) a quality check.

**3. Binomial Distribution**

*   **Domain:** `{0, 1, 2, ..., n}` (number of successes in `n` independent Bernoulli trials).
*   **PMF:** `P(X=k) = C(n, k) * p^k * (1-p)^(n-k)`, where `C(n, k)` is the binomial coefficient "n choose k".
*   **CDF:** Sum of the PMF from 0 to `k`. No simple closed-form expression.
*   **Expected Value:** `E[X] = n * p`
*   **Standard Deviation:** `σ = sqrt(n * p * (1-p))`
*   **Real-world Examples:**
    1.  The number of heads obtained after flipping a coin 20 times.
    2.  The number of defective items in a batch of 50, where each item has a known probability of being defective.
    3.  The number of patients who respond to a treatment out of a group of 100, given a known response probability.

**4. Normal (Gaussian) Distribution**

*   **Domain:** `(-∞, +∞)` (all real numbers).
*   **PDF:** `f(x) = (1 / (σ * sqrt(2π))) * e^(-(x-μ)² / (2σ²))`
*   **CDF:** No simple closed-form expression; calculated numerically (often using a Z-table or software).
*   **Expected Value:** `E[X] = μ` (the mean)
*   **Standard Deviation:** `σ`
*   **Real-world Examples:**
    1.  The distribution of human heights or weights in a large population.
    2.  Measurement errors in scientific experiments.
    3.  The distribution of sample means, as described by the Central Limit Theorem.

**5. Exponential Distribution**

*   **Domain:** `[0, +∞)` (non-negative real numbers).
*   **PDF:** `f(x) = λ * e^(-λx)` for `x ≥ 0`.
*   **CDF:** `F(x) = 1 - e^(-λx)` for `x ≥ 0`.
*   **Expected Value:** `E[X] = 1 / λ`
*   **Standard Deviation:** `σ = 1 / λ`
*   **Real-world Examples:**
    1.  The time until the next customer arrives at a store (related to the Poisson process).
    2.  The lifetime of a lightbulb or other electronic component (modeling time until failure).
    3.  The time until a radioactive particle decays.

**6. Poisson Distribution**

*   **Domain:** `{0, 1, 2, ...}` (all non-negative integers).
*   **PMF:** `P(X=k) = (λ^k * e^(-λ)) / k!`
*   **CDF:** Sum of the PMF from 0 to `k`. No simple closed-form expression.
*   **Expected Value:** `E[X] = λ`
*   **Standard Deviation:** `σ = sqrt(λ)`
*   **Real-world Examples:**
    1.  The number of emails you receive in an hour.
    2.  The number of calls a call center receives in a minute.
    3.  The number of typos on a page of a book.
    *   (Process: Events occur independently at a constant average rate, λ).

**7. Power-Law Distribution**

*   **Domain:** `[x_min, +∞)`, where `x_min > 0`.
*   **PDF:** `f(x) = ((α-1) / x_min) * (x / x_min)^(-α)`
*   **CDF:** `F(x) = 1 - (x / x_min)^(-α+1)`
*   **Expected Value:** `(α-1)/(α-2) * x_min` (only if `α > 2`). Can be infinite.
*   **Standard Deviation:** Can be infinite.
*   **Real-world Examples (often called the "80/20 rule" or Pareto principle):**
    1.  The distribution of wealth in a society (a few people have most of the wealth).
    2.  The frequency of words in a language (a few words like "the" and "a" are extremely common).
    3.  The distribution of city populations (a few megacities, many small towns).

---

### **Estimation**

**1. Estimator**

*   **Definition:** A rule or formula that uses sample data to calculate an estimate of a population parameter. The result of applying the estimator is called the "estimate".
*   **Illustrative Example:** The sample mean (formula: `Σx_i / n`) is an *estimator* for the population mean (μ). If you take a sample of students and their average height is 175cm, then 175cm is the *estimate*.
*   **Types:**
    *   **Point Estimator:** Provides a single value as the estimate (e.g., sample mean).
    *   **Interval Estimator:** Provides a range of values, called a confidence interval, that is likely to contain the population parameter.
*   **Properties of a Good Estimator:** Unbiased (accurate on average), efficient (low variance), and consistent (converges to the true value as sample size increases).

**2. Bias / Variance Dilemma**

*   **Definition:** A fundamental trade-off in machine learning and statistics. It decomposes a model's prediction error into three components: bias, variance, and irreducible error.
*   **Bias:** The error from erroneous assumptions in the learning algorithm. High bias can cause a model to miss relevant relations between features and target outputs (underfitting). Example: Using a linear model for a complex, non-linear relationship.
*   **Variance:** The error from sensitivity to small fluctuations in the training set. High variance can cause a model to capture random noise instead of the intended output (overfitting). Example: A complex decision tree that perfectly fits the training data but fails to generalize.
*   **Dilemma:** Increasing model complexity typically decreases bias but increases variance. Decreasing   increases bias but decreases variance. The goal is to find a sweet spot with low bias and low variance.
*   **Analogy:**
    *   Low Bias, Low Variance: Hitting the bullseye consistently.
    *   Low Bias, High Variance: Shots are centered around the bullseye but widely scattered.
    *   High Bias, Low Variance: Shots are tightly clustered but far from the bullseye.
    *   High Bias, High Variance: Shots are scattered and far from the bullseye.

---

### **Questions**

**1. What is the difference between covariance and correlation?**

*   **Definition:** Both measure the direction of the linear relationship between two variables.
*   **Covariance:** Indicates the direction (positive or negative). However, its magnitude is unbounded and depends on the units of the variables, making it hard to interpret. A covariance of 100 m
* ight be strong for one dataset but weak for another.
*   **Correlation:** A standardized version of covariance. It indicates both the direction and the *strength* of the linear relationship.
*   **Scale:** Covariance can range from -∞ to +∞. Correlation is always bounded between -1 and +1, making it unitless and easily comparable across different datasets.
*   **Conclusion:** Correlation is almost always preferred for interpreting the relationship between two variables because its standardized scale provides a clear measure of strength.

**2. For each distribution get...**

*   *(This question is answered in the "Probability Distributions" section above).*

**3. What is the link between Gaussian, Student, and Chi2 distributions?**

*   **Foundation:** All three are sampling distributions derived from a normally distributed (Gaussian) population.
*   **Gaussian (Normal) to Chi-Squared (χ²):** If you take `k` independent random variables from a standard normal distribution (μ=0, σ=1), square them, and add them up, the resulting distribution is a Chi-Squared distribution with `k` degrees of freedom. It's used in goodness-of-fit tests and for inferences about variance.
*   **Gaussian to Student's t-distribution:** If you take a sample from a normal population and calculate `(sample_mean - population_mean) / (sample_std_dev / sqrt(n))`, this statistic follows a t-distribution. It is shaped like a normal distribution but with heavier tails, accounting for the extra uncertainty of estimating the standard deviation from a small sample. As the sample size (`n`) gets large, the t-distribution converges to the normal distribution.
*   **Why are they useful?** They are the building blocks of classical hypothesis testing.
    *   **Gaussian (Z-test):** Used when the population standard deviation is known or the sample size is large.
    *   **Student's t (t-test):** Used when the population standard deviation is unknown and estimated from a small sample.
    *   **Chi-Squared (χ²-test):** Used for testing the variance of a population or for testing relationships between categorical variables (goodness-of-fit, independence).

**4. When would you consider a discrete distribution and when would you consider a continuous distribution?**

*   **Discrete Distribution:** Use when the variable you are modeling is countable. The outcomes are distinct and separate values (usually integers).
    *   **Examples:** The number of cars passing a point in an hour, the number of defective items in a batch, the result of a die roll.
    *   **Key Question:** Can you count the possible outcomes (even if there are infinitely many, like in Poisson)?
*   **Continuous Distribution:** Use when the variable can take on any value within a given range. There are infinitely many possible values between any two points.
    *   **Examples:** Height, weight, temperature, time.
    *   **Key Question:** Can you measure the outcome with arbitrary precision?

**5. What is the point of applying a distribution to your data?**

*   **Modeling and Understanding:** To provide a compact mathematical model that summarizes the underlying process generating the data. This helps us understand the data's central tendency, spread, and shape.
*   **Making Inferences:** Once we fit a distribution, we can use its mathematical properties to make inferences about the population, even for outcomes we haven't observed.
*   **Calculating Probabilities:** It allows us to calculate the probability of observing specific values or ranges of values, which is crucial for hypothesis testing and risk assessment.
*   **Simulation:** We can use the fitted distribution to generate new, synthetic data that resembles the original data, which is useful for simulations and "what-if" analyses.
*   **Identifying Anomalies:** If we have a good model for our data, we can identify new data points that are highly unlikely under that model, flagging them as potential outliers or anomalies.

**6. Can any function be a probability distribution?**

*   **No.** For a function `f(x)` to be a valid probability distribution (a PMF for discrete or a PDF for continuous), it must satisfy two key conditions:
    1.  **Non-negativity:** The function must be non-negative for all possible outcomes. `f(x) ≥ 0` for all `x`. You cannot have a negative probability.
    2.  **Normalization:** The sum (for discrete PMF) or integral (for continuous PDF) of the function over all possible outcomes must equal 1. This ensures that the total probability of *something* happening is 100%.

**7. The life expectancy (years) of a certain car follows an exponential distribution with λ=0.1. What is the probability that the car will live more than 10 years?**

*   **Formula:** The probability that the car lives *more* than `x` years is given by the survival function, `P(X > x) = e^(-λx)`.
*   **Parameters:** `λ = 0.1`, `x = 10`.
*   **Calculation:**
    *   `P(X > 10) = e^(-0.1 * 10)`
    *   `P(X > 10) = e^(-1)`
    *   `P(X > 10) ≈ 0.3679`
*   **Answer:** The probability that the car will live more than 10 years is approximately 36.8%.

**8. The height (cm) of a certain human population follows a Gaussian distribution with μ=170 and σ=10. What is the probability that one randomly picked person measures between 190 and 200?**

*   **Method:** We need to convert the heights to Z-scores and use a Z-table or calculator. The Z-score formula is `Z = (X - μ) / σ`. We want to find `P(190 < X < 200)`.
*   **Calculations:**
    1.  **Z-score for 190cm:** `Z₁ = (190 - 170) / 10 = 20 / 10 = 2.0`
    2.  **Z-score for 200cm:** `Z₂ = (200 - 170) / 10 = 30 / 10 = 3.0`
    3.  **Find Probabilities:** We need to find `P(Z < 3.0) - P(Z < 2.0)`.
        *   Using a standard Z-table or calculator, `P(Z < 3.0) ≈ 0.99865`.
        *   Using a standard Z-table or calculator, `P(Z < 2.0) ≈ 0.97725`.
    4.  **Subtract:** `0.99865 - 0.97725 = 0.0214`
*   **Answer:** The probability that a randomly picked person measures between 190cm and 200cm is approximately 2.14%.

**9. If height (cm) of a certain human population follows a Gaussian distribution with μ=170 and σ=10, then p(height < 0) > 0. How can it be?**

*   **Mathematical Reason:** The domain of a true Gaussian distribution is all real numbers, from -∞ to +∞. Therefore, mathematically, there is a non-zero (though infinitesimally small) probability for any value, including negative ones.
*   **Modeling Limitation:** This is a classic example of where a statistical model is an *approximation* of reality, not reality itself. Height is physically constrained to be positive.
*   **Practical Implication:** The probability of observing a height less than 0 is so astronomically small that it is effectively zero for all practical purposes. The Z-score for a height of 0 would be `(0 - 170) / 10 = -17`. The probability `P(Z < -17)` is far smaller than any meaningful threshold and would be rounded to 0 by any standard software.
*   **Conclusion:** It highlights the importance of understanding the limitations of a model. While the Gaussian distribution is a very useful model for height, it's not a perfect representation because its domain doesn't match the physical constraints of the real-world variable.

**10. What is the difference between probability and likelihood?**

*   *(This question is answered in the "Keywords" section, point 5, under "Likelihood").*

**11. List essential statistics features you can get from a dataset that can help you better understand it. Are these numbers always helpful?**

*   **Essential Statistics:**
    1.  **Measures of Central Tendency:** `Mean`, `Median`, `Mode`. Tells you where the "center" of your data is.
    2.  **Measures of Dispersion:** `Standard Deviation`/`Variance`, `Range`, `Interquartile Range (IQR)`. Tells you how spread out your data is.
    3.  **Shape of the Distribution:** `Skewness` (asymmetry) and `Kurtosis` (tailedness/peakedness). Tells you if the data is symmetric or lopsided.
    4.  **Count of Observations:** The total number of data points (`n`).
    5.  **Quartiles/Percentiles:** Values that divide your data into quarters (25th, 50th, 75th percentiles) or other proportions.
*   **Are they always helpful? No, context is critical.**
    *   The `mean` can be very misleading in a highly skewed distribution (e.g., average income); the `median` is often better.
    *   A `standard deviation` of 10 might be huge for one dataset (test scores out of 20) but tiny for another (house prices).
    *   These summary statistics can be identical for very different-looking distributions (see Anscombe's Quartet).
    *   **Conclusion:** Summary statistics are a vital starting point, but they must always be paired with data visualization (like histograms and box plots) to get the full picture and avoid being misled.

**12. What is the mathematical expression of the bias-variance dilemma?**

*   **Expression:** The Mean Squared Error (MSE) of an estimator `ŷ` for a true value `y` can be decomposed as:
    `MSE = E[(y - ŷ)²] = Bias(ŷ)² + Var(ŷ) + σ²`
*   **Where does this formula come from?** It's derived by adding and subtracting the expected value of the estimator `E[ŷ]` inside the squared term and expanding the expression.
*   **Breakdown:**
    *   `Bias(ŷ)²`: The squared difference between the true value and the average prediction of our model. `(E[ŷ] - y)²`. It measures the model's systematic error or "accuracy".
    *   `Var(ŷ)`: The variance of the model's predictions for a given point. `E[(ŷ - E[ŷ])²]`. It measures the model's "consistency" or sensitivity to the training data.
    *   `σ²`: The irreducible error (or noise). This is the variance of the true value `y` around its mean and represents the lower bound on the error that any model can achieve.
*   **What is the problem with 0 bias? And with 0 variance?**
    *   **0 Bias:** A model with zero bias is, on average, perfectly accurate. However, to achieve this, it might need to be extremely complex, making it highly sensitive to the training data (high variance). It would fit the training data perfectly but generalize poorly (overfitting).
    *   **0 Variance:** A model with zero variance is perfectly consistent; it gives the same prediction regardless of the training data. This implies an extremely simple, rigid model (e.g., always predicting the overall average). It would be very stable but likely inaccurate for most data points (high bias).

**13. Is linear regression a "biased" estimator?**

*   **It depends on the context.**
*   **In terms of its coefficients (β):** If the true relationship between the features and the target *is* linear and the assumptions of linear regression (like no omitted variables, homoscedasticity) are met, then the Ordinary Least Squares (OLS) estimator for the coefficients is **unbiased**.
*   **In terms of its predictions (ŷ):** If the true underlying relationship in the data is *not* linear (e.g., it's quadratic), then using a linear regression model will produce **biased predictions**. The model is systematically wrong because its linear assumption doesn't match reality. This is an example of model bias.
*   **Regularized Regression (Ridge, Lasso):** These are intentionally **biased** estimators. They add a penalty term to the loss function, which shrinks the coefficients towards zero. This introduces bias but reduces the variance of the model, often leading to a better overall MSE on new data.

**14. What is the relationship between the Poisson and the Binomial distributions?**

*   **Limiting Case:** The Poisson distribution is the limiting case of the Binomial distribution.
*   **Conditions:** When the number of trials `n` in a Binomial distribution is very large (`n → ∞`) and the probability of success `p` in each trial is very small (`p → 0`), the Binomial distribution can be approximated by a Poisson distribution.
*   **Parameter Relationship:** The parameter `λ` (the average rate) of the resulting Poisson distribution is equal to `n * p` from the Binomial distribution. `λ = n * p`.
*   **Practical Use:** This approximation is useful because the Binomial PMF can be computationally intensive with a very large `n`. If you are modeling a rare event over many opportunities (e.g., number of accidents on a highway with thousands of cars), it's much easier to use a Poisson model than a Binomial one.

**15. How can you visually see exponential and power-law relationships in your data?**

*   **Method:** Use a log-log plot or a semi-log plot. Plotting the data on transformed axes can make these non-linear relationships appear as straight lines, which are easy to identify visually.
*   **Exponential Relationship (`y = a * e^(bx)`):**
    *   Plot the data on a **semi-log plot** (logarithmic y-axis, linear x-axis).
    *   If the relationship is exponential, the data points will form a **straight line** on this plot.
*   **Power-Law Relationship (`y = a * x^k`):**
    *   Plot the data on a **log-log plot** (both x and y axes are logarithmic).
    *   If the relationship follows a power law, the data points will form a **straight line** on this plot. The slope of this line corresponds to the exponent `k`.

**16. Why does the uniform distribution have both a PMF and a PDF?**

*   **It doesn't have both for the same variable; it has one or the other depending on the type of variable.** This is a key distinction.
*   **Discrete Uniform Distribution:** Applies to a **discrete random variable** (e.g., rolling a die). It has a **Probability Mass Function (PMF)**, which assigns a specific probability to each of the `n` distinct outcomes (e.g., P(X=1) = 1/6, P(X=2) = 1/6, etc.).
*   **Continuous Uniform Distribution:** Applies to a **continuous random variable** (e.g., a random number between 0 and 1). It has a **Probability Density Function (PDF)**. The PDF gives the *density* over a range, and the probability of any single exact point is zero. Probability is calculated by finding the area under the PDF curve over an interval.

**17. What is the relationship between the Exponential distribution and the Poisson distribution?**

*   **Two Sides of the Same Coin:** They both model events happening in a Poisson process (events occurring independently at a constant average rate, λ).
*   **Poisson Distribution:** Describes the **count of eved interval of time or space.ents** occurring in a fix
    *   *Question:* How many emails will I get in the next hour? (Answer is a count: 0, 1, 2, ...)
*   **Exponential Distribution:** Describes the **time between consecutive events** in that same process.
    *   *Question:* How long until the next email arrives? (Answer is a continuous time value).
*   **Parameter Link:** The rate parameter `λ` is the same for both. If the number of events per hour follows a Poisson distribution with rate `λ`, then the time (in hours) between events follows an Exponential distribution with that same rate `λ`.