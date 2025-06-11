---
tags:
  - python
  - scikit_learn
  - sklearn
  - machine_learning
  - dimensionality_reduction
  - pca
  - nmf
  - tsne
  - concept
  - example
aliases:
  - Scikit-learn Dimensionality Reduction
  - Feature Reduction sklearn
  - PCA sklearn
related:
  - "[[160_Python_Libraries/Scikit_learn/_Scikit_learn_MOC|_Scikit_learn_MOC]]"
  - "[[Unsupervised_Learning]]"
  - "[[Principal_Component_Analysis_PCA|Principal Component Analysis (PCA)]]"
  - "[[Singular_Value_Decomposition|SVD]]"
  - "[[Overfitting_Underfitting]]"
  - "[[Curse_of_Dimensionality]]"
worksheet:
  - WS_ML_Libraries_1
date_created: 2025-06-09
---
# Scikit-learn: Dimensionality Reduction (`sklearn.decomposition`, `sklearn.manifold`)

Dimensionality reduction techniques are used to reduce the number of features (dimensions) in a dataset while retaining as much meaningful information as possible. This can be useful for:
-   Reducing computational complexity and training time of models.
-   Mitigating the [[Curse_of_Dimensionality|curse of dimensionality]].
-   Visualizing high-dimensional data in 2D or 3D.
-   Noise reduction by removing irrelevant or redundant features.
-   Compressing data.

Scikit-learn provides several algorithms for dimensionality reduction, primarily in the `sklearn.decomposition` and `sklearn.manifold` modules.

## Key Dimensionality Reduction Techniques

