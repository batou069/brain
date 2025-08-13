# Input

New Worksheet, new chapter: "Collaborative Filtering" in context of our project of "Movie recommendation system" which we built the infrastructure for, based on the movielens100k data set

you are provided with a worksheet filled with keywords and questions.

For the following keywords , provide answers in bullet point format and the following answers if applicable.

1) Short Description/what is it/one-sentence
2) What is it good for? Why is it done?
3) 3-5 bullet points with more details, dont just stretch sentences, actually inject more information
4) Examples, can be conceptual, analogy, or (preferred) real python code, if possible both a ready  implementation by a library like sklearn, and a from-scratch version.
5) If possible some math, using Latex and explanations. It should explain how it works, why it works, etc
6) if applicaple a mermaid diagram/graph compliant with obsidians mermaid version: no spaces in names, dont get too crazy with styling, keep it minimal and functional 
7) If you mention any new term that is not part of the worksheet (like a specific type of a high-level keyword - for example keyword is optimization and your answer mentions 2 examples for optimization techniques), then make a seperate "chapter" for that new keyword in the same format (point 1-5) - never mention something datascience related or machine learning related without properly explaining it

IMPORTANT: The output will be copied into obsidian, therefore your answer should be markdown inside a 4-backtick codeblock, such that following embedded 3tick codeblocks won't be disturbed

For the questions, provide a short answer and a long answer

```
# Keywords

1. Matrix Factorization
2. Singular Value Decomposition
3. Latent vectors
4. Alternating Least Squares
5. Implicit vs. explicit feedback
6. Cold start problem
7. Normalized Discounted Cumulative Gain
8. Mean Reciprocal Rank
9. Concept Drift

# Questions

1. When would you prefer to use ALS rather than SGD?
2. When would you move users from the “cold start" group to the "I know you" group?
3. Are there material differences when using MF vs. SVD for the use case of CF?
4. Does MF work better for binary data rather than, i.e. 1-10 score a user ranked an item?
5. How do you decide on the size of the vector to represent a user/item?
6. What can you do if you want to incorporate additional data to the model? e.g. movie length, is it technicolor, or did Sean Connery appear in it?
7. How would adding a row/column of zeros (user/item cold start) affect MF?
8. Would you use any of these methods if you had 10m items to recommend?
9. Why/how is regularization important in this domain?
10. Are the latent vectors meaningful in any way?
11. How would you decide on the retraining schedule for your model?
```

---

# Output
## Chapter: Collaborative Filtering

### Keywords

#### 1. Matrix Factorization
1.  **Short Description:** Matrix Factorization (MF) is a class of collaborative filtering algorithms that decomposes a large user-item interaction matrix into two smaller, lower-dimensional matrices representing latent user and item features.
2.  **What is it good for?** It's excellent at finding latent (hidden) features that explain the observed user-item interactions (like movie ratings), enabling the prediction of missing ratings and thus, generating personalized recommendations. It's also computationally efficient and scalable for sparse matrices, which are common in recommendation scenarios.
3.  **Details:**
    * The core idea is that user preferences can be modeled by a small number of hidden factors. For movies, these could be genres, actor preferences, director styles, or more abstract concepts the model learns on its own.
    * The two resulting matrices are the "user-feature matrix" (P) and the "item-feature matrix" (Q). Matrix P has a row for each user and k columns for the latent features. Matrix Q has a row for each item and k columns for the same latent features.
    * To predict a user's rating for an item, you compute the dot product of that user's vector from P and that item's vector from Q.
    * The process of finding P and Q is an optimization problem: we want to find matrices P and Q such that their product, P @ Q.T, is as close as possible to the original ratings matrix R for the known ratings.
4.  **Examples:**
    * **Analogy:** Imagine you have a grid of people's ratings for different foods. Matrix factorization is like discovering that the underlying factors driving these ratings are "sweetness" and "spiciness". It then gives each person a score for how much they like sweetness vs. spiciness, and each food a score for how sweet and spicy it is. To predict if someone will like a new food, you just see how well their preferences align with the food's characteristics.
    * **Python (Library - `scikit-learn` using `TruncatedSVD` as a proxy):**
        ```python
        import numpy as np
        from sklearn.decomposition import TruncatedSVD

        # User-Item Matrix (Users x Movies), 0 means not rated
        R = np.array([
            [5, 3, 0, 1],
            [4, 0, 0, 1],
            [1, 1, 0, 5],
            [1, 0, 0, 4],
            [0, 1, 5, 4],
        ])

        # Use TruncatedSVD which works on sparse matrices
        # n_components is the number of latent factors (k)
        svd = TruncatedSVD(n_components=2, random_state=42)
        
        # Factorize the matrix
        user_features = svd.fit_transform(R) # This is our P matrix
        item_features = svd.components_      # This is our Q matrix

        # Predict all ratings (including the ones we already know)
        predicted_ratings = np.dot(user_features, item_features)

        print("Original Matrix R:\n", R)
        print("\nPredicted Matrix (P @ Q):\n", predicted_ratings)
        # To get the prediction for User 1, Movie 3 (index 2):
        print("\nPredicted rating for User 1, Movie 3:", predicted_ratings[0, 2])
        ```
    * **Python (From Scratch - using Gradient Descent):**
        ```python
        import numpy as np

        def matrix_factorization_sgd(R, k, learning_rate=0.01, epochs=100, lmbda=0.1):
            num_users, num_items = R.shape
            
            # Initialize user and item latent feature matrices with random values
            P = np.random.rand(num_users, k)
            Q = np.random.rand(num_items, k)
            
            # Get the indices of the non-zero ratings
            users, items = R.nonzero()
            
            for epoch in range(epochs):
                for u, i in zip(users, items):
                    # Prediction error
                    error = R[u, i] - np.dot(P[u, :], Q[i, :])
                    
                    # Update user and item vectors
                    # The update includes a regularization term (lmbda)
                    P[u, :] += learning_rate * (error * Q[i, :] - lmbda * P[u, :])
                    Q[i, :] += learning_rate * (error * P[u, :] - lmbda * Q[i, :])
            
            return P, Q.T

        R = np.array([
            [5, 3, 0, 1],
            [4, 0, 0, 1],
            [1, 1, 0, 5],
            [1, 0, 0, 4],
            [0, 1, 5, 4],
        ])

        P, Q_T = matrix_factorization_sgd(R, k=2)
        predicted_ratings_scratch = np.dot(P, Q_T)
        print("Predicted Matrix from scratch:\n", predicted_ratings_scratch)
        ```

