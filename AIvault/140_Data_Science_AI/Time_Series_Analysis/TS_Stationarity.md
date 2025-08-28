---
tags:
  - time_series
  - stationarity
  - adf_test
  - kpss_test
  - differencing
  - concept
  - statsmodels
aliases:
  - Stationary Time Series
  - Non-Stationary Time Series
  - Stationarity Tests
related:
  - "[[_Time_Series_Analysis_MOC|_Time_Series_Analysis_MOC]]"
  - "[[TS_Components_Decomposition|Time Series Components]]"
  - "[[TS_Lag_and_Differencing]]"
  - "[[TS_Autoregressive_AR_Model|AR Models]]"
  - "[[TS_ARIMA_Family_Models|ARIMA Models]]"
worksheet:
  - WS_TimeSeries_1
date_created: 2025-08-27
---
# Stationarity in Time Series

**Stationarity** is a crucial statistical property of a time series. A time series is said to be stationary if its statistical properties—such as mean, variance, and autocorrelation—are all constant over time.

>[!question]- What is the difference between a stationary and non-stationary time series?
>
>[list2tab|#Stationary vs Non-Stationary]
>- Stationary Time Series
>    -   **Mean:** The mean of the series is constant over time. It does not have a [[TS_Components_Decomposition|trend]].
>    -   **Variance:** The variance of the series is constant over time (a property called homoscedasticity). The fluctuations around the mean are of a consistent width.
>    -   **Autocorrelation:** The autocorrelation structure (how an observation is related to its lagged values) is constant over time. It does not have [[TS_Components_Decomposition|seasonality]].
>    -   **Appearance:** The series appears to fluctuate around a constant mean, with a consistent width of variation. It tends to revert to its mean.
>    -   **Example:** A [[TS_White_Noise_and_Random_Walks|white noise]] series.
>- Non-Stationary Time Series
>    -   **Mean:** The mean of the series changes over time. This is characteristic of a series with a **trend** (upward or downward).
>    -   **Variance:** The variance of the series changes over time (heteroscedasticity). For example, fluctuations might get wider as the level of the series increases.
>    -   **Autocorrelation:** The autocorrelation structure changes over time. This is characteristic of a series with **seasonality**.
>    -   **Appearance:** The series exhibits clear trends, seasonal patterns, or changing variance. It does not revert to a constant mean.
>    -   **Example:** Stock prices (often have a trend), airline passenger numbers (have trend and seasonality).

## Why is Stationarity Important?
Many classical time series forecasting models, such as [[TS_ARIMA_Family_Models|AR, MA, and ARMA models]], are designed based on the assumption that the time series is stationary.
-   **Predictability:** If a series is stationary, its statistical properties are consistent in the future, making it easier to model and forecast. Past behavior is a reliable indicator of future behavior.
-   **Model Stability:** Models fitted to stationary data are more stable and reliable. If you fit a model to non-stationary data, the learned parameters might only be relevant for the historical period on which the model was trained and may not generalize well to the future.
-   **Avoiding Spurious Regressions:** Regressing two non-stationary time series against each other can often result in a statistically significant relationship even when none truly exists (a "spurious regression").

The [[TS_ARIMA_Model|ARIMA model]] is specifically designed to handle non-stationary data by first applying [[TS_Lag_and_Differencing|differencing]] to make the series stationary.

## How to Test for Stationarity

>[!question]- How can you test for stationarity in a time series dataset?
>You can test for stationarity using a combination of visual inspection and statistical hypothesis tests.
>
>1.  **Visual Inspection:**
>    -   **Time Series Plot:** Plot the data over time. Look for obvious trends or seasonal patterns. Check if the mean and variance appear constant.
>    -   **[[TS_Autocorrelation_ACF_PACF|Autocorrelation Function (ACF) Plot]]:** For a stationary series, the ACF will drop to zero relatively quickly. For a non-stationary series, the ACF will decay very slowly. For a seasonal series, the ACF will show significant peaks at seasonal lags.
>2.  **Summary Statistics:**
>    -   Split the time series into several parts and compare the summary statistics (mean, variance) of each part. If they are significantly different, the series is likely non-stationary.
>3.  **Statistical Tests (Hypothesis Tests):**
>    -   These provide a more formal way to test for stationarity, specifically for the presence of a "unit root," which is a statistical property of some non-stationary time series.
>    -   **Augmented Dickey-Fuller (ADF) Test:**
>        -   This is a unit root test.
>        -   **Null Hypothesis ($H_0$):** The time series has a unit root (it is non-stationary).
>        -   **Alternative Hypothesis ($H_1$):** The time series does not have a unit root (it is stationary).
>        -   **Interpretation:** If the p-value from the test is less than a significance level (e.g., 0.05), we **reject the null hypothesis** and conclude that the series is stationary.
>    -   **Kwiatkowski-Phillips-Schmidt-Shin (KPSS) Test:**
>        -   This test has the opposite null hypothesis, which can be more intuitive.
>        -   **Null Hypothesis ($H_0$):** The time series is stationary (around a constant mean or a linear trend).
>        -   **Alternative Hypothesis ($H_1$):** The time series has a unit root (it is non-stationary).
>        -   **Interpretation:** If the p-value is less than a significance level (e.g., 0.05), we **reject the null hypothesis** and conclude that the series is non-stationary.
>
>It's often recommended to use both ADF and KPSS tests. If they agree, you have a strong conclusion. If they disagree, the series is likely complex, and further investigation is needed.

### Python Example for Stationarity Testing
```python
import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import adfuller, kpss
from statsmodels.graphics.tsaplots import plot_acf
import matplotlib.pyplot as plt

# Create two sample time series
np.random.seed(42)
# 1. Stationary series (white noise)
stationary_series = pd.Series(np.random.randn(200))
# 2. Non-stationary series (random walk with a trend)
non_stationary_series = pd.Series(np.random.randn(200).cumsum() + np.arange(200) * 0.2)

def perform_stationarity_tests(series, series_name):
    print(f"--- Stationarity Tests for: {series_name} ---")
    # ADF Test
    adf_result = adfuller(series)
    print(f'ADF Statistic: {adf_result:.4f}')
    print(f'p-value: {adf_result:.4f}')
    print('Critical Values:')
    for key, value in adf_result.items():
        print(f'\t{key}: {value:.4f}')
    if adf_result <= 0.05:
        print("=> ADF Test: Reject H0. The series is likely stationary.")
    else:
        print("=> ADF Test: Fail to reject H0. The series is likely non-stationary.")
    
    # KPSS Test
    kpss_result = kpss(series, regression='c') # 'c' for constant mean, 'ct' for constant and trend
    print(f'\nKPSS Statistic: {kpss_result:.4f}')
    print(f'p-value: {kpss_result:.4f}')
    print('Critical Values:')
    for key, value in kpss_result.items():
        print(f'\t{key}: {value:.4f}')
    if kpss_result < 0.05:
        print("=> KPSS Test: Reject H0. The series is likely non-stationary.")
    else:
        print("=> KPSS Test: Fail to reject H0. The series is likely stationary.")
    print("-" * 40 + "\n")

# Run tests on both series
perform_stationarity_tests(stationary_series, "Stationary Series (White Noise)")
perform_stationarity_tests(non_stationary_series, "Non-Stationary Series (Random Walk with Trend)")

# Visualize the series and their ACFs
fig, axes = plt.subplots(2, 2, figsize=(14, 8))
stationary_series.plot(ax=axes, title="Stationary Series")
plot_acf(stationary_series, ax=axes, lags=40)
non_stationary_series.plot(ax=axes, title="Non-Stationary Series")
plot_acf(non_stationary_series, ax=axes, lags=40)
plt.tight_layout(); plt.show()
```
The output of this code will show that the stationary series has a low ADF p-value and a high KPSS p-value, while the non-stationary series has the opposite, confirming their nature. The ACF plot for the non-stationary series will show a very slow decay.

```python
# Using statsmodels for the statistical test is standard practice even in an sktime/sklearn workflow.
import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import adfuller
from sktime.transformations.series.difference import Differencer
from sktime.utils.plotting import plot_series
import matplotlib.pyplot as plt

# Create a non-stationary series (random walk with a trend)
np.random.seed(42)
non_stationary_series = pd.Series(np.random.randn(200).cumsum() + np.arange(200) * 0.2)
non_stationary_series.index = pd.period_range(start='2023-01-01', periods=200, freq='D')

# --- Test for stationarity ---
adf_result = adfuller(non_stationary_series)
print(f'ADF Test on Original Series - p-value: {adf_result:.4f}')
if adf_result > 0.05:
    print("Result: The original series is likely non-stationary.")
else:
    print("Result: The original series is likely stationary.")

# --- Make the series stationary using sktime's Differencer ---
# This is a transformation step in a machine learning pipeline
differencer = Differencer(lags=1)
stationary_series = differencer.fit_transform(non_stationary_series)

# --- Test the differenced series for stationarity ---
adf_result_diff = adfuller(stationary_series.dropna())
print(f'\nADF Test on Differenced Series - p-value: {adf_result_diff:.4f}')
if adf_result_diff <= 0.05:
    print("Result: The differenced series is likely stationary.")
else:
    print("Result: The differenced series is likely non-stationary.")

# --- Visualize the transformation ---
fig, axes = plot_series(non_stationary_series, stationary_series, labels=["Original Non-Stationary", "Differenced Stationary"])
plt.suptitle("Making a Series Stationary with Differencing")
plt.show()
```

## How to Make a Series Stationary
If a series is non-stationary, it often needs to be transformed before modeling. The most common method is **[[TS_Lag_and_Differencing|differencing]]**.

---