# Chapter: Linear Regression

## Keywords

### 1. Linearity

**Linearity** is the core assumption in linear regression that the relationship between the independent variables (X) and the mean of the dependent variable (E[y]) is a straight line.

- This means that a one-unit change in a predictor variable results in a constant change in the response variable.
    
The model equation is a linear combination of the parameters: $\hat{y} = \beta_0 + \beta_1 x_1 + \dots + \beta_p x_p$.
    
- It’s important to note that the features themselves don’t have to be linear. A model like $\hat{y} = \beta_0 + \beta_1 x + \beta_2 x^2$ is still a linear model because it’s linear in the coefficients $\beta_i$.
    
- You can check for linearity by plotting residuals against predicted values or by plotting the response against each predictor individually.
    

Python

```
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Generate perfectly linear data
X = np.array([[1], [2], [3], [4], [5]])
y_linear = 2 * X.flatten() + 1

# Fit linear model
model = LinearRegression().fit(X, y_linear)
y_pred = model.predict(X)

# A residual plot shows no pattern, supporting the linearity assumption
residuals = y_linear - y_pred
plt.scatter(y_pred, residuals)
plt.axhline(y=0, color='r', linestyle='--')
plt.title("Residual Plot for Linear Data")
plt.xlabel("Predicted Values")
plt.ylabel("Residuals")
plt.show() # The points are randomly scattered around the zero line, indicating linearity.
```

**Linearity** refers to the assumption that the underlying relationship you're trying to model can be described with a straight line. It doesn't necessarily mean the raw data points must form a perfect line, but that the _average_ value of your target variable changes linearly as your input feature changes. This is the simplest and most fundamental assumption of linear regression. If the true relationship is curved, the linear model will be a poor approximation.

---

### 2. Model assumptions

**Model assumptions** in linear regression are a set of conditions that should be met for the model's results (especially the statistical inferences) to be reliable and accurate.

- The four key assumptions are often remembered by the acronym **LINE**:
    
    - **L**inearity: The relationship between predictors and the outcome is linear.
        
    - **I**ndependence: The errors (residuals) are independent of each other.
        
    - **N**ormality: The errors are normally distributed.
        
    - **E**qual variance (Homoscedasticity): The errors have constant variance at every level of the predictor variables.
        
- Violating these assumptions can lead to misleading or incorrect conclusions about the model's coefficients and their significance.
    

Python

```
# This code block demonstrates checking assumptions, not the assumption itself.
import numpy as np
import statsmodels.api as sm
from statsmodels.stats.diagnostic import het_breuschpagan
from statsmodels.stats.stattools import durbin_watson
import scipy.stats as stats
import matplotlib.pyplot as plt

# Generate and fit a model
X = np.random.rand(100, 1) * 10
y = 2 * X.flatten() + 1 + np.random.normal(0, 2, 100) # Data that meets assumptions
X_const = sm.add_constant(X)
model = sm.OLS(y, X_const).fit()
residuals = model.resid

# 1. Linearity: Checked visually with residual vs. fitted plot.
# 2. Independence: Durbin-Watson test. Value near 2 is good.
dw_stat = durbin_watson(residuals)
print(f"Durbin-Watson (Independence): {dw_stat:.2f}")

# 3. Normality: Q-Q plot. Points should be on the line.
sm.qqplot(residuals, line='45')
# plt.show()

# 4. Equal Variance: Breusch-Pagan test. High p-value (>0.05) is good.
_, p_value, _, _ = het_breuschpagan(residuals, model.model.exog)
print(f"Breusch-Pagan p-value (Homoscedasticity): {p_value:.3f}")
```

The **assumptions** of linear regression are the "rules of the game" that your data should follow for the model to work correctly and for you to trust the results. Think of them as a checklist: Is the relationship linear? Are the data points independent? Are the errors random and normally distributed? Do the errors have a consistent spread? If you can check off these boxes, you can be confident in your model's coefficients, p-values, and predictions. If not, you may need to transform your data or choose a different model.

---

### 3. Feature Engineering

See answer in the "Regressions" chapter. The concept is identical.

---

### 4. Loss function

A **loss function** (or cost function) is a function that quantifies the "cost" or "error" of a model's predictions by measuring the difference between the predicted values and the actual values.

- The goal of training a model is to find the set of parameters that **minimizes** this loss function.
    