5.  **Math:**
    The goal is to find P and Q that minimize a **loss function**, typically the sum of squared errors on the known ratings. To prevent overfitting, a **regularization** term is added.
    The objective function to minimize is:
    $$ \mathcal{L} = \sum_{(u, i) \in K} (r_{ui} - \mathbf{p}_u^T \mathbf{q}_i)^2 + \lambda (\sum_u ||\mathbf{p}_u||^2 + \sum_i ||\mathbf{q}_i||^2) $$
    * $K$: The set of (u, i) pairs for which the rating $r_{ui}$ is known.
    * $r_{ui}$: The actual rating of user *u* for item *i*.
    * $\mathbf{p}_u$: The latent vector for user *u* (a row in P).
    * $\mathbf{q}_i$: The latent vector for item *i* (a row in Q, so its transpose is a column in $Q^T$).
    * $\mathbf{p}_u^T \mathbf{q}_i$: The predicted rating for user *u* on item *i*.
    * $\lambda$: The regularization parameter, which controls the trade-off between fitting the training data and keeping the model parameters small to generalize better.
    * $||\mathbf{p}_u||^2$ and $||\mathbf{q}_i||^2$: The squared L2 norm (magnitude) of the latent vectors, used for regularization.

---

#### 2. Singular Value Decomposition
1.  **Short Description:** Singular Value Decomposition (SVD) is a fundamental matrix decomposition technique from linear algebra that factors any matrix A into three distinct matrices: $U \Sigma V^T$.
2.  **What is it good for?** In its pure form, SVD is a powerful tool for dimensionality reduction, data compression, and identifying the most significant components in a dataset. In the context of CF, it's the theoretical foundation for matrix factorization, but it cannot be applied directly to recommendation matrices because of their missing values (sparsity).
3.  **Details:**
    * SVD works on a dense matrix (no missing values). To use it for recommendations, you would first have to impute the missing ratings (e.g., fill with the mean), which is often inaccurate and computationally expensive for large matrices.
    * The matrices are:
        * **U**: The left singular vectors (user-space), an orthogonal matrix.
        * **$\Sigma$**: A diagonal matrix of singular values, ordered by magnitude. These values represent the "importance" of each latent dimension.
        * **$V^T$**: The transpose of the right singular vectors (item-space), also an orthogonal matrix.
    * By keeping only the top *k* singular values in $\Sigma$ (and the corresponding columns in U and V), you get a "Truncated SVD", which is the best rank-*k* approximation of the original matrix in terms of Frobenius norm. This is the core idea behind its use for dimensionality reduction.
    * The models used in practice (like Funk SVD or those using ALS/SGD) are *inspired* by SVD but are not mathematically identical. They are designed to work directly on the sparse matrix of known ratings.
4.  **Examples:**
    * **Conceptual:** Think of SVD as finding the "best axes" to view your data. For a cloud of data points, the first singular vector ($v_1$) points in the direction of the greatest variance. The second ($v_2$) points in the direction of the next greatest variance, orthogonal to the first, and so on. The singular values ($\sigma_i$) tell you *how much* variance is captured by each axis.
    * **Python (Library - `numpy`):**
        ```python
        import numpy as np
        
        # SVD requires a dense matrix, so we'll fill zeros with the mean rating
        R = np.array([
            [5, 3, 1, 1],
            [4, 1, 2, 1],
            [1, 1, 3, 5],
            [1, 2, 4, 4],
            [2, 1, 5, 4],
        ], dtype=float)
        
        # Decompose the matrix
        U, sigma, VT = np.linalg.svd(R)
        
        # sigma is a 1D array of singular values, we need to make it a diagonal matrix
        # with the correct dimensions for reconstruction
        num_users, num_items = R.shape
        Sigma = np.zeros((num_users, num_items))
        Sigma[:R.shape[1], :R.shape[1]] = np.diag(sigma)
        
        
        # Reconstruct the original matrix
        R_reconstructed = U @ Sigma @ VT
        
        print("Original Matrix R:\n", R)
        print("\nReconstructed Matrix U @ Sigma @ VT:\n", np.round(R_reconstructed, 2))
        
        # To get a rank-2 approximation (dimensionality reduction)
        k = 2
        U_k = U[:, :k]
        Sigma_k = np.diag(sigma[:k])
        VT_k = VT[:k, :]
        R_approx_k = U_k @ Sigma_k @ VT_k
        print("\nRank-2 Approximation of R:\n", np.round(R_approx_k, 2))
        ```
5.  **Math:**
    Any real matrix $A$ of size $m \times n$ can be factored as:
    $$ A = U \Sigma V^T $$
    * $U$: An $m \times m$ orthogonal matrix. Its columns are the left-singular vectors.
    * $\Sigma$: An $m \times n$ diagonal matrix. The diagonal entries $\sigma_1, \sigma_2, \dots$ are the singular values of $A$, and are non-negative.
    * $V^T$: The transpose of an $n \times n$ orthogonal matrix $V$. The columns of $V$ (rows of $V^T$) are the right-singular vectors.
    * **Orthogonal Matrix Property:** $U^T U = I$ and $V^T V = I$.

6.  **Mermaid Diagram:**
    ```mermaid
    graph TD;
        A[Matrix A m x n] -->|Decomposes into| U[U m x m];
        A -->|Decomposes into| S[Sigma m x n <br> Diagonal];
        A -->|Decomposes into| VT[V_T n x n];
        U -->|Multiplied by| S;
        S -->|Multiplied by| VT;
        VT -->|Reconstructs| A_approx[Approximation of A];
    ```

---

