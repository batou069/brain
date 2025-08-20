---
tags:
  - seaborn
  - python
  - plotting
  - data_visualization
  - statistical_graphics
  - styling
  - themes
  - concept
aliases:
  - Seaborn Introduction
  - Seaborn Themes
  - sns.set_theme
related:
  - "[[170_Data_Visualization/Seaborn/_Seaborn_MOC|_Seaborn_MOC]]"
  - "[[Matplotlib_Overview]]"
  - "[[_Pandas_MOC]]"
worksheet:
  - WS_DataViz_1
date_created: 2025-08-20
---
# Seaborn: Overview and Styling

**Seaborn** is a Python data visualization library based on [[Matplotlib_Overview|Matplotlib]]. It provides a high-level interface for drawing attractive and informative statistical graphics. Seaborn aims to make visualization a central part of exploring and understanding data, and it integrates closely with [[_Pandas_MOC|Pandas]] data structures.

It is conventionally imported as `sns`:
```python
import seaborn as sns
import matplotlib.pyplot as plt # Often used for final customizations
```

## Core Philosophy
-   **Statistical Focus:** Designed specifically for statistical plotting, making it easy to visualize relationships, distributions, and categorical data.
-   **High-Level & Declarative:** You specify *what* you want to plot and how variables map to visual aesthetics, and Seaborn handles many of the plotting details.
-   **Aesthetic Defaults:** Comes with beautifully styled defaults that are often more visually appealing than Matplotlib's defaults.
-   **Pandas Integration:** Most functions are designed to work directly with Pandas DataFrames, where you can pass column names as strings.

## Styling and Themes
One of Seaborn's most immediate benefits is its ability to control the aesthetics of plots easily.

[list2tab|#Seaborn Styling]
- `sns.set_theme()`
    -   **Purpose:** A single function to set the theme, style, and context of all subsequent plots in a session.
    -   **Key Parameters:**
        -   `style`: Controls the aesthetic style of the plots. Options: `'darkgrid'` (default), `'whitegrid'`, `'dark'`, `'white'`, `'ticks'`.
        -   `palette`: Sets the color palette. Can be a Seaborn palette name (e.g., `'deep'`, `'muted'`, `'pastel'`, `'bright'`, `'dark'`, `'colorblind'`), a Matplotlib colormap, or a list of colors.
        -   `context`: Controls the scale of plot elements (line widths, font sizes, etc.) for different contexts. Options: `'notebook'` (default), `'paper'`, `'talk'`, `'poster'`.
        -   `font`, `font_scale`: Controls font properties.
    -   **Example:**
        ```python
        import seaborn as sns
        import matplotlib.pyplot as plt
        import numpy as np

        # Set a theme for all subsequent plots in the script/notebook
        # sns.set_theme(style="whitegrid", palette="pastel", context="talk")

        # Create a sample plot to see the effect
        # x = np.random.randn(100)
        # sns.histplot(x)
        # plt.title("Plot with Seaborn Theme")
        # plt.show()
        ```
- `sns.set_style()` and `sns.set_context()`
    -   These functions allow you to set the style and context independently.
    -   `sns.set_style("ticks")`
    -   `sns.set_context("paper", font_scale=1.2)`
- `sns.despine()`
    -   **Purpose:** Removes the top and right spines (axes lines) from a plot, which can improve clarity and aesthetics.
    -   **Example:**
        ```python
        # sns.set_theme(style="ticks") # 'ticks' style is good with despine
        # sns.lineplot(x=range(10), y=np.random.rand(10))
        # sns.despine(offset=10, trim=True) # Remove top/right spines, offset from axes
        # plt.show()
        ```
- Color Palettes (`sns.color_palette()`)
    -   Seaborn provides powerful tools for working with colors.
    -   You can create and view color palettes using `sns.color_palette()`.
    -   **Types of Palettes:**
        -   **Qualitative:** For representing categorical data where categories have no inherent order (e.g., `'deep'`, `'Set2'`).
        -   **Sequential:** For representing numerical or ordinal data that progresses from low to high (e.g., `'Blues'`, `'YlGnBu'`).
        -   **Diverging:** For representing data where both low and high values are interesting, with a clear midpoint (e.g., `'coolwarm'`, `'vlag'`).
    -   **Example:**
        ```python
        # my_palette = sns.color_palette("viridis", n_colors=8)
        # sns.palplot(my_palette) # Visualize the palette
        # plt.show()
        ```

## Figure-level vs. Axes-level Functions
Seaborn has two types of plotting functions:
-   **Axes-level functions:** Plot data onto a single Matplotlib `Axes` object (e.g., `scatterplot`, `histplot`, `boxplot`). You can combine them on a single Matplotlib figure.
-   **Figure-level functions:** Create a figure with one or more subplots and manage the figure layout. These functions (e.g., `relplot`, `displot`, `catplot`, `lmplot`, `pairplot`, `jointplot`) wrap axes-level functions and map data semantics to the figure structure (e.g., using `col`, `row`, `hue`). They return a `FacetGrid` or `PairGrid` object.

This distinction is key to understanding how to customize Seaborn plots. For figure-level plots, customization is done through the returned grid object's methods (e.g., `grid.set_axis_labels()`), while for axes-level plots, you use standard Matplotlib `ax` methods (`ax.set_title()`, etc.).

Seaborn's styling capabilities and high-level API make it an excellent starting point for creating beautiful and informative statistical visualizations in Python.

---