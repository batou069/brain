---
tags:
  - time_series
  - decomposition
  - stl
  - moving_average
  - classical_decomposition
  - concept
  - statsmodels
  - sktime
aliases:
  - Time Series Decomposition Methods
  - STL Decomposition
related:
  - "[[TS_Components_Decomposition]]"
  - "[[TS_Moving_Average]]"
  - "[[TS_Stationarity]]"
worksheet:
  - WS_TimeSeries_1
date_created: 2025-08-28
---
# Time Series Decomposition Methods

**Time Series Decomposition** is the process of separating a time series into its underlying components, typically [[TS_Components_Decomposition|Trend, Seasonality, and Residual]]. Several methods exist to perform this decomposition, ranging from simple classical approaches to more robust modern techniques.

## 1. Classical Decomposition
-   **Concept:** A relatively simple procedure that was one of the earliest methods developed. It's often used for initial analysis due to its simplicity.
-   **Method (for Additive Model):**
    1.  **Estimate Trend ($T_t$):** Calculate a [[TS_Moving_Average|moving average]] of the series. The window size of the moving average should be equal to the seasonal period `m`. A centered moving average is used to align the trend with the original data.
    2.  **Estimate Seasonality ($S_t$):** Detrend the series by subtracting the trend component ($Y_t - T_t$). Then, for each season (e.g., each month), average the detrended values. These averages form the seasonal component.
    3.  **Estimate Residual ($R_t$):** Subtract the estimated trend and seasonal components from the original data ($R_t = Y_t - T_t - S_t$).
-   **Pros:** Easy to understand and implement.
-   **Cons:**
    -   The trend estimate is unavailable for the first and last few observations.
    -   It assumes the seasonal component repeats exactly from year to year, which may not be true.
    -   Can be sensitive to outliers.
-   **Implementation:** `statsmodels.tsa.seasonal.seasonal_decompose`

## 2. X-12-ARIMA and X-13-ARIMA-SEATS
-   **Concept:** Sophisticated methods developed by the U.S. Census Bureau for seasonal adjustment of economic time series.
-   **Method:** They are based on an iterative process of fitting [[TS_ARIMA_Model|ARIMA models]] and using moving average filters to estimate trend and seasonal components. They can handle complex seasonality, trading day effects, and holiday effects.
-   **Pros:** Very robust and widely used in government and industry for official seasonal adjustments.
-   **Cons:** Can be more complex to use and configure.

## 3. STL (Seasonal and Trend decomposition using LOESS)
-   **Concept:** A versatile and robust method for decomposing time series, developed by R. B. Cleveland et al. LOESS (Locally Estimated Scatterplot Smoothing) is a non-parametric regression method.
-   **Method:** STL uses an iterative procedure of smoothing and subtracting to separate the components.
    -   It allows the seasonal component to change over time (though usually slowly).
    -   The smoothness of the trend component can be controlled by the user.
    -   It is robust to outliers.
-   **Pros:**
    -   **Versatility:** Can handle any type of seasonality (not just monthly or quarterly).
    -   **Robustness:** Less sensitive to outliers than classical decomposition.
    -   **Control:** Allows user control over the degree of smoothing for the trend and seasonal components.
    -   **Seasonal Component Flexibility:** The seasonal component is allowed to change over time.
-   **Cons:** Only provides support for additive decomposition directly. For multiplicative data, you must first take the log transform, perform additive decomposition, and then back-transform the components.
-   **Implementation:** `statsmodels.tsa.seasonal.STL`

## Python Example: Comparing Classical and STL Decomposition
This example uses `statsmodels` directly, as it is the primary library for these specific decomposition algorithms. `sktime`'s `Deseasonalizer` and `Detrender` transformers are inspired by these methods but are designed for a pipelining workflow.

```python
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose, STL
from sktime.datasets import load_airline

# Load data
y = load_airline()

# --- 1. Classical Decomposition (Multiplicative) ---
# This method is simpler but has limitations (e.g., endpoints).
classical_result = seasonal_decompose(y, model='multiplicative', period=12)

# --- 2. STL Decomposition (More Robust) ---
# STL is additive, so we first log-transform the multiplicative airline data.
y_log = np.log(y)
stl_result = STL(y_log, period=12).fit()

# --- Plotting the results ---
# fig, axes = plt.subplots(4, 2, figsize=(14, 10))

# Plot Classical Decomposition
axes.set_title("Classical Decomposition", loc='center')
classical_result.observed.plot(ax=axes, legend=False)
axes.set_ylabel("Observed")
classical_result.trend.plot(ax=axes, legend=False)
axes.set_ylabel("Trend")
classical_result.seasonal.plot(ax=axes, legend=False)
axes.set_ylabel("Seasonal")
classical_result.resid.plot(ax=axes, legend=False)
axes.set_ylabel("Residual")
axes.set_xlabel("Date")

# Plot STL Decomposition (on log scale)
axes.set_title("STL Decomposition (on Log Data)", loc='center')
stl_result.observed.plot(ax=axes, legend=False)
axes.set_ylabel("Observed (log)")
stl_result.trend.plot(ax=axes, legend=False)
axes.set_ylabel("Trend (log)")
stl_result.seasonal.plot(ax=axes, legend=False)
axes.set_ylabel("Seasonal (log)")
stl_result.resid.plot(ax=axes, legend=False)
axes.set_ylabel("Residual (log)")
axes.set_xlabel("Date")

plt.tight_layout()
plt.show()
```
> **Note on `sklearn` and `tsfresh`:** `scikit-learn` does not provide time series decomposition methods. `tsfresh` is a feature extraction library; it does not perform decomposition. The standard workflow is to use a library like `statsmodels` or `sktime` for decomposition, and then potentially use `tsfresh` or `sklearn` on the resulting components (e.g., training a model on the seasonally-adjusted series, or extracting features from the residuals).

Decomposition is a powerful exploratory tool and a crucial preprocessing step for many forecasting methods. **STL is generally preferred over classical decomposition** due to its robustness and flexibility.

---