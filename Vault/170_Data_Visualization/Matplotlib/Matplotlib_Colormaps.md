---
tags:
  - matplotlib
  - python
  - plotting
  - colormap
  - colors
  - data_visualization
  - concept
  - example
aliases:
  - Matplotlib cmaps
  - Color Maps in Matplotlib
related:
  - "[[170_Data_Visualization/Matplotlib/_Matplotlib_MOC|_Matplotlib_MOC]]"
  - "[[Matplotlib_Image_Display_imshow|Matplotlib imshow]]"
  - "[[Scatter_Plot]]"
  - "[[Heatmap]]"
worksheet:
  - WS_DataViz_1
date_created: 2025-06-09
---
# Matplotlib: Colormaps (`cmap`)

A **colormap** (or color map) in Matplotlib is a mapping from data values (often scalar values in a 2D array) to colors. Colormaps are essential for visualizing data where color intensity or hue represents a quantity, such as in [[170_Data_Visualization/Plot_Types/Heatmap|heatmaps]], contour plots, or when encoding a third dimension in a [[170_Data_Visualization/Plot_Types/Scatter_Plot|scatter plot]] using color.

Matplotlib provides a wide variety of built-in colormaps, and users can also create custom ones. Colormaps are typically specified using the `cmap` argument in plotting functions like `imshow()`, `scatter()`, `pcolormesh()`, `contourf()`.

## Types of Colormaps
Matplotlib colormaps are generally divided into several categories based on their color progression and intended use:

[list2tab|#Colormap Categories]
- Sequential
    - **Purpose:** Best for representing data that has an ordering, from low to high (or vice-versa). Typically use variations in lightness and often saturation of a single hue, or a smooth progression through related hues.
    - **Examples:** `'viridis'` (default for many functions), `'plasma'`, `'inferno'`, `'magma'`, `'cividis'` (perceptually uniform, good for colorblind viewers), `'Greys'`, `'Blues'`, `'Reds'`.
    - **Use Case:** Representing temperature, density, elevation, or any quantity that varies from low to high.
    - **Code Example (Conceptual for `imshow`):**
        ```python
        # import matplotlib.pyplot as plt
        # import numpy as np
        # data = np.random.rand(10, 10) # 0 to 1 values
        # plt.imshow(data, cmap='viridis')
        # plt.colorbar(label='Value Intensity')
        # plt.title('Sequential Colormap: Viridis')
        # plt.show()
        ```
- Diverging
    - **Purpose:** Best for representing data where there's a meaningful midpoint (often zero), and values diverge in two directions (e.g., positive and negative). Typically use two contrasting hues that meet at a neutral color (like white or light gray) in the middle.
    - **Examples:** `'coolwarm'`, `'RdBu'` (Red-Blue), `'PiYG'` (Pink-YellowGreen), `'seismic'`, `'bwr'` (Blue-White-Red).
    - **Use Case:** Representing correlation coefficients (-1 to +1), temperature differences from an average, profit/loss.
    - **Code Example (Conceptual for `imshow`):**
        ```python
        # data_diverging = np.random.randn(10, 10) # -ve and +ve values
        # plt.imshow(data_diverging, cmap='coolwarm', vmin=-3, vmax=3) # Center around 0
        # plt.colorbar(label='Value (Diverging)')
        # plt.title('Diverging Colormap: coolwarm')
        # plt.show()
        ```
- Qualitative (Categorical)
    - **Purpose:** Best for representing nominal categorical data where there is no inherent ordering between categories. Uses a set of distinct colors.
    - **Examples:** `'Pastel1'`, `'Set1'`, `'Set2'`, `'Set3'`, `'tab10'`, `'tab20'`.
    - **Use Case:** Coloring scatter plot points by category, coloring different lines in a line plot when they represent distinct groups.
    - **Code Example (Conceptual for `scatter`):**
        ```python
        # N = 50
        # x = np.random.rand(N)
        # y = np.random.rand(N)
        # categories = np.random.randint(0, 3, N) # 3 categories
        # plt.scatter(x, y, c=categories, cmap='Set1', alpha=0.7)
        # plt.title('Qualitative Colormap: Set1 for Categories')
        # plt.show()
        ```
- Cyclic
    - **Purpose:** Best for representing data that is periodic or wraps around, such as phase angle, wind direction, or time of day. The colors at the beginning and end of the colormap are often the same or visually similar.
    - **Examples:** `'twilight'`, `'twilight_shifted'`, `'hsv'`.
    - **Use Case:** Visualizing phase data, orientation.
    - **Code Example (Conceptual):**
        ```python
        # angles = np.linspace(0, 2 * np.pi, 100)
        # data_cyclic = np.sin(angles).reshape(10,10) # Example cyclic data
        # plt.imshow(data_cyclic, cmap='hsv')
        # plt.colorbar(label='Phase Angle (Conceptual)')
        # plt.title('Cyclic Colormap: hsv')
        # plt.show()
        ```

## Choosing a Colormap
-   **Perceptual Uniformity:** Prefer colormaps that are perceptually uniform, meaning a change in data value corresponds to a proportional change in perceived color. `'viridis'`, `'plasma'`, `'inferno'`, `'magma'`, `'cividis'` are designed for this. This helps in accurate interpretation and avoids creating misleading visual emphasis.
-   **Colorblind-Friendliness:** Consider colormaps that are accessible to people with common forms of color vision deficiency. `'viridis'` and `'cividis'` are good choices.
-   **Nature of Data:** Match the colormap type (sequential, diverging, qualitative, cyclic) to the nature of your data.
-   **Avoid Rainbow Colormaps (like 'jet'):** While visually striking, 'jet' and similar rainbow colormaps are generally discouraged for scientific visualization because they are not perceptually uniform, can introduce false boundaries, and are not colorblind-friendly.

## Customizing and Manipulating Colormaps
-   **Reversing a Colormap:** Append `_r` to a colormap name (e.g., `'viridis_r'`).
-   **Getting a Colormap Object:** `cmap = plt.get_cmap('viridis')`.
-   **Creating Custom Colormaps:** Use `matplotlib.colors.ListedColormap` or `matplotlib.colors.LinearSegmentedColormap`.
-   **Normalization (`norm` argument):** Functions like `imshow` use a `matplotlib.colors.Normalize` instance to scale data values (from `vmin` to `vmax`) to the range $[0, 1]$ before mapping to colors. You can provide custom normalizers (e.g., `LogNorm` for logarithmic scaling).

## Displaying a Colorbar
A colorbar is a key that shows the mapping between data values and colors.
-   `fig.colorbar(mappable_object, ax=ax, label='My Label')`
-   `plt.colorbar(mappable_object, label='My Label')`
The `mappable_object` is typically the object returned by the plotting function (e.g., the image object from `imshow`, or the path collection from `scatter`).

Effective use of colormaps is crucial for creating informative and interpretable visualizations of scalar data.

---