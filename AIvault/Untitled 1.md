
Filename: 140_Data_Science_AI/Time_Series_Analysis/TS_White_Noise_and_Random_Walks.md
````markdown
[[TS_White_Noise_and_Random_Walks]]
````

`````markdown

Filename: 140_Data_Science_AI/Time_Series_Analysis/TS_Forecasting_vs_Prediction.md
````markdown
[[TS_Forecasting_vs_Prediction]]
````

`````markdown

Filename: 140_Data_Science_AI/Time_Series_Analysis/TS_Handling_Missing_Values.md
````markdown
[[TS_Handling_Missing_Values]]---
        -   **Assumption:** The value was constant leading up to the next known observation.
        -   **Caution:** This introduces look-ahead bias, as it uses future information. It can be acceptable for cleaning historical data for visualization but should be avoided in features used for training a forecasting model.
​￼- Interpolation Methods
    -   **Method:** Fills missing values by estimating them based on other data points.
    ​￼-   **Types:**
        -   **Linear Interpolation:** Fills missing values by drawing a straight line between the points before and after the gap. A good general-purpose starting point.
        -   **Spline/Polynomial Interpolation:** Uses a curve (spline or polynomial) to fill the gap, which can be better for non-linear series.
        -   **Seasonal Interpolation:** More advanced methods that take seasonality into account.
    -   **Caution:** Like backward fill, interpolation uses future information to fill a gap, which can introduce look-ahead bias. It's often suitable for data exploration and visualization but requires care when used for model training.
​￼- Model-Based Imputation
    -   **Method:** Use a forecasting model to predict the missing values.
    ​￼-   **Process:**
        1.  Treat the missing values as points to be forecasted.
        2.  Train a time series model (like ARIMA, Exponential Smoothing, or even an ML model) on the data surrounding the missing value(s).
        3.  Use the model to predict the values for the missing time steps.
    -   **Use Case:** A more sophisticated and often more accurate approach, especially for larger gaps. `sktime`'s `Imputer` can use a forecaster for this.
​￼- Using a Rolling Window Mean/Median
    -   **Method:** Fill the missing value with the mean or median of a rolling window of data points immediately preceding it.
    -   **Advantage:** Better than the global mean as it uses local, more recent information and adapts to the series' changing level.

​￼## Python Example with `sktime` and `pandas`
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

# ￼–￼- 1. Using sktime's Imputer ￼–￼-
# Impute with the mean of a rolling window of size 12
imputer_rolling_mean = Imputer(method="mean", window_length=12)
y_imputed_rolling = imputer_rolling_mean.fit_transform(y_missing)

# Impute with linear interpolation
imputer_linear = Imputer(method="linear")
y_imputed_linear = imputer_linear.fit_transform(y_missing)

# Impute with forward fill
imputer_ffill = Imputer(method="ffill")
y_imputed_ffill = imputer_ffill.fit_transform(y_missing)

# ￼–￼- 2. Using pandas directly (for comparison) ￼–￼-
# y_imputed_pandas_ffill = y_missing.fillna(method='ffill')
# y_imputed_pandas_linear = y_missing.interpolate(method='linear')

# ￼–￼- Visualize the results ￼–￼-
# fig, ax = plt.subplots(figsize=(12, 6))
# y.plot(ax=ax, style='￼–￼', label='Original Data', color='gray')
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
````

This covers the next set of notes. I will continue with the remaining models and concepts from your list.