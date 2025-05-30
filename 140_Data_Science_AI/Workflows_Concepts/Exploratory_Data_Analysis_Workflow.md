---
tags:
  - data_science
  - workflow
  - eda
  - pandas
  - numpy
  - matplotlib
  - data_visualization
  - concept
aliases:
  - EDA Steps
  - Data Exploration Workflow
related:
  - "[[Pandas]]"
  - "[[NumPy]]"
  - "[[Matplotlib]]"
  - "[[Seaborn]]"
  - "[[Pandas_Data_Loading_IO]]"
  - "[[Pandas_Data_Inspection]]"
  - "[[Pandas_Handling_Missing_Data]]"
  - "[[Pandas_Descriptive_Statistics_Methods]]"
  - "[[140_Data_Science_AI/Pandas/Pandas_Plotting]]"
  - "[[Data_Visualization_for_EDA]]"
  - "[[Feature_Engineering_Pandas]]"
worksheet:
  - WS_DS_Workflow_Concepts_1
date_created: 2025-05-30
---
# Exploratory Data Analysis (EDA) Workflow

Exploratory Data Analysis (EDA) is a crucial initial step in any data science project. Its primary goal is to understand the data, identify patterns, spot anomalies, test hypotheses, and check assumptions with the help of summary statistics and graphical representations. A thorough EDA can guide feature engineering, model selection, and overall project direction.

## Core Objectives of EDA
- **Understand Data Structure:** Dimensions, data types, identify key variables.
- **Data Quality Assessment:** Identify missing values, outliers, duplicates, inconsistencies.
- **Summarize Data:** Calculate descriptive statistics (mean, median, mode, variance, etc.).
- **Discover Relationships:** Explore correlations and associations between variables.
- **Generate Hypotheses:** Formulate initial ideas about the data that can be tested later.
- **Inform Feature Engineering:** Identify potential new features or transformations.

## Typical EDA Steps

While the exact steps can vary based on the dataset and project goals, a general EDA workflow often includes:

