---
tags:
  - python
  - sktime
  - time_series
  - model_selection
  - hyperparameter_tuning
  - cross_validation
  - gridsearch
  - concept
  - example
aliases:
  - sktime Model Selection
  - sktime Hyperparameter Tuning
  - ForecastingGridSearchCV
related:
  - "[[160_Python_Libraries/sktime/_sktime_MOC|_sktime_MOC]]"
  - "[[sktime_Forecasting]]"
  - "[[sktime_Pipelines]]"
  - "[[TS_Cross_Validation_Evaluation]]"
  - "[[Sklearn_Model_Selection|scikit-learn Model Selection]]"
worksheet:
  - WS_TimeSeries_1
date_created: <% tp.file-creation_date("YYYY-MM-DD") %>
---
# sktime: Model Selection and Hyperparameter Tuning

Selecting the best model and tuning its hyperparameters are critical steps for achieving high forecasting accuracy. `sktime` provides specialized tools for these tasks that correctly handle the temporal nature of time series data, preventing the [[TS_Look_Ahead_Bias|look-ahead bias]] that would occur with standard [[Sklearn_Model_Selection|scikit-learn cross-validation]].

## Temporal Cross-Validation Splitters
As detailed in [[TS_Cross_Validation_Evaluation]], `sktime` provides splitters that respect the temporal order of the data. These are used as the `cv` argument in tuning strategies.

-   **`SlidingWindowSplitter(window_length, fh, step_length)`**: Uses a training window of a fixed size that slides forward in time.
-   **`ExpandingWindowSplitter(initial_window, fh, step_length)`**: Uses a training window that starts at an initial size and grows with each split, always including all past data.
-   **`SingleWindowSplitter(window_length)`**: Creates just a single train/test split.

## Hyperparameter Tuning with `ForecastingGridSearchCV`
-   **Purpose:** A tool analogous to scikit-learn's `GridSearchCV` but designed specifically for `sktime` forecasters. It performs an exhaustive search over a specified parameter grid to find the best hyperparameters for a forecaster.
-   **Key Components:**
    -   **`forecaster`**: The `sktime` forecasting model or [[sktime_Pipelines|pipeline]] to be tuned.
    -   **`cv`**: A temporal cross-validation splitter (e.g., `SlidingWindowSplitter`).
    -   **`param_grid`**: A dictionary defining the hyperparameters to search.
    -   **`scoring`**: A performance metric to evaluate the forecasts (e.g., `MeanAbsolutePercentageError`).
-   **How it Works:** For each combination of parameters in the grid, `ForecastingGridSearchCV` uses the `cv` splitter to train and evaluate the forecaster multiple times on different temporal folds. It then averages the scores and identifies the parameter combination that performed best on average.

### Example: Tuning an Exponential Smoothing Model
```python
import pandas as pd
import numpy as np
from sktime.datasets import load_airline
from sktime.forecasting.exp_smoothing import ExponentialSmoothing
from sktime.forecasting.model_selection import ForecastingGridSearchCV, SlidingWindowSplitter
from sktime.performance_metrics.forecasting import MeanAbsolutePercentageError

# 1. Load Data
y = load_airline()

# 2. Define the Temporal Cross-Validation Strategy
# Use a sliding window with a 10-year (120 months) training window
# Forecast 1 year (12 months) ahead in each fold
cv_splitter = SlidingWindowSplitter(window_length=120, fh=np.arange(1, 13))

# 3. Define the Forecaster and Parameter Grid
# We will tune the 'trend', 'seasonal', and 'smoothing_level' (alpha) parameters
forecaster = ExponentialSmoothing(sp=12) # Seasonal period is fixed at 12

param_grid = {
    "trend": ["add", "mul"],
    "seasonal": ["add", "mul"],
    "smoothing_level": [0.1, 0.2, 0.3] # Alpha parameter
}

# 4. Set up and Run GridSearchCV
# Use MAPE as the scoring metric. refit=True will refit the best model on all data.
gscv = ForecastingGridSearchCV(
    forecaster=forecaster,
    cv=cv_splitter,
    param_grid=param_grid,
    scoring=MeanAbsolutePercentageError(symmetric=False),
    n_jobs=-1, # Use all available CPU cores
    refit=True
)

print("Starting GridSearchCV for ExponentialSmoothing...")
gscv.fit(y)
print("GridSearchCV complete.")

# 5. Inspect Results
print("\n--- Hyperparameter Tuning Results ---")
print(f"Best MAPE score from CV: {gscv.best_score_:.4f}")
print(f"Best parameters found: {gscv.best_params_}")

# The `gscv` object is now a fitted forecaster with the best parameters
# We can use it to make predictions
# y_pred = gscv.predict(fh=np.arange(1, 13)) # Predict the next 12 months
# print("\nForecast for the next 12 months:\n", y_pred)
```

