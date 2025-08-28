---
tags:
  - time_series
  - forecasting
  - ar_model
  - autoregressive
  - arima
  - concept
aliases:
  - AR Model
  - Autoregressive Model
related:
  - "[[TS_ARIMA_Family_Models]]"
  - "[[TS_Autocorrelation_ACF_PACF]]"
  - "[[TS_Stationarity]]"
worksheet:
  - WS_TimeSeries_1
date_created: 2025-08-27
---
# Autoregressive (AR) Model

## Definition
An **Autoregressive (AR)** model is a type of statistical model for time series data where the current value of the series, $Y_t$, is expressed as a linear combination of its own past values (lags), plus a random error term (white noise).

The term "autoregressive" indicates that it is a regression of the variable against itself.

An AR model of order **$p$**, denoted **AR(p)**, is defined by the equation:
$$ Y_t = c + \phi_1 Y_{t-1} + \phi_2 Y_{t-2} + \dots + \phi_p Y_{t-p} + \epsilon_t $$
where:
-   $Y_t$ is the value of the time series at time $t$.
-   $c$ is a constant (intercept).
-   $\phi_1, \phi_2, \dots, \phi_p$ are the model parameters (coefficients for the lags).
-   $p$ is the **order** of the model, indicating how many past values are included.
-   $Y_{t-1}, \dots, Y_{t-p}$ are the past (lagged) values of the series.
-   $\epsilon_t$ is a white noise error term at time $t$.

## Key Characteristics
-   **Dependency on Past Values:** The model explicitly uses the past to predict the future.
-   **Stationarity Requirement:** AR models are defined for [[TS_Stationarity|stationary]] time series. If a series is non-stationary, it must be differenced first.
-   **Model Identification (Order $p$):**
    -   The primary tool for identifying the order $p$ is the **[[TS_Autocorrelation_ACF_PACF|Partial Autocorrelation Function (PACF)]]** plot.
    -   For a pure AR(p) process, the PACF plot will show a sharp **cut-off after lag $p$**. The partial autocorrelations for lags greater than $p$ will be non-significant (within the confidence interval).
    -   The Autocorrelation Function (ACF) plot for an AR(p) process will typically show a gradual, tapering decay (either exponentially or as a damped sine wave).

>[!question]- How do you determine the appropriate lag order for an autoregressive model?
>The appropriate lag order ($p$) for an AR model is determined by analyzing the **Partial Autocorrelation Function (PACF) plot** of the stationary time series.
>
>1.  **Ensure Stationarity:** First, make sure your time series is stationary. If not, apply [[TS_Lag_and_Differencing|differencing]] until it is.
>2.  **Plot the PACF:** Generate the PACF plot for the stationary series.
>3.  **Identify the Cut-off:** Look for the lag after which the PACF values abruptly drop to non-significance (i.e., fall inside the confidence interval band, usually shaded blue).
>4.  **Determine Order $p$:** The last significant lag before the cut-off is the suggested order $p$ for the AR model.
>
>**Example Interpretation:**
>-   If the PACF has a significant spike at lag 1 and then cuts off, it suggests an **AR(1)** model.
>-   If the PACF has significant spikes at lags 1 and 2 and then cuts off, it suggests an **AR(2)** model.
>
>While the PACF plot is the primary guide, it's also good practice to fit a few candidate models (e.g., if lag 2 is borderline significant, you might try both AR(1) and AR(2)) and compare them using information criteria like AIC or BIC to select the best model.

## Example
-   **AR(1) Model:** $Y_t = c + \phi_1 Y_{t-1} + \epsilon_t$
    -   If $\phi_1 = 0$, the series is just white noise.
    -   If $\phi_1 = 1$ and $c=0$, the series is a [[TS_White_Noise_and_Random_Walks|random walk]] (non-stationary).
    -   If $0 < \phi_1 < 1$, the series shows positive autocorrelation and tends to revert to its mean.
    -   If $-1 < \phi_1 < 0$, the series shows negative autocorrelation, tending to oscillate around its mean.

AR models are a fundamental component of the more general [[TS_ARIMA_Family_Models|ARIMA]] and [[TS_SARIMA_Model|SARIMA]] models.

---