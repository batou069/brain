---
tags:
  - time_series
  - forecasting
  - arima
  - arma
  - ar
  - ma
  - model
  - statsmodels
  - concept
  - differencing
  - stationarity
aliases:
  - ARIMA Models
  - ARMA
  - AR
  - MA
  - ARIMA
  - Autoregressive Integrated Moving Average
related:
  - "[[_Time_Series_Analysis_MOC|_Time_Series_Analysis_MOC]]"
  - "[[TS_Autoregressive_AR_Model]]"
  - "[[TS_Moving_Average_MA_Model]]"
  - "[[TS_ARMA_Model]]"
  - "[[TS_ARIMA_Model]]"
  - "[[TS_SARIMA_Model]]"
  - "[[TS_Stationarity]]"
  - "[[TS_Autocorrelation_ACF_PACF]]"
  - "[[TS_ARIMA_Family_Models]]"
  - "[[TS_Autoregressive_AR_Model|AR(p)]]"
  - "[[TS_Moving_Average_MA_Model|MA(q)]]"
  - "[[TS_Lag_and_Differencing|Differencing (I(d))]]"
worksheet:
  - WS_TimeSeries_1
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# ARIMA Family of Models

The ARIMA family of models are a class of statistical models for analyzing and forecasting time series data. They are one of the most widely used approaches for classical time series forecasting. The models in this family work by explicitly describing the autocorrelations in the data.

These models require the time series to be **[[TS_Stationarity|stationary]]** or to be made stationary through [[TS_Lag_and_Differencing|differencing]].

## Core Components
The models are built from three main components:
1.  **Autoregressive (AR):** A model that uses the dependent relationship between an observation and some number of lagged observations.
2.  **Integrated (I):** The use of differencing of raw observations (e.g., subtracting an observation from an observation at the previous time step) in order to make the time series stationary.
3.  **Moving Average (MA):** A model that uses the dependency between an observation and a residual error from a moving average model applied to lagged observations.

## The Models

