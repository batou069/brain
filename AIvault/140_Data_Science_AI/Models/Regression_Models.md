---
tags:
  - data_science
  - machine_learning
  - supervised_learning
  - regression
  - model
  - concept
aliases:
  - Regression Algorithms
related:
  - "[[Supervised_Learning]]"
  - "[[Model_Evaluation]]"
  - "[[Linear_Regression]]"
  - "[[Polynomial_Regression]]"
  - "[[L1_L2_Regularization]]"
worksheet:
  - WS_Math_Foundations_2
date_created: 2025-08-07
---
# Regression Models

## Definition
**Regression** is a type of [[Supervised_Learning|supervised learning]] task where the goal is to predict a continuous numerical value (the target or dependent variable) based on a set of input features (independent variables).

**Regression models** are the algorithms used to perform regression analysis. They learn a function that maps input features to a continuous output.

## Common Regression Models
[list2tab|#Regression Models]
- Linear Regression
    - **Description:** The simplest form of regression. It models the relationship between the dependent variable and one or more independent variables by fitting a linear equation to the observed data.
    - **Equation (Simple):** $y = \beta_0 + \beta_1 x + \epsilon$
    - **Equation (Multiple):** $y = \beta_0 + \beta_1 x_1 + \dots + \beta_p x_p + \epsilon$
    - **Strengths:** Simple, interpretable, fast to train.
    - **Weaknesses:** Assumes a linear relationship between features and target.
- Polynomial Regression
    - **Description:** A form of linear regression where the relationship between the independent variable $x$ and the dependent variable $y$ is modeled as an $n$-th degree polynomial in $x$.
    - **Equation:** $y = \beta_0 + \beta_1 x + \beta_2 x^2 + \dots + \beta_n x^n + \epsilon$
    - **Strengths:** Can model non-linear relationships.
    - **Weaknesses:** Prone to [[Overfitting_Underfitting|overfitting]], especially with high-degree polynomials.
- Ridge Regression
    - **Description:** A regularized version of linear regression that includes an [[L1_L2_Regularization|L2 regularization]] penalty.
    - **Strengths:** Reduces model complexity and prevents overfitting by shrinking coefficients. More stable than linear regression when features are correlated.
- Lasso Regression
    - **Description:** A regularized version of linear regression that includes an [[L1_L2_Regularization|L1 regularization]] penalty.
    - **Strengths:** Can perform automatic feature selection by shrinking some coefficients to exactly zero.
- Support Vector Regression (SVR)
    - **Description:** An adaptation of Support Vector Machines (SVM) for regression. It tries to find a function that deviates from the target values by a value no greater than a margin $\epsilon$ for as many training points as possible.
    - **Strengths:** Effective in high-dimensional spaces, robust to outliers (depending on the kernel and loss function).
- Decision Tree Regression
    - **Description:** A tree-based model that predicts the value of a target variable by learning simple decision rules inferred from the data features. The prediction is the average of the target values in the leaf node.
    - **Strengths:** Easy to understand and interpret, can capture non-linear relationships.
    - **Weaknesses:** Prone to overfitting, can be unstable.
- Ensemble Methods
    - **Description:** Combine multiple individual models (often decision trees) to produce a more robust and accurate prediction.
    - **Examples:**
        - **Random Forest Regression:** An ensemble of decision trees built using bagging.
        - **Gradient Boosting Regression (e.g., GBR, XGBoost, LightGBM):** An ensemble method that builds trees sequentially, where each new tree corrects the errors of the previous one.
    - **Strengths:** Typically provide state-of-the-art performance, robust to overfitting.

## Evaluation Metrics
The performance of regression models is assessed using metrics that measure the difference between the predicted values ($\hat{y}_i$) and the actual values ($y_i$). Common metrics include:
- **Mean Absolute Error (MAE):** $ \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i| $
- **Mean Squared Error (MSE):** $ \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 $
- **Root Mean Squared Error (RMSE):** $ \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2} $
- **R-squared ($R^2$) (Coefficient of Determination):** Measures the proportion of the variance in the dependent variable that is predictable from the independent variables. Values range from $-\infty$ to 1 (higher is better).

See [[Model_Evaluation]].

---