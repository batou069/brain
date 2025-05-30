---
tags:
  - data_science
  - machine_learning
  - feature_engineering
  - pandas
  - numpy
  - concept
aliases:
  - Pandas Feature Creation
  - Deriving Features Pandas
related:
  - "[[Pandas_DataFrame]]"
  - "[[Pandas_Series]]"
  - "[[Pandas_Apply_Map_Applymap]]"
  - "[[Pandas_Datetime_Operations]]"
  - "[[Pandas_String_Methods_Advanced]]"
  - "[[Pandas_Reshaping_Methods_Advanced]]"
  - "[[NumPy]]"
  - "[[Exploratory_Data_Analysis_Workflow]]"
  - "[[Basic_Data_Preprocessing_ML]]"
worksheet:
  - WS_DS_Workflow_Concepts_1
date_created: 2025-05-30
---
# Feature Engineering with Pandas

Feature engineering is the process of using domain knowledge to create new features (variables) from existing raw data. Well-engineered features can significantly improve the performance of machine learning models. [[Pandas]], along with [[NumPy]], provides a powerful toolkit for creating these new features.

## Why is Feature Engineering Important?
- **Improves Model Performance:** Better features provide more relevant information to the model, leading to higher accuracy and better generalization.
- **Reduces Complexity:** Good features can sometimes allow simpler models to perform as well as or better than complex models on raw data.
- **Enhances Interpretability:** Meaningful features can make model predictions easier to understand.
- **Handles Data Issues:** Can help manage missing data, outliers, or transform data into a more suitable format.

## Common Feature Engineering Techniques using Pandas

