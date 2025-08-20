---
tags:
  - matplotlib
  - python
  - api
  - plotting
  - object_oriented
  - figure
  - axes
  - concept
  - example
aliases:
  - Matplotlib OO API
  - Object-Based Matplotlib
related:
  - "[[Matplotlib_Overview]]"
  - "[[Matplotlib_Pyplot_API_vs_OO_API]]"
  - "[[Matplotlib_Figure_Subplot_Axes]]"
  - "[[Matplotlib_Pyplot_API]]"
worksheet:
  - WS_DataViz_1
date_created: 2025-08-20
---
# Matplotlib: Object-Oriented (OO) API

The **Object-Oriented (OO) API** is one of the two main ways to use [[Matplotlib_Overview|Matplotlib]], the other being the [[Matplotlib_Pyplot_API|pyplot API]]. The OO API is generally considered more powerful, flexible, and Pythonic for complex plots or when embedding Matplotlib in applications.

It involves explicitly creating and manipulating `Figure` and `Axes` objects.

## Core Idea
Instead of relying on a global state managed by `pyplot` (e.g., `plt.plot()` acting on the "current" axes), you explicitly:
1.  Create a **`Figure`** object (the top-level container).
2.  Add one or more **`Axes`** objects (subplots/plotting areas) to the Figure.
3.  Call methods directly on these `Axes` objects to create the plot (e.g., `ax.plot()`, `ax.scatter()`).
4.  Call methods on `Axes` or `Figure` objects for customization (e.g., `ax.set_title()`, `fig.savefig()`).

## Creating Figure and Axes
The most common way to start with the OO API is using `plt.subplots()`:

```python
import matplotlib.pyplot as plt
import numpy as np

# Create a Figure and a single Axes object
fig, ax = plt.subplots() 
# fig is a matplotlib.figure.Figure instance
# ax is a matplotlib.axes.Axes instance (or a single Axes if nrows=1, ncols=1)

# Create a Figure and a 2x2 grid of Axes objects
# fig_multiple, axs = plt.subplots(nrows=2, ncols=2, figsize=(8, 8))
# axs is now a 2D NumPy array of Axes objects:
# axs[0, 0] is the top-left subplot
# axs[0, 1] is the top-right subplot
# ... and so on.
```
-   `plt.subplots()` is a convenience function from `pyplot` that returns a `Figure` instance and an array (or single instance) of `Axes` objects.
-   You can also create a figure first (`fig = plt.figure()`) and then add axes to it (`ax1 = fig.add_subplot(1,2,1)`, `ax2 = fig.add_axes([left, bottom, width, height])`).

## Plotting and Customizing
Once you have an `Axes` object (e.g., `ax`), you use its methods:

[list2tab|#OO API Methods]
- Plotting Data
    -   `ax.plot(x, y, ...)`: For [[170_Data_Visualization/Plot_Types/Line_Plot|line plots]] and basic scatter plots (with line styles).
    -   `ax.scatter(x, y, ...)`: For [[170_Data_Visualization/Plot_Types/Scatter_Plot|scatter plots]] with more control over marker properties.
    -   `ax.bar(x, height, ...)`: For vertical [[170_Data_Visualization/Plot_Types/Bar_Chart|bar charts]].
    -   `ax.barh(y, width, ...)`: For horizontal bar charts.
    -   `ax.hist(data, bins=..., ...)`: For [[170_Data_Visualization/Plot_Types/Histogram|histograms]].
    -   `ax.boxplot(data, ...)`: For [[170_Data_Visualization/Plot_Types/Box_Plot|box plots]].
    -   `ax.pie(sizes, ...)`: For [[170_Data_Visualization/Plot_Types/Pie_Chart|pie charts]].
    -   `ax.imshow(image_data, ...)`: For displaying images or [[170_Data_Visualization/Plot_Types/Heatmap|heatmaps]]. See [[Matplotlib_Image_Display_imshow]].
    -   And many more specialized plotting methods.
- Setting Titles & Labels
    -   `ax.set_title("My Plot Title")`
    -   `ax.set_xlabel("X-axis Label")`
    -   `ax.set_ylabel("Y-axis Label")`
    -   `fig.suptitle("Overall Figure Title")` (called on the Figure object)
- Setting Limits
    -   `ax.set_xlim([xmin, xmax])`
    -   `ax.set_ylim([ymin, ymax])`
- Setting Ticks & Tick Labels
    -   `ax.set_xticks()`
    -   `ax.set_xticklabels()`
    -   `ax.set_yticks()`
    -   `ax.set_yticklabels()`
    -   `ax.tick_params(...)` for detailed tick customization.
- Legends
    -   `ax.legend()` (requires `label` argument in plotting calls like `ax.plot(..., label="Data Series")`).
- Gridlines
    -   `ax.grid(True/False, which='major', axis='both', ...)`
- Annotations & Text
    -   `ax.text(x, y, "my text", ...)`
    -   `ax.annotate("my annotation", xy=(x_point, y_point), xytext=(x_text, y_text), arrowprops=...)`

## Example (Revisiting the Sine/Cosine Plot OO-Style)
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

# Create a figure and one Axes
fig, ax = plt.subplots(figsize=(8, 5))

# Plot on the Axes object
ax.plot(x, y_sin, label='sin(x)', color='blue', linestyle='-')
ax.plot(x, y_cos, label='cos(x)', color='red', linestyle='--')

# Customize the Axes
ax.set_title('Sine and Cosine Waves (OO API)')
ax.set_xlabel('Angle (radians)')
ax.set_ylabel('Value')
ax.legend()
ax.grid(True)
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1.2, 1.2)

# Display the plot (still often uses pyplot's show)
# plt.show()
```

## Advantages
-   **Explicit Control:** You have direct handles to Figure and Axes objects, making it clear what part of the plot you are modifying.
-   **Better for Complex Layouts:** Essential for figures with multiple subplots, insets, or custom arrangements.
-   **Reusability:** Easier to write reusable functions or classes that create and customize plots because you can pass Figure or Axes objects around.
-   **Embedding:** The standard way to embed Matplotlib plots in GUI applications (Tkinter, Qt, WxPython) or web applications.
-   **Clarity in Larger Scripts:** Reduces ambiguity compared to the stateful `pyplot` API when dealing with multiple plots.

While `pyplot` is convenient for quick, interactive plotting, the Object-Oriented API is generally recommended for more structured, complex, or reusable plotting tasks. Often, a hybrid approach is used: `plt.subplots()` to get `fig` and `ax`, then OO methods on `ax`, and `plt.show()` at the end.

---