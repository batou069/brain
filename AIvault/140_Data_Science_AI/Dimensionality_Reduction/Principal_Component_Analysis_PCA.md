---
tags:
  - data_science
  - machine_learning
  - dimensionality_reduction
  - unsupervised_learning
  - pca
  - concept
aliases:
  - PCA
related:
  - "[[Dimensionality_Reduction]]"
  - "[[Unsupervised_Learning]]"
  - "[[Eigenvalues_Eigenvectors]]"
  - "[[Singular_Value_Decomposition]]"
  - "[[Covariance_Matrix]]"
  - "[[Change_of_Basis]]"
  - "[[Orthogonal_Matrix]]"
worksheet:
  - WS_Math_Foundations_2
date_created: 2025-08-07
---
# Principal Component Analysis (PCA)

## Definition
**Principal Component Analysis (PCA)** is a popular [[Dimensionality_Reduction|dimensionality reduction]] technique used in data science and machine learning. It is an [[Unsupervised_Learning|unsupervised learning]] method that transforms a set of correlated variables into a smaller set of uncorrelated variables called **principal components**.

The goal of PCA is to find a new set of axes (the principal components) such that the data, when projected onto these axes, has the maximum possible variance. The first principal component accounts for the largest possible variance in the data, the second principal component (orthogonal to the first) accounts for the second largest variance, and so on.

## Mathematical Foundation
PCA is fundamentally a [[Change_of_Basis|change of basis]] operation. The new basis vectors are the principal components. These components are the [[Eigenvalues_Eigenvectors|eigenvectors]] of the **[[Covariance_Matrix|covariance matrix]]** of the data.

**Steps:**
1.  **Standardize the Data:** Subtract the mean from each feature and optionally scale to unit variance. This is crucial as PCA is sensitive to the scale of the features.
2.  **Compute the Covariance Matrix:** Calculate the covariance matrix $\mathbf{\Sigma}$ of the standardized data.
3.  **Compute Eigenvectors and Eigenvalues:** Perform an [[Eigenvalues_Eigenvectors|eigendecomposition]] of the covariance matrix $\mathbf{\Sigma}$ to find its eigenvectors $\mathbf{v}_i$ and corresponding eigenvalues $\lambda_i$.
4.  **Sort Eigenvectors:** Sort the eigenvectors in descending order based on their corresponding eigenvalues. The eigenvalue $\lambda_i$ represents the amount of variance in the data along the direction of its eigenvector $\mathbf{v}_i$.
5.  **Select Principal Components:** The sorted eigenvectors are the principal components. The first principal component is the eigenvector with the largest eigenvalue. To reduce dimensionality from $d$ to $k$ ($k < d$), we select the first $k$ eigenvectors.
6.  **Transform the Data:** Project the original standardized data onto the selected principal components. This is done by forming a projection matrix $\mathbf{W}$ (an [[Orthogonal_Matrix|orthogonal matrix]]) with the top $k$ eigenvectors as its columns, and then multiplying the data by this matrix: $\mathbf{Z} = \mathbf{X}_{\text{std}} \mathbf{W}$.

Alternatively, PCA can be performed using the [[Singular_Value_Decomposition|Singular Value Decomposition (SVD)]] of the data matrix, which is often more numerically stable.

## Python Example
Let's use Scikit-learn's `PCA` to reduce a 2D dataset to 1D.

[list2tab|#PCA in Python]
- Calculation
    - We'll create some correlated 2D data and find its first principal component.
    - ```python
      import numpy as np
      import matplotlib.pyplot as plt
      from sklearn.preprocessing import StandardScaler
      from sklearn.decomposition import PCA
      
      # 1. Create correlated 2D data
      np.random.seed(42)
      X = np.dot(np.random.rand(2, 2), np.random.randn(2, 200)).T
      
      # 2. Standardize the data
      scaler = StandardScaler()
      X_scaled = scaler.fit_transform(X)
      
      # 3. Apply PCA
      # We want to reduce to 1 dimension (n_components=1)
      pca = PCA(n_components=1)
      X_pca = pca.fit_transform(X_scaled)
      
      print("Original data shape:", X_scaled.shape)
      print("Reduced data shape:", X_pca.shape)
      print("\nExplained variance ratio (by the 1st component):", pca.explained_variance_ratio_)
      print("First principal component (eigenvector):\n", pca.components_)
      
      # Expected Output:
      # Original data shape: (200, 2)
      # Reduced data shape: (200, 1)
      #
      # Explained variance ratio (by the 1st component): [0.89913154]
      # First principal component (eigenvector):
      # [[-0.70710678 -0.70710678]]
      ```
- Visualization
    - Let's visualize the original data and the direction of the first principal component.
    - ```python
      def draw_vector(v0, v1, ax=None):
          ax = ax or plt.gca()
          arrowprops=dict(arrowstyle='->', linewidth=2, shrinkA=0, shrinkB=0, color='red')
          ax.annotate('', v1, v0, arrowprops=arrowprops)
      
      # Plot the data
      plt.figure(figsize=(8, 6))
      plt.scatter(X_scaled[:, 0], X_scaled[:, 1], alpha=0.5)
      
      # Plot the first principal component
      # The component vector is scaled by its explained variance for visualization
      for length, vector in zip(pca.explained_variance_, pca.components_):
          v = vector * 3 * np.sqrt(length)
          draw_vector(pca.mean_, pca.mean_ + v)
      
      plt.xlabel("Feature 1 (Standardized)")
      plt.ylabel("Feature 2 (Standardized)")
      plt.title("PCA: Original Data and First Principal Component")
      plt.axis('equal')
      plt.grid(True)
      plt.show()
      ```
    - The output will be a scatter plot of the data with a red arrow showing the direction of the first principal component, which aligns with the direction of maximum variance.

## Applications
- **[[Dimensionality_Reduction|Dimensionality Reduction]]:**
    - Reduces the number of features in a dataset while retaining most of the important information (variance).
    - Helps combat the "curse of dimensionality".
    - Reduces computational cost and memory usage for subsequent modeling.
- **Data Visualization:**
    - Reducing high-dimensional data to 2 or 3 dimensions allows it to be plotted and visually inspected for patterns, clusters, or outliers.
- **Noise Filtering:**
    - By discarding components with low variance (which may correspond to noise), PCA can be used to clean up a dataset.
- **Feature Engineering / Preprocessing:**
    - The transformed principal components can be used as new, uncorrelated features for supervised learning models. This can be beneficial for algorithms that are sensitive to correlated features, like linear regression.
- **Image Compression:**
    - Can be used to compress images by representing them with fewer principal components.

## Limitations
- **Interpretability:** The principal components are linear combinations of the original features, which can make them difficult to interpret.
- **Linearity Assumption:** PCA assumes linear relationships between features. It may not perform well on data with complex, non-linear structures (for this, non-linear methods like t-SNE, UMAP, or Kernel PCA are used).
- **Information Loss:** It is a lossy compression technique. Some information is lost when components are discarded.
- **Scale Sensitivity:** As mentioned, PCA is highly sensitive to the scaling of the data. Features must be standardized before applying PCA.

---