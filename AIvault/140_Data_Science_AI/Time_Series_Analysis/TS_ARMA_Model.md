---
tags:
  - time_series
  - forecasting
  - arma
  - ar
  - ma
  - arima
  - concept
  - statsmodels
aliases:
  - ARMA
  - Autoregressive Moving Average Model
  - ARMA(p
  - q)
related:
  - "[[TS_ARIMA_Family_Models]]"
  - "[[TS_Autoregressive_AR_Model|AR(p)]]"
  - "[[TS_Moving_Average_MA_Model|MA(q)]]"
  - "[[TS_ARIMA_Model]]"
  - "[[TS_Stationarity]]"
  - "[[TS_Autocorrelation_ACF_PACF]]"
worksheet:
  - WS_TimeSeries_1
date_created: 2025-08-28
---
# ARMA (Autoregressive Moving Average) Model

## Definition
An **Autoregressive Moving Average (ARMA)** model is a statistical model for time series data that combines two components: an **[[TS_Autoregressive_AR_Model|Autoregressive (AR)]]** part and a **[[TS_Moving_Average_MA_Model|Moving Average (MA)]]** part. It is used to describe and forecast [[TS_Stationarity|stationary]] time series.

An ARMA model of order **(p, q)**, denoted **ARMA(p,q)**, is defined by the equation:
$$ Y_t = c + \underbrace{\phi_1 Y_{t-1} + \dots + \phi_p Y_{t-p}}_{\text{AR(p) part}} + \underbrace{\epsilon_t + \theta_1 \epsilon_{t-1} + \dots + \theta_q \epsilon_{t-q}}_{\text{MA(q) part}} $$
where:
-   $Y_t$ is the value of the time series at time $t$.
-   $c$ is a constant.
-   $p$ is the order of the autoregressive part.
-   $\phi_i$ are the AR parameters.
-   $q$ is the order of the moving average part.
-   $\theta_i$ are the MA parameters.
-   $\epsilon_t$ is the white noise error term at time $t$.

## Key Characteristics
-   **Stationarity Requirement:** The ARMA model is defined for **stationary** time series. If a series has a trend or seasonality, it must be made stationary (e.g., through [[TS_Lag_and_Differencing|differencing]]) before an ARMA model can be applied. When differencing is included, the model becomes an [[TS_ARIMA_Model|ARIMA]] model. An ARMA(p,q) model is equivalent to an ARIMA(p,0,q) model.
-   **Model Identification (Orders $p, q$):**
    -   Identifying the orders for a mixed ARMA model is more complex than for pure AR or MA models.
    -   **Signature Pattern:** For a stationary ARMA(p,q) process, both the **[[TS_Autocorrelation_ACF_PACF|ACF]]** and **[[TS_Autocorrelation_ACF_PACF|PACF]]** plots will **tail off** (decay gradually) after some initial lags.
        -   The ACF will tail off after lag $q$.
        -   The PACF will tail off after lag $p$.
    -   In practice, identifying $p$ and $q$ from these plots can be difficult. It often involves trying a few candidate models (e.g., ARMA(1,1), ARMA(2,1), ARMA(1,2)) and comparing them using information criteria like AIC or BIC. Automated tools like `AutoARIMA` are often used to search for the best orders.

## Python Example
Fitting a pure ARMA model is less common than fitting an ARIMA model, as most real-world series require differencing. The `statsmodels` and `sktime` `ARIMA` classes can be used to fit an ARMA model by setting the differencing order `d` to 0.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_process import ArmaProcess
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from sktime.forecasting.arima import ARIMA

# 1. Generate a sample ARMA(2,2) stationary series
np.random.seed(42)
ar_params = np.array([0.75, -0.25])
ma_params = np.array([0.65, 0.35])
arma_process = ArmaProcess(ar=np.r_[1, -ar_params], ma=np.r_[1, ma_params])
arma_data = pd.Series(arma_process.generate_sample(nsample=500))
arma_data.index = pd.period_range(start='2000-01-01', periods=500, freq='M')

# 2. Identify the model using ACF/PACF
# fig, axes = plt.subplots(1, 2, figsize=(14, 4))
# plot_acf(arma_data, ax=axes, lags=20, title="ACF of ARMA(2,2) Process")
# plot_pacf(arma_data, ax=axes, lags=20, title="PACF of ARMA(2,2) Process", method='ywm')
# plt.suptitle("ARMA Process: Both ACF and PACF Tail Off", y=1.02)
# plt.show()
# The plots will show a gradual decay, suggesting a mixed model.

# 3. Fit an ARMA(2,2) model using sktime's ARIMA wrapper
# We set d=0 to specify an ARMA model.
y_train = arma_data[:-36]
y_test = arma_data[-36:]

# Define the forecaster
# Note: sktime's ARIMA is a wrapper around statsmodels.tsa.arima.model.ARIMA
forecaster = ARIMA(
    order=(2, 0, 2), # (p, d, q) -> d=0 makes it an ARMA model
    suppress_warnings=True
)

print("Fitting ARMA(2,0,2) model...")
forecaster.fit(y_train)
print("Fitting complete.")
print(forecaster.summary())

# 4. Make a forecast
# from sktime.forecasting.base import ForecastingHorizon
# from sktime.utils.plotting import plot_series

# fh = ForecastingHorizon(y_test.index, is_relative=False)
# y_pred = forecaster.predict(fh)

# plot_series(y_train.tail(100), y_test, y_pred, labels=["Train (tail)", "Test", "ARMA Forecast"])
# plt.title("ARMA(2,2) Forecast")
# plt.show()
```

The ARMA model is a powerful tool for modeling stationary time series that exhibit both autoregressive and moving average behaviors. It forms the core of the more general and widely used [[TS_ARIMA_Model|ARIMA]] model.

---