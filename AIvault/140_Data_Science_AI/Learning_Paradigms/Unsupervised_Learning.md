---
tags:
  - data_science
  - machine_learning
  - unsupervised_learning
  - learning_paradigm
  - concept
aliases:
  - Unsupervised ML
related:
  - "[[Supervised_Learning]]"
  - "[[Reinforcement_Learning]]"
  - "[[Clustering_Methods]]"
  - "[[Dimensionality_Reduction]]"
  - "[[Anomaly_Detection]]"
worksheet:
  - WS_Math_Foundations_2
date_created: 2025-08-07
---
# Unsupervised Learning

## Definition
**Unsupervised learning** is one of the three main paradigms of machine learning, alongside [[Supervised_Learning|supervised learning]] and [[Reinforcement_Learning|reinforcement learning]]. It is characterized by the use of **unlabeled data**.

In unsupervised learning, the algorithm is given a dataset without explicit instructions on what to do with it. The goal is to explore the data and find some inherent structure, patterns, or relationships within it. The algorithm tries to learn these patterns without any corresponding output labels or feedback.

## Types of Unsupervised Learning Problems
Unsupervised learning can be broadly categorized into several types of tasks:

[list2tab|#Unsupervised Problem Types]
- Clustering
    - **Goal:** Group similar data points together into clusters. Data points in the same cluster are more similar to each other than to those in other clusters.
    - **Output:** A set of cluster labels for each data point.
    - **Examples:**
        - Segmenting customers into different groups based on their purchasing behavior.
        - Grouping similar news articles or documents.
        - Image segmentation to separate different objects in an image.
    - **Common Algorithms:** See [[Clustering_Methods]].
- Dimensionality Reduction
    - **Goal:** Reduce the number of features (variables) in a dataset while preserving as much of the important information as possible.
    - **Output:** A lower-dimensional representation of the original data.
    - **Examples:**
        - Compressing data for more efficient storage or computation.
        - Visualizing high-dimensional data in 2D or 3D.
        - Preprocessing for supervised learning algorithms to mitigate the curse of dimensionality.
    - **Common Algorithms:** See [[Dimensionality_Reduction]].
- Association Rule Mining
    - **Goal:** Discover interesting relationships or "association rules" among variables in large datasets.
    - **Output:** Rules of the form "If A, then B" (e.g., "If a customer buys bread, they are likely to also buy milk").
    - **Examples:**
        - Market basket analysis to understand which products are frequently bought together.
        - Recommender systems.
    - **Common Algorithms:** Apriori, Eclat, FP-Growth.
- Anomaly Detection
    - **Goal:** Identify rare items, events, or observations which raise suspicions by differing significantly from the majority of the data.
    - **Output:** A label indicating whether a data point is an anomaly or not.
    - **Examples:**
        - Fraud detection in credit card transactions.
        - Identifying defective products in manufacturing.
        - Network intrusion detection.
    - **Common Algorithms:** Isolation Forest, One-Class SVM.

## Diagram: Unsupervised Learning Process

```mermaid
graph TD
    A[Unlabeled Data (Features Only)] --> B[Machine Learning Algorithm];
    B -- Discovers Patterns --> C{Inferred Structure};
    
    subgraph Example_Outputs
        C --> D[Clusters];
        C --> E[Lower-Dimensional Data];
        C --> F[Association Rules];
        C --> G[Anomalies];
    end

    style C fill:#afa,stroke:#333,stroke-width:2px
```

## Key Characteristics
- **No Labels:** The defining feature is the absence of a target variable or ground truth.
- **Exploratory:** The goal is often to discover hidden patterns rather than to predict a specific output.
- **Evaluation is Subjective:** Evaluating the performance of an unsupervised model can be more challenging than for supervised models, as there is no single "correct" answer. Evaluation often involves qualitative assessment or proxy metrics (e.g., silhouette score for clustering).

Unsupervised learning is a powerful tool for understanding complex datasets and is often used as a preliminary step in a larger data analysis or supervised learning pipeline.

---