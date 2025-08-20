---
tags:
  - statistics
  - probability
  - likelihood
  - inference
  - bayesian
  - frequentist
  - concept_comparison
aliases:
  - Likelihood vs Probability
related:
  - "[[200_Statistics_Probability/_Statistics_Probability_MOC|_Statistics_Probability_MOC]]"
  - "[[Probability_Distributions_Overview]]"
  - "[[Bayes_Rule_Bayesian_Inference]]"
  - "[[Maximum_Likelihood_Estimation_MLE]]"
worksheet:
  - WS_StatsProb_1
date_created: 2025-08-20
---
# Probability vs. Likelihood

The terms "probability" and "likelihood" are often used interchangeably in everyday language, but in statistics and data science, they have distinct meanings. The key difference lies in what is assumed to be fixed and what is varying.

>[!question]- What is the difference between probability and likelihood?
>
>[list2tab|#Probability vs Likelihood]
>- Probability
>    -   **Perspective:** Forward-looking. Before the data is observed.
>    -   **What is Fixed:** The model parameters (or the process that generates outcomes) are assumed to be fixed and known.
>    -   **What is Varying:** The outcome (data) is the variable.
>    -   **Question It Answers:** "Given a known model/parameter, what is the chance of observing a particular future outcome?"
>    -   **Mathematical Notation:** $P(\text{data} | \theta)$, where $\theta$ represents the fixed model parameters.
>    -   **Properties:**
>        -   It's an area under a curve (for continuous variables) or a sum of heights (for discrete variables).
>        -   Summing or integrating probabilities over all possible outcomes results in 1.
>    -   **Example:**
>        -   **Question:** If I have a fair coin ($p_{heads} = 0.5$), what is the probability of getting 7 heads in 10 flips?
>        -   Here, the parameter $p_{heads}=0.5$ is fixed. We are calculating the probability of a future data outcome.
>- Likelihood
>    -   **Perspective:** Backward-looking. After the data has been observed.
>    -   **What is Fixed:** The outcome (data) is fixed and known.
>    -   **What is Varying:** The model parameters are the variables.
>    -   **Question It Answers:** "Given the observed data, how plausible are different values of the model parameters?"
>    -   **Mathematical Notation:** $\mathcal{L}(\theta | \text{data})$. Note that while the formula may look the same as probability ($P(\text{data} | \theta)$), the interpretation is different because $\theta$ is the variable.
>    -   **Properties:**
>        -   It is **not** a probability. It's a value proportional to the probability of the observed data for a given parameter value.
>        -   The likelihood function does **not** sum or integrate to 1 over all possible parameter values.
>        -   We are interested in the **relative** values of the likelihood function (e.g., which parameter value makes the observed data *most* likely?), not its absolute value.
>    -   **Example:**
>        -   **Question:** I flipped a coin 10 times and observed 7 heads. What is the likelihood of this outcome if the coin's probability of heads ($p_{heads}$) is 0.5? What if it's 0.7?
>        -   Here, the data (7 heads in 10 flips) is fixed. We are evaluating the likelihood of different parameter values ($\theta = p_{heads}$).
>        -   $\mathcal{L}(p_{heads}=0.5 | \text{data}) = \binom{10}{7} (0.5)^7 (0.5)^3 \approx 0.117$
>        -   $\mathcal{L}(p_{heads}=0.7 | \text{data}) = \binom{10}{7} (0.7)^7 (0.3)^3 \approx 0.267$
>        -   The observed data is more *likely* under the assumption that $p_{heads}=0.7$ than under the assumption that $p_{heads}=0.5$.

## Summary Table

[list2mdtable|#Key Differences]
- Feature
    - Probability
        - Likelihood
- **Variable**
    - Data / Outcome
        - Model Parameters ($\theta$)
- **Fixed**
    - Model Parameters ($\theta$)
        - Data / Outcome
- **Question**
    - What is the chance of future data given my model?
        - How plausible is my model given the data I've already seen?
- **Sum/Integral**
    - Sums/integrates to 1 over all possible data outcomes.
        - Does **not** sum/integrate to 1 over all possible parameter values.
- **Main Use**
    - Predicting future events.
        - Estimating model parameters from observed data.

## Role in Statistics and Machine Learning
-   **Probability** is the foundation of predicting future outcomes and understanding uncertainty. It's used in simulations, forecasting, and calculating p-values in frequentist statistics.
-   **Likelihood** is central to **[[Maximum_Likelihood_Estimation_MLE|Maximum Likelihood Estimation (MLE)]]**, a common method for fitting statistical models. MLE finds the parameter values ($\theta$) that maximize the likelihood function $\mathcal{L}(\theta | \text{data})$, i.e., the parameters that make the observed data most probable.
-   In **[[Bayes_Rule_Bayesian_Inference|Bayesian inference]]**, the likelihood is a key component of Bayes' Rule:
    $$ \underbrace{P(\theta | \text{data})}_{\text{Posterior}} \propto \underbrace{\mathcal{L}(\text{data} | \theta)}_{\text{Likelihood}} \times \underbrace{P(\theta)}_{\text{Prior}} $$
    Here, the likelihood function updates our prior belief about the parameters ($P(\theta)$) to arrive at our posterior belief ($P(\theta | \text{data})$) after observing the data.

Understanding this distinction is crucial for correctly interpreting statistical models and results.

---