- For linear regression, the most common loss function is the **Mean Squared Error (MSE)**.
    
- MSE is calculated as: $L(\hat{y}, y) = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$.
    
- The choice of loss function is critical as it defines what a "good" fit means and directly influences the final model parameters.
    

Python

```
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Actual values
y_true = np.array([2, 4, 6, 8])

# Predictions from a model
y_pred = np.array([2.5, 3.5, 6.2, 7.8])

# Calculate Mean Squared Error (MSE)
mse = mean_squared_error(y_true, y_pred)
print(f"Mean Squared Error (MSE): {mse:.2f}")

# Calculate Mean Absolute Error (MAE)
mae = mean_absolute_error(y_true, y_pred)
print(f"Mean Absolute Error (MAE): {mae:.2f}")
```

A **loss function** is the mathematical recipe that tells your model how bad its predictions are. For every prediction it makes, the loss function calculates a "penalty score"—the higher the score, the worse the prediction. During training, the model's entire goal is to adjust its internal parameters (like the slope and intercept in linear regression) over and over again to make this total penalty score as low as possible. It's the objective that guides the entire learning process.

---

### 5. Analytical solution

An **analytical solution** (or closed-form solution) is a solution to a problem that can be expressed in a precise mathematical formula.

- For Ordinary Least Squares (OLS) linear regression, an analytical solution exists for finding the optimal coefficients that minimize the sum of squared errors.
    
- This solution is known as the **Normal Equation**: $\hat{\beta} = (X^T X)^{-1} X^T y$.
    
- It provides the exact solution in a single calculation, without needing an iterative process like gradient descent.
    
- However, it can be computationally very expensive, especially for datasets with a large number of features, because it requires inverting a matrix $(X^T X)$, which is an $O(p^3)$ operation where p is the number of features.
    

Python

```
import numpy as np

# Sample data
X_raw = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3.9, 6.1, 8, 10.2])

# Add a column of ones to X for the intercept term
X_b = np.c_[np.ones((len(X_raw), 1)), X_raw]

# The Normal Equation: beta_hat = inv(X^T * X) * X^T * y
try:
    beta_analytical = np.linalg.inv(X_b.T @ X_b) @ X_b.T @ y
    print(f"Analytical solution for coefficients (intercept, slope): {beta_analytical}")
except np.linalg.LinAlgError:
    print("Matrix is not invertible.")

# For comparison with scikit-learn
from sklearn.linear_model import LinearRegression
model = LinearRegression().fit(X_raw.reshape(-1, 1), y)
print(f"Scikit-learn solution (intercept, slope): [{model.intercept_:.4f}, {model.coef_[0]:.4f}]")
```

An **analytical solution** is like having a direct formula to solve a problem. For linear regression, the "Normal Equation" is that magic formula. By plugging your data matrices (X and y) into this equation, you can calculate the exact best-fitting slope and intercept in one go, without any guessing or iteration. It's a mathematically elegant and precise way to solve the problem, but it can become slow and impractical if you have a massive number of features.

---

### 6. Optimization

**Optimization** is the process of finding the set of model parameters that minimizes the loss function.

- In machine learning, "learning" or "training" a model is fundamentally an optimization problem.
    
- There are two main approaches to optimization in linear regression:
    
    1. **Analytical solution**: Using the Normal Equation to solve for the parameters directly.
        
    2. **Iterative methods**: Algorithms like **Gradient Descent** that start with a random guess for the parameters and iteratively take small steps to reach the minimum of the loss function.
        
- Iterative methods are essential when an analytical solution is too computationally expensive or doesn't exist (as is the case for many complex models).
    

Python

```
# Scikit-learn's LinearRegression uses an analytical solver (scipy.linalg.lstsq).
# For an example of an iterative optimizer, we can use SGDRegressor.

import numpy as np
from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import StandardScaler

# Sample data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 3.9, 6.1, 8, 10.2])

# Gradient Descent works best with scaled features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Initialize the model which uses Stochastic Gradient Descent for optimization
# max_iter: number of passes over the data
# eta0: learning rate
sgd_model = SGDRegressor(max_iter=1000, tol=1e-3, eta0=0.1, random_state=42)
sgd_model.fit(X_scaled, y)

# Note: The coefficients are for the scaled data.
print(f"Coefficients from SGD optimization: {sgd_model.coef_}, Intercept: {sgd_model.intercept_}")
```

