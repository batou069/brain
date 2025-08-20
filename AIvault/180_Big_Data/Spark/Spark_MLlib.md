---
tags:
  - spark
  - pyspark
  - mllib
  - machine_learning
  - distributed_ml
  - classification
  - regression
  - clustering
  - concept
aliases:
  - Spark MLlib
  - MLlib
  - Spark Machine Learning Library
related:
  - "[[180_Big_Data/Spark/_Spark_MOC|_Spark_MOC]]"
  - "[[Spark_DataFrame_SQL|Spark DataFrame & SQL]]"
  - "[[RDD_Resilient_Distributed_Dataset|RDD]]"
  - "[[Scikit_learn_MOC|_Scikit_learn_MOC]]"
  - "[[Machine_Learning_Overview]]"
worksheet:
  - WS_Spark_1
date_created: 2025-08-20
---
# Spark MLlib (Machine Learning Library)

**MLlib** is Apache Spark's scalable machine learning library. It aims to make practical machine learning scalable and easy, providing tools such as:
-   Common learning algorithms (classification, regression, clustering, collaborative filtering).
-   Featurization utilities (feature extraction, transformation, dimensionality reduction, selection).
-   Pipelines for constructing, evaluating, and tuning ML workflows.
-   Persistence utilities for saving and loading algorithms, models, and pipelines.

MLlib has two main APIs:
1.  **`spark.mllib` (RDD-based API - Older):** The original API built on top of [[RDD_Resilient_Distributed_Dataset|RDDs]]. It is now in maintenance mode.
2.  **`spark.ml` (DataFrame-based API - Recommended):** The primary API since Spark 2.0, built on top of [[Spark_DataFrame_SQL|DataFrames]]. It offers a more user-friendly and uniform API, leveraging the optimizations of Spark SQL and DataFrames. This note will focus on the `spark.ml` API.

## Key Components of `spark.ml`

