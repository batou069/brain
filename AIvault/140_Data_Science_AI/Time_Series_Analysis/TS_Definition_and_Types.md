---
tags:
  - time_series
  - definition
  - univariate
  - multivariate
  - concept
aliases:
  - Time Series
  - Univariate Time Series
  - Multivariate Time Series
related:
  - "[[_Time_Series_Analysis_MOC|_Time_Series_Analysis_MOC]]"
  - "[[TS_Forecasting_vs_Prediction]]"
worksheet:
  - WS_TimeSeries_1
date_created: 2025-08-27
---
# Time Series: Definition and Types

## Definition
A **time series** is a sequence of data points collected or recorded at specific, successive points in time. These data points are typically ordered chronologically, and the time intervals between them are often (but not always) uniform.

The key characteristic of time series data is its **temporal dependence**, meaning the value of an observation at a given time is often dependent on the values of previous observations.

**Formal Notation:** A time series is often denoted as a set of observations $Y = \{y_{t_1}, y_{t_2}, \dots, y_{t_N}\}$, where $y_{t_i}$ is the value observed at time $t_i$. For equally spaced time points, this is simplified to $Y = \{y_1, y_2, \dots, y_T\}$.

## Types of Time Series

[list2tab|#Time Series Types]
- Univariate
    -   **Definition:** A time series that consists of single observations recorded sequentially over equal time increments. It involves only **one time-dependent variable**.
    -   **Goal:** The primary goal is to model and forecast future values of that single variable based on its own past values (its history).
    -   **Examples:**
        -   Monthly sales data for a single product.
        -   Daily closing price of a single stock.
        -   Hourly temperature readings for a specific city.
        -   Quarterly GDP of a country.
    -   **Models:** Classical models like [[TS_ARIMA_Family_Models|ARIMA]], [[TS_Exponential_Smoothing|Exponential Smoothing]], and [[TS_Prophet_Model|Prophet]] are primarily designed for univariate time series.
    -   **Example Data Structure:**
        | Date       | Sales |
        |------------|-------|
        | 2023-01-01 | 250   |
        | 2023-01-02 | 265   |
        | 2023-01-03 | 248   |
- Multivariate
    -   **Definition:** A time series that consists of multiple variables recorded at the same time points. It involves **two or more time-dependent variables**.
    -   **Goal:** The goal can be to forecast one or more of the variables, taking into account not only their own past values but also the past values and interdependencies of the other variables.
    -   **Examples:**
        -   Daily sales, advertising spend, and website traffic for a company.
        -   Hourly weather data for a city, including temperature, humidity, wind speed, and pressure.
        -   Quarterly economic data for a country, including GDP, inflation rate, and unemployment rate.
    -   **Models:** Specialized models are required to handle the interdependencies between variables, such as [[TS_Vector_Autoregression_VAR|Vector Autoregression (VAR)]], VARMA, or using machine learning models like Random Forest or neural networks (LSTMs, Transformers) with multiple input features.
    -   **Example Data Structure:**
        | Date       | Sales | Ad Spend | Web Traffic |
        |-----------------|------|-------|-----------------|
        | 2023-01-01 | 250  | 50    | 1200            |
        | 2023-01-02 | 265  | 55    | 1350            |
        | 2023-01-03 | 248  | 45    | 1180            |

## Key Characteristics to Analyze
Regardless of the type, time series analysis involves identifying and modeling several key characteristics:
-   **[[TS_Components_Decomposition|Trend]]:** The long-term direction of the series.
-   **[[TS_Components_Decomposition|Seasonality]]:** Regular, predictable patterns that repeat over a fixed period (e.g., daily, weekly, yearly).
-   **[[TS_Components_Decomposition|Cyclicality]]:** Patterns that are not of a fixed period, often related to longer-term economic or business cycles.
-   **[[TS_Stationarity|Stationarity]]:** A statistical property where the series' properties (mean, variance, autocorrelation) are constant over time.
-   **[[TS_Autocorrelation_ACF_PACF|Autocorrelation]]:** The correlation of the series with its own past values (lags).

Understanding whether you are dealing with a univariate or multivariate time series is the first step in selecting the appropriate modeling techniques and analytical approaches.

---