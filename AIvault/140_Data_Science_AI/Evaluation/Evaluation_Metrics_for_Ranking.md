---
tags:
  - data_science
  - machine_learning
  - evaluation
  - metrics
  - ranking
  - recommender_systems
  - concept
aliases:
  - Ranking Metrics
related:
  - "[[Model_Evaluation]]"
  - "[[_Collaborative_Filtering_MOC]]"
  - "[[Normalized_Discounted_Cumulative_Gain_NDCG]]"
  - "[[Mean_Reciprocal_Rank_MRR]]"
  - "[[Precision_Recall_at_K]]"
worksheet:
  - WS_Collaborative_Filtering_1
date_created: 2025-08-13
---
# Evaluation Metrics for Ranking

## Definition
In many machine learning applications, such as recommender systems or information retrieval (search engines), the goal is not just to predict a score or a class, but to produce an **ordered list** of items. **Evaluation metrics for ranking** are designed to assess the quality of these ordered lists.

Unlike standard classification metrics (like accuracy), ranking metrics care about the **position** of the relevant items in the recommended list. A relevant item at the top of the list is much better than a relevant item at the bottom.

## Key Concepts in Ranking Evaluation
- **Relevance:** A binary or graded judgment of how useful an item is for a given user or query. In a movie recommender, a "relevant" item might be a movie the user actually watched or rated highly (e.g., 4 or 5 stars).
- **Cutoff @K:** Since users rarely look at hundreds of recommendations, ranking metrics are often calculated on only the top *K* items in the list (e.g., top 5, 10, or 20). This is denoted as `@K`.

## Common Ranking Metrics
[list2tab|#Ranking Metrics]
- Precision@K / Recall@K
    - **Description:** Simple adaptations of precision and recall for ranking.
    - **Precision@K:** The proportion of recommended items in the top-K set that are relevant.
      $$ \text{Precision@K} = \frac{|\{\text{Relevant items}\} \cap \{\text{Top-K items}\}|}{K} $$
    - **Recall@K:** The proportion of all relevant items that are in the top-K set.
      $$ \text{Recall@K} = \frac{|\{\text{Relevant items}\} \cap \{\text{Top-K items}\}|}{|\{\text{All Relevant Items}\}|} $$
    - **Limitation:** They treat all positions within the top K equally and ignore the order.
- MRR
    - **Description:** [[Mean_Reciprocal_Rank_MRR|Mean Reciprocal Rank (MRR)]] is a metric that focuses on the rank of the *first* relevant item in the list. It is the average of the reciprocal ranks over all users/queries.
    - **Use Case:** Best for tasks where finding just one correct item is the main goal (e.g., question answering, "I'm feeling lucky" searches).
- MAP
    - **Description:** Mean Average Precision (MAP) is the mean of the Average Precision (AP) scores over all users/queries. AP rewards a model for placing many relevant items at the top of the list.
    - **Use Case:** Good for tasks where finding multiple relevant items is important (e.g., a standard search engine result page).
- NDCG
    - **Description:** [[Normalized_Discounted_Cumulative_Gain_NDCG|Normalized Discounted Cumulative Gain (NDCG)]] is a sophisticated metric that evaluates the entire ranking and has two key features:
        1.  It gives higher weight to relevant items that appear earlier in the list (Discounted).
        2.  It can handle graded relevance scores (e.g., 1-5 star ratings), not just binary relevance (Cumulative Gain).
        3.  It is normalized to a value between 0 and 1.
    - **Use Case:** The standard and most robust metric for evaluating ranked lists, especially when relevance is not binary.

## Python Example: Precision@K and Recall@K
```python
def precision_recall_at_k(recommended_items, relevant_items, k):
    """
    Calculates Precision@K and Recall@K.
    """
    # Ensure recommended_items is a list of unique items
    top_k_recs = recommended_items[:k]
    
    # Find the intersection of recommended and relevant items
    hits = set(top_k_recs) & set(relevant_items)
    
    # Calculate Precision@K
    precision = len(hits) / k if k > 0 else 0.0
    
    # Calculate Recall@K
    recall = len(hits) / len(relevant_items) if len(relevant_items) > 0 else 0.0
    
    return precision, recall

# Example usage for a single user
recommended_list = # Model's ranked output
ground_truth = # All items the user actually liked
K = 5

p_at_k, r_at_k = precision_recall_at_k(recommended_list, ground_truth, K)

print(f"Recommended Top-{K}: {recommended_list[:K]}")
print(f"Relevant Items: {ground_truth}")
print(f"Hits in Top-{K}: {set(recommended_list[:K]) & set(ground_truth)}")
print(f"\nPrecision@{K}: {p_at_k:.2f}")
print(f"Recall@{K}: {r_at_k:.2f}")

# Expected Output:
# Recommended Top-5:
# Relevant Items:
# Hits in Top-5: {500, 301}
#
# Precision@5: 0.40
# Recall@5: 0.50
```

---