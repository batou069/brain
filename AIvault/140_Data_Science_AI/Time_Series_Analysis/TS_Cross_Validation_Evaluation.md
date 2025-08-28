---
tags:
  - time_series
  - cross_validation
  - evaluation
  - model_selection
  - backtesting
  - look_ahead_bias
  - concept
  - sktime
  - sklearn
aliases:
  - Time Series Cross-Validation
  - Backtesting
  - Forward Chaining
  - Rolling Forecast Origin
related:
  - "[[140_Data_Science_AI/Time_Series_Analysis/_Time_Series_Analysis_MOC|_Time_Series_Analysis_MOC]]"
  - "[[Sklearn_Model_Selection|Standard Cross-Validation]]"
  - "[[TS_Look_Ahead_Bias]]"
worksheet:
  - WS_TimeSeries_1
date_created: 2025-08-27
---
# Cross-Validation and Evaluation for Time Series

Evaluating forecasting models requires a different approach to cross-validation than standard machine learning problems. The temporal dependence of time series data means that random shuffling of data is not appropriate, as it would destroy the time structure.

>[!question]- Why can't you use standard k-fold cross-validation for time series data, and what is the correct approach?
>
>**Why Standard K-Fold Fails:**
>Standard k-fold cross-validation randomly shuffles the data and splits it into $k$ folds. In each iteration, one fold is used for testing, and the remaining $k-1$ folds are used for training. This process violates the fundamental principle of time series data: **temporal order**.
>
>1.  **Data Leakage / [[TS_Look_Ahead_Bias|Look-ahead Bias]]:** By shuffling the data, the model would be trained on data points from the future to predict values in the past. For example, a training set might contain data from 2023, while the corresponding test set contains data from 2022. This is unrealistic and leads to overly optimistic performance estimates, as the model has "seen the future."
>2.  **Destruction of Temporal Dependencies:** Shuffling breaks the autocorrelation structure and trends that time series models are designed to learn. The model cannot learn patterns like "what happened yesterday influences today" if the data is not in chronological order.
>
>**The Correct Approach: Forward Chaining / Rolling Forecast Origin**
>The correct approach for time series cross-validation involves creating splits that respect the temporal order. The training set must always contain observations that occurred *before* the observations in the validation/test set. This process is often called **backtesting**, **forward chaining**, or **evaluation on a rolling forecasting origin**.
>
>There are two main schemes:
>1.  **Sliding Window (or Rolling Forecast Origin):** A training window of a fixed size slides forward in time.
>2.  **Expanding Window:** The training window starts small and grows, always including all past data.

## Time Series Cross-Validation Strategies

[list2tab|#TS CV Strategies]
- Sliding Window
    -   **Concept:** A training set of a fixed size `n` is used to forecast the next `h` steps (the test set). The window then slides forward by `s` steps, and the process is repeated.
    -   **Visualization:**
        ```
        Fold 1: [TRAIN_1][TEST_1]
        Fold 2:      [TRAIN_2][TEST_2]
        Fold 3:           [TRAIN_3][TEST_3]
        ```
    -   **Use Case:** Useful when older data might be less relevant, and you want the model to adapt to more recent patterns.
- Expanding Window
    -   **Concept:** The training set starts with an initial size and expands with each new fold, always including all data from the beginning of the series up to the start of the test set.
    -   **Visualization:**
        ```
        Fold 1: [TRAIN_1][TEST_1]
        Fold 2: [---TRAIN_2---][TEST_2]
        Fold 3: [------TRAIN_3------][TEST_3]
        ```
    -   **Use Case:** Suitable when all historical data is considered relevant for making future predictions.

## Python Example with `sktime` and `scikit-learn`
`sktime` provides specialized cross-validation splitters that are easy to use. `scikit-learn` also has `TimeSeriesSplit`.

```python
import numpy as np
import pandas as pd
from sktime.datasets import load_airline
from sktime.forecasting.model_selection import ExpandingWindowSplitter, SlidingWindowSplitter
from sktime.forecasting.naive import NaiveForecaster
from sktime.performance_metrics.forecasting import MeanAbsolutePercentageError
from sklearn.model_selection import TimeSeriesSplit

# Load data
y = load_airline()

# --- 1. sktime: Expanding Window Cross-Validation ---
# Create a splitter for an expanding window
# initial_window=72 (6 years), step_length=12 (evaluate yearly), fh=12 (forecast 1 year ahead)
cv_expanding = ExpandingWindowSplitter(initial_window=72, step_length=12, fh=np.arange(1, 13))
n_splits_expanding = cv_expanding.get_n_splits(y)
print(f"Number of splits for ExpandingWindowSplitter: {n_splits_expanding}")

# Loop through the splits
print("\n--- Expanding Window Splits (sktime) ---")
for i, (train_indices, test_indices) in enumerate(cv_expanding.split(y)):
    print(f"Fold {i+1}:")
    print(f"  Train indices: {train_indices.min()}-{train_indices.max()} (size: {len(train_indices)})")
    print(f"  Test indices: {test_indices.min()}-{test_indices.max()} (size: {len(test_indices)})")

# --- 2. sktime: Sliding Window Cross-Validation ---
# Create a splitter for a sliding window
window_length=72 (6 years), step_length=12, fh=12
cv_sliding = SlidingWindowSplitter(window_length=72, step_length=12, fh=np.arange(1, 13))
n_splits_sliding = cv_sliding.get_n_splits(y)
print(f"\nNumber of splits for SlidingWindowSplitter: {n_splits_sliding}")

# Loop through the splits
print("\n--- Sliding Window Splits (sktime) ---")
for i, (train_indices, test_indices) in enumerate(cv_sliding.split(y)):
    print(f"Fold {i+1}:")
    print(f"  Train indices: {train_indices.min()}-{train_indices.max()} (size: {len(train_indices)})")
    print(f"  Test indices: {test_indices.min()}-{test_indices.max()} (size: {len(test_indices)})")

# --- 3. scikit-learn: TimeSeriesSplit ---
# This is a simpler version, often used for ML models.
# It creates splits like (fold1_train), (fold1_train, fold2_train), etc.
tscv = TimeSeriesSplit(n_splits=5)
print("\n--- TimeSeriesSplit Splits (sklearn) ---")
for i, (train_index, test_index) in enumerate(tscv.split(y)):
    print(f"Fold {i+1}:")
    print(f"  TRAIN: indices {train_index.min()} to {train_index.max()}")
    print(f"  TEST:  indices {test_index.min()} to {test_index.max()}")

# --- Putting it together: Evaluating a forecaster with CV ---
forecaster = NaiveForecaster(strategy="seasonal_last", sp=12)
loss = MeanAbsolutePercentageError()
cv_scores = []
for train_indices, test_indices in cv_expanding.split(y):
    y_train = y.iloc[train_indices]
    y_test = y.iloc[test_indices]
    fh_cv = ForecastingHorizon(y_test.index, is_relative=False)
  
    forecaster.fit(y_train)
    y_pred = forecaster.predict(fh_cv)
  
    error = loss(y_test, y_pred)
    cv_scores.append(error)

print(f"\nCV MAPE Scores for Naive Forecaster: {np.round(cv_scores, 4)}")
print(f"Mean CV MAPE: {np.mean(cv_scores):.4f}")
```

By using these temporal cross-validation strategies, you can get a much more realistic and reliable estimate of your forecasting model's performance on unseen future data.

---