---
tags:
  - data_science
  - machine_learning
  - supervised_learning
  - learning_paradigm
  - concept
aliases:
  - Supervised ML
related:
  - "[[Unsupervised_Learning]]"
  - "[[Reinforcement_Learning]]"
  - "[[Regression_Models]]"
  - "[[Classification_Models]]"
  - "[[Labeled_Data]]"
  - "[[Model_Evaluation]]"
worksheet:
  - WS_Math_Foundations_2
date_created: 2025-08-07
---
# Supervised Learning

## Definition
**Supervised learning** is one of the three main paradigms of machine learning, alongside [[Unsupervised_Learning|unsupervised learning]] and [[Reinforcement_Learning|reinforcement learning]]. It is characterized by the use of **[[Labeled_Data|labeled data]]** to train algorithms.

In supervised learning, the algorithm learns from a training dataset where each data point is tagged with a correct output or "label". The goal is to learn a mapping function that can generalize from the training data to make accurate predictions on new, unseen data.

The mapping function is learned by minimizing a [[Loss_Function|loss function]], which measures the discrepancy between the model's predictions and the true labels.

## Workflow
1.  **Data Collection:** Gather a dataset of input features and their corresponding correct output labels.
2.  **Data Splitting:** Divide the dataset into a training set, a validation set, and a test set.
3.  **Model Training:** The algorithm learns the relationship between features and labels using the training set.
4.  **Model Evaluation:** The model's performance is evaluated on the unseen test set using various [[Model_Evaluation|evaluation metrics]]. The validation set is often used for hyperparameter tuning.
5.  **Deployment:** Once the model performs satisfactorily, it can be used to make predictions on new, unlabeled data.

## Types of Supervised Learning Problems
Supervised learning is primarily divided into two types of problems based on the nature of the output label:

[list2tab|#Supervised Problem Types]
- Regression
    - **Goal:** Predict a continuous numerical value.
    - **Labels:** The labels are real numbers (e.g., price, temperature, age).
    - **Examples:**
        - Predicting the price of a house based on its features (size, location, etc.).
        - Forecasting stock prices.
        - Estimating a person's age from a photograph.
    - **Common Algorithms:** See [[Regression_Models]].
- Classification
    - **Goal:** Predict a discrete class label or category.
    - **Labels:** The labels belong to a finite set of categories (e.g., "spam" or "not spam", "cat" or "dog").
    - **Sub-types:**
        - **Binary Classification:** Two possible outcome classes (e.g., Yes/No, True/False).
        - **Multi-Class Classification:** More than two mutually exclusive classes (e.g., classifying an image as a cat, dog, or bird).
        - **Multi-Label Classification:** Each sample can be assigned multiple labels (e.g., tagging a news article with "sports", "finance", and "europe").
    - **Common Algorithms:** See [[Classification_Models]].

## Key Concepts
- **Features:** The input variables ($X$) used to make a prediction.
- **Labels (Targets):** The output variable ($y$) that the model tries to predict.
- **Training:** The process of learning the mapping function from the training data.
- **Generalization:** The model's ability to perform well on new, unseen data.
- **[[Overfitting_Underfitting|Overfitting]]:** When a model learns the training data too well, including its noise, and fails to generalize.
- **[[Bias_Variance_Tradeoff|Bias-Variance Tradeoff]]:** A central problem in supervised learning, balancing model simplicity (bias) and complexity (variance).

## Diagram: Supervised Learning Process

```mermaid
graph TD
    subgraph Offline_Training
        A[Labeled Data (Features + Labels)] --> B{Split Data};
        B --> C[Training Set];
        B --> D[Test Set];
        C --> E[Machine Learning Algorithm];
        E -- Learns --> F((Trained Model));
    end

    subgraph Evaluation
        F -- Makes Predictions on --> D;
        D --> G{Evaluate Performance};
        G -- Metrics --> H[Performance Report];
    end
    
    subgraph Deployment
        F -- Deployed --> I[Prediction on New Data];
        J[New Unlabeled Data] --> I;
        I --> K[Predicted Label];
    end

    style F fill:#afa,stroke:#333,stroke-width:2px
```

---