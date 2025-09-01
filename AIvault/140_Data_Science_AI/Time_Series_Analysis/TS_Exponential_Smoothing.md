---
tags:
  - time_series
  - forecasting
  - exponential_smoothing
  - holt
  - holt_winters
  - ets
  - smoothing
  - concept
  - sktime
  - statsmodels
aliases:
  - Exponential Smoothing
  - ETS Models
  - Simple Exponential Smoothing
  - Holt's Linear Trend
  - Holt-Winters' Seasonal Method
related:
  - "[[TS_Smoothing_Methods]]"
  - "[[TS_Moving_Average]]"
  - "[[TS_Components_Decomposition|Time Series Components]]"
worksheet:
  - WS_TimeSeries_1
date_created: 2025-08-28
---
# Exponential Smoothing (ETS) Models

**Exponential Smoothing** is a family of classical forecasting methods that produce forecasts based on weighted averages of past observations, with the weights decaying exponentially as the observations get older. This means that more recent observations are given more weight in the forecast.

These methods are widely used for their simplicity, speed, and good performance on a wide range of time series data. They are often referred to as **ETS (Error, Trend, Seasonality)** models, which describes the components each model variation can handle.

## The Core Idea: Exponentially Weighted Averages
Unlike a simple [[TS_Moving_Average|moving average]] which gives equal weight to the last `k` observations, exponential smoothing assigns geometrically decreasing weights. The forecast is a combination of the previous observation and the previous forecast.

## The Family of Exponential Smoothing Models

[list2tab|#ETS Models]
- 1. Simple Exponential Smoothing (SES)
    -   **Model:** ETS(A,N,N) - Additive Error, No Trend, No Seasonality.
    -   **Purpose:** For forecasting time series with **no clear trend or seasonality**. It models only the level of the series.
    -   **Equation:**
        $$ \hat{y}_{t+1} = \alpha y_t + (1-\alpha) \hat{y}_t $$
    -   **Parameters:**
        -   $\alpha$ (alpha, `smoothing_level`): The smoothing parameter for the level, $0 \le \alpha \le 1$. A higher $\alpha$ gives more weight to recent observations and results in a more responsive, less smooth forecast. A lower $\alpha$ results in a smoother forecast.
    -   **Forecast:** The forecast for all future horizons is a flat line equal to the last smoothed level.
- 2. Holt's Linear Trend Method
    -   **Model:** ETS(A,A,N) - Additive Error, Additive Trend, No Seasonality.
    -   **Purpose:** Extends SES to handle data with a **trend**. It includes a second smoothing equation for the trend component.
    -   **Equations:**
        -   Level: $L_t = \alpha y_t + (1-\alpha)(L_{t-1} + T_{t-1})$
        -   Trend: $T_t = \beta(L_t - L_{t-1}) + (1-\beta)T_{t-1}$
        -   Forecast: $\hat{y}_{t+h} = L_t + h \cdot T_t$
    -   **Parameters:**
        -   $\alpha$ (`smoothing_level`): Smoothing parameter for the level.
        -   $\beta$ (beta, `smoothing_trend`): Smoothing parameter for the trend.
    -   **Damped Trend:** An extension adds a damping parameter $\phi$ (phi) to flatten the trend over long forecast horizons, which is often more realistic.
- 3. Holt-Winters' Seasonal Method
    -   **Model:** ETS(A,A,A) or ETS(A,A,M) - e.g., Additive Error, Additive Trend, Additive/Multiplicative Seasonality.
    -   **Purpose:** Extends Holt's method to capture **seasonality** in addition to a trend. It includes a third smoothing equation for the seasonal component.
    -   **Components:**
        -   Level ($L_t$)
        -   Trend ($T_t$)
        -   Seasonality ($S_t$)
    -   **Variations:**
        -   **Additive Seasonality:** The seasonal component is added to the trend and level. Used when seasonal fluctuations are roughly constant in size.
        -   **Multiplicative Seasonality:** The seasonal component is multiplied. Used when seasonal fluctuations grow or shrink proportionally to the level of the series.
    -   **Parameters:**
        -   $\alpha$ (`smoothing_level`)
        -   $\beta$ (`smoothing_trend`)
        -   $\gamma$ (gamma, `smoothing_seasonal`)
        -   `m` or `sp`: The seasonal period.

## Python Example with `sktime`
`sktime` provides a convenient wrapper for the `statsmodels` implementation of Exponential Smoothing.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sktime.datasets import load_airline
from sktime.forecasting.exp_smoothing import ExponentialSmoothing
from sktime.forecasting.base import ForecastingHorizon
from sktime.utils.plotting import plot_series

# 1. Load Data
# The airline dataset has a clear multiplicative trend and seasonality.
y = load_airline()

# 2. Split into training and test sets
y_train = y[y.index < "1960-01-01"]
y_test = y[y.index >= "1960-01-01"]

# 3. Define and Fit the Holt-Winters' Model
# We use 'mul' for multiplicative trend and seasonality, which is appropriate for this data.
# 'sp' is the seasonal period (12 for monthly data).
forecaster = ExponentialSmoothing(
    trend="mul",
    seasonal="mul",
    sp=12
)

# Fit the model to the training data
print("Fitting Holt-Winters' Exponential Smoothing model...")
forecaster.fit(y_train)
print("Model fitting complete.")
print(f"\nFitted Parameters:\n{forecaster.get_fitted_params()}")

# 4. Make a Forecast
fh = ForecastingHorizon(y_test.index, is_relative=False)
y_pred = forecaster.predict(fh)

# 5. Get Prediction Intervals
y_pred_intervals = forecaster.predict_interval(fh, coverage=0.95)

# 6. Visualize the results
plot_series(y_train, y_test, y_pred, labels=["y_train", "y_test", "y_pred"])
plt.fill_between(
    y_pred_intervals.index,
    y_pred_intervals.iloc[:, 0],
    y_pred_intervals.iloc[:, 1],
    alpha=0.2,
    color='green',
    label="95% Prediction Interval"
)
plt.title("Holt-Winters' Exponential Smoothing Forecast")
plt.legend(loc='upper left')
plt.show()

# 7. Evaluate the forecast
from sktime.performance_metrics.forecasting import mean_absolute_percentage_error
mape = mean_absolute_percentage_error(y_test, y_pred, symmetric=False)
print(f"\nMAPE on test set: {mape:.4f}")
```
> **Note on `sklearn` and `tsfresh`:** `scikit-learn` does not have built-in implementations of exponential smoothing models. You would use a library like `statsmodels` or `sktime` for this. `tsfresh` is a feature extraction library and would not be used to implement the model itself, but features it extracts could potentially be used by an ML model to try to learn similar patterns.

Exponential smoothing models are powerful, interpretable, and computationally efficient, making them a strong baseline and a widely used method for time series forecasting.

---