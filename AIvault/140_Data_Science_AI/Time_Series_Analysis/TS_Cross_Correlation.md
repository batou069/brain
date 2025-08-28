---
tags:
  - time_series
  - cross_correlation
  - correlation
  - multivariate
  - lag
  - concept
  - statsmodels
aliases:
  - Cross-Correlation Function
  - CCF
related:
  - "[[140_Data_Science_AI/Time_Series_Analysis/_Time_Series_Analysis_MOC|_Time_Series_Analysis_MOC]]"
  - "[[TS_Autocorrelation_ACF_PACF]]"
  - "[[TS_Granger_Causality]]"
  - "[[TS_Vector_Autoregression_VAR|VAR Models]]"
worksheet:
  - WS_TimeSeries_1
date_created: 2025-08-27
---
# Cross-Correlation

## Definition
**Cross-correlation** is a measure of the similarity or relationship between two time series as a function of the displacement of one relative to the other. It is essentially the [[Correlation_vs_Covariance|correlation]] between two time series at different time lags.

The **Cross-Correlation Function (CCF)** shows the correlation between series $X_t$ and series $Y_{t+k}$ for various values of the lag $k$.

-   If the peak correlation occurs at $k=0$, the two series are most correlated at the same time point (contemporaneous relationship).
-   If the peak correlation occurs at a positive lag $k > 0$, it suggests that series $X$ **leads** series $Y$. A change in $X$ at time $t$ is associated with a change in $Y$ at a later time $t+k$.
-   If the peak correlation occurs at a negative lag $k < 0$, it suggests that series $Y$ **leads** series $X$.

## Purpose and Use Cases

>[!question]- How can cross-correlation be used to identify relationships between two time series?
>Cross-correlation is a powerful tool for identifying and quantifying lead-lag relationships between two time series.
>
>1.  **Identifying Lags:** By plotting the Cross-Correlation Function (CCF), you can visually identify the lag at which the correlation between the two series is maximized. This lag indicates the time displacement that best aligns the patterns in the two series.
>2.  **Determining Leading/Lagging Variables:**
>    -   If the CCF peaks at a positive lag `k`, it implies that the first series is a **leading indicator** for the second series by `k` time steps. For example, if the CCF of (Advertising Spend, Sales) peaks at lag `k=1` (month), it suggests that this month's advertising spend is most correlated with next month's sales.
>    -   If the CCF peaks at a negative lag `k`, it implies the second series is a leading indicator for the first.
>3.  **Quantifying Relationship Strength:** The magnitude of the correlation coefficient at the peak lag indicates the strength of the linear relationship at that specific time offset.
>4.  **Input for Multivariate Models:** The identified lead-lag relationships are crucial for building multivariate forecasting models like [[TS_Vector_Autoregression_VAR|Vector Autoregression (VAR)]] or Dynamic Regression models. It helps in selecting which lagged variables of one series should be included as predictors for another series.
>5.  **Checking for Synchronicity:** A strong correlation at or very near lag 0 suggests the two series move together in time.

## Important Considerations
-   **Stationarity:** For the CCF to be meaningful and interpretable, both time series should be made **[[TS_Stationarity|stationary]]** first. If you calculate the CCF on two non-stationary series that both have trends, you will likely find a high correlation at all lags, which is spurious and misleading.
-   **Correlation is Not Causation:** A strong cross-correlation, even with a clear lead-lag relationship, does **not** prove that one series causes the other. There could be a third, confounding variable influencing both, or the relationship could be coincidental. See [[TS_Granger_Causality]] for a more formal (though still not definitive) test of predictive causality.
-   **Autocorrelation:** The own [[TS_Autocorrelation_ACF_PACF|autocorrelation]] within each series can sometimes complicate the interpretation of the CCF. Pre-whitening is an advanced technique used to remove autocorrelation before calculating the CCF to get a clearer picture of the relationship.

## Python Example
The `statsmodels` library provides a function to calculate and plot the CCF.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# --- Create two conceptual time series ---
# Let's model a scenario where advertising spend (series_x) leads sales (series_y) by 2 months.
np.random.seed(42)
time_index = pd.to_datetime(pd.date_range(start='2020-01-01', periods=100, freq='MS'))

# Advertising Spend (with some noise)
series_x = pd.Series(100 + np.sin(np.linspace(0, 8 * np.pi, 100)) * 20 + np.random.randn(100) * 5, index=time_index)
series_x.name = "Ad_Spend"

# Sales: related to Ad Spend from 2 months ago, plus its own trend and noise
# We use .shift(2) to create the lag
series_y = pd.Series(200 + np.arange(100) * 0.5 + series_x.shift(2) * 1.5 + np.random.randn(100) * 10, index=time_index)
series_y.name = "Sales"

# Drop initial NaNs created by the shift
series_x = series_x.iloc[2:]
series_y = series_y.iloc[2:]

# --- Make series stationary (important for meaningful CCF) ---
# Simple differencing to remove trends
x_diff = series_x.diff().dropna()
y_diff = series_y.diff().dropna()

# --- Calculate and Plot Cross-Correlation ---
# We use statsmodels.tsa.stattools.ccf
# Note: statsmodels ccf calculates Corr(x(t), y(t+k)), so a positive lag k means x leads y.
ccf_values = sm.tsa.stattools.ccf(x_diff, y_diff, adjusted=False)

# Plotting the CCF
fig, ax = plt.subplots(figsize=(10, 5))
ax.stem(ccf_values, use_line_collection=True) # use_line_collection for newer matplotlib
ax.axhline(0, color='black', lw=0.5)
# Add confidence interval lines (approximate for large samples)
conf_interval = 2 / np.sqrt(len(x_diff))
ax.axhline(conf_interval, color='red', linestyle='--', lw=1)
ax.axhline(-conf_interval, color='red', linestyle='--', lw=1)
ax.set_title('Cross-Correlation Function (CCF) between Ad Spend and Sales (Differenced)')
ax.set_xlabel('Lag (k)')
ax.set_ylabel('Cross-Correlation')
ax.set_xlim()
plt.grid(True)
plt.show()
```
> **Expected Result:** The CCF plot should show a significant positive peak at **lag k=2**. This correctly identifies that the `Ad_Spend` series is a leading indicator for the `Sales` series by 2 time steps (months in this case).

---