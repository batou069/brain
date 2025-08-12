---
tags:
  - data_science
  - machine_learning
  - model_tuning
  - overfitting
  - underfitting
  - concept
aliases:
  - Overfitting
  - Underfitting
related:
  - "[[Bias_Variance_Tradeoff]]"
  - "[[L1_L2_Regularization]]"
  - "[[Cross_Validation]]"
  - "[[Model_Evaluation]]"
worksheet:
  - WS_Math_Foundations_2
date_created: 2025-08-07
---
# Overfitting and Underfitting

## Definition
**Overfitting** and **underfitting** are two of the most common problems in machine learning that prevent a model from generalizing well to new, unseen data. They represent two ends of a spectrum related to model complexity and are closely tied to the [[Bias_Variance_Tradeoff|bias-variance tradeoff]].

[list2tab|#Overfitting vs Underfitting]
- Underfitting
    - **What it is:** An underfit model is too simple to capture the underlying patterns in the data. It performs poorly on both the training data and the test data.
    - **Characteristics:**
        - High bias.
        - Low variance.
        - High training error.
        - High test error (similar to training error).
    - **Causes:**
        - The model is not complex enough (e.g., using a linear model for non-linear data).
        - Insufficient training (the model has not converged).
        - Not enough features or poor feature selection.
    - **Solutions:**
        - Use a more complex model (e.g., switch from linear to polynomial regression, use a deeper neural network).
        - Engineer better features.
        - Train for longer or use a better optimization algorithm.
        - Reduce regularization.
- Overfitting
    - **What it is:** An overfit model learns the training data too well, including the noise and random fluctuations. It performs exceptionally well on the training data but fails to generalize to new, unseen data.
    - **Characteristics:**
        - Low bias.
        - High variance.
        - Very low training error.
        - High test error (much higher than training error).
    - **Causes:**
        - The model is too complex for the amount of data available (e.g., high-degree polynomial, very deep neural network).
        - Insufficient training data.
        - Training for too many epochs.
    - **Solutions:**
        - **Get more data:** This is often the most effective solution.
        - **Simplify the model:** Use a less complex model.
        - **[[L1_L2_Regularization|Regularization]]:** Add L1 or L2 penalties to the loss function to constrain model weights.
        - **Dropout:** A regularization technique for neural networks that randomly drops units during training.
        - **Early Stopping:** Stop training when performance on a validation set starts to degrade.
        - **[[Cross_Validation|Cross-Validation]]:** Use a more robust validation strategy.
        - **Data Augmentation:** Create more training data from the existing data (e.g., rotating, flipping images).

>[!todo]
>Expand this note with visualizations showing underfit, good fit, and overfit models on a sample dataset.

---