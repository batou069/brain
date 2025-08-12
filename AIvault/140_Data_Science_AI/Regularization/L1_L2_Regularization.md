---
tags:
  - data_science
  - machine_learning
  - regularization
  - lasso
  - ridge
  - overfitting
  - concept
aliases:
  - L1 Regularization
  - L2 Regularization
  - Lasso Regression
  - Ridge Regression
  - Weight Decay
related:
  - "[[Overfitting_Underfitting]]"
  - "[[Bias_Variance_Tradeoff]]"
  - "[[Loss_Function]]"
  - "[[p-norm]]"
  - "[[Linear_Regression]]"
worksheet:
  - WS_Math_Foundations_2
date_created: 2025-08-07
---
# L1 and L2 Regularization

## Definition
**Regularization** is a set of techniques used in machine learning to prevent [[Overfitting_Underfitting|overfitting]]. It works by adding a penalty term to the [[Loss_Function|loss function]], which discourages the model from learning overly complex patterns or assigning excessive weights to features.

The two most common types of regularization are L1 (Lasso) and L2 (Ridge). They are based on adding a penalty proportional to the [[p-norm|L1 norm]] or [[p-norm|L2 norm]] of the model's weight vector $\mathbf{w}$.

The general form of the regularized loss function is:
$$ \text{New Loss} = \text{Original Loss} + \lambda \cdot (\text{Regularization Term}) $$
- **Original Loss:** The function we want to minimize (e.g., Mean Squared Error for regression).
- **$\lambda$ (lambda):** The regularization parameter (a hyperparameter). It controls the strength of the penalty.
    - $\lambda = 0$: No regularization.
    - $\lambda \to \infty$: High regularization, weights are pushed towards zero.
- **Regularization Term:** The penalty based on the model weights.

## L2 Regularization (Ridge / Weight Decay)
- **Regularization Term:** The squared L2 norm of the weight vector.
  $$ R(\mathbf{w}) = \|\mathbf{w}\|_2^2 = \sum_{j=1}^{p} w_j^2 $$
  (Note: The bias term $w_0$ is usually not regularized).
- **Loss Function (for Linear Regression):**
  $$ L_{\text{Ridge}}(\mathbf{w}) = \sum_{i=1}^{n} (y_i - \mathbf{w}^T\mathbf{x}_i)^2 + \lambda \sum_{j=1}^{p} w_j^2 $$
- **Effect:**
    - Penalizes large weight coefficients.
    - Encourages the model to use all features but with smaller, more distributed weights.
    - It **shrinks** the coefficients towards zero but does not force them to be exactly zero (unless $\lambda \to \infty$).
    - Geometrically, it constrains the solution to lie within an L2-ball (a hypersphere).
    - The resulting loss function is convex, making it easy to optimize.
- **Common Name:** **Ridge Regression** when applied to linear regression. Also known as **Weight Decay** in the context of neural networks.

## L1 Regularization (Lasso)
- **Regularization Term:** The L1 norm of the weight vector.
  $$ R(\mathbf{w}) = \|\mathbf{w}\|_1 = \sum_{j=1}^{p} |w_j| $$
- **Loss Function (for Linear Regression):**
  $$ L_{\text{Lasso}}(\mathbf{w}) = \sum_{i=1}^{n} (y_i - \mathbf{w}^T\mathbf{x}_i)^2 + \lambda \sum_{j=1}^{p} |w_j| $$
- **Effect:**
    - Also penalizes large weight coefficients.
    - A key difference is that L1 regularization can shrink some coefficients to be **exactly zero**.
    - This makes L1 regularization useful for **automatic feature selection**, as it effectively removes irrelevant features from the model.
    - Geometrically, it constrains the solution to lie within an L1-ball (a hyperdiamond/rhombus). The sharp corners of this shape make it likely that the optimal solution will lie on an axis, where some weights are zero.
- **Common Name:** **Lasso Regression** (Least Absolute Shrinkage and Selection Operator) when applied to linear regression.

## Comparison
[list2tab|#L1 vs L2]
- Property
    - L1 (Lasso)
        - L2 (Ridge)
- Penalty Term
    - $\lambda \sum |w_j|$
        - $\lambda \sum w_j^2$
- Feature Selection
    - Yes (produces sparse models)
        - No (shrinks weights, doesn't zero them out)
- Solution
    - Can be non-unique, computationally harder
        - Unique, closed-form solution exists
- Robustness
    - Can be less stable with correlated features
        - Generally more stable with correlated features
- Use Case
    - When you suspect many features are irrelevant
        - When you believe all features are relevant

**Elastic Net** is a hybrid model that combines both L1 and L2 penalties, benefiting from both feature selection and stability with correlated features.

## Python Example
Let's use Scikit-learn to see the effect of Lasso and Ridge on a regression problem with some irrelevant features.

```python
import numpy as np
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

# 1. Create synthetic data
np.random.seed(42)
n_samples, n_features = 50, 200
X = np.random.randn(n_samples, n_features)
# Create a target y where only the first 10 features are relevant
coef = 3 * np.random.randn(n_features)
inds = np.arange(n_features)
np.random.shuffle(inds)
coef[inds[10:]] = 0  # Zero out all but 10 coefficients
y = np.dot(X, coef)
y += 0.01 * np.random.normal(size=n_samples) # Add some noise

# 2. Fit different models
# Use a pipeline to scale data before fitting
lr = make_pipeline(StandardScaler(), LinearRegression())
ridge = make_pipeline(StandardScaler(), Ridge(alpha=1.0)) # alpha is lambda
lasso = make_pipeline(StandardScaler(), Lasso(alpha=1.0))

lr.fit(X, y)
ridge.fit(X, y)
lasso.fit(X, y)

# 3. Inspect the coefficients
lr_coef = lr.named_steps['linearregression'].coef_
ridge_coef = ridge.named_steps['ridge'].coef_
lasso_coef = lasso.named_steps['lasso'].coef_

print("--- Number of non-zero coefficients ---")
print(f"Linear Regression: {np.sum(lr_coef != 0)}")
print(f"Ridge Regression (alpha=1): {np.sum(ridge_coef != 0)}")
print(f"Lasso Regression (alpha=1): {np.sum(lasso_coef != 0)}")
print(f"(True number of non-zero coefficients was 10)")

# Expected Output:
# --- Number of non-zero coefficients ---
# Linear Regression: 200
# Ridge Regression (alpha=1): 200
# Lasso Regression (alpha=1): 4
# (True number of non-zero coefficients was 10)
```
The output shows that Linear Regression uses all 200 features. Ridge also uses all 200, but their magnitudes would be smaller. Lasso, with its L1 penalty, correctly identified that most features were irrelevant and shrunk their coefficients to exactly zero, resulting in a sparse model with only 4 non-zero coefficients.

---