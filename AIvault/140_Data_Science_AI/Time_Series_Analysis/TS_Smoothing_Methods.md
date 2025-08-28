---
tags:
  - time_series
  - forecasting
  - smoothing
  - moving_average
  - exponential_smoothing
  - holt
  - holt_winters
  - concept
aliases:
  - Time Series Smoothing
  - Smoothing Techniques
related:
  - "[[140_Data_Science_AI/Time_Series_Analysis/_Time_Series_Analysis_MOC|_Time_Series_Analysis_MOC]]"
  - "[[TS_Moving_Average]]"
  - "[[TS_Exponential_Smoothing]]"
  - "[[TS_Components_Decomposition|Time Series Components]]"
worksheet:
  - WS_TimeSeries_1
date_created: 2025-08-27
---
# Time Series Smoothing Methods

**Smoothing** techniques are a class of time series forecasting methods that aim to separate the underlying pattern (signal) from the random fluctuations (noise). These methods produce a "smoothed" version of the time series, which can be used to identify trends and seasonality, or be projected into the future for forecasting.

## Core Idea
The fundamental idea behind smoothing is that observations that are close in time are likely to have similar underlying values. Therefore, a good estimate for the current underlying value can be obtained by averaging past observations.

## Main Types of Smoothing Methods

1.  **[[TS_Moving_Average|Moving Average (MA) Smoothing]]:**
    -   **Concept:** The simplest form of smoothing. The smoothed value at time $t$ is the simple, unweighted average of the last $k$ observations.
    -   **Use:** Primarily for smoothing and trend visualization. As a forecasting method, it's very basic (produces a flat forecast).

2.  **[[TS_Exponential_Smoothing|Exponential Smoothing]]:**
    -   **Concept:** A more sophisticated method where the forecast is a weighted average of past observations, with the weights decaying exponentially as the observations get older. More recent observations are given more weight.
    -   **Advantages:** Overcomes the limitations of simple moving average by giving more importance to recent data and not having a fixed "window" that drops old data abruptly.
    -   **Family of Models:**
        -   **Simple Exponential Smoothing (SES):** For data with no trend or seasonality.
        -   **Holt's Linear Trend Method:** Extends SES to handle data with a trend.
        -   **Holt-Winters' Seasonal Method:** Extends Holt's method to capture seasonality (both additive and multiplicative).

>[!question]- How does exponential smoothing differ from moving average models in handling time series data?
>This question can refer to two comparisons: Exponential Smoothing vs. Moving Average *Smoothing*, and Exponential Smoothing vs. the [[TS_Moving_Average_MA_Model|Moving Average (MA) Model]] from ARIMA.
>
>**1. Exponential Smoothing vs. Moving Average *Smoothing***
>
>[list2mdtable|#ES vs. MA Smoothing]
>- Feature
>    - Moving Average Smoothing
>        - Exponential Smoothing
>- **Weights**
>    - Assigns **equal weight** to all observations within the defined window.
>        - Assigns **exponentially decreasing weights** to past observations. The most recent observation gets the most weight.
>- **"Memory"**
>    - Has a fixed memory of size `k` (the window size). Observations older than `k` are completely forgotten.
>        - Theoretically has an infinite memory, as all past observations contribute to the forecast (though the influence of very old observations becomes negligible).
>- **Lag**
>    - The lag is more pronounced, typically around `k/2`.
>        - Generally more responsive to recent changes, resulting in less lag.
>- **Forecasting**
>    - A simple MA produces a flat forecast (the last calculated average).
>        - The family of ES models can produce more sophisticated forecasts, including those with trends (Holt's) and seasonality (Holt-Winters).
>
>**2. Exponential Smoothing vs. Moving Average *(MA) Model***
>
>-   **Exponential Smoothing** models are based on a weighted average of **past observations**.
>-   The **[[TS_Moving_Average_MA_Model|MA Model]]** (part of ARIMA) is fundamentally different; it's based on a weighted average of **past forecast errors (random shocks)**.
>
>In summary, exponential smoothing is a more sophisticated forecasting method than simple moving average smoothing because of its adaptive, exponentially weighted nature. It is distinct from the MA model of ARIMA, which models the error structure of the series.

## Python Example with `sktime`
`sktime` provides wrappers for classical models, including Exponential Smoothing from `statsmodels`.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sktime.datasets import load_airline
from sktime.forecasting.exp_smoothing import ExponentialSmoothing
from sktime.utils.plotting import plot_series

# Load data
y = load_airline()

# Split into train and test sets
y_train = y[y.index < "1960-01-01"]
y_test = y[y.index >= "1960-01-01"]

# --- Define and Fit the Model ---
# We use Holt-Winters' method because the airline data has both trend and seasonality.
# 'mul' specifies multiplicative models for trend and seasonality.
# 'sp' is the seasonal period (12 for monthly data).
forecaster = ExponentialSmoothing(
    trend="mul",
    seasonal="mul",
    sp=12
)

# Fit the model to the training data
forecaster.fit(y_train)

# --- Make a Forecast ---
# Define the forecasting horizon to match the test set
fh = ForecastingHorizon(y_test.index, is_relative=False)
y_pred = forecaster.predict(fh)

# --- Visualize the Forecast ---
plot_series(y_train, y_test, y_pred, labels=["y_train", "y_test", "y_pred"])
plt.title("Holt-Winters' Exponential Smoothing Forecast with sktime")
plt.show()

# --- For comparison: A simple Rolling Mean ---
# This is for smoothing, not forecasting in the same way.
rolling_mean = y_train.rolling(window=12).mean()
plot_series(y_train, rolling_mean, labels=["Original Train Data", "12-Month Rolling Mean"])
plt.title("Simple Moving Average Smoothing")
plt.show()
```
> **Note on `tsfresh`:** `tsfresh` is not a modeling or smoothing library. It would be used in a different context: to extract features from the time series (or its residuals after smoothing) to be used in a machine learning model. For example, after applying smoothing, you could analyze the residuals with `tsfresh` to see if any complex patterns remain.

---