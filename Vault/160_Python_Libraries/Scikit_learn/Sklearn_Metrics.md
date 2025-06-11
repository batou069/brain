---
tags:
  - python
  - scikit_learn
  - sklearn
  - machine_learning
  - metrics
  - model_evaluation
  - classification_metrics
  - regression_metrics
  - clustering_metrics
  - concept
  - example
aliases:
  - Scikit-learn Evaluation Metrics
  - sklearn.metrics
related:
  - "[[160_Python_Libraries/Scikit_learn/_Scikit_learn_MOC|_Scikit_learn_MOC]]"
  - "[[Model_Evaluation_Metrics]]"
  - "[[Confusion_Matrix]]"
  - "[[ROC_Curve_AUC]]"
worksheet:
  - WS_ML_Libraries_1
date_created: 2025-06-09
---
# Scikit-learn: Model Evaluation Metrics (`sklearn.metrics`)

Evaluating the performance of machine learning models is crucial for understanding their effectiveness and comparing different models. The `sklearn.metrics` module in Scikit-learn provides a wide range of functions for calculating various evaluation metrics for classification, regression, and clustering tasks.

## Common Metric Types

[list2tab|#Metric Types]
- Classification Metrics
    - **Purpose:** Assess the performance of classification models.
    - **Common Metrics:**
        -   **`accuracy_score`**: Proportion of correctly classified samples. Most intuitive, but can be misleading for imbalanced datasets.
            $$ \text{Accuracy} = \frac{\text{Number of correct predictions}}{\text{Total number of predictions}} $$
        -   **`precision_score`**: Ability of the classifier not to label a negative sample as positive. (TP / (TP + FP))
            $$ \text{Precision} = \frac{\text{True Positives (TP)}}{\text{True Positives (TP) + False Positives (FP)}} $$
        -   **`recall_score` (Sensitivity, True Positive Rate)**: Ability of the classifier to find all the positive samples. (TP / (TP + FN))
            $$ \text{Recall} = \frac{\text{True Positives (TP)}}{\text{True Positives (TP) + False Negatives (FN)}} $$
        -   **`f1_score`**: Weighted average (harmonic mean) of Precision and Recall. Good for imbalanced classes.
            $$ F1 = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}} $$
        -   **`confusion_matrix`**: A table showing true vs. predicted classes (TP, FP, FN, TN).
        -   **`classification_report`**: Text report showing main classification metrics (precision, recall, F1-score, support) per class.
        -   **`roc_auc_score` (Area Under the ROC Curve)**: Measures the ability of a classifier to distinguish between classes. ROC curve plots True Positive Rate vs. False Positive Rate. AUC = 1 is perfect, 0.5 is random. Requires probability scores or decision function values. See [[ROC_Curve_AUC]].
        -   `roc_curve`: Computes Receiver Operating Characteristic (ROC) curve.
        -   `precision_recall_curve`: Computes precision-recall pairs for different probability thresholds.
        -   `log_loss` (Logistic Loss or Cross-Entropy Loss): Loss function used in logistic regression and neural networks.
    - **Example (Evaluating a product category classifier):**
        ```python
        from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report, roc_auc_score
        from sklearn.linear_model import LogisticRegression
        from sklearn.model_selection import train_test_split
        import pandas as pd
        import numpy as np

        # Conceptual product data: features and multi-class category
        X_prod_features = pd.DataFrame(np.random.rand(100, 5))
        y_prod_category = pd.Series(np.random.randint(0, 3, 100)) # 3 classes: 0, 1, 2

        # X_train, X_test, y_train, y_test = train_test_split(X_prod_features, y_prod_category, test_size=0.3, random_state=42)
        # model = LogisticRegression(solver='liblinear', multi_class='ovr') # One-vs-Rest for multi-class
        # model.fit(X_train, y_train)
        # y_pred = model.predict(X_test)
        # y_pred_proba = model.predict_proba(X_test) # For ROC AUC with multi-class 'ovr'

        # print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
        # # For multiclass, precision/recall/f1 need an averaging strategy (e.g., 'macro', 'weighted')
        # print(f"Precision (macro): {precision_score(y_test, y_pred, average='macro'):.4f}")
        # print(f"Recall (macro): {recall_score(y_test, y_pred, average='macro'):.4f}")
        # print(f"F1-score (macro): {f1_score(y_test, y_pred, average='macro'):.4f}")
        # print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
        # print("\nClassification Report:\n", classification_report(y_test, y_pred, target_names=['Cat A', 'Cat B', 'Cat C']))
        
        # ROC AUC for multi-class requires one-vs-rest or one-vs-one approach
        # For 'ovr' and 3 classes, y_pred_proba will have 3 columns
        # if y_pred_proba.shape[1] == 3: # Ensure it's multi-class probabilities
        #     try:
        #         roc_auc = roc_auc_score(y_test, y_pred_proba, multi_class='ovr', average='macro')
        #         print(f"ROC AUC (macro OVR): {roc_auc:.4f}")
        #     except ValueError as e:
        #         print(f"Could not compute ROC AUC for multi-class: {e}") # e.g. if only one class present in y_test
        ```
