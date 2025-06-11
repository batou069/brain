---
tags:
  - plotly
  - python
  - data_visualization
  - interactive_plotting
  - 3d_plots
  - scatter3d
  - surface
  - mesh
  - concept
  - example
aliases:
  - Plotly 3D Charts
  - 3D Scatter Plotly
  - 3D Surface Plotly
related:
  - "[[170_Data_Visualization/Plotly/_Plotly_MOC|_Plotly_MOC]]"
  - "[[Plotly_Express_Quickstarts]]"
  - "[[Plotly_Graph_Objects_Detailed]]"
  - "[[Visualizing_Multidimensional_Data]]"
worksheet:
  - WS_DataViz_1
date_created: 2025-06-11
---
# Plotly: 3D Plots

Plotly provides robust support for creating various types of interactive 3D visualizations. These are useful for exploring relationships between three numerical variables or visualizing surfaces and volumes. Common 3D plot types include 3D scatter plots, 3D line plots, 3D surface plots, and 3D mesh plots.

These are typically created using functions from [[Plotly_Express_Quickstarts|`plotly.express` (`px`)]] or by constructing traces from [[Plotly_Graph_Objects_Detailed|`plotly.graph_objects` (`go`)]].

## Common 3D Plot Types

[list2tab|#3D Plot Types]
- `px.scatter_3d` / `go.Scatter3d`
    -   **Purpose:** Creates a 3D scatter plot to visualize the relationship between three numerical variables. Additional dimensions can be encoded using color and size of markers.
    -   **Key Parameters (`px.scatter_3d`):**
        -   `data_frame`: Pandas DataFrame.
        -   `x`, `y`, `z`: Column names for the three axes.
        -   `color`: Column for color mapping.
        -   `size`: Column for marker size mapping.
        -   `symbol`: Column for marker symbol mapping (categorical).
        -   `hover_name`, `hover_data`.
        -   `opacity`.
    -   **Key Parameters (`go.Scatter3d`):**
        -   `x`, `y`, `z`: Lists or arrays of coordinates.
        -   `mode`: `{'markers', 'lines', 'lines+markers', 'text'}`.
        -   `marker=dict(color=..., size=..., symbol=...)`.
        -   `line=dict(color=..., width=...)`.
    -   **Example (Visualizing product features: price, rating, weight):**
        ```python
        import plotly.express as px
        import pandas as pd
        import numpy as np

        # Conceptual product data
        # np.random.seed(42)
        # df_3d_products = pd.DataFrame({
        #     'price': np.random.uniform(10, 300, 100),
        #     'customer_rating': np.random.uniform(1, 5, 100).round(1),
        #     'product_weight_kg': np.random.uniform(0.1, 5, 100).round(2),
        #     'category': np.random.choice(['A', 'B', 'C'], 100)
        # })

        # fig_scatter3d = px.scatter_3d(
        #     df_3d_products,
        #     x='price',
        #     y='customer_rating',
        #     z='product_weight_kg',
        #     color='category',
        #     size='price', # Example: size by price itself
        #     opacity=0.7,
        #     title="3D Scatter Plot of Product Features",
        #     labels={'price': 'Price ($)', 'customer_rating': 'Rating', 'product_weight_kg': 'Weight (kg)'}
        # )
        # fig_scatter3d.update_layout(margin=dict(l=0, r=0, b=0, t=40)) # Adjust margins
        # fig_scatter3d.show()
        ```
- `px.line_3d` / `go.Scatter3d` (with `mode='lines'` or `'lines+markers'`)
    -   **Purpose:** Creates a 3D line plot, often used to visualize trajectories or paths in 3D space.
    -   **Key Parameters:** Similar to `scatter_3d`, but `mode` in `go.Scatter3d` would be set to include lines. Plotly Express `px.line_3d` implies lines.
    -   **Example (Simulated trajectory of a drone):**
        ```python
        import plotly.express as px
        import pandas as pd
        import numpy as np

        # Conceptual drone trajectory data
        # t = np.linspace(0, 2 * np.pi, 100)
        # x_traj = np.cos(t)
        # y_traj = np.sin(t)
        # z_traj = t / (2 * np.pi) # Increasing altitude
        # drone_path_df = pd.DataFrame({'x': x_traj, 'y': y_traj, 'z': z_traj, 'time': t})

        # fig_line3d = px.line_3d(
        #     drone_path_df,
        #     x='x', y='y', z='z',
        #     color='time', # Color line by time
        #     title="Drone Flight Path",
        #     labels={'z': 'Altitude'}
        # )
        # fig_line3d.update_traces(marker=dict(size=3)) # Add small markers if desired
        # fig_line3d.show()
        ```
- `go.Surface` (No direct Plotly Express equivalent, built with Graph Objects)
    -   **Purpose:** Creates a 3D surface plot from a grid of x, y, and z coordinates. Useful for visualizing functions $z = f(x,y)$.
    -   **Key Parameters (`go.Surface`):**
        -   `x`, `y`: 1D arrays defining the grid.
        -   `z`: 2D array of z-values corresponding to the x-y grid.
        -   `colorscale`: Colormap for the surface.
        -   `contours`: Settings for displaying contour lines on the surface.
    -   **Example (Plotting $z = \sin(\sqrt{x^2 + y^2})$ ):**
        ```python
        import plotly.graph_objects as go
        import numpy as np

        # Define grid
        # x_surf = np.linspace(-5, 5, 50)
        # y_surf = np.linspace(-5, 5, 50)
        # X_grid, Y_grid = np.meshgrid(x_surf, y_surf)
        # Z_grid = np.sin(np.sqrt(X_grid**2 + Y_grid**2))

        # fig_surface = go.Figure(data=[
        #     go.Surface(z=Z_grid, x=X_grid, y=Y_grid, colorscale='Viridis')
        # ])
        # fig_surface.update_layout(
        #     title='3D Surface Plot: z = sin(sqrt(x² + y²))',
        #     scene=dict(
        #         xaxis_title='X Axis',
        #         yaxis_title='Y Axis',
        #         zaxis_title='Z Axis (sin value)'
        #     ),
        #     autosize=False, width=700, height=700,
        #     margin=dict(l=65, r=50, b=65, t=90)
        # )
        # fig_surface.show()
        ```
- `go.Mesh3d`
    -   **Purpose:** Creates 3D mesh plots, defined by a set of vertices and faces (typically triangles or quadrilaterals). Used for visualizing complex 3D geometries.
    -   **Key Parameters:** `x`, `y`, `z` (coordinates of vertices), `i`, `j`, `k` (indices defining triangular faces), `intensity`, `colorscale`.
    -   More complex to set up data for, often used in scientific visualization or CAD-like applications.

## Interactivity in 3D Plots
Plotly's 3D plots are inherently interactive:
-   **Rotation:** Click and drag to rotate the plot and view from different angles.
-   **Zoom:** Use mouse wheel or pinch gestures to zoom in/out.
-   **Pan:** Often possible with specific mouse button combinations or modebar tools.
-   **Hover Tooltips:** Provide information about individual data points.

## Layout for 3D Scenes (`layout.scene`)
When working with 3D plots, the layout is configured via the `scene` attribute within `fig.update_layout()`:
```python
# fig.update_layout(
#     scene=dict(
#         xaxis=dict(title='X Label', backgroundcolor="rgb(200, 200, 230)"),
#         yaxis=dict(title='Y Label', showgrid=False),
#         zaxis=dict(title='Z Label', range=[-5, 5]),
#         camera=dict(
#             eye=dict(x=1.25, y=1.25, z=1.25) # Set initial camera view
#         ),
#         aspectmode='cube' # 'data', 'cube', 'auto', 'manual'
#     )
# )
```
-   `xaxis`, `yaxis`, `zaxis`: Dictionaries to configure each 3D axis (title, range, gridlines, background).
-   `camera`: Controls the viewpoint (eye position, center, up vector).
-   `aspectmode`, `aspectratio`: Control the aspect ratio of the 3D scene.

3D plotting with Plotly allows for insightful exploration of data with three numerical dimensions, offering a level of interactivity that is very helpful for understanding complex structures.

---