[list2tab|#spark.ml Components]
- DataFrame as Primary Data Structure
    -   `spark.ml` uses DataFrames to represent datasets, which can hold a variety of data types. A typical DataFrame has columns for features, labels (for supervised learning), and predictions.
- Transformers
    -   An algorithm that can transform one DataFrame into another DataFrame.
    -   Implements a `.transform()` method.
    -   Examples:
        -   Feature Transformers: `VectorAssembler` (combines multiple columns into a single feature vector), `StandardScaler`, `MinMaxScaler`, `StringIndexer` (encodes string labels to numerical indices), `OneHotEncoder`, `PCA`.
        -   Fitted Models: A trained model is also a transformer that transforms a DataFrame with features into a DataFrame with predictions.
- Estimators
    -   An algorithm which can be fit on a DataFrame to produce a Transformer.
    -   Implements a `.fit()` method, which takes a DataFrame and returns a model (which is a Transformer).
    -   Examples: `LogisticRegression` (classifier), `DecisionTreeRegressor` (regressor), `KMeans` (clustering algorithm).
- Pipelines (`Pipeline`)
    -   Chains multiple Transformers and Estimators together to specify an ML workflow.
    -   A `Pipeline` itself is an Estimator. When `fit()` is called on a Pipeline, it fits all Estimators in sequence. The resulting `PipelineModel` is a Transformer.
    -   Ensures that training and test data go through the same processing steps.
    -   Example: A pipeline might consist of `StringIndexer` -> `OneHotEncoder` -> `VectorAssembler` -> `LogisticRegression`.
- Evaluation (`Evaluator`)
    -   Used to measure the performance of a model.
    -   Examples: `BinaryClassificationEvaluator` (metrics: areaUnderROC, areaUnderPR), `MulticlassClassificationEvaluator` (metrics: accuracy, f1, precision, recall), `RegressionEvaluator` (metrics: rmse, mse, r2, mae).
- Parameter Tuning (Hyperparameter Optimization)
    -   Tools for finding the best hyperparameters for models.
    -   `CrossValidator`: Uses K-fold cross-validation to evaluate each parameter combination.
    -   `TrainValidationSplit`: Simpler, splits data once into training and validation sets.
    -   Requires an `Estimator` (e.g., a model or a full Pipeline), a set of `ParamGridBuilder` (parameter grids), and an `Evaluator`.

## Common ML Tasks and Algorithms in `spark.ml`

[list2tab|#MLlib Algorithms]
- Classification
    -   `LogisticRegression`
    -   `DecisionTreeClassifier`
    -   `RandomForestClassifier`
    -   `GBTClassifier` (Gradient-Boosted Trees)
    -   `MultilayerPerceptronClassifier` (Basic Neural Network)
    -   `LinearSVC` (Linear Support Vector Classifier)
    -   `NaiveBayes`
- Regression
    -   `LinearRegression`
    -   `DecisionTreeRegressor`
    -   `RandomForestRegressor`
    -   `GBTRegressor`
    -   `GeneralizedLinearRegression` (GLM)
    -   `IsotonicRegression`
- Clustering
    -   `KMeans`
    -   `LDA` (Latent Dirichlet Allocation - for topic modeling, can be seen as a form of clustering)
    -   `BisectingKMeans`
    -   `GaussianMixture` (GMM)
- Collaborative Filtering
    -   `ALS` (Alternating Least Squares): For building recommendation systems.
- Featurization
    -   **Extraction:** `TFIDF`, `Word2Vec`, `CountVectorizer`, `FeatureHasher`.
    -   **Transformation:** `StringIndexer`, `OneHotEncoder`, `VectorAssembler`, `StandardScaler`, `MinMaxScaler`, `PCA`, `Normalizer`, `Bucketizer`, `QuantileDiscretizer`.
    -   **Selection:** `ChiSqSelector`, `VectorSlicer`.

## Example: Logistic Regression for E-commerce Customer Churn Prediction
```python
# from pyspark.sql import SparkSession
# from pyspark.ml.feature import VectorAssembler, StringIndexer, StandardScaler
# from pyspark.ml.classification import LogisticRegression
# from pyspark.ml import Pipeline
# from pyspark.ml.evaluation import BinaryClassificationEvaluator
# from pyspark.sql.functions import col
# import pandas as pd # For creating initial dummy data

# spark = SparkSession.builder.appName("MLlibChurnPrediction").master("local[*]").getOrCreate()

# Sample customer data (conceptual - replace with actual data loading)
# pandas_df = pd.DataFrame({
#     'customer_id': ['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10'],
#     'age':,
#     'gender': ['F', 'M', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F'],
#     'monthly_spend':,
#     'last_purchase_days_ago':,
#     'churned': # Target variable
# })
# spark_df = spark.createDataFrame(pandas_df)

# 1. Feature Engineering
# Index 'gender' string column to numerical
# gender_indexer = StringIndexer(inputCol="gender", outputCol="gender_indexed", handleInvalid="keep")
# Assemble features into a single vector
# feature_cols = ["age", "gender_indexed", "monthly_spend", "last_purchase_days_ago"]
# assembler = VectorAssembler(inputCols=feature_cols, outputCol="raw_features")
# Scale features
# scaler = StandardScaler(inputCol="raw_features", outputCol="scaled_features")

# 2. Define the Model
# logistic_regression = LogisticRegression(featuresCol="scaled_features", labelCol="churned")

# 3. Create a Pipeline
# pipeline = Pipeline(stages=[gender_indexer, assembler, scaler, logistic_regression])

# 4. Split Data
# train_data, test_data = spark_df.randomSplit([0.7, 0.3], seed=42)

# 5. Train the Model (Fit the Pipeline)
# try:
#     pipeline_model = pipeline.fit(train_data)
# except Exception as e: # Catch potential errors with tiny dummy data
#     print(f"Error during pipeline fitting (likely due to small/dummy data): {e}")
#     pipeline_model = None # Ensure it's defined

# 6. Make Predictions
# if pipeline_model:
#     predictions = pipeline_model.transform(test_data)
#     print("--- Predictions (sample) ---")
#     predictions.select("customer_id", "churned", "probability", "prediction").show(5)

    # 7. Evaluate the Model
    # evaluator = BinaryClassificationEvaluator(labelCol="churned", rawPredictionCol="rawPrediction", metricName="areaUnderROC")
    # auc = evaluator.evaluate(predictions)
    # print(f"Area Under ROC on Test Data: {auc:.4f}")

    # For accuracy:
    # from pyspark.ml.evaluation import MulticlassClassificationEvaluator
    # acc_evaluator = MulticlassClassificationEvaluator(labelCol="churned", predictionCol="prediction", metricName="accuracy")
    # accuracy = acc_evaluator.evaluate(predictions)
    # print(f"Accuracy on Test Data: {accuracy:.4f}")

# spark.stop()
```

## Advantages of MLlib (`spark.ml`)
-   **Scalability:** Designed to run on large distributed datasets.
-   **DataFrame Integration:** Leverages the power and optimizations of Spark SQL and DataFrames.
-   **Unified API:** Consistent API across different algorithms and pipeline stages.
-   **Pipeline Persistence:** Entire ML pipelines (including preprocessing and model) can be saved and loaded.

MLlib provides a robust framework for building scalable machine learning pipelines in Spark, making it suitable for handling Big Data ML tasks.

---