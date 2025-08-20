---
tags:
  - data_visualization
  - plotting
  - scatter_plot_matrix
  - pair_plot
  - multivariate
  - correlation
  - concept
aliases:
  - Pair Plot
  - Pairs Plot
  - Scatterplot Matrix
related:
  - "[[Visualizing_Multidimensional_Data]]"
  - "[[Scatter_Plot]]"
  - "[[Histogram]]"
  - "[[Kernel_Density_Estimate_KDE|KDE Plot]]"
  - "[[Seaborn_Multi_Plot_Grids]]"
  - "[[_Pandas_MOC]]"
worksheet:
  - WS_DataViz_1
date_created: 2025-08-20
---
# Scatter Plot Matrix (Pair Plot)

## Definition
A **scatter plot matrix**, often called a **pair plot** or **pairs plot**, is a grid (or matrix) of scatter plots used to visualize the pairwise relationships between several numerical variables in a dataset.

Each cell $(i,j)$ in the grid shows a [[Scatter_Plot|scatter plot]] of variable $i$ against variable $j$. The diagonal cells typically display a univariate plot of each variable, such as a [[Histogram|histogram]] or a [[Kernel_Density_Estimate_KDE|Kernel Density Estimate (KDE) plot]].

## Purpose
-   **Explore Pairwise Relationships:** To quickly identify correlations, trends, clusters, and outliers between all pairs of numerical variables in a dataset.
-   **Understand Univariate Distributions:** The diagonal plots help understand the distribution of each individual variable.
-   **Identify Potential Interactions:** Can give clues about how variables might interact with each other.
-   **High-Level Overview of Multivariate Data:** Provides a comprehensive initial look at the structure of moderately high-dimensional numerical data.

## Key Characteristics
-   **Grid Structure:** Forms a square matrix of plots, where the number of rows and columns equals the number of variables being analyzed.
-   **Off-Diagonal Plots:** Scatter plots showing $Variable_i$ vs. $Variable_j$. The plot in cell $(i,j)$ is often the mirror image (axes swapped) of the plot in cell $(j,i)$, though some implementations might show different information (e.g., correlation coefficient) in the upper or lower triangle.
-   **Diagonal Plots:** Univariate distributions (histogram or KDE) of each variable.
-   **Hue Encoding (Optional):** Points in the scatter plots can be colored by a categorical variable to see how relationships differ across groups.

## When to Use
-   When you have multiple numerical variables (e.g., 3 to 10-15 variables) and want to explore all their pairwise relationships simultaneously.
-   As an initial step in [[Exploratory_Data_Analysis_Workflow|Exploratory Data Analysis (EDA)]] for multivariate numerical data.
-   To visually inspect for multicollinearity before building regression models.

## Implementation
-   **Seaborn:** `sns.pairplot(data_df, hue="category_col", diag_kind="kde", kind="scatter", ...)` is a very powerful and convenient function. See [[Seaborn_Multi_Plot_Grids]].
-   **Pandas:** `pandas.plotting.scatter_matrix(data_df, diagonal="kde", ...)` provides a similar functionality.
-   **Matplotlib:** Can be constructed manually using subplots, but it's much more verbose.

## Example Scenario
>[!question]- For Scatter Plot Matrix: Come up with a scenario where it would be useful. Is this plot the best way to visualize this scenario?
>
>**Scenario:** Analyzing an e-commerce dataset containing product features like `price`, `average_customer_rating`, `number_of_reviews`, and `shipping_time_days`. We want to understand how these numerical features relate to each other and see their individual distributions.
>
>**Usefulness:** A scatter plot matrix is highly useful to:
>1.  See if `price` is correlated with `average_customer_rating` or `number_of_reviews`.
>2.  Check if products with more `number_of_reviews` tend to have higher or lower `average_customer_rating`.
>3.  Observe the distribution of each feature (e.g., is `price` skewed? Is `shipping_time_days` normally distributed?).
>4.  If a `hue` variable like `product_category` is added, see if these relationships differ across categories.
>
>**Is this the best way?**
>Yes, for a quick, comprehensive overview of all pairwise relationships and individual distributions among a moderate number of numerical variables, a scatter plot matrix (pair plot) is an **excellent and standard choice**.
>
>**Alternatives & Complements:**
>-   A [[Heatmap|heatmap]] of the correlation matrix provides a quantitative summary of linear relationships but doesn't show the actual data points, clusters, or non-linear patterns like a scatter plot matrix does.
>-   For a very large number of variables, a scatter plot matrix can become too large and cluttered. In such cases, [[Dimensionality_Reduction|dimensionality reduction]] techniques might be used first, or one might focus on a subset of key variables or use a correlation heatmap.

**Obsidian Chart Plugin Example / Conceptual Output:**
> [!note] A full scatter plot matrix is a complex grid of multiple individual plots. It's not feasible to represent this entire structure with a single basic Obsidian Chart block. The description below outlines what one would see. In Python, `sns.pairplot()` generates this entire figure.

**Conceptual Description of a Scatter Plot Matrix for 3 Variables (e.g., Price, Rating, Reviews):**

Imagine a 3x3 grid of plots:

|                     | **Price (X-axis)**                               | **Rating (X-axis)**                              | **Reviews (X-axis)**                             |
| :------------------ | :----------------------------------------------- | :----------------------------------------------- | :----------------------------------------------- |
| **Price (Y-axis)**  | Histogram/KDE of Price                           | Scatter: Price vs. Rating                        | Scatter: Price vs. Reviews                       |
| **Rating (Y-axis)** | Scatter: Rating vs. Price                        | Histogram/KDE of Rating                          | Scatter: Rating vs. Reviews                      |
| **Reviews (Y-axis)**| Scatter: Reviews vs. Price                       | Scatter: Reviews vs. Rating                      | Histogram/KDE of Reviews                         |

-   Each off-diagonal cell $(i,j)$ contains a scatter plot of variable $i$ vs. variable $j$.
-   Each diagonal cell $(i,i)$ contains a histogram or KDE plot of variable $i$.
-   If a `hue` variable (e.g., product category) is used, points/distributions in all plots would be colored by this category.

This provides a rich, dense summary of the multivariate data.

---