**Optimization** is the search for the best solution. In linear regression, the "best solution" means finding the slope and intercept that make the line fit the data as closely as possible. The "closeness" of the fit is measured by a loss function (like MSE). Optimization algorithms, like Gradient Descent, are the engines that drive this search. They systematically tweak the model's parameters, observe whether the loss goes down, and then adjust again, continuing this process until they find the parameter values that result in the lowest possible loss.

---

### 7. Ordinary Least Squares / Gradient Descent

**Ordinary Least Squares (OLS)** is a method for estimating the parameters in a linear regression model by minimizing the sum of the squared differences between the observed and predicted values, while **Gradient Descent** is an iterative optimization algorithm used to find that minimum.

- **OLS** is the _objective_ or the _method_. Its goal is to minimize the Sum of Squared Residuals (SSR): $SSR = \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$.
    
- **Gradient Descent** is the _algorithm_ or the _process_ to achieve that goal. It calculates the gradient (slope) of the loss function and takes a step in the opposite direction to move towards the minimum.
    
- The Normal Equation provides an analytical way to solve the OLS problem directly. Gradient Descent provides an iterative way.
    

Python

```
# OLS is the method that scikit-learn's LinearRegression implements.
# Gradient Descent is the optimizer used by SGDRegressor.

from sklearn.linear_model import LinearRegression, SGDRegressor
import numpy as np

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 3.9, 6.1, 8, 10.2])

# 1. OLS using an analytical solver
ols_model = LinearRegression()
ols_model.fit(X, y)
print(f"OLS (analytical) Intercept: {ols_model.intercept_:.4f}, Slope: {ols_model.coef_[0]:.4f}")

# 2. OLS using Gradient Descent for optimization
# Note: For this simple problem, results will be very similar.
# SGD needs to be configured (learning rate, etc.)
sgd_model = SGDRegressor(max_iter=1000, tol=1e-4, learning_rate='constant', eta0=0.05, random_state=42)
# SGD works with 1D y, but needs feature scaling for best performance, which we omit for this simple comparison.
sgd_model.fit(X, y.ravel())
print(f"OLS (Gradient Descent) Intercept: {sgd_model.intercept_[0]:.4f}, Slope: {sgd_model.coef_[0]:.4f}")
```

Think of **Ordinary Least Squares (OLS)** as the destination: it's the principle that the best-fitting line is the one that has the minimum possible sum of squared errors. **Gradient Descent** is one of the vehicles you can use to get to that destination. It's an algorithm that starts at a random point on the error surface and takes steps "downhill" until it reaches the lowest point (the OLS solution). The Normal Equation is another "vehicle"—a high-speed train that takes you directly to the destination in one step.

---

### 8. r squared

See answer in the "Regressions" chapter. The concept is identical.

---

### 9. Ridge/Lasso/ElasticNet

**Ridge, Lasso, and Elastic Net** are regularized versions of linear regression that add a penalty term to the loss function to prevent overfitting and handle multicollinearity.

- **Ridge Regression (L2 Regularization)**: Adds a penalty equal to the _square_ of the magnitude of the coefficients ($\alpha \sum \beta_j^2$). It shrinks large coefficients towards zero but never sets them exactly to zero.

- **Lasso Regression (L1 Regularization)**: Adds a penalty equal to the _absolute value_ of the magnitude of the coefficients ($\alpha \sum |\beta_j|$). It can shrink some coefficients to zero, performing automatic feature selection.

- **Elastic Net**: Combines Ridge and Lasso with both L1 and L2 penalty terms, balancing their benefits (handles correlated features better than Lasso while providing feature selection).
    

Python

```
import numpy as np
from sklearn.linear_model import Ridge, Lasso, ElasticNet

# Sample data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 3.9, 6.1, 8, 10.2])

# Alpha is the regularization strength parameter
alpha = 0.1

# Ridge (L2)
ridge_model = Ridge(alpha=alpha).fit(X, y)
print(f"Ridge Coef: {ridge_model.coef_[0]:.4f}")

# Lasso (L1)
lasso_model = Lasso(alpha=alpha).fit(X, y)
print(f"Lasso Coef: {lasso_model.coef_[0]:.4f}")

# ElasticNet (L1 + L2)
# l1_ratio defines the mix: 1.0 is Lasso, 0.0 is Ridge.
enet_model = ElasticNet(alpha=alpha, l1_ratio=0.5).fit(X, y)
print(f"ElasticNet Coef: {enet_model.coef_[0]:.4f}")
```

