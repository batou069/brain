---
tags:
  - mathematics
  - linear_algebra
  - vector
  - cosine_similarity
  - similarity_measure
  - dot_product
  - concept
aliases:
  - Vector Cosine Similarity
related:
  - "[[Vector]]"
  - "[[Dot_Product]]"
  - "[[p-norm]]"
  - "[[Orthogonal_Vectors]]"
worksheet:
  - WS_Math_Foundations_1
date_created: 2025-05-30
---
# Cosine Similarity

## Definition
**Cosine similarity** is a measure of similarity between two non-zero [[Vector|vectors]] of an inner product space. It measures the cosine of the angle between them. This value is bounded between -1 and 1.

For two vectors $\mathbf{a}$ and $\mathbf{b}$, the cosine similarity, $\cos(\theta)$, is calculated using their [[Dot_Product|dot product]] and magnitudes (L2 [[p-norm|norms]]):
$$ \text{cosine similarity} = \cos(\theta) = \frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{a}\| \|\mathbf{b}\|} = \frac{\sum_{i=1}^{n} a_i b_i}{\sqrt{\sum_{i=1}^{n} a_i^2} \sqrt{\sum_{i=1}^{n} b_i^2}} $$
where:
- $\mathbf{a} \cdot \mathbf{b}$ is the dot product of vectors $\mathbf{a}$ and $\mathbf{b}$.
- $\|\mathbf{a}\|$ is the magnitude (Euclidean or L2 norm) of vector $\mathbf{a}$.
- $\|\mathbf{b}\|$ is the magnitude (Euclidean or L2 norm) of vector $\mathbf{b}$.

## Interpretation of Values
- **$\cos(\theta) = 1$**: The vectors point in the exact same direction (angle $\theta = 0^\circ$). Maximum similarity.
- **$\cos(\theta) = 0$**: The vectors are [[Orthogonal_Vectors|orthogonal]] (angle $\theta = 90^\circ$). No similarity (in terms of direction).
- **$\cos(\theta) = -1$**: The vectors point in exact opposite directions (angle $\theta = 180^\circ$). Maximum dissimilarity (or pointing in opposite directions).
- Values between 0 and 1 indicate an acute angle (some similarity in direction).
- Values between -1 and 0 indicate an obtuse angle (some dissimilarity in direction).

## Key Characteristics
[list2tab|#Cosine Similarity Characteristics]
- **Focus on Direction, Not Magnitude:** Cosine similarity is primarily concerned with the orientation (direction) of the vectors, not their magnitudes. Two vectors with very different lengths can still have a cosine similarity of 1 if they point in the same direction.
- **Range:** The value is always between -1 and 1, inclusive.
- **Common in High Dimensions:** It is particularly useful in high-dimensional spaces, where Euclidean distance can sometimes be misleading (due to the "curse of dimensionality").
- **Non-negativity (Optional):** In some applications, especially where vector components are non-negative (e.g., term frequencies in text documents), cosine similarity values will range from 0 to 1.

## Applications
- **Text Analysis / Document Similarity (Natural Language Processing - NLP):**
    - To measure the similarity between documents represented as term frequency vectors (e.g., TF-IDF vectors). Documents with similar content (and thus similar word frequencies) will have vectors pointing in similar directions.
- **Recommendation Systems:**
    - To find users with similar tastes or items with similar characteristics by comparing their respective feature vectors.
- **Information Retrieval:**
    - Ranking documents based on their similarity to a query vector.
- **Bioinformatics:**
    - Comparing gene expression profiles or protein sequences.
- **Image Recognition:**
    - Comparing feature vectors extracted from images.

## Example
Let $\mathbf{a} = (2, 1)$ and $\mathbf{b} = (4, 2)$.
- $\mathbf{a} \cdot \mathbf{b} = (2)(4) + (1)(2) = 8 + 2 = 10$
- $\|\mathbf{a}\| = \sqrt{2^2 + 1^2} = \sqrt{4 + 1} = \sqrt{5}$
- $\|\mathbf{b}\| = \sqrt{4^2 + 2^2} = \sqrt{16 + 4} = \sqrt{20} = 2\sqrt{5}$
- $\cos(\theta) = \frac{10}{\sqrt{5} \cdot 2\sqrt{5}} = \frac{10}{2 \cdot 5} = \frac{10}{10} = 1$.
The vectors point in the same direction ( $\mathbf{b}$ is a scalar multiple of $\mathbf{a}$, specifically $\mathbf{b} = 2\mathbf{a}$ ).

Let $\mathbf{c} = (1, 0)$ and $\mathbf{d} = (0, 1)$.
- $\mathbf{c} \cdot \mathbf{d} = (1)(0) + (0)(1) = 0$
- $\|\mathbf{c}\| = \sqrt{1^2 + 0^2} = 1$
- $\|\mathbf{d}\| = \sqrt{0^2 + 1^2} = 1$
- $\cos(\theta) = \frac{0}{1 \cdot 1} = 0$.
The vectors are orthogonal.

## Advantages and Disadvantages
**Advantages:**
- Effective in measuring orientation similarity, especially in high dimensions.
- Robust to differences in vector magnitudes.
- Bounded range makes interpretation easier.

**Disadvantages:**
- Ignores vector magnitudes, which might be important in some contexts.
- If vectors are centered (mean subtracted), it becomes equivalent to Pearson correlation coefficient.
- Can be computationally more intensive than Euclidean distance for dense vectors due to norm calculations, though often efficient for sparse vectors.

---