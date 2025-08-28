---
tags:
  - python
  - tsfresh
  - time_series
  - feature_extraction
  - machine_learning
  - concept
  - example
aliases:
  - tsfresh extract_features
  - Time Series Feature Extraction
related:
  - "[[160_Python_Libraries/tsfresh/_tsfresh_MOC|_tsfresh_MOC]]"
  - "[[tsfresh_Data_Format]]"
  - "[[tsfresh_Feature_Selection]]"
worksheet:
  - WS_TimeSeries_1
date_created: 2025-08-27
---
# tsfresh: Feature Extraction

The core functionality of `tsfresh` is automated feature extraction. The `extract_features()` function takes a time series in the required [[tsfresh_Data_Format|flat DataFrame format]] and computes a comprehensive set of features for each time series instance (`id`).

## The `extract_features()` Function
-   **Purpose:** Calculates a DataFrame of features from a time series.
-   **Syntax:**
    ```python
    from tsfresh import extract_features
    
    # extracted_features = extract_features(
    #     timeseries_container,
    #     column_id=None,
    #     column_sort=None,
    #     column_kind=None, # For multivariate
    #     column_value=None, # For univariate
    #     default_fc_parameters=None, # Settings for which features to calculate
    #     kind_to_fc_parameters=None, # Settings per kind of value
    #     n_jobs=1 # Number of parallel jobs
    # )
    ```
-   **Output:** A `pandas.DataFrame` where:
    -   The **index** consists of the unique IDs from the input `column_id`.
    -   The **columns** are the extracted features. The column names are descriptive, often in the format `"value_column__feature_name__parameters"`.

## Feature Calculation Settings
You can control which features are calculated using the `default_fc_parameters` or `kind_to_fc_parameters` arguments. `tsfresh` provides several pre-configured settings:

-   **`ComprehensiveFCParameters()`**: Extracts all available features (over 750). Can be computationally expensive.
-   **`EfficientFCParameters()`**: A smaller, curated set of features that are computationally efficient to calculate and have shown to be useful in many cases.
-   **`MinimalFCParameters()`**: A very small, basic set of features (e.g., min, max, mean, median, std, sum, length). Very fast.
-   **Custom Dictionary:** You can provide your own dictionary to specify exactly which features and parameters to use.

## Example: Extracting Features from Sensor Data
Let's use the conceptual machine sensor data from the [[tsfresh_Data_Format]] note.

```python
import pandas as pd
from tsfresh import extract_features
from tsfresh.feature_extraction import MinimalFCParameters, EfficientFCParameters

# Create a sample flat DataFrame
data = {
    'machine_id': ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B'],
    'timestamp':,
    'temperature': [25.1, 25.3, 25.2, 25.5, 30.2, 30.1, 30.4, 30.3],
    'pressure': [101.2, 101.3, 101.2, 101.4, 98.5, 98.6, 98.5, 98.4]
}
flat_df = pd.DataFrame(data)

# --- 1. Extracting a Minimal Set of Features ---
# tsfresh will extract features for both 'temperature' and 'pressure' columns
# minimal_features = extract_features(
#     flat_df,
#     column_id="machine_id",
#     column_sort="timestamp",
#     default_fc_parameters=MinimalFCParameters(),
#     n_jobs=1 # Set to 0 for all cores, 1 to avoid issues in some environments
# )

# print("--- Minimal Extracted Features ---")
# print(minimal_features)

# --- 2. Extracting an Efficient Set of Features ---
# This will generate many more columns
# efficient_features = extract_features(
#     flat_df,
#     column_id="machine_id",
#     column_sort="timestamp",
#     default_fc_parameters=EfficientFCParameters(),
#     n_jobs=1
# )

# print("\n--- Efficient Extracted Features (first 5 columns) ---")
# print(efficient_features.iloc[:, :5])
# print(f"Total efficient features extracted: {efficient_features.shape}")

# --- 3. Extracting Features for a Single Value Column ---
# If you only want features for 'temperature', you can specify column_value
# temp_features = extract_features(
#     flat_df,
#     column_id="machine_id",
#     column_sort="timestamp",
#     column_value="temperature", # Specify the value column
#     default_fc_parameters=MinimalFCParameters(),
#     n_jobs=1
# )
# print("\n--- Minimal Features for Temperature Only ---")
# print(temp_features)

# --- 4. Using a Custom Feature Dictionary ---
# custom_settings = {
#     "mean": None, # No parameters for mean
#     "quantile": [{"q": 0.25}, {"q": 0.75}], # Calculate 25th and 75th percentiles
#     "cwt_coefficients": [{"widths": (2, 5, 10), "coeff": 8, "w": 5}] # A more complex feature
# }

# # We need to specify which columns get which features using kind_to_fc_parameters
# # First, we need a 'kind' column. Let's reshape our data.
# flat_df_melted = flat_df.melt(id_vars=["machine_id", "timestamp"], var_name="kind", value_name="value")
# print("\n--- Melted DataFrame for kind_to_fc_parameters ---")
# print(flat_df_melted)

# custom_features = extract_features(
#     flat_df_melted,
#     column_id="machine_id",
#     column_sort="timestamp",
#     column_kind="kind",
#     column_value="value",
#     kind_to_fc_parameters={
#         "temperature": MinimalFCParameters(), # Minimal features for temperature
#         "pressure": custom_settings # Custom features for pressure
#     },
#     n_jobs=1
# )
# print("\n--- Custom Extracted Features ---")
# print(custom_features)
```

## Use in a Machine Learning Workflow
The output of `extract_features` is a standard feature matrix where each row corresponds to a time series instance (`id`). This DataFrame can be directly used as the input `X` for a `scikit-learn` model.

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Assume 'efficient_features' is our X and 'y_target' is our y from the previous note
# X = efficient_features
# y = pd.Series(, index=['A', 'B']) # Target from previous note

# Align X and y (important if some IDs have no target)
# X, y = X.align(y, join='inner', axis=0)

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42, stratify=y)

# classifier = RandomForestClassifier(random_state=42)
# classifier.fit(X_train, y_train)

# y_pred = classifier.predict(X_test)
# print("\n--- Classification Report using tsfresh features ---")
# print(classification_report(y_test, y_pred))
```

`extract_features` automates the time-consuming process of manual feature engineering for time series, allowing data scientists to quickly generate a rich set of potentially predictive features for their models. The next step is often to use [[tsfresh_Feature_Selection|feature selection]] to reduce this large feature set to only the most relevant ones.

---