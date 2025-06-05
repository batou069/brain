---
tags:
  - MOC
  - data_science
  - ai
  - machine_learning
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Data Science & AI MOC (Map of Content)

This note serves as a central hub for all topics related to **Data Science, Artificial Intelligence, and Machine Learning**.

## Core Libraries & Tools
- "[[NumPy_MOC|NumPy]]"
- "[[Pandas_MOC|Pandas]]" (*Placeholder*)
- "[[Matplotlib_MOC|Matplotlib]]" (*Placeholder*)
- "[[Pillow_PIL_MOC|Pillow (PIL Fork)]]" (*Placeholder*)
- "[[Scikit-learn_MOC|Scikit-learn]]" (*Placeholder*)
- "[[TensorFlow_MOC|TensorFlow]]" (*Placeholder*)
- "[[PyTorch_MOC|PyTorch]]" (*Placeholder*)

## Mathematical Foundations
- "[[Linear_Algebra]]" (Link to existing MOC)
- "[[Statistics_DS_AI]]" (*Placeholder*)
- "[[Probability_DS_AI]]" (*Placeholder*)
- "[[Calculus_DS_AI]]" (*Placeholder*)

## Data Handling & Preprocessing
- "[[Data_Acquisition]]"
- "[[Exploratory_Data_Analysis]]" (EDA)
- "[[Feature_Engineering]]" (*Placeholder*)
- "[[Data_Cleaning]]" (*Placeholder*)
- "[[Data_Transformation]]" (*Placeholder*)
- "[[Standardization_Scaling]]" (*Implied by NumPy exercises*)

## Machine Learning Concepts
- "[[Supervised_Learning]]"
- "[[Unsupervised_Learning]]"
- "[[Reinforcement_Learning]]"
- "[[Regression_Models]]"
- "[[Classification_Models]]"
- "[[Clustering_Methods]]"
- "[[Dimensionality_Reduction]]"
- "[[Model_Evaluation]]"
- "[[Overfitting_Underfitting]]" (*Placeholder*)
- "[[Bias_Variance_Tradeoff]]" (*Placeholder*)
- "[[Ensemble_Methods]]"

## Deep Learning & Neural Networks
- "[[Neural_Networks]]"
- "[[Activation_Function]]" (*Placeholder*)
- "[[Backpropagation]]"
- "[[Convolutional_Neural_Networks]]" (CNN)
- "[[Recurrent_Neural_Networks]]" (RNN)
- "[[Transformers_DL]]" (*Placeholder*)
- "[[Generative_AI]]"

## Image Processing
- "[[Image_Representation_Digital]]" (*Implied by NumPy exercises*)
- "[[Color_Spaces]]" (*Placeholder*)
- Basic Image Manipulations (Cropping, Resizing, Filtering - *Implied*)

## Natural Language Processing (NLP)
- "[[NLP_Overview]]" (*Placeholder*)
- "[[Tokenization]]" (*Placeholder*)
- "[[Embeddings_NLP]]" (*Placeholder*)

## Notes in this Section

```dataview
LIST
FROM "140_Data_Science_AI"
WHERE file.folder = this.file.folder AND file.name != this.file.name AND !contains(file.name, "MOC") AND !contains(file.folder, "NumPy") AND !contains(file.folder, "Matplotlib") AND !contains(file.folder, "Pillow_PIL")
SORT file.name ASC
```

---
Use this MOC to navigate the Data Science & AI section.