---
tags:
  - time_series
  - decomposition
  - trend
  - seasonality
  - cyclicality
  - residual
  - noise
  - concept
  - statsmodels
aliases:
  - Time Series Components
  - Time Series Decomposition
  - Trend
  - Seasonality
  - Cyclicality
  - Residuals
related:
  - "[[_Time_Series_Analysis_MOC|_Time_Series_Analysis_MOC]]"
  - "[[TS_Stationarity]]"
  - "[[TS_Decomposition_Methods]]"
worksheet:
  - WS_TimeSeries_1
date_created: 2025-08-27
---
# Components of a Time Series & Decomposition

A time series can often be thought of as a combination of several underlying components. **Time Series Decomposition** is the process of separating a time series into these constituent parts. This is a powerful tool for understanding the underlying patterns in the data and is often a crucial step before forecasting.

A time series ($Y_t$) is typically decomposed into:
-   **Trend ($T_t$)**
-   **Seasonality ($S_t$)**
-   **Cyclicality ($C_t$)** (often combined with Trend)
-   **Residual / Noise / Irregular component ($R_t$ or $\epsilon_t$)**

## Decomposition Models
There are two primary models for combining these components:

1.  **Additive Model:**
    $$ Y_t = T_t + S_t + C_t + R_t $$
    -   **Assumption:** The magnitude of the seasonal and cyclical effects is independent of the trend. The seasonality has the same amplitude and frequency over time.
    -   **Use Case:** Suitable for time series where the seasonal variation is roughly constant over time.

2.  **Multiplicative Model:**
    $$ Y_t = T_t \times S_t \times C_t \times R_t $$
    -   **Assumption:** The magnitude of the seasonal and cyclical effects is proportional to the level of the trend. The seasonality's amplitude increases or decreases as the trend increases or decreases.
    -   **Use Case:** Common in economic time series (e.g., retail sales) where seasonal fluctuations grow as the overall sales trend grows.
    -   A multiplicative model can often be converted to an additive model by taking the logarithm: $\log(Y_t) = \log(T_t) + \log(S_t) + \log(C_t) + \log(R_t)$.

## The Components in Detail

