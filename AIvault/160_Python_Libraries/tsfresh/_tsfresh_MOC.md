---
tags:
  - python
  - library
  - tsfresh
  - time_series
  - feature_engineering
  - feature_extraction
  - machine_learning
  - moc
  - concept
aliases:
  - tsfresh MOC
  - tsfresh Library
related:
  - "[[_Python_Libraries_MOC]]"
  - "[[140_Data-Science_AI/Time_Series_Analysis/_Time_Series_Analysis_MOC|_Time_Series_Analysis_MOC]]"
  - "[[TS_Feature_Engineering_for_ML]]"
  - "[[_Pandas_MOC]]"
  - "[[_Scikit_learn_MOC|Scikit-learn MOC]]"
  - "[[160_Python_Libraries/sktime/_sktime_MOC|sktime]]"
worksheet:
  - WS_TimeSeries_1
date_created: <% tp.file-creation_date("YYYY-MM-DD") %>
---
# tsfresh MOC  Fresh 🌿

**tsfresh (Time Series FeatuRe Extraction on basis of Scalable Hypothesis tests)** is a Python package that automatically calculates a large number of time series features. It is particularly useful for tasks like time series classification and regression, where each time series sample needs to be converted into a feature vector for a standard machine learning model.

The library also includes methods for evaluating the significance of these extracted features to help with feature selection.

## Core Philosophy & Features
-   **Automated Feature Extraction:** Extracts hundreds of features from time series, describing various characteristics like trend, seasonality, peaks, variance, and complexity.
-   **Scalability:** Built on [[_Pandas_MOC|Pandas]] and can be scaled to large datasets (e.g., using Dask).
-   **Feature Significance Testing:** Includes a feature selection mechanism based on hypothesis testing that evaluates the significance of each extracted feature for predicting the target variable.
-   **Versatility:** Can be applied to any kind of time series data, from sensor readings and stock prices to audio signals and robot trajectories.
-   **Compatibility:** Integrates well with [[_Scikit_learn_MOC|scikit-learn]] and [[160_Python_Libraries/sktime/_sktime_MOC|sktime]] pipelines.

## Key Concepts & Usage
-   [[tsfresh_Data_Format|Data Format Requirements]]
    -   Understanding the "flat" and "stacked" DataFrame formats that `tsfresh` expects.
-   [[tsfresh_Feature_Extraction|Feature Extraction]]
    -   Using `extract_features()` to generate a comprehensive feature matrix.
    -   Understanding different feature sets (`MinimalFCParameters`, `EfficientFCParameters`, `ComprehensiveFCParameters`).
-   [[tsfresh_Feature_Selection|Feature Filtering and Selection]]
    -   Using `select_features()` to filter for relevant features based on their significance to a target variable.
-   [[tsfresh_Pipelines_sklearn|Integration with scikit-learn Pipelines]]
    -   Using `tsfresh` as a feature extraction step in an ML workflow.
-   [[tsfresh_Forecasting_Usage|Usage in Forecasting]]
    -   Understanding how to adapt `tsfresh` for forecasting tasks using rolling windows.

## Typical Workflow (for Classification/Regression)
1.  **Format Data:** Prepare the time series data into the required "flat" DataFrame format (`[id, time, value1, value2, ...]`).
2.  **Extract Features:** Use `extract_features()` to generate a large number of features for each time series `id`.
3.  **Filter Features (Optional but Recommended):** Use `select_features()` with a target vector `y` to select only the most relevant features.
4.  **Train Model:** Use the resulting feature matrix to train a standard `scikit-learn` classifier or regressor.

## Notes in this tsfresh Section
```dataview
LIST
FROM "160_Python_Libraries/tsfresh"
WHERE file.folder = this.file.folder AND file.name != this.file.name AND !contains(file.name, "MOC")
SORT file.name ASC
```

---