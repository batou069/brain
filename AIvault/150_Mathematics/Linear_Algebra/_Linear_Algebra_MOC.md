---
tags:
  - mathematics
  - linear_algebra
  - vectors
  - matrices
  - moc
aliases:
  - Linear Algebra MOC
  - Vectors and Matrices MOC
related:
  - "[[_Mathematics_MOC]]"
  - "[[Vector]]"
  - "[[Matrix]]"
worksheet:
  - WS_Math_Foundations_1
date_created: 2025-05-30
---
# Linear Algebra (Vectors & Matrices) MOC

Linear algebra is a branch of mathematics concerning [[Vector|vector spaces]] and linear mappings between such spaces. It includes the study of lines, planes, and subspaces, but is also concerned with properties common to all vector spaces. It is a cornerstone of modern mathematics and is indispensable in Data Science and Machine Learning for representing and manipulating data.

## Core Concepts

[list2tab|#Linear Algebra Topics]
- Vectors
    - [[Vector|Definition and Properties]]
    - [[Row_Vector|Row Vector]] vs. [[Column_Vector|Column Vector]]
    - [[Vector_Operations|Vector Operations]] (Addition, Scalar Multiplication)
    - [[Dot_Product|Dot Product (Inner Product)]]
    - [[p-norm|Vector Norms (p-norm)]] (e.g., L1, L2, L-infinity norms)
    - [[Cosine_Similarity|Cosine Similarity]]
- Matrices
    - [[Matrix|Definition and Properties]]
    - [[Matrix_Operations|Matrix Operations]] (Addition, Scalar Multiplication)
    - [[Matrix_Product|Matrix Product]]
        - [[Matrix_Multiplication_Associativity|Associativity and Optimal Order]]
        - [[Matrix_Multiplication_Complexity|Complexity]]
    - [[Hadamard_Product|Hadamard Product (Element-wise Product)]]
    - [[Element_wise_Matrix_Operations|Other Element-wise Operations]]
    - [[Transpose_Matrix|Transpose of a Matrix]]
    - [[Matrix_Inversion|Matrix Inversion]] and its [[Matrix_Inversion_Complexity|Complexity]]
    - [[Determinant_Matrix|Determinant of a Matrix]]
    - [[Transformation_Matrix|Transformation Matrix]]
        - [[Matrix_Transformations_and_Distance|Effect on Distances]]
    - Special Matrices (Identity, Diagonal, Symmetric, Orthogonal)
- Eigen-Decomposition & Singular Value Decomposition (SVD)
    - [[Eigenvalues_Eigenvectors|Eigenvalues and Eigenvectors]]
    - [[Singular_Value_Decomposition|Singular Values and Singular Vectors (SVD)]]
- Advanced Topics
    - [[Matrix_Calculus|Matrix Calculus]] (see also [[_Calculus_MOC]])
    - [[Vector_Space|Vector Spaces and Subspaces]]
    - [[Linear_Independence_Basis_Dimension|Linear Independence, Basis, and Dimension]]

## Applications in AI/ML
- **Data Representation:** Datasets are often represented as matrices (samples as rows, features as columns). Individual samples can be vectors.
- **Dimensionality Reduction:** Techniques like PCA (Principal Component Analysis) rely heavily on eigenvalues/eigenvectors and SVD.
- **Recommendation Systems:** Matrix factorization techniques (related to SVD) are common.
- **Natural Language Processing (NLP):** Word embeddings represent words as vectors.
- **Computer Graphics & Vision:** Transformations (scaling, rotation, translation) are represented by matrices.
- **Solving Systems of Linear Equations:** Found in various optimization problems.
- **Neural Networks:** Weights in neural networks are often organized into matrices, and computations involve matrix multiplications.

## Notes in this Section
```dataview
LIST
FROM "150_Mathematics/Linear_Algebra"
WHERE file.folder = this.file.folder AND file.name != this.file.name AND !contains(file.name, "MOC")
SORT file.name ASC
```

---