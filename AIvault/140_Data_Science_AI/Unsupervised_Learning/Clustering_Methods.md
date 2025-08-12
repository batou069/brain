---
tags:
  - data_science
  - machine_learning
  - unsupervised_learning
  - clustering
  - model
  - concept
aliases:
  - Clustering Algorithms
  - Cluster Analysis
related:
  - "[[Unsupervised_Learning]]"
  - "[[Model_Evaluation]]"
  - "[[K_Means_Clustering]]"
  - "[[Hierarchical_Clustering]]"
  - "[[DBSCAN]]"
worksheet:
  - WS_Math_Foundations_2
date_created: 2025-08-07
---
# Clustering Methods

## Definition
**Clustering** or **cluster analysis** is a primary task in [[Unsupervised_Learning|unsupervised learning]]. It involves partitioning a set of data points into a number of groups, called **clusters**, such that data points in the same group are more similar to each other than to those in other groups.

The goal is to discover the natural groupings in the data without any prior knowledge of the group labels.

## Types of Clustering Algorithms
Clustering algorithms can be categorized based on their underlying approach:

[list2tab|#Clustering Types]
- Partitioning
    - **Description:** These methods divide the dataset into a pre-determined number of non-overlapping clusters. Each data point belongs to exactly one cluster.
    - **Examples:**
        - **K-Means:** An iterative algorithm that partitions data into *K* clusters by minimizing the variance within each cluster (the sum of squared distances to the cluster's centroid).
        - **K-Medoids (PAM):** Similar to K-Means, but uses actual data points (medoids) as cluster centers, making it more robust to outliers.
- Hierarchical
    - **Description:** These methods create a tree-like structure of clusters, called a dendrogram.
    - **Sub-types:**
        - **Agglomerative (Bottom-up):** Starts with each data point as its own cluster and iteratively merges the closest pairs of clusters until only one cluster remains.
        - **Divisive (Top-down):** Starts with all data points in a single cluster and recursively splits clusters until each data point is its own cluster.
    - **Examples:** Agglomerative Clustering with different linkage criteria (Ward, complete, average).
- Density-Based
    - **Description:** These methods define clusters as dense regions of data points separated by regions of lower density. They can discover clusters of arbitrary shape and are robust to noise.
    - **Examples:**
        - **DBSCAN (Density-Based Spatial Clustering of Applications with Noise):** Groups together points that are closely packed together, marking as outliers points that lie alone in low-density regions.
        - **OPTICS:** An extension of DBSCAN that handles clusters of varying density.
- Distribution-Based
    - **Description:** These methods assume that the data is composed of a mixture of distributions (e.g., Gaussian distributions) and aim to find the parameters of these distributions that best fit the data.
    - **Examples:**
        - **Gaussian Mixture Models (GMM):** Assumes data points are generated from a mixture of a finite number of Gaussian distributions with unknown parameters. It uses an Expectation-Maximization (EM) algorithm to find these parameters.

## Key Considerations
- **Choice of *K*:** For partitioning methods like K-Means, the number of clusters *K* must be specified beforehand. Techniques like the Elbow Method or Silhouette Analysis can help determine an optimal *K*.
- **Distance Metric:** The definition of "similarity" or "distance" (e.g., Euclidean, Manhattan, Cosine) is crucial and can significantly impact the results.
- **Feature Scaling:** Most clustering algorithms are sensitive to the scale of the features, so standardization or normalization is usually a required preprocessing step.
- **Cluster Shape:** Different algorithms have different assumptions about the shape of clusters. K-Means assumes spherical, equally-sized clusters, while DBSCAN can find arbitrary shapes.

## Evaluation Metrics
Since clustering is unsupervised, evaluation is less straightforward than for supervised tasks.
- **Internal Metrics:** Evaluate the quality of the clustering based only on the data itself.
    - **Silhouette Score:** Measures how similar a point is to its own cluster compared to other clusters. Ranges from -1 to 1 (higher is better).
    - **Calinski-Harabasz Index:** Ratio of between-cluster dispersion to within-cluster dispersion (higher is better).
    - **Davies-Bouldin Index:** Ratio of within-cluster distances to between-cluster distances (lower is better).
- **External Metrics:** Used when ground truth labels are available (e.g., for academic comparison).
    - **Adjusted Rand Index (ARI):** Measures the similarity between the true and predicted clusterings, adjusted for chance.
    - **Homogeneity, Completeness, V-measure.**

See [[Model_Evaluation]].

---