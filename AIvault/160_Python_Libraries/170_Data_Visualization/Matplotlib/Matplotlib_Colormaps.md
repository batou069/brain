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
  - colormaps
  - heatmap
  - scatter_plot
aliases:
  - Matplotlib cmaps
  - Color Maps in Matplotlib
  - Matplotlib cmap
  - Sequential Colormaps
  - Diverging Colormaps
  - Qualitative Colormaps
related:
  - "[[160_Python_Libraries/170_Data_Visualization/Matplotlib/_Matplotlib_MOC|_Matplotlib_MOC]]"
  - "[[Matplotlib_Image_Display_imshow|Matplotlib imshow]]"
  - "[[Scatter_Plot]]"
  - "[[Heatmap]]"
  - "[[Matplotlib_Image_Display_imshow|imshow]]"
worksheet:
  - WS_DataViz_1
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Matplotlib: Colormaps (`cmap`)

A **colormap** (or color map) in Matplotlib is a mapping from data values (often scalar values in a 2D array) to colors. Colormaps are essential for visualizing data where color intensity or hue represents a quantity, such as in [[170_Data_Visualization/Plot_Types/Heatmap|heatmaps]], contour plots, or when encoding a third dimension in a [[Scatter_Plot|scatter plot]] using color.

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

# Matplotlib: Working with Colormaps (`cmap`)

**Colormaps** (or color maps) in Matplotlib are mappings from data values (often scalar data in a 2D array, or the `c` argument in a scatter plot) to colors. They are essential for visualizing data where color intensity or hue represents a numerical quantity or a category.

Colormaps are specified using the `cmap` argument in various Matplotlib functions like `imshow()`, `scatter()`, `pcolormesh()`, `contourf()`.

## Types of Colormaps
Matplotlib provides a wide variety of built-in colormaps, generally categorized into:

1.  **Sequential Colormaps:**
    -   **Purpose:** Used for representing data that has a natural ordering, typically progressing from low to high values (or vice-versa).
    -   **Characteristics:** Usually change in lightness and often saturation of a single hue, or progress through a sequence of related hues.
    -   **Examples:** `'viridis'` (default for many functions now), `'plasma'`, `'inferno'`, `'magma'`, `'cividis'` (perceptually uniform, good for colorblindness), `'Greys'`, `'Blues'`, `'Reds'`, `'Greens'`.
    -   **Use Case:** Visualizing temperature, density, elevation, or any quantity where values range from low to high.

2.  **Diverging Colormaps:**
    -   **Purpose:** Used for representing data where values diverge from a central, meaningful midpoint (often zero).
    -   **Characteristics:** Typically use two contrasting colors for the extremes and a neutral color (like white or light gray) for the midpoint.
    -   **Examples:** `'coolwarm'` (blue-white-red), `'RdBu'` (Red-White-Blue), `'PiYG'` (Pink-Yellow-Green), `'seismic'` (blue-white-red, good for +/- deviations).
    -   **Use Case:** Visualizing correlation coefficients (-1 to +1), differences from a mean, profit/loss.

3.  **Qualitative (Categorical) Colormaps:**
    -   **Purpose:** Used for representing categorical data where there is no inherent ordering of categories.
    -   **Characteristics:** Use a set of distinct, easily distinguishable colors. The number of distinct colors is usually limited.
    -   **Examples:** `'Pastel1'`, `'Pastel2'`, `'Paired'`, `'Accent'`, `'Set1'`, `'Set2'`, `'Set3'`, `'tab10'`, `'tab20'`.
    -   **Use Case:** Coloring scatter plot points by category, coloring different bars in a bar chart representing different groups.

4.  **Cyclic Colormaps:**
    -   **Purpose:** Used for representing data where values wrap around (e.g., phase angle, wind direction).
    -   **Characteristics:** Colors at the beginning and end of the colormap are the same.
    -   **Examples:** `'twilight'`, `'twilight_shifted'`, `'hsv'`.

## Using Colormaps