#### 3. Latent vectors
1.  **Short Description:** Latent vectors (or feature vectors) are lower-dimensional representations of users and items that capture their underlying, unobserved characteristics.
2.  **What is it good for?** They form the core of matrix factorization models by embedding complex entities (users and items) into a shared, continuous vector space. In this space, the proximity or alignment of a user's vector and an item's vector can be used to predict affinity (e.g., a rating).
3.  **Details:**
    * The "latent" part means these features are not given to the model but are learned automatically from the patterns in the rating data.
    * The dimensionality of these vectors (often denoted by *k*) is a hyperparameter. A small *k* might not capture enough detail, while a large *k* can lead to overfitting and be computationally expensive.
    * For a movie recommendation system, a latent vector for a movie might encode dimensions corresponding to "is it a blockbuster?", "how serious is it?", "is it for kids?". A user's vector would encode their preference along these same dimensions.
    * The model doesn't know the human-interpretable meaning of these dimensions. Dimension 1 might be "blockbuster-ness" or it might be a complex combination of genre, director style, and era that we can't easily name.
4.  **Examples:**
    * **Conceptual:**
        * User A's vector: `[0.9, 0.1]` (Loves action, dislikes romance)
        * Movie X (Die Hard) vector: `[0.8, 0.2]` (High on action, low on romance)
        * Movie Y (Titanic) vector: `[0.3, 0.9]` (Low on action, high on romance)
        * Prediction for User A, Movie X: `0.9*0.8 + 0.1*0.2 = 0.72 + 0.02 = 0.74` (High affinity)
        * Prediction for User A, Movie Y: `0.9*0.3 + 0.1*0.9 = 0.27 + 0.09 = 0.36` (Low affinity)
    * **Python:** The latent vectors are the matrices `P` and `Q` (or `user_features` and `item_features`) from the Matrix Factorization examples above.
        ```python
        # Using the from-scratch MF example
        # P is the matrix of user latent vectors
        # Q_T is the matrix of item latent vectors (transposed)
        user_1_latent_vector = P[0, :]
        item_1_latent_vector = Q_T[:, 0]
        
        print("User 1's Latent Vector:", user_1_latent_vector)
        print("Item 1's Latent Vector:", item_1_latent_vector)
        
        # The predicted rating is their dot product
        predicted_rating = np.dot(user_1_latent_vector, item_1_latent_vector)
        print("Predicted Rating:", predicted_rating)
        ```
5.  **Math:**
    In the matrix factorization model, for a user *u* and item *i*, their latent vectors are $\mathbf{p}_u \in \mathbb{R}^k$ and $\mathbf{q}_i \in \mathbb{R}^k$. The predicted rating $\hat{r}_{ui}$ is simply their dot product:
    $$ \hat{r}_{ui} = \mathbf{p}_u^T \mathbf{q}_i = \sum_{j=1}^{k} p_{uj} \cdot q_{ij} $$
    This formula shows how the individual components of the user's preference vector ($p_{uj}$) align with the components of the item's characteristic vector ($q_{ij}$), and their sum forms the final prediction.

---

#### 4. Alternating Least Squares
1.  **Short Description:** Alternating Least Squares (ALS) is an iterative optimization technique used to solve matrix factorization problems by fixing one of the latent matrices (e.g., user features) and solving for the other, then alternating back and forth.
2.  **What is it good for?** ALS is particularly effective for working with implicit feedback datasets and can be easily parallelized, making it highly scalable for large-scale recommendation systems (it's a key component in systems like Apache Spark's MLlib).
3.  **Details:**
    * The core challenge of the MF objective function is that it's not convex when solving for P and Q simultaneously. However, if you hold P constant, the problem of solving for Q becomes a standard least squares problem (and vice versa).
    * The "alternating" process is:
        1.  Initialize P and Q with random values.
        2.  **Fix P**, solve for Q by minimizing the loss function.
        3.  **Fix Q**, solve for P by minimizing the loss function.
        4.  Repeat steps 2 and 3 until the solution converges (or for a fixed number of iterations).
    * Because the updates for each user (or item) are independent of each other when the other matrix is fixed, the calculations can be distributed across multiple machines, which is why it's great for parallel computing.
4.  **Examples:**
    * **Python (Library - `implicit`):** The `implicit` library is purpose-built for this.
        ```python
        # pip install implicit
        import numpy as np
        import scipy.sparse as sparse
        from implicit.als import AlternatingLeastSquares

        # Use a sparse matrix for implicit feedback (1 for interaction, 0 for none)
        R_implicit = np.array([
            [1, 1, 0, 1],
            [1, 0, 0, 1],
            [0, 1, 0, 1],
            [0, 0, 0, 1],
            [0, 1, 1, 1],
        ])
        R_sparse = sparse.csr_matrix(R_implicit)

        # Initialize the model
        # factors = number of latent features (k)
        model = AlternatingLeastSquares(factors=3, regularization=0.1, iterations=50)

        # Train the model
        model.fit(R_sparse)

        # Get the latent vectors
        user_factors = model.user_factors
        item_factors = model.item_factors
        
        # Get recommendations for a user (e.g., user 0)
        user_id = 0
        recommendations = model.recommend(user_id, R_sparse[user_id])
        print(f"Recommendations for user {user_id}: {recommendations}")
        ```
5.  **Math:**
    The process alternates between two steps.
    1.  **Solve for user vectors $\mathbf{p}_u$ (given Q is fixed):**
        For each user *u*, we want to find the vector $\mathbf{p}_u$ that minimizes the error for all items *i* they have rated. The equation for a single user *u* is:
        $$ \frac{\partial \mathcal{L}}{\partial \mathbf{p}_u} = -2 \sum_{i \in I_u} (r_{ui} - \mathbf{p}_u^T \mathbf{q}_i)\mathbf{q}_i + 2\lambda \mathbf{p}_u = 0 $$
        Solving for $\mathbf{p}_u$ gives a closed-form solution:
        $$ \mathbf{p}_u = (\sum_{i \in I_u} \mathbf{q}_i \mathbf{q}_i^T + \lambda I)^{-1} (\sum_{i \in I_u} r_{ui} \mathbf{q}_i) $$
        Where $I_u$ is the set of items rated by user *u*, and *I* is the identity matrix.

    2.  **Solve for item vectors $\mathbf{q}_i$ (given P is fixed):**
        Similarly, for each item *i*, we solve for $\mathbf{q}_i$:
        $$ \mathbf{q}_i = (\sum_{u \in U_i} \mathbf{p}_u \mathbf{p}_u^T + \lambda I)^{-1} (\sum_{u \in U_i} r_{ui} \mathbf{p}_u) $$
        Where $U_i$ is the set of users who rated item *i*.

