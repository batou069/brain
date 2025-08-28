---
tags:
  - time_series
  - forecasting
  - machine_learning
  - feature_engineering
  - lag_features
  - rolling_window
  - sktime
  - tsfresh
  - concept
aliases:
  - Time Series Feature Engineering
  - Features for Time Series ML
related:
  - "[[140_Data_Science_AI/Time_Series_Analysis/_Time_Series_Analysis_MOC|_Time_Series_Analysis_MOC]]"
  - "[[TS_Rolling_Window_Operations]]"
  - "[[TS_Lag_and_Differencing]]"
  - "[[160_Python_Libraries/sktime/_sktime_MOC|sktime]]"
  - "[[160_Python_Libraries/tsfresh/_tsfresh_MOC|tsfresh]]"
worksheet:
  - WS_TimeSeries_1
date_created: 2025-08-27
---
# Feature Engineering for Time Series Machine Learning

>[!question]- How can you use a model like Random Forest, which doesn't inherently understand time, for a forecasting problem?
>Standard machine learning models like Random Forest, Gradient Boosting, or Linear Regression do not inherently understand the sequential nature of time series data. To use them for forecasting, you must **transform the time series problem into a standard supervised learning problem**.
>
>This is done through **feature engineering**, where you create a set of input features (X) and a target variable (y) from the original time series. The key is to create features that capture the temporal dependencies.
>
>The main types of features created are:
>1.  **Lag Features:** Past values of the time series itself. For example, to predict the value at time `t`, you might use the values at `t-1`, `t-2`, `t-3`, etc., as input features.
>2.  **Rolling Window Features:** Statistics calculated over a sliding window of past values (e.g., the rolling mean or standard deviation over the last 7 days). This summarizes the recent trend and volatility.
>3.  **Date/Time Features:** Features derived from the timestamp itself, such as the hour of the day, day of the week, month, year, quarter, or flags for holidays. This helps the model learn seasonal and calendar-based patterns.
>
>Once you have this feature matrix `X` and target vector `y`, you can train any standard regression model (like `sklearn.ensemble.RandomForestRegressor`) to learn the mapping from `X` to `y`.

## Example: Creating Features with `sktime` and `sklearn`

This example shows how to create lag and rolling window features to prepare a time series for a machine learning model.

```python
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sktime.transformations.series.lag import Lag
from sktime.transformations.series.window_summarizer import WindowSummarizer
from sktime.forecasting.base import ForecastingHorizon
from sktime.forecasting.compose import make_reduction
from sktime.datasets import load_airline

# Load data
y = load_airline()
# sktime uses PeriodIndex, for some sklearn/pandas functions, a Timestamp index is easier
y.index = y.index.to_timestamp()

# --- Feature Engineering without tsfresh ---
# We will use sktime's transformers to create features.
# sktime's make_reduction automatically handles this feature creation and model wrapping.

# Define the forecasting horizon (e.g., predict the next 12 months)
fh = ForecastingHorizon(np.arange(1, 13))

# Create a regressor that will be used for forecasting
regressor = RandomForestRegressor(random_state=42)

# Use make_reduction to convert the forecasting task into a regression task.
# It will automatically create lag features. We can also add rolling window features.
# Let's specify lags 1 through 12, and a rolling mean over a window of 12.
forecaster = make_reduction(
    regressor,
    strategy="recursive",
    window_length=12, # This creates lag features [y(t-1), ..., y(t-12)]
    scitype="tabular-regressor"
)

# Split data into train and test sets
y_train = y[y.index < "1960-01-01"]
y_test = y[y.index >= "1960-01-01"]

# Fit the forecaster
forecaster.fit(y_train)

# Make predictions
y_pred = forecaster.predict(fh)

# Evaluate
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"RMSE without tsfresh features: {rmse:.2f}")

# To see the features it created internally:
X_transformed, y_transformed = forecaster._get_transformed_X_y(y_train)
print("\nFeatures created by make_reduction (lags):\n", X_transformed.head())
```

## Example: Adding Features with `tsfresh`

`tsfresh` can automatically extract a large number of features. We can combine these with the lag/window features for a potentially richer feature set.

```python
from sktime.transformations.series.tsfresh import TSFreshFeatureExtractor
from sklearn.pipeline import make_pipeline

# --- Feature Engineering with tsfresh ---

# 1. Create a pipeline of transformers
# First, create lag features, then extract tsfresh features from a rolling window
# Note: This is an advanced use case. A simpler approach is to extract tsfresh features
# from the whole series and combine them with other features.
# For this example, let's use a simpler tsfresh transformer from sktime.

# TSFreshFeatureExtractor extracts features from the whole series provided.
# We can put this in a pipeline with the regressor.
tsfresh_extractor = TSFreshFeatureExtractor(
    default_fc_parameters="MinimalFCParameters", # Use a minimal set for speed
    disable_progressbar=True,
    show_warnings=False
)

# Create a new forecaster that uses tsfresh features in addition to lags
# This requires a more manual pipeline setup.
# Let's demonstrate a simpler workflow: extract features, then train.

from tsfresh import extract_features
from tsfresh.utilities.dataframe_functions import make_forecasting_frame

# Create a forecasting frame suitable for tsfresh
df_ts = y_train.to_frame(name="value")
df_ts['id'] = 'airline'
df_ts['time'] = df_ts.index

# This creates rows for each point in time we want to predict,
# with the corresponding historical data rolled out.
df_rolled, y_tsfresh = make_forecasting_frame(df_ts, kind="value", max_timeshift=12, rolling_direction=1)

# Extract tsfresh features from the rolled series
X_tsfresh = extract_features(df_rolled, column_id="id", column_sort="time", column_kind="kind", column_value="value",
                             default_fc_parameters="MinimalFCParameters", n_jobs=1)

# Align X and y (tsfresh might drop some initial rows)
X_tsfresh = X_tsfresh.loc[y_tsfresh.index]

# Train a standard sklearn regressor on these features
regressor_tsfresh = RandomForestRegressor(random_state=42)
regressor_tsfresh.fit(X_tsfresh, y_tsfresh)

# To make a real forecast, you would need to construct the feature vector for future time steps,
# which involves rolling the window forward. This demonstrates the feature creation part.
print(f"\n--- With tsfresh ---")
print(f"Shape of extracted tsfresh features for training: {X_tsfresh.shape}")
print("Example tsfresh features:\n", X_tsfresh.head())
```

> This second example shows the complexity of using `tsfresh` for a forecasting task. It excels at creating a rich feature set for time series **classification** or **regression** (where each time series is one sample), but for forecasting, it requires careful construction of the input data (`make_forecasting_frame`) to simulate the rolling window from which features are extracted for each prediction step. `sktime`'s `make_reduction` provides a more direct path for forecasting with standard regressors.

---