# K-means Algorithm Pseudocode

**Objective:** To partition a set of $n$ data points into $k$ distinct clusters, where each data point belongs to the cluster with the nearest mean.

**Notation:**
* $X = \{\vec{x}_1, \vec{x}_2, \dots, \vec{x}_n\}$: The set of $n$ data point vectors.
* $k$: The desired number of clusters.
* $C = \{\vec{\mu}_1, \vec{\mu}_2, \dots, \vec{\mu}_k\}$: The set of $k$ centroid vectors.
* $S_j$: The set of data points belonging to cluster $j$.

---

**Algorithm:** **K-means**

**Input:**
* Data points $X = \{\vec{x}_1, \dots, \vec{x}_n\}$
* Number of clusters $k$

**Output:**
* Set of centroids $C = \{\vec{\mu}_1, \dots, \vec{\mu}_k\}$
* Partition of data points into sets $S_1, \dots, S_k$

---

1.  **Initialize Centroids:**
* Select $k$ initial centroids $\{\vec{\mu}_1, \dots, \vec{\mu}_k\}$ from the dataset $X$. A common method is to choose $k$ points at random.
- *(Note: K-means++ is a more robust initialization method.)*

2.  **Repeat until convergence:**
* **Assignment Step:** For each data point $\vec{x}_i \in X$:
    * Assign $\vec{x}_i$ to the cluster $S_j$ corresponding to the nearest centroid $\vec{\mu}_j$. The distance is typically the squared Euclidean distance.
    * $j \leftarrow \underset{j \in \{1, \dots, k\}}{\arg\min} ||\vec{x}_i - \vec{\mu}_j||^2$
* Update the cluster sets: $S_j \leftarrow S_j \cup \{\vec{x}_i\}$
    * *(Ensure each point is only in one cluster per iteration by clearing sets $S_j$ at the start of the loop.)*
* **Update Step:** For each cluster $j \in \{1, \dots, k\}$:
    * Recalculate the centroid $\vec{\mu}_j$ as the mean of all data points in its cluster $S_j$.
    * $\vec{\mu}_j \leftarrow \frac{1}{|S_j|} \sum_{\vec{x} \in S_j} \vec{x}$

3.  **Return** the set of centroids $C$ and the final cluster assignments $S_1, \dots, S_k$.

---

**Convergence:** The algorithm has converged when the cluster assignments no longer change between iterations, or when the change in the centroid positions falls below a small tolerance threshold $\epsilon$.