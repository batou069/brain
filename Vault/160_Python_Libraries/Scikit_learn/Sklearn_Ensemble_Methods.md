---
tags:
  - python
  - scikit_learn
  - sklearn
  - machine_learning
  - ensemble_methods
  - random_forest
  - gradient_boosting
  - adaboost
  - concept
  - example
aliases:
  - Scikit-learn Ensembles
  - Random Forest
  - Gradient Boosting
  - AdaBoost
related:
  - "[[160_Python_Libraries/Scikit_learn/_Scikit_learn_MOC|_Scikit_learn_MOC]]"
  - "[[Sklearn_Tree_Based_Models|Decision Trees]]"
  - "[[Overfitting_Underfitting]]"
  - "[[Bias_Variance_Tradeoff]]"
worksheet:
  - WS_ML_Libraries_1
date_created: 2025-06-09
---
# Scikit-learn: Ensemble Methods (`sklearn.ensemble`)

Ensemble methods combine the predictions of several base estimators (often [[Sklearn_Tree_Based_Models|Decision Trees]]) built with a given learning algorithm in order to improve generalizability and robustness over a single estimator. The `sklearn.ensemble` module includes popular ensemble techniques.

Two main families of ensemble methods are:
1.  **Averaging methods (Bagging):** Build several estimators independently and then average their predictions. The combined estimator is usually better than any single base estimator because its variance is reduced.
    -   Example: Random Forests, ExtraTrees.
2.  **Boosting methods:** Base estimators are built sequentially, and one tries to reduce the bias of the combined estimator. The motivation is to combine several weak models to produce a powerful ensemble.
    -   Example: AdaBoost, Gradient Tree Boosting.

## Key Ensemble Models

