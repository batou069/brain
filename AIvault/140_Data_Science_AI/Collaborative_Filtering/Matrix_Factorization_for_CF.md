---
tags:
  - data_science
  - collaborative_filtering
  - matrix_factorization
  - latent_factors
  - model
  - concept
aliases:
  - MF for CF
related:
  - "[[_Collaborative_Filtering_MOC]]"
  - "[[User-Item_Interaction_Matrix]]"
  - "[[Latent_Factors]]"
  - "[[Matrix_Factorization_vs_SVD_for_CF]]"
  - "[[Alternating_Least_Squares_ALS]]"
  - "[[Stochastic_Gradient_Descent_SGD_for_CF]]"
  - "[[L1_L2_Regularization]]"
  - "[[Loss_Function]]"
worksheet:
  - WS_Collaborative_Filtering_1
date_created: 2025-08-13
---
# Matrix Factorization for Collaborative Filtering

## Definition
**Matrix Factorization (MF)** is a class of models used in [[_Collaborative_Filtering_MOC|Collaborative Filtering]] that characterizes both users and items by vectors of [[Latent_Factors|latent factors]] inferred from user-item interaction patterns. The core idea is to decompose the large, sparse [[User-Item_Interaction_Matrix|user-item interaction matrix]] $\mathbf{R}$ into the product of two smaller, dense matrices: a user-factor matrix $\mathbf{P}$ and an item-factor matrix $\mathbf{Q}$.

- Let $\mathbf{R}$ be the $m \times n$ user-item matrix.
- We want to find:
    - $\mathbf{P}$, an $m \times k$ user-factor matrix.
    - $\mathbf{Q}$, an $n \times k$ item-factor matrix.
- such that their product approximates $\mathbf{R}$:
  $$ \mathbf{R} \approx \mathbf{P} \mathbf{Q}^T $$
  Here, $k$ is the number of latent factors, which is a hyperparameter and is typically much smaller than $m$ or $n$ ($k \ll m, n$).

## Intuition
- Each row $p_u$ in $\mathbf{P}$ is a $k$-dimensional vector representing user $u$.
- Each row $q_i$ in $\mathbf{Q}$ is a $k$-dimensional vector representing item $i$.
- The predicted rating $\hat{R}_{ui}$ that user $u$ would give to item $i$ is the dot product of their respective latent vectors:
  $$ \hat{R}_{ui} = p_u \cdot q_i = \sum_{f=1}^{k} P_{uf} Q_{if} $$
The goal of the learning process is to find the matrices $\mathbf{P}$ and $\mathbf{Q}$ that minimize the difference between the predicted ratings and the known ratings in $\mathbf{R}$.

[d2]
```d2
# Matrix Factorization for Collaborative Filtering
direction: right

# User-Factor Matrix P
P: {
  shape: sql_table
  "User Factors (P)": {
    style.bold: true
  }
  "m users": ""
  "...": ""
  "k factors": ""
}

# Multiplication Operator
op: "×" {
  shape: circle
  style.fill: "#f8f9fa"
  style.stroke: "#495057"
}

# Item-Factor Matrix Q^T
QT: {
  shape: sql_table
  "Item Factors (Qᵀ)": {
    style.bold: true
  }
  "k factors": ""
  "...": ""
  "n items": ""
}

# User-Item Matrix R
R: {
  shape: sql_table
  "User-Item Ratings (R)": {
    style.bold: true
  }
  "m users": ""
  "...": ""
  "n items": ""
}

# Prediction Cloud
prediction: {
  shape: cloud
  "Prediction for (user u, item i) is the dot product: r̂_ui = p_u ⋅ q_i"
}

# --- Connections ---
# P and QT are multiplied to approximate R
P -> op
QT -> op
op -> R: {
  label: "≈" # Approximates
  style.stroke-width: 2
}

# Prediction is derived from P and QT
P -> prediction: {style.stroke-dash: 2}
QT -> prediction: {style.stroke-dash: 2}
```

## Learning the Factors
The latent factors in $\mathbf{P}$ and $\mathbf{Q}$ are learned by minimizing a [[Loss_Function|loss function]]. For explicit feedback (ratings), this is typically the sum of squared errors on the known ratings, plus a regularization term.

- **Loss Function:**
  $$ L = \sum_{(u,i) \in K} (R_{ui} - p_u \cdot q_i)^2 + \lambda \left( \sum_u \|p_u\|^2 + \sum_i \|q_i\|^2 \right) $$
  - $K$: The set of $(u,i)$ pairs for which the rating $R_{ui}$ is known.
  - $\lambda$: The regularization parameter.
- **Optimization:** This loss function is typically minimized using algorithms like:
    - **[[Stochastic_Gradient_Descent_SGD_for_CF|Stochastic Gradient Descent (SGD)]]**
    - **[[Alternating_Least_Squares_ALS|Alternating Least Squares (ALS)]]**

## Key Questions & Considerations

>[!question] How do you decide on the size of the vector to represent a user/item?
>The size of the latent vector, $k$, is a crucial hyperparameter.
>- **Too small $k$:** The model may be too simple to capture the nuances of user preferences, leading to high bias and **[[Overfitting_Underfitting|underfitting]]**.
>- **Too large $k$:** The model may be too complex, learning noise instead of the signal, leading to high variance and **[[Overfitting_Underfitting|overfitting]]**. It also increases computational cost.
>
>The optimal value of $k$ is typically found through **hyperparameter tuning**. This involves:
>1.  Choosing a range of values for $k$ (e.g., 10, 20, 50, 100).
>2.  Training the MF model for each value of $k$.
>3.  Evaluating each model's performance on a validation set using a ranking metric like [[Normalized_Discounted_Cumulative_Gain_NDCG|NDCG]] or [[Mean_Reciprocal_Rank_MRR|MRR]].
>4.  Selecting the value of $k$ that yields the best performance on the validation set.

>[!question] Why/how is regularization important in this domain?
>Regularization is critical in matrix factorization for several reasons:
>1.  **Preventing Overfitting:** The user-item matrix is very sparse. Without regularization, the model can achieve zero error on the training data by learning extremely large factor values for the few known ratings. These large values will not generalize well to the unknown ratings, leading to poor recommendations.
>2.  **Handling Sparsity:** Regularization helps to "smooth out" the learned factors, making the model more robust and able to make reasonable predictions even for users or items with very few ratings.
>3.  **The Math:** The [[L1_L2_Regularization|L2 regularization]] term ($\lambda (\|p_u\|^2 + \|q_i\|^2)$) penalizes the magnitude of the latent vectors. This forces the model to find smaller, more generalizable factor values that explain the observed ratings without fitting to the noise.

>[!question] Would you use any of these methods if you had 10m items to recommend?
>Yes, absolutely. Matrix factorization methods are designed to be scalable and are one of the primary techniques used in large-scale industrial recommender systems with millions of users and items.
>- **Scalability:** Algorithms like [[Alternating_Least_Squares_ALS|ALS]] and [[Stochastic_Gradient_Descent_SGD_for_CF|SGD]] are well-suited for distributed computing frameworks like Apache Spark. They can process massive, sparse matrices efficiently.
>- **Efficiency:** Instead of dealing with a huge $m \times n$ matrix, the model only needs to store the dense $m \times k$ and $n \times k$ factor matrices. Since $k$ is small, this is much more memory-efficient.
>- **Prediction Speed:** Once the factors are learned, predicting a rating is just a dot product, which is very fast. For recommending the top N items, specialized libraries (e.g., Faiss, Annoy) can be used to perform efficient Approximate Nearest Neighbor searches in the latent factor space.

---