6.  **Mermaid Diagram:**
    ```mermaid
    graph TD;
        Start --> Init[Initialize P and Q randomly];
        Init --> Loop{Repeat N times};
        Loop --> FixP[Fix P, Solve for Q <br> using least squares];
        FixP --> FixQ[Fix Q, Solve for P <br> using least squares];
        FixQ --> Loop;
        Loop --> End[Converged P and Q];
    ```

---

#### 5. Implicit vs. Explicit Feedback
1.  **Short Description:** Explicit feedback is direct, quantitative user input (e.g., a 1-5 star rating), while implicit feedback is indirect evidence of user interest derived from their behavior (e.g., clicks, views, purchases).
2.  **What is it good for?** Understanding this distinction is crucial for choosing the right modeling approach. Explicit feedback is rich in information but often sparse, while implicit feedback is abundant but noisy and lacks negative sentiment.
3.  **Details:**
    * **Explicit Feedback:**
        * Examples: Movie ratings (1-5 stars), product reviews (1-10 score).
        * Pros: High-quality signal of user preference. Clearly indicates positive and negative opinions.
        * Cons: Users often don't provide it, leading to very sparse data.
    * **Implicit Feedback:**
        * Examples: Watching a movie, adding an item to a cart, time spent on a page, number of times a song is played.
        * Pros: Plentiful and easy to collect without requiring extra user effort.
        * Cons: Noisy. A user might click an item by mistake. Crucially, it only provides positive signals; the absence of an interaction is not a confirmed sign of dislike (the user might not have seen the item).
    * Modeling approaches differ. For explicit feedback, you predict the rating value itself (a regression problem). For implicit feedback, you often model the *confidence* that a user likes an item, treating all interactions as positive examples and unobserved items as a mix of negative and unknown examples. ALS is particularly well-suited for this.
4.  **Examples:**
    * **Explicit:** The MovieLens 100k dataset, where users give movies a rating from 1 to 5.
    * **Implicit:** A dataset from an e-commerce site where the data is a log of `(user_id, item_id, timestamp)` for every time a user viewed a product page.
    * **Modeling Implicit Data:** You might create a matrix where a `1` means the user interacted with the item and `0` means they didn't. When modeling, you assign a higher confidence to the `1`s than the `0`s. The model's goal becomes distinguishing between the `1`s and `0`s, essentially a ranking problem.

---

#### 6. Cold Start Problem
1.  **Short Description:** The cold start problem refers to the difficulty of making accurate recommendations for new users or new items that have little to no interaction history.
2.  **What is it good for?** Addressing the cold start problem is critical for the practical success of a recommendation system, as new users and new items are constantly being added. A system that can't handle them will fail to engage new users and promote new content.
3.  **Details:**
    * **New User Cold Start:** A new user has not rated any items, so a collaborative filtering model has no data to compare their tastes to others.
    * **New Item Cold Start:** A new item has not been rated by any users, so the model doesn't know how to recommend it or who might like it.
    * **Common Solutions:**
        * **Content-Based Filtering:** Recommend items based on their attributes (e.g., for a new movie, use its genre, director, actors) and a user's profile.
        * **Hybrid Approaches:** Combine collaborative filtering with content-based methods. For a new user, you might start with a content-based approach (e.g., ask them to select genres they like) and gradually transition to CF as they provide more ratings.
        * **Popularity-Based:** Recommend the most popular items to new users as a safe default.
        * **User Onboarding:** Actively prompt new users to rate a few well-known items to quickly build an initial profile.
4.  **Examples:**
    * **New User:** You sign up for Netflix. It has no idea what you like. It asks you to pick 3 movies you've enjoyed. This is an onboarding process to mitigate the cold start problem.
    * **New Item:** A new movie is added to the catalog. The system can initially recommend it to users who have liked other movies by the same director or with the same lead actor.

---

#### 7. Normalized Discounted Cumulative Gain (NDCG)
1.  **Short Description:** NDCG is a ranking metric that evaluates the quality of a recommended list by giving more weight to highly-ranked, relevant items.
2.  **What is it good for?** It is one of the most popular and robust offline metrics for evaluating recommendation systems because it considers both the relevance of the recommended items (the "gain") and their position in the list (the "discount").
3.  **Details:**
    * **Cumulative Gain (CG):** The sum of the relevance scores of the items in the recommended list. It doesn't care about the order.
    * **Discounted Cumulative Gain (DCG):** An improvement on CG. It penalizes relevant items that are ranked lower in the list by applying a logarithmic discount. The idea is that a user is less likely to see items further down the list.
    * **Normalized DCG (NDCG):** An improvement on DCG. It normalizes the DCG score by the score of the *ideal* ranking (IDCG), which is the best possible DCG for that user. This makes the score fall between 0 and 1, allowing for fair comparison across different users and queries.
4.  **Examples:**
    * **Python (From Scratch):**
        ```python
        import numpy as np

        def ndcg_at_k(true_relevance, predicted_scores, k):
            # Create a list of (score, relevance) and sort by score
            recommendations = sorted(zip(predicted_scores, true_relevance), key=lambda x: x[0], reverse=True)
            
            # Get the relevance of the top-k recommended items
            rec_relevance = [rel for score, rel in recommendations[:k]]
            
            # Calculate DCG
            dcg = rec_relevance[0] + np.sum(rec_relevance[1:] / np.log2(np.arange(2, len(rec_relevance) + 1)))
            
            # Calculate IDCG (ideal ranking)
            ideal_relevance = sorted(true_relevance, reverse=True)
            idcg = ideal_relevance[0] + np.sum(ideal_relevance[1:k] / np.log2(np.arange(2, len(ideal_relevance[:k]) + 1)))
            
            if not idcg:
                return 0.0
            
            return dcg / idcg

        # Example: User rated 5 movies. We recommend 3.
        # True relevance scores (e.g., actual ratings 1-5)
        true_ratings = [5, 2, 3, 1, 4] 
        # Our model's predicted scores for these 5 movies
        model_scores = [0.9, 0.8, 0.7, 0.6, 0.5]

        # Let's say we recommend the top 3 based on model_scores
        # The true ratings of our top 3 recommendations are [5, 2, 3]
        
        ndcg_score = ndcg_at_k(true_ratings, model_scores, k=3)
        print(f"NDCG@3 Score: {ndcg_score:.4f}")
        ```