[list2tab|#Ensemble Models]
- Random Forest
    - **Models:** `RandomForestClassifier`, `RandomForestRegressor`
    - **Concept (Bagging):** An ensemble of [[Sklearn_Tree_Based_Models|Decision Trees]]. Each tree in the forest is built from a sample drawn with replacement (bootstrap sample) from the training set. Additionally, when splitting each node during the construction of a tree, the best split is found from a random subset of features instead of all features.
    - **Purpose:** Improves accuracy and controls [[Overfitting_Underfitting|overfitting]] compared to a single decision tree.
    - **Key Parameters:**
        -   `n_estimators`: The number of trees in the forest (default 100).
        -   `criterion`: Function to measure split quality (e.g., 'gini', 'entropy' for classifier; 'squared_error', 'absolute_error' for regressor).
        -   `max_depth`: Maximum depth of the individual trees.
        -   `min_samples_split`, `min_samples_leaf`: Minimum samples for splitting/leaf.
        -   `max_features`: Number of features to consider for the best split.
        -   `bootstrap`: Whether bootstrap samples are used (default True).
        -   `oob_score`: Whether to use out-of-bag samples to estimate generalization accuracy (default False).
    - **Example (Customer churn prediction - classification):**
        ```python
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.model_selection import train_test_split
        import pandas as pd
        import numpy as np

        # Conceptual customer data for churn prediction
        # Features: usage_minutes, contract_type (needs encoding), customer_service_calls
        # Target: churn (0=No, 1=Yes)
        X_customer_profile = pd.DataFrame({
            'usage_minutes': np.random.randint(50, 1000, 200),
            'contract_type': np.random.choice(['monthly', 'annual', 'two_year'], 200),
            'cs_calls': np.random.randint(0, 5, 200)
        })
        # Preprocess 'contract_type' (e.g., one-hot encode)
        X_customer_profile = pd.get_dummies(X_customer_profile, columns=['contract_type'], drop_first=True)
        y_churn_status = pd.Series(np.random.randint(0, 2, 200))

        # X_train, X_test, y_train, y_test = train_test_split(X_customer_profile, y_churn_status, test_size=0.3, random_state=42)

        # rf_clf = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42, class_weight='balanced')
        # rf_clf.fit(X_train, y_train)
        # accuracy = rf_clf.score(X_test, y_test)
        # print(f"Random Forest Classifier Accuracy: {accuracy:.4f}")
        # Feature importances:
        # importances = rf_clf.feature_importances_
        # feature_names = X_train.columns
        # sorted_indices = np.argsort(importances)[::-1]
        # print("\nFeature Importances:")
        # for i in sorted_indices:
        #     print(f"{feature_names[i]}: {importances[i]:.4f}")
        ```
- Gradient Tree Boosting (Gradient Boosting Machines - GBM)
    - **Models:** `GradientBoostingClassifier`, `GradientBoostingRegressor`
    - **Concept (Boosting):** Builds an additive model in a forward stage-wise fashion. It fits a new tree to the residuals (errors) of the previous trees. This means each new tree tries to correct the errors made by the ensemble of trees already built.
    - **Purpose:** Often provides high predictive accuracy. Can be prone to overfitting if not tuned carefully.
    - **Key Parameters:**
        -   `n_estimators`: Number of boosting stages (trees) to perform.
        -   `learning_rate`: Shrinks the contribution of each tree. There is a trade-off with `n_estimators`.
        -   `max_depth`: Maximum depth of the individual regression estimators.
        -   `subsample`: Fraction of samples to be used for fitting individual base learners (stochastic gradient boosting).
        -   `loss`: Loss function to be optimized ('log_loss' for classification, 'squared_error' for regression).
    - **Example (Predicting e-commerce sales amount - regression):**
        ```python
        from sklearn.ensemble import GradientBoostingRegressor
        from sklearn.model_selection import train_test_split
        from sklearn.metrics import mean_squared_error
        import pandas as pd
        import numpy as np

        # Conceptual sales data
        # Features: marketing_spend, previous_month_sales, num_promotions
        # Target: current_month_sales
        X_sales_drivers = pd.DataFrame({
            'marketing_spend': np.random.uniform(1000, 10000, 100),
            'prev_month_sales': np.random.uniform(5000, 50000, 100),
            'num_promotions': np.random.randint(0, 5, 100)
        })
        y_current_sales = X_sales_drivers['prev_month_sales'] * (1 + X_sales_drivers['marketing_spend']/50000 + X_sales_drivers['num_promotions']*0.05) + np.random.randn(100)*5000

        # X_train, X_test, y_train, y_test = train_test_split(X_sales_drivers, y_current_sales, test_size=0.25, random_state=42)

        # gbr_model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
        # gbr_model.fit(X_train, y_train)
        # predictions = gbr_model.predict(X_test)
        # mse = mean_squared_error(y_test, predictions)
        # print(f"Gradient Boosting Regressor MSE: {mse:.2f}")
        ```
- AdaBoost (Adaptive Boosting)
    - **Models:** `AdaBoostClassifier`, `AdaBoostRegressor`
    - **Concept (Boosting):** Fits a sequence of weak learners (e.g., shallow decision trees) on repeatedly modified versions of the data. Predictions from all of them are then combined through a weighted majority vote (or sum) to produce the final prediction. It focuses more on samples that are misclassified by previous learners by increasing their weights.
    - **Key Parameters:**
        -   `base_estimator`: The base estimator from which the ensemble is built (default is `DecisionTreeClassifier(max_depth=1)` for classifier).
        -   `n_estimators`: The maximum number of estimators at which boosting is terminated.
        -   `learning_rate`: Shrinks the contribution of each classifier/regressor.
    - **Example (Product defect classification):**
        ```python
        from sklearn.ensemble import AdaBoostClassifier
        from sklearn.tree import DecisionTreeClassifier # Often used as base estimator
        # Using X_customer_profile, y_churn_status for a classification example structure
        X_customer_profile = pd.DataFrame(np.random.rand(100,3)) # Dummy features
        y_churn_status = pd.Series(np.random.randint(0,2,100)) # Dummy target
        # X_train, X_test, y_train, y_test = train_test_split(X_customer_profile, y_churn_status, test_size=0.3, random_state=42)

        # Define a base estimator (optional, AdaBoost uses a Decision Stump by default)
        # base_tree = DecisionTreeClassifier(max_depth=1)
        # ada_clf = AdaBoostClassifier(estimator=base_tree, n_estimators=50, learning_rate=1.0, random_state=42, algorithm='SAMME') # SAMME for discrete
        # ada_clf.fit(X_train, y_train)
        # accuracy = ada_clf.score(X_test, y_test)
        # print(f"AdaBoost Classifier Accuracy: {accuracy:.4f}")
        ```
- Other Ensembles
    - **`ExtraTreesClassifier` / `ExtraTreesRegressor` (Extremely Randomized Trees):** Similar to Random Forests, but randomness goes further in the way splits are computed. Splits are chosen from random thresholds for features rather than the most discriminative thresholds. This can sometimes reduce variance further but might slightly increase bias.
    - **`VotingClassifier` / `VotingRegressor`:** Combines conceptually different machine learning classifiers/regressors and uses a majority vote (hard voting) or the average of predicted probabilities (soft voting) / predicted values to predict the class labels / values.
    - **Stacking (`StackingClassifier` / `StackingRegressor`):** Combines multiple classification or regression models via a meta-classifier or meta-regressor. The base models are trained on the full training set, then the meta-model is trained on the outputs (predictions) of the base models as features.

## Advantages of Ensemble Methods
-   **Improved Accuracy:** Generally yield better predictive performance than any single constituent model.
-   **Reduced Overfitting / Better Generalization:** Especially true for bagging methods like Random Forests, by averaging out variance.
-   **Robustness:** Less sensitive to the specifics of a single training set.
-   **Feature Importance:** Methods like Random Forests and Gradient Boosting provide measures of feature importance.

## Considerations
-   **Increased Complexity:** Ensembles are more complex than single models, making them harder to interpret directly.
-   **Computational Cost:** Training multiple models can be computationally expensive and time-consuming.
-   **Tuning:** Ensembles often have more hyperparameters to tune.

Ensemble methods are a cornerstone of modern machine learning, frequently winning competitions and providing state-of-the-art results for many tabular data problems.

---