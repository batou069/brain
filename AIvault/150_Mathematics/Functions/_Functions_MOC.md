---
tags:
  - mathematics
  - functions
  - moc
aliases:
  - Functions MOC
  - Mathematical Functions MOC
related:
  - "[[_Mathematics_MOC]]"
worksheet:
  - WS_Math_Foundations_1
date_created: 2025-05-30
---
# Mathematical Functions MOC

This section covers various mathematical functions that are frequently encountered in data science, machine learning, statistics, and AI. Understanding their properties, graphs, and applications is crucial.

## Core Functions

[list2card|addClass(ab-col3)]
- **Basic & Algebraic Functions**
    - [[Polynomials|Polynomials]]
    - [[Absolute_Value_Function|Absolute Value Function]]
    - [[Step_Function|Step Function]]
- **Transcendental Functions**
    - [[Exponential_Function|Exponential Function]] (and its [[Exponential_Function_Significance|Significance]])
    - [[Logarithmic_Function|Logarithmic Function]]
    - [[Trigonometric_Functions|Trigonometric Functions]] (sine, cosine, tangent, etc.)
    - [[Hyperbolic_Functions|Hyperbolic Functions]] (sinh, cosh, tanh, etc.)
- **Special Functions**
    - [[Gamma_Function|Gamma Function]]
- **Activation & Utility Functions in ML/AI**
    - [[Sigmoid_Function|Sigmoid (Logistic) Function]]
    - [[Logit_Function|Logit Function]]
    - [[Softmax_Function|Softmax Function]]
    - [[Rectified_Linear_Unit_ReLU|Rectified Linear Unit (ReLU)]] (and variants)
    - [[argmax_argmin|Argmax / Argmin]]

## Importance in AI/ML
- **Activation Functions:** Functions like [[Sigmoid_Function|Sigmoid]], [[Hyperbolic_Functions|tanh]], and [[Rectified_Linear_Unit_ReLU|ReLU]] are used in neural networks to introduce non-linearity, enabling models to learn complex patterns.
- **Loss Functions:** Mathematical functions are used to quantify the error or "loss" of a model's predictions, which is then minimized during training.
- **Probability Distributions:** Many probability distributions are defined by specific mathematical functions (e.g., the Gaussian/Normal distribution uses an exponential function).
- **Transformations:** Functions are used to transform data into more suitable formats for analysis or modeling (e.g., log transform for skewed data).
- **Model Building:** The core of many statistical and machine learning models is a mathematical function that maps inputs to outputs.

## Notes in this Section
```dataview
LIST
FROM "150_Mathematics/Functions"
WHERE file.folder = this.file.folder AND file.name != this.file.name AND !contains(file.name, "MOC")
SORT file.name ASC
```

---