---
tags:
  - python
  - scikit_learn
  - sklearn
  - machine_learning
  - clustering
  - unsupervised_learning
  - kmeans
  - dbscan
  - concept
  - example
aliases:
  - Scikit-learn Clustering Algorithms
  - sklearn.cluster
related:
  - "[[160_Python_Libraries/Scikit_learn/_Scikit_learn_MOC|_Scikit_learn_MOC]]"
  - "[[Unsupervised_Learning]]"
  - "[[K_Means_Clustering]]"
  - "[[DBSCAN_Clustering]]"
  - "[[Hierarchical_Clustering]]"
  - "[[Sklearn_Metrics|Clustering Metrics]]"
worksheet:
  - WS_ML_Libraries_1
date_created: 2025-06-09
---
# Scikit-learn: Clustering Algorithms (`sklearn.cluster`)

Clustering is a type of [[Unsupervised_Learning|unsupervised learning]] where the goal is to group a set of objects in such a way that objects in the same group (called a **cluster**) are more similar (in some sense) to each other than to those in other groups (clusters). The `sklearn.cluster` module in Scikit-learn provides implementations of several popular clustering algorithms.

## Key Clustering Algorithms

[list2tab|#Clustering Algorithms]
- K-Means
    - **Model:** `KMeans`
    - **Concept:** Partitions $n$ observations into $k$ clusters in which each observation belongs to the cluster with the nearest mean (cluster centroid), serving as a prototype of the cluster.
    - **Algorithm:** Iteratively assigns points to the closest centroid and then recalculates centroids based on the new assignments, until convergence.
    - **Key Parameters:**
        -   `n_clusters`: The number of clusters to form (k). Must be specified beforehand.
        -   `init`: `{'k-means++', 'random'}` or an ndarray. Method for initialization. 'k-means++' is generally preferred as it speeds up convergence.
        -   `n_init`: Number of times the k-means algorithm will be run with different centroid seeds. The final results will be the best output of `n_init` consecutive runs in terms of inertia. (e.g., `n_init='auto'` or an integer).
        -   `max_iter`: Maximum number of iterations for a single run.
        -   `tol`: Relative tolerance with regards to Frobenius norm of the difference in the cluster centers of two consecutive iterations to declare convergence.
    - **Attributes:** `cluster_centers_` (coordinates of cluster centroids), `labels_` (label of each point), `inertia_` (sum of squared distances of samples to their closest cluster center).
    - **Example (Segmenting customers based on spending and frequency):**
        ```python
        from sklearn.cluster import KMeans
        from sklearn.preprocessing import StandardScaler
        import pandas as pd
        import numpy as np
        # import matplotlib.pyplot as plt

        # Conceptual customer data: annual_spend, purchase_frequency
        np.random.seed(42)
        X_customer_behavior = pd.DataFrame({
            'annual_spend': np.concatenate([np.random.normal(500, 100, 50),
                                            np.random.normal(2000, 300, 50),
                                            np.random.normal(5000, 500, 50)]),
            'purchase_frequency': np.concatenate([np.random.normal(5, 1, 50),
                                                  np.random.normal(15, 3, 50),
                                                  np.random.normal(10, 2, 50)])
        })
        X_customer_behavior = X_customer_behavior[X_customer_behavior['annual_spend'] > 0] # Ensure positive spend
        X_customer_behavior = X_customer_behavior[X_customer_behavior['purchase_frequency'] > 0]


        # Scaling is important for K-Means
        # scaler = StandardScaler()
        # X_scaled = scaler.fit_transform(X_customer_behavior)

        # kmeans = KMeans(n_clusters=3, random_state=42, n_init='auto')
        # kmeans.fit(X_scaled)
        # cluster_labels = kmeans.labels_
        # centroids_scaled = kmeans.cluster_centers_
        # centroids_original = scaler.inverse_transform(centroids_scaled)

        # print("Cluster labels (first 10):", cluster_labels[:10])
        # print("Centroids (original scale):\n", pd.DataFrame(centroids_original, columns=X_customer_behavior.columns))
        # print(f"Inertia (WCSS): {kmeans.inertia_:.2f}")

        # Visualize (conceptual)
        # plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=cluster_labels, cmap='viridis', s=50, alpha=0.7)
        # plt.scatter(centroids_scaled[:, 0], centroids_scaled[:, 1], marker='X', s=200, color='red', label='Centroids')
        # plt.title('Customer Segments (K-Means)')
        # plt.xlabel('Scaled Annual Spend')
        # plt.ylabel('Scaled Purchase Frequency')
        # plt.legend(); plt.show()
        ```
    -   **Note:** K-Means assumes spherical clusters and can be sensitive to the initial placement of centroids. The number of clusters $k$ must be chosen (e.g., using elbow method or silhouette analysis).
- DBSCAN (Density-Based Spatial Clustering of Applications with Noise)
    - **Model:** `DBSCAN`
    - **Concept:** Finds core samples of high density and expands clusters from them. Good for data which contains clusters of similar density and can find clusters of arbitrary shapes. It can also identify points that are not part of any cluster (noise/outliers).
    - **Key Parameters:**
        -   `eps`: The maximum distance between two samples for one to be considered as in the neighborhood of the other.
        -   `min_samples`: The number of samples (or total weight) in a neighborhood for a point to be considered as a core point. This includes the point itself.
    - **Attributes:** `labels_` (cluster labels, -1 for noise points), `core_sample_indices_`.
    - **Example (Finding dense regions of product features):**
        ```python
        from sklearn.cluster import DBSCAN
        from sklearn.preprocessing import StandardScaler
        import pandas as pd
        import numpy as np

        # Conceptual product feature data (e.g., from sensor readings on products)
        # np.random.seed(0)
        # n_points_per_cluster = 50
        # C1 = [-5, -2] + .8 * np.random.randn(n_points_per_cluster, 2)
        # C2 = [4, -1] + .1 * np.random.randn(n_points_per_cluster, 2)
        # C3 = [1, -2] + .2 * np.random.randn(n_points_per_cluster, 2)
        # C4 = [-2, 3] + .3 * np.random.randn(n_points_per_cluster, 2)
        # C5 = [3, -2] + 1.6 * np.random.randn(n_points_per_cluster, 2)
        # C6 = [5, 6] + 2 * np.random.randn(n_points_per_cluster, 2) # Noise
        # X_features = np.vstack((C1, C2, C3, C4, C5, C6))
        # X_features_df = pd.DataFrame(X_features, columns=['feature1', 'feature2'])

        # scaler = StandardScaler()
        # X_scaled = scaler.fit_transform(X_features_df)

        # dbscan = DBSCAN(eps=0.3, min_samples=5) # eps and min_samples need tuning
        # dbscan.fit(X_scaled)
        # cluster_labels_dbscan = dbscan.labels_
        # n_clusters_ = len(set(cluster_labels_dbscan)) - (1 if -1 in cluster_labels_dbscan else 0)
        # n_noise_ = list(cluster_labels_dbscan).count(-1)

        # print(f"Estimated number of clusters: {n_clusters_}")
        # print(f"Estimated number of noise points: {n_noise_}")
        # print("Cluster labels (first 20):", cluster_labels_dbscan[:20])
        ```
    -   **Note:** DBSCAN does not require specifying the number of clusters beforehand, but `eps` and `min_samples` are sensitive parameters that need careful tuning.
- Agglomerative Hierarchical Clustering
    - **Model:** `AgglomerativeClustering`
    - **Concept:** A bottom-up hierarchical clustering approach. Each observation starts in its own cluster, and clusters are successively merged together based on a linkage criterion (measuring similarity between clusters). The process creates a tree-like structure (dendrogram).
    - **Key Parameters:**
        -   `n_clusters`: The number of clusters to find. If `None`, `distance_threshold` must be set.
        -   `linkage`: `{'ward', 'complete', 'average', 'single'}`. Which linkage criterion to use.
            -   `ward`: Minimizes the variance of the clusters being merged.
            -   `average`: Uses the average of the distances of each observation of the two sets.
            -   `complete` (max linkage): Uses the maximum distances between all observations of the two sets.
            -   `single`: Uses the minimum of the distances between all observations of the two sets.
        -   `distance_threshold`: The linkage distance threshold above which, clusters will not be merged. If not None, `n_clusters` must be None.
    - **Example (Grouping similar customer reviews based on embeddings):**
        ```python
        from sklearn.cluster import AgglomerativeClustering
        import numpy as np
        # import matplotlib.pyplot as plt
        # from scipy.cluster.hierarchy import dendrogram # For plotting dendrogram

        # Conceptual data: Assume X_review_embeddings is a NumPy array of text embeddings
        # np.random.seed(10)
        # X_review_embeddings = np.random.rand(15, 5) # 15 reviews, 5 dimensions

        # agg_clustering = AgglomerativeClustering(n_clusters=3, linkage='ward')
        # cluster_labels_agg = agg_clustering.fit_predict(X_review_embeddings)
        # print("Agglomerative Clustering labels:", cluster_labels_agg)

        # To plot a dendrogram (more involved, often done with scipy.cluster.hierarchy)
        # from scipy.cluster.hierarchy import linkage, dendrogram
        # linked = linkage(X_review_embeddings, method='ward')
        # plt.figure(figsize=(10, 7))
        # dendrogram(linked,
        #            orientation='top',
        #            distance_sort='descending',
        #            show_leaf_counts=True)
        # plt.title("Dendrogram for Agglomerative Clustering")
        # plt.xlabel("Sample index or (cluster size)")
        # plt.ylabel("Distance (Ward)")
        # plt.show()
        ```
- Other Clustering Algorithms
    - **Mean Shift (`MeanShift`):** A centroid-based algorithm that aims to discover "blobs" in a smooth density of samples. Does not require specifying the number of clusters.
    - **Spectral Clustering (`SpectralClustering`):** Applies K-Means on a projection of the graph Laplacian. Useful for finding non-convex clusters.
    - **Affinity Propagation (`AffinityPropagation`):** Based on message passing between data points. Does not require specifying the number of clusters.
    - **BIRCH (`Birch`):** Builds a tree structure (Clustering Feature Tree) for large datasets. Good for incremental learning.
    - **OPTICS (`OPTICS`):** Similar to DBSCAN but can find clusters of varying densities.

## Considerations for Clustering
-   **Feature Scaling:** Many clustering algorithms (especially distance-based like K-Means, DBSCAN) are sensitive to feature scales. It's crucial to scale features appropriately (e.g., using `StandardScaler` or `MinMaxScaler`) before clustering.
-   **Choosing `k` (for K-Means, Agglomerative):** Determining the optimal number of clusters is often a key challenge. Techniques include:
    -   Elbow method (plotting inertia vs. k for K-Means).
    -   Silhouette analysis.
    -   Davies-Bouldin Index.
    -   Gap statistic.
    -   Visual inspection of dendrograms (for hierarchical).
-   **Algorithm Assumptions:** Different algorithms make different assumptions about cluster shapes (e.g., K-Means assumes spherical, DBSCAN finds arbitrary shapes). Choose an algorithm appropriate for the expected data structure.
-   **[[Sklearn_Metrics|Evaluating Clustering Performance]]:** If ground truth labels are available (rare in true unsupervised clustering), metrics like Adjusted Rand Index, Normalized Mutual Information can be used. Otherwise, intrinsic metrics like Silhouette Score or Davies-Bouldin Index are used.

Clustering is a powerful exploratory tool for discovering natural groupings and structure in unlabeled data.

---