5.  **Math:**

The formula for NDCG at position *k* is:
$$ \text{NDCG}_k = \frac{\text{DCG}_k}{\text{IDCG}_k} $$
Where:
$$ \text{DCG}_k = \sum_{i=1}^{k} \frac{rel_i}{\log_2(i+1)} $$
* $rel_i$: The relevance of the item at position *i* in the recommended list.
* $\text{IDCG}_k$ is the DCG score of the perfect ranking (i.e., sorting all relevant items by their true relevance and calculating DCG for that list).

---

#### 8. Mean Reciprocal Rank (MRR)
1.  **Short Description:** MRR is a ranking metric that evaluates a system based on the rank of the *first* correct or relevant item in a list of recommendations.
2.  **What is it good for?** MRR is useful when you care most about getting just one good recommendation to the user quickly (e.g., "customers who bought this also bought..." on a product page, or a search engine answering a specific question). It's simple and easy to interpret.
3.  **Details:**
    * For a single query or user, the Reciprocal Rank is $\frac{1}{\text{rank}}$, where "rank" is the position of the first relevant item. If no relevant item is found in the list, the score is 0.
    * The MRR is the average of the Reciprocal Ranks across all users or queries in your test set.
    * It heavily rewards systems that place a correct item at the very top of the list.
    * It's less informative than NDCG if you care about the overall quality and diversity of the entire list, as it completely ignores all items after the first relevant one.
4.  **Examples:**
    * **Conceptual:**
        * User 1: First relevant movie is at rank 2. Score = 1/2.
        * User 2: First relevant movie is at rank 1. Score = 1/1.
        * User 3: First relevant movie is at rank 5. Score = 1/5.
        * MRR = `(1/2 + 1/1 + 1/5) / 3 = (0.5 + 1.0 + 0.2) / 3 = 1.7 / 3 = 0.567`
    * **Python (From Scratch):**
        ```python
        def calculate_mrr(recommendations_list):
            """
            recommendations_list: A list of lists. Each inner list is a user's
                                  recommendation, with 1 for relevant, 0 for not.
            """
            reciprocal_ranks = []
            for user_recs in recommendations_list:
                for i, item_relevance in enumerate(user_recs):
                    if item_relevance == 1:
                        reciprocal_ranks.append(1 / (i + 1))
                        break # Move to next user after finding first relevant item
                else: # This 'else' belongs to the 'for' loop
                    reciprocal_ranks.append(0) # No relevant item found
            
            return np.mean(reciprocal_ranks) if reciprocal_ranks else 0

        # Example recommendations for 3 users
        # 1 means relevant, 0 means not
        recs = [
            [0, 1, 0, 1, 0], # User 1: First relevant at rank 2
            [1, 0, 0, 0, 1], # User 2: First relevant at rank 1
            [0, 0, 0, 0, 1]  # User 3: First relevant at rank 5
        ]
        mrr_score = calculate_mrr(recs)
        print(f"MRR Score: {mrr_score:.4f}")
        ```
5.  **Math:**
    $$ \text{MRR} = \frac{1}{|Q|} \sum_{i=1}^{|Q|} \frac{1}{\text{rank}_i} $$
    * $|Q|$: The total number of queries (or users) in the test set.
    * $\text{rank}_i$: The rank of the first relevant document for the *i*-th query.

---

#### 9. Concept Drift
1.  **Short Description:** Concept drift is the phenomenon where the statistical properties of the target variable (what you are trying to predict) change over time, causing a trained model's performance to degrade.
2.  **What is it good for?** Recognizing and planning for concept drift is essential for maintaining the long-term accuracy and relevance of a recommendation model. A model trained on last year's data may not perform well on today's user behavior.
3.  **Details:**
    * **Causes in Recommendations:**
        * **Changing User Tastes:** A user's preferences evolve. Someone who watched only comedies might start exploring dramas.
        * **Seasonality:** People watch more holiday movies in December.
        * **External Events:** A major world event, a new popular TV show, or a viral trend on social media can suddenly change what people are interested in.
    * **Types of Drift:**
        * **Sudden Drift:** A rapid change (e.g., a pandemic starts, and everyone starts watching movies about outbreaks).
        * **Gradual Drift:** A slow, continuous change (e.g., the slow rise in popularity of a new genre).
    * **Handling Drift:**
        * **Regular Retraining:** The most common solution. Retrain the model on recent data periodically (e.g., daily, weekly).
        * **Online Learning:** Update the model incrementally as new data (new ratings) arrives, rather than doing full batch retraining.
        * **Drift Detection Algorithms:** Monitor the model's performance on a live validation set and trigger a retraining automatically when performance drops below a threshold.
4.  **Examples:**
    * A model trained in 2019 would have no concept of the massive surge in popularity of shows like "Tiger King" or "The Queen's Gambit" in 2020. Without retraining, it would fail to recommend these to users who would likely enjoy them.
    * A music recommendation system needs to constantly adapt to new hit songs and artists that appear on platforms like TikTok.

---
#### New Terms Introduced

#### A. Loss Function
1.  **Short Description:** A loss function (or cost function) is a function that quantifies the difference between a model's prediction and the actual ground truth value.
2.  **What is it good for?** It provides the objective measure that a machine learning algorithm tries to minimize during training. The entire goal of training is to adjust the model's parameters (like the latent vectors in MF) to make the loss as small as possible.
3.  **Details:**
    * The choice of loss function depends on the task. For regression (like predicting a 1-5 rating), **Mean Squared Error (MSE)** is common. For classification, **Cross-Entropy** is often used.
    * A smaller loss value means the model's predictions are closer to the actual data. A loss of 0 would mean a perfect fit.
    * The process of minimizing this function is typically done using optimization algorithms like Gradient Descent or ALS.