[list2tab|#Dim Reduction Tech]
- Principal Component Analysis (PCA)
    - **Module:** `sklearn.decomposition`
    - **Model:** `PCA`
    - **Concept:** A linear dimensionality reduction technique that transforms the data into a new coordinate system such that the greatest variance by some scalar projection of the data comes to lie on the first coordinate (called the first principal component), the second greatest variance on the second coordinate, and so on. It uses [[Singular_Value_Decomposition|Singular Value Decomposition (SVD)]] of the (mean-centered) data.
    - **Purpose:** Retains dimensions that capture the most variance in the data. Useful for noise filtering, visualization, and feature extraction.
    - **Key Parameters:**
        -   `n_components`: Number of components to keep. If `0 < n_components < 1`, it's the percentage of variance to retain. If an integer, it's the number of components.
        -   `svd_solver`: `{'auto', 'full', 'arpack', 'randomized'}`.
    - **Attributes:** `components_` (principal axes), `explained_variance_ratio_` (percentage of variance explained by each component).
    - **Example (Reducing features of product data for visualization):**
        ```python
        from sklearn.decomposition import PCA
        from sklearn.preprocessing import StandardScaler
        import pandas as pd
        import numpy as np
        # import matplotlib.pyplot as plt

        # Conceptual product data with multiple features
        np.random.seed(0)
        X_products = pd.DataFrame(np.random.rand(100, 10), columns=[f'feature_{i}' for i in range(10)])
        # Add some correlation for PCA to be more interesting
        X_products['feature_0'] = X_products['feature_0'] + X_products['feature_1'] * 0.5
        X_products['feature_2'] = X_products['feature_2'] - X_products['feature_3'] * 0.7

        # Scaling is crucial for PCA
        # scaler = StandardScaler()
        # X_scaled = scaler.fit_transform(X_products)

        # Reduce to 2 components for visualization
        # pca = PCA(n_components=2, random_state=42)
        # X_pca = pca.fit_transform(X_scaled)

        # print("Original shape:", X_scaled.shape)
        # print("Reduced shape (PCA):", X_pca.shape)
        # print(f"Explained variance ratio by 2 components: {pca.explained_variance_ratio_.sum():.4f}")

        # Conceptual visualization
        # plt.figure(figsize=(8, 6))
        # plt.scatter(X_pca[:, 0], X_pca[:, 1], alpha=0.7) # Assuming some coloring 'c' if target exists
        # plt.title('PCA of Product Features (2 Components)')
        # plt.xlabel('Principal Component 1')
        # plt.ylabel('Principal Component 2')
        # plt.grid(True); plt.show()
        ```
- Non-negative Matrix Factorization (NMF)
    - **Module:** `sklearn.decomposition`
    - **Model:** `NMF`
    - **Concept:** A dimensionality reduction and matrix factorization technique where a non-negative matrix $\mathbf{X}$ is factorized into two non-negative matrices $\mathbf{W}$ and $\mathbf{H}$ ($\mathbf{X} \approx \mathbf{W}\mathbf{H}$). Often used for parts-based representation.
    - **Purpose:** Useful when features are non-negative (e.g., pixel intensities, word counts) and an additive, parts-based representation is desired.
    - **Key Parameters:**
        -   `n_components`: Number of components (rank of factorization).
        -   `init`: Method used to initialize W and H.
        -   `solver`: Numerical solver to use.
    - **Example (Topic modeling on product review term frequencies - conceptual):**
        ```python
        from sklearn.decomposition import NMF
        from sklearn.feature_extraction.text import TfidfVectorizer
        import pandas as pd

        # Conceptual product review data
        reviews = [
            "great product excellent quality fast shipping",
            "love this item works perfectly very good",
            "terrible product broke after one day bad quality",
            "not good poor design would not buy again",
            "amazing features and good price highly recommend"
        ]
        # vectorizer = TfidfVectorizer(max_df=0.95, min_df=1, stop_words='english')
        # X_tfidf = vectorizer.fit_transform(reviews) # TF-IDF matrix (non-negative)

        # Reduce to 2 "topics" (components)
        # nmf_model = NMF(n_components=2, init='random', random_state=42, max_iter=500) # max_iter might need adjustment
        # W_nmf = nmf_model.fit_transform(X_tfidf) # Document-topic matrix
        # H_nmf = nmf_model.components_        # Topic-term matrix

        # print("NMF Document-Topic Matrix (W) shape:", W_nmf.shape)
        # print("NMF Topic-Term Matrix (H) shape:", H_nmf.shape)
        # Displaying top words per topic would require more code with feature_names_from_vectorizer
        ```
- t-distributed Stochastic Neighbor Embedding (t-SNE)
    - **Module:** `sklearn.manifold`
    - **Model:** `TSNE`
    - **Concept:** A non-linear dimensionality reduction technique primarily used for **visualization** of high-dimensional datasets in low-dimensional space (typically 2D or 3D). It models data points by converting high-dimensional Euclidean distances between data points into conditional probabilities representing similarities.
    - **Purpose:** Excellent for revealing underlying manifold structure and clusters in high-dimensional data for visualization. Not typically used for feature reduction before classification/regression directly, as it doesn't learn a `transform` method for new data in the same way PCA does (though some workarounds exist).
    - **Key Parameters:**
        -   `n_components`: Dimension of the embedded space (usually 2 or 3).
        -   `perplexity`: Related to the number of nearest neighbors. Typical values between 5 and 50.
        -   `learning_rate`: Usually between 10 and 1000.
        -   `n_iter`: Maximum number of iterations for optimization.
        -   `init`: `{'random', 'pca'}`. Initialization of embeddings. 'pca' is often more stable.
    - **Example (Visualizing high-dimensional customer segments):**
        ```python
        from sklearn.manifold import TSNE
        from sklearn.preprocessing import StandardScaler
        import pandas as pd
        import numpy as np
        # import matplotlib.pyplot as plt

        # Conceptual high-dimensional customer feature data
        # np.random.seed(1)
        # X_high_dim_customers = pd.DataFrame(np.random.rand(150, 20), columns=[f'hd_feat_{i}' for i in range(20)])
        # True underlying clusters for coloring plot (not used by t-SNE itself)
        # y_true_labels = np.concatenate([np.zeros(50), np.ones(50), np.full(50, 2)])

        # scaler = StandardScaler()
        # X_hd_scaled = scaler.fit_transform(X_high_dim_customers)

        # tsne = TSNE(n_components=2, perplexity=30, learning_rate='auto',
        #             init='pca', n_iter=1000, random_state=42) # learning_rate='auto' available in newer sklearn
        # X_tsne = tsne.fit_transform(X_hd_scaled)

        # print("Original shape:", X_hd_scaled.shape)
        # print("Reduced shape (t-SNE):", X_tsne.shape)

        # Conceptual visualization
        # plt.figure(figsize=(8, 6))
        # scatter_tsne = plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=y_true_labels, cmap='viridis', alpha=0.7)
        # plt.title('t-SNE visualization of Customer Data')
        # plt.xlabel('t-SNE Component 1')
        # plt.ylabel('t-SNE Component 2')
        # plt.legend(handles=scatter_tsne.legend_elements(), labels=['Segment 0', 'Segment 1', 'Segment 2'])
        # plt.grid(True); plt.show()
        ```
- Other Techniques
    - **Independent Component Analysis (ICA - `FastICA`):** Separates a multivariate signal into additive subcomponents that are maximally independent.
    - **Linear Discriminant Analysis (LDA - `LinearDiscriminantAnalysis`):** Can be used for dimensionality reduction in classification tasks by maximizing class separability. It's a supervised method.
    - **Manifold Learning (`Isomap`, `LocallyLinearEmbedding`, `SpectralEmbedding`):** Non-linear techniques that assume data lies on a low-dimensional manifold embedded in the high-dimensional space. Aim to "unroll" this manifold.

## Considerations
-   **Feature Scaling:** Most dimensionality reduction techniques (especially PCA, t-SNE) are sensitive to feature scales. It's generally recommended to scale data (e.g., using `StandardScaler`) before applying them.
-   **Interpretability:** Linear methods like PCA offer more interpretable components (linear combinations of original features). Non-linear methods like t-SNE produce embeddings where the axes don't have a direct, simple interpretation.
-   **Computational Cost:** Some methods (e.g., t-SNE, Isomap) can be computationally expensive for very large datasets. PCA with randomized SVD can be more scalable.
-   **Purpose:** Choose a method based on your goal:
    -   **Visualization:** t-SNE, UMAP (not in sklearn core but popular), PCA.
    -   **Feature extraction for supervised learning:** PCA, NMF, LDA (if supervised).
    -   **Noise reduction:** PCA.

Dimensionality reduction is a powerful tool for managing and understanding complex, high-dimensional data.

---