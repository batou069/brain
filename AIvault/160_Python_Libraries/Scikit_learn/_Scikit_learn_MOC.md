---
tags:
  - python
  - library
  - scikit_learn
  - sklearn
  - machine_learning
  - data_mining
  - moc
  - concept
aliases:
  - Scikit-learn MOC
  - sklearn MOC
related:
  - "[[_Python_Libraries_MOC]]"
  - "[[_NumPy_MOC]]"
  - "[[_Pandas_MOC]]"
  - "[[SciPy_Library]]"
  - "[[Machine_Learning_Overview]]"
  - "[[Supervised_Learning]]"
  - "[[Unsupervised_Learning]]"
  - "[[Model_Evaluation_Metrics]]"
worksheet:
  - WS_ML_Libraries_1
date_created: 2025-06-09
---
# Scikit-learn MOC 🤖⚙️

**Scikit-learn** (often imported as `sklearn`) is one of the most popular and comprehensive open-source machine learning libraries for Python. It provides a wide range of tools for building and evaluating machine learning models, covering tasks like classification, regression, clustering, dimensionality reduction, model selection, and preprocessing.

## Core Philosophy & Features
-   **Simple and Consistent API:** Offers a clean, consistent interface for using different algorithms (Estimator API: `fit()`, `predict()`, `transform()`).
-   **Comprehensive Toolset:** Covers a vast array of ML tasks.
-   **Built on NumPy, SciPy, and Matplotlib:** Leverages these foundational libraries for efficient computation and visualization.
-   **Well-Documented:** Extensive documentation with examples and user guides.
-   **Active Community:** Large and active community contributing to its development and providing support.
-   **Widely Used:** A standard tool in both industry and academia for machine learning projects.

## Key Modules & Functionality Areas
Scikit-learn's functionality is organized into several modules:

[list2card|addClass(ab-col3)|#Sklearn Modules]
- **[[Sklearn_Preprocessing|Preprocessing (`sklearn.preprocessing`)]]**
  - Feature scaling, normalization, encoding categorical features, imputation.
- **[[Sklearn_Model_Selection|Model Selection (`sklearn.model_selection`)]]**
  - Splitting data (train/test), cross-validation, hyperparameter tuning (GridSearchCV, RandomizedSearchCV).
- **[[Sklearn_Supervised_Learning_Models|Supervised Learning Models]]**
  - **[[Sklearn_Linear_Models|Linear Models (`sklearn.linear_model`)]]:** Logistic Regression, Linear Regression, Ridge, Lasso, ElasticNet.
  - **[[Sklearn_Support_Vector_Machines|Support Vector Machines (`sklearn.svm`)]]:** SVC, SVR, NuSVC, NuSVR.
  - **[[Sklearn_Tree_Based_Models|Tree-based Models (`sklearn.tree`)]]:** Decision Trees (Classifier, Regressor).
  - **[[Sklearn_Ensemble_Methods|Ensemble Methods (`sklearn.ensemble`)]]:** Random Forests, Gradient Boosting, AdaBoost, ExtraTrees.
  - **[[Sklearn_Nearest_Neighbors|Nearest Neighbors (`sklearn.neighbors`)]]:** KNeighborsClassifier, KNeighborsRegressor.
  - **Naive Bayes (`sklearn.naive_bayes`):** GaussianNB, MultinomialNB, BernoulliNB.
- **[[Sklearn_Unsupervised_Learning_Models|Unsupervised Learning Models]]**
  - **[[Sklearn_Clustering|Clustering (`sklearn.cluster`)]]:** K-Means, DBSCAN, Agglomerative Clustering, Spectral Clustering.
  - **[[Sklearn_Dimensionality_Reduction|Dimensionality Reduction (`sklearn.decomposition`)]]:** PCA, NMF, ICA, TruncatedSVD.
  - **Manifold Learning (`sklearn.manifold`):** t-SNE, Isomap, LLE.
  - **Density Estimation (`sklearn.mixture`):** Gaussian Mixture Models.
- **[[Sklearn_Metrics|Metrics (`sklearn.metrics`)]]**
  - Model evaluation: accuracy, precision, recall, F1-score, ROC AUC, confusion matrix, regression metrics (MSE, MAE, R2).
- **[[Sklearn_Pipelines|Pipelines (`sklearn.pipeline`)]]**
  - Chaining multiple processing steps (e.g., preprocessing + model).
- **Feature Extraction (`sklearn.feature_extraction`)**
  - Tools for extracting features from text (`CountVectorizer`, `TfidfVectorizer`) and images.
- **Datasets (`sklearn.datasets`)**
  - Includes utilities to load sample datasets (e.g., Iris, Digits, Boston Housing) and generate synthetic data.

## Notes in this Scikit-learn Section
```dataview
LIST
FROM "160_Python_Libraries/Scikit_learn"
WHERE file.folder = this.file.folder AND file.name != this.file.name AND !contains(file.name, "MOC")
SORT file.name ASC
```

---