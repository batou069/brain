---
tags:
  - python
  - scikit_learn
  - sklearn
  - machine_learning
  - pipeline
  - workflow
  - preprocessing
  - model_selection
  - concept
  - example
aliases:
  - Scikit-learn Pipelines
  - sklearn.pipeline.Pipeline
  - ColumnTransformer
related:
  - "[[160_Python_Libraries/Scikit_learn/_Scikit_learn_MOC|_Scikit_learn_MOC]]"
  - "[[Sklearn_Preprocessing]]"
  - "[[Sklearn_Model_Selection]]"
  - "[[Sklearn_Dimensionality_Reduction]]"
worksheet:
  - WS_ML_Libraries_1
date_created: 2025-06-09
---
# Scikit-learn: Pipelines (`sklearn.pipeline`)

Pipelines in Scikit-learn are a powerful tool for chaining multiple data processing steps (transformers) and a final estimator (model) into a single object. This simplifies workflows, helps prevent data leakage, and makes it easier to deploy models.

## `Pipeline` Object
-   **Purpose:** Sequentially apply a list of transformers and a final estimator. Intermediate steps of the pipeline must be 'transforms' (i.e., must have `fit` and `transform` methods), and the final estimator only needs to implement `fit`.
-   **Syntax:** `Pipeline(steps)` where `steps` is a list of (name, transform) tuples.
-   **Benefits:**
    1.  **Convenience and Encapsulation:** Combines multiple steps into one.
    2.  **Joint Parameter Selection:** Allows grid searching over parameters of all steps in the pipeline simultaneously (e.g., using `GridSearchCV`).
    3.  **Preventing Data Leakage:** Ensures that transformations (like scaling or imputation) learned from the training data are correctly applied to validation/test data during cross-validation or prediction, without fitting these transformers on the test data.
    4.  **Reproducibility:** Makes the entire workflow more reproducible.

## `ColumnTransformer` Object (`sklearn.compose.ColumnTransformer`)
-   **Purpose:** Applies different transformers to different columns of an array or Pandas DataFrame. This is extremely useful when your dataset has features of different types (e.g., numerical and categorical) that require different preprocessing.
-   **Syntax:** `ColumnTransformer(transformers, remainder='drop')` where `transformers` is a list of (name, transformer, columns) tuples.
    -   `columns` can be a list of column names (for DataFrames), column indices, a boolean mask, or a callable.
    -   `remainder`: `{'drop', 'passthrough'}` or an estimator. What to do with columns not specified in `transformers`.
        -   `'drop'`: (Default) Drops the remaining columns.
        -   `'passthrough'`: Keeps the remaining columns unchanged.

## Example: Combining Preprocessing and Modeling

Let's create a pipeline for an e-commerce scenario: predicting whether a customer will purchase a product based on their age (numerical), region (categorical), and browsing time (numerical).

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Conceptual customer interaction data
np.random.seed(42)
data = {
    'age': np.random.randint(18, 65, 200),
    'region': np.random.choice(['North', 'South', 'East', 'West', np.nan], 200), # Categorical with NaNs
    'browsing_time_min': np.random.uniform(1, 120, 200),
    'purchased': np.random.randint(0, 2, 200) # Target variable
}
data['browsing_time_min'] = np.where(np.random.rand(200) < 0.1, np.nan, data['browsing_time_min']) # Add NaNs to numerical
df = pd.DataFrame(data)

X = df.drop('purchased', axis=1)
y = df['purchased']

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Define preprocessing for numerical features
# 1. Impute missing values with the median
# 2. Scale features
numerical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

# Define preprocessing for categorical features
# 1. Impute missing values with a constant (e.g., 'Missing')
# 2. One-hot encode
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='Missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False)) # sparse_output for dense array
])

# Identify numerical and categorical columns
numerical_cols = X.select_dtypes(include=np.number).columns.tolist()
categorical_cols = X.select_dtypes(include='object').columns.tolist()

# Create a preprocessor object using ColumnTransformer
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_cols),
        ('cat', categorical_transformer, categorical_cols)
    ],
    remainder='passthrough' # Keep any other columns (if any)
)

# Create the full pipeline with a classifier
# full_pipeline = Pipeline(steps=[
#     ('preprocessor', preprocessor),
#     ('classifier', LogisticRegression(solver='liblinear', random_state=42))
# ])

# Fit the pipeline
# full_pipeline.fit(X_train, y_train)

# Make predictions
# y_pred = full_pipeline.predict(X_test)
# accuracy = accuracy_score(y_test, y_pred)
# print(f"Pipeline Accuracy: {accuracy:.4f}")

# Hyperparameter tuning with the pipeline
# param_grid_pipeline = {
#     'preprocessor__num__imputer__strategy': ['mean', 'median'], # Accessing nested parameters
#     'classifier__C': [0.1, 1.0, 10.0],
#     'classifier__penalty': ['l1', 'l2']
# }

# grid_search_pipeline = GridSearchCV(full_pipeline, param_grid_pipeline, cv=3, scoring='accuracy', n_jobs=-1)
# grid_search_pipeline.fit(X_train, y_train)

# print("\nBest parameters for pipeline:", grid_search_pipeline.best_params_)
# print(f"Best CV accuracy for pipeline: {grid_search_pipeline.best_score_:.4f}")

# best_pipeline_model = grid_search_pipeline.best_estimator_
# y_pred_best = best_pipeline_model.predict(X_test)
# best_accuracy = accuracy_score(y_test, y_pred_best)
# print(f"Test accuracy with best pipeline: {best_accuracy:.4f}")
```

## Key Advantages Illustrated by Example
-   **Workflow Simplification:** The entire sequence of imputation, scaling, encoding, and model training is encapsulated in `full_pipeline`.
-   **Correct Cross-Validation:** When `full_pipeline` is used with `GridSearchCV` or `cross_val_score`, the preprocessing steps (imputation, scaling) are fitted *only* on the training portion of each CV fold, and then applied to the validation/test portion of that fold. This correctly prevents data leakage.
-   **Parameter Tuning Across Steps:** `GridSearchCV` can tune hyperparameters of both the preprocessor steps (e.g., `preprocessor__num__imputer__strategy`) and the final classifier (e.g., `classifier__C`) simultaneously. Parameter names in the grid are `stepname__parametername`.

Pipelines are a best practice in Scikit-learn for building robust and maintainable machine learning workflows.

---