---
tags:
  - time_series
  - autocorrelation
  - acf
  - pacf
  - correlation
  - model_identification
  - concept
  - statsmodels
aliases:
  - Autocorrelation
  - Partial Autocorrelation
  - ACF
  - PACF
related:
  - "[[_Time_Series_Analysis_MOC|_Time_Series_Analysis_MOC]]"
  - "[[TS_Stationarity]]"
  - "[[TS_Lag_and_Differencing|Lag]]"
  - "[[TS_Autoregressive_AR_Model|AR Model]]"
  - "[[TS_Moving_Average_MA_Model|MA Model]]"
  - "[[TS_ARIMA_Family_Models|ARIMA Models]]"
worksheet:
  - WS_TimeSeries_1
date_created: 2025-08-27
---
# Autocorrelation (ACF) and Partial Autocorrelation (PACF)

**Autocorrelation** is the correlation of a time series with a delayed copy of itself (a [[TS_Lag_and_Differencing|lagged]] version). It's a fundamental concept for understanding the internal structure of a time series and for identifying appropriate models like [[TS_ARIMA_Family_Models|ARIMA]].

The **Autocorrelation Function (ACF)** and **Partial Autocorrelation Function (PACF)** are key tools used to measure and visualize this self-correlation.

## Autocorrelation Function (ACF)
-   **Definition:** The ACF at lag $k$ measures the correlation between the time series $y_t$ and its value at a previous time point, $y_{t-k}$.
-   **What it Measures:** It measures the **direct and indirect** relationship between an observation and its lag. The correlation at lag 2, for example, is influenced by the direct effect of lag 2 on the current observation, but also indirectly through the effect of lag 1 (since lag 2 influences lag 1, which in turn influences the current observation).
-   **ACF Plot:** A plot of the autocorrelation for different lag values.
    -   The y-axis is the correlation coefficient (from -1 to 1).
    -   The x-axis is the lag number.
    -   The plot typically includes a shaded area representing the confidence interval (e.g., 95%). Lags with correlation values outside this area are considered statistically significant.
-   **Interpretation:**
    -   **Non-stationary series:** The ACF plot shows a very slow, linear decay.
    -   **Seasonal series:** The ACF plot shows significant spikes at seasonal lags (e.g., at lags 12, 24, 36 for monthly data).
    -   **[[TS_Moving_Average_MA_Model|Moving Average (MA) models]]:** The ACF plot is used to identify the order ($q$) of an MA model. The ACF will be significant for the first $q$ lags and then abruptly cut off to zero (or within the confidence interval).

## Partial Autocorrelation Function (PACF)
-   **Definition:** The PACF at lag $k$ measures the correlation between the time series $y_t$ and its value at lag $k$, but **after removing the effects of the intervening lags** ($y_{t-1}, y_{t-2}, \dots, y_{t-k+1}$).
-   **What it Measures:** It measures only the **direct** relationship between an observation and its value at lag $k$, removing the indirect correlations.
-   **PACF Plot:** A plot of the partial autocorrelation for different lag values, similar in layout to the ACF plot.
-   **Interpretation:**
    -   **[[TS_Autoregressive_AR_Model|Autoregressive (AR) models]]:** The PACF plot is used to identify the order ($p$) of an AR model. The PACF will be significant for the first $p$ lags and then abruptly cut off to zero (or within the confidence interval).

