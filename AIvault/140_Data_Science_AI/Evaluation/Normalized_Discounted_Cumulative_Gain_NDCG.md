---
tags:
  - data_science
  - machine_learning
  - evaluation
  - metrics
  - ranking
  - ndcg
  - concept
aliases:
  - NDCG
related:
  - "[[Evaluation_Metrics_for_Ranking]]"
worksheet:
  - WS_Collaborative_Filtering_1
date_created: 2025-08-13
---
# Normalized Discounted Cumulative Gain (NDCG)

## Definition
**Normalized Discounted Cumulative Gain (NDCG)** is a measure of ranking quality that is widely used to evaluate recommender systems and search engines. It assesses the quality of a ranked list of items by considering both the **position** of items and their **graded relevance**.

NDCG is an improvement over simpler metrics because it rewards:
1.  Placing highly relevant items at the top of the list.
2.  Using a graded scale of relevance, not just binary (relevant/not relevant).

## Calculation Steps
The calculation of NDCG for a single user/query at a cutoff position $K$ involves three steps:

1.  **Cumulative Gain (CG@K):**
    The sum of the relevance scores of the top $K$ recommended items. It does not consider the position of the items.
    $$ \text{CG}_K = \sum_{i=1}^{K} \text{rel}_i $$
    where $\text{rel}_i$ is the relevance score of the item at position $i$.

2.  **Discounted Cumulative Gain (DCG@K):**
    An improvement on CG that penalizes relevant items that appear lower in the list. This is done by applying a logarithmic discount to the relevance scores based on their position.
    $$ \text{DCG}_K = \sum_{i=1}^{K} \frac{\text{rel}_i}{\log_2(i+1)} $$
    An alternative formulation that gives more weight to relevance is also common:
    $$ \text{DCG}_K = \sum_{i=1}^{K} \frac{2^{\text{rel}_i} - 1}{\log_2(i+1)} $$

3.  **Normalized Discounted Cumulative Gain (NDCG@K):**
    DCG scores can vary depending on the user and the number of relevant items. To get a score between 0 and 1 that is comparable across different queries, we normalize DCG by the **Ideal Discounted Cumulative Gain (IDCG)**. IDCG is the DCG score of a perfectly sorted list (all relevant items ranked by relevance at the top).
    $$ \text{NDCG}_K = \frac{\text{DCG}_K}{\text{IDCG}_K} $$
    - An NDCG of 1.0 represents a perfect ranking.
    - An NDCG of 0.0 represents the worst possible ranking.

## Python Example

```python
import numpy as np

def dcg_at_k(relevance_scores, k):
    """Calculates DCG@K for a list of relevance scores."""
    relevance_scores = np.asarray(relevance_scores)[:k]
    if relevance_scores.size:
        # Denominators are log2(2), log2(3), ..., log2(k+1)
        discounts = np.log2(np.arange(2, relevance_scores.size + 2))
        return np.sum(relevance_scores / discounts)
    return 0.0

def ndcg_at_k(recommended_relevance, k):
    """Calculates NDCG@K."""
    dcg = dcg_at_k(recommended_relevance, k)
    
    # To get IDCG, we sort the relevance scores in descending order
    ideal_relevance = sorted(recommended_relevance, reverse=True)
    idcg = dcg_at_k(ideal_relevance, k)
    
    if not idcg:
        return 0.0
    
    return dcg / idcg

# Example usage for a single user
# Assume relevance is a 0-5 scale.
# Model's recommended list has these relevance scores:
relevance_list = 
K = 5

ndcg_score = ndcg_at_k(relevance_list, K)

# Let's see the steps:
dcg_score = dcg_at_k(relevance_list, K)
ideal_list_at_5 = sorted(relevance_list[:K], reverse=True) #
idcg_score = dcg_at_k(ideal_list_at_5, K)

print(f"Relevance scores of top-{K} recs: {relevance_list[:K]}")
print(f"DCG@{K}: {dcg_score:.4f}")
print(f"Ideal order of scores for top-{K}: {ideal_list_at_5}")
print(f"IDCG@{K}: {idcg_score:.4f}")
print(f"\nNDCG@{K}: {ndcg_score:.4f}")

# Expected Output:
# Relevance scores of top-5 recs:
# DCG@5: 6.8614
# Ideal order of scores for top-5:
# IDCG@5: 7.1293
#
# NDCG@5: 0.9624
```

## Advantages
- **Position-Aware:** It heavily rewards placing relevant items at the very top of the list.
- **Handles Graded Relevance:** Unlike metrics that require binary relevance (hit/miss), NDCG can naturally use multi-level relevance scores (e.g., 1-5 star ratings), which provides a more nuanced evaluation.
- **Normalized:** The score is normalized to $[0, 1]$, making it easy to interpret and compare across different users or queries.

NDCG is considered a state-of-the-art metric for evaluating ranking quality in many information retrieval and recommender system tasks.

---