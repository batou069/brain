---
tags:
  - python
  - scikit_learn
  - sklearn
  - machine_learning
  - model_selection
  - cross_validation
  - hyperparameter_tuning
  - train_test_split
  - concept
  - example
aliases:
  - Scikit-learn Model Selection
  - Cross-Validation sklearn
  - Hyperparameter Tuning sklearn
  - Train-Test Split
related:
  - "[[160_Python_Libraries/Scikit_learn/_Scikit_learn_MOC|_Scikit_learn_MOC]]"
  - "[[Overfitting_Underfitting]]"
  - "[[Bias_Variance_Tradeoff]]"
  - "[[Model_Evaluation_Metrics]]"
worksheet:
  - WS_ML_Libraries_1
date_created: 2025-06-09
---
# Scikit-learn: Model Selection (`sklearn.model_selection`)

The `sklearn.model_selection` module in Scikit-learn provides essential tools for evaluating and selecting the best machine learning models and their parameters. This involves splitting data, performing cross-validation, and tuning hyperparameters.

## Key Tasks & Tools

[list2tab|#Model Selection Tools]
- Splitting Data
    - **Purpose:** To divide the dataset into training and testing (and optionally validation) sets. The model is trained on the training set and evaluated on the unseen test set to estimate its performance on new data and detect [[Overfitting_Underfitting|overfitting]].
    - **Tool:** **`train_test_split`**
    - **Key Parameters:**
        -   `arrays`: Sequence of indexables with same length / shape (e.g., X, y).
        -   `test_size`: Float (proportion of dataset for test split) or int (absolute number of test samples).
        -   `train_size`: Float or int (complementary to `test_size`).
        -   `random_state`: Seed for reproducibility.
        -   `shuffle`: Whether to shuffle data before splitting (default True).
        -   `stratify`: Array-like, if not None, data is split in a stratified fashion, using this as class labels (ensures proportional representation of classes in train/test splits, useful for imbalanced datasets).
    - **Example:**
        ```python
        from sklearn.model_selection import train_test_split
        import numpy as np
        import pandas as pd

        # Conceptual e-commerce data: features and target (e.g., predict if a customer will purchase)
        # Assume X_features has product views, time_on_site, etc.
        # Assume y_target is 0 (no purchase) or 1 (purchase)
        X_features = pd.DataFrame(np.random.rand(100, 5), columns=[f'feat_{i}' for i in range(5)])
        y_target = pd.Series(np.random.randint(0, 2, 100))

        X_train, X_test, y_train, y_test = train_test_split(
            X_features, y_target, test_size=0.25, random_state=42, stratify=y_target
        )
        # print("X_train shape:", X_train.shape)
        # print("X_test shape:", X_test.shape)
        # print("y_train shape:", y_train.shape)
        # print("y_test shape:", y_test.shape)
        # print("\nProportion of target in y_train:\n", y_train.value_counts(normalize=True))
        # print("\nProportion of target in y_test:\n", y_test.value_counts(normalize=True))
        ```
- Cross-Validation (CV)
    - **Purpose:** A more robust method for estimating model performance than a single train-test split. It involves splitting the training data into multiple "folds," training the model on some folds, and validating it on the remaining fold, then averaging the performance across all folds. This helps in getting a more stable estimate of how the model will perform on unseen data and reduces variance in the performance estimate.
    - **Tools:**
        -   **`KFold`**: Basic K-fold cross-validation. Divides data into K consecutive folds.
        -   **`StratifiedKFold`**: K-fold variant that preserves the percentage of samples for each class (useful for classification with imbalanced classes).
        -   **`RepeatedKFold` / `RepeatedStratifiedKFold`**: Repeats K-Fold CV multiple times with different randomizations in each repetition.
        -   **`LeaveOneOut` (LOOCV)**: Each sample is used once as a test set while the remaining samples form the training set. Computationally expensive for large datasets.
        -   **`LeavePOut` (LPO)**: Leaves P samples out for testing.
        -   **`GroupKFold`**: Ensures that the same group of samples is not represented in both testing and training sets (e.g., if data has groups like patients, ensure all data from one patient is in either train or test, not split).
        -   **`cross_val_score`**: A helper function to evaluate a model using a CV strategy and a scoring metric.
        -   **`cross_validate`**: Similar to `cross_val_score` but allows specifying multiple metrics and returns fit times, score times, and test scores.
    - **Example (`cross_val_score` with `KFold`):**
        ```python
        from sklearn.model_selection import KFold, cross_val_score
        from sklearn.linear_model import LogisticRegression # Example model
        import numpy as np
        import pandas as pd

        # Using X_features, y_target from previous example
        X_features = pd.DataFrame(np.random.rand(100, 5), columns=[f'feat_{i}' for i in range(5)])
        y_target = pd.Series(np.random.randint(0, 2, 100))
        
        model = LogisticRegression(solver='liblinear')
        # Define the cross-validation strategy
        kfold_cv = KFold(n_splits=5, shuffle=True, random_state=42)
        
        # Perform cross-validation
        # 'accuracy' is one of many possible scoring metrics
        scores = cross_val_score(model, X_features, y_target, cv=kfold_cv, scoring='accuracy')
        # print("Cross-validation scores (accuracy per fold):", scores)
        # print(f"Mean CV accuracy: {scores.mean():.4f} (+/- {scores.std() * 2:.4f})")
        ```
- Hyperparameter Tuning
    - **Purpose:** Finding the optimal combination of hyperparameters for a machine learning model to achieve the best performance on unseen data. Hyperparameters are parameters set *before* the learning process begins (e.g., `C` in SVM, `n_estimators` in Random Forest).
    - **Tools:**
        -   **`GridSearchCV`**: Exhaustively searches over a specified parameter grid. Trains and evaluates the model for every combination of hyperparameters using cross-validation.
        -   **`RandomizedSearchCV`**: Samples a fixed number of parameter settings from specified distributions. Can be more efficient than GridSearchCV when the search space is large.
        -   Specialized tools for Bayesian optimization or other advanced techniques (e.g., `scikit-optimize`, `Optuna`, `Hyperopt`).
    - **Example (`GridSearchCV`):**
        ```python
        from sklearn.model_selection import GridSearchCV
        from sklearn.ensemble import RandomForestClassifier
        import numpy as np
        import pandas as pd

        # Using X_train, y_train from train_test_split example
        X_train = pd.DataFrame(np.random.rand(75, 5), columns=[f'feat_{i}' for i in range(5)]) # 75 samples for train
        y_train = pd.Series(np.random.randint(0, 2, 75))

        # Define the model
        rf_model = RandomForestClassifier(random_state=42)
        
        # Define the parameter grid to search
        param_grid = {
            'n_estimators': [50, 100, 150],
            'max_depth': [None, 10, 20, 30],
            'min_samples_split': [2, 5, 10]
        }
        
        # Set up GridSearchCV
        # cv=3 means 3-fold cross-validation for each parameter combination
        grid_search = GridSearchCV(estimator=rf_model, param_grid=param_grid,
                                   cv=3, scoring='accuracy', verbose=0, n_jobs=-1) # n_jobs=-1 uses all processors
        
        # Fit GridSearchCV to the training data
        # grid_search.fit(X_train, y_train)
        
        # Best parameters and best score
        # print("Best parameters found:", grid_search.best_params_)
        # print(f"Best cross-validation accuracy: {grid_search.best_score_:.4f}")
        
        # The best_estimator_ attribute holds the model trained with the best parameters
        # best_rf_model = grid_search.best_estimator_
        ```
- Plotting Learning and Validation Curves
    - **Purpose:** To diagnose model performance, such as [[Overfitting_Underfitting|overfitting]] or [[Bias_Variance_Tradeoff|underfitting]], or to see how performance changes with dataset size or a hyperparameter.
    - **Tools:**
        -   **`learning_curve`**: Generates scores for different training set sizes to assess if the model benefits from more data.
        -   **`validation_curve`**: Generates scores for different values of a single hyperparameter to see its impact.
    - **Example (`learning_curve`):**
        ```python
        from sklearn.model_selection import learning_curve
        from sklearn.linear_model import LogisticRegression
        import numpy as np
        import matplotlib.pyplot as plt
        import pandas as pd

        X_features = pd.DataFrame(np.random.rand(100, 5), columns=[f'feat_{i}' for i in range(5)])
        y_target = pd.Series(np.random.randint(0, 2, 100))
        model = LogisticRegression(solver='liblinear')

        train_sizes, train_scores, validation_scores = learning_curve(
            estimator=model,
            X=X_features,
            y=y_target,
            train_sizes=np.linspace(0.1, 1.0, 10), # 10 steps from 10% to 100% of training data
            cv=5, # 5-fold cross-validation
            scoring='accuracy',
            n_jobs=-1
        )

        # Calculate mean and standard deviation for plotting
        # train_scores_mean = np.mean(train_scores, axis=1)
        # validation_scores_mean = np.mean(validation_scores, axis=1)

        # Plot learning curve (conceptual, actual plotting code omitted for brevity here)
        # plt.figure()
        # plt.plot(train_sizes, train_scores_mean, 'o-', color="r", label="Training score")
        # plt.plot(train_sizes, validation_scores_mean, 'o-', color="g", label="Cross-validation score")
        # plt.title("Learning Curve")
        # plt.xlabel("Training examples")
        # plt.ylabel("Accuracy Score")
        # plt.legend(loc="best")
        # plt.grid()
        # plt.show()
        ```

These model selection tools are essential for building robust machine learning models that generalize well to new, unseen data.

---