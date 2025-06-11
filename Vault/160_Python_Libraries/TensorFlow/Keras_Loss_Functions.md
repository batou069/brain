---
tags:
  - python
  - tensorflow
  - tf
  - keras
  - neural_networks
  - loss_functions
  - objective_function
  - concept
  - example
aliases:
  - tf.keras.losses
  - Keras Loss
  - Cost Function Keras
related:
  - "[[Keras_API_in_TensorFlow]]"
  - "[[Keras_Optimizers]]"
  - "[[Model_Evaluation_Metrics]]"
worksheet:
  - WS_DeepLearning_1
date_created: 2025-06-11
---
# Keras: Loss Functions (`tf.keras.losses`)

A **loss function** (or objective function, cost function) in Keras (`tf.keras.losses`) quantifies how well a machine learning model performs by measuring the difference between the model's predictions and the true target values. The goal of training a model is to find a set of parameters (weights and biases) that **minimizes** this loss function.

Loss functions are specified during the `model.compile()` step.

## Role of Loss Functions
-   **Guides Optimization:** The [[Keras_Optimizers|optimizer]] uses the gradients of the loss function with respect to the model's parameters to update these parameters in a direction that reduces the loss.
-   **Problem Specific:** The choice of loss function depends heavily on the type of problem being solved (e.g., regression, binary classification, multi-class classification).

## Common Loss Functions in `tf.keras.losses`
Keras provides loss functions as classes or as string identifiers.

