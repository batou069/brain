---
tags:
---
---
# Exploratory Data Analysis (EDA) Summary 

## Keywords 

*   **Objectives:** The primary goal of EDA is to understand the main characteristics of a dataset. It involves summarizing data, often with visual methods, to uncover patterns, spot anomalies, test hypotheses, and check assumptions. EDA helps in identifying errors, understanding relationships between variables, and ensuring the validity of results. 

*   **Variable descriptions:** This involves understanding each variable in the dataset, including its meaning and data type (e.g., numerical, categorical). This initial step provides a clearer picture of the data you are working with. 

*   **Target variable:** Also known as the dependent or response variable, this is the outcome you aim to predict or explain. It's the variable of primary interest in a study and can be either continuous or categorical. 

*   **Data understanding:** This is the process of getting to know your data. It involves generating questions to guide your investigation and using tools like visualization and transformation to find answers. 

*   **Missing values:** These are data points that are not stored for a variable. Handling them is a critical step in data cleaning and can significantly impact the results of an analysis. 

*   **Duplicated values:** These are identical rows in a dataset. Removing them is important as they can distort statistical summaries and lead to incorrect insights. 

*   **Outliers:** These are data points that are significantly different from other observations in a dataset. They can be caused by errors or represent genuine, albeit unusual, data. 

*   **Data visualization:** This is a key component of EDA, allowing for the visual exploration of data to identify trends, outliers, and relationships between variables. Common visualizations include histograms, box plots, scatter plots, and heatmaps. 

*   **Univariate, bivariate and multivariate analysis:** These are different levels of data analysis based on the number of variables being examined. 
    *   **Univariate analysis** focuses on a single variable to describe its distribution. 
    *   **Bivariate analysis** examines the relationship between two variables. 
    *   **Multivariate analysis** investigates the relationships between more than two variables simultaneously. 

## Questions 

1.  **What can you do about missing values?** 
    *   **Deletion:** Rows or columns with missing values can be removed. 
    *   **Imputation:** Missing values can be replaced with a calculated value like the mean, median, or mode of the column. 
    *   **Advanced Imputation:** More complex methods like K-Nearest Neighbors (KNN) or machine learning models can be used to predict and fill in missing values. 
    *   **Create a new category:** For categorical variables, "missing" can be treated as a new category. 

2.  **Why is it important to know the type of each variable?** 
    *   **Appropriate Analysis:** The type of variable (e.g., categorical, numerical) determines which statistical methods and visualizations are appropriate. 
    *   **Data Cleaning:** Knowing the variable type helps in identifying impossible or incorrect values (e.g., text in a numeric field). 
    *   **Feature Engineering:** Understanding variable types is crucial for creating new features that can improve model performance. 

3.  **What are the different techniques to detect and neutralize outliers?** 
    *   **Detection:** 
        *   **Visualization:** Box plots, scatter plots, and histograms can visually reveal outliers. 
        *   **Statistical Methods:** The Z-score (measures how many standard deviations a data point is from the mean) and the Interquartile Range (IQR) method are common statistical techniques. 
    *   **Neutralization:** 
        *   **Trimming/Removal:** Outliers can be removed from the dataset. 
        *   **Capping/Winsorization:** Outliers are replaced with the nearest "non-outlier" value. 
        *   **Imputation:** Outliers can be treated as missing values and imputed. 
        *   **Transformation:** Applying a mathematical transformation (e.g., logarithm) to the variable can reduce the effect of outliers. 

4.  **How can you identify useless variables?** 
    *   **High Percentage of Missing Values:** Variables with a large proportion of missing data may not be useful. 
    *   **Low Variance:** Variables that have the same or nearly the same value for all observations offer little information. 
    *   **Irrelevance to the Target Variable:** If a variable shows no relationship or correlation with the target variable, it may be a candidate for removal. 
    *   **High Correlation with Other Variables (Multicollinearity):** If two explanatory variables are highly correlated, one of them might be redundant. 

