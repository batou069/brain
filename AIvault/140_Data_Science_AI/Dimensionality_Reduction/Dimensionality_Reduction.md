---
tags:
  - data_science
  - machine_learning
  - unsupervised_learning
  - dimensionality_reduction
  - feature_selection
  - feature_extraction
  - concept
aliases:
  - Dimension Reduction
related:
  - "[[Unsupervised_Learning]]"
  - "[[Principal_Component_Analysis_PCA]]"
  - "[[t_SNE]]"
  - "[[Curse_of_Dimensionality]]"
worksheet:
  - WS_Math_Foundations_2
date_created: 2025-08-07
---
# Dimensionality Reduction

## Definition
**Dimensionality reduction** is the process of reducing the number of features (or dimensions) in a dataset. It is a key technique in machine learning and data analysis, used to transform high-dimensional data into a lower-dimensional representation while retaining as much meaningful information as possible.

This is often necessary to combat the **[[Curse_of_Dimensionality|curse of dimensionality]]**, where high-dimensional spaces have counter-intuitive properties that can make data sparse and algorithms less effective.

## Why Reduce Dimensionality?
- **Improved Model Performance:** Can lead to better generalization and prevent [[Overfitting_Underfitting|overfitting]] by removing noise and redundant features.
- **Reduced Computational Cost:** Fewer dimensions mean faster training times and less memory/storage requirements.
- **Data Visualization:** Reducing data to 2 or 3 dimensions allows for plotting and visual exploration of high-dimensional datasets.
- **Noise Reduction:** Can filter out irrelevant noise features.
- **Easier Interpretation:** A model with fewer features can sometimes be easier to understand and explain.

## Main Approaches
There are two main approaches to dimensionality reduction:

[list2tab|#Reduction Approaches]
- Feature Selection
    - **Description:** This approach involves selecting a subset of the original features and discarding the rest. No new features are created.
    - **Methods:**
        - **Filter Methods:** Select features based on their statistical properties (e.g., correlation with the target, mutual information, variance). These are independent of the model being used. (e.g., VarianceThreshold, SelectKBest).
        - **Wrapper Methods:** Use a specific machine learning model to evaluate the usefulness of feature subsets. They "wrap" the model training process. (e.g., Recursive Feature Elimination - RFE).
        - **Embedded Methods:** Feature selection is performed as part of the model training process itself. (e.g., [[L1_L2_Regularization|L1 Regularization (Lasso)]] which shrinks some feature weights to zero).
    - **Pros:** Preserves original features and their interpretability.
    - **Cons:** May discard features that are useful in combination with others.
- Feature Extraction
    - **Description:** This approach creates a new, smaller set of features by combining or transforming the original features. The new features are combinations of the old ones.
    - **Methods:**
        - **[[Principal_Component_Analysis_PCA|Principal Component Analysis (PCA)]]:** A linear technique that finds a new set of orthogonal axes (principal components) that capture the maximum variance in the data.
        - **Linear Discriminant Analysis (LDA):** A supervised linear technique that finds a feature subspace that maximizes the separability between classes.
        - **Non-linear Methods:** Used when the data has a complex, non-linear structure.
            - **t-SNE (t-Distributed Stochastic Neighbor Embedding):** Excellent for visualizing high-dimensional data in 2D or 3D, but not suitable for general-purpose dimensionality reduction before modeling.
            - **UMAP (Uniform Manifold Approximation and Projection):** Another powerful visualization technique, often faster than t-SNE.
            - **Autoencoders:** Neural networks trained to reconstruct their input, with a bottleneck hidden layer that learns a compressed, lower-dimensional representation of the data.

## Choosing the Right Technique
- For **visualization**, t-SNE or UMAP are often the best choices.
- For **linear dimensionality reduction** as a preprocessing step, PCA is the standard go-to method.
- If you have **labeled data** and want to maximize class separability, LDA is a good option.
- If you need to **preserve the original features** for interpretability, use feature selection methods.
- For **complex non-linear structures**, autoencoders or other manifold learning techniques might be necessary.

Dimensionality reduction is a powerful tool but requires careful application, as it can lead to information loss if not used appropriately.

---