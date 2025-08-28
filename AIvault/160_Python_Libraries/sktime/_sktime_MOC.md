---
tags:
  - python
  - library
  - sktime
  - time_series
  - forecasting
  - classification
  - machine_learning
  - moc
  - concept
aliases:
  - sktime MOC
  - sktime Library
related:
  - "[[_Python_Libraries_MOC]]"
  - "[[140_Data_Science_AI/Time_Series_Analysis/_Time_Series_Analysis_MOC|_Time_Series_Analysis_MOC]]"
  - "[[_Scikit_learn_MOC|Scikit-learn MOC]]"
  - "[[_Pandas_MOC]]"
  - "[[160_Python_Libraries/Statsmodels_Library|Statsmodels Library]]"
worksheet:
  - WS_TimeSeries_1
date_created: 2025-08-27
---
# sktime MOC 🕰️🔧

**sktime** is a comprehensive, open-source Python library for time series analysis, with a strong focus on providing a unified interface for various time series tasks. It is designed to be compatible with [[_Scikit_learn_MOC|scikit-learn]] and follows its API design principles (e.g., `fit`, `predict`, `transform`).

sktime aims to be a "scikit-learn for time series," providing a versatile toolkit for forecasting, time series classification, time series regression, and time series clustering.

## Core Philosophy & Features
-   **Unified API:** Provides a consistent API for different algorithms and tasks, making it easy to switch between models.
-   **Scikit-learn Compatibility:** Follows the familiar `fit`/`predict`/`transform` paradigm and is compatible with scikit-learn pipelines and model selection tools.
-   **Comprehensive Time Series Tasks:**
    -   **Forecasting:** Predicting future values of a time series.
    -   **Time Series Classification:** Assigning a class label to an entire time series.
    -   **Time Series Regression:** Predicting a continuous output for an entire time series.
    -   **Time Series Clustering:** Grouping similar time series together.
-   **Rich Model Zoo:** Includes wrappers for many classical forecasting models (from `statsmodels`, `pmdarima`, `Prophet`) and implementations of numerous modern, specialized time series algorithms (e.g., for classification).
-   **Pipelining and Composition:** Allows for building complex workflows by chaining transformers and forecasters/classifiers.
-   **Specialized Tools:** Provides dedicated tools for time series specific tasks like temporal cross-validation, feature extraction, and transformations.

## Key Concepts & Usage
-   [[sktime_Data_Representation|Data Representation in sktime]]
    -   Working with `pandas` Series and DataFrames with time-based indices.
-   [[sktime_Forecasting|Forecasting with sktime]]
    -   The `Forecaster` API (`fit`, `predict`, `update`).
    -   Using classical models (ARIMA, Exponential Smoothing) and machine learning models.
    -   [[sktime_Forecasting_Reduction|Forecasting via Reduction to Regression]].
    -   Evaluating forecasts.
-   [[sktime_Transformations|Time Series Transformations]]
    -   Detrending, deseasonalizing, differencing, feature extraction.
    -   Using transformers like `Deseasonalizer`, `Detrender`, `Lag`.
-   [[sktime_Pipelines|Pipelines in sktime]]
    -   Chaining transformations and estimators (e.g., `TransformedTargetForecaster`).
-   [[sktime_Model_Selection_Tuning|Model Selection and Tuning]]
    -   Using temporal cross-validation splitters (`SlidingWindowSplitter`, `ExpandingWindowSplitter`).
    -   Hyperparameter tuning with `ForecastingGridSearchCV`.
-   [[sktime_Classification_Regression|Time Series Classification and Regression]]
    -   Using classifiers/regressors that work on time series data.
    -   Algorithms like `ROCKET`, `TimeSeriesForestClassifier`.

## Notes in this sktime Section
```dataview
LIST
FROM "160_Python_Libraries/sktime"
WHERE file.folder = this.file.folder AND file.name != this.file.name AND !contains(file.name, "MOC")
SORT file.name ASC
```

---