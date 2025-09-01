---
tags:
  - time_series
  - forecasting
  - sarima
  - arima
  - seasonality
  - statsmodels
  - sktime
  - concept
  - arma
  - ar
  - ma
aliases:
  - SARIMA
  - Seasonal ARIMA
  - SARIMA(p
  - d
  - q)(P
  - D
  - Q)m
  - ARMA
  - Autoregressive Moving Average Model
  - ARMA(p
  - q)
related:
  - "[[TS_ARIMA_Family_Models]]"
  - "[[TS_ARIMA_Model]]"
  - "[[TS_Components_Decomposition|Seasonality]]"
  - "[[TS_Autocorrelation_ACF_PACF]]"
  - "[[TS_Lag_and_Differencing]]"
  - "[[TS_Autoregressive_AR_Model|AR(p)]]"
  - "[[TS_Moving_Average_MA_Model|MA(q)]]"
  - "[[TS_Stationarity]]"
worksheet:
  - WS_TimeSeries_1
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# SARIMA (Seasonal Autoregressive Integrated Moving Average) Model

## Definition
The **Seasonal Autoregressive Integrated Moving Average (SARIMA)** model is an extension of the [[TS_ARIMA_Model|ARIMA]] model that explicitly supports time series data with a **seasonal component**. It is one of the most widely used statistical methods for forecasting seasonal time series.

A SARIMA model is denoted as **SARIMA(p,d,q)(P,D,Q)m**, where:
-   `(p,d,q)` are the non-seasonal parameters, the same as in a standard ARIMA model.
-   `(P,D,Q)m` are the seasonal parameters.

## Components of SARIMA(p,d,q)(P,D,Q)m
The model is a combination of non-seasonal and seasonal components:

-   **Non-Seasonal Part (p,d,q):**
    -   **p:** The order of the non-seasonal Autoregressive (AR) part.
    -   **d:** The order of non-seasonal differencing.
    -   **q:** The order of the non-seasonal Moving Average (MA) part.
    -   These components model the relationships between consecutive observations (e.g., between $y_t$ and $y_{t-1}$).

-   **Seasonal Part (P,D,Q)m:**
    -   **P:** The order of the **Seasonal** Autoregressive (SAR) part. It models the relationship between an observation and observations from previous seasons (e.g., between $y_t$ and $y_{t-m}$).
    -   **D:** The order of **Seasonal** differencing. It computes the difference between an observation and its value from the previous season ($y_t - y_{t-m}$). This is used to remove the seasonal trend.
    -   **Q:** The order of the **Seasonal** Moving Average (SMA) part. It models the relationship between an observation and the forecast errors from previous seasons.
    -   **m:** The **seasonal period** or frequency (e.g., `m=12` for monthly data with yearly seasonality, `m=4` for quarterly data, `m=7` for daily data with weekly seasonality).