>[!question]- What is the role of autocorrelation and partial autocorrelation in identifying time series model parameters?
>ACF and PACF plots are the primary tools for identifying the orders ($p, q$) of ARMA and ARIMA models for a [[TS_Stationarity|stationary]] time series.
>
>1.  **Identify the AR order ($p$):**
>    -   Look at the **PACF plot**.
>    -   The lag at which the PACF plot "cuts off" (i.e., drops to non-significance) suggests the order of the AR component. If the PACF has a significant spike at lag 1 and lag 2, but is non-significant for all lags greater than 2, this suggests an AR(2) model.
>
>2.  **Identify the MA order ($q$):**
>    -   Look at the **ACF plot**.
>    -   The lag at which the ACF plot "cuts off" suggests the order of the MA component. If the ACF has a significant spike at lag 1, but is non-significant for all lags greater than 1, this suggests an MA(1) model.
>
>3.  **Identify ARMA/ARIMA models:**
>    -   If both the ACF and PACF plots show a tapering or tailing-off pattern (decaying gradually rather than cutting off abruptly), it suggests that both AR and MA components are present (an ARMA model).
>
>**Summary Table for Model Identification:**
>
>[list2mdtable|#ACF/PACF Patterns for Model Identification]
>- Model
>    - ACF Pattern
>        - PACF Pattern
>- **AR(p)**
>    - Tails off (exponential decay or damped sine wave)
>        - **Cuts off after lag p**
>- **MA(q)**
>    - **Cuts off after lag q**
>        - Tails off (exponential decay or damped sine wave)
>- **ARMA(p,q)**
>    - Tails off after lag q
>        - Tails off after lag p
>
>This identification process is performed on the **stationary** version of the time series. If the original series is non-stationary, you must first apply [[TS_Lag_and_Differencing|differencing]] and then analyze the ACF/PACF of the differenced series to determine the AR and MA orders ($p, q$). The number of times you differenced the series gives you the integrated order ($d$) for an ARIMA(p,d,q) model.

## Python Example
The `statsmodels` library is excellent for plotting ACF and PACF.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima_process import ArmaProcess

# --- Example 1: AR(2) Process ---
# An AR(2) process: Y_t = 0.75 * Y_{t-1} - 0.25 * Y_{t-2} + noise
ar_params = np.array([0.75, -0.25])
ma_params = np.array([]) # No MA component
ar_process = ArmaProcess(ar=np.r_[1, -ar_params], ma=np.r_[1, ma_params])
ar_data = ar_process.generate_sample(nsample=500)

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
plot_acf(ar_data, ax=axes, lags=20, title='ACF of AR(2) Process')
plot_pacf(ar_data, ax=axes, lags=20, title='PACF of AR(2) Process', method='ywm')
plt.suptitle('AR(2) Process: ACF Tails Off, PACF Cuts Off at 2', y=1.02)
plt.tight_layout()
plt.show()
# The PACF plot should show significant spikes at lags 1 and 2, then cut off.

# --- Example 2: MA(2) Process ---
# An MA(2) process: Y_t = 0.6 * noise_{t-1} + 0.3 * noise_{t-2} + noise_t
ar_params_ma = np.array([])
ma_params_ma = np.array([0.6, 0.3])
ma_process = ArmaProcess(ar=np.r_[1, -ar_params_ma], ma=np.r_[1, ma_params_ma])
ma_data = ma_process.generate_sample(nsample=500)

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
plot_acf(ma_data, ax=axes, lags=20, title='ACF of MA(2) Process')
plot_pacf(ma_data, ax=axes, lags=20, title='PACF of MA(2) Process', method='ywm')
plt.suptitle('MA(2) Process: ACF Cuts Off at 2, PACF Tails Off', y=1.02)
plt.tight_layout()
plt.show()
# The ACF plot should show significant spikes at lags 1 and 2, then cut off.

# --- Example 3: Non-Stationary Process (Random Walk) ---
# A random walk is non-stationary
np.random.seed(1)
random_walk = np.random.randn(500).cumsum()

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
plot_acf(random_walk, ax=axes, lags=40, title='ACF of Non-Stationary Process')
plot_pacf(random_walk, ax=axes, lags=40, title='PACF of Non-Stationary Process', method='ywm')
plt.suptitle('Non-Stationary Process: ACF Decays Very Slowly', y=1.02)
plt.tight_layout()
plt.show()
# The ACF plot will show a very slow, linear decay, a classic sign of non-stationarity.
```

ACF and PACF plots are indispensable visual tools for the initial analysis and model identification phase of time series forecasting.

---