4.  **Examples:**
    * **Mean Squared Error (MSE):** Used for predicting continuous values. It heavily penalizes large errors.
        $$ \text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 $$
        Where $y_i$ is the true value and $\hat{y}_i$ is the predicted value. The MF objective function we saw earlier is based on the Sum of Squared Errors (the same idea as MSE).
    * **Binary Cross-Entropy:** Used for binary classification (predicting a probability between 0 and 1).
        $$ \text{BCE} = -\frac{1}{n} \sum_{i=1}^{n} [y_i \log(\hat{y}_i) + (1 - y_i) \log(1 - \hat{y}_i)] $$

#### B. Regularization
1.  **Short Description:** Regularization is a technique used to prevent overfitting by adding a penalty term to the loss function, which discourages the model from learning overly complex patterns.
2.  **What is it good for?** It improves a model's ability to generalize to new, unseen data. Without regularization, a model might perfectly memorize the training data but fail miserably when making predictions on data it hasn't seen before.
3.  **Details:**
    * Overfitting occurs when a model learns not only the underlying patterns in the data but also the noise and random fluctuations specific to the training set.
    * The penalty term is based on the magnitude of the model's parameters (e.g., the latent vectors P and Q). By penalizing large parameter values, regularization forces the model to find simpler solutions that are more likely to be robust.
    * The strength of the regularization is controlled by a hyperparameter, often denoted by lambda ($\lambda$). A higher lambda means a stronger penalty and a simpler model.
4.  **Examples:**
    * **L2 Regularization (Ridge):** Adds the sum of the squared magnitudes of the parameters to the loss function. This is the type used in the MF math shown earlier. It tends to keep all parameter values small.
        $$ \text{Loss}_{L2} = \text{Original Loss} + \lambda \sum_{j} w_j^2 $$
    * **L1 Regularization (Lasso):** Adds the sum of the absolute values of the parameters. This can force some parameter values to become exactly zero, effectively performing feature selection.
        $$ \text{Loss}_{L1} = \text{Original Loss} + \lambda \sum_{j} |w_j| $$


### Questions

**1. When would you prefer to use ALS rather than SGD?**

* **Short Answer:** You'd prefer ALS when you need to parallelize training across many machines, especially with large implicit feedback datasets. You'd prefer SGD for smaller datasets or when online learning (updating the model with single data points) is required.

* **Long Answer:**
    The choice between Alternating Least Squares (ALS) and Stochastic Gradient Descent (SGD) for optimizing matrix factorization depends on the data characteristics and the system architecture.
    * **Choose ALS for Parallelism:** ALS is deterministic and its updates can be computed independently for each user (when fixing items) and each item (when fixing users). This structure makes it trivial to parallelize using frameworks like Apache Spark. If you have a massive dataset and access to a distributed computing cluster, ALS is often the more scalable choice.
    * **Choose ALS for Implicit Data:** ALS is particularly well-suited for implicit feedback models. The formulation allows for an efficient global recalculation of user/item vectors based on all their interactions, which works well with the confidence-based approach used for implicit data.
    * **Choose SGD for Flexibility and Online Learning:** SGD is an online algorithm, meaning it can update the model one rating at a time. This is extremely useful if you need your model to learn in near real-time as new user interactions occur. It doesn't require a full batch recalculation.
    * **Choose SGD for Simplicity on a Single Machine:** For smaller datasets that fit on a single machine, SGD is often faster and easier to implement than a parallelized ALS system. It converges more quickly in terms of data passes, though each pass is slower.

**2. When would you move users from the “cold start" group to the "I know you" group?**

* **Short Answer:** You'd move a user out of the "cold start" group as soon as they have provided enough interaction data for the collaborative filtering model to generate meaningful, personalized recommendations.

* **Long Answer:**
    There isn't a single magic number, but the transition is typically based on a threshold of user activity. This threshold is a hyperparameter that needs to be determined based on model performance.
    1.  **Interaction Count Threshold:** The most common method is to set a minimum number of interactions (e.g., ratings). For instance, a user is considered "warm" once they have rated **5 to 20 movies**. Below this, the CF model's predictions are likely to be unstable and no better than a popularity-based baseline.
    2.  **Model Confidence Score:** A more sophisticated approach is to measure the model's confidence in its predictions for a user. Once the variance or uncertainty of the predictions for that user drops below a certain level, they can be moved out of the cold start group.
    3.  **A/B Testing:** The ideal threshold can be found through A/B testing. You can test different thresholds (e.g., 5 ratings vs. 10 ratings vs. 20 ratings) and see which one leads to better engagement metrics (like click-through rate or watch time) for the users transitioning out of the cold start phase. The goal is to switch them to the personalized model as soon as it starts outperforming the generic "cold start" model (e.g., top popular).

**3. Are there material differences when using MF vs. SVD for the use case of CF?**

* **Short Answer:** Yes, there are critical differences. Pure SVD cannot be used directly on sparse recommendation matrices with missing values. The Matrix Factorization (MF) techniques used in Collaborative Filtering (like Funk SVD) are *inspired* by SVD but are fundamentally different optimization-based models designed to work on sparse data.

* **Long Answer:**
    While the terms are sometimes used interchangeably, they are not the same in practice.
    * **SVD's Data Requirement:** Mathematical SVD is a deterministic algorithm that requires a **dense matrix** (no missing values). To apply it to a user-item matrix, you would first have to fill in all the missing ratings, a process called imputation. This is problematic because imputing with a simple value like the mean can heavily skew the data and is computationally infeasible for massive matrices.
    * **MF's Approach:** Matrix Factorization models used in CF (often called "model-based CF") are a class of algorithms that solve an optimization problem. They **only consider the known ratings** in the sparse matrix when calculating the loss function. They don't need the missing values to be filled. They learn the latent vectors P and Q by trying to make their dot product reconstruct the *known* ratings as accurately as possible.
    * **The "Funk SVD" Misnomer:** The popular algorithm that won the Netflix Prize was named "Funk SVD" by Simon Funk. It uses SGD to find the latent factors, but it's not a true SVD. The name stuck and created confusion. It's more accurately described as a regularized matrix factorization model solved with SGD.
    In summary, you use **Matrix Factorization** (optimized with ALS or SGD) for collaborative filtering. You use the *concept* of SVD (finding a low-rank approximation) as the theoretical motivation for why MF works.

