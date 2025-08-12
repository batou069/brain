---
tags:
  - data_science
  - machine_learning
  - model_tuning
  - bias
  - variance
  - tradeoff
  - concept
aliases:
  - Bias-Variance Dilemma
related:
  - "[[Overfitting_Underfitting]]"
  - "[[Model_Evaluation]]"
  - "[[Ensemble_Methods]]"
worksheet:
  - WS_Math_Foundations_2
date_created: 2025-08-07
---
# Bias-Variance Tradeoff

## Definition
The **bias-variance tradeoff** is a fundamental concept in [[Supervised_Learning|supervised learning]] that describes the relationship between a model's complexity, its ability to fit the training data, and its ability to generalize to unseen data.

The total expected error of a model on unseen data can be decomposed into three parts:
$$ \text{Expected Error} = \text{Bias}^2 + \text{Variance} + \text{Irreducible Error} $$
- **Irreducible Error:** Noise inherent in the problem itself, which cannot be reduced by any model.

[list2tab|#Bias vs Variance]
- Bias
    - **Definition:** Bias is the error from erroneous assumptions in the learning algorithm. High bias can cause an algorithm to miss the relevant relations between features and target outputs. It represents the model's tendency to consistently learn the wrong thing by not being complex enough.
    - **Characteristics:**
        - Leads to **[[Overfitting_Underfitting|underfitting]].**
        - A simple model (e.g., linear regression on non-linear data) has high bias.
        - The model makes strong assumptions about the data.
- Variance
    - **Definition:** Variance is the error from sensitivity to small fluctuations in the training set. High variance can cause an algorithm to model the random noise in the training data, rather than the intended outputs. It represents the model's tendency to learn random things irrespective of the real signal.
    - **Characteristics:**
        - Leads to **[[Overfitting_Underfitting|overfitting]].**
        - A very complex model (e.g., a high-degree polynomial or a deep decision tree) has high variance.
        - The model's predictions would change significantly if trained on a different subset of the data.

## The Tradeoff
- **Simple Models (Low Complexity):** High Bias, Low Variance.
- **Complex Models (High Complexity):** Low Bias, High Variance.

The goal is to find a sweet spot in model complexity that minimizes the total error by balancing bias and variance. As you decrease bias (by increasing model complexity), variance tends to increase, and vice versa.

>[!todo]
>Expand this note with a bullseye diagram to visualize bias and variance, and a graph showing the tradeoff curve (Error vs. Model Complexity).

## Managing the Tradeoff
- **Regularization ([[L1_L2_Regularization|L1/L2]]):** Increases bias slightly to significantly reduce variance.
- **[[Ensemble_Methods|Ensemble Methods]]:**
    - **Bagging (e.g., Random Forest):** Primarily reduces variance by averaging the predictions of multiple models trained on different subsets of the data.
    - **Boosting (e.g., Gradient Boosting):** Primarily reduces bias by training models sequentially, where each model focuses on the errors of the previous one.
- **Getting More Data:** Can help reduce variance.
- **Feature Engineering:** Can help reduce bias by providing the model with more relevant information.

---