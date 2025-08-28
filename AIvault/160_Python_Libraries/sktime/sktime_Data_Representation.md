---
tags:
  - python
  - sktime
  - time_series
  - data_representation
  - pandas
  - numpy
  - concept
aliases:
  - sktime Data Structures
  - sktime Data Formats
related:
  - "[[160_Python_Libraries/sktime/_sktime_MOC|_sktime_MOC]]"
  - "[[_Pandas_MOC]]"
worksheet:
  - WS_TimeSeries_1
date_created: 2025-08-27
---
# sktime: Data Representation

`sktime` uses standard Python data science libraries, primarily **[[_Pandas_MOC|Pandas]]**, for representing time series data. Understanding these data structures is key to using the library effectively.

## Univariate Time Series
-   **Representation:** A `pandas.Series`.
-   **Index:** The index of the Series must be a valid time series index. `sktime` is flexible and supports several types:
    -   `pd.PeriodIndex` (preferred for fixed-frequency data, e.g., monthly, daily).
    -   `pd.DatetimeIndex` (for specific points in time).
    -   `pd.RangeIndex` or `pd.Int64Index` (for integer time points).
-   **Values:** The values of the Series are the observations, typically numerical (`float` or `int`).

**Example:**
```python
import pandas as pd
from sktime.datasets import load_airline

# load_airline() returns a pandas Series with a PeriodIndex
y = load_airline()

print("--- Univariate Time Series (sktime) ---")
print("Type:", type(y))
print("Index Type:", type(y.index))
print("Dtype of values:", y.dtype)
print("\nHead of the series:")
print(y.head())
```

## Multivariate Time Series
-   **Representation:** A `pandas.DataFrame`.
-   **Index:** Same as for univariate series (e.g., `pd.PeriodIndex`, `pd.DatetimeIndex`).
-   **Columns:** Each column represents a different variable of the time series.
-   **Values:** All columns should contain numerical data.

**Example:**
```python
import pandas as pd
from sktime.datasets import load_longley

# load_longley() returns a DataFrame with multiple economic variables and a PeriodIndex
y, X = load_longley() # y is the target series, X are the exogenous variables

# Combine them for a multivariate representation
longley_df = pd.concat([y, X], axis=1)

print("\n--- Multivariate Time Series (sktime) ---")
print("Type:", type(longley_df))
print("Index Type:", type(longley_df.index))
print("\nHead of the DataFrame:")
print(longley_df.head())
```

## Panel Data (Collections of Time Series)
For tasks like time series classification, regression, or clustering, the input is often a collection of multiple time series (a panel). `sktime` supports several formats for this, most commonly nested `pandas` DataFrames.

-   **Representation:** A `pandas.DataFrame` where at least one column contains `pandas.Series` objects.
-   **Structure:**
    -   Each row represents a single time series instance.
    -   Columns can contain metadata (like class labels).
    -   One or more columns contain the actual time series data, where each cell holds an entire `pandas.Series`.

**Example (for Time Series Classification):**
```python
import pandas as pd
from sktime.datasets import load_arrow_head

# Load a sample time series classification dataset
X_train, y_train = load_arrow_head(split="train")

print("\n--- Panel Data for Classification (sktime) ---")
print("Type of X_train:", type(X_train))
print("Shape of X_train DataFrame:", X_train.shape)
print("\nHead of the panel DataFrame:")
print(X_train.head())

# Inspect a single cell to see the nested Series
print("\nInspecting a single time series instance (first row, first column):")
first_series = X_train.iloc
print("Type of cell content:", type(first_series))
print("Content:\n", first_series)
```This nested structure is powerful because it keeps related time series data organized in a single DataFrame, along with any associated metadata or labels. `sktime`'s algorithms are designed to work with these nested structures for panel data tasks.

## Forecasting Horizon (`fh`)
When forecasting, `sktime` requires a **Forecasting Horizon** to specify *which* future time points to predict. This is not a data container but an object that defines the prediction time points relative to the training data.

-   **Representation:** A `numpy` array, a list of integers, or a `sktime.forecasting.base.ForecastingHorizon` object.
-   **Types:**
    -   **Relative:** Specifies steps *relative* to the end of the training data (e.g., `fh = np.arange(1, 13)` to predict the next 12 months).
    -   **Absolute:** Specifies the actual index points to predict (e.g., `fh = pd.PeriodIndex(['1961-01', '1961-02'], freq='M')`).

**Example:**```python
import numpy as np
from sktime.forecasting.base import ForecastingHorizon

# Relative horizon: predict the next 3 time steps
fh_relative = ForecastingHorizon()
print(f"\nRelative Forecasting Horizon: {fh_relative}")

# Absolute horizon: predict specific dates
# (assuming y is the airline dataset)
fh_absolute = ForecastingHorizon(y_test.index, is_relative=False)
print(f"Absolute Forecasting Horizon: {fh_absolute}")
```

By adhering to these data representation conventions, `sktime` can provide a consistent and powerful API for a wide range of time series tasks.

---