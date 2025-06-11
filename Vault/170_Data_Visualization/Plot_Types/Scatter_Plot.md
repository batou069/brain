---
tags:
  - data_visualization
  - plotting
  - scatter_plot
  - correlation
  - relationship
  - concept
  - chart
aliases:
  - Scatter Chart
  - Scatter Graph
  - Point Plot
related:
  - "[[Matplotlib_Basic_Plotting_Functions]]"
  - "[[Seaborn_Relational_Plots]]"
  - "[[Choosing_the_Right_Plot]]"
  - "[[Visualizing_Multidimensional_Data]]"
  - "[[Trend_Line]]"
worksheet:
  - WS_DataViz_1
date_created: 2025-06-09
---
# Scatter Plot

## Definition
A **scatter plot** (also called a scatter graph, scatter chart, scattergram, or scatter diagram) is a type of plot or mathematical diagram using Cartesian coordinates to display values for typically two numerical variables for a set of data. Each point on the plot represents an individual observation or data point, with its position determined by its values for the two variables.

## Purpose
-   **Visualizing Relationships:** To observe and show relationships (correlations) between two numerical variables.
    -   Positive correlation: As one variable increases, the other tends to increase.
    -   Negative correlation: As one variable increases, the other tends to decrease.
    -   No correlation: No discernible pattern.
-   **Identifying Clusters:** To detect groups or clusters of data points that share similar characteristics.
-   **Detecting Outliers:** To spot data points that deviate significantly from the general pattern.
-   **Foundation for Regression:** Often the first step before performing [[Linear_Regression|linear regression]] or other regression analyses; a [[Trend_Line|trend line]] can be overlaid.

## Key Characteristics
-   Each axis represents a numerical variable.
-   Each data point is represented by a marker (e.g., dot, circle, x).
-   Additional dimensions can be encoded using marker properties:
    -   **Color (`c` or `hue`):** For a third categorical or numerical variable.
    -   **Size (`s`):** For a third numerical variable (making it a bubble chart).
    -   **Shape (`marker` or `style`):** For a third categorical variable.

## When to Use
-   When you have two numerical variables and want to see if/how they are related.
-   When you want to identify patterns like linearity, non-linearity, clusters, or outliers in bivariate data.

## Matplotlib & Seaborn Implementation
-   **Matplotlib:** `plt.scatter(x, y, ...)` or `ax.scatter(x, y, ...)`.
-   **Seaborn:** `sns.scatterplot(x="col_x", y="col_y", data=df, ...)` or `sns.relplot(x="...", y="...", kind="scatter", data=df, ...)`. Seaborn adds easy `hue`, `size`, `style` semantics.

## Example Scenario & Chart
>[!question]- For Scatter Plot: Come up with a scenario where it would be useful. Is this plot the best way to visualize this scenario?
>
>**Scenario:** Investigating the relationship between the `total_bill` amount and the `tip` amount from customer transactions at a restaurant. Each transaction is a data point.
>
>**Usefulness:** A scatter plot is highly useful to:
>1.  See if there's a tendency for higher bills to result in higher tips (positive correlation).
>2.  Identify any unusual tipping behavior (outliers).
>3.  Observe the general spread and density of tip amounts for different bill sizes.
>
>**Is this the best way?**
>Yes, for visualizing the direct relationship and correlation between two numerical variables like `total_bill` and `tip`, a scatter plot is the **primary and most effective choice**.
>
>**Alternatives & Complements:**
>-   A [[Trend_Line|regression line]] (e.g., from `sns.regplot` or `sns.lmplot`) can be added to quantify the linear trend.
>-   [[Heatmap|Heatmaps]] or 2D density plots (`sns.kdeplot(x=..., y=...)`) can be used if there are many overlapping points to show density, but they obscure individual points.
>-   Binning one variable and then using [[Box_Plot|box plots]] for the other can show distribution changes but loses the point-by-point relationship.

**Obsidian Chart Plugin Example (Illustrative):**
```chart
type: line
labels: [T1, T2, T3, T4, T5, T6, T7, T8, T9, T10]
series:
  - title: Bill vs. Tip
    data: [1.01, 1.66, 3.50, 3.31, 3.61, 4.71, 2.00, 3.12, 1.96, 3.23]
    backgroundColor: rgba(0, 123, 255, 0.6)
    pointRadius: 5
    fill: false
options:
  xTitle: Total Bill ($)
  yTitle: Tip Amount ($)
  xMin: 0
  yMin: 0
  title: Scatter Plot Total Bill vs. Tip Amount
```

---