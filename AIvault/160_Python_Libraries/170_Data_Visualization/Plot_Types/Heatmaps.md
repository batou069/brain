---
tags:
  - data_visualization
  - plotting
  - heatmap
  - matrix
  - correlation
  - concept
  - chart
aliases:
  - Heat Map
  - Density Heatmap
related:
  - "[[Matplotlib_Image_Display_imshow]]"
  - "[[Seaborn_Matrix_Plots]]"
  - "[[Choosing_the_Right_Plot]]"
  - "[[Correlation_Matrix_Visualization]]"
worksheet:
  - WS_DataViz_1
date_created: 2025-08-20
---
# Heatmap

## Definition
A **heatmap** is a graphical representation of data where values in a matrix are represented as colors. It's a 2D visualization technique that uses a color scale to show the magnitude of a phenomenon across two discrete variables or dimensions.

Larger values are typically represented by darker or more intense colors, while smaller values are represented by lighter or less intense colors (or vice-versa, depending on the chosen colormap and context).

## Key Characteristics
-   **Matrix Data:** Input is typically a 2D array or matrix.
-   **Color Encoding:** Values in the matrix cells are mapped to colors using a [[Matplotlib_Colormaps|colormap]].
-   **Grid Structure:** The plot consists of colored cells arranged in a grid, corresponding to the rows and columns of the input matrix.
-   **Annotations (Optional):** Numerical values can be displayed within each cell for precise information.
-   **Clustering (Optional):** Rows and/or columns can be reordered using hierarchical clustering to group similar items together, often revealing patterns (see [[Seaborn_Matrix_Plots|`sns.clustermap`]]).

## Purpose
-   **Visualizing Matrices of Values:** To get an intuitive overview of the magnitude of values across a 2D grid.
-   **Identifying Patterns and Clusters:** Patterns, clusters, highs, and lows often become visually apparent through color variations.
-   **[[Correlation_Matrix_Visualization|Visualizing Correlation Matrices]]:** A very common use case to quickly see relationships between many variables.
-   **Showing Co-occurrence or Interaction:** For example, user-item interaction matrices in recommendation systems.
-   **Displaying Confusion Matrices:** In classification, to see how well a model predicts different classes.

## When to Use
-   When you have a 2D matrix of numerical values and want to visualize their magnitudes and patterns.
-   For exploring relationships in correlation matrices.
-   When comparing values across two categorical dimensions (after aggregating data into a matrix, e.g., a pivot table).
-   For visualizing genomic data, web traffic by time/day, etc.

## Matplotlib & Seaborn Implementation
-   **Matplotlib:** `plt.imshow(data_matrix, cmap=..., ...)` or `ax.imshow(...)` is the fundamental function. Additional work is needed for labels, colorbar, annotations. See [[Matplotlib_Image_Display_imshow]].
-   **Seaborn:** `sns.heatmap(data_matrix, annot=True, cmap=..., fmt=".2f", ...)` provides a high-level interface specifically for creating well-formatted heatmaps with good defaults for annotations, colorbars, etc. `sns.clustermap(...)` adds hierarchical clustering.

## Example Scenario & Chart
>[!question]- For Heatmap: Come up with a scenario where it would be useful. Is this plot the best way to visualize this scenario?
>
>**Scenario:** Visualizing the monthly sales performance (e.g., percentage change from previous month) for different product categories over a year for an e-commerce business. Rows are product categories, columns are months, cell color represents sales performance.
>
>**Usefulness:** A heatmap is highly useful to:
>1.  Quickly identify which product categories performed well or poorly in specific months.
>2.  Spot seasonal trends across categories (e.g., all categories doing well in Q4).
>3.  Compare performance across categories for a given month, or across months for a given category.
>4.  Detect anomalies or unusual performance patterns.
>
>**Is this the best way?**
>Yes, for visualizing this type of matrix data where you want to see patterns of intensity across two discrete dimensions (category and month), a heatmap is an **excellent and standard choice**.
>
>**Alternatives & Complements:**
>-   Multiple [[Line_Plot|line plots]] (one per category, with months on x-axis) could show trends but might become cluttered with many categories. A heatmap handles more categories more cleanly.
>-   [[Bar_Chart|Grouped or stacked bar charts]] could compare categories month by month, but the overall yearly pattern across all categories might be less obvious than in a heatmap.

**Obsidian Chart Plugin Example (Illustrative):**
> [!note] True heatmaps with continuous color scales are not a native Chart.js type that the basic Obsidian Charts plugin directly renders as a single "heatmap" chart type. You could simulate it with a matrix of colored cells, but this is complex. Below is a conceptual representation of the *data* for a heatmap. The visualization relies on mapping values to colors.
>
> A common way to implement heatmaps in Chart.js (which Obsidian Charts uses) is via a `matrix` dataset type if supported by the plugin version, or by using a scatter plot where each point is a large square, and its color is mapped to the value. For simplicity here, I'll describe the data structure.

```
Conceptual Data for Monthly Sales Performance Heatmap (% Change):

Product Category | Jan  | Feb  | Mar  | Apr  | May  | Jun
-----------------|------|------|------|------|------|------
Electronics      | +5%  | +3%  | -1%  | +7%  | +4%  | +2%
Books            | +2%  | +1%  | +0%  | +3%  | +2%  | -1%
Clothing         | -3%  | +8%  | +10% | +5%  | +1%  | -2%
Home Goods       | +4%  | +2%  | +1%  | +2%  | +3%  | +0%

(Imagine this table where each cell's background color intensity corresponds to the percentage value, e.g., dark green for high positive %, dark red for high negative %, white/light yellow for near 0%.)
```

**If a `matrix` chart type were available in Obsidian Charts (hypothetical):**
```chart
// This is HYPOTHETICAL for Obsidian Charts basic plugin
// It shows the data structure one might feed to a heatmap library
type: matrix // Assuming a 'matrix' type existed for heatmaps
datasets: [{
  label: 'Monthly Sales % Change',
  data: [ // Array of arrays representing rows
    [5, 3, -1, 7, 4, 2],  // Electronics
    [2, 1, 0, 3, 2, -1],  // Books
    [-3, 8, 10, 5, 1, -2], // Clothing
    [4, 2, 1, 2, 3, 0]    // Home Goods
  ],
  // Colormap settings would be part of options
}]
options: {
  plugins: { title: { display: true, text: 'Sales Performance Heatmap' } },
  scales: {
    y: {
      labels: ['Electronics', 'Books', 'Clothing', 'Home Goods'],
      title: { display: true, text: 'Product Category' }
    },
    x: {
      labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
      title: { display: true, text: 'Month' }
    }
  },
  // colorScale: { type: 'diverging', mid: 0, min: -10, max: 10, lowColor: 'red', highColor: 'green' } // Conceptual
}
```
> **Actual Implementation:** In Python, `sns.heatmap(df_performance)` would directly render this from a Pandas DataFrame `df_performance`.

---