[list2tab|#ARIMA Family]
- [[TS_Autoregressive_AR_Model|AR(p) - Autoregressive Model]]
    -   **Concept:** A regression of the variable against its own past (lagged) values. The current value $Y_t$ is a linear combination of its previous $p$ values plus a white noise error term.
    -   **Equation:** $Y_t = c + \phi_1 Y_{t-1} + \phi_2 Y_{t-2} + \dots + \phi_p Y_{t-p} + \epsilon_t$
    -   **Parameter ($p$):** The order of the AR model, representing the number of lag observations included.
    -   **Identification:** The [[TS_Autocorrelation_ACF_PACF|PACF plot]] cuts off after lag $p$.
- [[TS_Moving_Average_MA_Model|MA(q) - Moving Average Model]]
    -   **Concept:** The current value $Y_t$ is a linear combination of the current and past white noise error terms. It models the "shocks" or random errors of the process.
    -   **Equation:** $Y_t = \mu + \epsilon_t + \theta_1 \epsilon_{t-1} + \theta_2 \epsilon_{t-2} + \dots + \theta_q \epsilon_{t-q}$
    -   **Parameter ($q$):** The order of the MA model, representing the number of lagged forecast errors in the prediction equation.
    -   **Identification:** The [[TS_Autocorrelation_ACF_PACF|ACF plot]] cuts off after lag $q$.
- [[TS_ARMA_Model|ARMA(p,q) - Autoregressive Moving Average Model]]
    -   **Concept:** A combination of AR and MA models. It models the current value $Y_t$ based on both its own past values and past error terms.
    -   **Equation:** Combines the AR and MA equations.
    -   **Parameters ($p, q$):** The orders of the AR and MA components, respectively.
    -   **Identification:** Both ACF and PACF plots tail off gradually.
- [[TS_ARIMA_Model|ARIMA(p,d,q) - Autoregressive Integrated Moving Average Model]]
    -   **Concept:** An extension of the ARMA model that can be applied to **non-stationary** time series.
    -   **Parameter ($d$):** The **order of differencing**. It represents the number of times the raw observations are differenced to make the series stationary before fitting the ARMA(p,q) model.
    -   **Process:**
        1.  Difference the time series $d$ times to achieve stationarity.
        2.  Identify the $p$ and $q$ orders for the differenced series using ACF/PACF plots.
        3.  Fit the ARMA(p,q) model to the differenced series.
        4.  To forecast, the model's predictions for the differenced series are "integrated" (undifferenced) to return them to the original scale.
- [[TS_SARIMA_Model|SARIMA(p,d,q)(P,D,Q)m - Seasonal ARIMA]]
    -   **Concept:** An extension of ARIMA that explicitly supports time series data with a **seasonal component**.
    -   **Parameters:**
        -   `(p,d,q)`: The non-seasonal part of the model (as in ARIMA).
        -   `(P,D,Q)`: The **seasonal part** of the model, which are similar to the non-seasonal components but involve backshifts of the seasonal period.
            -   `P`: Seasonal AR order.
            -   `D`: Seasonal differencing order.
            -   `Q`: Seasonal MA order.
        -   `m`: The seasonal period (e.g., 12 for monthly data, 4 for quarterly, 7 for daily with weekly seasonality).
    -   >[!question]- When would you choose SARIMA over ARIMA for modeling a time series?
        >You would choose a **SARIMA** model over a standard **ARIMA** model when the time series exhibits a clear and consistent **seasonal pattern**.
        >
        >1.  **Presence of Seasonality:** The primary indicator is the presence of a repeating pattern at a fixed frequency (e.g., sales peaking every December, electricity usage peaking every day in the afternoon).
        >2.  **Visual Evidence:** A plot of the time series shows a regular, periodic fluctuation.
        >3.  **ACF/PACF Plots:** The Autocorrelation Function (ACF) plot of the (differenced) series shows significant spikes at lags corresponding to the seasonal period (e.g., at lags 12, 24, 36 for monthly data).
        >
        >While a standard ARIMA model might be able to capture some seasonality if $p$ is large enough, it's not designed for it and is often less efficient and less interpretable. SARIMA is explicitly designed to handle seasonality by including seasonal AR, differencing, and MA terms, which directly model the relationship between an observation and observations from previous seasons. This generally leads to a more parsimonious and accurate model for seasonal data.

## General Modeling Procedure (Box-Jenkins Method)
1.  **Identification:**
    -   Plot the time series data to check for trends, seasonality, and other patterns.
    -   Use [[TS_Lag_and_Differencing|differencing]] if necessary to make the series stationary.
    -   Examine the ACF and PACF plots of the stationary series to identify potential orders for $p$ and $q$ (and seasonal P, Q).
2.  **Estimation:**
    -   Fit the chosen ARIMA(p,d,q) or SARIMA model to the data. The model uses techniques like Maximum Likelihood Estimation (MLE) to estimate the model coefficients ($\phi$'s and $\theta$'s).
3.  **Diagnostic Checking:**
    -   Evaluate the fitted model. The primary check is to analyze the model's **residuals**. The residuals should ideally be [[TS_White_Noise_and_Random_Walks|white noise]] (i.e., have no remaining autocorrelation).
    -   Plot the ACF of the residuals. If there are no significant spikes, the model is likely adequate.
    -   Use statistical tests like the Ljung-Box test to formally check for autocorrelation in residuals.
    -   Compare models using information criteria like AIC (Akaike Information Criterion) or BIC (Bayesian Information Criterion) - lower values are better.
4.  **Forecasting:**
    -   Use the validated model to forecast future values of the time series.

This family of models provides a powerful framework for forecasting based on the internal structure of a time series.

---

# ARIMA (Autoregressive Integrated Moving Average) Model

## Definition
An **Autoregressive Integrated Moving Average (ARIMA)** model is a generalization of the simpler [[TS_ARMA_Model|Autoregressive Moving Average (ARMA)]] model. ARIMA models are a class of statistical models for analyzing and forecasting time series data. They are particularly powerful because they can be applied to **non-stationary** time series, which are common in real-world scenarios.

The model is specified by three order parameters: **(p, d, q)**.

## Components of ARIMA(p, d, q)
1.  **AR(p) - Autoregressive Component:**
    -   Refers to the use of past values of the time series to predict the current value.
    -   **$p$** is the **order of the autoregressive part**, indicating how many lagged observations are included in the model. This is determined by the [[TS_Autocorrelation_ACF_PACF|PACF plot]].
2.  **I(d) - Integrated Component:**
    -   Refers to the **degree of differencing** applied to the time series to make it stationary.
    -   **$d$** is the **order of differencing**.
        -   $d=0$: The series is already stationary (model is ARMA).
        -   $d=1$: The series is differenced once ($y'_t = y_t - y_{t-1}$) to remove a linear trend.
        -   $d=2$: The series is differenced twice to remove a quadratic trend.
    -   This component is what allows ARIMA to handle non-stationary data.
3.  **MA(q) - Moving Average Component:**
    -   Refers to the use of past forecast errors (random shocks) to predict the current value.
    -   **$q$** is the **order of the moving average part**, indicating how many lagged forecast errors are included in the model. This is determined by the [[TS_Autocorrelation_ACF_PACF|ACF plot]].

In essence, an ARIMA(p,d,q) model is an ARMA(p,q) model fitted to the time series after it has been differenced $d$ times.

## The Box-Jenkins Methodology for ARIMA Modeling
This is the standard iterative process for fitting an ARIMA model:

1.  **Model Identification:**
    -   **Plot the data:** Visually inspect the time series for trends, seasonality, and other patterns.
    -   **Check for [[TS_Stationarity|Stationarity]]:** Use visual inspection (slowly decaying ACF) and statistical tests (e.g., ADF test) to determine if the series is stationary.
    -   **Difference if necessary:** If the series is non-stationary, apply first-order differencing. Re-test for stationarity. If still not stationary, consider second-order differencing. The number of times you difference gives you the **$d$** parameter.
    -   **Identify $p$ and $q$:** Plot the ACF and PACF of the now-stationary (differenced) series.
        -   Look for a cut-off in the **PACF** to identify the AR order **$p$**.
        -   Look for a cut-off in the **ACF** to identify the MA order **$q$**.
        -   If both tail off, an ARMA model is suggested.
2.  **Parameter Estimation:**
    -   Fit the identified ARIMA(p,d,q) model to the original time series data.
    -   The model uses numerical optimization methods (like Maximum Likelihood Estimation) to find the best values for the coefficients ($\phi$'s for AR part, $\theta$'s for MA part).
3.  **Diagnostic Checking:**
    -   Evaluate the fitted model to ensure it's adequate.
    -   **Analyze Residuals:** The residuals of a good model should be [[TS_White_Noise_and_Random_Walks|white noise]] (i.e., have zero mean, constant variance, and no autocorrelation).
    -   Plot the ACF of the residuals. There should be no significant spikes.
    -   Use statistical tests like the Ljung-Box test to formally check for autocorrelation in the residuals.
    -   If the model is inadequate, return to the identification step to try a different model order.
    -   Compare different candidate models using information criteria like AIC (Akaike Information Criterion) or BIC (Bayesian Information Criterion), where lower values are better.
4.  **Forecasting:**
    -   Use the validated model to make forecasts for future time periods.
    -   The model automatically handles the "integration" (un-differencing) to return forecasts on the original scale of the data.

## Python Example (statsmodels)
Let's model the CO2 dataset, which has a clear trend.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import adfuller
from statsmodels.datasets import co2

# Load and prepare data
data = co2.load_pandas().data
y = data['co2'].resample('MS').mean().ffill()

# 1. Identification
# y.plot(title='Monthly CO2 Levels')
# plt.show() # Shows a clear upward trend -> non-stationary

# Check for stationarity
# adf_result = adfuller(y)
# print(f'ADF Test p-value: {adf_result:.4f}') # p-value will be high -> non-stationary

# Difference the data to make it stationary
# y_diff = y.diff().dropna()
# y_diff.plot(title='First-Differenced CO2 Levels')
# plt.show() # Trend is gone, but seasonality remains

# adf_result_diff = adfuller(y_diff)
# print(f'ADF Test p-value on differenced data: {adf_result_diff:.4f}') # p-value will be low -> stationary

# Now, find p and q from ACF/PACF of the differenced series
# fig, axes = plt.subplots(1, 2, figsize=(16, 4))
# plot_acf(y_diff, ax=axes, lags=40)
# plot_pacf(y_diff, ax=axes, lags=40)
# plt.show()
# The ACF/PACF plots will show significant spikes at seasonal lags (12, 24),
# indicating that a SARIMA model is actually more appropriate.
# However, for a simple ARIMA example, we might observe the non-seasonal part.
# Let's assume we identify p=1 and q=1 based on the initial lags. So we'll try ARIMA(1,1,1).

# 2. Estimation
# Fit an ARIMA(1,1,1) model to the original data
# The model will handle the d=1 differencing internally.
# try:
#     model = ARIMA(y, order=(1, 1, 1))
#     model_fit = model.fit()
# except Exception as e:
#     print(f"Model fitting failed, likely due to data issues or statsmodels version: {e}")
#     model_fit = None # Ensure it's defined

# 3. Diagnostic Checking
# if model_fit:
#     print(model_fit.summary())
#     # Plot residuals
#     residuals = pd.DataFrame(model_fit.resid)
#     fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,4))
#     residuals.plot(title="Residuals", ax=ax1)
#     plot_acf(residuals, ax=ax2, title="Residuals ACF")
#     plt.show()
#     # We would still see seasonality in the residuals, confirming SARIMA is better.

# 4. Forecasting
# if model_fit:
#     # Forecast the next 36 months (3 years)
#     forecast = model_fit.get_forecast(steps=36)
#     forecast_ci = forecast.conf_int() # Get confidence intervals

#     ax = y.plot(label='Observed', figsize=(12, 6))
#     forecast.predicted_mean.plot(ax=ax, label='Forecast')
#     ax.fill_between(forecast_ci.index,
#                     forecast_ci.iloc[:, 0],
#                     forecast_ci.iloc[:, 1], color='k', alpha=.25)
#     ax.set_xlabel('Date')
#     ax.set_ylabel('CO2 Levels')
#     plt.legend()
#     plt.show()
```
> **Note:** This example intentionally uses a simple ARIMA on seasonal data to illustrate the process. The diagnostic step correctly reveals that a [[TS_SARIMA_Model|SARIMA]] model would be a better choice to capture the seasonality.

ARIMA models are a powerful and flexible class of models for univariate time series forecasting, especially for data with trends.

---

# ARIMA (Autoregressive Integrated Moving Average) Model

## Definition
An **Autoregressive Integrated Moving Average (ARIMA)** model is a generalization of the simpler [[TS_ARMA_Model|Autoregressive Moving Average (ARMA)]] model. ARIMA models are a class of statistical models for analyzing and forecasting time series data. They are particularly powerful because they can be applied to **non-stationary** time series, which are common in real-world scenarios.

The model is specified by three order parameters: **(p, d, q)**.

## Components of ARIMA(p, d, q)
1.  **AR(p) - Autoregressive Component:**
    -   Refers to the use of past values of the time series to predict the current value.
    -   **$p$** is the **order of the autoregressive part**, indicating how many lagged observations are included in the model. This is determined by the [[TS_Autocorrelation_ACF_PACF|PACF plot]].
2.  **I(d) - Integrated Component:**
    -   Refers to the **degree of differencing** applied to the time series to make it stationary.
    -   **$d$** is the **order of differencing**.
        -   $d=0$: The series is already stationary (model is ARMA).
        -   $d=1$: The series is differenced once ($y'_t = y_t - y_{t-1}$) to remove a linear trend.
        -   $d=2$: The series is differenced twice to remove a quadratic trend.
    -   This component is what allows ARIMA to handle non-stationary data.
3.  **MA(q) - Moving Average Component:**
    -   Refers to the use of past forecast errors (random shocks) to predict the current value.
    -   **$q$** is the **order of the moving average part**, indicating how many lagged forecast errors are included in the model. This is determined by the [[TS_Autocorrelation_ACF_PACF|ACF plot]].

In essence, an ARIMA(p,d,q) model is an ARMA(p,q) model fitted to the time series after it has been differenced $d$ times.

## The Box-Jenkins Methodology for ARIMA Modeling
This is the standard iterative process for fitting an ARIMA model:

1.  **Model Identification:**
    -   **Plot the data:** Visually inspect the time series for trends, seasonality, and other patterns.
    -   **Check for [[TS_Stationarity|Stationarity]]:** Use visual inspection (slowly decaying ACF) and statistical tests (e.g., ADF test) to determine if the series is stationary.
    -   **Difference if necessary:** If the series is non-stationary, apply first-order differencing. Re-test for stationarity. If still not stationary, consider second-order differencing. The number of times you difference gives you the **$d$** parameter.
    -   **Identify $p$ and $q$:** Plot the ACF and PACF of the now-stationary (differenced) series.
        -   Look for a cut-off in the **PACF** to identify the AR order **$p$**.
        -   Look for a cut-off in the **ACF** to identify the MA order **$q$**.
        -   If both tail off, an ARMA model is suggested.
2.  **Parameter Estimation:**
    -   Fit the identified ARIMA(p,d,q) model to the original time series data.
    -   The model uses numerical optimization methods (like Maximum Likelihood Estimation) to find the best values for the coefficients ($\phi$'s for AR part, $\theta$'s for MA part).
3.  **Diagnostic Checking:**
    -   Evaluate the fitted model to ensure it's adequate.
    -   **Analyze Residuals:** The residuals of a good model should be [[TS_White_Noise_and_Random_Walks|white noise]] (i.e., have zero mean, constant variance, and no autocorrelation).
    -   Plot the ACF of the residuals. There should be no significant spikes.
    -   Use statistical tests like the Ljung-Box test to formally check for autocorrelation in the residuals.
    -   If the model is inadequate, return to the identification step to try a different model order.
    -   Compare different candidate models using information criteria like AIC (Akaike Information Criterion) or BIC (Bayesian Information Criterion), where lower values are better.
4.  **Forecasting:**
    -   Use the validated model to make forecasts for future time periods.
    -   The model automatically handles the "integration" (un-differencing) to return forecasts on the original scale of the data.

## Python Example (statsmodels)
Let's model the CO2 dataset, which has a clear trend.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import adfuller
from statsmodels.datasets import co2

# Load and prepare data
data = co2.load_pandas().data
y = data['co2'].resample('MS').mean().ffill()

# 1. Identification
# y.plot(title='Monthly CO2 Levels')
# plt.show() # Shows a clear upward trend -> non-stationary

# Check for stationarity
# adf_result = adfuller(y)
# print(f'ADF Test p-value: {adf_result:.4f}') # p-value will be high -> non-stationary

# Difference the data to make it stationary
# y_diff = y.diff().dropna()
# y_diff.plot(title='First-Differenced CO2 Levels')
# plt.show() # Trend is gone, but seasonality remains

# adf_result_diff = adfuller(y_diff)
# print(f'ADF Test p-value on differenced data: {adf_result_diff:.4f}') # p-value will be low -> stationary

# Now, find p and q from ACF/PACF of the differenced series
# fig, axes = plt.subplots(1, 2, figsize=(16, 4))
# plot_acf(y_diff, ax=axes, lags=40)
# plot_pacf(y_diff, ax=axes, lags=40)
# plt.show()
# The ACF/PACF plots will show significant spikes at seasonal lags (12, 24),
# indicating that a SARIMA model is actually more appropriate.
# However, for a simple ARIMA example, we might observe the non-seasonal part.
# Let's assume we identify p=1 and q=1 based on the initial lags. So we'll try ARIMA(1,1,1).

# 2. Estimation
# Fit an ARIMA(1,1,1) model to the original data
# The model will handle the d=1 differencing internally.
# try:
#     model = ARIMA(y, order=(1, 1, 1))
#     model_fit = model.fit()
# except Exception as e:
#     print(f"Model fitting failed, likely due to data issues or statsmodels version: {e}")
#     model_fit = None # Ensure it's defined

# 3. Diagnostic Checking
# if model_fit:
#     print(model_fit.summary())
#     # Plot residuals
#     residuals = pd.DataFrame(model_fit.resid)
#     fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,4))
#     residuals.plot(title="Residuals", ax=ax1)
#     plot_acf(residuals, ax=ax2, title="Residuals ACF")
#     plt.show()
#     # We would still see seasonality in the residuals, confirming SARIMA is better.

# 4. Forecasting
# if model_fit:
#     # Forecast the next 36 months (3 years)
#     forecast = model_fit.get_forecast(steps=36)
#     forecast_ci = forecast.conf_int() # Get confidence intervals

#     ax = y.plot(label='Observed', figsize=(12, 6))
#     forecast.predicted_mean.plot(ax=ax, label='Forecast')
#     ax.fill_between(forecast_ci.index,
#                     forecast_ci.iloc[:, 0],
#                     forecast_ci.iloc[:, 1], color='k', alpha=.25)
#     ax.set_xlabel('Date')
#     ax.set_ylabel('CO2 Levels')
#     plt.legend()
#     plt.show()
```
> **Note:** This example intentionally uses a simple ARIMA on seasonal data to illustrate the process. The diagnostic step correctly reveals that a [[TS_SARIMA_Model|SARIMA]] model would be a better choice to capture the seasonality.

ARIMA models are a powerful and flexible class of models for univariate time series forecasting, especially for data with trends.

---