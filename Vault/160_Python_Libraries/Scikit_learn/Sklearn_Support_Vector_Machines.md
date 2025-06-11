---
tags:
  - python
  - scikit_learn
  - sklearn
  - machine_learning
  - svm
  - svc
  - svr
  - classification
  - regression
  - concept
  - example
aliases:
  - Scikit-learn SVM
  - Support Vector Classifier
  - Support Vector Regressor
  - SVC
  - SVR
related:
  - "[[160_Python_Libraries/Scikit_learn/_Scikit_learn_MOC|_Scikit_learn_MOC]]"
  - "[[Supervised_Learning]]"
  - "[[Kernels_ML|Kernel Trick]]"
  - "[[Margin_Maximization_SVM|Margin Maximization (SVM)]]"
worksheet:
  - WS_ML_Libraries_1
date_created: 2025-06-09
---
# Scikit-learn: Support Vector Machines (`sklearn.svm`)

Support Vector Machines (SVMs) are powerful and versatile supervised learning models used for [[Sklearn_Supervised_Learning_Models|classification]], [[Sklearn_Supervised_Learning_Models|regression]], and outlier detection. They are particularly effective in high-dimensional spaces and are memory efficient as they use a subset of training points (support vectors) in the decision function.

The `sklearn.svm` module includes several SVM implementations.

## Key SVM Models

