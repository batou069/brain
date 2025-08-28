---
tags:
  - python
  - sktime
  - time_series
  - forecasting
  - model
  - api
  - concept
  - example
aliases:
  - sktime Forecasting
  - sktime Forecaster API
related:
  - "[[160_Python_Libraries/sktime/_sktime_MOC|_sktime_MOC]]"
  - "[[sktime_Forecasting_Reduction]]"
  - "[[sktime_Model_Selection_Tuning]]"
  - "[[TS_ARIMA_Model]]"
  - "[[TS_Exponential_Smoothing]]"
worksheet:
  - WS_TimeSeries_1
date_created: 2025-08-27
---
# sktime: Forecasting

Forecasting is one of the core tasks in `sktime`. The library provides a unified API for a wide range of forecasting models, from classical statistical methods to machine learning approaches.

## The `Forecaster` API
All forecasting models in `sktime` follow a consistent API based on the `BaseForecaster` class, which is analogous to scikit-learn's `Estimator` API.

**Key Methods:**
-   **`fit(y, X=None, fh=None)`:** Trains the forecasting model.
    -   `y`: The training time series (a `pandas` Series or DataFrame).
    -   `X` (optional): Exogenous variables (features) for the training period.
    -   `fh` (optional): The forecasting horizon. Can be provided at `fit` or `predict` time.
-   **`predict(fh=None, X=None)`:** Generates point forecasts for the specified forecasting horizon.
    -   `fh`: A `ForecastingHorizon` object specifying the future time points to predict.
    -   `X` (optional): Future values of exogenous variables, required if the model was trained with them.
-   **`predict_interval(fh=None, X=None, coverage=0.90)`:** Generates prediction intervals (confidence intervals) for the forecasts.
-   **`update(y, X=None, update_params=True)`:** Updates the model with new data without re-fitting from scratch (for models that support it).

## Forecasting Horizon (`fh`)
The Forecasting Horizon is a key object in `sktime` that specifies the time points you want to forecast. It can be created in several ways:
-   **Integer array-like:** `fh =` (predict next 3 steps).
-   **NumPy array:** `fh = np.arange(1, 13)` (predict next 12 steps).
-   **`sktime.forecasting.base.ForecastingHorizon` object:** More powerful, can handle different index types and relative/absolute horizons.

## Example: Forecasting Airline Passengers
This example demonstrates fitting a classical model (a wrapper around `statsmodels` SARIMA) and making predictions.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sktime.datasets import load_airline
from sktime.forecasting.arima import AutoARIMA
from sktime.forecasting.base import ForecastingHorizon
from sktime.utils.plotting import plot_series

# 1. Load Data
y = load_airline()

# 2. Split into training and test sets
y_train = y[y.index < "1960-01-01"]
y_test = y[y.index >= "1960-01-01"]

# 3. Define the Forecaster
# AutoARIMA automatically finds the best (p,d,q)(P,D,Q)m parameters.
# sp=12 indicates a seasonal period of 12 months.
forecaster = AutoARIMA(sp=12, suppress_warnings=True)

# 4. Fit the model to the training data
print("Fitting AutoARIMA model...")
forecaster.fit(y_train)
print("Model fitting complete.")
print(f"Best ARIMA order found: {forecaster.get_fitted_params()}")

# 5. Define the Forecasting Horizon (fh) for the test period
fh = ForecastingHorizon(y_test.index, is_relative=False)

# 6. Make Predictions
y_pred = forecaster.predict(fh)

# 7. Get Prediction Intervals
y_pred_intervals = forecaster.predict_interval(fh, coverage=0.90)

# 8. Visualize the results
# plot_series(y_train, y_test, y_pred, labels=["y_train", "y_test", "y_pred"])
# plt.fill_between(y_pred_intervals.index,
#                  y_pred_intervals.iloc[:, 0],
#                  y_pred_intervals.iloc[:, 1],
#                  alpha=0.2, color='green', label="90% Prediction Interval")
# plt.title("Airline Passengers Forecast with AutoARIMA")
# plt.legend()
# plt.show()

# 9. Evaluate the forecast
# from sktime.performance_metrics.forecasting import MeanAbsolutePercentageError
# mape = MeanAbsolutePercentageError()
# print(f"\nMAPE on test set: {mape(y_test, y_pred):.4f}")
```

## Forecasting with Exogenous Variables (X)
Many models can incorporate external variables (also known as covariates or exogenous features) to improve forecasts.

```python
from sktime.forecasting.compose import TransformedTargetForecaster
from sktime.transformations.series.detrend import Deseasonalizer
from sktime.forecasting.arima import ARIMA

# (Using y_train, y_test from above)
# Create a conceptual exogenous variable, e.g., a dummy 'holiday' feature
# In a real scenario, this would be known future data (e.g., marketing campaigns, holidays)
X = pd.DataFrame(index=y.index)
X['holiday_promo'] = 0
X.loc['1955-07-01':'1955-07-31', 'holiday_promo'] = 1
X.loc['1956-07-01':'1956-07-31', 'holiday_promo'] = 1
X.loc['1957-12-01':'1957-12-31', 'holiday_promo'] = 1

X_train = X[X.index < "1960-01-01"]
X_test = X[X.index >= "1960-01-01"]

# Use a SARIMAX model (via ARIMA wrapper) which can handle exogenous variables
# We'll also deseasonalize the target first using a pipeline
forecaster_exog = TransformedTargetForecaster(steps=[
    ("deseasonalize", Deseasonalizer(model="multiplicative", sp=12)),
    ("forecast", ARIMA(
        order=(1, 1, 0), # Non-seasonal order
        seasonal_order=(1, 1, 0, 12), # Seasonal order
        suppress_warnings=True
    ))
])

# Fit with both y_train and X_train
# forecaster_exog.fit(y=y_train, X=X_train)

# Predict using the future exogenous variables X_test
# y_pred_exog = forecaster_exog.predict(fh=fh, X=X_test)

# plot_series(y_test, y_pred_exog, labels=["y_test", "y_pred_with_exog"])
# plt.title("Forecast with Exogenous Variable (Holiday Promo)")
# plt.show()
```

`sktime`'s unified API simplifies the process of experimenting with and comparing a wide variety of forecasting models, from classical statistical methods to complex machine learning pipelines.

---