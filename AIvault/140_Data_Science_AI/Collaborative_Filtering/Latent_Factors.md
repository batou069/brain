---
tags:
  - data_science
  - collaborative_filtering
  - matrix_factorization
  - latent_factors
  - embeddings
  - concept
aliases:
  - Latent Vectors
  - User Embeddings
  - Item Embeddings
related:
  - "[[Matrix_Factorization_for_CF]]"
  - "[[Vector]]"
  - "[[Embeddings]]"
worksheet:
  - WS_Collaborative_Filtering_1
date_created: 2025-08-13
---
# Latent Factors

## Definition
In the context of [[Matrix_Factorization_for_CF|Matrix Factorization]] for collaborative filtering, **latent factors** (or latent vectors) are the low-dimensional vector representations of users and items. The term "latent" means hidden or unobserved; these factors are not present in the original data but are inferred by the model during training.

- **User Latent Vector ($p_u$):** A vector of size $k$ that represents user $u$. It captures the user's tastes and preferences along $k$ hidden dimensions.
- **Item Latent Vector ($q_i$):** A vector of size $k$ that represents item $i$. It captures the item's characteristics along the same $k$ hidden dimensions.

These vectors are essentially **[[Embeddings|embeddings]]** of users and items into a shared low-dimensional "preference space".

## Intuition and Meaning

>[!question] Are the latent vectors meaningful in any way?
>
>Yes, absolutely, though their meaning is often not explicit.
>
>1.  **Implicit Meaning:** The dimensions of the latent vectors are not pre-defined by humans. The model learns them automatically based on the patterns in the rating data. A single dimension might represent a concept like "serious vs. escapist films," "appeal to adults vs. children," or "high-budget action vs. low-budget indie." Often, a single dimension is a complex mixture of multiple concepts.
>
>2.  **Geometric Interpretation:** The power of latent factors lies in their geometric relationships in the shared $k$-dimensional space.
>        1. **Similarity:** Users with similar tastes will have latent vectors that are close to each other in this space. Similarly, items with similar characteristics (that appeal to the same types of users) will have latent vectors that are close together.
>        2. **Prediction:** The predicted rating is the dot product of the user and item vectors ($\hat{R}_{ui} = p_u \cdot q_i$). Geometrically, this means a user is predicted to like an item if their vectors are pointing in a similar direction and have large magnitudes. A high rating results from a strong alignment between a user's preference vector and an item's characteristic vector.
>
>3.  **Discovering Genres and Tastes:** We can analyze the learned latent vectors to discover hidden relationships. For example, we could use a [[Clustering_Methods|clustering]] algorithm on the item vectors to find "implicit genres" based on how users rate them, which might be different from explicit genre tags.

## Example of Latent Factors
Imagine a simplified model with $k=2$ latent factors for movies.
- **Factor 1:** Might range from "Action/Adventure" (-1) to "Comedy/Romance" (+1).
- **Factor 2:** Might range from "Mainstream/Blockbuster" (-1) to "Arthouse/Indie" (+1).

[list2tab|#Latent Factor Example]
- User/Movie
    - Vector
        - Interpretation
- **User A**
    - $p_A = [-0.9, -0.8]$
        - Strongly prefers mainstream action movies.
- **User B**
    - $p_B = [0.8, 0.9]$
        - Strongly prefers indie romantic comedies.
- **Movie X**
    - $q_X = [-1.0, -0.7]$
        - A quintessential mainstream action film.
- **Movie Y**
    - $q_Y = [0.7, 1.0]$
        - A classic indie romantic comedy.
- **Movie Z**
    - $q_Z = [-0.8, 0.9]$
        - An indie action film (rare combination).

**Predictions:**
- **User A on Movie X:** $\hat{R}_{AX} = p_A \cdot q_X = (-0.9)(-1.0) + (-0.8)(-0.7) = 0.9 + 0.56 = 1.46$ (High predicted rating).
- **User A on Movie Y:** $\hat{R}_{AY} = p_A \cdot q_Y = (-0.9)(0.7) + (-0.8)(1.0) = -0.63 - 0.8 = -1.43$ (Low predicted rating).
- **User B on Movie X:** $\hat{R}_{BX} = p_B \cdot q_X = (0.8)(-1.0) + (0.9)(-0.7) = -0.8 - 0.63 = -1.43$ (Low predicted rating).
- **User B on Movie Y:** $\hat{R}_{BY} = p_B \cdot q_Y = (0.8)(0.7) + (0.9)(1.0) = 0.56 + 0.9 = 1.46$ (High predicted rating).

This demonstrates how the dot product translates the alignment of latent factors into a rating prediction.

## Applications Beyond Recommendation
Once learned, these latent vectors (embeddings) can be used for other tasks:
- **Finding Similar Items:** Calculate the [[Cosine_Similarity|cosine similarity]] between item vectors to find items that are alike.
- **Finding Similar Users:** Find users with similar tastes for community-building features.
- **Visualization:** Use [[Principal_Component_Analysis_PCA|PCA]] or [[t_SNE|t-SNE]] to visualize the item or user space in 2D.

---