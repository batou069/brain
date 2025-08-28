---
tags:
  - python
  - sktime
  - time_series
  - forecasting
  - machine_learning
  - reduction
  - sklearn
  - concept
  - example
aliases:
  - sktime Reduction
  - Forecasting with sklearn Regressors
related:
  - "[[160_Python_Libraries/sktime/_sktime_MOC|_sktime_MOC]]"
  - "[[sktime_Forecasting]]"
  - "[[TS_Feature_Engineering_for_ML]]"
  - "[[160_Python_Libraries/Scikit_learn/_Scikit_learn_MOC|Scikit-learn]]"
worksheet:
  - WS_TimeSeries_1
date_created: 2025-08-27
---
# sktime: Forecasting via Reduction to Regression

A powerful feature of `sktime` is its ability to use any standard [[160_Python_Libraries/Scikit_learn/_Scikit_learn_MOC|scikit-learn]] regression model for time series forecasting. This is achieved through a process called **reduction**, where the time series forecasting problem is transformed into a standard supervised regression problem.

The `sktime.forecasting.compose.make_reduction` function is the primary tool for this.

## The Concept of Reduction
The core idea is to create a feature matrix `X` and a target vector `y` from the time series, which can then be used to train a standard regressor.

-   **Target `y`:** The value we want to predict at time $t$.
-   **Features `X`:** Information from the past that we use to make the prediction. This is typically:
    -   **Lagged values** of the time series (e.g., $y_{t-1}, y_{t-2}, \dots$).
    -   **Rolling window features** (e.g., mean of the last 7 values).
    -   **Date/time features** (e.g., month, day of week).
    -   Exogenous variables.

`make_reduction` automates this feature creation process.

## Forecasting Strategies for Reduction
When forecasting multiple steps into the future, the reducer needs a strategy to handle the fact that future lagged values are not yet known.

-   **`strategy="recursive"`:**
    -   A single model is trained to predict one step ahead ($y_t$ from past values).
    -   To predict $y_{t+1}$, it uses the actual past values.
    -   To predict $y_{t+2}$, it uses the *predicted* value for $y_{t+1}$ as an input feature, along with other actual past values. This process is repeated recursively.
    -   This is a common and flexible strategy.
-   **`strategy="direct"`:**
    -   A separate model is trained for each step in the forecasting horizon.
    -   To predict 1 step ahead, one model is trained. To predict 2 steps ahead, a completely different model is trained, and so on.
    -   Can be more accurate if the time series structure changes over the horizon, but is more computationally expensive as it requires training multiple models.
-   **`strategy="multioutput"`:**
    -   A single model is trained to predict the entire forecasting horizon at once.
    -   Requires a regressor that supports multi-output targets (e.g., `RandomForestRegressor`).

## Example: Using `RandomForestRegressor` for Forecasting
This example demonstrates how to wrap a `scikit-learn` `RandomForestRegressor` to forecast the airline passenger data.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sktime.datasets import load_airline
from sktime.forecasting.compose import make_reduction
from sktime.forecasting.base import ForecastingHorizon
from sktime.utils.plotting import plot_series
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_percentage_error

# 1. Load Data
y = load_airline()
y.index = y.index.to_timestamp() # Convert to Timestamp index for easier plotting

# 2. Split into training and test sets
y_train = y[y.index < "1960-01-01"]
y_test = y[y.index >= "1960-01-01"]

# 3. Define the scikit-learn regressor
# This regressor doesn't know anything about time series
regressor = RandomForestRegressor(n_estimators=100, random_state=42)

# 4. Create the sktime forecaster using make_reduction
# We'll use a recursive strategy and a window_length of 12 to create 12 lag features.
forecaster = make_reduction(
    estimator=regressor,
    strategy="recursive",
    window_length=12,
    scitype="tabular-regressor"
)

# 5. Fit the forecaster to the training data
print("Fitting RandomForest forecaster...")
forecaster.fit(y_train)
print("Fitting complete.")

# 6. Make Predictions
fh = ForecastingHorizon(y_test.index, is_relative=False)
y_pred = forecaster.predict(fh)

# 7. Visualize and Evaluate
# plot_series(y_train, y_test, y_pred, labels=["y_train", "y_test", "y_pred_RandomForest"])
# plt.title("Forecasting with RandomForest via sktime Reduction")
# plt.show()

# mape = mean_absolute_percentage_error(y_test, y_pred)
# print(f"\nMAPE on test set using RandomForest: {mape:.4f}")

# You can inspect the features the reducer created internally
# X_transformed, y_transformed = forecaster._get_transformed_X_y(y_train)
# print("\nExample of features created for the regression task (lags):")
# print(X_transformed.tail())
```

## Combining with Other `sktime` Transformers
The power of this approach is that it can be combined with other `sktime` transformers in a pipeline to create a rich feature set for the `sklearn` regressor.

```python
from sktime.forecasting.compose import TransformedTargetForecaster
from sktime.transformations.series.detrend import Deseasonalizer
from sktime.transformations.series.time_since import TimeSince
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

# Create a more complex forecaster
# 1. Deseasonalize the data
# 2. Create features (lags are created by make_reduction)
# 3. Train a RandomForestRegressor on the deseasonalized data and features
forecaster_pipeline = TransformedTargetForecaster(steps=[
    ("deseasonalizer", Deseasonalizer(model="multiplicative", sp=12)),
    ("forecaster", make_reduction(
        RandomForestRegressor(n_estimators=100, random_state=42),
        strategy="recursive",
        window_length=12
    ))
])

# Fit and predict as before
# forecaster_pipeline.fit(y_train)
# y_pred_pipeline = forecaster_pipeline.predict(fh)

# plot_series(y_test, y_pred_pipeline, labels=["y_test", "y_pred_Pipeline"])
# plt.title("Forecasting with Deseasonalized RandomForest")
# plt.show()
```

The reduction approach seamlessly bridges the gap between classical time series forecasting and modern machine learning, allowing you to leverage the power of `scikit-learn`'s rich ecosystem of regression models for forecasting tasks.

---