---
tags:
  - time_series
  - preprocessing
  - missing_values
  - imputation
  - interpolation
  - concept
  - pandas
  - sktime
aliases:
  - Handling Missing Data in Time Series
  - Time Series Imputation
related:
  - "[[140_Data_Science_AI/Time_Series_Analysis/_Time_Series_Analysis_MOC|_Time_Series_Analysis_MOC]]"
  - "[[TS_Forecasting_vs_Prediction]]"
worksheet:
  - WS_TimeSeries_1
date_created: 2025-08-28
---
# Handling Missing Values in Time Series

Missing values are a common problem in real-world time series data. They can occur due to sensor failures, data transmission errors, or manual data entry issues. Handling them appropriately is crucial because many time series models cannot work with missing data, and improper handling can distort the temporal structure of the series.

>[!question]- How do you handle missing values in a time series, and why is simple mean imputation often a bad idea?
>
>**Why Simple Mean Imputation is Often Bad:**
>Using the overall mean of the entire series to fill in missing values is generally a poor choice for time series data because:
>1.  **It Ignores Temporality:** It completely disregards the time-dependent nature of the data. A value in 2023 is likely to be more similar to its neighbors in 2023 than to the overall average of data from 2010-2023.
>2.  **It Distorts Trends:** If the series has an upward trend, filling a missing value with the overall mean will create an artificial dip in the data, disrupting the trend.
>3.  **It Distorts Seasonality:** It can flatten out seasonal peaks and troughs, masking important periodic patterns.
>4.  **It Reduces Variance:** It artificially reduces the variance of the time series.
>
>In short, it fails to preserve the structural components (trend, seasonality, autocorrelation) that are essential for time series analysis.

## Better Methods for Handling Missing Values in Time Series

[list2tab|#TS Imputation Methods]
- Simple Imputation Methods (Use with Caution)
    -   **Forward Fill (`ffill`):**
        -   **Method:** Propagates the last valid observation forward to fill the gap.
        -   **Assumption:** The value of the series remains constant after the last known observation.
        -   **Use Case:** Good for data that changes infrequently or when you want to avoid look-ahead bias.
    -   **Backward Fill (`bfill`):**
        -   **Method:** Propagates the next valid observation backward to fill the gap.
        -   **Assumption:** The value was constant leading up to the next known observation.
        -   **Caution:** This introduces look-ahead bias, as it uses future information. It can be acceptable for cleaning historical data for visualization but should be avoided in features used for training a forecasting model.
- Interpolation Methods
    -   **Method:** Fills missing values by estimating them based on other data points.
    -   **Types:**
        -   **Linear Interpolation:** Fills missing values by drawing a straight line between the points before and after the gap. A good general-purpose starting point.
        -   **Spline/Polynomial Interpolation:** Uses a curve (spline or polynomial) to fill the gap, which can be better for non-linear series.
        -   **Seasonal Interpolation:** More advanced methods that take seasonality into account.
    -   **Caution:** Like backward fill, interpolation uses future information to fill a gap, which can introduce look-ahead bias. It's often suitable for data exploration and visualization but requires care when used for model training.
- Model-Based Imputation
    -   **Method:** Use a forecasting model to predict the missing values.
    -   **Process:**
        1.  Treat the missing values as points to be forecasted.
        2.  Train a time series model (like ARIMA, Exponential Smoothing, or even an ML model) on the data surrounding the missing value(s).
        3.  Use the model to predict the values for the missing time steps.
    -   **Use Case:** A more sophisticated and often more accurate approach, especially for larger gaps. `sktime`'s `Imputer` can use a forecaster for this.
- Using a Rolling Window Mean/Median
    -   **Method:** Fill the missing value with the mean or median of a rolling window of data points immediately preceding it.
    -   **Advantage:** Better than the global mean as it uses local, more recent information and adapts to the series' changing level.

## Python Example with `sktime` and `pandas`
`sktime` provides a convenient `Imputer` transformer that can be used in pipelines.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sktime.transformations.series.impute import Imputer
from sktime.datasets import load_airline

# Load data and introduce some missing values
y = load_airline()
y.index = y.index.to_timestamp() # Use Timestamp for easier plotting
y_missing = y.copy()
y_missing.iloc] = np.nan # Create a gap

# --- 1. Using sktime's Imputer ---
# Impute with the mean of a rolling window of size 12
imputer_rolling_mean = Imputer(method="mean", window_length=12)
y_imputed_rolling = imputer_rolling_mean.fit_transform(y_missing)

# Impute with linear interpolation
imputer_linear = Imputer(method="linear")
y_imputed_linear = imputer_linear.fit_transform(y_missing)

# Impute with forward fill
imputer_ffill = Imputer(method="ffill")
y_imputed_ffill = imputer_ffill.fit_transform(y_missing)

# --- 2. Using pandas directly (for comparison) ---
# y_imputed_pandas_ffill = y_missing.fillna(method='ffill')
# y_imputed_pandas_linear = y_missing.interpolate(method='linear')

# --- Visualize the results ---
# fig, ax = plt.subplots(figsize=(12, 6))
# y.plot(ax=ax, style='--', label='Original Data', color='gray')
# y_missing.plot(ax=ax, style='o-', label='Data with Missing Values')
# y_imputed_rolling.plot(ax=ax, style='.-', label='Imputed (Rolling Mean)')
# y_imputed_linear.plot(ax=ax, style='.-', label='Imputed (Linear Interpolation)')
# y_imputed_ffill.plot(ax=ax, style='.-', label='Imputed (Forward Fill)')
# ax.set_title("Comparing Time Series Imputation Methods")
# ax.set_xlabel("Date")
# ax.set_ylabel("Airline Passengers")
# ax.legend()
# plt.grid(True)
# plt.show()
```

The choice of imputation method depends on the nature of the data and the specific task. For forecasting, methods that do not use future information (like forward fill or rolling window statistics based on past data) are the safest to prevent look-ahead bias.

---