**Ridge, Lasso, and Elastic Net** are "disciplined" versions of linear regression. Standard linear regression can sometimes get over-excited and produce very large coefficients, especially if features are correlated or you have too many features (overfitting). These regularized models add a "penalty" to the objective function that punishes large coefficients. **Lasso** is a strict disciplinarian that can force some coefficients to be exactly zero, effectively kicking useless features out of the model. **Ridge** is a bit gentler, shrinking all coefficients towards zero but keeping them all in the model. **Elastic Net** is a flexible hybrid of the two.

## Questions

### 1. Why is Mean of Squared Errors (MSE) presented as the default loss function for linear regression?

MSE is the default loss function for several key reasons:

1. **Connection to Maximum Likelihood**: Minimizing the MSE is equivalent to maximizing the likelihood of the data under the assumption that the errors are **normally (Gaussian) distributed**. This provides a strong statistical foundation.
    
2. **Mathematical Convenience**: The squared term makes the loss function **differentiable and convex**. This guarantees that there is a single, global minimum, which can be found efficiently either by the analytical Normal Equation or by optimization algorithms like Gradient Descent.
    
3. **Penalty for Large Errors:** By squaring the error term $(y_i - \hat{y}_i)^2$, MSE penalizes large errors much more heavily than small ones, which is often a desirable property.


    

---

### 2. What are the alternatives to MSE? What are the criteria to choose the right loss function?

Alternatives to MSE include:

- **Mean Absolute Error (MAE)** or L1 Loss: $L = \frac{1}{n} \sum |y_i - \hat{y}_i|$. It's less sensitive to outliers than MSE.

- **Huber Loss**: A combination of MSE and MAE. It's quadratic for small errors and linear for large errors, providing a good balance of sensitivity and robustness to outliers.
    
- **Quantile Loss**: Used in Quantile Regression. It's an asymmetric loss function that allows you to estimate any quantile, not just the mean.
    

**Criteria for choosing a loss function:**

- **Presence of Outliers**: If your dataset has many significant outliers, **MAE or Huber Loss** are more robust choices than MSE because they don't square the large errors produced by the outliers.
    
- **Goal of the Model**: If you want to penalize large errors severely, **MSE** is appropriate. If all errors are equally important regardless of magnitude, **MAE** might be better. If you need to predict a specific percentile (e.g., the 90th percentile price), you must use **Quantile Loss**.
    
- **Distribution of Errors**: While MSE corresponds to a Normal distribution of errors, other loss functions correspond to different distributions (e.g., MAE corresponds to a Laplace distribution).
    

---

### 3. What does linear regression assume about the data? When do you expect these assumptions to hold true?

Linear regression assumes:

1. **Linearity**: The relationship between X and the mean of Y is linear.
    
2. **Independence**: The errors are independent of one another.
    
3. **Homoscedasticity**: The errors have constant variance.
    
4. **Normality**: The errors are normally distributed.
    

You might expect these assumptions to hold true in **well-controlled experiments** or in physical systems where relationships are known to be linear. For instance, in physics, Hooke's Law (F=−kx) is inherently linear. In finance, assumptions are often violated. In social sciences, data is often noisy and relationships are complex, but linear models can still be useful approximations. The independence assumption holds if data points are randomly sampled and don't have a time-series or clustered structure.

---

### 4. Why is homoscedasticity important? What can you do if you face heteroscedastic data?

**Homoscedasticity** (constant error variance) is important because OLS assumes it to provide the most efficient, unbiased estimates. If this assumption is violated (**heteroscedasticity**), your coefficient estimates will still be unbiased, but their standard errors will be wrong. This means all **statistical tests of significance (p-values, t-tests) and confidence intervals for the coefficients will be unreliable and misleading**.

If you face heteroscedastic data, you can:

1. **Transform the Dependent Variable**: Applying a transformation like log(y) or sqrt(y) can often stabilize the variance.
    
2. **Use Weighted Least Squares (WLS)**: This is a modified version of OLS that gives less weight to observations with higher variance, effectively correcting for the heteroscedasticity.
    
3. **Use Heteroscedasticity-Consistent Standard Errors**: Also known as "robust" standard errors (e.g., Huber-White standard errors). This method corrects the standard errors after fitting the OLS model, allowing for valid statistical inference even with heteroscedasticity.
    

