---
tags:
  - data_science
  - collaborative_filtering
  - matrix_factorization
  - optimization
  - als
  - concept
aliases:
  - ALS
related:
  - "[[Matrix_Factorization_for_CF]]"
  - "[[Stochastic_Gradient_Descent_SGD_for_CF]]"
  - "[[Linear_Least_Squares]]"
  - "[[Loss_Function]]"
  - "[[Implicit_vs_Explicit_Feedback]]"
worksheet:
  - WS_Collaborative_Filtering_1
date_created: 2025-08-13
---
# Alternating Least Squares (ALS)

## Definition
**Alternating Least Squares (ALS)** is an iterative optimization algorithm used to find the latent factors in [[Matrix_Factorization_for_CF|Matrix Factorization]] for collaborative filtering. It is particularly well-suited for this problem because it can be parallelized and adapted for both explicit and implicit feedback datasets.

The core idea of ALS is to solve for the user-factor matrix $\mathbf{P}$ and the item-factor matrix $\mathbf{Q}$ alternately, holding one constant while optimizing the other.

## The Optimization Problem
The [[Loss_Function|loss function]] for matrix factorization is:
$$ L = \sum_{(u,i) \in K} (R_{ui} - p_u \cdot q_i)^2 + \lambda \left( \sum_u \|p_u\|^2 + \sum_i \|q_i\|^2 \right) $$
This function is non-convex if we try to solve for both $\mathbf{P}$ and $\mathbf{Q}$ simultaneously. However, if we fix one of the matrices ($\mathbf{P}$ or $\mathbf{Q}$), the problem becomes a standard [[Linear_Least_Squares|least squares]] problem with L2 regularization (Ridge Regression) for the other matrix, which is convex and can be solved optimally.

## Algorithm Steps
1.  **Initialize:** Initialize the user-factor matrix $\mathbf{P}$ and the item-factor matrix $\mathbf{Q}$ with small random values.
2.  **Alternate:** Repeat the following steps for a fixed number of iterations or until convergence:
    a.  **Fix $\mathbf{Q}$, Solve for $\mathbf{P}$:** Treat the item vectors $q_i$ as constant. For each user $u$, the loss function becomes a quadratic function of their latent vector $p_u$. We can solve for the optimal $p_u$ that minimizes the error for all items rated by that user. This can be done independently for each user, making this step highly parallelizable.
       $$ p_u \leftarrow \left( \sum_{i \in R_u} q_i q_i^T + \lambda I \right)^{-1} \left( \sum_{i \in R_u} R_{ui} q_i \right) $$
       (where $R_u$ is the set of items rated by user $u$)
    b.  **Fix $\mathbf{P}$, Solve for $\mathbf{Q}$:** Treat the user vectors $p_u$ as constant. For each item $i$, solve for the optimal latent vector $q_i$ that minimizes the error for all users who rated that item. This step is also highly parallelizable across items.
       $$ q_i \leftarrow \left( \sum_{u \in U_i} p_u p_u^T + \lambda I \right)^{-1} \left( \sum_{u \in U_i} R_{ui} p_u \right) $$
       (where $U_i$ is the set of users who rated item $i$)
3.  **Termination:** After the final iteration, the learned matrices $\mathbf{P}$ and $\mathbf{Q}$ can be used to make predictions.

## ALS for Implicit Feedback
ALS is particularly popular for [[Implicit_vs_Explicit_Feedback|implicit feedback]] datasets. The model is adapted as follows:
- The interaction matrix $\mathbf{R}$ is replaced by a binary preference matrix $\mathbf{Pref}$, where $Pref_{ui} = 1$ if an interaction occurred and $0$ otherwise.
- A confidence matrix $\mathbf{C}$ is introduced. The confidence $C_{ui}$ is low for unobserved interactions (0s) and higher for observed interactions (1s). A common formulation is $C_{ui} = 1 + \alpha \cdot \mathrm{interactioncount}_{ui}$.
- The loss function is modified to be a weighted sum, giving more importance to fitting the observed interactions:
  $$ L = \sum_{u,i} C_{ui} (Pref_{ui} - p_u \cdot q_i)^2 + \lambda \left( \sum_u \|p_u\|^2 + \sum_i \|q_i\|^2 \right) $$

## ALS vs. SGD

>[!question] When would you prefer to use ALS rather than SGD?
>
>Both ALS and [[Stochastic_Gradient_Descent_SGD_for_CF|Stochastic Gradient Descent (SGD)]] are effective for training matrix factorization models, but they have different strengths and weaknesses.
>
>[list2tab|#ALS vs SGD]
>- Aspect
>    - Alternating Least Squares (ALS)
>        - Stochastic Gradient Descent (SGD)
>- Parallelization
>    - **Highly parallelizable.** Each user/item factor can be updated independently within an iteration. Ideal for distributed systems like Spark.
>        - Inherently sequential. Updates are made one rating at a time, making parallelization more complex.
>- Convergence
>    - Faster convergence (fewer iterations) as it solves an exact least-squares problem in each step.
>        - Slower convergence (more iterations) as it takes small steps. Requires careful tuning of learning rate.
>- Data Type
>    - **The standard choice for implicit feedback** due to its efficient handling of the weighted loss function over all user-item pairs.
>        - Works well for explicit feedback. Can be adapted for implicit feedback but is often less efficient than ALS.
>- Implementation
>    - Can be more complex to implement from scratch due to matrix inversions.
>        - Simpler to implement.
>- New Data
>    - Less flexible for online learning where new ratings arrive continuously.
>        - More flexible for online learning; can easily update factors with new ratings.
>
>**Conclusion:**
>- **Choose ALS when:**
>    - You have a large-scale, static dataset.
>    - You can leverage parallel/distributed computing (e.g., using Apache Spark).
>    - You are working with **implicit feedback** data (this is the key use case).
>- **Choose SGD when:**
>    - You need an online learning system that can update quickly with new data.
>    - You are working with explicit feedback on a single machine and want a simpler implementation.
>    - You cannot use a distributed framework.

---