[list2tab|#Time Series Components]
- Trend ($T_t$)
    -   **Definition:** The long-term, underlying direction of the time series. It represents the general increase, decrease, or stagnation in the data over a long period.
    -   **Examples:**
        -   Upward trend: Annual sales of a growing company.
        -   Downward trend: Market share of an obsolete technology.
        -   No trend: Annual rainfall in a stable climate.
    -   **Identification:** Visual inspection of the plot, moving averages, regression.
- Seasonality ($S_t$)
    -   **Definition:** A regular and predictable pattern that repeats over a **fixed and known period**. This period is called the seasonal period.
    -   **Examples:**
        -   Retail sales peaking before Christmas (yearly seasonality).
        -   Electricity consumption being higher during the day and lower at night (daily seasonality).
        -   Restaurant traffic being higher on weekends (weekly seasonality).
    -   **Identification:** Box plots grouped by the seasonal period (e.g., month, day of the week), autocorrelation plots ([[TS_Autocorrelation_ACF_PACF|ACF]]) showing peaks at seasonal lags.
- Cyclicality ($C_t$)
    -   **Definition:** Patterns or fluctuations that occur at **irregular and non-fixed intervals**. Cycles are typically longer than seasonal patterns.
    -   **Examples:**
        -   Business cycles (recession, expansion) which can last for several years.
        -   El Niño/La Niña weather cycles.
    -   **Identification:** Harder to identify than seasonality. Often requires domain knowledge and observing long-term data.
    -   >[!question]- What is the difference between seasonality and cyclicality?
        >The key difference is **regularity and predictability of the period**.
        >
        >-   **Seasonality** is a pattern that repeats over a **fixed, known, and predictable period** (e.g., every 12 months, every 7 days, every 24 hours). The duration of the pattern is constant.
        >-   **Cyclicality** is a pattern of rises and falls that is **not of a fixed period**. The duration of a cycle can vary, and its timing is not as predictable as seasonality. Cycles are typically longer than seasonal patterns.
        >
        >In practice, for many decomposition methods, the cyclical component is often combined with the trend component to form a "trend-cycle" component because it's difficult to separate them without very long series and domain expertise.
- Residual / Noise ($R_t$)
    -   **Definition:** The random, irregular, and unpredictable component of the time series that remains after the trend, seasonality, and cyclical components have been removed.
    -   **Ideal Properties:** For a good decomposition and model, the residuals should ideally be [[TS_White_Noise_and_Random_Walks|white noise]] (i.e., have a mean of zero, constant variance, and no autocorrelation).
    -   **Identification:** Analyzing the residual plot after decomposition. If patterns (like autocorrelation) remain in the residuals, it suggests the model has not captured all the underlying structure.

## Decomposition in Practice (Python Example)

>[!question]- How can time series decomposition help in understanding and forecasting a time series?
>Decomposition is a powerful analytical tool with several benefits:
>
>1.  **Better Understanding of Data:** It breaks down a complex series into simpler, more interpretable components. This helps in identifying:
>    -   The long-term growth or decline (Trend).
>    -   Predictable periodic patterns (Seasonality).
>    -   The magnitude of random fluctuations (Residuals).
>2.  **Improved Forecasting:**
>    -   **Separate Forecasting:** You can forecast each component separately and then combine them to get the final forecast. For example, you can use a simple linear model for the trend, repeat the last seasonal cycle for seasonality, and assume residuals are zero.
>    -   **Deseasonalizing Data:** Many statistical models (like [[TS_ARIMA_Family_Models|ARIMA]]) require the data to be [[TS_Stationarity|stationary]]. By identifying and removing the trend and seasonality, you can model the remaining stationary component. The trend and seasonality can then be added back to the forecast of the stationary component.
>3.  **Anomaly Detection:** By analyzing the residual component, you can identify unusual data points (anomalies or outliers) that don't fit the typical trend and seasonal patterns.
>4.  **Model Selection:** The characteristics of the decomposed components can guide the choice of an appropriate forecasting model. For example, a strong seasonal component suggests using a model that can handle seasonality, like [[TS_SARIMA_Model|SARIMA]] or [[TS_Exponential_Smoothing|Holt-Winters]].

The `statsmodels` library in Python provides tools for classical and STL decomposition.

```python
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose, STL
# Using a sample dataset from statsmodels for demonstration
from statsmodels.datasets import co2

# Load monthly CO2 data
data = co2.load_pandas().data
# Resample to monthly start, fill missing values
y = data['co2'].resample('MS').mean().ffill()

# 1. Classical Decomposition (Additive)
# Simple, but can have issues with endpoints
additive_decomposition = seasonal_decompose(y, model='additive', period=12)

# 2. STL Decomposition (Seasonal-Trend decomposition using LOESS)
# More robust and flexible than classical decomposition
stl_decomposition = STL(y, period=12).fit()

# Plotting the STL decomposition
fig = stl_decomposition.plot()
fig.suptitle('STL Decomposition of CO2 Data', y=1.02)
plt.tight_layout()
plt.show()

# Accessing the components
trend_component = stl_decomposition.trend
seasonal_component = stl_decomposition.seasonal
residual_component = stl_decomposition.resid
```
The resulting plot clearly shows the strong upward trend, the regular yearly seasonality, and the remaining residuals.

### Example using `sktime` and `statsmodels`
This example shows how decomposition is used as a preprocessing step. A machine learning model would then be trained on the deseasonalized data or on the components as separate features.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sktime.transformations.series.detrend import Deseasonalizer, Detrender
from sktime.datasets import load_airline
from sktime.utils.plotting import plot_series

# Load a classic time series dataset with trend and seasonality
y = load_airline()

# --- Decompose using sktime transformers ---
# 1. Remove the multiplicative seasonality
# The 'sp' parameter specifies the seasonal period (12 for monthly data)
deseasonalizer = Deseasonalizer(model="multiplicative", sp=12)
y_deseasonalized = deseasonalizer.fit_transform(y)

# 2. Remove the trend from the deseasonalized data
# We can use a polynomial detrender
detrender = Detrender(forecaster=None) # Uses linear regression by default
y_detrended_deseasonalized = detrender.fit_transform(y_deseasonalized)

# The result of these transformations is the residual component
residuals_sktime = y_detrended_deseasonalized

# --- Visualize the components ---
# To get the trend and seasonal components themselves for plotting:
trend_sktime = detrender.forecaster_.predict(fh=np.arange(len(y)) + 1)
# The seasonal component is y_deseasonalized / trend_sktime
seasonal_sktime = y_deseasonalized / trend_sktime

# fig, axes = plt.subplots(4, 1, figsize=(10, 8), sharex=True)
# plot_series(y, ax=axes, labels=["Original Data"])
# plot_series(trend_sktime, ax=axes, labels=["Trend (sktime)"])
# plot_series(seasonal_sktime, ax=axes, labels=["Seasonality (sktime)"])
# plot_series(residuals_sktime, ax=axes, labels=["Residuals (sktime)"])
# plt.suptitle("Time Series Decomposition with sktime", y=0.99)
# plt.tight_layout()
# plt.show()

# --- For comparison, the classic statsmodels decomposition ---
from statsmodels.tsa.seasonal import seasonal_decompose
result_sm = seasonal_decompose(y, model='multiplicative', period=12)
# result_sm.plot()
# plt.suptitle("Time Series Decomposition with statsmodels", y=1.02)
# plt.show()
```
>
**Note on `tsfresh`:** `tsfresh` is not used for decomposition. It's a feature extraction library. After decomposing a series, you could potentially use `tsfresh` to extract features from the **residual component** to see if any complex, non-obvious patterns remain. For example:
> ```python
> from tsfresh import extract_features
> from tsfresh.feature_extraction import ComprehensiveFCParameters
> 
> # Assuming 'residuals_sktime' is a pandas Series from the sktime example
> # tsfresh requires a specific DataFrame format: [id, time, value]
> residuals_df = residuals_sktime.to_frame(name="value")
> residuals_df['id'] = 'co2_series'
> residuals_df['time'] = residuals_sktime.index.to_timestamp() # Convert PeriodIndex to Timestamp
> 
> # Extract features from the residuals
> # This would be a large set of features
> extracted_features = extract_features(residuals_df, column_id="id", column_sort="time",
>                                       default_fc_parameters=ComprehensiveFCParameters())
> print("Shape of extracted features from residuals:", extracted_features.shape)
> print(extracted_features.head())
> ```
> This demonstrates how `tsfresh` can be used as an *extension* to analyze the output of a decomposition process.
> 
---