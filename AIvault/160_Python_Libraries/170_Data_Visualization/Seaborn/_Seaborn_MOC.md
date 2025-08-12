---
tags: [seaborn, python, plotting, data_visualization, statistical_graphics, library, moc, concept]
aliases: [Seaborn Library MOC, sns]
related:
  - "[[_Data_Visualization_MOC]]"
  - "[[Matplotlib_Overview]]" # Seaborn is built on Matplotlib
  - "[[_Pandas_MOC]]" # Seaborn integrates well with Pandas DataFrames
  - "[[Categorical_vs_Numerical_Data_Visualization]]"
  - "[[Seaborn_Themes_Styles|Seaborn Themes and Styles]]"
worksheet: [WS_DataViz_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Seaborn MOC 📊🎨

**Seaborn** is a Python data visualization library based on [[Matplotlib_Overview|Matplotlib]]. It provides a high-level interface for drawing attractive and informative statistical graphics. Seaborn aims to make visualization a central part of exploring and understanding data, and it integrates closely with [[_Pandas_MOC|Pandas]] data structures.

## Core Philosophy & Features
-   **Statistical Focus:** Designed for creating common statistical plot types with ease.
-   **High-Level Interface:** Simplifies the creation of complex visualizations with less code compared to raw Matplotlib.
-   **[[Seaborn_Themes_Styles|Aesthetically Pleasing Defaults]]:** Comes with several built-in themes and color palettes.
-   **Pandas Integration:** Works seamlessly with Pandas DataFrames.
-   **Specialized Plots:** Offers functions for visualizing distributions, categorical data, relationships, regressions, and matrices.

## Key Plotting Function Categories & Functions
Seaborn's plotting functions can be broadly categorized. Many functions have a figure-level counterpart (e.g., `relplot` for `scatterplot` and `lineplot`) that can create faceted plots.

[list2card|addClass(ab-col2)|#Seaborn Plot Categories]
- **[[Seaborn_Relational_Plots|Relational Plots]] (`relplot`, `scatterplot`, `lineplot`)**
  - Visualizing relationships between two numerical variables.
  - `scatterplot`: Shows relationship using point markers.
  - `lineplot`: Shows relationship using lines, often for trends or time series.
- **[[Seaborn_Distribution_Plots|Distribution Plots]] (`displot`, `histplot`, `kdeplot`, `ecdfplot`, `rugplot`)**
  - Visualizing the distribution of one or more variables.
  - `histplot`: [[Histogram|Histograms]].
  - `kdeplot`: Kernel Density Estimates.
  - `ecdfplot`: Empirical Cumulative Distribution Functions.
- **[[Seaborn_Categorical_Plots|Categorical Plots]] (`catplot`, and specific functions)**
  - Visualizing relationships where one variable is categorical.
  - **Scatter:** `stripplot`, `swarmplot`.
  - **Distribution:** `boxplot`, `violinplot`, `boxenplot`.
  - **Estimate:** `barplot`, `pointplot`, `countplot`.
- **[[Seaborn_Regression_Plots|Regression Plots]] (`regplot`, `lmplot`)**
  - Visualizing linear regression models with scatter data.
- **[[Seaborn_Matrix_Plots|Matrix Plots]] (`heatmap`, `clustermap`)**
  - Visualizing matrix data, like correlation matrices or heatmaps.
- **[[Seaborn_Multi_Plot_Grids|Multi-Plot Grids]] (`FacetGrid`, `PairGrid`, `JointGrid`)**
  - Creating figures with multiple subplots based on data structure to compare subsets or pairwise relationships.
  - `pairplot`: A specific instance for pairwise relationships (scatter plot matrix).
  - `jointplot`: Shows bivariate relationship along with marginal univariate distributions.

## Customization and Integration
-   **[[Seaborn_Themes_Styles|Themes and Styles (`sns.set_theme()`, `sns.set_style()`)]]**
-   **Color Palettes (`sns.color_palette()`, `palette=` argument)**
-   **Integration with Matplotlib:** Seaborn plots are Matplotlib objects, allowing for customization using Matplotlib's API. (See "Can you use seaborn in a matplotlib plot?" in the MOC intro).

## Basic Usage Snippet
```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Example: Using a built-in dataset
# tips = sns.load_dataset("tips")

# Relational plot (scatterplot)
# sns.scatterplot(x="total_bill", y="tip", hue="time", data=tips)
# plt.title("Tip Amount vs. Total Bill by Time of Day")
# plt.show()

# Distribution plot (histogram)
# sns.histplot(data=tips, x="total_bill", kde=True, hue="sex")
# plt.title("Distribution of Total Bill by Sex")
# plt.show()

# Categorical plot (boxplot)
# sns.boxplot(x="day", y="total_bill", data=tips, palette="Set2")
# plt.title("Total Bill Distribution by Day")
# plt.show()
```

## Notes in this Seaborn Section
```dataview
LIST
FROM "170_Data_Visualization/Seaborn"
WHERE file.folder = this.file.folder AND file.name != this.file.name AND !contains(file.name, "MOC")
SORT file.name ASC
```

---