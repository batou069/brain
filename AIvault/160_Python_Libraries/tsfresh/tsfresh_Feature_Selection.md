---
tags:
  - python
  - tsfresh
  - time_series
  - feature_selection
  - machine_learning
  - hypothesis_testing
  - concept
  - example
aliases:
  - tsfresh select_features
  - Time Series Feature Selection
related:
  - "[[160_Python_Libraries/tsfresh/_tsfresh_MOC|_tsfresh_MOC]]"
  - "[[tsfresh_Feature_Extraction]]"
  - "[[Hypothesis_Testing]]"
worksheet:
  - WS_TimeSeries_1
date_created: 2025-08-27
---
# tsfresh: Feature Filtering and Selection

After using [[tsfresh_Feature_Extraction|`extract_features()`]] to generate a large number of features, many of these features may be irrelevant or redundant for predicting a specific target variable. Using all of them can lead to [[Overfitting_Underfitting|overfitting]], increased model complexity, and longer training times.

`tsfresh` provides a built-in feature selection procedure based on statistical hypothesis testing to filter this large feature set down to only the most significant ones.

## The `select_features()` Function
-   **Purpose:** Evaluates the significance of each feature in the input feature matrix `X` with respect to a target vector `y`. It returns a new DataFrame containing only the relevant features.
-   **How it Works:** For each feature column, `tsfresh` performs a series of hypothesis tests to check if there is a statistically significant relationship between that feature and the target variable. It then uses a Benjamini-Yekutieli procedure to control the false discovery rate and decides which features to keep.
    -   For binary/categorical targets, it uses tests like the Wilcoxon rank-sum test.
    -   For continuous targets, it uses tests like the Kendall rank correlation test.
-   **Syntax:**
    ```python
    from tsfresh import select_features
    
    # X_filtered = select_features(X, y, fdr_level=0.05)
    ```
-   **Parameters:**
    -   `X`: The feature matrix DataFrame produced by `extract_features()`. The index must correspond to the time series IDs.
    -   `y`: The target `pandas.Series`. The index must match the index of `X`.
    -   `fdr_level` (False Discovery Rate): The p-value threshold for the hypothesis tests, corrected for multiple testing. Default is 0.05. Features with a p-value below this level are considered significant and are kept.

## Example: Selecting Features for Machine Classification
Let's continue the example from the previous notes, where we extracted features from machine sensor data and have a target indicating if a machine is faulty.

```python
import pandas as pd
from tsfresh import extract_features, select_features
from tsfresh.feature_extraction import ComprehensiveFCParameters
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# --- 1. Create Sample Data ---
# Create a more complex dataset to make feature selection meaningful
def create_ts_sample(is_faulty, n_steps=100):
    time = range(n_steps)
    if is_faulty:
        # Faulty machines have a slight upward trend and higher noise
        temp = 25 + np.arange(n_steps) * 0.05 + np.random.randn(n_steps) * 0.5
        pressure = 101 - np.arange(n_steps) * 0.02 + np.random.randn(n_steps) * 0.8
    else:
        # Normal machines are stable
        temp = 25 + np.random.randn(n_steps) * 0.2
        pressure = 101 + np.random.randn(n_steps) * 0.3
    return pd.DataFrame({'time': time, 'temperature': temp, 'pressure': pressure})

n_series = 20
all_dfs = []
y_list = []
for i in range(n_series):
    is_faulty_flag = i % 2 == 0 # Alternate between faulty and normal
    df = create_ts_sample(is_faulty_flag)
    df['id'] = f'machine_{i}'
    all_dfs.append(df)
    y_list.append(is_faulty_flag)

timeseries_df = pd.concat(all_dfs)
y_target = pd.Series(y_list, index=[f'machine_{i}' for i in range(n_series)])

# --- 2. Extract a Comprehensive Set of Features ---
# This will create a very wide DataFrame with many features
# extracted_features = extract_features(
#     timeseries_df,
#     column_id="id",
#     column_sort="time",
#     default_fc_parameters=ComprehensiveFCParameters(),
#     n_jobs=1
# )
# print(f"Shape of original extracted features: {extracted_features.shape}")

# --- 3. Select Significant Features ---
# Ensure target is aligned with features
# y_target_aligned = y_target.loc[extracted_features.index]

# selected_features = select_features(extracted_features, y_target_aligned)
# print(f"Shape after feature selection: {selected_features.shape}")
# print("\nSome of the selected features:")
# print(selected_features.columns.tolist()[:10])

# --- 4. Compare ML Model Performance ---
# X_train_full, X_test_full, y_train, y_test = train_test_split(extracted_features, y_target_aligned, test_size=0.3, random_state=42)
# X_train_sel, X_test_sel, _, _ = train_test_split(selected_features, y_target_aligned, test_size=0.3, random_state=42)

# # Model with all features
# clf_full = RandomForestClassifier(random_state=42)
# clf_full.fit(X_train_full, y_train)
# y_pred_full = clf_full.predict(X_test_full)
# accuracy_full = accuracy_score(y_test, y_pred_full)
# print(f"\nAccuracy with ALL features: {accuracy_full:.4f}")

# # Model with selected features
# clf_selected = RandomForestClassifier(random_state=42)
# clf_selected.fit(X_train_sel, y_train)
# y_pred_sel = clf_selected.predict(X_test_sel)
# accuracy_selected = accuracy_score(y_test, y_pred_sel)
# print(f"Accuracy with SELECTED features: {accuracy_selected:.4f}")
```
> **Expected Outcome:** The model trained on the selected features will often have comparable or even better performance than the model trained on all features. This is because removing irrelevant and noisy features can help the model generalize better and avoid overfitting, while also being much faster to train.

## Advantages of `select_features()`
-   **Reduces Overfitting:** By removing features that are not significantly related to the target, it helps the model focus on the real signal and generalize better to unseen data.
-   **Improves Model Performance:** Can lead to faster training times and lower memory consumption due to the reduced number of features.
-   **Enhances Interpretability:** Working with a smaller set of significant features can make it easier to understand what drives the model's predictions.
-   **Automated and Statistically Grounded:** Provides a systematic and statistically sound way to perform feature selection, removing the need for manual trial and error.

The combination of `extract_features()` and `select_features()` provides a powerful, automated workflow for building machine learning models on time series data.

---