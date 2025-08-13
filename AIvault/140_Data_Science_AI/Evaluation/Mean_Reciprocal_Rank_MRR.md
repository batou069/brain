---
tags:
  - data_science
  - machine_learning
  - evaluation
  - metrics
  - ranking
  - mrr
  - concept
aliases:
  - MRR
related:
  - "[[Evaluation_Metrics_for_Ranking]]"
worksheet:
  - WS_Collaborative_Filtering_1
date_created: 2025-08-13
---
# Mean Reciprocal Rank (MRR)

## Definition
**Mean Reciprocal Rank (MRR)** is a statistic used to evaluate systems that produce a ranked list of responses to a query or user need. The reciprocal rank of a query response is the multiplicative inverse of the rank of the *first* correct or relevant answer. The MRR is the average of the reciprocal ranks for a set of queries $Q$.

## Calculation
For a single query, the **Reciprocal Rank (RR)** is:
$$ \text{RR} = \frac{1}{\text{rank}_1} $$
where $\text{rank}_1$ is the position (rank) of the first relevant item in the recommended list. If no relevant item is found in the list, the reciprocal rank is 0.

The **Mean Reciprocal Rank (MRR)** is the average of the RR scores over all queries in the set $Q$:
$$ \text{MRR} = \frac{1}{|Q|} \sum_{i=1}^{|Q|} \frac{1}{\text{rank}_i} $$

## Interpretation
- The MRR score is between 0 and 1.
- A score of 1 means that for every query, the first relevant item was found at the very first position.
- A score of 0 means no relevant items were found for any query.
- A higher MRR score indicates that the system is better at returning a relevant item quickly at the top of the list.

## Key Characteristics
- **Focus on the First Hit:** MRR only cares about the rank of the single highest-ranked relevant item. It completely ignores the position of any other relevant items in the list.
- **Simplicity:** It is simple to calculate and interpret.

## Python Example

```python
def calculate_mrr(recommendations_list):
    """
    Calculates the Mean Reciprocal Rank for a list of recommendation scenarios.
    
    :param recommendations_list: A list of tuples, where each tuple is
                                 (ranked_list, set_of_relevant_items).
    :return: The MRR score.
    """
    reciprocal_ranks = []
    for ranked_list, relevant_set in recommendations_list:
        rr = 0.0
        for i, item in enumerate(ranked_list):
            if item in relevant_set:
                rr = 1.0 / (i + 1) # i is 0-indexed, rank is 1-indexed
                break # Found the first relevant item, stop
        reciprocal_ranks.append(rr)
        
    return np.mean(reciprocal_ranks) if reciprocal_ranks else 0.0

# Example usage with multiple "queries" (users)
import numpy as np

# User 1: First relevant item is at rank 3
user1_recs = (, {301, 800}) # RR = 1/3
# User 2: First relevant item is at rank 1
user2_recs = (, {408, 901}) # RR = 1/1
# User 3: No relevant items in the list
user3_recs = (, {500, 800}) # RR = 0

all_user_scenarios = [user1_recs, user2_recs, user3_recs]

mrr_score = calculate_mrr(all_user_scenarios)

print(f"Reciprocal Ranks for each user: [1/3, 1/1, 0] = {[1/3, 1.0, 0.0]}")
print(f"\nMean Reciprocal Rank (MRR): {mrr_score:.4f}")

# Expected Output:
# Reciprocal Ranks for each user: [1/3, 1/1, 0] = [0.3333333333333333, 1.0, 0.0]
#
# Mean Reciprocal Rank (MRR): 0.4444
```

## Use Cases and Limitations
**Best Use Cases:**
- MRR is ideal for tasks where the user is likely only interested in finding a single correct answer, and finding it quickly is important.
- **Question Answering:** Finding the single best document that answers a question.
- **"I'm feeling lucky" style searches:** Where the goal is to take the user directly to the best result.
- **Fact retrieval.**

**Limitations:**
- **Ignores Other Relevant Items:** It does not measure the overall quality of the ranking beyond the first correct item. A list with one relevant item at rank 2 gets the same score (0.5) as a list with five relevant items starting at rank 2.
- **Not Ideal for General Search/Recommendation:** For tasks where a user wants to see a variety of relevant options (like a typical e-commerce search or movie recommendation), metrics like [[Normalized_Discounted_Cumulative_Gain_NDCG|NDCG]] or Mean Average Precision (MAP) are more appropriate because they consider the entire ranked list.

---