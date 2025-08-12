---
tags:
  - data_science
  - machine_learning
  - preprocessing
  - scaling
  - normalization
  - encoding
  - pandas
  - scikit_learn
  - concept
aliases:
  - ML Data Preprocessing
  - Scaling Data
  - Normalizing Data
  - Encoding Categorical Data
related:
  - "[[Pandas_DataFrame]]"
  - "[[NumPy_ndarray]]"
  - "[[Feature_Engineering_Pandas]]"
  - "[[Exploratory_Data_Analysis_Workflow]]"
  - "[[Scikit-learn]]"
  - "[[Pandas_Reshaping_Methods_Advanced]]"
worksheet:
  - WS_DS_Workflow_Concepts_1
date_created: 2025-05-30
---
# Basic Data Preprocessing for Machine Learning

Data preprocessing is a critical step in the machine learning pipeline that involves transforming raw data into a clean and suitable format for modeling. Machine learning algorithms often have specific requirements for input data, such as numerical features, no missing values, and features on a similar scale. This note covers some basic but essential preprocessing techniques.

## Why is Preprocessing Necessary?
- **Improve Model Performance:** Algorithms can learn more effectively from well-prepared data.
- **Meet Algorithm Requirements:** Many algorithms (e.g., SVMs, k-NN, neural networks, gradient descent based) are sensitive to feature scales or require numerical input.
- **Handle Data Issues:** Address problems like missing data, inconsistent formatting, or irrelevant features.
- **Reduce Noise:** Clean data can lead to more robust and generalizable models.

## Common Preprocessing Steps