---

### 5. After fitting a model, you plot the CDF of errors. What is the expected shape of the plot? What does it mean if the plot is not as expected?

The expected shape of the Cumulative Distribution Function (CDF) plot of standardized residuals would be an **S-shaped curve that closely follows the CDF of the standard normal distribution**. A more common and easier-to-interpret plot is the **Q-Q (Quantile-Quantile) plot**, where the quantiles of the residuals are plotted against the quantiles of a normal distribution. In a Q-Q plot, the expected result is a **straight 45-degree line**.

If the plot deviates significantly from the expected shape (i.e., the points on the Q-Q plot are not on the straight line), it means the **normality assumption is violated**.

- **S-shaped curve on Q-Q plot**: Indicates "light" or "heavy" tails compared to a normal distribution.
    
- **Bowed or curved pattern**: Indicates skewness in the residuals. This could suggest that a non-linear transformation of variables is needed or that there are outliers.
    

---

### 6. In real life, a lot of relations are not linear. What can you do about it? List pros and cons of your solutions.

When relations aren't linear, you have several options:

1. **Polynomial Regression**: Add polynomial terms (x2,x3) as features.
    
    - **Pros**: Simple to implement, can capture a wide variety of curved relationships, still uses the linear regression framework.
        
    - **Cons**: Prone to overfitting with high degrees, can be less interpretable, behavior at the edges (extrapolation) can be wild.
        
2. **Feature Transformation**: Apply a non-linear function to a predictor or the response (e.g., log(x), sqrtx, 1/x).
    
    - **Pros**: Can often "linearize" the relationship, can also help fix other issues like heteroscedasticity, often based on domain knowledge.
        
    - **Cons**: Requires trial-and-error or domain expertise to find the right transformation, makes interpretation less direct (e.g., "a one-unit change in log(x)...").
        
3. **Use a Non-Linear Model**: Switch to a more flexible model that doesn't assume linearity.
    
    - **Examples**: k-Nearest Neighbors, Decision Trees, Random Forests, Gradient Boosting Machines, Support Vector Regression.
        
    - **Pros**: Can capture very complex patterns without manual feature engineering, often more accurate.
        
    - **Cons**: Generally less interpretable ("black box" models), can be more computationally expensive, higher risk of overfitting if not tuned properly.
        

---

### 7. If an analytical solution exists, why would we use gradient descent to fit this model?

We would use an iterative method like Gradient Descent instead of the analytical Normal Equation for two main reasons:

1. **Computational Scalability (Number of Features)**: The Normal Equation requires calculating the inverse of the $X^T X$ matrix, a $p \times p$ matrix, where $p$ is the number of features. The computational complexity of matrix inversion is roughly $O(p^3)$. If you have a very large number of features (e.g., $p > 10,000$), this calculation becomes prohibitively slow or even impossible. Gradient Descent scales better, with a complexity closer to $O(n \cdot p)$ per iteration.
    
2. **Online Learning**: Gradient Descent (specifically Stochastic Gradient Descent) can be used for online learning, where the model is updated as new data arrives one point at a time. The Normal Equation requires having the entire dataset available at once to perform the calculation.
    

---

### 8. Can we use linear regression as a classifier?

Yes, but it's a **bad idea**. You can technically use linear regression for a classification task by labeling the two classes as 0 and 1. The model would produce a continuous output, and you could set a threshold (e.g., > 0.5) to classify new points.

However, this approach has serious flaws:

- **Unbounded Predictions**: The model can predict values much greater than 1 or less than 0, which makes no sense in a classification context.
    
- **Sensitivity to Outliers**: An outlier can easily drag the regression line and shift the decision boundary, leading to poor classification performance.
    
- **Wrong Error Assumption**: The model assumes normally distributed errors, but for a 0/1 outcome, the errors follow a binomial distribution.
    

**Logistic Regression** is the appropriate linear model for classification because its sigmoid function squashes the output to a valid probability between 0 and 1, and it uses a more appropriate loss function (Log Loss).

---

### 9. Compare L1 and L2 regularization. Are they really fundamentally different from one another?

Yes, they are fundamentally different in their effect on model coefficients, which stems from the geometry of their penalty terms.

