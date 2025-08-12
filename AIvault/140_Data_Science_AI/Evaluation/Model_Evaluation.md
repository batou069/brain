---
tags:
  - data_science
  - machine_learning
  - evaluation
  - metrics
  - concept
aliases:
  - Performance Metrics
  - Model Assessment
related:
  - "[[Regression_Models]]"
  - "[[Classification_Models]]"
  - "[[Clustering_Methods]]"
  - "[[Cross_Validation]]"
  - "[[Confusion_Matrix]]"
worksheet:
  - WS_Math_Foundations_2
date_created: 2025-08-07
---
# Model Evaluation

## Definition
**Model evaluation** is the process of using various metrics to understand and quantify the performance of a trained machine learning model. It is a critical step in the model development lifecycle, used to select the best model, tune its hyperparameters, and assess its ability to generalize to new, unseen data.

The choice of evaluation metrics depends heavily on the type of machine learning task (e.g., regression, classification, clustering).

## Evaluation for Supervised Learning
In [[Supervised_Learning|supervised learning]], we have ground truth labels, making evaluation relatively straightforward. We compare the model's predictions ($\hat{y}$) with the true labels ($y$).

### Metrics for [[Regression_Models|Regression]]
These metrics measure the magnitude of the error between continuous predicted and actual values.
- **Mean Absolute Error (MAE):** The average of the absolute differences between predictions and actual values. Less sensitive to outliers than MSE.
  $$ \text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i| $$
- **Mean Squared Error (MSE):** The average of the squared differences. Penalizes larger errors more heavily.
  $$ \text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 $$
- **Root Mean Squared Error (RMSE):** The square root of the MSE. It is in the same units as the target variable, making it more interpretable.
  $$ \text{RMSE} = \sqrt{\text{MSE}} $$
- **R-squared ($R^2$) (Coefficient of Determination):** Represents the proportion of variance in the dependent variable that is explained by the model. Ranges from $-\infty$ to 1.
  $$ R^2 = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2} $$

### Metrics for [[Classification_Models|Classification]]
These metrics are often derived from a [[Confusion_Matrix|confusion matrix]], which tabulates the number of correct and incorrect predictions for each class.
- **Accuracy:** The ratio of correct predictions to the total number of predictions. Can be misleading for imbalanced datasets.
  $$ \text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN} $$
- **Precision:** Of all the instances the model predicted as positive, what fraction were actually positive? (Measures exactness).
  $$ \text{Precision} = \frac{TP}{TP + FP} $$
- **Recall (Sensitivity, True Positive Rate):** Of all the actual positive instances, what fraction did the model correctly identify? (Measures completeness).
  $$ \text{Recall} = \frac{TP}{TP + FN} $$
- **F1-Score:** The harmonic mean of Precision and Recall. Useful when you need a balance between the two.
  $$ F1 = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}} $$
- **Specificity (True Negative Rate):** Of all the actual negative instances, what fraction did the model correctly identify?
  $$ \text{Specificity} = \frac{TN}{TN + FP} $$
- **AUC-ROC Curve:** The Area Under the Receiver Operating Characteristic Curve plots the True Positive Rate (Recall) vs. the False Positive Rate at various threshold settings. AUC represents the model's ability to distinguish between classes. An AUC of 1 is perfect, while 0.5 is no better than random guessing.

## Evaluation for Unsupervised Learning
Evaluation is more challenging for [[Unsupervised_Learning|unsupervised learning]] as there are no ground truth labels.

### Metrics for [[Clustering_Methods|Clustering]]
- **Internal Metrics (No ground truth needed):**
    - **Silhouette Score:** Measures how well-separated clusters are. A score close to +1 indicates dense, well-separated clusters.
    - **Calinski-Harabasz Index:** Based on the ratio of between-cluster dispersion to within-cluster dispersion. Higher is better.
    - **Davies-Bouldin Index:** Based on a ratio of within-cluster to between-cluster separation. Lower is better.
- **External Metrics (Requires ground truth labels for comparison):**
    - **Adjusted Rand Index (ARI):** Measures the similarity between true and predicted clusterings, corrected for chance.
    - **Homogeneity, Completeness, V-measure.**

## Validation Techniques
- **Train-Test Split:** The simplest technique, where the data is split into a training set and a single hold-out test set.
- **[[Cross_Validation|Cross-Validation (CV)]]:** A more robust technique where the data is split into multiple "folds". The model is trained and evaluated multiple times, with a different fold used as the test set each time. The results are then averaged. This gives a more reliable estimate of the model's performance on unseen data.
    - **K-Fold Cross-Validation** is the most common type.

---