[list2tab|#Preprocessing Techniques]
- **1. Handling Missing Data**
    - **Recap:** As covered in [[Exploratory_Data_Analysis_Workflow|EDA]] and [[Pandas_Handling_Missing_Data]], this involves strategies like:
        - **Imputation:** Filling missing values (e.g., with mean, median, mode, or more sophisticated methods like k-NN imputation or model-based imputation).
        - **Deletion:** Removing rows or columns with missing values (use with caution to avoid losing too much data).
    - **Tools:** [[Pandas]] (`.fillna()`, `.dropna()`), [[Scikit-learn]] (`SimpleImputer`, `KNNImputer`).

- **2. Scaling and Normalization (for Numerical Features)**
    - **Purpose:** Transform numerical features to be on a similar scale. This is important for algorithms that are sensitive to feature magnitudes, such as:
        - Distance-based algorithms (k-NN, SVM, K-Means).
        - Algorithms using gradient descent (Linear Regression, Logistic Regression, Neural Networks).
    - **Common Techniques:**
        - **Min-Max Scaling (Normalization):**
            - **Formula:** $X_{scaled} = \frac{X - X_{min}}{X_{max} - X_{min}}$
            - **Range:** Rescales features to a fixed range, typically.
            - **Pros:** Preserves the shape of the original distribution. Good when you need bounded values.
            - **Cons:** Sensitive to outliers (outliers can squash the majority of data into a small part of the range).
            - **Tools:** [[Scikit-learn]] `MinMaxScaler`, or manually with [[Pandas]]/[[NumPy]].
              ```python
              # Using Pandas/NumPy (manual)
              # df['col_scaled'] = (df['col'] - df['col'].min()) / (df['col'].max() - df['col'].min())
              
              # Using Scikit-learn
              # from sklearn.preprocessing import MinMaxScaler
              # scaler = MinMaxScaler()
              # df['col_scaled_sklearn'] = scaler.fit_transform(df[['col']]) 
              ```
        - **Standardization (Z-score Normalization):**
            - **Formula:** $X_{scaled} = \frac{X - \mu}{\sigma}$ (where $\mu$ is mean, $\sigma$ is standard deviation)
            - **Range:** Rescales features to have zero mean and unit variance. Not bounded to a specific range.
            - **Pros:** Less affected by outliers compared to Min-Max scaling. Often preferred for algorithms that assume data is normally distributed (though it doesn't make data normal).
            - **Cons:** Does not produce values in a bounded range.
            - **Tools:** [[Scikit-learn]] `StandardScaler`, or manually with [[Pandas]]/[[NumPy]].
              ```python
              # Using Pandas/NumPy (manual)
              # df['col_standardized'] = (df['col'] - df['col'].mean()) / df['col'].std()

              # Using Scikit-learn
              # from sklearn.preprocessing import StandardScaler
              # scaler = StandardScaler()
              # df['col_standardized_sklearn'] = scaler.fit_transform(df[['col']])
              ```
        - **Robust Scaling:**
            - **Purpose:** Uses statistics that are robust to outliers (e.g., median and Interquartile Range - IQR).
            - **Formula:** $X_{scaled} = \frac{X - median}{IQR}$
            - **Pros:** Handles outliers better than Min-Max or Standardization.
            - **Tools:** [[Scikit-learn]] `RobustScaler`.
    - >[!warning] **Data Leakage with Scaling:** Always fit scalers (e.g., `MinMaxScaler`, `StandardScaler`) on the *training data only* and then use the *fitted* scaler to transform both the training and test/validation data. Fitting on the entire dataset before splitting can lead to data leakage.

- **3. Encoding Categorical Variables**
    - **Purpose:** Convert categorical features (text labels) into a numerical format that machine learning algorithms can understand.
    - **Common Techniques:**
        - **One-Hot Encoding:**
            - **Process:** Creates new binary (0 or 1) columns for each category. Each column indicates the presence (1) or absence (0) of a category.
            - **Pros:** No ordinal relationship is implied. Suitable for nominal categorical data.
            - **Cons:** Can lead to high dimensionality if the categorical variable has many unique categories (curse of dimensionality).
            - **Tools:** [[Pandas]] `pd.get_dummies()` (see [[Pandas_Reshaping_Methods_Advanced]]), [[Scikit-learn]] `OneHotEncoder`.
              ```python
              # Using Pandas
              # df_encoded = pd.get_dummies(df, columns=['categorical_col'], drop_first=True) 
              # drop_first=True helps avoid multicollinearity
              ```
        - **Label Encoding:**
            - **Process:** Assigns a unique integer to each category (e.g., Red=0, Green=1, Blue=2).
            - **Pros:** Simple, doesn't increase dimensionality.
            - **Cons:** Introduces an artificial ordinal relationship (e.g., implies Blue > Green > Red), which might mislead algorithms that interpret magnitudes (like linear models or tree-based models in some cases if not handled carefully). Generally suitable for ordinal categorical data or for target variables in classification. For tree-based models (like Decision Trees, Random Forests), label encoding is often acceptable for features.
            - **Tools:** [[Scikit-learn]] `LabelEncoder`.
              ```python
              # from sklearn.preprocessing import LabelEncoder
              # le = LabelEncoder()
              # df['categorical_col_encoded'] = le.fit_transform(df['categorical_col'])
              ```
        - **Other methods:** Ordinal Encoding (for explicitly ordinal data), Target Encoding, Frequency Encoding (see [[Feature_Engineering_Pandas]]).
    - >[!tip] For nominal categorical features (no inherent order), One-Hot Encoding is generally preferred for most algorithms. For tree-based models, Label Encoding can sometimes work well and be more memory-efficient.

- **4. Feature Selection (Brief Mention)**
    - **Purpose:** Select a subset of relevant features to use in model construction.
    - **Benefits:** Can improve model performance (by removing noise/irrelevant features), reduce overfitting, speed up training, and improve interpretability.
    - **Techniques:** Filter methods (e.g., correlation, chi-squared), Wrapper methods (e.g., recursive feature elimination), Embedded methods (e.g., L1 regularization). (This is a large topic, often covered in more detail separately).

## Preprocessing Pipeline
It's common practice, especially when using [[Scikit-learn]], to build a preprocessing pipeline (e.g., using `sklearn.pipeline.Pipeline` and `sklearn.compose.ColumnTransformer`). This allows you to:
- Apply different transformations to different columns.
- Encapsulate all preprocessing steps.
- Prevent data leakage by ensuring steps are fitted correctly on training data and applied to test data.

## General Workflow
1.  **Split Data:** Divide your dataset into training and testing (and possibly validation) sets *before* any preprocessing that learns from the data (like fitting scalers or encoders).
2.  **Fit on Training Data:** Fit all preprocessing transformers (scalers, encoders, imputers) *only* on the training data.
3.  **Transform All Sets:** Apply the *fitted* transformers to transform the training data, validation data, and test data.

Proper data preprocessing is a foundational skill in machine learning, directly impacting the success of your models.

---