---
tags:
  - data_science
  - collaborative_filtering
  - matrix_factorization
  - optimization
  - sgd
  - concept
aliases:
  - SGD for Matrix Factorization
related:
  - "[[Matrix_Factorization_for_CF]]"
  - "[[Alternating_Least_Squares_ALS]]"
  - "[[Gradient_Descent]]"
  - "[[Loss_Function]]"
worksheet:
  - WS_Collaborative_Filtering_1
date_created: 2025-08-13
---
# Stochastic Gradient Descent (SGD) for Collaborative Filtering

## Definition
**Stochastic Gradient Descent (SGD)** is an iterative optimization algorithm commonly used to train [[Matrix_Factorization_for_CF|Matrix Factorization]] models, particularly for explicit feedback datasets. It is an efficient and simple way to minimize the [[Loss_Function|loss function]] associated with the model.

Unlike batch [[Gradient_Descent|Gradient Descent]] which computes the gradient using the entire dataset, SGD approximates the gradient using a single training example at a time.

## The Optimization Problem
The regularized loss function for matrix factorization with explicit ratings is:
$$ L = \sum_{(u,i) \in K} (R_{ui} - p_u \cdot q_i)^2 + \lambda \left( \sum_u \|p_u\|^2 + \sum_i \|q_i\|^2 \right) $$
To minimize this using SGD, we process one known rating $R_{ui}$ at a time.

## Algorithm Steps
1.  **Initialize:** Initialize the user-factor matrix $\mathbf{P}$ and the item-factor matrix $\mathbf{Q}$ with small random values. Also initialize user biases $b_u$ and item biases $b_i$ to zero if using them.
2.  **Loop:** Repeat for a fixed number of epochs (passes through the entire training data):
    a.  Shuffle the training data (the set $K$ of known ratings).
    b.  **Iterate:** For each known rating $R_{ui}$ in the training data:
        i.   **Calculate Prediction Error:**
             $$ e_{ui} = R_{ui} - \hat{R}_{ui} = R_{ui} - (p_u \cdot q_i) $$
             (If including biases, $\hat{R}_{ui} = \mu + b_u + b_i + p_u \cdot q_i$)
        ii.  **Compute Gradients:** Calculate the partial derivatives of the squared error term $(e_{ui})^2$ plus the regularization term with respect to the parameters $p_u$ and $q_i$.
             $$ \frac{\partial L}{\partial p_{uf}} = -2 e_{ui} q_{if} + 2\lambda p_{uf} $$
             $$ \frac{\partial L}{\partial q_{if}} = -2 e_{ui} p_{uf} + 2\lambda q_{if} $$
        iii. **Update Factors:** Update the user and item latent vectors by taking a small step in the opposite direction of the gradient.
             $$ p_u \leftarrow p_u - \eta \left( -e_{ui} q_i + \lambda p_u \right) $$
             $$ q_i \leftarrow q_i - \eta \left( -e_{ui} p_u + \lambda q_i \right) $$
             (where $\eta$ is the learning rate, a hyperparameter).
3.  **Termination:** After the final epoch, the learned matrices $\mathbf{P}$ and $\mathbf{Q}$ are ready.

## Python Example (Conceptual)
A full implementation is lengthy, but the core update step can be illustrated.

```python
import numpy as np

# Assume P, Q, ratings are initialized
# P: user_factors, Q: item_factors
# ratings: list of (user_id, item_id, rating) tuples

def train_sgd(ratings, P, Q, learning_rate=0.01, lambda_reg=0.1, epochs=20):
    for epoch in range(epochs):
        # Shuffle data for each epoch
        np.random.shuffle(ratings)
        
        for user_id, item_id, rating in ratings:
            # Get user and item vectors
            p_u = P[user_id]
            q_i = Q[item_id]
            
            # Calculate prediction and error
            prediction = np.dot(p_u, q_i)
            error = rating - prediction
            
            # Update factors with gradients
            P[user_id] += learning_rate * (error * q_i - lambda_reg * p_u)
            Q[item_id] += learning_rate * (error * p_u - lambda_reg * q_i)
            
    return P, Q

# --- Conceptual Usage ---
# num_users = 100
# num_items = 200
# num_factors = 10
# P = np.random.rand(num_users, num_factors) * 0.1
# Q = np.random.rand(num_items, num_factors) * 0.1
# ratings = [...] # Load your training data
# P_trained, Q_trained = train_sgd(ratings, P, Q)
# print("Training complete. P and Q matrices are now learned.")
```

## Advantages and Disadvantages
**Advantages:**
- **Simplicity:** Relatively easy to implement.
- **Flexibility:** Can easily accommodate different loss functions and models.
- **Online Learning:** Well-suited for online settings where new ratings arrive continuously, as the model can be updated one rating at a time without retraining on the whole dataset.
- **Efficiency:** Can be faster than [[Alternating_Least_Squares_ALS|ALS]] on single-machine, explicit feedback datasets, as it doesn't require complex matrix operations.

**Disadvantages:**
- **Sequential Nature:** Harder to parallelize compared to ALS.
- **Hyperparameter Tuning:** Requires careful tuning of the learning rate ($\eta$) and regularization parameter ($\lambda$).
- **Slower Convergence:** May require many epochs to converge to a good solution.
- **Less Ideal for Implicit Feedback:** While adaptable, it's often less efficient than specialized ALS for implicit feedback scenarios where the loss is calculated over all (including unobserved) pairs.

For a detailed comparison with ALS, see [[Alternating_Least_Squares_ALS]].

---