**4. Does MF work better for binary data rather than, i.e. 1-10 score a user ranked an item?**

* **Short Answer:** Not necessarily "better," but differently. MF is highly adaptable. For explicit scores (1-10), it's treated as a regression problem. For binary data (implicit feedback), it's treated as a ranking or classification problem, often by modeling confidence. Both are powerful applications of MF.

* **Long Answer:**
    Matrix Factorization is a flexible framework that can be adapted to both scenarios effectively, but the interpretation and objective function change.
    * **Explicit Data (1-10 scores):** When dealing with explicit ratings, MF models are typically trained to solve a **regression problem**. The objective is to minimize the Mean Squared Error between the predicted rating ($\mathbf{p}_u^T \mathbf{q}_i$) and the actual rating ($r_{ui}$). The model learns the nuances of preference (a 9 is better than an 8). This data is rich but sparse.
    * **Binary Data (Implicit Feedback):** When dealing with binary data (viewed/not-viewed, purchased/not-purchased), the task becomes more about **ranking and classification**. A `1` doesn't mean "loved it," it just means "interacted." A `0` doesn't mean "hated it," it means "unknown." A common approach (popularized by the paper "Collaborative Filtering for Implicit Feedback Datasets") is to model the *confidence* of a preference. You treat all interactions as positive examples (with high confidence) and all non-interactions as negative examples (with low confidence). The model then tries to predict which of the unobserved items the user is most likely to interact with. ALS is particularly effective for this formulation.

    Neither is inherently "better"; the best approach depends on the data you have. If you have high-quality explicit ratings, use them. If you only have interaction logs, the implicit feedback approach is extremely powerful and often works on a much larger scale.

**5. How do you decide on the size of the vector to represent a user/item?**

* **Short Answer:** The size of the latent vector (the number of factors, *k*) is a critical hyperparameter that is usually determined through experimentation and cross-validation, balancing model complexity and performance.

* **Long Answer:**
    Choosing the number of latent factors, *k*, involves a trade-off:
    * **Too small *k*:** The model may be too simple to capture the complexities of user tastes (underfitting). For example, with only 2 factors for movies, you might only capture "blockbuster vs. indie" and "comedy vs. drama," missing out on nuances like "dark humor" or "sci-fi world-building."
    * **Too large *k*:** The model might learn the noise in the training data instead of the true underlying patterns (overfitting). It also increases computational cost (training time, memory) and can make the model less robust.

    The process for choosing *k* is empirical:
    1.  **Define a Range:** Start with a reasonable range of values to test, for example, `k = [10, 20, 50, 100, 200]`.
    2.  **Cross-Validation:** Split your data into training and validation sets. For each value of *k* in your range, train the MF model on the training set.
    3.  **Evaluate Performance:** Evaluate the performance of each trained model on the validation set using a relevant metric (like RMSE for explicit ratings, or NDCG/MRR for implicit ranking).
    4.  **Plot and Select:** Plot the performance metric against the number of factors. Typically, you'll see performance improve as *k* increases, then plateau, and possibly even decrease if overfitting becomes severe. The "elbow" of this curve—the point of diminishing returns—is often the best choice for *k*. This balances predictive power with model simplicity.

**6. What can you do if you want to incorporate additional data to the model? e.g. movie length, is it technicolor, or did Sean Connery appear in it?**

* **Short Answer:** You move from pure Collaborative Filtering to a **Hybrid Model**. The most common approach is to incorporate this content-based data (item features) directly into the matrix factorization model.

* **Long Answer:**
    Standard MF only uses the user-item interaction data. To include side information (also called metadata), you need to extend the model.
    1.  **Factorization Machines (FM):** This is a powerful and popular solution. FMs generalize the MF model and are designed to work with any categorical or numerical feature data. You can throw in user features (age, location), item features (genre, director, actors), and contextual features (time of day, device) all into one model. It learns the interactions between all these features automatically.
    2.  **Hybrid Matrix Factorization:** You can modify the prediction rule. Instead of just $\hat{r}_{ui} = \mathbf{p}_u^T \mathbf{q}_i$, you can add terms for the features. For example, if you have item features (like genre), you can have another latent matrix for genre features, and the prediction becomes a combination of the CF part and the content part.
    3.  **Feature Engineering:** You can create new features from the metadata. For example, instead of just a user ID, you could have a user vector that is a concatenation of the learned latent vector and one-hot encoded demographic data.
    4.  **Two-Stage Model:** A simpler approach is to use a content-based model to generate an initial list of candidates and then use a CF model to re-rank those candidates. This is particularly useful for solving the item cold-start problem, as the content-based model can make recommendations for new items that have no interaction history.

**7. How would adding a row/column of zeros (user/item cold start) affect MF?**

* **Short Answer:** It would have almost no effect on the training of existing user/item vectors, but the model would be unable to learn a meaningful vector for the new all-zero row/column, resulting in useless (likely near-zero) predictions for that user/item.

* **Long Answer:**
    Let's break down the impact of adding a new user (an all-zero row) to the ratings matrix `R`:
    * **Effect on Training:** The optimization algorithms for MF (SGD, ALS) iterate over the *known* ratings. Since the new user has no known ratings (the row is all zeros, which in a sparse representation means no entries), they will simply be ignored during the training process. The existing latent vectors for other users and all items will not be affected.
    * **The New User's Latent Vector:** The new user's latent vector, $\mathbf{p}_{new}$, is typically initialized randomly or to zeros. Since this user is never included in any updates (because they have no ratings to calculate error from), their latent vector will remain at its initial state.
    * **Predictions for the New User:** When you try to predict a rating for this new user for any item *i*, you calculate $\hat{r}_{new, i} = \mathbf{p}_{new}^T \mathbf{q}_i$. If $\mathbf{p}_{new}$ is a zero vector, the prediction will always be 0. If it's a small random vector, the prediction will be a small random number. In either case, the predictions are meaningless and non-personalized. This is the definition of the user cold-start problem within an MF framework. The same logic applies to a new item (an all-zero column).

**8. Would you use any of these methods if you had 10m items to recommend?**

