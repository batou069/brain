---
tags:
  - python
  - scikit_learn
  - sklearn
  - machine_learning
  - decision_tree
  - classification
  - regression
  - concept
  - example
aliases:
  - Scikit-learn Decision Trees
  - sklearn.tree
related:
  - "[[160_Python_Libraries/Scikit_learn/_Scikit_learn_MOC|_Scikit_learn_MOC]]"
  - "[[Supervised_Learning]]"
  - "[[Sklearn_Ensemble_Methods]]"
  - "[[Overfitting_Underfitting]]"
worksheet:
  - WS_ML_Libraries_1
date_created: 2025-06-09
---
# Scikit-learn: Tree-based Models (`sklearn.tree`)

Decision Trees are versatile supervised learning models used for both classification and regression tasks. They work by learning simple decision rules inferred from the data features to predict a target variable. The `sklearn.tree` module in Scikit-learn provides implementations for these models.

## Key Tree-based Models

[list2tab|#Tree Models]
- Decision Tree Classifier
    - **Model:** `DecisionTreeClassifier`
    - **Purpose:** Predicts the class label of a sample by learning simple decision rules. The tree is built by recursively splitting the data based on feature values that best separate the classes.
    - **Splitting Criteria:** Common criteria to measure the quality of a split include:
        -   `criterion='gini'` (Gini impurity): Measures the frequency at which any element of the dataset will be mislabelled.
        -   `criterion='entropy'` (Information Gain): Uses entropy from information theory.
    - **Key Parameters:**
        -   `criterion`: The function to measure the quality of a split.
        -   `max_depth`: The maximum depth of the tree. Controls complexity; helps prevent overfitting.
        -   `min_samples_split`: The minimum number of samples required to split an internal node.
        -   `min_samples_leaf`: The minimum number of samples required to be at a leaf node.
        -   `max_features`: The number of features to consider when looking for the best split.
        -   `class_weight`: Weights associated with classes. Useful for imbalanced datasets.
    - **Example (Predicting if a customer will click on a product based on browsing history):**
        ```python
        from sklearn.tree import DecisionTreeClassifier, plot_tree
        from sklearn.model_selection import train_test_split
        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt

        # Conceptual customer browsing data
        # Features: pages_viewed, time_on_site_min, previous_purchases
        # Target: clicked_on_featured_product (0 or 1)
        X_browsing = pd.DataFrame({
            'pages_viewed': np.random.randint(1, 20, 100),
            'time_on_site_min': np.random.uniform(0.5, 60, 100),
            'previous_purchases': np.random.randint(0, 5, 100)
        })
        y_clicked = pd.Series(np.random.randint(0, 2, 100))

        # X_train, X_test, y_train, y_test = train_test_split(X_browsing, y_clicked, test_size=0.3, random_state=42)

        # dt_classifier = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=42)
        # dt_classifier.fit(X_train, y_train)
        
        # accuracy = dt_classifier.score(X_test, y_test)
        # print(f"Decision Tree Classifier Accuracy: {accuracy:.4f}")

        # Visualize the tree (optional, can be large)
        # plt.figure(figsize=(15,10))
        # plot_tree(dt_classifier, filled=True, feature_names=X_browsing.columns.tolist(), class_names=['No_Click', 'Click'], rounded=True)
        # plt.show()
        ```
- Decision Tree Regressor
    - **Model:** `DecisionTreeRegressor`
    - **Purpose:** Predicts a continuous target variable. Similar to the classifier, but it splits data to minimize a regression criterion.
    - **Splitting Criteria:** Common criteria for regression:
        -   `criterion='squared_error'` (Mean Squared Error - MSE): Default.
        -   `criterion='friedman_mse'`: MSE with improvement score by Friedman.
        -   `criterion='absolute_error'` (Mean Absolute Error - MAE).
        -   `criterion='poisson'`: For modeling count data.
    - **Key Parameters:** Similar to `DecisionTreeClassifier` (`max_depth`, `min_samples_split`, etc.).
    - **Example (Predicting product review score (1-5) based on review length & sentiment score):**
        ```python
        from sklearn.tree import DecisionTreeRegressor
        import pandas as pd
        import numpy as np

        # Conceptual review data
        # Features: review_length_chars, sentiment_score_nlp (-1 to 1)
        # Target: review_rating (1 to 5)
        X_review_features = pd.DataFrame({
            'review_length_chars': np.random.randint(50, 1000, 100),
            'sentiment_score_nlp': np.random.uniform(-1, 1, 100)
        })
        y_review_rating = pd.Series(np.random.randint(1, 6, 100)) # Target: 1,2,3,4,5

        # X_train, X_test, y_train, y_test = train_test_split(X_review_features, y_review_rating, test_size=0.3, random_state=42)

        # dt_regressor = DecisionTreeRegressor(criterion='squared_error', max_depth=4, random_state=42)
        # dt_regressor.fit(X_train, y_train)
        
        # from sklearn.metrics import mean_squared_error
        # predictions = dt_regressor.predict(X_test)
        # mse = mean_squared_error(y_test, predictions)
        # print(f"Decision Tree Regressor MSE: {mse:.4f}")

        # Visualize the tree (can also be done for regressors)
        # plt.figure(figsize=(18,12))
        # plot_tree(dt_regressor, filled=True, feature_names=X_review_features.columns.tolist(), rounded=True, precision=2)
        # plt.show()
        ```

## Advantages of Decision Trees
-   **Interpretability:** Easy to understand and visualize. The decision rules are explicit.
-   **Handles Both Numerical and Categorical Data:** Can work with different data types, though Scikit-learn's implementation primarily handles numerical data (categorical data needs preprocessing like one-hot encoding).
-   **Non-parametric:** Makes no strong assumptions about the underlying data distribution.
-   **Feature Importance:** Can provide a measure of how important each feature is for making predictions. (`feature_importances_` attribute).
-   **Relatively Fast:** Training and prediction are generally fast.

## Disadvantages of Decision Trees
-   **[[Overfitting_Underfitting|Overfitting]]:** Decision trees can easily overfit the training data, creating complex trees that do not generalize well to unseen data. Pruning or setting constraints on tree growth (like `max_depth`, `min_samples_leaf`) is crucial.
-   **Instability:** Small variations in the data can lead to a completely different tree being generated. This is often mitigated by using trees within an [[Sklearn_Ensemble_Methods|ensemble]] (like Random Forests).
-   **Bias towards Features with More Levels:** For categorical features with many levels, information gain measures can be biased towards those features.
-   **Locally Optimal Decisions:** Trees make locally optimal decisions at each split, which may not lead to a globally optimal tree.
-   **Difficulty with Non-axis-parallel Boundaries:** Decision boundaries are always axis-parallel. They can struggle with diagonal relationships if not deep enough or if features are not transformed.

Decision trees are fundamental building blocks for more powerful [[Sklearn_Ensemble_Methods|ensemble methods]] like Random Forests and Gradient Boosting machines, which often overcome many of the individual tree's limitations.

---