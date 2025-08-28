---
tags:
  - python
  - sktime
  - time_series
  - classification
  - regression
  - panel_data
  - rocket
  - concept
  - example
aliases:
  - sktime Time Series Classification
  - sktime Time Series Regression
  - ROCKET
related:
  - "[[160_Python_Libraries/sktime/_sktime_MOC|_sktime_MOC]]"
  - "[[sktime_Data_Representation]]"
  - "[[_Scikit_learn_MOC|Scikit-learn MOC]]"
worksheet:
  - WS_TimeSeries_1
date_created: 2025-08-27
---
# sktime: Time Series Classification and Regression

Beyond forecasting, `sktime` provides a comprehensive framework for other supervised learning tasks where the **entire time series is a single data point**.

-   **Time Series Classification (TSC):** The goal is to predict a categorical target variable based on a time series input.
    -   *Example:* Classifying an ECG signal as "normal" or "arrhythmia".
    -   *Example:* Identifying the type of activity (e.g., "walking", "running", "sitting") from accelerometer sensor data.
-   **Time Series Regression (TSR):** The goal is to predict a continuous target variable based on a time series input.
    -   *Example:* Predicting the remaining useful life of a machine based on its recent sensor vibration data.
    -   *Example:* Estimating a patient's age based on their EEG signal.

## The `sktime` Approach
`sktime` uses a consistent API, similar to scikit-learn, for these tasks. The input data `X` is typically a [[sktime_Data_Representation|panel DataFrame]] where each cell contains a `pandas.Series` object, and `y` is a `numpy` array of labels.

## Key Algorithms in `sktime`

[list2tab|#sktime TSC/TSR Algorithms]
- Shapelet-based
    -   **Concept:** Shapelets are representative sub-sequences of a time series that are highly discriminative for a particular class. These models find such shapelets and use their presence or distance to classify new series.
    -   **Models:** `ShapeletTransformClassifier`.
- Dictionary-based
    -   **Concept:** Transforms a time series into a "bag of patterns" or "bag of words" representation by discretizing the series into symbolic words. Standard classifiers are then used on this representation.
    -   **Models:** `BOSSEnsemble`, `WEASEL`.
- Interval-based
    -   **Concept:** Extracts features from various random intervals of the time series.
    -   **Models:** `TimeSeriesForestClassifier` (an ensemble of decision trees built on interval features), `RandomIntervalSpectralEnsemble` (RISE).
- Distance-based
    -   **Concept:** Classifies time series based on their distance to other series in the training set, using specialized time series distance measures like Dynamic Time Warping (DTW).
    -   **Models:** `KNeighborsTimeSeriesClassifier`.
- Deep Learning
    -   **Concept:** Uses deep neural network architectures like CNNs, LSTMs, or ResNets.
    -   **Models:** `CNNClassifier`, `InceptionTimeClassifier`.
- Feature-based (ROCKET)
    -   **Concept:** A modern, highly efficient, and accurate approach. ROCKET (RandOm Convolutional KErnel Transform) generates a large number of random but diverse convolutional kernels, applies them to the time series, and extracts two features (max and proportion of positive values) per kernel. A simple linear classifier is then trained on these features.
    -   **Models:** `RocketClassifier`. Often a very strong baseline.

## Example: Time Series Classification
This example uses the `ArrowHead` dataset, where the task is to classify the shape of an arrowhead from its time series outline.

```python
import numpy as np
from sktime.datasets import load_arrow_head
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 1. Load Panel Data
X, y = load_arrow_head(return_X_y=True)
# X is a pandas DataFrame where each cell in the 'dim_0' column is a pandas Series
# y is a numpy array of class labels ('0', '1', '2')

# Split data (sktime provides its own train/test splits, but we can use sklearn too)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

print(f"Training data shape: {X_train.shape}")
print(f"Test data shape: {X_test.shape}")

# --- 2. Using a Time Series Forest Classifier ---
from sktime.classification.interval_based import TimeSeriesForestClassifier

# tsc_forest = TimeSeriesForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
# print("\nTraining TimeSeriesForestClassifier...")
# tsc_forest.fit(X_train, y_train)
# y_pred_forest = tsc_forest.predict(X_test)
# accuracy_forest = accuracy_score(y_test, y_pred_forest)
# print(f"TimeSeriesForestClassifier Accuracy: {accuracy_forest:.4f}")

# --- 3. Using the ROCKET Classifier ---
from sktime.classification.kernel_based import RocketClassifier

# ROCKET is often very fast and accurate.
# tsc_rocket = RocketClassifier(num_kernels=10000, random_state=42) # 10,000 is the default
# print("\nTraining RocketClassifier...")
# tsc_rocket.fit(X_train, y_train)
# y_pred_rocket = tsc_rocket.predict(X_test)
# accuracy_rocket = accuracy_score(y_test, y_pred_rocket)
# print(f"RocketClassifier Accuracy: {accuracy_rocket:.4f}")
```

## Using `tsfresh` for Feature-Based Classification
An alternative approach is to use a library like [[160_Python_Libraries/tsfresh/_tsfresh_MOC|`tsfresh`]] to extract a large number of features and then use a standard `scikit-learn` classifier. `sktime` provides a convenient wrapper for this.

```python
from sktime.transformations.series.tsfresh import TSFreshFeatureExtractor
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# (Using X_train, X_test, y_train, y_test from the previous example)

# Create a pipeline that first extracts features with tsfresh,
# then classifies with a RandomForest.
# "MinimalFCParameters" is a small, fast set of features.
tsfresh_pipeline = make_pipeline(
    TSFreshFeatureExtractor(default_fc_parameters="MinimalFCParameters", show_warnings=False),
    RandomForestClassifier(n_estimators=100, random_state=42)
)

# print("\nTraining pipeline with TSFresh and RandomForest...")
# tsfresh_pipeline.fit(X_train, y_train)
# y_pred_tsfresh = tsfresh_pipeline.predict(X_test)
# accuracy_tsfresh = accuracy_score(y_test, y_pred_tsfresh)
# print(f"TSFresh + RandomForest Accuracy: {accuracy_tsfresh:.4f}")

# To see the features created by tsfresh:
# feature_extractor = TSFreshFeatureExtractor(default_fc_parameters="MinimalFCParameters", show_warnings=False)
# X_train_transformed = feature_extractor.fit_transform(X_train)
# print("\nShape of tsfresh features:", X_train_transformed.shape)
# print("Example features:\n", X_train_transformed.head())
```

`sktime` provides a powerful and unified framework for tackling complex time series tasks beyond forecasting, bringing a wide range of specialized algorithms into a familiar, scikit-learn-like API.

---