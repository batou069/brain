---
tags:
  - matplotlib
  - python
  - library
  - data_visualization
  - plotting
  - concept
  - overview
aliases:
  - Matplotlib Library
related:
  - "[[170_Data_Visualization/Matplotlib/_Matplotlib_MOC|_Matplotlib_MOC]]"
  - "[[_Python_Libraries_MOC]]"
  - "[[_NumPy_MOC]]"
  - "[[_Pandas_MOC]]"
  - "[[Matplotlib_Pyplot_API_vs_OO_API]]"
  - "[[Matplotlib_Figure_Subplot_Axes]]"
worksheet:
  - WS_DataViz_1
date_created: 2025-06-03
---
# Matplotlib Overview

## Definition
**Matplotlib** is a comprehensive and widely used open-source plotting library for the [[Python]] programming language and its numerical mathematics extension [[_NumPy_MOC|NumPy]]. It provides a flexible platform for creating a wide variety of static, animated, and interactive visualizations in Python. Matplotlib is often considered the foundational plotting library in the Python scientific computing ecosystem.

## Core Features
-   **Versatile Plotting:** Can generate [[Line_Plot|line plots]], [[Scatter_Plot|scatter plots]], [[Bar_Chart|bar charts]], [[Histogram|histograms]], error charts, [[Pie_Chart|pie charts]], [[Heatmap|heatmaps]], contour plots, [[Matplotlib_3D_Plotting|3D plots]], and much more.
-   **Publication Quality:** Produces high-quality figures suitable for publication in various formats (PNG, PDF, SVG, EPS, etc.).
-   **[[Matplotlib_Customization|Customization]]:** Offers extensive control over virtually every aspect of a figure: colors, line styles, markers, fonts, labels, titles, legends, annotations, layout.
-   **Two Main APIs:**
    1.  The **[[Matplotlib_Pyplot_API_vs_OO_API|pyplot API]]** (`matplotlib.pyplot`): A state-based, procedural interface similar to MATLAB. Convenient for quick, interactive plotting.
    2.  The **[[Matplotlib_Pyplot_API_vs_OO_API|Object-Oriented API]]:** Provides more control and flexibility by working directly with Figure and Axes objects. Preferred for complex plots and embedding.
-   **Integration with NumPy:** Seamlessly integrates with NumPy arrays for plotting numerical data.
-   **Integration with Pandas:** [[_Pandas_MOC|Pandas]] DataFrames and Series have built-in plotting methods that use Matplotlib under the hood.
-   **Extensible:** Can be extended with various toolkits and third-party packages (e.g., [[170_Data_Visualization/Seaborn/_Seaborn_MOC|Seaborn]] for statistical visualizations, Basemap/Cartopy for mapping).

## Key Components
The primary objects you interact with in Matplotlib are:
-   **[[Matplotlib_Figure_Subplot_Axes|Figure (`matplotlib.figure.Figure`)]]:** The top-level container for all plot elements.
-   **[[Matplotlib_Figure_Subplot_Axes|Axes (`matplotlib.axes.Axes`)]]:** An individual plot or chart within a Figure. This is where data is plotted. Often referred to as a "subplot" when part of a grid.

## Basic Usage Example (`pyplot` API)
```python
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
x = np.linspace(0, 10, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

# Create a new figure and set its size
plt.figure(figsize=(8, 5))

# Plotting lines
plt.plot(x, y_sin, label='sin(x)', color='blue', linestyle='-')
plt.plot(x, y_cos, label='cos(x)', color='red', linestyle='--')

# Adding plot elements
plt.title('Sine and Cosine Waves')
plt.xlabel('X-axis (radians)')
plt.ylabel('Y-axis (value)')
plt.legend() # Show legend
plt.grid(True) # Add a grid

# Display the plot
plt.show()
```






Matplotlib's flexibility and extensive feature set make it a powerful tool for nearly any kind of 2D (and basic 3D) plotting task in Python.

---