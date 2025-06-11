---
tags:
  - python
  - scikit_learn
  - sklearn
  - machine_learning
  - linear_models
  - regression
  - classification
  - concept
  - example
aliases:
  - Scikit-learn Linear Models
  - sklearn.linear_model
related:
  - "[[160_Python_Libraries/Scikit_learn/_Scikit_learn_MOC|_Scikit_learn_MOC]]"
  - "[[Linear_Regression]]"
  - "[[Logistic_Regression]]"
  - "[[Regularization_ML|Regularization (L1, L2)]]"
worksheet:
  - WS_ML_Libraries_1
date_created: 2025-06-09
---
# Scikit-learn: Linear Models (`sklearn.linear_model`)

The `sklearn.linear_model` module in Scikit-learn implements a variety of linear models for both regression and classification tasks. These models assume a linear relationship between features and the output (or a transformation of the output).

## Key Linear Models

[list2tab|#Linear Models]
- Ordinary Least Squares (OLS) Regression
    - **Model:** `LinearRegression`
    - **Purpose:** Fits a linear model to minimize the residual sum of squares between the observed targets in the dataset, and the targets predicted by the linear approximation.
    - **Equation (simple):** $y = \beta_0 + \beta_1 x_1 + \dots + \beta_p x_p + \epsilon$
    - **Key Parameters:**
        - `fit_intercept`: Whether to calculate the intercept (default True).
        - `positive`: Forces coefficients to be positive (default False).
    - **Attributes:** `coef_` (coefficients $\beta_1, \dots, \beta_p$), `intercept_` ($\beta_0$).
    - **Example (Predicting product price based on features):**
        ```python
        from sklearn.linear_model import LinearRegression
        import numpy as np
        import pandas as pd

        # Conceptual product data: features (e.g., size, material_cost) and target (price)
        X_product_features = pd.DataFrame({
            'size_cm':,
            'material_cost': [5, 7, 6, 10, 5.5]
        })
        y_product_price = pd.Series()

        ols_model = LinearRegression()
        ols_model.fit(X_product_features, y_product_price)
        # print("OLS Coefficients:", ols_model.coef_)
        # print("OLS Intercept:", ols_model.intercept_)
        # predictions = ols_model.predict(X_product_features)
        ```
- Ridge Regression
    - **Model:** `Ridge`
    - **Purpose:** Linear least squares with L2 regularization. It adds a penalty equal to the square of the magnitude of coefficients ($\alpha \sum \beta_j^2$) to the loss function. This helps to shrink coefficients and reduce model complexity, preventing [[Overfitting_Underfitting|overfitting]].
    - **Key Parameters:**
        - `alpha`: Regularization strength (float, default 1.0). Larger alpha means stronger regularization.
    - **Example (Regularized price prediction):**
        ```python
        from sklearn.linear_model import Ridge
        # Using X_product_features, y_product_price from OLS example
        ridge_model = Ridge(alpha=1.0) # Alpha is the regularization strength
        # ridge_model.fit(X_product_features, y_product_price)
        # print("Ridge Coefficients:", ridge_model.coef_)
        # print("Ridge Intercept:", ridge_model.intercept_)
        ```
- Lasso Regression
    - **Model:** `Lasso`
    - **Purpose:** Linear Model trained with L1 prior as regularizer. It adds a penalty equal to the absolute value of the magnitude of coefficients ($\alpha \sum |\beta_j|$) to the loss function. This can lead to sparse models where some feature coefficients become exactly zero, effectively performing feature selection.
    - **Key Parameters:**
        - `alpha`: Regularization strength (float, default 1.0).
    - **Example (Price prediction with potential feature selection):**
        ```python
        from sklearn.linear_model import Lasso
        # Using X_product_features, y_product_price
        lasso_model = Lasso(alpha=0.1) # Smaller alpha for less aggressive feature removal
        # lasso_model.fit(X_product_features, y_product_price)
        # print("Lasso Coefficients:", lasso_model.coef_) # Some might be zero
        # print("Lasso Intercept:", lasso_model.intercept_)
        ```
- ElasticNet Regression
    - **Model:** `ElasticNet`
    - **Purpose:** A linear regression model trained with combined L1 and L2 priors as regularizer. It's a middle ground between Ridge and Lasso, useful when there are multiple correlated features.
    - **Penalty:** $\alpha \cdot \text{l1_ratio} \sum |\beta_j| + 0.5 \cdot \alpha \cdot (1 - \text{l1_ratio}) \sum \beta_j^2$
    - **Key Parameters:**
        - `alpha`: Constant that multiplies the penalty terms.
        - `l1_ratio`: The ElasticNet mixing parameter, with $0 \le \text{l1_ratio} \le 1$.
            - `l1_ratio = 0` is equivalent to Ridge.
            - `l1_ratio = 1` is equivalent to Lasso.
            - $0 < \text{l1_ratio} < 1$ combines L1 and L2.
    - **Example:**
        ```python
        from sklearn.linear_model import ElasticNet
        # Using X_product_features, y_product_price
        elastic_model = ElasticNet(alpha=0.1, l1_ratio=0.5)
        # elastic_model.fit(X_product_features, y_product_price)
        # print("ElasticNet Coefficients:", elastic_model.coef_)
        ```
- Logistic Regression
    - **Model:** `LogisticRegression`
    - **Purpose:** Linear model for [[Binary_Classification|binary classification]] (can be extended to multi-class). It models the probability of a binary outcome using the [[Sigmoid_Function|logistic (sigmoid) function]]. Despite its name, it's a classification algorithm.
    - **Key Parameters:**
        - `penalty`: `{'l1', 'l2', 'elasticnet', None}` (default 'l2'). Type of regularization.
        - `C`: Inverse of regularization strength (float, default 1.0). Smaller C means stronger regularization.
        - `solver`: Algorithm to use in the optimization problem (e.g., 'liblinear', 'lbfgs', 'saga'). Different solvers support different penalties.
        - `multi_class`: `{'auto', 'ovr', 'multinomial'}` (default 'auto'). For multi-class problems.
    - **Example (Predicting if a customer clicks an ad):**
        ```python
        from sklearn.linear_model import LogisticRegression
        from sklearn.model_selection import train_test_split
        import pandas as pd
        import numpy as np

        # Conceptual customer data: features and target (clicked_ad: 0 or 1)
        X_customer_features = pd.DataFrame(np.random.rand(100, 3), columns=['age', 'time_on_website', 'previous_purchases'])
        y_clicked_ad = pd.Series(np.random.randint(0, 2, 100))
        # X_train, X_test, y_train, y_test = train_test_split(X_customer_features, y_clicked_ad, test_size=0.3, random_state=42)

        logreg_model = LogisticRegression(solver='liblinear', C=1.0)
        # logreg_model.fit(X_train, y_train)
        # Probabilities for test set: logreg_model.predict_proba(X_test)
        # Predictions for test set: logreg_model.predict(X_test)
        # Accuracy: logreg_model.score(X_test, y_test)
        ```
- Perceptron
    - **Model:** `Perceptron`
    - **Purpose:** A simple algorithm for binary classification. It's a type of linear classifier, i.e., a classification algorithm that makes its predictions based on a linear predictor function combining a set of weights with the feature vector.
    - **Note:** Less commonly used directly now compared to Logistic Regression or SVMs for many tasks, but historically important.
- Stochastic Gradient Descent (SGD) based models
    - **Models:** `SGDClassifier`, `SGDRegressor`
    - **Purpose:** Implements linear classifiers (SVM, logistic regression, etc.) and regressors (linear regression, Huber regression, etc.) with stochastic gradient descent (SGD) learning. Efficient for large datasets (online learning).
    - **Key Parameters:** `loss` (e.g., 'hinge' for linear SVM, 'log_loss' for logistic regression, 'squared_error' for OLS), `penalty`, `alpha`.
    - **Example (`SGDClassifier` for product category prediction):**
        ```python
        from sklearn.linear_model import SGDClassifier
        from sklearn.preprocessing import StandardScaler
        import pandas as pd
        import numpy as np
        
        # Conceptual product data: features (e.g., description length, num_images) and target (category_id)
        # Assume X_prod_feats is numeric, y_prod_cat is integer category labels
        X_prod_feats = pd.DataFrame(np.random.rand(200, 4), columns=['desc_len', 'num_img', 'avg_word_len', 'price_scaled'])
        y_prod_cat = pd.Series(np.random.randint(0, 3, 200)) # 3 categories

        # Scaling is often important for SGD
        # scaler = StandardScaler()
        # X_scaled = scaler.fit_transform(X_prod_feats)

        sgd_clf = SGDClassifier(loss='hinge', penalty='l2', alpha=0.0001, max_iter=1000, tol=1e-3, random_state=42)
        # sgd_clf.fit(X_scaled, y_prod_cat)
        # predictions_sgd = sgd_clf.predict(scaler.transform(X_prod_feats.sample(5, random_state=1))) # Example prediction
        ```

## Common Characteristics
-   **Interpretability:** Coefficients ($\beta_j$) in linear models often have a direct interpretation (e.g., a one-unit increase in $x_j$ is associated with a $\beta_j$ change in $y$, holding other features constant).
-   **Efficiency:** Generally fast to train, especially compared to more complex models.
-   **Baseline Models:** Often serve as good baseline models to compare against more sophisticated approaches.
-   **Assumption of Linearity:** Their primary assumption is that the relationship between features and the target (or a transformation of it) is linear. If this assumption is violated, their performance may be poor.

Linear models are foundational in machine learning and provide a good starting point for many predictive modeling tasks.

---