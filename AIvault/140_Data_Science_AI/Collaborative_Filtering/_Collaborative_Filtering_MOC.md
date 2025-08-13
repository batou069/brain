---
tags:
  - data_science
  - machine_learning
  - recommender_systems
  - collaborative_filtering
  - moc
aliases:
  - CF MOC
  - Collaborative Filtering
related:
  - "[[_Data_Science_AI_MOC]]"
  - "[[Supervised_Learning]]"
  - "[[Unsupervised_Learning]]"
worksheet:
  - WS_Collaborative_Filtering_1
date_created: 2025-08-13
---
# Collaborative Filtering MOC

**Collaborative Filtering (CF)** is a technique used by recommender systems. The core idea is to make automatic predictions (filtering) about the interests of a user by collecting preferences or taste information from many users (collaborating). The underlying assumption is that if person A has the same opinion as person B on an issue, A is more likely to have B's opinion on a different issue than that of a randomly chosen person.

This chapter explores the foundational concepts, models, and challenges related to building a movie recommendation system using collaborative filtering.

## Foundational Concepts
- **[[User-Item_Interaction_Matrix|User-Item Interaction Matrix]]:** The core data structure representing user preferences.
- **[[Implicit_vs_Explicit_Feedback|Implicit vs. Explicit Feedback]]:** The two main types of user data used for recommendations.

## Core Modeling Techniques
- **[[Matrix_Factorization_for_CF|Matrix Factorization]]:** The primary technique for modern collaborative filtering, which decomposes the interaction matrix into low-dimensional [[Latent_Factors|latent factors]] for users and items.
- **[[Matrix_Factorization_vs_SVD_for_CF|Comparison with SVD]]:** Understanding the practical differences between general Matrix Factorization and pure [[Singular_Value_Decomposition|SVD]] in the context of CF.
- **Optimization Algorithms:**
    - **[[Alternating_Least_Squares_ALS|Alternating Least Squares (ALS)]]**
    - **[[Stochastic_Gradient_Descent_SGD_for_CF|Stochastic Gradient Descent (SGD)]]**

## Key Challenges
- **[[Cold_Start_Problem|The Cold Start Problem]]:** How to make recommendations for new users or new items.
- **[[Concept_Drift_in_Recommenders|Concept Drift]]:** Handling changes in user preferences and item popularity over time.
- **Scalability:** Dealing with massive datasets (millions of users and items).

## Alternative & Hybrid Approaches
- **[[Content-Based_Filtering|Content-Based Filtering]]:** An alternative paradigm based on item attributes.
- **[[Hybrid_Recommender_Systems|Hybrid Recommender Systems]]:** Combining collaborative filtering with other methods to improve performance and address challenges like the cold start problem.

## Evaluation
- **[[Evaluation_Metrics_for_Ranking|Evaluation Metrics for Ranking]]:** Assessing the quality of a ranked recommendation list.
    - **[[Normalized_Discounted_Cumulative_Gain_NDCG|Normalized Discounted Cumulative Gain (NDCG)]]**
    - **[[Mean_Reciprocal_Rank_MRR|Mean Reciprocal Rank (MRR)]]**

## Notes in this Section
```dataview
LIST
FROM "140_Data_Science_AI/Collaborative_Filtering"
WHERE file.folder = this.file.folder AND file.name != this.file.name AND !contains(file.name, "MOC")
SORT file.name ASC
```

---