* **Short Answer:** Yes, absolutely, but not in isolation. At that scale, MF (especially with ALS) is a core component, but it's used within a larger multi-stage recommendation architecture.

* **Long Answer:**
    Recommending from 10 million items requires a system designed for scale, not just a single algorithm. A typical large-scale system looks like this:
    1.  **Candidate Generation (Retrieval):** The first step is to quickly filter the 10 million items down to a few hundred plausible candidates for a given user. You cannot afford to score every single item. This stage uses highly efficient but less precise models.
        * **Matrix Factorization is perfect here.** You can use the user and item vectors from a trained MF model (like one from ALS) to perform a fast nearest-neighbor search (e.g., using libraries like Faiss or Annoy) to find the items whose vectors are closest to the user's vector in the latent space.
        * Other methods include simple content-based filtering or business rules (e.g., "show new items").
    2.  **Filtering:** Apply hard constraints, like removing items the user has already seen, or filtering by region or language.
    3.  **Ranking (Scoring):** This is where a more complex and precise model scores the few hundred candidates. This model can be more computationally expensive because it's only dealing with a small set of items. You could use a more complex model here, like a deep neural network or a Factorization Machine that incorporates many more features than the simple MF model used for retrieval.
    4.  **Re-ranking/Post-processing:** The final ranked list might be adjusted to add diversity, remove sensitive content, or boost items for business reasons (e.g., promoting a sponsored product).

    So, yes, MF is a workhorse for candidate generation at massive scale due to its efficiency in creating embeddings for fast retrieval.

**9. Why/how is regularization important in this domain?**

* **Short Answer:** Regularization is crucial to prevent overfitting. Without it, the model would learn to perfectly predict the ratings in the training set, including their noise, and would fail to generalize to make accurate predictions for unseen user-item pairs.

* **Long Answer:**
    In recommendation systems, the user-item matrix is typically very sparse, meaning each user has rated only a tiny fraction of the available items. This sparsity makes overfitting a significant risk.
    * **How it Works:** Regularization adds a penalty to the loss function based on the size of the latent factor values. The MF objective is to minimize: `Error + λ * Penalty`.
        * The `Error` term (e.g., squared error) pushes the model to fit the data it knows.
        * The `Penalty` term (e.g., the sum of squared values of all latent vectors) pushes the model to keep the latent vector values small.
    * **Why it's Important:** Imagine a user has rated only one movie, "Die Hard," with a 5-star rating. Without regularization, the model could achieve zero error by learning an enormous latent vector for that user and for "Die Hard" that perfectly align, while all other components are zero. This model has perfectly "explained" that one rating, but the learned vector is useless for predicting their rating on any other movie. Regularization prevents this by penalizing those huge vector values, forcing the model to find a more "reasonable" and smaller vector for the user that might not perfectly predict the 5-star rating (maybe it predicts a 4.8) but is far more likely to be useful for predicting their affinity for other action movies. It forces the model to learn more general, robust preferences.

**10. Are the latent vectors meaningful in any way?**

* **Short Answer:** While individual dimensions of the latent vectors are usually not directly interpretable by humans, the vectors as a whole are very meaningful. They place users and items in a shared "taste space" where proximity indicates similarity.

* **Long Answer:**
    The meaning of latent vectors is a fascinating topic.
    * **Not Directly Interpretable:** It's tempting to think that for movies, factor 1 will be "comedy vs. drama," factor 2 will be "action level," etc. This is almost never the case. The dimensions are abstract mathematical constructs that the optimization algorithm found useful for minimizing the loss function. A single dimension could be a complex blend of genre, era, director style, and something entirely unnamable.
    * **Meaningful in Relation to Each Other:** The power of latent vectors comes from their relative positions.
        * **Item Similarity:** If the latent vectors for "Die Hard" and "Lethal Weapon" are very close to each other in this space, it means the model has learned that people who rate one of them highly also tend to rate the other highly. You can use this to create a "More like this" feature.
        * **User Similarity:** Similarly, if two users' latent vectors are close, it means they have similar tastes.
        * **User-Item Affinity:** The dot product between a user vector and an item vector is a measure of their alignment in this taste space, which is why it works as a prediction.
    * **Exploratory Analysis:** While you can't label the axes, you can explore the space. You could take the vector for "Star Wars," find its nearest neighbors in the item-vector space, and you would likely find other sci-fi and fantasy films. You could take the vectors for "comedy" movies and "drama" movies, average them, and see if the resulting vectors point in different directions in the space. This can give you some intuition about what the model has learned.

**11. How would you decide on the retraining schedule for your model?**

* **Short Answer:** The retraining schedule should be based on the rate of concept drift and business needs, determined by continuously monitoring the model's online and offline performance. A common starting point is weekly or daily, adjusted based on results.

* **Long Answer:**
    Deciding on the optimal retraining frequency is a balance between model accuracy and computational cost.
    1.  **Monitor for Concept Drift:** The primary driver for retraining is drift.
        * **Online Performance Monitoring:** Track key business metrics (e.g., click-through rate on recommendations, user session length, conversion rate) in an A/B testing framework. When the live model's performance starts to degrade compared to a baseline or a newly trained model, it's time to retrain.
        * **Offline Performance Monitoring:** Periodically (e.g., daily), score a newly trained model on a fixed, recent test set (e.g., the last day's worth of data). Plot the performance (e.g., NDCG) over time. If you see a consistent drop in the old model's performance or a consistent improvement from a freshly trained one, you've found your drift rate.
    2.  **Consider Data Velocity:** How quickly does new, meaningful data arrive? For a site like YouTube or Netflix with millions of new interactions per hour, daily or even hourly retraining might be necessary. For a smaller service, weekly might be sufficient.
    3.  **Cost vs. Benefit Analysis:** Retraining models costs money (computation time, engineering resources). You need to weigh the cost of retraining against the benefit of having a more accurate model (increased user engagement and revenue).
    4.  **Typical Schedules:**
        * **Batch Retraining:** A full retraining from scratch. Common schedules are **daily** or **weekly**.
        * **Online/Incremental Learning:** For systems that need to be highly responsive, you can have a daily batch retrain combined with an **online learning** component that updates the model with new interactions every few minutes or hours. This provides a good balance of stability and responsiveness.