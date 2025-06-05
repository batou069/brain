---
tags:
  - python
  - library
  - statsmodels
  - statistics
  - econometrics
  - regression
  - time_series
  - concept
aliases:
  - StatsModels
related:
  - "[[_Python_Libraries_MOC]]"
  - "[[_NumPy_MOC]]"
  - "[[_Pandas_MOC]]"
  - "[[SciPy_Library]]"
  - "[[Linear_Regression]]"
  - "[[Generalized_Linear_Models_GLM]]"
  - "[[Time_Series_Analysis]]"
  - "[[Hypothesis_Testing]]"
worksheet:
  - WS_Python_Packages_1
date_created: 2025-06-01
---
# Statsmodels Library

## Overview
**Statsmodels** is a Python module that provides classes and functions for the estimation of many different statistical models, as well as for conducting statistical tests and statistical data exploration. It complements [[SciPy_Library|SciPy]]'s `scipy.stats` module by focusing more on statistical modeling and econometrics, often providing more extensive results summaries and diagnostics similar to those found in statistical software like R or Stata.

Statsmodels integrates well with [[_Pandas_MOC|Pandas]] for data handling and [[_NumPy_MOC|NumPy]] for numerical operations.

## Key Features and Modules
[list2tab|#Statsmodels Features]
- **Regression Models**
    - **Linear Regression (OLS - Ordinary Least Squares):** `statsmodels.api.OLS` or `statsmodels.formula.api.ols` (using R-style formulas).
        - Provides detailed summary statistics including R-squared, F-statistic, coefficients, standard errors, t-statistics, p-values, confidence intervals.
    - **[[Generalized_Linear_Models_GLM|Generalized Linear Models (GLM)]]:** `statsmodels.api.GLM` or `statsmodels.formula.api.glm`.
        - Supports various distributions (families) like Binomial (for logistic regression), Poisson, Gamma, Gaussian, etc., and link functions.
    - **Robust Linear Models (RLM):** Less sensitive to outliers. `statsmodels.api.RLM`.
    - **Linear Mixed Effects Models:** For hierarchical/multilevel data. `statsmodels.formula.api.mixedlm`.
    - Other regression models like Quantile Regression, Discrete Choice Models (Logit, Probit).
- **[[Time_Series_Analysis|Time Series Analysis]] (`statsmodels.tsa`)**
    - **Autoregressive (AR), Moving Average (MA), ARMA, ARIMA, SARIMA models:** For modeling and forecasting time series data. `statsmodels.tsa.arima.model.ARIMA`.
    - **Vector Autoregression (VAR) models:** For multivariate time series. `statsmodels.tsa.api.VAR`.
    - **State Space Models (Kalman Filtering):** `statsmodels.tsa.statespace`. Includes models like SARIMAX, Unobserved Components.
    - **Tools for time series diagnostics:** Autocorrelation (ACF), Partial Autocorrelation (PACF) plots, stationarity tests (e.g., ADF test), seasonality decomposition.
- **Analysis of Variance (ANOVA)**
    - `statsmodels.formula.api.ols` combined with `statsmodels.api.anova_lm` for ANOVA tables.
- **Nonparametric Methods**
    - Kernel Density Estimation (KDE): `statsmodels.api.nonparametric.KDEUnivariate`.
    - Kernel Regression.
- **Statistical Tests**
    - Numerous tests for means, variances, proportions, goodness of fit, normality, multicollinearity, heteroscedasticity, autocorrelation, etc. Often found within model results or `statsmodels.stats` module.
    - Examples: t-tests, F-tests, Chi-squared tests, Durbin-Watson test, Jarque-Bera test.
- **Other Areas**
    - Survival analysis (limited).
    - Multivariate statistics (e.g., MANOVA, Factor Analysis - some experimental).
    - Imputation techniques.

## Example Usage

### Ordinary Least Squares (OLS) Regression
```python
import statsmodels.api as sm
import pandas as pd
import numpy as np

# Sample data (e.g., predict salary based on years of experience)
data = {'YearsExperience': [1.1, 1.3, 1.5, 2.0, 2.2, 2.9, 3.0, 3.2, 3.2, 3.7],
        'Salary': [39343, 46205, 37731, 43525, 39891, 56642, 60150, 54445, 64445, 57189]}
df = pd.DataFrame(data)

# Define dependent (y) and independent (X) variables
y = df['Salary']
X = df['YearsExperience']

# Add a constant (intercept) to the independent variables
X = sm.add_constant(X) #  y = beta_0 * 1 + beta_1 * X

# Fit the OLS model
model = sm.OLS(y, X)
results = model.fit()

# Print the summary
# print(results.summary())
# Key outputs from summary: R-squared, Adj. R-squared, F-statistic,
# Coef (coefficients), Std.Err, t (t-statistic), P>|t| (p-value), Conf. Int.
```
> The `results.summary()` provides a comprehensive table similar to R's `summary(lm_model)`.

### Logistic Regression (using GLM)
```python
import statsmodels.api as sm
import pandas as pd
import numpy as np

# Sample data for binary outcome (e.g., pass/fail based on hours studied)
data_logit = {'HoursStudied': [0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 1.75, 2.00, 2.25, 2.50,
                               2.75, 3.00, 3.25, 3.50, 4.00, 4.25, 4.50, 4.75, 5.00, 5.50],
              'Pass': [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1]}
df_logit = pd.DataFrame(data_logit)

y_logit = df_logit['Pass']
X_logit = df_logit['HoursStudied']
X_logit = sm.add_constant(X_logit)

# Fit GLM with binomial family (for logistic regression)
logit_model = sm.GLM(y_logit, X_logit, family=sm.families.Binomial())
logit_results = logit_model.fit()

# Print summary
# print(logit_results.summary())
```

### ARIMA Time Series Model
```python
import statsmodels.api as sm
import pandas as pd
import numpy as np

# Sample time series data (e.g., monthly sales)
# np.random.seed(42)
# date_rng = pd.date_range(start='2020-01-01', end='2023-12-31', freq='M')
# sales_data = np.random.randn(len(date_rng)).cumsum() + 50
# sales_ts = pd.Series(sales_data, index=date_rng)

# Fit an ARIMA(p,d,q) model, e.g., ARIMA(5,1,0)
# This requires selecting appropriate orders (p,d,q) based on ACF/PACF plots, AIC/BIC, etc.
# For demonstration, we'll use arbitrary orders.
# try:
#     arima_model = sm.tsa.arima.ARIMA(sales_ts, order=(5,1,0))
#     arima_results = arima_model.fit()
#     # Print summary
#     print(arima_results.summary())
#     # Make predictions
#     # forecast = arima_results.predict(start=len(sales_ts)-10, end=len(sales_ts)+5) # In-sample and out-of-sample
#     # sales_ts.plot(label='Observed')
#     # forecast.plot(label='Forecast')
#     # import matplotlib.pyplot as plt
#     # plt.legend(); plt.show()
# except Exception as e:
#     print(f"ARIMA example requires time series data; placeholder error: {e}")
#     # Placeholder if data generation fails or for minimal example
#     pass
```
> **Note:** Proper time series modeling involves more steps like checking for stationarity, model identification (ACF/PACF), and diagnostics.

## Common Applications
- **Econometrics:** Modeling economic relationships, forecasting economic variables.
- **Social Sciences:** Analyzing survey data, modeling social phenomena.
- **Business Analytics:** Sales forecasting, customer behavior analysis, financial modeling.
- **Biostatistics:** Analyzing clinical trial data, epidemiological studies.
- **Any field requiring rigorous statistical modeling beyond basic descriptive statistics.**

Statsmodels is a powerful library for users who need detailed statistical output, hypothesis testing, and a wide range of traditional statistical and econometric models in Python. It's often used when the goal is inference and understanding relationships, rather than just predictive accuracy (though it can be used for prediction too).

---