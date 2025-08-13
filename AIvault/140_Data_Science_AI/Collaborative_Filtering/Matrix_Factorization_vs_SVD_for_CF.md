---
tags:
  - data_science
  - collaborative_filtering
  - matrix_factorization
  - svd
  - concept
aliases:
  - MF vs SVD
related:
  - "[[Matrix_Factorization_for_CF]]"
  - "[[Singular_Value_Decomposition]]"
  - "[[User-Item_Interaction_Matrix]]"
worksheet:
  - WS_Collaborative_Filtering_1
date_created: 2025-08-13
---
# Matrix Factorization vs. SVD for Collaborative Filtering

While [[Matrix_Factorization_for_CF|Matrix Factorization (MF)]] and [[Singular_Value_Decomposition|Singular Value Decomposition (SVD)]] both decompose a matrix into a product of lower-dimensional matrices, their application and properties in the context of [[_Collaborative_Filtering_MOC|Collaborative Filtering]] have crucial differences.

## Singular Value Decomposition (SVD)
- **Mathematical Definition:** SVD is a precise mathematical decomposition of *any* matrix $\mathbf{R}$ into $\mathbf{R} = \mathbf{U} \mathbf{\Sigma} \mathbf{V}^T$, where $\mathbf{U}$ and $\mathbf{V}$ are [[Orthogonal_Matrix|orthogonal matrices]] and $\mathbf{\Sigma}$ is a diagonal matrix of [[Singular_Values|singular values]].
- **The Problem with Sparsity:** The mathematical definition of SVD is undefined for matrices with missing values. The [[User-Item_Interaction_Matrix|user-item interaction matrix]] $\mathbf{R}$ is extremely sparse. To use pure SVD, one would first have to **impute** the missing values (e.g., fill them with the mean rating).
- **Consequences of Imputation:**
    - **Massive Data:** Imputing values turns a sparse matrix into a dense one, which can be computationally infeasible for large datasets (e.g., millions of users and items).
    - **Inaccurate Data:** Filling missing values with a simple average is a strong and often incorrect assumption, which can significantly skew the data and lead to poor factorization.

## Matrix Factorization (MF) for CF
- **Modeling Approach:** MF models (like those trained with [[Alternating_Least_Squares_ALS|ALS]] or [[Stochastic_Gradient_Descent_SGD_for_CF|SGD]]) are not a direct mathematical decomposition but rather a machine learning approach to **approximate** the original matrix.
- **Handles Sparsity Directly:** The key difference is that these models learn the latent factors $\mathbf{P}$ and $\mathbf{Q}$ by only considering the **known ratings** in the sparse matrix $\mathbf{R}$. The loss function is computed only over the observed user-item pairs.
- **Flexibility:** This approach allows for the easy addition of [[L1_L2_Regularization|regularization]] terms and biases to the model, which helps prevent overfitting and can improve accuracy. The model is: $\hat{R}_{ui} = \mu + b_u + b_i + p_u \cdot q_i$.

>[!question] Are there material differences when using MF vs. SVD for the use case of CF?
>
>Yes, the differences are material and significant. The term "SVD" is often used loosely in the recommender system community to refer to the general class of matrix factorization models, but this is technically incorrect.
>
>**Summary of Material Differences:**
>
>[list2tab|#MF vs SVD Comparison]
>- Aspect
>    - Pure SVD
>        - MF for CF (ALS/SGD)
>- Handling Missing Data
>    - Cannot handle missing values. Requires imputation.
>        - Designed to work directly with sparse matrices.
>- Computational Cost
>    - Very high on the imputed (dense) matrix.
>        - Much lower, as it only processes known ratings.
>- Accuracy
>    - Often poor due to inaccurate imputation.
>        - Generally much higher, as it learns from true data.
>- Model Flexibility
>    - A fixed mathematical decomposition.
>        - Flexible machine learning model (can add biases, regularization, etc.).
>- Orthogonality
>    - Produces orthogonal factors ($\mathbf{U}, \mathbf{V}$).
>        - Factors ($\mathbf{P}, \mathbf{Q}$) are not constrained to be orthogonal.
>
>**Conclusion:** For the use case of Collaborative Filtering on sparse user-item data, **Matrix Factorization models are vastly superior to pure SVD**. The ability to work directly with sparse data without imputation is the critical advantage. While SVD provides the theoretical underpinning for low-rank approximation, the practical algorithms used for CF are iterative, optimization-based methods that are inspired by, but not identical to, SVD.

## FunkSVD (The "SVD" of the Netflix Prize)
The confusion often stems from the famous Netflix Prize competition, where a winning method by Simon Funk was popularized under the name "FunkSVD". This algorithm is actually a [[Matrix_Factorization_for_CF|Matrix Factorization]] model trained with [[Stochastic_Gradient_Descent_SGD_for_CF|Stochastic Gradient Descent]]. It does not perform a true SVD but was named that way due to its similarity in finding a low-rank approximation. This has led to the terms SVD and MF being used interchangeably in the recommender system literature.

---