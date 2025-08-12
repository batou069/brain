---
tags:
  - data_science
  - machine_learning
  - supervised_learning
  - classification
  - model
  - concept
aliases:
  - Classification Algorithms
related:
  - "[[Supervised_Learning]]"
  - "[[Model_Evaluation]]"
  - "[[Logistic_Regression]]"
  - "[[Support_Vector_Machines_SVM]]"
  - "[[Decision_Trees]]"
  - "[[Ensemble_Methods]]"
worksheet:
  - WS_Math_Foundations_2
date_created: 2025-08-07
---
# Classification Models

## Definition
**Classification** is a type of [[Supervised_Learning|supervised learning]] task where the goal is to predict a discrete class label or category for a given input. The target variable is categorical.

**Classification models** are the algorithms used to perform classification. They learn a decision boundary that separates the different classes in the feature space.

## Types of Classification
- **Binary Classification:** Two possible outcome classes (e.g., Spam/Not Spam, Fraud/Not Fraud).
- **Multi-Class Classification:** More than two mutually exclusive classes (e.g., classifying an animal as a Cat, Dog, or Bird).
- **Multi-Label Classification:** Each sample can be assigned one or more labels (e.g., tagging a movie with genres like Action, Comedy, Sci-Fi).

## Common Classification Models
[list2tab|#Classification Models]
- Logistic Regression
    - **Description:** Despite its name, it's a classification algorithm. It models the probability of a binary outcome using the [[Sigmoid_Function|logistic (sigmoid) function]]. For multi-class problems, it can be extended (e.g., using a [[Softmax_Function|softmax function]]).
    - **Strengths:** Simple, interpretable (coefficients can be related to [[Odds|odds ratios]]), fast, provides probabilities.
- k-Nearest Neighbors (k-NN)
    - **Description:** A non-parametric, instance-based algorithm. It classifies a new data point based on the majority class of its 'k' nearest neighbors in the feature space.
    - **Strengths:** Simple to understand, no training phase required (lazy learner).
    - **Weaknesses:** Computationally expensive during prediction, sensitive to feature scaling and irrelevant features.
- Support Vector Machines (SVM)
    - **Description:** Finds an optimal hyperplane that best separates the classes in the feature space. The optimal hyperplane is the one that maximizes the margin between the classes.
    - **Strengths:** Effective in high-dimensional spaces, memory efficient, versatile due to different kernel functions (linear, polynomial, RBF).
- Naive Bayes
    - **Description:** A family of probabilistic classifiers based on applying Bayes' theorem with a "naive" assumption of conditional independence between features.
    - **Strengths:** Very fast, works well with high-dimensional data (e.g., text classification), requires little training data.
    - **Weaknesses:** The strong independence assumption is often violated in reality.
- Decision Trees
    - **Description:** A tree-based model that classifies data by learning a hierarchy of simple if/else decision rules based on the features.
    - **Strengths:** Highly interpretable, can handle both numerical and categorical data.
    - **Weaknesses:** Prone to [[Overfitting_Underfitting|overfitting]], can be unstable.
- Ensemble Methods
    - **Description:** Combine multiple individual models (often decision trees) to create a more powerful and robust classifier.
    - **Examples:**
        - **Random Forest:** An ensemble of decision trees built using bagging.
        - **Gradient Boosting (e.g., GBR, XGBoost, LightGBM):** An ensemble method that builds trees sequentially to correct the errors of previous trees.
    - **Strengths:** Typically provide state-of-the-art performance, robust to overfitting.

## Evaluation Metrics
The performance of classification models is assessed using metrics derived from a **confusion matrix**. Common metrics include:
- **Accuracy:** Overall correct predictions / total predictions.
- **Precision:** True Positives / (True Positives + False Positives). Measures the accuracy of positive predictions.
- **Recall (Sensitivity):** True Positives / (True Positives + False Negatives). Measures the ability to find all positive samples.
- **F1-Score:** The harmonic mean of Precision and Recall: $2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}$.
- **AUC-ROC Curve:** Area Under the Receiver Operating Characteristic Curve. Measures the model's ability to distinguish between classes.

See [[Model_Evaluation]].

---