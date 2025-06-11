---
tags:
  - spark
  - pyspark
  - workflow
  - data_analysis
  - eda
  - dataframe
  - sql
  - example
aliases:
  - Spark EDA Workflow Example
  - PySpark Bank Marketing Analysis
related:
  - "[[PySpark_Overview]]"
  - "[[PySpark_SparkSession_SparkContext]]"
  - "[[PySpark_Data_Sources]]"
  - "[[PySpark_DataFrame_Operations]]"
  - "[[PySpark_SQL_Functions]]"
  - "[[170_Data_Visualization/_Data_Visualization_MOC|Data Visualization]]"
worksheet:
  - WS_Spark_1
date_created: 2025-06-11
---
# PySpark Workflow: Bank Marketing Dataset Analysis (Conceptual Example)

This note outlines a conceptual workflow for analyzing a dataset like the "Bank Marketing" dataset using PySpark, addressing typical tasks from Exercise 2. This involves loading data, basic inspection, descriptive statistics, and answering analytical questions.

**Assumed Dataset:** A "Bank Marketing" dataset, typically available from UCI Machine Learning Repository or Kaggle. Common columns might include: `age`, `job`, `marital`, `education`, `default`, `balance`, `housing`, `loan`, `contact`, `day`, `month`, `duration`, `campaign`, `pdays`, `previous`, `poutcome`, `deposit` (target variable: 'yes'/'no').

## 1. Setup and Data Loading

**Goal:** Initialize Spark and load the dataset into a DataFrame.

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, avg, when, desc, round, expr
# Potentially import visualization libraries if running in an environment that supports it
# import matplotlib.pyplot as plt
# import seaborn as sns

# 1. Initialize SparkSession
# spark = SparkSession.builder \
#     .appName("BankMarketingAnalysis") \
#     .master("local[*]") \ # Or your cluster master URL
#     .getOrCreate()

# 2. Load the dataset (assuming CSV format)
# file_path = "path/to/bank-full.csv" # Replace with actual path
# bank_df = spark.read.csv(file_path, header=True, inferSchema=True, sep=';') # Common separator for this dataset

# print("Dataset Schema:")
# bank_df.printSchema()
# print(f"Number of rows: {bank_df.count()}")
```
-   **Concepts:** [[PySpark_SparkSession_SparkContext|SparkSession]], [[PySpark_Data_Sources|Reading CSVs]], `inferSchema`.
-   **Considerations:** For large datasets, explicitly defining the schema with `StructType` is more robust and performant than `inferSchema=True`.

## 2. Initial Data Inspection and Exploration

**Goal:** Understand the data structure, types, and get a first look at the content.

```python
# 3. Print 10 random rows from the dataset
# print("\nRandom 10 rows:")
# bank_df.sample(withReplacement=False, fraction=0.1, seed=42).show(10, truncate=False) # Adjust fraction as needed
# A more direct way for a fixed number if dataset is not huge, but sample is better for large data.
# For truly random N rows without knowing fraction:
# if bank_df.count() > 10: # Ensure there are enough rows
#     random_sample_df = bank_df.orderBy(rand()).limit(10) # rand() might be from pyspark.sql.functions
#     random_sample_df.show(truncate=False)
# else:
#     bank_df.show(truncate=False)


# 4. What are the relative proportions of 'yes' and 'no' for the 'deposit' feature?
# print("\nProportion of 'deposit' classes:")
# deposit_proportions = bank_df.groupBy("deposit").count()
# total_count = bank_df.count()
# deposit_proportions = deposit_proportions.withColumn("proportion", round(col("count") / total_count, 4))
# deposit_proportions.show()

# Inspect other qualitative variables (e.g., 'job', 'marital', 'education')
# qualitative_cols = ["job", "marital", "education", "default", "housing", "loan", "contact", "month", "poutcome"]
# for q_col in qualitative_cols:
#     print(f"\nProportions for '{q_col}':")
#     prop_df = bank_df.groupBy(q_col).count().withColumn("proportion", round(col("count") / total_count, 4)).orderBy(desc("count"))
#     prop_df.show(truncate=False)

# 5. Get descriptive statistics for numerical variables
# numerical_cols = ['age', 'balance', 'day', 'duration', 'campaign', 'pdays', 'previous']
# print("\nDescriptive statistics for numerical variables:")
# bank_df.select(numerical_cols).describe().show(truncate=False, vertical=True) # vertical for better display if many columns
```
-   **Concepts:** `sample()`, `groupBy().count()`, `withColumn()`, `select().describe()`, [[PySpark_SQL_Functions|SQL functions]] like `round`, `desc`.
-   **Considerations:** `rand()` for ordering can be expensive on very large datasets. `sample()` is generally preferred. `describe()` provides count, mean, stddev, min, max for numerical columns.

## 3. Visualizations (Conceptual - Requires Plotting Environment)

**Goal:** Visually inspect variables and relationships. Spark itself doesn't plot; you'd typically convert a small sample or aggregated data to Pandas for plotting with Matplotlib/Seaborn, or use Spark-integrated BI tools.

```python
# 6. Use relevant visualizations
# Example: Distribution of 'age' (Histogram)
# age_data_pd = bank_df.select("age").sample(False, 0.1).toPandas() # Sample for plotting
# plt.figure(figsize=(8,5))
# sns.histplot(age_data_pd['age'], kde=True, bins=30)
# plt.title("Age Distribution of Clients")
# plt.xlabel("Age"); plt.ylabel("Frequency"); plt.show()