## Model Comparison and Selection
You can use these tools to compare entirely different models.

```python
from sktime.forecasting.naive import NaiveForecaster
from sktime.forecasting.arima import AutoARIMA
from sktime.forecasting.model_evaluation import evaluate

# Define a list of forecasters to compare
forecasters_to_compare = {
    "Seasonal Naive": NaiveForecaster(strategy="seasonal_last", sp=12),
    "AutoARIMA": AutoARIMA(sp=12, suppress_warnings=True),
    "Tuned ETS": gscv.best_forecaster_ # The best model from our grid search above
}

# Use the same CV splitter for a fair comparison
cv = SlidingWindowSplitter(window_length=120, fh=np.arange(1, 13))

# The evaluate function runs the cross-validation for each forecaster
# results = []
# for name, forecaster in forecasters_to_compare.items():
#     print(f"\nEvaluating forecaster: {name}")
#     # The evaluate function is a convenient wrapper
#     cv_results = evaluate(
#         forecaster=forecaster,
#         y=y,
#         cv=cv,
#         scoring=MeanAbsolutePercentageError(symmetric=False),
#         return_data=False # We only want the scores
#     )
#     # The result contains test scores for each fold
#     mean_mape = cv_results["test_MeanAbsolutePercentageError"].mean()
#     std_mape = cv_results["test_MeanAbsolutePercentageError"].std()
#     results.append({"Model": name, "Mean MAPE": mean_mape, "Std MAPE": std_mape})
#     print(f"  Mean CV MAPE: {mean_mape:.4f} (+/- {std_mape:.4f})")

# results_df = pd.DataFrame(results)
# print("\n--- Model Comparison Summary ---")
# print(results_df.sort_values(by="Mean MAPE"))
```

## Tuning Pipelines
The `param_grid` can also access and tune parameters of transformers within a [[sktime_Pipelines|pipeline]] using the `stepname__parametername` syntax, just like in scikit-learn.

```python
from sktime.forecasting.compose import TransformedTargetForecaster
from sktime.transformations.series.detrend import Detrender
from sktime.forecasting.trend import PolynomialTrendForecaster

# Example pipeline: Detrend with a polynomial, then forecast residuals with a naive model
pipeline = TransformedTargetForecaster(steps=[
    ("detrender", Detrender(forecaster=PolynomialTrendForecaster())),
    ("forecaster", NaiveForecaster(strategy="last"))
])

# Define a grid to tune the degree of the polynomial detrender
pipeline_param_grid = {
    "detrender__forecaster__degree": # Tune the 'degree' of the PolynomialTrendForecaster
}

# Set up GridSearchCV for the pipeline
# gscv_pipeline = ForecastingGridSearchCV(
#     forecaster=pipeline,
#     cv=SlidingWindowSplitter(window_length=100),
#     param_grid=pipeline_param_grid,
#     scoring=MeanAbsolutePercentageError(symmetric=False)
# )

# gscv_pipeline.fit(y)
# print("\n--- Pipeline Tuning Results ---")
# print(f"Best pipeline parameters: {gscv_pipeline.best_params_}")
```

`sktime`'s model selection and tuning tools provide a robust and theoretically sound framework for evaluating and optimizing time series models, ensuring that temporal dependencies are respected and preventing common pitfalls like data leakage.

---