---
tags:
  - python
  - scikit_learn
  - sklearn
  - machine_learning
  - preprocessing
  - scaling
  - encoding
  - imputation
  - concept
  - example
aliases:
  - Scikit-learn Preprocessing
  - Feature Scaling sklearn
  - Categorical Encoding sklearn
related:
  - "[[160_Python_Libraries/Scikit_learn/_Scikit_learn_MOC|_Scikit_learn_MOC]]"
  - "[[Basic_Data_Preprocessing_ML]]"
  - "[[_Pandas_MOC]]"
worksheet:
  - WS_ML_Libraries_1
date_created: 2025-06-09
---
# Scikit-learn: Data Preprocessing (`sklearn.preprocessing`)

Data preprocessing is a crucial step in the machine learning pipeline. Scikit-learn's `sklearn.preprocessing` module provides a rich set of tools for transforming raw feature data into a format that is more suitable for machine learning algorithms.

## Common Preprocessing Tasks & Tools

[list2tab|#Preprocessing Tools]
- Feature Scaling
    - **Purpose:** To bring all features onto a similar scale. This is important for algorithms sensitive to feature magnitudes (e.g., SVMs, k-NN, gradient descent-based algorithms like linear regression, neural networks).
    - **Tools:**
        -   **`StandardScaler`**: Standardizes features by removing the mean and scaling to unit variance (Z-score normalization). $X_{scaled} = \frac{X - \mu}{\sigma}$.
        -   **`MinMaxScaler`**: Scales features to a given range, typically $[0, 1]$ or $[-1, 1]$. $X_{scaled} = \frac{X - X_{min}}{X_{max} - X_{min}}$.
        -   **`RobustScaler`**: Scales features using statistics that are robust to outliers (e.g., median and Interquartile Range - IQR).
        -   **`MaxAbsScaler`**: Scales each feature by its maximum absolute value. Preserves sparsity.
    - **Example (`StandardScaler`):**
        ```python
        from sklearn.preprocessing import StandardScaler
        import numpy as np
        import pandas as pd

        # Conceptual e-commerce data: product price and customer rating
        data = pd.DataFrame({
            'price': [10.0, 150.0, 55.0, 250.0, 20.0],
            'avg_rating': [4.5, 3.0, 4.8, 2.5, 4.0]
        })

        scaler = StandardScaler()
        # Fit on training data, then transform training and test data separately
        # For simplicity, fitting and transforming the same data here:
        scaled_data = scaler.fit_transform(data)
        # print("Original Data:\n", data)
        # print("\nScaled Data (StandardScaler):\n", pd.DataFrame(scaled_data, columns=data.columns))
        # Mean of scaled data will be ~0, std dev ~1
        ```
    -   **Important:** Fit scalers *only* on the training data and use the *fitted* scaler to transform both training and test/validation sets to prevent data leakage.
- Encoding Categorical Features
    - **Purpose:** Convert categorical (non-numerical) features into a numerical format that machine learning algorithms can understand.
    - **Tools:**
        -   **`OrdinalEncoder`**: Encodes categorical features as an integer array (0 to n_categories-1). Suitable for ordinal features where order matters.
        -   **`OneHotEncoder`**: Encodes categorical integer features as a one-hot numeric array (dummy variables). Creates a new binary column for each category. Suitable for nominal features.
        -   `LabelEncoder`: Encodes target labels (y) with value between 0 and n_classes-1. Generally used for target variable, not features.
    - **Example (`OneHotEncoder`):**
        ```python
        from sklearn.preprocessing import OneHotEncoder
        import pandas as pd

        # Conceptual data: product category
        data_cat = pd.DataFrame({'category': ['Electronics', 'Books', 'Clothing', 'Electronics', 'Books']})

        # sparse_output=False returns a dense array
        onehot_encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
        encoded_categories = onehot_encoder.fit_transform(data_cat[['category']])
        # feature_names = onehot_encoder.get_feature_names_out(['category'])
        # encoded_df = pd.DataFrame(encoded_categories, columns=feature_names)
        # print("Original Categories:\n", data_cat)
        # print("\nOne-Hot Encoded Categories:\n", encoded_df)
        ```
    -   Pandas `pd.get_dummies()` is often more convenient for one-hot encoding DataFrames directly.
- Imputation of Missing Values
    - **Purpose:** Handle missing values (NaNs) in the dataset.
    - **Tools:**
        -   **`SimpleImputer`**: Replaces missing values using a descriptive statistic (mean, median, most frequent) along each column, or a constant value.
        -   `KNNImputer`: Imputes missing values using the k-Nearest Neighbors approach.
        -   `IterativeImputer`: Models each feature with missing values as a function of other features and uses that estimate for imputation (multivariate imputation).
    - **Example (`SimpleImputer`):**
        ```python
        from sklearn.impute import SimpleImputer
        import numpy as np
        import pandas as pd

        # Conceptual data: product stock levels, some missing
        data_missing = pd.DataFrame({'stock_level': [100, 50, np.nan, 200, np.nan, 75]})

        # Impute with mean
        mean_imputer = SimpleImputer(strategy='mean')
        data_missing['stock_level_mean_imputed'] = mean_imputer.fit_transform(data_missing[['stock_level']])

        # Impute with a constant
        # constant_imputer = SimpleImputer(strategy='constant', fill_value=0)
        # data_missing['stock_level_zero_imputed'] = constant_imputer.fit_transform(data_missing[['stock_level']])
        # print(data_missing)
        ```
- Discretization (Binning)
    - **Purpose:** Convert continuous numerical features into discrete bins (categorical features).
    - **Tools:**
        -   **`KBinsDiscretizer`**: Bins continuous data into intervals. Strategies include 'uniform' (all bins have same width), 'quantile' (all bins have same number of samples), 'kmeans'.
    - **Example (`KBinsDiscretizer`):**
        ```python
        from sklearn.preprocessing import KBinsDiscretizer
        import numpy as np
        import pandas as pd

        # Conceptual data: customer age
        ages = pd.DataFrame({'age':})
        
        # Bin into 3 bins with uniform width
        binner_uniform = KBinsDiscretizer(n_bins=3, encode='ordinal', strategy='uniform', subsample=None) # subsample=None if scikit-learn >=1.3
        ages['age_bin_uniform'] = binner_uniform.fit_transform(ages[['age']])

        # Bin into 3 bins based on quantiles
        # binner_quantile = KBinsDiscretizer(n_bins=3, encode='ordinal', strategy='quantile', subsample=None)
        # ages['age_bin_quantile'] = binner_quantile.fit_transform(ages[['age']])
        # print(ages)
        # print("\nBin edges (uniform):", binner_uniform.bin_edges_)
        ```
- Polynomial Features
    - **Purpose:** Generate polynomial and interaction features. Can help model non-linear relationships.
    - **Tool:** **`PolynomialFeatures`**
    - **Example:**
        ```python
        from sklearn.preprocessing import PolynomialFeatures
        import numpy as np
        X = np.arange(6).reshape(3, 2) # Sample data: [,,]
        poly = PolynomialFeatures(degree=2, include_bias=False) # include_bias=False to skip the column of 1s
        poly_features = poly.fit_transform(X)
        # If X = [x1, x2], degree=2 features are [x1, x2, x1^2, x1*x2, x2^2]
        # print("Original X:\n", X)
        # print("Polynomial Features (degree 2):\n", poly_features)
        # print("Feature names:", poly.get_feature_names_out(['x1', 'x2']))
        ```
- Custom Transformers
    - **Purpose:** Apply user-defined functions as transformers in a Scikit-learn pipeline.
    - **Tool:** **`FunctionTransformer`**
    - **Example (applying log transform):**
        ```python
        from sklearn.preprocessing import FunctionTransformer
        import numpy as np
        # Log transform (add 1 to handle zeros if necessary)
        log_transformer = FunctionTransformer(lambda x: np.log1p(x), validate=True)
        data_to_log = np.array([,])
        log_transformed_data = log_transformer.transform(data_to_log)
        # print("Original data:\n", data_to_log)
        # print("Log-transformed data (log1p):\n", log_transformed_data)
        ```

## Best Practices
-   **Fit on Training Data Only:** Always fit transformers (scalers, encoders, imputers) on the training dataset and then use the *fitted* transformer to `transform` both the training and the test/validation datasets. This prevents data leakage from the test set into the training process.
-   **Pipelines:** Use [[Sklearn_Pipelines|`sklearn.pipeline.Pipeline`]] to chain preprocessing steps and a model together. This simplifies the workflow and helps prevent data leakage.
-   **`ColumnTransformer`:** Use `sklearn.compose.ColumnTransformer` to apply different preprocessing steps to different columns of your dataset (e.g., scale numerical columns, one-hot encode categorical columns).

Effective preprocessing is often one of the most critical factors in building successful machine learning models.

---