# Example: 'deposit' vs 'balance' (Box Plot)
# deposit_balance_pd = bank_df.select("deposit", "balance").sample(False, 0.1).toPandas()
# plt.figure(figsize=(8,5))
# sns.boxplot(x="deposit", y="balance", data=deposit_balance_pd)
# plt.title("Balance Distribution by Deposit Outcome")
# plt.yscale('log') # Balance can be highly skewed, log scale might help
# plt.show()

# Example: Relationship between 'duration' (call duration) and 'deposit' (Bar plot of means)
# duration_deposit_agg = bank_df.groupBy("deposit").agg(avg("duration").alias("avg_duration"))
# duration_deposit_pd = duration_deposit_agg.toPandas()
# plt.figure(figsize=(7,5))
# sns.barplot(x="deposit", y="avg_duration", data=duration_deposit_pd)
# plt.title("Average Call Duration by Deposit Outcome")
# plt.show()
```-   **Concepts:** Sampling data for visualization (`.sample().toPandas()`), using Matplotlib/Seaborn.
-   **Considerations:** Always sample or aggregate before `toPandas()` if the Spark DataFrame is large.

## 4. Answering Analytical Questions

**Goal:** Use DataFrame transformations and actions to answer specific questions.

```python
# 7. Who is the client with the biggest balance?
# (Assuming an 'id' or 'client_identifier' column exists, let's add one for example)
# from pyspark.sql.functions import monotonically_increasing_id
# bank_df_with_id = bank_df.withColumn("client_id", monotonically_increasing_id())

# biggest_balance_client = bank_df_with_id.orderBy(desc("balance")).first()
# if biggest_balance_client:
#     print(f"\nClient with biggest balance (ID: {biggest_balance_client['client_id']}): Balance = {biggest_balance_client['balance']}")
# else:
#     print("\nNo data to determine client with biggest balance.")


# 8. What is the proportion of clients whose balance is more than twice the average?
# avg_balance_val = bank_df.select(avg("balance")).first()[0]
# if avg_balance_val is not None:
#     twice_avg_balance = avg_balance_val * 2
#     high_balance_clients_count = bank_df.filter(col("balance") > twice_avg_balance).count()
#     proportion_high_balance = high_balance_clients_count / total_count if total_count > 0 else 0
#     print(f"\nAverage balance: {avg_balance_val:.2f}")
#     print(f"Proportion of clients with balance > {twice_avg_balance:.2f}: {proportion_high_balance:.4f}")
# else:
#     print("\nCould not calculate average balance.")


# 9. Do people with higher education have a better chance to deposit?
# (Assuming 'education' levels are ordered: 'unknown', 'primary', 'secondary', 'tertiary')
# education_deposit_summary = bank_df.groupBy("education", "deposit") \
#                                    .count() \
#                                    .orderBy("education", "deposit")
# print("\nDeposit outcome by Education Level:")
# education_deposit_summary.show()

# To calculate deposit rate per education level:
# education_totals = bank_df.groupBy("education").count().withColumnRenamed("count", "total_in_education")
# education_yes_deposit = bank_df.filter(col("deposit") == "yes") \
#                                .groupBy("education").count().withColumnRenamed("count", "yes_deposits")
# education_rates = education_totals.join(education_yes_deposit, "education", "left_outer") \
#                                   .na.fill(0, subset=["yes_deposits"]) \
#                                   .withColumn("deposit_rate", round(col("yes_deposits") / col("total_in_education"), 4)) \
#                                   .orderBy("education") # Or order by a custom education level order
# print("\nDeposit Rate by Education Level:")
# education_rates.show()


# 10. What are the best predictors for deposit?
# This is a machine learning question. Would involve:
# - Feature engineering (e.g., converting categoricals to numerical, scaling).
# - Training a classification model (e.g., Logistic Regression, Decision Tree, Random Forest from Spark MLlib).
# - Evaluating feature importances from the model.
# print("\nFinding best predictors involves ML modeling (e.g., feature importances from a classifier).")
# print("Conceptual steps: Preprocess data, train a model (e.g., RandomForestClassifier from spark.ml.classification), extract featureImportances.")
```
-   **Concepts:** `orderBy().first()`, aggregate functions (`avg`, `count`), filtering, joins, conditional logic. For predictors, it points towards [[Spark_MLlib|MLlib]].

## 5. Cleanup
```python
# 11. Stop the SparkSession
# spark.stop()
```

This workflow provides a conceptual guide. Actual implementation would involve handling data types more carefully, robust error checking, and potentially more sophisticated feature engineering and visualization techniques depending on the depth of analysis required.

---