---
tags:
  - matplotlib
  - python
  - plotting
  - 3d_plots
  - mplot3d
  - scatter3d
  - surface_plot
  - concept
  - example
aliases:
  - Matplotlib 3D
  - 3D Scatter Plot Matplotlib
  - 3D Surface Plot Matplotlib
related:
  - "[[Matplotlib_Overview]]"
  - "[[Matplotlib_Figure_Subplot_Axes]]"
  - "[[Visualizing_Multidimensional_Data]]"
worksheet:
  - WS_DataViz_1
date_created: 2025-08-20
---
# Matplotlib: 3D Plotting (`mpl_toolkits.mplot3d`)

Matplotlib provides basic capabilities for creating 3D plots through its `mpl_toolkits.mplot3d` toolkit. This toolkit extends Matplotlib's 2D plotting functionality to allow for the creation of 3D scatter plots, surface plots, wireframe plots, contour plots, bar charts, and more.

To create a 3D plot, you need to create a regular [[Matplotlib_Figure_Subplot_Axes|Figure]] and then add an `Axes3D` subplot to it.

## Creating a 3D Axes
The most common way to create a 3D axes object is:```python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D # Necessary for registering the 3D projection

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# Alternatively: ax = plt.axes(projection='3d')
```
The `projection='3d'` argument is key here. Once you have the `ax` (an `Axes3D` object), you can use its specific methods for 3D plotting.

## Common 3D Plot Types

[list2tab|#3D Plot Types]
- 3D Scatter Plot (`ax.scatter` or `ax.scatter3D`)
    - **Purpose:** To visualize the relationship between three numerical variables, where each point is plotted in 3D space. Additional dimensions can be encoded using color (`c`) and size (`s`) of markers.
    - **Example (E-commerce: Price, Rating, Review Count):**
        ```python
        import matplotlib.pyplot as plt
        import numpy as np
        # from mpl_toolkits.mplot3d import Axes3D # Already imported conceptually

        # Conceptual product data
        # np.random.seed(42)
        # n_products = 100
        # price = np.random.uniform(10, 200, n_products)
        # avg_rating = np.random.uniform(1, 5, n_products)
        # review_count = np.random.randint(5, 500, n_products)
        # # Color by a fourth variable, e.g., profit margin (conceptual)
        # profit_margin_ratio = np.random.rand(n_products)

        # fig = plt.figure(figsize=(10, 8))
        # ax = fig.add_subplot(111, projection='3d')

        # scatter = ax.scatter(price, avg_rating, review_count, 
        #                      c=profit_margin_ratio, cmap='viridis', s=50, alpha=0.7)
        
        # ax.set_title('3D Scatter Plot: Product Features')
        # ax.set_xlabel('Price ($)')
        # ax.set_ylabel('Average Rating (1-5)')
        # ax.set_zlabel('Number of Reviews')
        # fig.colorbar(scatter, label='Profit Margin Ratio', shrink=0.5, aspect=10)
        # plt.show()
        ```
    -   **Obsidian Chart Plugin Example:** Basic Obsidian Charts do not support 3D scatter plots directly. This would be described conceptually or an image embedded.
- 3D Surface Plot (`ax.plot_surface`)
    - **Purpose:** To visualize a 3D surface defined by $z = f(x,y)$. Requires X, Y, and Z data to be 2D arrays (grids).
    - **Key Parameters:** `X`, `Y`, `Z`, `cmap` (colormap), `rstride`, `cstride` (row/column stride for downsampling), `linewidth`, `edgecolor`.
    - **Example (Plotting $z = \sin(\sqrt{x^2 + y^2})$):**
        ```python
        import matplotlib.pyplot as plt
        import numpy as np
        # from mpl_toolkits.mplot3d import Axes3D

        # fig = plt.figure(figsize=(10, 8))
        # ax = fig.add_subplot(111, projection='3d')

        # Create X and Y data for the grid
        # x_surf = np.linspace(-5, 5, 50)
        # y_surf = np.linspace(-5, 5, 50)
        # X_surf, Y_surf = np.meshgrid(x_surf, y_surf)
        # Z_surf = np.sin(np.sqrt(X_surf**2 + Y_surf**2))

        # surf = ax.plot_surface(X_surf, Y_surf, Z_surf, cmap='magma', edgecolor='none')
        
        # ax.set_title('3D Surface Plot: $z = sin(\sqrt{x^2+y^2})$')
        # ax.set_xlabel('X axis')
        # ax.set_ylabel('Y axis')
        # ax.set_zlabel('Z axis (sin value)')
        # fig.colorbar(surf, shrink=0.5, aspect=10, label='Z value')
        # plt.show()
        ```
    -   **Obsidian Chart Plugin Example:** Not directly supported.
- 3D Wireframe Plot (`ax.plot_wireframe`)
    - **Purpose:** Similar to `plot_surface` but only draws the wireframe structure of the surface.
    - **Example:**
        ```python
        # (Using X_surf, Y_surf, Z_surf from surface plot example)
        # fig = plt.figure(figsize=(10, 8))
        # ax = fig.add_subplot(111, projection='3d')
        # ax.plot_wireframe(X_surf, Y_surf, Z_surf, rstride=3, cstride=3, color='cyan')
        # ax.set_title('3D Wireframe Plot')
        # plt.show()
        ```- 3D Line Plot (`ax.plot` or `ax.plot3D`)
    - **Purpose:** To plot lines or trajectories in 3D space. Takes 1D arrays for x, y, and z coordinates.
    - **Example (A helix):**
        ```python
        # fig = plt.figure(figsize=(8, 6))
        # ax = fig.add_subplot(111, projection='3d')
        # t = np.linspace(0, 10 * np.pi, 500)
        # x_line = np.sin(t)
        # y_line = np.cos(t)
        # z_line = t / (2*np.pi) # Height increases with t
        # ax.plot(x_line, y_line, z_line, label='Helical Path', color='purple')
        # ax.set_title('3D Line Plot (Helix)')
        # ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
        # ax.legend()
        # plt.show()
        ```
- 3D Bar Chart (`ax.bar3d`)
    - **Purpose:** Creates 3D bar charts. Can be hard to interpret due to occlusion.
- Contour Plots in 3D (`ax.contour3D`, `ax.contourf3D`)
    - **Purpose:** Draws 3D contour lines or filled contours for a function $z = f(x,y)$.

## Customization and Interaction
-   **Setting Axis Labels:** `ax.set_xlabel()`, `ax.set_ylabel()`, `ax.set_zlabel()`.
-   **Setting Axis Limits:** `ax.set_xlim()`, `ax.set_ylim()`, `ax.set_zlim()`.
-   **Setting View Angle:** `ax.view_init(elev, azim)` where `elev` is elevation angle and `azim` is azimuthal angle. This is crucial for finding a good perspective. Interactive rotation is often available in Matplotlib backends (e.g., Qt, Tk, Jupyter with `%matplotlib widget`).
-   **Colormaps (`cmap`):** Used extensively in surface and scatter plots to map values to colors.

## Challenges of 3D Plotting
-   **Occlusion:** Objects in the foreground can hide objects in the background.
-   **Perspective Distortion:** The perception of depth and relative sizes can be tricky.
-   **Difficulty in Reading Exact Values:** Harder to read precise data values compared to 2D plots.
-   **Interactivity is Often Key:** The ability to rotate, zoom, and pan 3D plots interactively is very important for understanding them. Static 3D plots can be less effective.

While Matplotlib's 3D capabilities are useful for basic 3D visualization, for highly interactive and advanced 3D graphics, specialized libraries like Plotly, Mayavi, or PyVista might offer more features.

---