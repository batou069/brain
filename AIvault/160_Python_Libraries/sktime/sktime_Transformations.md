---
tags:
  - python
  - sktime
  - time_series
  - transformation
  - preprocessing
  - feature_engineering
  - concept
  - example
aliases:
  - sktime Transformers
  - Time Series Transformations sktime
related:
  - "[[160_Python_Libraries/sktime/_sktime_MOC|_sktime_MOC]]"
  - "[[sktime_Pipelines]]"
  - "[[TS_Components_Decomposition]]"
  - "[[TS_Lag_and_Differencing]]"
  - "[[TS_Feature_Engineering_for_ML]]"
worksheet:
  - WS_TimeSeries_1
date_created: 2025-08-27
---
# sktime: Time Series Transformations

`sktime` provides a rich library of transformers that are specifically designed for time series data. These transformers follow the `scikit-learn` API (`fit`, `transform`, `fit_transform`) and can be seamlessly integrated into [[sktime_Pipelines|`sktime` pipelines]].

They are used for tasks like preprocessing, feature extraction, and data conversion.

## Types of Transformers

[list2tab|#sktime Transformer Types]
- Detrending & Deseasonalizing
    -   **Purpose:** To remove trend and seasonal components from a time series, often to make it stationary or to simplify the pattern for another model to learn.
    -   **Transformers:**
        -   **`Deseasonalizer(sp, model)`**: Removes seasonality. `sp` is the seasonal period, `model` can be `"additive"` or `"multiplicative"`.
        -   **`Detrender(forecaster)`**: Removes the trend. It fits a `forecaster` (e.g., a linear regression model) to the data and returns the residuals.
    -   **Example:**
        ```python
        from sktime.datasets import load_airline
        from sktime.transformations.series.detrend import Deseasonalizer, Detrender
        from sktime.forecasting.polynomial import PolynomialTrendForecaster
        from sktime.utils.plotting import plot_series

        y = load_airline()

        # Deseasonalize the data
        deseasonalizer = Deseasonalizer(model="multiplicative", sp=12)
        y_deseasonalized = deseasonalizer.fit_transform(y)

        # Detrend the deseasonalized data
        detrender = Detrender(forecaster=PolynomialTrendForecaster(degree=1))
        y_detrended = detrender.fit_transform(y_deseasonalized)

        # plot_series(y, y_deseasonalized, y_detrended, labels=["Original", "Deseasonalized", "Detrended & Deseasonalized"])
        # plt.suptitle("Detrending and Deseasonalizing with sktime")
        # plt.show()
        ```
- Differencing & Lagging
    -   **Purpose:** To create lagged and differenced versions of the time series, which are crucial for achieving stationarity and for creating features for ML models.
    -   **Transformers:**
        -   **`Differencer(lags)`**: Applies differencing. `lags` can be an integer (e.g., `1` for first-order) or a list (e.g., `[1, 12]` for first and seasonal differencing).
        -   **`Lag(lags)`**: Creates lag features.
    -   **Example:**
        ```python
        from sktime.transformations.series.difference import Differencer
        from sktime.transformations.series.lag import Lag

        y = load_airline()

        # Apply first differencing
        y_diff1 = Differencer(lags=1).fit_transform(y)
        
        # Apply seasonal differencing (period 12)
        y_diff12 = Differencer(lags=12).fit_transform(y)

        # Create lag features (returns a DataFrame)
        # Lags 1, 2, and 12 (seasonal lag)
        lag_transformer = Lag()
        y_with_lags = lag_transformer.fit_transform(y)
        
        # print("--- Original Series (head) ---")
        # print(y.head())
        # print("\n--- Series with Lag Features (head) ---")
        # print(y_with_lags.head(15)) # Show more to see lag 12 appear
        ```
- Feature Extraction
    -   **Purpose:** To extract meaningful features from a time series, often for use in time series classification or regression.
    -   **Transformers:**
        -   **`TSFreshFeatureExtractor`**: A wrapper around the powerful [[160_Python_Libraries/tsfresh/_tsfresh_MOC|`tsfresh`]] library to extract a comprehensive set of features.
        -   **`WindowSummarizer`**: A flexible transformer for creating rolling window features (e.g., rolling mean, std dev). This is extremely useful for [[sktime_Forecasting_Reduction|reduction]].
        -   **`SummaryTransformer`**: Extracts summary statistics (mean, std, min, max) from the entire series.
    -   **Example (`WindowSummarizer`):**
        ```python
        from sktime.transformations.series.window_summarizer import WindowSummarizer
        import numpy as np

        y = load_airline()

        # Create rolling 12-month mean and std dev features
        # lag_feature specifies which lags to apply the functions to
        summarizer = WindowSummarizer(
            lag_feature={
                "mean": [], # Mean of lags 1 through 12
                "std": []  # Std dev of lags 1 through 12
            },
            target_cols=["y"] # Name of the column in the output DataFrame
        )

        y_with_rolling_features = summarizer.fit_transform(y.to_frame(name="y"))
        # print("\n--- Series with Rolling Window Features ---")
        # print(y_with_rolling_features.head(15))
        ```
- Other Useful Transformers
    -   **`BoxCoxTransformer`**: Applies a power transform to stabilize variance.
    -   **`Imputer`**: Fills missing values using various strategies (e.g., mean, median, ffill, bfill).
    -   **`FourierTransformer`**: Creates Fourier terms (sines and cosines) which can help model complex seasonality.
    -   **`OptionalPassthrough`**: A meta-transformer that allows you to switch a transformation step on or off, useful for hyperparameter tuning.

These transformers are the building blocks for creating sophisticated preprocessing and feature engineering pipelines in `sktime`, enabling both classical and machine learning approaches to time series tasks.

---