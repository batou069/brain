---
tags:
  - statistics
  - probability
  - bayes_rule
  - bayesian_inference
  - conditional_probability
  - concept
aliases:
  - Bayes' Theorem
  - Bayesian Statistics
related:
  - "[[200_Statistics_Probability/_Statistics_Probability_MOC|_Statistics_Probability_MOC]]"
  - "[[Probability_vs_Likelihood]]"
  - "[[Conditional_Probability]]"
worksheet:
  - WS_StatsProb_1
date_created: 2025-08-20
---
# Bayes' Rule and Bayesian Inference

## Bayes' Rule (Bayes' Theorem)
**Bayes' Rule** is a fundamental theorem in probability theory that describes the probability of an event, based on prior knowledge of conditions that might be related to the event. It provides a way to update our beliefs in light of new evidence.

The formula is:
$$ P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)} $$
where:
-   **$P(A|B)$** is the **posterior probability**: the probability of hypothesis $A$ being true, given that evidence $B$ is true.
-   **$P(B|A)$** is the **likelihood**: the probability of observing evidence $B$, given that hypothesis $A$ is true.
-   **$P(A)$** is the **prior probability**: our initial belief in the probability of hypothesis $A$, before seeing any evidence.
-   **$P(B)$** is the **marginal probability** (or evidence): the total probability of observing the evidence $B$. It acts as a normalization constant. It can be calculated using the law of total probability: $P(B) = P(B|A)P(A) + P(B|\neg A)P(\neg A)$.

In essence, Bayes' Rule tells us how to perform a "reversal of conditionality"—if we know how likely the evidence is given the hypothesis, we can calculate how likely the hypothesis is given the evidence.

## Bayesian Inference
**Bayesian inference** is a method of statistical inference in which Bayes' Rule is used to update the probability for a hypothesis as more evidence or information becomes available. It is a major school of thought in statistics, contrasting with frequentist inference.

In the context of statistical modeling, we often rephrase Bayes' Rule using model parameters ($\theta$) and observed data:
$$ \underbrace{P(\theta | \text{data})}_{\text{Posterior}} = \frac{\overbrace{P(\text{data} | \theta)}^{\text{Likelihood}} \cdot \overbrace{P(\theta)}^{\text{Prior}}}{\underbrace{P(\text{data})}_{\text{Evidence}}} $$
Or, since the evidence $P(\text{data})$ is a constant for a given dataset:
$$ \text{Posterior} \propto \text{Likelihood} \times \text{Prior} $$

[list2tab|#Bayesian Inference Components]
- Prior ($P(\theta)$)
    -   Represents our beliefs about the model parameters $\theta$ **before** we see any data.
    -   It can be **informative** (based on previous studies or domain knowledge) or **uninformative/vague** (if we have little prior knowledge, e.g., a uniform distribution).
    -   The choice of prior is a key aspect of Bayesian modeling.
- Likelihood ($P(\text{data} | \theta)$ or $\mathcal{L}(\theta | \text{data})$)
    -   Represents the information about the parameters $\theta$ that is contained in the observed data.
    -   It's the probability of observing our data, given a specific set of parameter values. See [[Probability_vs_Likelihood]].
- Posterior ($P(\theta | \text{data})$)
    -   Represents our **updated beliefs** about the model parameters $\theta$ **after** observing the data.
    -   It is a combination of our prior beliefs and the evidence from the data.
    -   The posterior is a full probability distribution for the parameters, not just a single point estimate. This allows us to quantify our uncertainty about the parameters (e.g., using credible intervals).
- Evidence ($P(\text{data})$)
    -   The marginal probability of the data, calculated by integrating the likelihood over all possible parameter values weighted by the prior: $P(\text{data}) = \int P(\text{data} | \theta) P(\theta) \,d\theta$.
    -   It acts as a normalization constant to ensure the posterior distribution integrates to 1.
    -   Calculating the evidence can be computationally very difficult, which is why many Bayesian methods (like Markov Chain Monte Carlo - MCMC) work with the unnormalized posterior ($\text{Likelihood} \times \text{Prior}$).

## Example: Medical Diagnosis
Suppose there is a disease that affects 1% of the population. A test for this disease is 99% accurate for people who have the disease (99% sensitivity) and 98% accurate for people who do not have the disease (98% specificity, meaning a 2% false positive rate).

-   **Hypothesis A:** A person has the disease.
-   **Evidence B:** The person tests positive.
-   We want to find **$P(A|B)$**: the probability the person has the disease given they tested positive.

**Information we have:**
-   **Prior $P(A)$:** $0.01$ (1% of population has the disease).
-   **Prior $P(\neg A)$:** $1 - 0.01 = 0.99$ (99% do not have it).
-   **Likelihood $P(B|A)$:** $0.99$ (Test is positive given they have the disease - sensitivity).
-   **Likelihood of positive test for healthy person $P(B|\neg A)$:** $1 - 0.98 = 0.02$ (False positive rate).

**Calculate the Evidence $P(B)$:**
$P(B) = P(B|A)P(A) + P(B|\neg A)P(\neg A)$
$P(B) = (0.99 \cdot 0.01) + (0.02 \cdot 0.99)$
$P(B) = 0.0099 + 0.0198 = 0.0297$

**Apply Bayes' Rule:**
$$ P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)} = \frac{0.99 \cdot 0.01}{0.0297} = \frac{0.0099}{0.0297} \approx 0.3333 $$

**Conclusion:** Even with a positive test result, the probability of actually having the disease is only about 33.3%. This counter-intuitive result highlights the importance of considering the low prior probability (base rate) of the disease.

## Applications
-   **Spam Filtering:** Classifying emails as spam or not spam based on the words they contain.
-   **Medical Diagnosis:** As shown in the example.
-   **A/B Testing:** Bayesian methods can provide more intuitive results (e.g., "the probability that version B is better than version A is 98%") compared to frequentist p-values.
-   **Machine Learning:**
    -   **Naive Bayes Classifier:** A simple but effective classification algorithm based on Bayes' rule with a "naive" assumption of feature independence.
    -   **Bayesian Neural Networks:** Networks where weights are represented by probability distributions instead of single point values, allowing for better uncertainty quantification.
    -   **Parameter Estimation:** Used to find posterior distributions for model parameters.
-   **Robotics and Control Systems:** Updating the state of a system based on sensor readings (e.g., Kalman filters are related to Bayesian inference).

Bayesian inference provides a powerful framework for reasoning under uncertainty and updating knowledge based on evidence.

---