---
tags:
  - python
  - tsfresh
  - scikit_learn
  - sklearn
  - pipeline
  - machine_learning
  - feature_extraction
  - concept
  - example
aliases:
  - tsfresh sklearn Pipeline
  - Integrating tsfresh with scikit-learn
related:
  - "[[160_Python_Libraries/tsfresh/_tsfresh_MOC|_tsfresh_MOC]]"
  - "[[tsfresh_Feature_Extraction]]"
  - "[[tsfresh_Feature_Selection]]"
  - "[[_Scikit_learn_MOC|Scikit-learn MOC]]"
  - "[[Sklearn_Pipelines]]"
worksheet:
  - WS_TimeSeries_1
date_created: 2025-08-27
---
# tsfresh: Integration with scikit-learn Pipelines

`tsfresh` is designed to integrate smoothly with [[_Scikit_learn_MOC|scikit-learn]]'s `Pipeline` objects. This allows you to include the feature extraction and selection steps as part of your standard machine learning workflow, which is excellent for reproducibility, preventing data leakage, and hyperparameter tuning.

`tsfresh` provides several scikit-learn compatible transformer classes for this purpose.

## Key `tsfresh` Transformers for Pipelines

1.  **`TSFreshFeatureExtractor`:**
    -   A transformer that wraps the `extract_features()` function.
    -   In its `fit()` method, it does nothing.
    -   In its `transform()` method, it takes a DataFrame in the [[tsfresh_Data_Format|tsfresh flat format]] and returns the extracted feature matrix.
2.  **`RelevantFeatureAugmenter`:**
    -   A more advanced transformer that combines feature extraction, feature selection, and transformation into a single step.
    -   In its `fit()` method, it extracts features, uses `select_features()` to determine which ones are relevant, and stores this list of relevant features.
    -   In its `transform()` method, it extracts all features and then filters them down to only the relevant ones identified during `fit`. This is crucial for preventing data leakage, as the feature selection is learned *only* from the training data.

## Example: Using `tsfresh` in a scikit-learn Pipeline
This example demonstrates building a full pipeline for a time series classification problem, from raw data to a final prediction.

```python
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from tsfresh.transformers import TSFreshFeatureExtractor, RelevantFeatureAugmenter
from tsfresh.utilities.dataframe_functions import format_time_series_for_tsfresh

# --- 1. Create Sample Data ---
# Using the same data generation as the previous note
def create_ts_sample(is_faulty, n_steps=50):
    time = range(n_steps)
    if is_faulty:
        temp = 25 + np.arange(n_steps) * 0.1 + np.random.randn(n_steps) * 0.5
    else:
        temp = 25 + np.random.randn(n_steps) * 0.2
    return pd.DataFrame({'time': time, 'temperature': temp})

n_series = 50
all_dfs = []
y_list = []
for i in range(n_series):
    is_faulty_flag = i % 2 == 0
    df = create_ts_sample(is_faulty_flag)
    df['id'] = f'machine_{i}'
    all_dfs.append(df)
    y_list.append(is_faulty_flag)

timeseries_df = pd.concat(all_dfs)
y_target = pd.Series(y_list, index=[f'machine_{i}' for i in range(n_series)])

# Split the IDs for training and testing
y_train, y_test = train_test_split(y_target, test_size=0.3, random_state=42, stratify=y_target)
X_train_flat = timeseries_df[timeseries_df['id'].isin(y_train.index)]
X_test_flat = timeseries_df[timeseries_df['id'].isin(y_test.index)]

# --- 2. Build a Pipeline with RelevantFeatureAugmenter ---
# This is the most robust approach.
# It will extract, select, and transform features all in one go.
# We need to tell it which columns to use.
pipeline_with_selection = Pipeline([
    ('augmenter', RelevantFeatureAugmenter(
        column_id='id',
        column_sort='time',
        # We can specify which features to calculate to speed things up
        # default_fc_parameters=EfficientFCParameters()
    )),
    ('classifier', RandomForestClassifier(random_state=42))
])

# 3. Fit the pipeline on the training data
# The augmenter needs both X and y in its fit method to perform selection
# print("--- Fitting Pipeline with Feature Selection ---")
# pipeline_with_selection.fit(X_train_flat, y_train)

# 4. Make predictions on the test data
# y_pred = pipeline_with_selection.predict(X_test_flat)

# 5. Evaluate
# print("\n--- Classification Report (Pipeline with Selection) ---")
# print(classification_report(y_test, y_pred))

# --- Alternative: Pipeline with TSFreshFeatureExtractor (no selection) ---
# This pipeline extracts all features and then trains the classifier.
# pipeline_no_selection = Pipeline([
#     ('extractor', TSFreshFeatureExtractor(
#         column_id='id',
#         column_sort='time',
#         # Using a smaller feature set for this example
#         default_fc_parameters=MinimalFCParameters()
#     )),
#     ('classifier', RandomForestClassifier(random_state=42))
# ])

# print("\n\n--- Fitting Pipeline without Feature Selection ---")
# pipeline_no_selection.fit(X_train_flat, y_train)
# y_pred_no_sel = pipeline_no_selection.predict(X_test_flat)
# print("\n--- Classification Report (Pipeline without Selection) ---")
# print(classification_report(y_test, y_pred_no_sel))
```

## Advantages of Using Pipelines with `tsfresh`
-   **Prevents Data Leakage:** Feature selection is a form of "learning" from the data. By putting `RelevantFeatureAugmenter` in a pipeline, you ensure that the selection of important features is learned *only* from the training set during `fit()`. When `transform` is called on the test set, it only uses the features that were selected based on the training data, which is the correct and robust way to evaluate the model.
-   **Reproducibility and Simplicity:** The entire workflow, from raw time series to a trained model, is encapsulated in a single scikit-learn `Pipeline` object. This makes it easy to save, load, and reuse the entire process.
-   **Hyperparameter Tuning:** You can use scikit-learn's `GridSearchCV` or `RandomizedSearchCV` to tune not only the parameters of your final classifier but also the parameters of the `tsfresh` transformers (e.g., which feature set to use).
    ```python
    # from sklearn.model_selection import GridSearchCV
    # param_grid = {
    #     'augmenter__fdr_level': [0.05, 0.01], # Tune the feature selection threshold
    #     'classifier__n_estimators': # Tune the classifier
    # }
    # grid_search = GridSearchCV(pipeline_with_selection, param_grid, cv=3)
    # grid_search.fit(timeseries_df, y_target) # Fit on the full dataset for CV
    # print("\nBest params from GridSearchCV:", grid_search.best_params_)
    ```

Integrating `tsfresh` into scikit-learn pipelines is the recommended best practice for building robust and scalable machine learning models for time series classification and regression tasks.

---