- Regression Metrics
    - **Purpose:** Assess the performance of regression models.
    - **Common Metrics:**
        -   **`mean_absolute_error` (MAE)**: Average of the absolute differences between predicted and actual values.
            $$ MAE = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i| $$
        -   **`mean_squared_error` (MSE)**: Average of the squared differences between predicted and actual values. Penalizes larger errors more.
            $$ MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 $$
        -   **`root_mean_squared_error` (RMSE)**: Square root of MSE. In the same units as the target variable. (Calculated as `np.sqrt(mean_squared_error(...))`).
        -   **`r2_score` (R-squared, Coefficient of Determination)**: Proportion of the variance in the dependent variable that is predictable from the independent variables. Ranges from $-\infty$ to 1 (1 is perfect, 0 means model does no better than predicting the mean).
            $$ R^2 = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2} $$
        -   `median_absolute_error`: Robust to outliers.
        -   `explained_variance_score`: Measures the proportion to which a model accounts for the variance of datasets.
    - **Example (Evaluating product price prediction):**
        ```python
        from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
        from sklearn.linear_model import LinearRegression
        import numpy as np
        import pandas as pd

        # Conceptual product data
        X_product_features = pd.DataFrame(np.random.rand(100, 3), columns=['feat1', 'feat2', 'feat3'])
        y_product_price = pd.Series(50 + X_product_features['feat1']*20 + X_product_features['feat2']*30 + np.random.randn(100)*10)
        
        # X_train, X_test, y_train, y_test = train_test_split(X_product_features, y_product_price, test_size=0.3, random_state=42)
        # reg_model = LinearRegression()
        # reg_model.fit(X_train, y_train)
        # y_pred_reg = reg_model.predict(X_test)

        # print(f"Mean Absolute Error (MAE): {mean_absolute_error(y_test, y_pred_reg):.2f}")
        # print(f"Mean Squared Error (MSE): {mean_squared_error(y_test, y_pred_reg):.2f}")
        # print(f"Root Mean Squared Error (RMSE): {np.sqrt(mean_squared_error(y_test, y_pred_reg)):.2f}")
        # print(f"R-squared (R2 Score): {r2_score(y_test, y_pred_reg):.4f}")
        ```
- Clustering Metrics
    - **Purpose:** Assess the quality of clustering algorithms. Evaluation is more complex as ground truth labels are often unavailable.
    - **Types:**
        -   **With Ground Truth Labels (External Measures):**
            -   `adjusted_rand_score`
            -   `normalized_mutual_info_score`
            -   `fowlkes_mallows_score`
        -   **Without Ground Truth Labels (Internal Measures):**
            -   `silhouette_score`: Measures how similar an object is to its own cluster (cohesion) compared to other clusters (separation). Ranges from -1 to 1 (higher is better).
            -   `davies_bouldin_score`: Ratio of within-cluster scatter to between-cluster separation. Lower is better (closer to 0).
            -   `calinski_harabasz_score` (Variance Ratio Criterion). Higher is better.
    - **Example (Evaluating customer segments from K-Means):**
        ```python
        from sklearn.metrics import silhouette_score, davies_bouldin_score
        from sklearn.cluster import KMeans
        import numpy as np
        import pandas as pd

        # Conceptual customer data (e.g., from K-Means example in Sklearn_Clustering)
        X_customer_behavior = pd.DataFrame(np.random.rand(100, 2), columns=['spend', 'frequency'])
        # Assume X_scaled is the scaled version of X_customer_behavior

        # kmeans_model = KMeans(n_clusters=3, random_state=42, n_init='auto')
        # cluster_labels = kmeans_model.fit_predict(X_scaled) # Assuming X_scaled is defined

        # if len(np.unique(cluster_labels)) > 1: # Metrics require at least 2 clusters
        #     sil_score = silhouette_score(X_scaled, cluster_labels)
        #     db_score = davies_bouldin_score(X_scaled, cluster_labels)
        #     print(f"Silhouette Score: {sil_score:.4f}")
        #     print(f"Davies-Bouldin Score: {db_score:.4f}")
        # else:
        #     print("Not enough clusters to calculate silhouette or Davies-Bouldin score.")
        ```

## Choosing the Right Metric
-   The choice of metric depends heavily on the **problem domain, the business objective, and the characteristics of the data** (e.g., class imbalance in classification).
-   For classification, if classes are imbalanced, accuracy can be misleading. Precision, recall, F1-score, or ROC AUC are often more informative.
-   For regression, MAE is more interpretable in terms of average error magnitude, while MSE/RMSE penalize larger errors more heavily. R-squared indicates the proportion of variance explained.
-   Always consider multiple metrics to get a holistic view of model performance.

The `sklearn.metrics` module is indispensable for quantitatively assessing how well machine learning models perform.

---