>[!question]- When would you choose SARIMA over ARIMA for modeling a time series?
>You would choose a **SARIMA** model over a standard **ARIMA** model when the time series exhibits a clear and consistent **seasonal pattern**.
>
>1.  **Presence of Seasonality:** The primary indicator is the presence of a repeating pattern at a fixed frequency (e.g., sales peaking every December, electricity usage peaking every day in the afternoon).
>2.  **Visual Evidence:** A plot of the time series shows a regular, periodic fluctuation. A seasonal subseries plot (plotting each season's data on top of each other) can make this even clearer.
>3.  **ACF/PACF Plots:** The Autocorrelation Function (ACF) plot of the (differenced) series shows significant spikes at lags corresponding to the seasonal period (e.g., at lags 12, 24, 36 for monthly data). This is a strong statistical indicator of seasonality.
>
>While a standard ARIMA model might be able to capture some seasonality if its non-seasonal AR order ($p$) is large enough to reach back to the previous season, this approach is inefficient, less interpretable, and often less accurate. SARIMA is explicitly designed to handle seasonality by including seasonal AR, differencing, and MA terms, which directly model the relationship between an observation and observations from previous seasons. This generally leads to a more parsimonious (simpler) and accurate model for seasonal data.

## Modeling Procedure
The process is an extension of the Box-Jenkins methodology for ARIMA:
1.  **Identification:**
    -   Plot the data to visually identify trend and seasonality. The seasonal period `m` is usually determined from domain knowledge or visual inspection.
    -   Apply seasonal differencing (`D=1`) if seasonality is strong. Apply non-seasonal differencing (`d=1`) if a trend remains.
    -   Plot the ACF and PACF of the differenced series.
    -   **Identify seasonal orders (P, Q):** Look at the spikes at seasonal lags (`m`, `2m`, `3m`, ...).
        -   The PACF cutting off at lag `m*P` suggests a SAR(P) model.
        -   The ACF cutting off at lag `m*Q` suggests a SMA(Q) model.
    -   **Identify non-seasonal orders (p, q):** Look at the first few lags (1, 2, 3, ...) as you would for a standard ARIMA model.
2.  **Estimation:** Fit the chosen SARIMA(p,d,q)(P,D,Q)m model to the data.
3.  **Diagnostic Checking:** Analyze the model's residuals. They should resemble white noise, with no significant spikes left in their ACF/PACF plots.
4.  **Forecasting:** Use the fitted model to make future predictions.

## Python Example with `sktime`
`sktime` provides a wrapper for `statsmodels`' SARIMAX implementation, as well as `AutoARIMA` which can automatically find the best SARIMA orders.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sktime.datasets import load_airline
from sktime.forecasting.arima import AutoARIMA
from sktime.forecasting.base import ForecastingHorizon
from sktime.utils.plotting import plot_series

# 1. Load Data
# The airline dataset has a clear trend and multiplicative seasonality.
y = load_airline()

# 2. Split into training and test sets
y_train = y[y.index < "1960-01-01"]
y_test = y[y.index >= "1960-01-01"]

# 3. Define and Fit the AutoARIMA Forecaster
# AutoARIMA from the pmdarima library is a powerful tool that automatically
# searches for the best (p,d,q)(P,D,Q)m parameters.
# We just need to specify the seasonal period 'sp'.
forecaster = AutoARIMA(
    sp=12,                 # Seasonal period (12 for monthly data)
    suppress_warnings=True,
    stepwise=True,         # Use a stepwise algorithm to find the best model faster
    n_jobs=-1,             # Use all available cores
    max_p=5, max_q=5,      # Set limits for the search
    max_P=2, max_Q=2
)

print("Fitting AutoARIMA (SARIMA) model...")
forecaster.fit(y_train)
print("Model fitting complete.")

# 4. Inspect the best model found
print(f"\nBest SARIMA model found by AutoARIMA: {forecaster.get_fitted_params()}")

# 5. Make a Forecast
fh = ForecastingHorizon(y_test.index, is_relative=False)
y_pred = forecaster.predict(fh)

# 6. Get Prediction Intervals
y_pred_intervals = forecaster.predict_interval(fh, coverage=0.90)

# 7. Visualize the results
plot_series(y_train, y_test, y_pred, labels=["y_train", "y_test", "y_pred"])
plt.fill_between(
    y_pred_intervals.index,
    y_pred_intervals.iloc[:, 0],
    y_pred_intervals.iloc[:, 1],
    alpha=0.2,
    color='green',
    label="90% Prediction Interval"
)
plt.title("Airline Passengers Forecast with AutoARIMA (SARIMA)")
plt.legend(loc='upper left')
plt.show()

# 8. Evaluate the forecast
from sktime.performance_metrics.forecasting import mean_absolute_percentage_error
mape = mean_absolute_percentage_error(y_test, y_pred, symmetric=False)
print(f"\nMAPE on test set: {mape:.4f}")
```
> **Note on `sklearn` and `tsfresh`:** Standard `sklearn` models do not handle seasonality directly. To use them, you would first need to **deseasonalize** the data (e.g., using `sktime.transformations.series.detrend.Deseasonalizer` or `statsmodels.tsa.seasonal.seasonal_decompose`) or create explicit seasonal features (e.g., month-of-year dummy variables). `tsfresh` can extract features like `autocorrelation` at specific seasonal lags, which could then be used by an `sklearn` model to learn the seasonal pattern. However, SARIMA provides a more direct and statistically grounded approach for modeling seasonality.

SARIMA is a powerful and widely-used model for forecasting univariate time series that exhibit both trend and seasonal patterns.

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