| Feature                 | L1 Regularization (Lasso)                                          | L2 Regularization (Ridge)                                         |
| ----------------------- | ------------------------------------------------------------------ | ----------------------------------------------------------------- |
| **Penalty Term**        | Sum of absolute values of coefficients: $\lambda \sum \|\beta_j\|$ | Sum of squares of coefficients: $\lambda \sum \beta_j^2$          |
| **Effect on Coefs**     | Can shrink coefficients to be **exactly zero**.                    | Shrinks coefficients towards zero, but **never to exactly zero**. |
| **Feature Selection**   | Performs **automatic feature selection**.                          | Keeps all features in the model.                                  |
| **Geometry**            | The constraint region is a **diamond** (or hyperdiamond).          | The constraint region is a **circle** (or hypersphere).           |
| **Solution**            | No simple analytical solution; requires iterative solvers.         | Has an analytical solution.                                       |
| **Correlated Features** | Tends to arbitrarily select one feature from a correlated group.   | Shrinks the coefficients of correlated features together.         |

The fundamental difference comes from their geometric shapes. The sharp corners of the L1 "diamond" make it likely that the elliptical contours of the loss function will touch the constraint region at an axis, forcing that coefficient to zero. The smooth L2 "circle" has no corners, so the intersection almost never occurs on an axis, resulting in non-zero coefficients.

---

### 10. How do you detect multicollinearity? Can you fix it? What's so bad about it anyway?

**Multicollinearity** is a condition where two or more predictor variables in a regression model are highly correlated with each other.

**How to detect it:**

1. **Correlation Matrix**: Calculate a correlation matrix for all predictor variables. High pairwise correlation coefficients (e.g., > 0.8) are a red flag.
    
2. **Variance Inflation Factor (VIF)**: This is the standard method. VIF measures how much the variance of an estimated regression coefficient is increased because of collinearity. A common rule of thumb is that a **VIF > 5 or 10 indicates problematic multicollinearity**.
    

What's so bad about it?

Multicollinearity doesn't reduce the overall predictive power of the model, but it wreaks havoc on the interpretation of individual coefficients:

- **Unstable Coefficients**: The coefficient estimates can change dramatically in response to small changes in the model or the data.
    
- **Inflated Standard Errors**: This makes the coefficients look statistically insignificant (high p-values) even when the predictors are actually important. It becomes difficult to assess the individual importance of each predictor.
    

**How to fix it:**

1. **Remove One of the Correlated Features**: If two features are highly correlated, they are largely redundant. Dropping one is the simplest solution.
    
2. **Combine the Correlated Features**: Create a new feature that is a combination of the correlated ones (e.g., an average or an interaction term).
    
3. **Use a Regularized Model**: **Ridge Regression** is particularly effective at handling multicollinearity. It shrinks the coefficients of correlated predictors together, stabilizing the model.
    
4. **Use Principal Component Regression (PCR)**: This technique transforms the correlated features into a set of uncorrelated principal components and runs the regression on them.

Shorter answer:
- **Multicollinearity**: High correlation between predictor variables in regression, causing unstable coefficients and inflated standard errors without reducing predictive power.
- **Detection**: Use correlation matrix (high coefficients, e.g., >0.8) or Variance Inflation Factor (VIF > 5 or 10 indicates issues).
- **Issues**: Unstable coefficient estimates and high p-values obscure individual predictor importance.
- **Fixes**: Remove or combine correlated features, use Ridge Regression, or apply Principal Component Regression (PCR).

# Exercises

## Exercise 1: Toy Dataset with Heteroscedastic Inputs

The goal of this exercise is to understand:
1) how noise in the input variables can violate model assumptions 
and 
2) how feature transformations can sometimes fix the problem

Here's an explanation of the exercises and the steps you should take to complete them.
### Steps to Take:

1. **Generate the Data**: Create a synthetic dataset.
    
    - **Inputs (X)**: Create two or three input variables. For example, `X1 = np.linspace(1, 100, 200)` and `X2 = np.random.rand(200) * 50`.
        
    - **Linear Relation (y)**: Define true coefficients (e.g., `beta_1 = 2`, `beta_2 = -3`, `intercept = 5`) and create the target `y` using them: `y_true = intercept + beta_1 * X1 + beta_2 * X2`.
        
    - **Normal Noise on Target**: Add standard random noise to the target to simulate real-world measurement error: `y_noisy = y_true + np.random.normal(0, 10, 200)`. This `y_noisy` is your final target variable.
        
    - **Heteroscedastic Noise on Inputs**: This is the key part. Add noise to an input variable where the amount of noise **depends on the variable's value**. For example, make the noise in `X1` larger for larger values of `X1`: `X1_noisy = X1 + np.random.normal(0, scale=X1 * 0.1)`. This means your measurement of `X1` gets less reliable as `X1` increases.
        
