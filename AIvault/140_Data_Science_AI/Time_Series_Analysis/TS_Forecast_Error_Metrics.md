---
tags:
  - time_series
  - forecasting
  - evaluation
  - metrics
  - error
  - mae
  - mse
  - rmse
  - mape
  - concept
  - sklearn
aliases:
  - Forecast Error
  - Forecasting Metrics
  - MAE
  - MSE
  - RMSE
  - MAPE
related:
  - "[[140_Data_Science_AI/Time_Series_Analysis/_Time_Series_Analysis_MOC|_Time_Series_Analysis_MOC]]"
  - "[[TS_Cross_Validation_Evaluation]]"
  - "[[Model_Evaluation_Metrics]]"
worksheet:
  - WS_TimeSeries_1
date_created: <% tp.file-creation_date("YYYY-MM-DD") %>
---
# Time Series Forecast Error Metrics

Evaluating the accuracy of a forecast is a critical step in the modeling process. Forecast error metrics quantify the difference between the predicted values and the actual observed values.

Let $y_t$ be the actual value at time $t$, and $\hat{y}_t$ be the forecasted value at time $t$. The forecast error is $e_t = y_t - \hat{y}_t$. Metrics are typically calculated over a set of $n$ forecast points (e.g., a test set).

## Common Forecast Error Metrics

[list2tab|#Error Metrics]
- Scale-Dependent Errors
    -   **Description:** These metrics are in the same units as the original data. They are easy to interpret but cannot be used to compare forecasts across different time series with different scales.
    -   **Mean Absolute Error (MAE):**
        -   **Formula:** $MAE = \frac{1}{n} \sum_{t=1}^{n} |y_t - \hat{y}_t|$
        -   **Interpretation:** The average absolute difference between the forecast and the actual value. It's easy to understand and robust to outliers.
    -   **Mean Squared Error (MSE):**
        -   **Formula:** $MSE = \frac{1}{n} \sum_{t=1}^{n} (y_t - \hat{y}_t)^2$
        -   **Interpretation:** The average of the squared errors. It penalizes larger errors more heavily than smaller ones due to the squaring.
    -   **Root Mean Squared Error (RMSE):**
        -   **Formula:** $RMSE = \sqrt{MSE} = \sqrt{\frac{1}{n} \sum_{t=1}^{n} (y_t - \hat{y}_t)^2}$
        -   **Interpretation:** The square root of the MSE. It's also in the same units as the original data, making it more interpretable than MSE. Like MSE, it penalizes large errors more than MAE.
- Percentage Errors
    -   **Description:** These metrics are unit-free and are useful for comparing forecast performance across time series with different scales.
    -   **Mean Absolute Percentage Error (MAPE):**
        -   **Formula:** $MAPE = \frac{1}{n} \sum_{t=1}^{n} \left| \frac{y_t - \hat{y}_t}{y_t} \right| \times 100\%$
        -   **Interpretation:** The average absolute percentage difference between the forecast and the actual value.
        -   >[!question]- Why is Mean Absolute Percentage Error (MAPE) a useful metric for evaluating time series forecasts?
            >MAPE is particularly useful for several reasons:
            >1.  **Scale Independence:** Because it's a percentage, it is unit-free. This allows you to compare the forecast accuracy of different time series that have different scales (e.g., comparing the forecast for a product that sells 1,000,000 units with a product that sells 100 units). An MAE of 10 is huge for the second product but tiny for the first; a MAPE of 5% is comparable for both.
            >2.  **Easy Interpretation and Communication:** Percentage errors are intuitive and easy to explain to non-technical stakeholders. Saying "the forecast is off by an average of 5%" is more universally understood than "the RMSE is 253.7 units."
            >3.  **Relative Error:** It measures the error relative to the actual value, which can be more meaningful than the absolute error.
            >
            >**Limitations of MAPE:**
            >-   It is **undefined** if any actual value $y_t$ is zero.
            >-   It can produce extremely large or infinite values if an actual value is very close to zero.
            >-   It can be biased: it puts a heavier penalty on negative errors (when $\hat{y}_t > y_t$) than on positive errors. For example, the error can't exceed 100% for over-forecasts, but there's no upper limit for under-forecasts.
    -   **Symmetric Mean Absolute Percentage Error (sMAPE):**
        -   An alternative to MAPE that attempts to correct for the bias by using the average of the actual and forecast values in the denominator. Its range is typically $[0\%, 200\%]$.
- Scaled Errors
    -   **Description:** These metrics scale the errors based on the in-sample variability of the time series, making them comparable across series.
    -   **Mean Absolute Scaled Error (MASE):**
        -   **Concept:** The MAE of the forecast is scaled by the in-sample MAE of a naive, one-step forecast (e.g., a random walk forecast where $\hat{y}_t = y_{t-1}$).
        -   **Interpretation:**
            -   MASE < 1: The forecast is better than the naive forecast.
            -   MASE > 1: The forecast is worse than the naive forecast.
        -   **Advantage:** A good, general-purpose metric that is less prone to the issues of MAPE and is scale-independent.

## Python Example
`scikit-learn` and `sktime` provide implementations for these metrics.

```python
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, mean_absolute_percentage_error
from sktime.performance_metrics.forecasting import MeanAbsoluteScaledError

# --- Example Data ---
# Actual observed values (e.g., from a test set)
y_true = pd.Series()
# Forecasted values from a model
y_pred = pd.Series()
# Training data is needed for MASE calculation
y_train = pd.Series() # Example training data

# --- Calculate Metrics ---

# 1. Scale-Dependent Errors
mae = mean_absolute_error(y_true, y_pred)
mse = mean_squared_error(y_true, y_pred)
rmse = np.sqrt(mse)

print("--- Scale-Dependent Errors ---")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")

# 2. Percentage Error
mape = mean_absolute_percentage_error(y_true, y_pred)

print("\n--- Percentage Errors ---")
print(f"Mean Absolute Percentage Error (MAPE): {mape*100:.2f}%")

# 3. Scaled Error (using sktime)
mase_calculator = MeanAbsoluteScaledError()
# The calculator needs the training data to compute the naive forecast error
mase = mase_calculator(y_true, y_pred, y_train=y_train)

print("\n--- Scaled Errors ---")
print(f"Mean Absolute Scaled Error (MASE): {mase:.4f}")
# Since MASE is likely < 1, our forecast is better than a naive random walk forecast.
```

## Choosing a Metric
-   **RMSE** is often preferred when large errors are particularly undesirable.
-   **MAE** is a good choice for a straightforward, interpretable measure of average error.
-   **MAPE** is excellent for communication and comparing across series of different scales, but be cautious if your data contains zeros or values close to zero.
-   **MASE** is a robust, general-purpose metric that is scale-free and avoids many of the pitfalls of MAPE.

It's often best practice to evaluate a forecast using multiple metrics to get a comprehensive understanding of its performance.

---