[list2card|addClass(ab-col1)|#EDA Workflow Steps]
- **1. Data Loading & Initial Inspection**
    - **Action:** Load the dataset (e.g., using [[Pandas_Data_Loading_IO]] like `pd.read_csv()`, `pd.read_excel()`, `pd.read_sql()`).
    - **Tools:** [[Pandas]]
    - **Inspection:**
        - `df.head()`, `df.tail()`: View first/last few rows.
        - `df.shape`: Get dimensions (rows, columns).
        - `df.info()`: Get a concise summary including data types, non-null counts, and memory usage.
        - `df.dtypes`: Check data types of each column.
        - `df.describe(include='all')`: Generate descriptive statistics. `include='all'` provides stats for both numeric and categorical columns. (See [[Pandas_sum_min_max_describe]], [[Pandas_Descriptive_Statistics_Methods]])
- **2. Data Cleaning**
    - **Action:** Address data quality issues identified in the inspection phase.
    - **Tools:** [[Pandas]], [[NumPy]]
    - **Sub-steps:**
        - **Handling Missing Values:**
            - `df.isnull().sum()`: Count missing values per column.
            - Visualization: Heatmaps of missing data (e.g., using `seaborn.heatmap(df.isnull())`).
            - Strategies: Imputation (mean, median, mode, model-based), Deletion (rows or columns). (See [[Pandas_Handling_Missing_Data]], [[Pandas_Representing_Missing_Values]])
        - **Handling Duplicates:**
            - `df.duplicated().sum()`: Count duplicate rows.
            - `df.drop_duplicates(inplace=True)`: Remove duplicate rows.
        - **Handling Outliers:**
            - Visualization: Box plots, scatter plots.
            - Statistical methods: Z-score, IQR (Interquartile Range).
            - Strategies: Capping, transformation, removal (with caution).
        - **Correcting Data Types:** Ensure columns have appropriate data types (e.g., converting object to numeric or datetime using `pd.to_numeric()`, `[[Pandas_Datetime_Operations#pd.to_datetime()|pd.to_datetime()]]`).
        - **Standardizing/Normalizing Text:** (If applicable) e.g., converting to lowercase, removing extra spaces using [[Pandas_String_Methods_Advanced]].
- **3. Univariate Analysis**
    - **Action:** Analyze individual variables one by one to understand their distributions.
    - **Tools:** [[Pandas]], [[Matplotlib]], [[Seaborn]]
    - **Numeric Variables:**
        - Histograms (`df['col'].hist()`, `plt.hist()`, `sns.histplot()`): Understand distribution shape (skewness, modality).
        - Density Plots (`df['col'].plot(kind='density')`, `sns.kdeplot()`): Smoothed version of histogram.
        - Box Plots (`df.boxplot(column='col')`, `plt.boxplot()`, `sns.boxplot()`): Identify median, quartiles, outliers.
    - **Categorical Variables:**
        - Frequency Tables / Bar Charts (`df['col'].value_counts()`, `df['col'].value_counts().plot(kind='bar')`, `sns.countplot()`): Show frequency of each category.
        - Pie Charts (use with caution, better for few categories): `df['col'].value_counts().plot(kind='pie')`.
- **4. Bivariate/Multivariate Analysis**
    - **Action:** Explore relationships between two or more variables.
    - **Tools:** [[Pandas]], [[Matplotlib]], [[Seaborn]]
    - **Numeric vs. Numeric:**
        - Scatter Plots (`df.plot(kind='scatter', x='col1', y='col2')`, `plt.scatter()`, `sns.scatterplot()`): Visualize relationship, identify patterns (linear, non-linear), clusters.
        - Correlation Matrix (`df.corr()`, `sns.heatmap(df.corr(), annot=True)`): Quantify linear relationships. (See [[Pandas_Descriptive_Statistics_Methods#df.corr()|df.corr()]])
    - **Categorical vs. Numeric:**
        - Box Plots per category (`sns.boxplot(x='cat_col', y='num_col', data=df)`).
        - Violin Plots (`sns.violinplot(x='cat_col', y='num_col', data=df)`).
        - Bar plots of mean/median per category (`df.groupby('cat_col')['num_col'].mean().plot(kind='bar')`).
    - **Categorical vs. Categorical:**
        - Contingency Tables / Crosstabs (`pd.crosstab(df['cat_col1'], df['cat_col2'])`).
        - Stacked/Grouped Bar Charts (`pd.crosstab(...).plot(kind='bar', stacked=True)`).
        - Heatmaps of crosstabs.
    - **Multivariate (more than two variables):**
        - Scatter plots with color/size encoding for a third variable (`sns.scatterplot(x='col1', y='col2', hue='cat_col3', size='num_col4', data=df)`).
        - Pair Plots (`sns.pairplot(df)`): Grid of scatter plots for all pairs of numeric variables, and histograms/density plots on the diagonal. Can also include categorical variables using `hue`.
        - 3D Plots (use sparingly, can be hard to interpret). (See [[Matplotlib_3D_Plotting]])
- **5. Deriving Insights & Feature Engineering (Initial Thoughts)**
    - **Action:** Based on the analyses, document key observations, patterns, and anomalies. Start thinking about potential new features that could be created from existing ones.
    - **Tools:** Domain knowledge, critical thinking.
    - Examples:
        - "Sales are highest in Q4."
        - "Users from region X have significantly higher engagement."
        - "Variable A and Variable B are highly correlated, suggesting multicollinearity if both are used in a linear model."
        - "Consider creating a 'day_of_week' feature from the timestamp." (See [[Feature_Engineering_Pandas]])
- **6. Documentation & Reporting**
    - **Action:** Document all findings, visualizations, and cleaning steps. This is often done in a Jupyter Notebook or a dedicated report.
    - **Importance:** Ensures reproducibility, helps communicate findings to stakeholders, and serves as a reference for future steps.

## Iterative Process
EDA is not strictly linear. You might revisit earlier steps as you uncover new insights. For example, discovering an outlier in bivariate analysis might lead you back to data cleaning.

## Visualization
Effective [[Data_Visualization_for_EDA|data visualization]] is a cornerstone of EDA. [[Matplotlib]] provides fine-grained control, while [[Seaborn]] offers high-level interfaces for creating informative and attractive statistical graphics. [[140_Data_Science_AI/Pandas/Pandas_Plotting]] provides convenient wrappers around Matplotlib.

---