5.  **What do you need to know about a categorical variable?** 
    *   **Frequency Distribution:** The number of occurrences of each category. 
    *   **Number of Unique Categories:** How many different categories exist. 
    *   **Mode:** The most frequent category. 
    *   **Visualizations:** Bar charts and pie charts are effective for visualizing the distribution of categorical variables. 

6.  **What do you need to know about a quantitative variable?** 
    *   **Measures of Central Tendency:** Mean, median, and mode to understand the center of the distribution. 
    *   **Measures of Spread:** Standard deviation, variance, and interquartile range to understand the variability of the data. 
    *   **Distribution Shape:** Whether the data is symmetric (like a normal distribution), skewed, or has multiple peaks. 
    *   **Visualizations:** Histograms, box plots, and density plots are used to visualize the distribution. 

7.  **Why is it important to understand the relationship between explanatory variables?** 
    *   **Avoid Multicollinearity:** High correlation between explanatory variables (multicollinearity) can make it difficult to determine the individual effect of each variable on the target variable in a model. 
    *   **Better Model Interpretation:** Understanding these relationships helps in building more interpretable and reliable models. 
    *   **Feature Selection:** It can help in selecting a better subset of features for a model, potentially improving its performance. 

8.  **What are the main things to look for in an EDA?** 
    *   **Data Quality:** Check for missing values, duplicates, and outliers. 
    *   **Data Structure:** Understand the variables and their types. 
    *   **Variable Distributions:** Analyze the distribution of each variable individually (univariate analysis). 
    *   **Relationships between Variables:** Explore the relationships between pairs of variables (bivariate analysis) and among multiple variables (multivariate analysis). 
    *   **Patterns and Trends:** Look for interesting patterns, trends, or anomalies in the data. 

## Checklist

8.1 **Create a checklist to rationalize your workflow.** 

*   [ ] **1. Data Collection & Initial Inspection:** 
    * [ ] Load the data.
    *   [ ] Get a first look at the data (e.g., using `.head()`, `.info()`, `.describe()` in pandas). 
    *   [ ] Understand the meaning of each variable. 

*   [ ] **2. Data Cleaning:** 
    *   [ ] **Missing Values:** 
        *   [ ] Identify columns with missing values. 
        *   [ ] Decide on a strategy to handle them (e.g., remove, impute). 
    *   [ ] **Duplicate Values:** 
        *   [ ] Check for and remove duplicate rows. 
    *   [ ] **Outliers:** 
        *   [ ] Detect outliers using visual and statistical methods. 
            * exp_total T
            * exp_de T
            * age
            * salary_no_extras
            * yearly_bonus+stocks T
            * vacation_days T
            * 
        *   [ ] Decide on a strategy to handle them (e.g., remove, cap, transform). 