[list2tab|#SVM Models]
- Support Vector Classification (SVC)
    - **Model:** `SVC` (also `NuSVC`, `LinearSVC`)
    - **Purpose:** Used for binary and multi-class classification tasks. The goal of an SVC is to find a hyperplane in an N-dimensional space (N = number of features) that distinctly classifies the data points. The "best" hyperplane is the one that has the largest margin between the two classes (see [[Margin_Maximization_SVM|Margin Maximization]]).
    - **[[Kernels_ML|Kernel Trick]]:** SVMs can perform non-linear classification using the kernel trick, implicitly mapping their inputs into high-dimensional feature spaces.
    - **Key Parameters for `SVC`:**
        -   `C`: Regularization parameter (float, default 1.0). The strength of the regularization is inversely proportional to C. Must be strictly positive.
        -   `kernel`: `{'linear', 'poly', 'rbf', 'sigmoid', 'precomputed'}` or a callable (default 'rbf'). Specifies the kernel type to be used in the algorithm.
        -   `gamma`: `{'scale', 'auto'}` or float (default 'scale'). Kernel coefficient for 'rbf', 'poly', and 'sigmoid'.
            -   If `gamma='scale'` (default) then it uses `1 / (n_features * X.var())`.
            -   If `gamma='auto'`, it uses `1 / n_features`.
        -   `degree`: Degree of the polynomial kernel function ('poly') (default 3). Ignored by all other kernels.
        -   `probability`: Whether to enable probability estimates (boolean, default False). Slower to train.
        -   `class_weight`: Set the parameter C of class i to `class_weight[i]*C`. Useful for imbalanced datasets.
    - **`LinearSVC`**: Similar to `SVC` with `kernel='linear'`, but implemented in terms of `liblinear` rather than `libsvm`, so it has more flexibility in the choice of penalties and loss functions and should scale better to large numbers of samples. It does not support the `kernel` parameter (it's always linear).
    - **Example (Classifying product reviews as positive/negative):**
        ```python
        from sklearn.svm import SVC
        from sklearn.model_selection import train_test_split
        from sklearn.preprocessing import StandardScaler
        from sklearn.feature_extraction.text import TfidfVectorizer # For text features
        import pandas as pd
        import numpy as np

        # Conceptual data: product review text and sentiment (0=negative, 1=positive)
        reviews_data = pd.DataFrame({
            'review_text': ['great product love it', 'terrible waste of money', 'okay but not great', 'best purchase ever', 'would not recommend'],
            'sentiment': [1, 0, 0, 1, 0]
        })
        # For real text data, extensive preprocessing is needed.
        # Here, using TF-IDF for a simple feature representation.
        vectorizer = TfidfVectorizer(max_features=100) # Limit features for example
        X_text_features = vectorizer.fit_transform(reviews_data['review_text'])
        y_sentiment = reviews_data['sentiment']

        # X_train, X_test, y_train, y_test = train_test_split(X_text_features, y_sentiment, test_size=0.3, random_state=42)

        # SVC with RBF kernel
        # svc_model = SVC(kernel='rbf', C=1.0, gamma='scale', probability=True, random_state=42)
        # svc_model.fit(X_train, y_train)
        # accuracy = svc_model.score(X_test, y_test)
        # print(f"SVC Accuracy: {accuracy:.4f}")

        # LinearSVC example (often faster for text data)
        # from sklearn.svm import LinearSVC
        # linear_svc_model = LinearSVC(C=0.5, random_state=42, dual="auto") # dual="auto" or dual=True/False depending on n_samples/n_features
        # linear_svc_model.fit(X_train, y_train)
        # accuracy_linear = linear_svc_model.score(X_test, y_test)
        # print(f"LinearSVC Accuracy: {accuracy_linear:.4f}")
        ```
- Support Vector Regression (SVR)
    - **Model:** `SVR` (also `NuSVR`, `LinearSVR`)
    - **Purpose:** Used for regression tasks. The goal is to find a function that deviates from $y$ by a value no greater than $\epsilon$ (epsilon) for each training point, and at the same time is as flat as possible. The points within the $\epsilon$-tube do not contribute to the loss.
    - **Key Parameters for `SVR`:**
        -   `kernel`, `C`, `gamma`, `degree`: Similar to `SVC`.
        -   `epsilon`: Epsilon in the epsilon-SVR model. It specifies the epsilon-tube within which no penalty is associated in the training loss function with points predicted within a distance epsilon from the actual value. (float, default 0.1).
    - **`LinearSVR`**: Similar to `SVR` with `kernel='linear'`, but implemented in terms of `liblinear`. Faster for linear cases.
    - **Example (Predicting product price based on features):**
        ```python
        from sklearn.svm import SVR
        from sklearn.preprocessing import StandardScaler
        import pandas as pd
        import numpy as np

        # Conceptual product data from previous Linear Models example
        X_product_features = pd.DataFrame({
            'size_cm':,
            'material_cost': [5, 7, 6, 10, 5.5],
            'feature3': [0.2, 0.8, 0.5, 0.9, 0.3] # Added another feature
        })
        y_product_price = pd.Series()
        
        # Scaling is often important for SVR
        # scaler_X = StandardScaler()
        # X_scaled = scaler_X.fit_transform(X_product_features)
        # scaler_y = StandardScaler() # Scale target too if its range is large
        # y_scaled = scaler_y.fit_transform(y_product_price.values.reshape(-1,1)).ravel()

        # svr_model = SVR(kernel='rbf', C=100, gamma=0.1, epsilon=0.1)
        # svr_model.fit(X_scaled, y_scaled)
        # predictions_scaled = svr_model.predict(X_scaled)
        # predictions_original_scale = scaler_y.inverse_transform(predictions_scaled.reshape(-1,1))
        # print("SVR Predictions (original scale, first 5):", predictions_original_scale.ravel()[:5])
        ```
- One-Class SVM
    - **Model:** `OneClassSVM`
    - **Purpose:** Used for novelty or outlier detection. It learns a decision boundary that encloses the "normal" data points. New points falling outside this boundary are considered outliers or novel.
    - **Key Parameters:** `kernel`, `gamma`, `nu` (An upper bound on the fraction of training errors and a lower bound of the fraction of support vectors. Should be in the interval (0, 1].).
    - **Example (Detecting anomalous product transactions):**
        ```python
        from sklearn.svm import OneClassSVM
        import numpy as np
        import pandas as pd

        # Conceptual transaction data (amount, items_count)
        # Assume most transactions are "normal"
        normal_transactions = np.random.multivariate_normal(mean=[50, 3], cov=[[100, 10], [10, 1]], size=100)
        # Add some anomalies
        anomalies = np.array([[500, 1], [10, 20], [1, 15]])
        X_transactions = np.vstack([normal_transactions, anomalies])
        X_transactions_df = pd.DataFrame(X_transactions, columns=['amount', 'items_count'])

        # Fit OneClassSVM
        # nu is an estimate of the proportion of outliers in the data
        # one_class_svm = OneClassSVM(kernel='rbf', gamma='auto', nu=0.05) # Expect ~5% outliers
        # one_class_svm.fit(X_transactions_df)
        
        # predict returns +1 for inliers (normal), -1 for outliers (anomalous)
        # predictions_novelty = one_class_svm.predict(X_transactions_df)
        # num_outliers = (predictions_novelty == -1).sum()
        # print(f"Number of outliers detected: {num_outliers} out of {len(X_transactions_df)}")
        # print("Predictions (first 10 and last 3):", np.concatenate((predictions_novelty[:10], predictions_novelty[-3:])))
        ```

## Advantages of SVMs
-   Effective in high-dimensional spaces (even when number of dimensions > number of samples).
-   Memory efficient as they use a subset of training points (support vectors) in the decision function.
-   Versatile due to different [[Kernels_ML|kernel functions]] allowing for linear and non-linear decision boundaries.

## Disadvantages of SVMs
-   Can be computationally intensive to train, especially for large datasets (complexity can be between $O(N_{samples}^2 \cdot N_{features})$ and $O(N_{samples}^3 \cdot N_{features})$ for some implementations/kernels). `LinearSVC`/`LinearSVR` are much faster for linear cases.
-   Performance is sensitive to the choice of kernel and hyperparameters (`C`, `gamma`). Requires careful tuning (e.g., using [[Sklearn_Model_Selection|GridSearchCV]]).
-   Less interpretable compared to models like Decision Trees or Linear Regression; it's harder to understand the contribution of individual features directly from the fitted model with non-linear kernels.

SVMs are a powerful class of models, particularly strong when clear margins of separation exist or when dealing with high-dimensional data.

---