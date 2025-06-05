---
tags:
  - seaborn
  - python
  - plotting
  - data_visualization
  - statistical_graphics
  - library
  - moc
  - concept
aliases:
  - Seaborn Library MOC
  - sns
related:
  - "[[_Data_Visualization_MOC]]"
  - "[[Matplotlib_Overview]]"
  - "[[_Pandas_MOC]]"
  - "[[Categorical_vs_Numerical_Data_Visualization]]"
worksheet:
  - WS_DataViz_1
date_created: 2025-06-03
---
# Seaborn MOC 📊🎨

**Seaborn** is a Python data visualization library based on [[Matplotlib_Overview|Matplotlib]]. It provides a high-level interface for drawing attractive and informative statistical graphics. Seaborn aims to make visualization a central part of exploring and understanding data, and it integrates closely with [[_Pandas_MOC|Pandas]] data structures.

## Core Philosophy & Features
-   **Statistical Focus:** Designed for creating common statistical plot types with ease.
-   **High-Level Interface:** Simplifies the creation of complex visualizations with less code compared to raw Matplotlib.
-   **Aesthetically Pleasing Defaults:** Comes with several built-in themes and color palettes for creating visually appealing plots out of the box.
-   **Pandas Integration:** Works seamlessly with Pandas DataFrames, allowing direct plotting from DataFrame columns.
-   **Specialized Plots:** Offers functions for visualizing distributions, categorical data, relationships, regressions, and matrices.

## Key Plotting Functions Categories
Seaborn's plotting functions can be broadly categorized:

1.  **Relational Plots (`relplot`)**: Visualizing relationships between variables.
    -   [[Scatter_Plot|Scatter plots]] (`scatterplot`)
    -   [[Line_Plot|Line plots]] (`lineplot`)
2.  **Distribution Plots (`displot`)**: Visualizing distributions of single variables or between variables.
    -   [[Histogram|Histograms]] (`histplot`)
    -   Kernel Density Estimates (`kdeplot`)
    -   Empirical Cumulative Distribution Functions (`ecdfplot`)
    -   Rug plots (`rugplot`)
3.  **Categorical Plots (`catplot`)**: Visualizing relationships involving categorical data.
    -   **Categorical scatterplots:**
        -   `stripplot` (jitter optional)
        -   `swarmplot` (non-overlapping points)
    -   **Categorical distribution plots:**
        -   [[Box_Plot|Box plots]] (`boxplot`)
        -   [[Violin_Plot|Violin plots]] (`violinplot`)
        -   Boxen plots (`boxenplot`)
    -   **Categorical estimate plots:**
        -   [[Bar_Chart|Bar plots]] (`barplot`) (shows point estimate and confidence interval)
        -   Point plots (`pointplot`)
        -   Count plots (`countplot`)
4.  **Regression Plots (`regplot`, `lmplot`)**: Visualizing linear regression models.
5.  **Matrix Plots**: Visualizing matrix data.
    -   [[Heatmap|Heatmaps]] (`heatmap`)
    -   Cluster maps (`clustermap`)
6.  **Multi-plot Grids**: Creating figures with multiple subplots based on data structure.
    -   `FacetGrid`
    -   `PairGrid` (for pairwise relationships, creating plots like [[Scatter_Plot_Matrix|scatter plot matrices]])
    -   `JointGrid` (for joint and marginal distributions)

## Basic Usage
```python
import seaborn as sns
import matplotlib.pyplot as plt # Often used for customization
import pandas as pd

# Load a sample dataset (e.g., 'tips' dataset from Seaborn)
tips = sns.load_dataset("tips")

# Example: Scatter plot with regression line
sns.lmplot(x="total_bill", y="tip", data=tips, hue="smoker")
plt.title("Tip Amount vs. Total Bill")
plt.show()

# Example: Box plot
plt.figure(figsize=(8,6)) # Can use plt to control figure size
sns.boxplot(x="day", y="total_bill", data=tips, palette="pastel")
plt.title("Total Bill Distribution by Day")
plt.show()
```

>[!question]- Can you use seaborn in a matplotlib plot?
>Yes, absolutely. Seaborn is built **on top of** Matplotlib.
>1.  **Seaborn functions return Matplotlib Axes objects** (or a `FacetGrid`/`PairGrid` object that manages Matplotlib Axes). This means you can use Matplotlib commands to further customize plots created by Seaborn.
>2.  You can use Seaborn to style Matplotlib plots (`sns.set_theme()`).
>3.  You can create a Matplotlib Figure and Axes, and then pass the `ax` object to many Seaborn plotting functions using the `ax=` parameter.
>
>Example:
>```python
>import seaborn as sns
>import matplotlib.pyplot as plt
>import pandas as pd
>
># Sample data
>data = pd.DataFrame({'x': range(10), 'y': [i**2 for i in range(10)]})
>
># Create Matplotlib figure and axes
>fig, ax = plt.subplots(figsize=(6,4))
>
># Use Seaborn to plot on the Matplotlib axes
>sns.lineplot(x='x', y='y', data=data, ax=ax, color='purple', linewidth=2)
>
># Further customize using Matplotlib methods on 'ax'
>ax.set_title("Seaborn Plot on Matplotlib Axes (Customized)")
>ax.set_xlabel("Custom X Label")
>ax.set_ylabel("Custom Y Label")
>ax.grid(True, linestyle=':', alpha=0.7)
>
>plt.show()
>```
>This integration is one of Seaborn's strengths, allowing users to leverage Seaborn's high-level statistical plotting with Matplotlib's extensive customization capabilities.

## Notes in this Section
```dataview
LIST
FROM "170_Data_Visualization/Seaborn"
WHERE file.folder = this.file.folder AND file.name != this.file.name AND !contains(file.name, "MOC")
SORT file.name ASC
```
*(This section will be populated with more specific notes on Seaborn plot types and features).*

---