*   [ ] **3. Univariate Analysis:** 
    *   [ ] For each **quantitative** variable, analyze: 
        *   [ ] Central tendency (mean, median). 
        *   [ ] Spread (standard deviation, IQR). 
        *   [ ] Distribution (histogram, box plot). 
    *   [ ] For each **categorical** variable, analyze: 
        *   [ ] Frequency of each category (frequency table). 
        *   [ ] Visualize with a bar chart. 
        * Do:
            * lower and strip:
                * seniority_lvl
                * city
                * position
                * tech_main
                * tech_other
            - company_type:
                - remap
            * remove:
                * gender: 
                    * diverse
                * status_employment: 
                    * working student
                    * full-time position, part-time position, & self-employed (freelancing, tutoring)
                    * intern
                    * full-time, but 32 hours per week (it was my request, i'm a student)
                    * werkstudent

*   [ ] **4. Bivariate and Multivariate Analysis:** 
    *   [ ] **Quantitative vs. Quantitative:** 
        *   [ ] Create scatter plots to visualize relationships. 
        *   [ ] Calculate correlation coefficients. 
    *   [ ] **Categorical vs. Quantitative:** 
        *   [ ] Use side-by-side box plots or violin plots. 
    *   [ ] **Categorical vs. Categorical:** 
        *   [ ] Create a contingency table (crosstab). 
        *   [ ] Use a stacked or grouped bar chart. 
    *   [ ] **Multivariate:** 
        *   [ ] Use heatmaps to visualize correlations between multiple variables. 
        *   [ ] Consider pair plots to see relationships across several variables at once. 

*   [ ] **5. Summarize and Document:** 
    *   [ ] Document all findings and insights. 
    *   [ ] Formulate hypotheses for further analysis or modeling. 
    *   [ ] Identify any remaining data quality issues. 

## Example Code Snippets:

*   **Python (pandas & numpy):** 
    ```python
    import pandas as pd
    import numpy as np

    # Load data
    df = pd.read_csv('your_data.csv')

    # Initial inspection
    print(df.info())
    print(df.describe())

    # Missing values
    print(df.isnull().sum())
    # Fill missing values with the mean
    df['column_name'].fillna(df['column_name'].mean(), inplace=True)

    # Duplicated values
    print(df.duplicated().sum())
    df.drop_duplicates(inplace=True)
    ```

---

# Data Preprocessing

## **Keywords**

*   **Standardization**
    *   Rescales data to have a mean of 0 and a standard deviation of 1.
    *   It assumes the data follows a Gaussian (normal) distribution.
    *   The formula is: `z = (x - mean) / standard_deviation`.
    *   It is less affected by outliers than normalization.
    *   **Pandas Example:**
        ```python
        import pandas as pd
        data = {'col1': [10, 20, 30, 40, 50]}
        df = pd.DataFrame(data)
        df['standardized'] = (df['col1'] - df['col1'].mean()) / df['col1'].std()
        print(df)
        ```

*   **Normalization**
    *   Rescales the features to a fixed range, typically between 0 and 1.
    *   Also known as Min-Max scaling.
    *   The formula is: `x_normalized = (x - min) / (max - min)`.
    *   It is sensitive to outliers, as they can influence the min and max values.
    *   **Pandas Example:**
        ```python
        import pandas as pd
        data = {'col1': [10, 20, 30, 40, 50]}
        df = pd.DataFrame(data)
        df['normalized'] = (df['col1'] - df['col1'].min()) / (df['col1'].max() - df['col1'].min())
        print(df)
        ```

*   **Scaling**
    *   A general term for changing the range of feature values.
    *   Both standardization and normalization are types of scaling.
    *   The goal is to ensure that no single feature dominates a model's learning process simply because its values are larger.

*   **Outliers**
    *   Data points that are significantly different from other observations in a dataset.
    *   They can be caused by measurement errors or represent genuine, rare occurrences.
    *   Outliers can skew statistical measures and negatively impact the performance of machine learning models.

*   **Encoding**
    *   The process of converting categorical data (text labels) into a numerical format.
    *   Machine learning algorithms require numerical input, making encoding a necessary preprocessing step for categorical features.

*   **Imputation**
    *   The process of replacing missing values (NA or nulls) in a dataset with substituted values.
    *   This allows for the use of algorithms that cannot handle missing data.
    *   **Pandas Example (Mean Imputation):**
        ```python
        import pandas as pd
        import numpy as np
        data = {'col1': [10, 20, np.nan, 40, 50]}
        df = pd.DataFrame(data)
        mean_value = df['col1'].mean()
        df['col1'].fillna(mean_value, inplace=True)
        print(df)
        ```

*   **Binning**
    *   Also known as discretization, it is the process of converting continuous numerical variables into discrete categorical bins.
    *   This can help reduce the effects of minor observation errors and improve model performance.
    *   **Pandas Example:**
        ```python
        import pandas as pd
        data = {'age': [15, 22, 35, 48, 62, 75]}
        df = pd.DataFrame(data)
        bins = [0, 18, 35, 60, 100]
        labels = ['Child', 'Young Adult', 'Adult', 'Senior']
        df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels, right=False)
        print(df)
        ```

*   **Feature Engineering**
    *   The process of using domain knowledge to create new features from existing data.
    *   The goal is to enhance the predictive power of machine learning models by providing them with more relevant information.

## **Encoders**

*   **Label Encoder**
    *   Assigns a unique integer to each category in a variable.
    *   For example, `[RED, GREEN, BLUE]` might become `[2, 1, 0]`.
    *   This can inadvertently introduce an ordinal relationship where none exists, which can be problematic for some models.

*   **One-Hot Encoder**
    *   Creates new binary (0 or 1) columns for each category in the original variable.
    *   For a category like `color` with values `[RED, GREEN, BLUE]`, it would create three new columns: `is_RED`, `is_GREEN`, and `is_BLUE`.
    *   This avoids the issue of implied order found in Label Encoding.

*   **Ordinal Encoder**
    *   Converts categorical features into integer codes, similar to Label Encoder.
    *   It is specifically used when the categories have a natural, meaningful order (e.g., `[LOW, MEDIUM, HIGH]`).
    *   The integer encoding reflects this order (e.g., `[0, 1, 2]`).

*   **Target Encoder**
    *   Replaces each category with the mean of the target variable for that category.
    *   For example, if the average house price for the "urban" category is $300,000, "urban" would be replaced by 300000.
    *   This is a powerful technique but can lead to overfitting if not used carefully.

## **SKLearn's Preprocessing**

Scikit-learn's `preprocessing` module offers a wide array of tools for data transformation.

*   **Encoders (`OneHotEncoder`, `OrdinalEncoder`, `LabelEncoder`)**
    *   These are used to convert categorical features into numerical representations suitable for machine learning models. `TargetEncoder` is also available but is currently experimental.

*   **Scalers (`MaxAbsScaler`, `MinMaxScaler`, `StandardScaler`, `RobustScaler`)**
    *   `MinMaxScaler`: Normalizes data to a `[0, 1]` range.
    *   `StandardScaler`: Standardizes data to have a mean of 0 and a standard deviation of 1.
    *   `RobustScaler`: Scales data using statistics that are robust to outliers (like the median and interquartile range). It is useful when the data contains many outliers.
    *   `MaxAbsScaler`: Scales each feature by its maximum absolute value, bringing the data into a `[-1, 1]` range.

*   **Transformers (`PolynomialFeatures`, `PowerTransformer`, `QuantileTransformer`, `FunctionTransformer`)**
    *   `PolynomialFeatures`: Generates new features that are polynomial combinations of the original features, which can help capture non-linear relationships.
    *   `PowerTransformer`: Applies a power transformation (like Yeo-Johnson or Box-Cox) to make the data more Gaussian-like.
    *   `QuantileTransformer`: Transforms features to follow a uniform or normal distribution.
    *   `FunctionTransformer`: Allows you to apply a custom, user-defined function to your features (e.g., `log(x)`).

*   **Discretizers (`KBinsDiscretizer`)**
    *   `KBinsDiscretizer`: Bins continuous data into k intervals (bins). This is scikit-learn's primary tool for binning.

*   **Imputers (`SimpleImputer`, `KNNImputer`)**
    *   `SimpleImputer`: A basic imputer that can replace missing values with a constant value or using the mean, median, or mode of the column.
    *   `KNNImputer`: A more advanced imputer that fills missing values using the k-Nearest Neighbors approach.

## **Questions**

1.  **What is the difference between standardization and normalization?**
    *   **Standardization** rescales data to have a mean of 0 and a standard deviation of 1, without being bounded to a specific range.
    *   **Normalization** (specifically Min-Max scaling) rescales data to a fixed range, usually 0 to 1.

2.  **Name at least 3 simple techniques for outlier detection, and 3 strategies for how to treat them.**
    *   **Detection Techniques:**
        *   **Visual Inspection:** Using plots like box plots and scatter plots to visually identify points far from the main data cluster.
        *   **Interquartile Range (IQR):** Data points that fall below Q1 - 1.5*IQR or above Q3 + 1.5*IQR are considered outliers.
        *   **Z-Score:** Identifying data points with a Z-score greater than a certain threshold (commonly 3 or -3) as outliers.
    *   **Treatment Strategies:**
        *   **Removal:** Deleting the outlier observations from the dataset.
        *   **Transformation:** Applying a mathematical transformation (e.g., logarithm) to reduce the skewness of the data and the impact of the outlier.
        *   **Capping (Winsorization):** Replacing outlier values with the maximum and minimum "non-outlier" values.

3.  **When is median standardization preferred over mean standardization? -- Why do you need standardization?**
    *   Median-based standardization (like scikit-learn's `RobustScaler`) is preferred when the data contains significant outliers. The median is less sensitive to extreme values than the mean, providing a more robust scaling.
    *   Standardization is necessary because machine learning algorithms that use distance calculations (like K-Means, KNN, and SVM) or rely on gradient descent can be biased by features with large value ranges. Scaling ensures all features contribute more equally to the model's learning process.

4.  **What is the difference between the following two variables? `variable: WEAK, MEDIUM, STRONG` and `variable: BLUE, GREEN, YELLOW` - What implications does this have on encoding?**
    *   **Difference:** The first variable (`WEAK, MEDIUM, STRONG`) is **ordinal**, meaning its categories have a clear, intrinsic order. The second variable (`BLUE, GREEN, YELLOW`) is **nominal**, meaning its categories have no inherent order or rank.
    *   **Encoding Implications:**
        *   For the **ordinal** variable, an `OrdinalEncoder` is appropriate because it maps the categories to integers that preserve the natural order (e.g., `WEAK:0, MEDIUM:1, STRONG:2`).
        *   For the **nominal** variable, a `OneHotEncoder` is the correct choice. It creates separate binary columns for each color, avoiding the creation of a false and misleading order.

5.  **Is it possible to impute na? Is data science possible without data?**
    *   Yes, it is not only possible but also a common and crucial step in data preprocessing to impute (fill in) missing values (`na`).
    *   No, data science is fundamentally impossible without data. Data is the raw material from which insights are derived, models are trained, and conclusions are drawn.

6.  **What problems can arise from One-Hot Encoding?**
    *   **Curse of Dimensionality:** If a categorical variable has many unique categories (high cardinality), One-Hot Encoding will create a large number of new features. This can make the dataset very sparse and computationally expensive to process.
    *   **Multicollinearity:** By default, One-Hot Encoding can introduce perfect multicollinearity (e.g., if you know a sample is not `is_RED` and not `is_GREEN`, you know it must be `is_BLUE`). This can be handled by dropping one of the new columns.

7.  **Is preprocessing chosen based on the data type or the intended model?**
    *   It's based on **both**. The **data type** dictates the possible preprocessing steps (e.g., you encode categorical data, not numerical). The **intended model** influences the choice among those steps (e.g., tree-based models are less sensitive to feature scaling than distance-based models like SVM).

8.  **Why is feature engineering important? How does it help without creating new data?**
    *   Feature engineering is important because it can significantly improve a model's predictive performance by making the underlying patterns in the data more apparent to the learning algorithm.
    *   It doesn't create new raw data; instead, it **transforms existing data** to create more informative features. For example, from a `date` column, you can engineer features like `day_of_week` or `is_holiday`, which might be more predictive than the original date itself.

9.  **Feature engineering can lead to too many features, how do you know if it is worth it?**
    *   You can determine if adding new features is worthwhile through:
        *   **Model Performance:** Train the model with and without the new features and compare performance metrics (e.g., accuracy, R-squared) on a validation set.
        *   **Feature Importance:** Use techniques like permutation importance or SHAP values to see if the new features contribute significantly to the model's predictions.
        *   **Regularization:** Techniques like L1 regularization can automatically penalize and shrink the coefficients of less important features to zero, effectively performing feature selection.

10. **How do you know the right transformation for a feature?**
    *   There is no single rule; choosing the right transformation often involves a combination of:
        *   **Data Exploration:** Visualizing the distribution of the feature (e.g., with a histogram). If the data is skewed, a log or power transformation might help make it more symmetric.
        *   **Domain Knowledge:** Understanding the nature of the variable can suggest appropriate transformations.
        *   **Experimentation:** Trying different transformations and evaluating their impact on model performance is a common and effective approach.

---
