---
tags:
  - data_visualization
  - categorical_data
  - numerical_data
  - plotting
  - concept
aliases:
  - Visualizing Categorical Data
  - Visualizing Numerical Data
  - Plotting Different Data Types
related:
  - "[[_Data_Visualization_MOC]]"
  - "[[Choosing_the_Right_Plot]]"
  - "[[Bar_Chart]]"
  - "[[Pie_Chart]]"
  - "[[Histogram]]"
  - "[[Box_Plot]]"
  - "[[Scatter_Plot]]"
  - "[[Line_Plot]]"
worksheet:
  - WS_DataViz_1
date_created: 2025-06-03
---
# Visualizing Categorical vs. Numerical Data

The type of data you are working with—categorical or numerical—fundamentally influences the appropriate methods for visualization. Understanding this distinction is key to [[Choosing_the_Right_Plot|choosing the right plot type]].

## Data Types Recap
-   **Numerical (Quantitative) Data:** Represents measurable quantities.
    -   **Continuous:** Can take any value within a range (e.g., height, temperature, time).
    -   **Discrete:** Can only take specific, distinct values, often integers (e.g., number of children, count of defects).
-   **Categorical (Qualitative) Data:** Represents characteristics or labels that can be divided into groups or categories.
    -   **Nominal:** Categories with no intrinsic order (e.g., colors, gender, country names).
    -   **Ordinal:** Categories with a meaningful order or ranking, but the differences between categories are not necessarily uniform (e.g., education level: High School, Bachelor's, Master's, PhD; satisfaction rating: Low, Medium, High).

>[!question] What is different between visualization of categorical and numerical data?

The primary differences lie in:
1.  **Purpose of Visualization:**
    *   **Numerical:** Often visualized to understand its distribution (central tendency, spread, shape, outliers), trends over time, or relationships with other numerical variables.
    *   **Categorical:** Often visualized to show frequencies, proportions, or to compare a numerical measure across different categories.
2.  **Plot Types Used:** Different plot types are inherently suited to one type of data or a combination.
3.  **Mathematical Operations:** Meaningful mathematical operations (like mean, median) are typically applied to numerical data, while frequencies and proportions are key for categorical data.

## Visualizing Numerical Data

[list2tab|#Numerical Data Plots]
- Single Numerical Variable (Univariate)
    - **Goal:** Understand the distribution of the data.
    - **Common Plots:**
        -   **[[Histogram|Histogram]]:** Shows frequency distribution in bins. Reveals shape (skewness, modality), central tendency, spread.
        -   **Density Plot (KDE):** Smoothed version of a histogram. Good for visualizing distribution shape.
        -   **[[Box_Plot|Box Plot]]:** Summarizes distribution via quartiles (median, IQR), shows outliers.
        -   **[[Violin_Plot|Violin Plot]]:** Combines box plot with KDE to show distribution shape.
        -   **ECDF Plot (Empirical Cumulative Distribution Function):** Shows the proportion of data points less than or equal to a given value.
    - **Example Scenario:** Visualizing the distribution of exam scores for a class.
- Two Numerical Variables (Bivariate)
    - **Goal:** Understand the relationship or correlation between them.
    - **Common Plots:**
        -   **[[Scatter_Plot|Scatter Plot]]:** Each point represents an observation. Reveals patterns, correlation, clusters, outliers.
        -   **[[Line_Plot|Line Plot]]:** If one variable has a natural ordering (like time). Shows trends.
        -   **[[Heatmap|Heatmap]] (for binned 2D data or correlation matrices):** Shows density or correlation strength.
        -   **Joint Plot (e.g., `seaborn.jointplot`):** Combines scatter plot with marginal distributions (histograms/KDEs).
    - **Example Scenario:** Relationship between advertising spend and sales.
- Multiple Numerical Variables (Multivariate)
    - **Goal:** Explore relationships among several variables.
    - **Common Plots:**
        -   **[[Scatter_Plot_Matrix|Scatter Plot Matrix (Pair Plot)]]:** Grid of scatter plots for all pairs of variables.
        -   **3D Scatter Plot:** For three variables (use with caution, can be hard to interpret).
        -   **Parallel Coordinates Plot:** Each variable gets an axis, observations are lines.
        -   [[Heatmap|Heatmap]] of a correlation matrix.
        -   Use visual encodings (color, size, shape) on 2D scatter plots to represent additional dimensions.
    - **Example Scenario:** Exploring relationships between height, weight, age, and blood pressure.

## Visualizing Categorical Data

[list2tab|#Categorical Data Plots]
- Single Categorical Variable (Univariate)
    - **Goal:** Understand the frequency or proportion of each category.
    - **Common Plots:**
        -   **[[Bar_Chart|Bar Chart (or Count Plot)]]:** Height of bar represents frequency or proportion of each category.
        -   **[[Pie_Chart|Pie Chart]]:** Represents parts of a whole (proportions). Best for few categories, often less effective than bar charts for comparison.
    - **Example Scenario:** Distribution of car colors in a parking lot.
- One Categorical and One Numerical Variable (Bivariate)
    - **Goal:** Compare the numerical variable across different categories.
    - **Common Plots:**
        -   **[[Bar_Chart|Bar Chart]] (with mean/median/sum):** Bar height represents an aggregate of the numerical variable for each category.
        -   **[[Box_Plot|Box Plot]]:** Shows distribution of the numerical variable for each category.
        -   **[[Violin_Plot|Violin Plot]]:** Similar to box plot, but also shows distribution shape for each category.
        -   **Strip Plot / Swarm Plot:** Shows individual data points of the numerical variable for each category (good for smaller datasets).
        -   **Point Plot:** Shows point estimates (e.g., mean) and confidence intervals for the numerical variable across categories.
    - **Example Scenario:** Comparing average salaries across different job departments.
- Two Categorical Variables (Bivariate)
    - **Goal:** Understand the relationship or joint distribution of the two categorical variables.
    - **Common Plots:**
        -   **Grouped or Stacked [[Bar_Chart|Bar Chart]]:** Based on a contingency table (crosstabulation).
        -   **Mosaic Plot:** Area of rectangles proportional to cell frequencies in a contingency table.
        -   **[[Heatmap|Heatmap]] of a contingency table.**
    - **Example Scenario:** Relationship between education level and job satisfaction category.
- Multiple Categorical Variables (Multivariate)
    - **Goal:** Explore interactions between several categorical variables.
    - **Common Plots:**
        -   **Facet Grids (Small Multiples):** Create a grid of plots where each subplot shows the relationship for a subset of categories.
        -   **Mosaic Plots (extended).**
        -   Use color/shape encoding in other plot types if one variable is numerical.
    - **Example Scenario:** How does product preference (categorical) vary across different age groups (categorical) and regions (categorical)?

## Key Differences Summarized
-   **Axes:** Numerical data typically uses continuous axes. Categorical data uses discrete axes where each category is a point or a section.
-   **Aggregation:** Numerical data often involves aggregation like mean, median, sum for comparisons across categories. Categorical data involves counting frequencies or proportions.
-   **Ordering:** Numerical data has an inherent order. Nominal categorical data does not (though ordinal does). This affects plot choices (e.g., line plots are usually not for nominal categorical x-axis).

Choosing appropriate visualizations based on data type is fundamental to accurate and insightful data exploration.

---