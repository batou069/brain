---
tags:
  - time_series
  - forecasting
  - multivariate
  - var
  - vector_autoregression
  - concept
  - statsmodels
  - sktime
aliases:
  - VAR Model
  - Vector Autoregression
related:
  - "[[TS_Multivariate_Models]]"
  - "[[TS_Autoregressive_AR_Model|AR Model]]"
  - "[[TS_Granger_Causality]]"
  - "[[TS_Stationarity]]"
worksheet:
  - WS_TimeSeries_1
date_created: 2025-08-28
---
# Vector Autoregression (VAR) Model

## Definition
A **Vector Autoregression (VAR)** model is a multivariate forecasting algorithm that is used when two or more time series influence each other. It is a generalization of the univariate [[TS_Autoregressive_AR_Model|Autoregressive (AR) model]] to multiple, interdependent time series.

In a VAR model, each variable is modeled as a linear combination of its own past (lagged) values and the past values of all other variables in the system.

For a simple case with two variables, $y_1$ and $y_2$, and one lag ($p=1$), the VAR(1) model would be:
$$ y_{1,t} = c_1 + \phi_{11,1} y_{1,t-1} + \phi_{12,1} y_{2,t-1} + \epsilon_{1,t} $$
$$ y_{2,t} = c_2 + \phi_{21,1} y_{1,t-1} + \phi_{22,1} y_{2,t-1} + \epsilon_{2,t} $$
where:
-   $y_{1,t}$ and $y_{2,t}$ are the values of the two series at time $t$.
-   $c_1, c_2$ are constants (intercepts).
-   $\phi_{ij,k}$ is the coefficient that captures the influence of the $k$-th lag of variable $j$ on variable $i$.
-   $\epsilon_{1,t}, \epsilon_{2,t}$ are white noise error terms.

## Key Characteristics
-   **Multivariate:** Designed specifically for [[TS_Definition_and_Types|multivariate time series]] where variables are endogenous (i.e., they influence each other).
-   **System of Equations:** A VAR(p) model for $K$ variables is a system of $K$ simultaneous equations.
-   **Stationarity Requirement:** VAR models require all time series in the system to be [[TS_Stationarity|stationary]]. If they are not, they must be differenced before fitting the model.
-   **Model Identification (Order $p$):**
    -   Determining the optimal lag order $p$ is a key step.
    -   This is typically done by fitting VAR models with different lag orders and selecting the one that minimizes information criteria like **AIC (Akaike Information Criterion)**, **BIC (Bayesian Information Criterion)**, FPE, or HQIC.
-   **Forecasting:** Once fitted, the model can produce forecasts for all variables in the system simultaneously. The forecasts are generated recursively.

## Use Cases
-   **Macroeconomics:** Modeling and forecasting relationships between economic indicators like GDP, inflation, interest rates, and unemployment.
-   **Finance:** Analyzing the dynamic relationships between different stock returns, asset prices, or volatility measures.
-   **Marketing:** Modeling the interplay between sales, advertising spend across different channels, and competitor pricing.
-   **Policy Analysis (Impulse Response Functions):** A key application of VAR models is to analyze **Impulse Response Functions (IRFs)**, which trace the effect of a one-time shock to one of the variables on the current and future values of all other variables in the system.

## Python Example with `sktime`
`sktime` provides a wrapper for the `statsmodels` VAR implementation.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sktime.forecasting.var import VAR
from sktime.datasets import load_longley
from sktime.utils.plotting import plot_series

# 1. Load Multivariate Data
# The Longley dataset contains several US macroeconomic variables.
# We'll try to forecast 'GNP' and 'UNEMP' using all variables.
y, X = load_longley()
data_full = pd.concat([y, X], axis=1)

# All variables in a VAR model must be endogenous.
# Let's use a subset for simplicity: GNP, UNEMP, ARMED.FORCE
data_subset = data_full[['GNP', 'UNEMP', 'ARMED.FORCE']]

# 2. Check for Stationarity and Difference if Needed
# (For this example, we'll assume the data is stationary after one difference,
# which is a common practice for economic data. A full analysis would test each series.)
data_diff = data_subset.diff().dropna()

# 3. Split into train and test sets
train_data = data_diff.iloc[:-5] # Use last 5 years for testing
test_data = data_diff.iloc[-5:]

# 4. Define and Fit the VAR Forecaster
# sktime's VAR can automatically select the best lag order based on AIC.
forecaster = VAR(maxlags=5, ic='aic') # Search for best lag up to 5, using AIC

print("Fitting VAR model...")
forecaster.fit(train_data)
print("Fitting complete.")
print(f"\nBest lag order selected by AIC: {forecaster.get_fitted_params()['k_ar']}")
print("\nModel Summary (for GNP equation):")
print(forecaster.summary().tables) # statsmodels summary for the first variable

# 5. Make a Forecast
# Define the forecasting horizon for the test period
fh = np.arange(1, len(test_data) + 1)
y_pred = forecaster.predict(fh=fh)

# 6. Visualize the results for one variable (e.g., GNP)
plot_series(train_data['GNP'], test_data['GNP'], y_pred['GNP'], labels=["Train", "Test", "VAR Forecast"])
plt.title("VAR Forecast for GNP (Differenced)")
plt.show()

# Note: To get forecasts on the original scale, the predictions would need to be "un-differenced".
# This requires an extra step of adding the last known value of the original series back to the cumulative sum of the forecasted differences.
```
> **Note on `sklearn` and `tsfresh`:** `scikit-learn` does not have a native VAR model implementation. To tackle a multivariate forecasting problem with `sklearn`, you would need to perform extensive [[TS_Feature_Engineering_for_ML|feature engineering]], creating lagged features from *all* the variables to predict each target variable. `tsfresh` could be used to extract features from each individual series, but it doesn't inherently capture the cross-variable dynamics in the way a VAR model does.

VAR models are a powerful tool for analyzing and forecasting interdependent multivariate time series systems.

---