---
tags:
  - data_visualization
  - statistics
  - anscombes_quartet
  - summary_statistics
  - importance_of_plotting
  - concept
  - example
aliases:
  - Anscombe's Quartet
  - Importance of Visualizing Data
related:
  - "[[Data_Visualization_Importance]]"
  - "[[Descriptive_Statistics_Methods]]"
worksheet:
  - WS_DataViz_1
date_created: 2025-08-20
---
# Anscombe's Quartet

## Definition
**Anscombe's Quartet** comprises four datasets that have nearly identical simple descriptive statistics, yet appear very different when graphed. Each dataset consists of eleven $(x,y)$ points. The quartet was constructed in 1973 by the statistician Francis Anscombe to demonstrate the importance of **graphing data before analyzing it** and the effect of outliers and other influential observations on statistical properties.

## The Data
The four datasets are typically presented as follows:

| Dataset | X values (I, II, III) | Y values (I) | Y values (II) | Y values (III) | X values (IV) | Y values (IV) |
|---------|-----------------------|--------------|---------------|----------------|---------------|---------------|
| I       | 10.0                  | 8.04         | 9.14          | 7.46           | 8.0           | 6.58          |
| I       | 8.0                   | 6.95         | 8.14          | 6.77           | 8.0           | 5.76          |
| I       | 13.0                  | 7.58         | 8.74          | 12.74          | 8.0           | 7.71          |
| I       | 9.0                   | 8.81         | 8.77          | 7.11           | 8.0           | 8.84          |
| I       | 11.0                  | 8.33         | 9.26          | 7.81           | 8.0           | 8.47          |
| I       | 14.0                  | 9.96         | 8.10          | 8.84           | 8.0           | 7.04          |
| I       | 6.0                   | 7.24         | 6.13          | 6.08           | 8.0           | 5.25          |
| I       | 4.0                   | 4.26         | 3.10          | 5.39           | 19.0          | 12.50         |
| I       | 12.0                  | 10.84        | 9.13          | 8.15           | 8.0           | 5.56          |
| I       | 7.0                   | 4.82         | 7.26          | 6.42           | 8.0           | 7.91          |
| I       | 5.0                   | 5.68         | 4.74          | 5.73           | 8.0           | 6.89          |

## Nearly Identical Descriptive Statistics
For all four datasets:
-   Mean of $x$: $9.0$
-   Variance of $x$: $11.0$
-   Mean of $y$: $7.50$ (approximately)
-   Variance of $y$: $4.12$ (approximately)
-   Correlation between $x$ and $y$: $0.816$ (approximately)
-   Linear regression line: $y \approx 3.00 + 0.500x$ (approximately)
-   Coefficient of determination ($R^2$): $0.67$ (approximately)

If one were to only look at these summary statistics, one might conclude that the four datasets are very similar.

## Visual Differences
However, when plotted as [[170_Data_Visualization/Plot_Types/Scatter_Plot|scatter plots]], they reveal vastly different structures:

[list2tab|#Dataset Visuals]
- Dataset I
    -   **Appearance:** Consists of points that appear to follow a simple linear relationship with some scatter, fitting typical assumptions for linear regression.
    -   **Obsidian Chart (Conceptual - actual data points vary slightly):**
        ```chart
        type: scatter
        labels: ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10', 'P11']
        datasets:
          - label: 'Dataset I'
            data: [
                {x: 10, y: 8.04}, {x: 8, y: 6.95}, {x: 13, y: 7.58}, {x: 9, y: 8.81}, {x: 11, y: 8.33},
                {x: 14, y: 9.96}, {x: 6, y: 7.24}, {x: 4, y: 4.26}, {x: 12, y: 10.84}, {x: 7, y: 4.82}, {x: 5, y: 5.68}
            ]
            backgroundColor: 'rgba(0, 123, 255, 0.7)'
        options: { title: { display: true, text: 'Anscombe I: Linear with Scatter' } }
        ```
- Dataset II
    -   **Appearance:** The relationship between $x$ and $y$ is clearly non-linear (quadratic). A straight line regression is inappropriate.
    -   **Obsidian Chart (Conceptual):**
        ```chart
        type: scatter
        datasets:
          - label: 'Dataset II'
            data: [
                {x: 10, y: 9.14}, {x: 8, y: 8.14}, {x: 13, y: 8.74}, {x: 9, y: 8.77}, {x: 11, y: 9.26},
                {x: 14, y: 8.10}, {x: 6, y: 6.13}, {x: 4, y: 3.10}, {x: 12, y: 9.13}, {x: 7, y: 7.26}, {x: 5, y: 4.74}
            ]
            backgroundColor: 'rgba(255, 99, 132, 0.7)'
        options: { title: { display: true, text: 'Anscombe II: Non-linear (Quadratic)' } }
        ```
- Dataset III
    -   **Appearance:** The relationship is perfectly linear, but there is one significant outlier that skews the regression line and correlation. Without the outlier, the correlation would be much stronger and the regression line different.
    -   **Obsidian Chart (Conceptual):**
        ```chart
        type: scatter
        datasets:
          - label: 'Dataset III'
            data: [
                {x: 10, y: 7.46}, {x: 8, y: 6.77}, {x: 13, y: 12.74}, {x: 9, y: 7.11}, {x: 11, y: 7.81},
                {x: 14, y: 8.84}, {x: 6, y: 6.08}, {x: 4, y: 5.39}, {x: 12, y: 8.15}, {x: 7, y: 6.42}, {x: 5, y: 5.73}
            ]
            backgroundColor: 'rgba(75, 192, 192, 0.7)'
        options: { title: { display: true, text: 'Anscombe III: Linear with Outlier' } }
        ```
- Dataset IV
    -   **Appearance:** All $x$ values are the same except for one outlier which has a very high $x$ value. This single point exerts high leverage and determines the regression line. There's no clear relationship among the other points.
    -   **Obsidian Chart (Conceptual):**
        ```chart
        type: scatter
        datasets:
          - label: 'Dataset IV'
            data: [
                {x: 8, y: 6.58}, {x: 8, y: 5.76}, {x: 8, y: 7.71}, {x: 8, y: 8.84}, {x: 8, y: 8.47},
                {x: 8, y: 7.04}, {x: 8, y: 5.25}, {x: 19, y: 12.50}, {x: 8, y: 5.56}, {x: 8, y: 7.91}, {x: 8, y: 6.89}
            ]
            backgroundColor: 'rgba(255, 159, 64, 0.7)'
        options: { title: { display: true, text: 'Anscombe IV: High Leverage Point' } }
        ```

## Lesson
Anscombe's Quartet powerfully illustrates that **summary statistics alone are not sufficient to understand a dataset.** Visualizing data is essential to:
-   Identify the underlying structure and relationships.
-   Detect outliers or influential points.
-   Assess the appropriateness of statistical models (e.g., linear regression).
-   Avoid drawing incorrect conclusions based solely on numerical summaries.

It underscores the importance of [[Exploratory_Data_Analysis_Workflow|Exploratory Data Analysis (EDA)]] and the critical role of [[Data_Visualization_Importance|data visualization]] in the analytical process.

---