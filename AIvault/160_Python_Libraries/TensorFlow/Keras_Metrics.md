---
tags:
  - python
  - tensorflow
  - tf
  - keras
  - neural_networks
  - metrics
  - model_evaluation
  - accuracy
  - precision
  - recall
  - concept
  - example
aliases:
  - tf.keras.metrics
  - Keras Evaluation Metrics
related:
  - "[[Keras_API_in_TensorFlow]]"
  - "[[Keras_Loss_Functions]]"
  - "[[Model_Evaluation_Metrics]]"
  - "[[Sklearn_Metrics]]"
worksheet:
  - WS_DeepLearning_1
date_created: 2025-06-11
---
# Keras: Metrics (`tf.keras.metrics`)

**Metrics** in Keras (`tf.keras.metrics`) are used to monitor and evaluate the performance of your machine learning model during training and testing. Unlike [[Keras_Loss_Functions|loss functions]] (which are optimized/minimized during training), metrics are primarily for human interpretation and understanding how well the model is performing on a specific aspect.

Metrics are specified in the `metrics` argument of the `model.compile()` method and are reported during training (`model.fit()`) and evaluation (`model.evaluate()`).

## Key Characteristics of Metrics
-   **Not Optimized Directly:** The training process directly optimizes the loss function, not the metrics. However, metrics should ideally improve as the loss decreases.
-   **Problem-Specific:** The choice of metrics depends on the type of problem (classification, regression) and the specific goals.
-   **Stateful Objects:** Keras metrics are stateful objects. They accumulate values over batches during an epoch (or evaluation) and then compute the final metric result.
    -   `update_state()`: Adds new observations.
    -   `result()`: Computes and returns the current metric value.
    -   `reset_state()`: Clears the accumulated state.
    (You usually don't call these directly when using `model.compile` and `model.fit`/`evaluate`.)

## Common Metrics in `tf.keras.metrics`
Keras provides metrics as classes or as string identifiers.

[list2tab|#Keras Metrics]
- Classification Metrics
    -   **Accuracy:**
        -   **Class:** `tf.keras.metrics.Accuracy()`
        -   **String:** `'accuracy'` or `'acc'`
        -   **Purpose:** Proportion of correct predictions. Suitable for balanced datasets.
        -   For multi-class with integer labels, use `SparseCategoricalAccuracy`.
    -   **Binary Accuracy:**
        -   **Class:** `tf.keras.metrics.BinaryAccuracy()`
        -   **String:** `'binary_accuracy'`
        -   **Purpose:** Accuracy for binary classification tasks (output is a single probability).
    -   **Categorical Accuracy:**
        -   **Class:** `tf.keras.metrics.CategoricalAccuracy()`
        -   **String:** `'categorical_accuracy'`
        -   **Purpose:** Accuracy for multi-class classification where labels are **one-hot encoded**.
    -   **Sparse Categorical Accuracy:**
        -   **Class:** `tf.keras.metrics.SparseCategoricalAccuracy()`
        -   **String:** `'sparse_categorical_accuracy'`
        -   **Purpose:** Accuracy for multi-class classification where labels are **integers**.
    -   **Precision:**
        -   **Class:** `tf.keras.metrics.Precision()`
        -   **String:** `'precision'` (can be ambiguous, better to use class)
        -   **Purpose:** TP / (TP + FP). Of all samples predicted as positive, what fraction was actually positive? Important when False Positives are costly.
        -   **Key Arg:** `thresholds` (for binary), `top_k` (for multi-label), `class_id` (for specific class in multi-class).
    -   **Recall (Sensitivity):**
        -   **Class:** `tf.keras.metrics.Recall()`
        -   **String:** `'recall'` (can be ambiguous)
        -   **Purpose:** TP / (TP + FN). Of all actual positive samples, what fraction did the model correctly identify? Important when False Negatives are costly.
    -   **AUC (Area Under the ROC Curve):**
        -   **Class:** `tf.keras.metrics.AUC()`
        -   **String:** `'AUC'` (can be ambiguous)
        -   **Purpose:** Measures the ability of a classifier to distinguish between classes. See [[ROC_Curve_AUC]].
        -   **Key Args:** `num_thresholds`, `curve` (`'ROC'` or `'PR'`), `multi_label`.
    -   **TruePositives, FalsePositives, TrueNegatives, FalseNegatives:**
        -   Classes: `tf.keras.metrics.TruePositives()`, etc.
        -   Purpose: Count these basic confusion matrix components.
    -   **F1-Score (Conceptual - often calculated from Precision/Recall or via custom metric):**
        -   While not a direct built-in string metric like 'accuracy', F1 can be implemented as a custom metric or derived. Some libraries like `tensorflow_addons` provide it.
- Regression Metrics
    -   **Mean Squared Error (MSE):**
        -   **Class:** `tf.keras.metrics.MeanSquaredError()`
        -   **String:** `'mean_squared_error'` or `'mse'`
        -   **Purpose:** Average of squared differences between true and predicted values.
    -   **Root Mean Squared Error (RMSE):**
        -   **Class:** `tf.keras.metrics.RootMeanSquaredError()`
        -   **String:** `'root_mean_squared_error'` or `'rmse'`
        -   **Purpose:** Square root of MSE, in the same units as the target.
    -   **Mean Absolute Error (MAE):**
        -   **Class:** `tf.keras.metrics.MeanAbsoluteError()`
        -   **String:** `'mean_absolute_error'` or `'mae'`
        -   **Purpose:** Average of absolute differences.
    -   **Mean Absolute Percentage Error (MAPE):**
        -   **Class:** `tf.keras.metrics.MeanAbsolutePercentageError()`
        -   **String:** `'mean_absolute_percentage_error'` or `'mape'`
    -   **Cosine Similarity:**
        -   **Class:** `tf.keras.metrics.CosineSimilarity()`
        -   **String:** `'cosine_similarity'`
        -   **Purpose:** Measures cosine of the angle between true and predicted vectors. Useful for comparing directions (e.g., in embeddings).
    -   **R^2 Score (Coefficient of Determination - `tf.keras.metrics.R2Score` in TF Addons or custom):**
        -   Not directly in core `tf.keras.metrics` as a simple string, but can be implemented or found in `tensorflow_addons.metrics.R2Score`.

## Using Metrics in `model.compile()`
You pass a list of metrics (as strings or metric class instances) to the `metrics` argument of `model.compile()`.

**Example (Product Category Classification):**
```python
import tensorflow as tf
from tensorflow import keras
import numpy as np

# Conceptual data (num_features=5, num_classes=3)
# X_train = np.random.rand(100, 5).astype(np.float32)
# y_train_int = np.random.randint(0, 3, 100) # Integer labels

# model = keras.Sequential([
#     keras.layers.Dense(32, activation='relu', input_shape=(5,)),
#     keras.layers.Dense(3, activation='softmax') # Output for 3 classes
# ])

# Compile with various metrics
# model.compile(
#     optimizer=keras.optimizers.Adam(0.001),
#     loss=keras.losses.SparseCategoricalCrossentropy(),
#     metrics=[
#         'accuracy', # Simple string for common one
#         keras.metrics.SparseCategoricalAccuracy(name='sparse_acc'), # Explicit class instance with custom name
#         keras.metrics.Precision(name='precision_macro', class_id=None), # For multi-class, often need to specify averaging or class_id
#         keras.metrics.Recall(name='recall_macro', class_id=None),
#         keras.metrics.AUC(name='auc_roc_ovr', multi_label=False, curve='ROC') # One-vs-Rest for multi-class ROC AUC
#     ]
# )

# print("Model compiled. Conceptual training would show these metrics.")
# Conceptual training call:
# history = model.fit(X_train, y_train_int, epochs=2, batch_size=16, verbose=0)
# if history:
#     print("\nMetrics from training history (conceptual):")
#     for metric_name in history.history.keys():
#         print(f"- {metric_name}: {history.history[metric_name][-1]:.4f}") # Last epoch value

# Conceptual evaluation call:
# X_test = np.random.rand(20, 5).astype(np.float32)
# y_test_int = np.random.randint(0, 3, 20)
# eval_results = model.evaluate(X_test, y_test_int, verbose=0)
# print("\nEvaluation results (conceptual):")
# for name, value in zip(model.metrics_names, eval_results):
#     print(f"- {name}: {value:.4f}")
```
**Note on Multi-Class Precision/Recall/AUC:**
For multi-class problems, metrics like Precision, Recall, and AUC often require specifying how to average across classes (e.g., 'macro', 'micro', 'weighted') or which specific class to evaluate if not done globally. Keras's default behavior for these might vary or they might be more suited for binary contexts unless configured for multi-class (e.g., `AUC(multi_label=True, num_labels=...)` or by using one-vs-rest approaches). `Precision(class_id=...)` or `Recall(class_id=...)` can focus on a specific class. `tensorflow_addons` often provides more comprehensive multi-class versions.

## Custom Metrics
You can create custom metrics by:
1.  Writing a Python function that takes `y_true` and `y_pred` and returns a scalar tensor.
2.  Subclassing `tf.keras.metrics.Metric` for more complex stateful metrics.

**Example: Custom F1 Score (Simplified for Binary)**
```python
# import tensorflow as tf
# from tensorflow import keras

# def f1_metric(y_true, y_pred):
#     # For binary case, assuming y_pred are probabilities
#     y_pred_binary = tf.cast(y_pred > 0.5, tf.float32)
#     true_positives = tf.reduce_sum(y_true * y_pred_binary)
#     predicted_positives = tf.reduce_sum(y_pred_binary)
#     possible_positives = tf.reduce_sum(y_true)
    
#     precision = true_positives / (predicted_positives + keras.backend.epsilon())
#     recall = true_positives / (possible_positives + keras.backend.epsilon())
    
#     f1 = 2 * (precision * recall) / (precision + recall + keras.backend.epsilon())
#     return f1

# model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy', f1_metric])
```

Metrics provide valuable insights into different aspects of a model's performance beyond the single scalar value of the loss function, helping to understand its strengths and weaknesses.

---