[list2tab|#Keras Loss Functions]
- Regression Losses
    -   **Mean Squared Error (MSE):**
        -   **Class:** `tf.keras.losses.MeanSquaredError()`
        -   **String:** `'mean_squared_error'` or `'mse'`
        -   **Formula:** $L = \frac{1}{N} \sum_{i=1}^{N} (y_{true,i} - y_{pred,i})^2$
        -   **Use Case:** Common for regression tasks. Penalizes larger errors more heavily due to squaring. Assumes errors are normally distributed.
        -   **Example (Predicting product price):**
            ```python
            # from tensorflow import keras
            # model.compile(optimizer='adam', loss=keras.losses.MeanSquaredError())
            # Or: model.compile(optimizer='adam', loss='mse')
            ```
    -   **Mean Absolute Error (MAE):**
        -   **Class:** `tf.keras.losses.MeanAbsoluteError()`
        -   **String:** `'mean_absolute_error'` or `'mae'`
        -   **Formula:** $L = \frac{1}{N} \sum_{i=1}^{N} |y_{true,i} - y_{pred,i}|$
        -   **Use Case:** Regression. Less sensitive to outliers compared to MSE as errors are not squared.
    -   **Mean Absolute Percentage Error (MAPE):**
        -   **Class:** `tf.keras.losses.MeanAbsolutePercentageError()`
        -   **String:** `'mean_absolute_percentage_error'` or `'mape'`
        -   **Formula:** $L = \frac{100\%}{N} \sum_{i=1}^{N} \left| \frac{y_{true,i} - y_{pred,i}}{y_{true,i}} \right|$ (Careful with $y_{true,i}=0$)
        -   **Use Case:** Regression. Expresses error as a percentage, often more interpretable.
    -   **Huber Loss:**
        -   **Class:** `tf.keras.losses.Huber()`
        -   **Concept:** Combines MSE and MAE. It's quadratic for small errors and linear for large errors, making it less sensitive to outliers than MSE but still differentiable.
        -   **Key Parameter:** `delta` (float, default 1.0): The point where the loss changes from quadratic to linear.
- Binary Classification Losses
    -   **Binary Cross-Entropy (Log Loss):**
        -   **Class:** `tf.keras.losses.BinaryCrossentropy()`
        -   **String:** `'binary_crossentropy'`
        -   **Formula (for a single sample):** $L = -(y_{true} \log(y_{pred}) + (1 - y_{true}) \log(1 - y_{pred}))$
        -   **Use Case:** For binary classification problems where the model outputs a probability (typically via a [[Sigmoid_Function|sigmoid]] activation in the last layer). $y_{true}$ is 0 or 1. $y_{pred}$ is the predicted probability for class 1.
        -   **Key Parameter:** `from_logits`: Boolean (default `False`). If `True`, assumes `y_pred` are raw logits (pre-sigmoid values) and applies sigmoid internally for numerical stability. If `False` (default), assumes `y_pred` are probabilities (output of sigmoid).
        -   **Example (Predicting customer churn: 0 or 1):**
            ```python
            # from tensorflow import keras
            # model.compile(optimizer='adam',
            #               loss=keras.losses.BinaryCrossentropy(from_logits=False), # If last layer is sigmoid
            #               # loss=keras.losses.BinaryCrossentropy(from_logits=True), # If last layer is linear
            #               metrics=['accuracy'])
            ```
    -   **Hinge Loss:**
        -   **Class:** `tf.keras.losses.Hinge()`
        -   **String:** `'hinge'`
        -   **Use Case:** Primarily used for training Support Vector Machines (SVMs) for "maximum-margin" classification. Typically, target $y_{true}$ should be -1 or 1.
- Multi-Class Classification Losses
    -   **Categorical Cross-Entropy:**
        -   **Class:** `tf.keras.losses.CategoricalCrossentropy()`
        -   **String:** `'categorical_crossentropy'`
        -   **Use Case:** For multi-class classification problems where target labels are **one-hot encoded** (e.g., `[0, 1, 0]` for class 1 out of 3). The model's last layer typically uses a [[Softmax_Function|softmax]] activation to output a probability distribution over classes.
        -   **Key Parameter:** `from_logits`: Boolean (default `False`). If `True`, assumes `y_pred` are raw logits and applies softmax internally.
        -   **Example (Classifying product images into 10 categories, labels are one-hot):**
            ```python
            # from tensorflow import keras
            # # y_train_one_hot = keras.utils.to_categorical(y_train_integers, num_classes=10)
            # model.compile(optimizer='adam',
            #               loss=keras.losses.CategoricalCrossentropy(from_logits=False), # If last layer is softmax
            #               metrics=['accuracy'])
            ```
    -   **Sparse Categorical Cross-Entropy:**
        -   **Class:** `tf.keras.losses.SparseCategoricalCrossentropy()`
        -   **String:** `'sparse_categorical_crossentropy'`
        -   **Use Case:** For multi-class classification problems where target labels are **integers** (e.g., 0, 1, 2, ... for classes). The model's last layer also typically uses a softmax activation. This avoids the need to manually one-hot encode integer labels.
        -   **Key Parameter:** `from_logits`: Boolean (default `False`).
        -   **Example (Classifying product images, labels are 0, 1, ..., 9):**
            ```python
            # from tensorflow import keras
            # model.compile(optimizer='adam',
            #               loss=keras.losses.SparseCategoricalCrossentropy(from_logits=False), # If last layer is softmax
            #               metrics=['accuracy'])
            ```
    -   **Kullback-Leibler Divergence (KL Divergence):**
        -   **Class:** `tf.keras.losses.KLDivergence()` or `tf.keras.losses.KLD`
        -   **String:** `'kullback_leibler_divergence'` or `'kld'`
        -   **Use Case:** Measures how one probability distribution diverges from a second, expected probability distribution. Used in VAEs (Variational Autoencoders) or when comparing distributions.

## Custom Loss Functions
You can define your own custom loss functions in Keras. A custom loss function should take `y_true` and `y_pred` as arguments and return a scalar loss value per sample. TensorFlow operations should be used for differentiability.

**Example: Custom Weighted MSE**
```python
import tensorflow as tf
from tensorflow import keras

# def my_custom_weighted_mse(y_true, y_pred):
#     # Assume y_true might have a third dimension for sample weights, or weights are passed differently
#     # For simplicity, let's define a simple weighting based on true value
#     squared_difference = tf.square(y_true - y_pred)
#     # Example: Penalize errors more for larger true values (conceptual)
#     weights = tf.cast(y_true > 50, tf.float32) * 1.5 + 0.5 # Higher weight if y_true > 50
#     weighted_squared_difference = weights * squared_difference
#     return tf.reduce_mean(weighted_squared_difference, axis=-1) # Average over last axis

# model.compile(optimizer='adam', loss=my_custom_weighted_mse)
```

## Choosing a Loss Function
-   **Regression:** Start with `MeanSquaredError` or `MeanAbsoluteError`. Consider `Huber` if outliers are an issue. `MAPE` if percentage error is important.
-   **Binary Classification:** `BinaryCrossentropy` is standard.
-   **Multi-Class Classification:**
    -   `SparseCategoricalCrossentropy` if labels are integers.
    -   `CategoricalCrossentropy` if labels are one-hot encoded.
-   **`from_logits=True`:** Generally recommended for numerical stability when the model's last layer produces raw scores (logits) without an activation function (like sigmoid or softmax). The loss function will then apply the appropriate transformation internally.

The loss function is a critical choice as it directly defines what the model aims to optimize during training.

---