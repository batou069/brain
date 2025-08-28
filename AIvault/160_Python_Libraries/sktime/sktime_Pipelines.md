---
tags:
  - python
  - sktime
  - time_series
  - pipeline
  - composition
  - forecasting
  - concept
  - example
aliases:
  - sktime Pipelines
  - TransformedTargetForecaster
related:
  - "[[160_Python_Libraries/sktime/_sktime_MOC|_sktime_MOC]]"
  - "[[sktime_Transformations]]"
  - "[[sktime_Forecasting]]"
  - "[[Sklearn_Pipelines]]"
worksheet:
  - WS_TimeSeries_1
date_created: 2025-08-27
---
# sktime: Pipelines and Composition

`sktime` provides powerful tools for creating pipelines that chain together multiple [[sktime_Transformations|transformers]] and a final estimator (like a [[sktime_Forecasting|forecaster]] or classifier). This is a core feature that promotes modular, reproducible, and robust time series modeling workflows, inspired by [[Sklearn_Pipelines|scikit-learn's Pipeline object]].

## Why Use Pipelines?
-   **Workflow Organization:** Encapsulates all preprocessing and modeling steps into a single object.
-   **Preventing Data Leakage:** Crucial for correct model evaluation. Pipelines ensure that information from the validation or test set does not "leak" into the training process (e.g., by fitting transformers only on the training data within each cross-validation fold).
-   **Hyperparameter Tuning:** Allows for joint tuning of parameters from all steps in the pipeline (both transformers and the final estimator) using tools like `ForecastingGridSearchCV`.
-   **Reproducibility:** A single pipeline object represents the entire modeling process, making it easy to save, load, and reuse.

## Key Pipelining Tools in `sktime`

[list2tab|#sktime Pipelines]
- `TransformedTargetForecaster`
    -   **Purpose:** The primary tool for building forecasting pipelines. It chains transformers that are applied to the target series `y` before it is passed to the final forecasting model.
    -   **How it Works:**
        1.  During `fit()`, the transformers are fitted and applied to `y` in sequence.
        2.  The final forecaster is then fitted on the transformed `y`.
        3.  During `predict()`, the forecaster makes predictions on the transformed scale.
        4.  The pipeline then applies the *inverse transform* of each transformer in reverse order to return the forecasts to the original scale.
    -   **Syntax:** `TransformedTargetForecaster(steps)` where `steps` is a list of `(name, transformer)` tuples.
    -   **Example (Deseasonalize -> Detrend -> Forecast):**
        ```python
        from sktime.datasets import load_airline
        from sktime.forecasting.compose import TransformedTargetForecaster
        from sktime.transformations.series.detrend import Deseasonalizer, Detrender
        from sktime.forecasting.naive import NaiveForecaster
        from sktime.utils.plotting import plot_series

        y = load_airline()
        y_train = y[y.index < "1960-01-01"]
        y_test = y[y.index >= "1960-01-01"]

        # Create a pipeline
        forecaster_pipeline = TransformedTargetForecaster(steps=[
            ("deseasonalizer", Deseasonalizer(model="multiplicative", sp=12)),
            ("detrender", Detrender()),
            ("forecaster", NaiveForecaster(strategy="drift"))
        ])

        # Fit the entire pipeline
        # forecaster_pipeline.fit(y_train)

        # Make predictions (inverse transforms are applied automatically)
        # y_pred = forecaster_pipeline.predict(fh=list(range(1, 13)))

        # plot_series(y_train, y_test, y_pred, labels=["Train", "Test", "Prediction"])
        # plt.title("Forecasting Pipeline: Deseasonalize -> Detrend -> NaiveForecaster")
        # plt.show()
        ```
- `ForecastingPipeline`
    -   **Purpose:** A more general pipeline that can handle transformations for both the target `y` and exogenous variables `X`.
    -   **Note:** For many common cases where only the target `y` is transformed, `TransformedTargetForecaster` is often simpler and sufficient.
- `FeatureUnion` and `ColumnEnsembleTransformer`
    -   **Purpose:** To apply different transformations in parallel and combine their results.
    -   `FeatureUnion` is a general tool for parallel transformers.
    -   `ColumnEnsembleTransformer` is useful for applying different transformations to different columns in a multivariate time series.
- `make_pipeline` Utility
    -   A convenience function to create a pipeline without needing to name the steps. The steps are automatically named after their class in lowercase.
    -   **Example:**
        ```python
        from sktime.forecasting.compose import make_forecasting_pipeline
        # from sktime.transformations.series.boxcox import BoxCoxTransformer
        # from sktime.forecasting.arima import AutoARIMA

        # A pipeline that first applies a Box-Cox transform, then fits an AutoARIMA
        # pipe = make_forecasting_pipeline(
        #     BoxCoxTransformer(),
        #     AutoARIMA(sp=12, suppress_warnings=True)
        # )
        # print(pipe)
        ```

## Pipelining with [[sktime_Forecasting_Reduction|Reducers]]
Pipelines are extremely powerful when combined with reducers, allowing you to chain `sktime` time series feature transformers with a standard `scikit-learn` model.

```python
from sktime.datasets import load_airline
from sktime.forecasting.compose import make_reduction
from sktime.transformations.series.window_summarizer import WindowSummarizer
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import make_pipeline as make_sklearn_pipeline

# 1. Define the sklearn regressor and any sklearn preprocessing
# Here we create a pipeline of a WindowSummarizer and a RandomForest
# Note: This requires a more advanced setup where the sktime transformer's
# output (a DataFrame) is fed into the sklearn model.
# The `make_reduction` function is the primary "pipeline" for this use case.

# Let's show a more direct example of chaining sktime transformers before reduction.
y = load_airline()
y_train = y[y.index < "1960-01-01"]

# Create a pipeline that first creates rolling window features,
# then passes the resulting DataFrame to the reducer.
# This is more advanced and often requires custom classes or using the ` ForecastingPipeline`.

# A more common pattern is to transform the target first, then reduce.
forecaster_ml_pipeline = TransformedTargetForecaster(steps=[
    ("deseasonalizer", Deseasonalizer(model="multiplicative", sp=12)),
    ("forecaster", make_reduction(
        RandomForestRegressor(n_estimators=100, random_state=42),
        strategy="recursive",
        window_length=12
    ))
])

# This pipeline will:
# 1. Deseasonalize the training data `y_train`.
# 2. Pass the deseasonalized data to `make_reduction`.
# 3. `make_reduction` will create lag features from the deseasonalized data.
# 4. The RandomForestRegressor will be trained on these lag features.
# 5. When predicting, it forecasts the deseasonalized series, and then the
#    `TransformedTargetForecaster` re-seasonalizes the forecast.

# forecaster_ml_pipeline.fit(y_train)
# y_pred_ml = forecaster_ml_pipeline.predict(fh=list(range(1, 13)))

# plot_series(y_train, y_test, y_pred_ml, labels=["Train", "Test", "ML Pipeline Pred"])
# plt.show()
```

By using pipelines, you can build complex, robust, and reproducible time series models in `sktime` while maintaining clean and organized code.

---