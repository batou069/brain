---
tags:
  - matplotlib
  - python
  - library
  - data_visualization
  - plotting
aliases:
  - Matplotlib Library
related:
  - "[[Python]]"
  - "[[NumPy]]"
  - "[[Pandas_MOC|Pandas]]"
  - "[[SciPy_MOC|SciPy]]"
  - "[[Pyplot_API]]"
  - "[[Figure_Subplot_Axes]]"
  - "[[Image_Display_Matplotlib]]"
worksheet: [WS_NumPy] # Implied by exercises requiring visualization
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Matplotlib

## Definition

**Matplotlib** is a comprehensive and widely used open-source plotting library for the [[Python]] programming language and its numerical mathematics extension [[NumPy]]. It provides a flexible platform for creating a wide variety of static, animated, and interactive visualizations in Python.

## Core Features

- **Versatile Plotting:** Can generate line plots, scatter plots, bar charts, histograms, error charts, pie charts, heatmaps, contour plots, 3D plots, and much more.
- **Publication Quality:** Produces high-quality figures suitable for publication in various formats (PNG, PDF, SVG, EPS, etc.).
- **Customization:** Offers extensive control over virtually every aspect of a figure: colors, line styles, markers, fonts, labels, titles, legends, annotations, layout.
- **[[Pyplot_API|`pyplot` Interface]]:** Provides a MATLAB-like procedural interface (`matplotlib.pyplot`) for convenient, stateful plotting. This is often the easiest way to get started.
- **Object-Oriented API:** Offers a more powerful and flexible object-oriented API for greater control over complex plots and embedding Matplotlib in applications. This involves working directly with [[Figure_Subplot_Axes|`Figure`, `Axes`, and other objects]].
- **Integration with NumPy:** Seamlessly integrates with NumPy arrays for plotting numerical data.
- **Integration with Pandas:** [[Pandas_MOC|Pandas]] DataFrames and Series have built-in plotting methods that use Matplotlib under the hood.
- **Extensible:** Can be extended with various toolkits and third-party packages (e.g., Seaborn for statistical visualizations, Basemap/Cartopy for mapping).

## Basic Usage (`pyplot` API)

The `matplotlib.pyplot` module is typically imported as `plt`.

```python
import matplotlib.pyplot as plt
import numpy as np

# --- Simple Line Plot ---
x = np.linspace(0, 10, 100) # 100 points from 0 to 10
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.figure(figsize=(8, 5)) # Create a new figure, set its size

plt.plot(x, y_sin, label='sin(x)', color='blue', linestyle='-')
plt.plot(x, y_cos, label='cos(x)', color='red', linestyle='--')

plt.title('Sine and Cosine Waves')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend() # Show legend using labels from plot()
plt.grid(True)
# plt.savefig("sine_cosine.png") # Save the figure
plt.show() # Display the plot


# --- Scatter Plot ---
x_rand = np.random.rand(50)
y_rand = np.random.rand(50)
colors = np.random.rand(50)
sizes = 100 * np.random.rand(50)

plt.figure(figsize=(8, 5))
plt.scatter(x_rand, y_rand, c=colors, s=sizes, alpha=0.7, cmap='viridis')
plt.title('Random Scatter Plot')
plt.xlabel('X Value')
plt.ylabel('Y Value')
plt.colorbar(label='Color Intensity') # Show color bar
# plt.savefig("scatter_plot.png")
plt.show()
```

## Key Components

- **[[Figure_Subplot_Axes|Figure]]:** The outermost container for all plot elements. A figure can contain multiple [[Figure_Subplot_Axes|Axes (subplots)]].
- **[[Figure_Subplot_Axes|Axes]]:** An individual plot or chart within a figure. This is where data is plotted, and it contains the x-axis, y-axis, title, labels, etc.
- **Axis:** The number-line-like objects that define the graph's boundaries and ticks.

## Related Concepts
- [[Python]], [[NumPy]], [[Pandas_MOC|Pandas]]
- [[Data_Visualization]]
- [[Pyplot_API]] (Common interface)
- [[Figure_Subplot_Axes]] (Plot structure)
- [[Image_Display_Matplotlib]] (For showing images)
- [[Seaborn_MOC|Seaborn]] (Statistical plotting library based on Matplotlib)

---
**Source:** NumPy Worksheet Exercises (Implied), Matplotlib Documentation