[list2tab|#Feature Engineering Techniques]
- **1. Creating Features from Existing Numeric Columns**
    - **Polynomial Features:** Create interaction terms or polynomial terms (e.g., $x^2$, $x^3$, $x_1 \cdot x_2$).
      ```python
      import pandas as pd
      df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]})
      df['A_squared'] = df['A']**2
      df['A_times_B'] = df['A'] * df['B']
      print("Polynomial features:\n", df)
      ```
    - **Ratios and Differences:** Create new features by dividing or subtracting columns.
      ```python
      # df['A_div_B'] = df['A'] / (df['B'] + 1e-6) # Add small constant to avoid division by zero
      # df['B_minus_A'] = df['B'] - df['A']
      ```
    - **Binning/Discretization:** Convert continuous numerical data into discrete bins (categories). This can help capture non-linear relationships.
      ```python
      ages = pd.Series([22, 35, 67, 45, 28, 52, 80, 19])
      bins = [18, 30, 40, 50, 60, 100]
      labels = ['18-30', '31-40', '41-50', '51-60', '60+']
      df['Age_Group'] = pd.cut(ages, bins=bins, labels=labels, right=False)
      # pd.qcut can be used for quantile-based binning
      print("\nBinned ages:\n", df[['Age_Group']]) # Assuming 'ages' was a column in df or combined
      ```
    - **Transformations:** Apply mathematical transformations like log, square root, Box-Cox to stabilize variance, make data more normal, or handle skewness.
      ```python
      import numpy as np
      # df['A_log'] = np.log(df['A'] + 1e-6) # Add small constant if A can be 0
      ```

- **2. Extracting Features from Datetime Columns**
    - Using the `.dt` accessor on datetime [[Pandas_Series]]. (See [[Pandas_Datetime_Operations]])
      ```python
      df_time = pd.DataFrame({'timestamp': pd.to_datetime(['2023-01-15 10:30', '2023-03-20 18:45'])})
      df_time['year'] = df_time['timestamp'].dt.year
      df_time['month'] = df_time['timestamp'].dt.month
      df_time['dayofweek'] = df_time['timestamp'].dt.dayofweek # Monday=0, Sunday=6
      df_time['hour'] = df_time['timestamp'].dt.hour
      df_time['is_weekend'] = df_time['dayofweek'].isin([5, 6])
      print("\nDatetime features:\n", df_time)
      ```
    - **Time Since/Until an Event:** Calculate durations.
      ```python
      # current_date = pd.to_datetime('today')
      # df['days_since_event'] = (current_date - df['event_date']).dt.days
      ```
    - **Cyclical Features:** Encode cyclical time features (like month or hour) using sine/cosine transformations to preserve their cyclical nature for models.
      ```python
      # df['hour_sin'] = np.sin(2 * np.pi * df_time['hour']/24.0)
      # df['hour_cos'] = np.cos(2 * np.pi * df_time['hour']/24.0)
      ```

- **3. Deriving Features from Text Data**
    - Using `.str` accessor methods. (See [[Pandas_String_Methods_Advanced]])
    - **Length of Text:**
      ```python
      df_text = pd.DataFrame({'comment': ['This is good!', 'Awful service.', 'Okay']})
      df_text['comment_length'] = df_text['comment'].str.len()
      print("\nText length feature:\n", df_text)
      ```
    - **Word Count:**
      ```python
      # df_text['word_count'] = df_text['comment'].str.split().str.len()
      ```
    - **Presence of Keywords:**
      ```python
      # df_text['has_good'] = df_text['comment'].str.contains('good', case=False)
      ```
    - **More Advanced:** Using TF-IDF, word embeddings (often done with libraries like Scikit-learn, NLTK, spaCy, Gensim).

- **4. Creating Features from Categorical Data**
    - **One-Hot Encoding:** Convert categorical variables into dummy/indicator variables.
      ```python
      df_cat = pd.DataFrame({'Color': ['Red', 'Blue', 'Green']})
      color_dummies = pd.get_dummies(df_cat['Color'], prefix='Color') # See [[Pandas_Reshaping_Methods_Advanced]]
      df_cat = pd.concat([df_cat, color_dummies], axis=1)
      print("\nOne-hot encoded features:\n", df_cat)
      ```
    - **Label Encoding:** Assign a unique integer to each category. (Use with caution, as it implies an ordinal relationship that might not exist).
      ```python
      # df_cat['Color_Label'] = df_cat['Color'].astype('category').cat.codes
      ```
    - **Frequency Encoding:** Replace categories with their frequencies.
      ```python
      # color_freq = df_cat['Color'].value_counts(normalize=True)
      # df_cat['Color_Freq'] = df_cat['Color'].map(color_freq)
      ```
    - **Target Encoding (Mean Encoding):** Replace categories with the average target value for that category. (Powerful but prone to overfitting; requires careful validation).

- **5. Interaction Features**
    - Combine two or more features to capture interactions between them.
    - **Categorical-Categorical:** Create a new feature representing the combination.
      ```python
      # df['Color_Size_Interaction'] = df['Color'] + '_' + df['Size']
      # Then one-hot encode this new interaction feature.
      ```
    - **Numeric-Categorical:** Group by the categorical feature and compute aggregations of the numeric feature (e.g., mean `num_col` for each category in `cat_col`). This can then be mapped back.
      ```python
      # mean_val_by_cat = df.groupby('Category')['Value'].transform('mean')
      # df['Mean_Value_for_Category'] = mean_val_by_cat
      ```

- **6. Handling Missing Data with Feature Engineering**
    - **Indicator for Missingness:** Create a binary feature indicating whether a value was missing in the original column before imputation.
      ```python
      # df['Original_Col_Was_Missing'] = df['Original_Col'].isnull().astype(int)
      # df['Original_Col'].fillna(some_value, inplace=True)
      ```
    - This can sometimes provide useful information to the model if the pattern of missingness itself is predictive.

## Best Practices
- **Domain Knowledge:** Leverage understanding of the problem domain to create meaningful features.
- **Iterative Process:** Feature engineering is often iterative. Try different features and evaluate their impact on model performance.
- **Avoid Data Leakage:** When creating features (especially using target variable information like in target encoding), ensure you are using a proper validation strategy (e.g., create features based on training data only and then apply to validation/test sets).
- **Simplicity:** Start with simpler features and add complexity as needed.
- **Documentation:** Keep track of how features were created.

Feature engineering is as much an art as it is a science, and it's a critical component of building effective machine learning models. [[Exploratory_Data_Analysis_Workflow|EDA]] often provides strong clues for which features might be useful.

---