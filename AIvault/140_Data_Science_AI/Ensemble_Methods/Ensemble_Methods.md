---
tags:
  - data_science
  - machine_learning
  - ensemble_methods
  - bagging
  - boosting
  - stacking
  - concept
aliases:
  - Ensemble Learning
related:
  - "[[Decision_Trees]]"
  - "[[Random_Forest]]"
  - "[[Gradient_Boosting]]"
  - "[[Bias_Variance_Tradeoff]]"
  - "[[Overfitting_Underfitting]]"
worksheet:
  - WS_Math_Foundations_2
date_created: 2025-08-20
---
# Ensemble Methods

## Definition
**Ensemble learning** (or **ensemble methods**) is a machine learning technique where multiple individual models, often called "weak learners" or "base estimators," are strategically combined to produce one optimal predictive model. The goal is to achieve better performance than any of the constituent models could on their own.

The intuition is that by combining diverse and independent models, their individual errors can cancel each other out, leading to a more robust, accurate, and generalizable final prediction.

## Main Types of Ensemble Methods
[list2tab|#Ensemble Types]
- Bagging
    - **Stands for:** Bootstrap Aggregating.
    - **How it works:**
        1.  **Bootstrap:** Create multiple random subsets of the original training data by sampling with replacement.
        2.  **Aggregate:** Train a separate base model (e.g., a [[Decision_Trees|Decision Tree]]) on each subset.
        3.  **Combine:** The final prediction is made by averaging the predictions of all models (for regression) or by taking a majority vote (for classification).
    - **Primary Goal:** To reduce **variance** and combat [[Overfitting_Underfitting|overfitting]]. It is most effective with unstable models that have high variance (like deep decision trees).
    - **Example:** **[[Random_Forest|Random Forest]]** is a popular bagging method that uses decision trees as base learners and adds an extra layer of randomness by selecting a random subset of features at each split.
- Boosting
    - **Description:** Models are built sequentially, where each subsequent model attempts to correct the errors of its predecessor.
    - **How it works:**
        1.  Train a simple base model on the data.
        2.  Identify the errors made by the model.
        3.  Train a new model that focuses on the instances where the previous model performed poorly (by giving them higher weights).
        4.  Combine all models, typically through a weighted sum, to make the final prediction.
    - **Primary Goal:** To reduce **bias** and build a strong, complex model from simple ones (weak learners).
    - **Examples:**
        - **AdaBoost (Adaptive Boosting)**
        - **[[Gradient_Boosting|Gradient Boosting Machines (GBM)]]**
        - **XGBoost, LightGBM, CatBoost** (highly optimized implementations of gradient boosting).
- Stacking
    - **Description:** Stacking (or Stacked Generalization) involves training a new model to combine the predictions of several other base models.
    - **How it works:**
        1.  Train several different base models (e.g., a logistic regression, an SVM, a random forest) on the training data.
        2.  Use these base models to make predictions on a hold-out set (or through cross-validation).
        3.  These predictions are then used as input features to train a final "meta-model" (or "blender").
    - **Primary Goal:** To leverage the strengths of different types of models by learning how to best combine their predictions.

## Why Ensembles Work
- **Wisdom of the Crowd:** The collective knowledge of a diverse group is often better than that of a single expert.
- **Reduced Variance (Bagging):** Averaging the predictions of multiple models smooths out noise and reduces the impact of individual model errors.
- **Reduced Bias (Boosting):** Sequentially focusing on errors allows the ensemble to capture complex patterns that individual weak models would miss.
- **Improved Robustness:** The final model is less sensitive to the specifics of a single training set or the weaknesses of a single algorithm.

Ensemble methods, particularly gradient boosting and random forests, are responsible for many state-of-the-art results on tabular data and are widely used in both industry and machine learning competitions.

---