**1. In `imshow()` for 2D arrays (e.g., heatmaps, images):**
```python
import matplotlib.pyplot as plt
import numpy as np

# Conceptual e-commerce data: heatmap of product co-occurrence
# Rows/Cols could be product IDs, values are co-purchase counts
cooccurrence_matrix = np.random.rand(5, 5) 
# Make it symmetric for a co-occurrence feel
cooccurrence_matrix = (cooccurrence_matrix + cooccurrence_matrix.T) / 2 
np.fill_diagonal(cooccurrence_matrix, 0) # No self-co-occurrence for this example

# fig, ax = plt.subplots()
# im = ax.imshow(cooccurrence_matrix, cmap='viridis') # 'viridis' is a sequential colormap
# ax.set_title("Product Co-occurrence Heatmap (Viridis)")
# fig.colorbar(im, label="Co-occurrence Score")
# plt.show()

# Using a diverging colormap if data had a meaningful midpoint (e.g., correlation)
# correlation_matrix = np.random.uniform(-1, 1, (5,5))
# correlation_matrix = (correlation_matrix + correlation_matrix.T)/2
# np.fill_diagonal(correlation_matrix, 1)

# fig2, ax2 = plt.subplots()
# im2 = ax2.imshow(correlation_matrix, cmap='coolwarm', vmin=-1, vmax=1)
# ax2.set_title("Correlation Matrix (Coolwarm)")
# fig2.colorbar(im2, label="Correlation Coefficient")
# plt.show()
```

**2. In `scatter()` for coloring points by a third variable:**
```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Conceptual product data: price, rating, and units_sold
# product_scatter_data = pd.DataFrame({
#     'price': np.random.uniform(10, 200, 100),
#     'rating': np.random.uniform(2.5, 5.0, 100).round(1),
#     'units_sold': np.random.randint(10, 500, 100),
#     'category': np.random.choice(['Elec', 'Book', 'App'], 100)
# })

# fig, ax = plt.subplots(1, 2, figsize=(14, 5))

# Scatter plot with color mapped to a continuous variable ('units_sold')
# sc1 = ax.scatter(
#     product_scatter_data['price'], product_scatter_data['rating'],
#     c=product_scatter_data['units_sold'], # Color by units_sold
#     cmap='plasma', # Sequential colormap
#     s=50, alpha=0.7
# )
# fig.colorbar(sc1, ax=ax, label='Units Sold')
# ax.set_title("Price vs. Rating (Color by Units Sold)")
# ax.set_xlabel("Price ($)")
# ax.set_ylabel("Customer Rating")

# Scatter plot with color mapped to a categorical variable ('category')
# For categorical, it's often better to use Seaborn or manually map categories to colors
# Here, we'll map categories to integers then use a qualitative cmap, or let scatter handle it
# unique_categories = product_scatter_data['category'].unique()
# category_to_int = {cat: i for i, cat in enumerate(unique_categories)}
# product_scatter_data['category_int'] = product_scatter_data['category'].map(category_to_int)

# sc2 = ax.scatter(
#     product_scatter_data['price'], product_scatter_data['rating'],
#     c=product_scatter_data['category_int'],
#     cmap='tab10', # Qualitative colormap
#     s=50, alpha=0.7
# )
# # Create a custom legend for categorical colors
# handles = [plt.Line2D(,, marker='o', color='w', label=cat,
#                       markerfacecolor=plt.cm.tab10(i/len(unique_categories))) for i, cat in enumerate(unique_categories)]
# ax.legend(handles=handles, title="Category")
# ax.set_title("Price vs. Rating (Color by Category)")
# ax.set_xlabel("Price ($)")
# ax.set_ylabel("Customer Rating")

# plt.tight_layout()
# plt.show()
```

## Getting and Modifying Colormaps
-   You can get a colormap object using `plt.cm.get_cmap('name')` or `matplotlib.colormaps['name']`.
-   Colormaps can be reversed by appending `_r` to their name (e.g., `'viridis_r'`).
-   You can create custom colormaps using `matplotlib.colors.LinearSegmentedColormap` or `ListedColormap`.

## Colorbars (`plt.colorbar()` / `fig.colorbar()`)
When using a colormap to map data values to colors (e.g., in `imshow` or `scatter` with a `c` array), a **colorbar** is essential to show the mapping between colors and data values.
-   `fig.colorbar(mappable_object, ax=ax, label="Description", orientation="vertical"/"horizontal")`
    -   `mappable_object`: The object returned by the plotting function (e.g., the `PathCollection` from `scatter`, or the `AxesImage` from `imshow`).

## Choosing Colormaps
-   **Perceptually Uniform Colormaps:** For sequential data, prefer colormaps like 'viridis', 'plasma', 'inferno', 'magma', 'cividis'. These are designed such that changes in lightness correspond linearly to changes in data values, making them easier to interpret correctly and often better for colorblind individuals.
-   **Avoid Rainbow Colormaps (like 'jet'):** While colorful, 'jet' and similar rainbow colormaps can introduce artificial visual boundaries and distort perception of data due to non-uniform changes in lightness.
-   **Consider Colorblindness:** Use tools or guidelines (e.g., ColorBrewer2.org) to choose colorblind-friendly palettes.

Colormaps are a powerful tool for adding another dimension of information to your plots or for clearly representing matrix-like data.

---