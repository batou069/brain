---
tags:
  - data_science
  - collaborative_filtering
  - recommender_systems
  - matrix
  - concept
aliases:
  - Utility Matrix
  - User-Item Matrix
related:
  - "[[_Collaborative_Filtering_MOC]]"
  - "[[Matrix]]"
  - "[[Implicit_vs_Explicit_Feedback]]"
  - "[[Matrix_Factorization_for_CF]]"
worksheet:
  - WS_Collaborative_Filtering_1
date_created: 2025-08-13
---
# User-Item Interaction Matrix

## Definition
The **User-Item Interaction Matrix** (also known as the **utility matrix** or **ratings matrix**) is the fundamental data structure used in [[_Collaborative_Filtering_MOC|Collaborative Filtering]]. It is a [[Matrix|matrix]] that represents the interactions between users and items.

- **Rows** typically represent users.
- **Columns** typically represent items (e.g., movies, products, songs).
- **Entries** in the matrix, $R_{ui}$, represent the interaction of user $u$ with item $i$.

The nature of the entries depends on the type of feedback collected. See [[Implicit_vs_Explicit_Feedback]].

## Structure
Let $\mathbf{R}$ be a user-item interaction matrix with $m$ users and $n$ items.
$$
\mathbf{R} =
\begin{pmatrix}
R_{11} & R_{12} & \dots & R_{1n} \\
R_{21} & R_{22} & \dots & R_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
R_{m1} & R_{m2} & \dots & R_{mn}
\end{pmatrix}
$$
- $R_{ui}$: The rating given by user $u$ to item $i$.

## Key Characteristic: Sparsity
In real-world scenarios, this matrix is almost always **extremely sparse**. This means that most of its entries are empty or unknown. A typical user has only interacted with (e.g., rated, purchased, viewed) a tiny fraction of the total available items.

- **Example:** In the MovieLens 100k dataset, there are 943 users and 1682 movies, leading to $943 \times 1682 = 1,586,126$ possible ratings. However, the dataset only contains 100,000 ratings.
- **Sparsity Calculation:**
  $$ \text{Sparsity} = 1 - \frac{\text{Number of Non-zero Entries}}{\text{Total Number of Entries}} $$
  For MovieLens 100k: $1 - \frac{100,000}{1,586,126} \approx 1 - 0.063 = 0.937$, or **93.7% sparse**. For larger datasets like Netflix or Amazon, sparsity is often >99.9%.

## The Goal of Collaborative Filtering
The primary goal of collaborative filtering is to **predict the missing values** in this sparse matrix. By predicting the rating a user *would* give to an item they haven't seen yet, the system can recommend items with the highest predicted ratings.

## Python Example (Conceptual)
We can represent a sparse user-item matrix using a Pandas DataFrame, often created from a long-format data file.

```python
import pandas as pd
import numpy as np

# Sample data similar to MovieLens format: (user_id, item_id, rating)
data = {
    'user_id':,
    'movie_id':,
    'rating':
}
df = pd.DataFrame(data)

# Create the user-item interaction matrix using pivot_table
# Missing values (NaN) represent the sparsity
utility_matrix = df.pivot_table(index='user_id', columns='movie_id', values='rating')

print("Original data (long format):\n", df)
print("\nUser-Item Interaction Matrix (sparse):\n", utility_matrix)

# Expected Output:
# Original data (long format):
#    user_id  movie_id  rating
# 0        1       101       5
# 1        1       102       3
# 2        2       101       4
# 3        2       103       5
# 4        3       102       2
# 5        3       103       4
# 6        3       104       5
#
# User-Item Interaction Matrix (sparse):
# movie_id  101  102  103  104
# user_id                      
# 1         5.0  3.0  NaN  NaN
# 2         4.0  NaN  5.0  NaN
# 3         NaN  2.0  4.0  5.0
```
The task of [[Matrix_Factorization_for_CF|Matrix Factorization]] is to learn latent factors that can reconstruct this matrix, filling in the `NaN` values with predictions.

---