2. **Model without Transforms (Baseline)**:
    
    - Fit a standard `LinearRegression` model using your noisy inputs (`X1_noisy`, `X2`) to predict your noisy target (`y_noisy`).
        
    - Examine the coefficients. They will likely be different from the true coefficients you defined because the noise in the inputs biases the result.
        
3. **Apply Feature Transforms**:
    
    - The problem is that the variance of the noise in `X1_noisy` is not constant. A **logarithmic transformation** is a common technique to stabilize variance.
        
    - Create a new transformed feature: `X1_transformed = np.log1p(X1_noisy)`. (`log1p` is used to gracefully handle values close to zero).
        
4. **Model with Transforms**:
    
    - Fit a _new_ `LinearRegression` model using your transformed input (`X1_transformed`) and other inputs (`X2`) to predict the target (`y_noisy`).
        
    - **Note**: Because you transformed an input, the new coefficient for that feature won't be directly comparable to your original true coefficient. The goal is to see if the overall model fit improves.
        
5. **Compare and Conclude**:
    
    - Split your data into training and testing sets _before_ modeling.
        
    - Compare the **R-squared** or **Mean Squared Error (MSE)** of the baseline model and the transformed model on the test set. The model using the transformed feature should show a better score, demonstrating that accounting for the heteroscedastic input noise resulted in a better fit.
        

---

## Exercise 2: Fish Market Dataset

The goal of this exercise is to practice the standard, end-to-end workflow of a regression task on a real-world dataset.

### Steps to Take:

1. **Data Loading and Exploration (EDA)**:
    
    - Find and download the "Fish Market" dataset (it's widely available on platforms like Kaggle). Load it into a pandas DataFrame.
        
    - **Explore the data**:
        
        - Use `.info()` and `.describe()` to get a summary of columns, data types, and statistics.
            
        - Check for missing values with `.isnull().sum()`.
            
        - The target variable is `Weight`. The features are `Species`, `Length1`, `Length2`, `Length3`, `Height`, and `Width`.
            
2. **Data Preprocessing**:
    
    - **Handle Categorical Features**: The `Species` column is text-based and must be converted to a numerical format. Use **one-hot encoding** (`pd.get_dummies()`) to create new binary columns for each fish species.
        
    - **Check for Multicollinearity**: The three length variables (`Length1`, `Length2`, `Length3`) are likely highly correlated. You can confirm this with a correlation matrix (`.corr()`). For a first attempt, you can leave them in, but be aware that this might make the individual coefficients unstable. A more advanced approach would be to drop two of them or combine them using Principal Component Analysis (PCA).
        
3. **Prepare for Modeling**:
    
    - Define your feature matrix `X` (all columns except `Weight`, and with `Species` one-hot encoded) and your target vector `y` (`Weight`).
        
    - **Split the data** into training and testing sets using `train_test_split` from scikit-learn. A common split is 80% for training and 20% for testing.
        
4. **Model Training**:
    
    - Choose a linear regression implementation. `sklearn.linear_model.LinearRegression` is the standard choice.
        
    - Initialize the model: `model = LinearRegression()`.
        
    - Train the model on the **training data only**: `model.fit(X_train, y_train)`.
        
5. **Model Evaluation**:
    
    - Make predictions on the **unseen test data**: `y_pred = model.predict(X_test)`.
        
    - **Calculate performance metrics** to see how well your model did:
        
        - **R-squared (R2)**: `model.score(X_test, y_test)`. This tells you the proportion of variance in fish weight that your model can explain. Closer to 1 is better.
            
        - **Root Mean Squared Error (RMSE)**: `np.sqrt(mean_squared_error(y_test, y_pred))`. This tells you the typical error of your predictions in the original unit (grams). A lower RMSE is better.
            
    - **Analyze Residuals**: Plot the residuals (`y_test - y_pred`) against the predicted values (`y_pred`). Look for random scatter around the zero line. If you see a pattern (like a cone shape), it suggests that a simple linear model may not be the best fit and the assumptions (like homoscedasticity of the _target's error_) might be violated.