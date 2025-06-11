---
tags:
  - plotly
  - python
  - data_visualization
  - interactive_plotting
  - graph_objects
  - go
  - low_level_api
  - concept
  - example
aliases:
  - Plotly Graph Objects
  - go.Figure
  - Plotly Traces
  - Plotly Layout Customization
related:
  - "[[170_Data_Visualization/Plotly/_Plotly_MOC|_Plotly_MOC]]"
  - "[[Plotly_Overview_Architecture]]"
  - "[[Plotly_Express_Quickstarts]]"
worksheet:
  - WS_DataViz_1
date_created: 2025-06-11
---
# Plotly: Graph Objects (`go`)

While [[Plotly_Express_Quickstarts|Plotly Express (`px`)]] provides a high-level interface for creating figures quickly, **Plotly Graph Objects** (typically imported as `go` from `plotly.graph_objects`) offer a lower-level, more explicit API for building and customizing Plotly figures. Every Plotly Express figure is ultimately composed of Graph Objects.

Using Graph Objects gives you fine-grained control over every aspect of the visualization, including individual traces, layout properties, annotations, shapes, and UI elements.

## Core Structure: `go.Figure`
A Plotly figure created with Graph Objects is an instance of `go.Figure`. This object has two main attributes that define the plot:
1.  **`data`**: A list of **traces**. Each trace is an object representing a specific type of plot (e.g., `go.Scatter`, `go.Bar`, `go.Pie`) and the data it displays.
2.  **`layout`**: An object (`go.Layout`) that defines the non-data-related appearance of the figure (e.g., title, axis labels, legend, colors, fonts).

See [[Plotly_Overview_Architecture]] for more details on this structure.

## Creating a Figure with Graph Objects

The general workflow is:
1.  Create an empty `go.Figure` object or initialize it with a list of traces.
2.  Add traces to the figure using `fig.add_trace(go.SomeTraceType(...))`.
3.  Update the figure's layout using `fig.update_layout(...)` and specific axis updates like `fig.update_xaxes(...)`, `fig.update_yaxes(...)`.
4.  Display the figure using `fig.show()`.

**Example: Basic Scatter Plot with Graph Objects**
```python
import plotly.graph_objects as go
import numpy as np
import pandas as pd # For creating example data

# Conceptual e-commerce data: number of items in cart vs. total order value
np.random.seed(42)
num_items = np.random.randint(1, 10, 50)
order_value = num_items * np.random.uniform(5, 25, 50) + np.random.normal(0, 10, 50)
order_value = np.clip(order_value, 5, None) # Ensure positive order value

# 1. Create an empty Figure object
fig = go.Figure()

# 2. Add a Scatter trace
fig.add_trace(go.Scatter(
    x=num_items,
    y=order_value,
    mode='markers', # 'lines', 'lines+markers', 'text'
    name='Customer Orders', # Appears in legend
    marker=dict(
        color='royalblue',
        size=10,
        opacity=0.7,
        line=dict(width=1, color='DarkSlateGrey')
    ),
    text=[f"Items: {ni}, Value: ${ov:.2f}" for ni, ov in zip(num_items, order_value)], # Hover text
    hoverinfo='text'
))

# 3. Update the layout
fig.update_layout(
    title_text="Order Value vs. Number of Items in Cart",
    title_x=0.5, # Center title
    xaxis_title="Number of Items",
    yaxis_title="Total Order Value ($)",
    legend_title_text="Data Series",
    plot_bgcolor='rgba(240, 240, 240, 0.95)', # Light gray plot background
    paper_bgcolor='white',
    font=dict(family="Arial, sans-serif", size=12, color="black")
)

# Customize axes
fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGrey')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGrey', zeroline=True, zerolinewidth=2, zerolinecolor='Black')

# 4. Show the figure
# fig.show()
```

## Common Trace Types (`go.*`)
Plotly offers a vast array of trace types. Some common ones include:

[list2tab|#Common GO Traces]
- `go.Scatter`
    -   For line plots (`mode='lines'`), scatter plots (`mode='markers'`), or both (`mode='lines+markers'`).
    -   Also used for time series, area plots (with `fill` attribute).
- `go.Bar`
    -   For vertical or horizontal bar charts.
    -   Attributes: `x`, `y`, `orientation` ('v' or 'h'), `marker_color`, `text`.
- `go.Pie`
    -   For pie charts.
    -   Attributes: `labels`, `values`, `hole` (for donut charts), `marker_colors`.
- `go.Histogram`
    -   For histograms.
    -   Attributes: `x` (or `y`), `nbinsx`, `histnorm` ('percent', 'probability', 'density', 'probability density').
- `go.Box`
    -   For box plots.
    -   Attributes: `y` (or `x`), `name`, `boxpoints` ('all', 'outliers', 'suspectedoutliers', False).
- `go.Violin`
    -   For violin plots.
    -   Attributes: `y` (or `x`), `name`, `box_visible`, `points`.
- `go.Heatmap`
    -   For heatmaps.
    -   Attributes: `z` (2D array of values), `x` (column labels), `y` (row labels), `colorscale`.
- `go.Contour`
    -   For contour plots.
- `go.Table`
    -   For creating tables within a figure.
- 3D Traces
    -   `go.Scatter3d`: For 3D scatter and line plots.
    -   `go.Surface`: For 3D surface plots from a grid of z-values.
    -   `go.Mesh3d`: For 3D mesh plots.
- Map Traces
    -   `go.Scattergeo`, `go.Choropleth`: For geographical maps using natural Earth projection.
    -   `go.Scattermapbox`, `go.Choroplethmapbox`, `go.Densitymapbox`: For tile-based maps using Mapbox.

Each trace type has many specific attributes to control its appearance and behavior.

## Updating Layout and Traces
-   **`fig.update_layout(**kwargs)`:** Modifies attributes of the `layout` object (e.g., title, axes, legend, colors, fonts, annotations, shapes). Can update nested attributes using dictionary-style updates or underscore notation (e.g., `xaxis_title_text='X'`).
-   **`fig.update_xaxes(**kwargs)`, `fig.update_yaxes(**kwargs)`, `fig.update_zaxes(**kwargs)`:** Specific methods to update properties of the x, y, or z axes. Can target specific axes in subplots using `row` and `col` arguments.
-   **`fig.add_annotation(...)`, `fig.add_shape(...)`, `fig.add_vline(...)`, `fig.add_hline(...)`:** Add specific layout elements.
-   **`fig.update_traces(patch, selector=None, row=None, col=None)`:** Modifies attributes of existing traces.
    -   `patch`: A dictionary of attributes to update.
    -   `selector`: A dictionary or a function to select which traces to update. If `None`, updates all traces.
-   **`fig.add_trace(trace, row=None, col=None)`:** Adds a new trace, optionally to a specific subplot in a figure created with `make_subplots`.

**Example: Figure with Multiple Traces and Subplots**
```python
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Data for two product categories' monthly clicks
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
clicks_product_A = 
clicks_product_B = 

# Revenue data
revenue_product_A = 
revenue_product_B = 

# Create a figure with 1 row and 2 columns
fig = make_subplots(rows=1, cols=2,
                    subplot_titles=("Monthly Clicks per Product", "Monthly Revenue per Product"))

# Subplot 1: Clicks (Bar chart)
fig.add_trace(go.Bar(name='Product A Clicks', x=months, y=clicks_product_A, marker_color='indianred'),
              row=1, col=1)
fig.add_trace(go.Bar(name='Product B Clicks', x=months, y=clicks_product_B, marker_color='lightsalmon'),
              row=1, col=1)

# Subplot 2: Revenue (Line chart)
fig.add_trace(go.Scatter(name='Product A Revenue', x=months, y=revenue_product_A, mode='lines+markers', line=dict(color='blue')),
              row=1, col=2)
fig.add_trace(go.Scatter(name='Product B Revenue', x=months, y=revenue_product_B, mode='lines+markers', line=dict(color='green')),
              row=1, col=2)

# Update layout for the entire figure
fig.update_layout(
    title_text="E-commerce Product Performance Dashboard",
    title_x=0.5,
    height=500,
    barmode='group' # For the bar chart in subplot 1
)

# Update axes titles for each subplot
fig.update_xaxes(title_text="Month", row=1, col=1)
fig.update_yaxes(title_text="Number of Clicks", row=1, col=1)
fig.update_xaxes(title_text="Month", row=1, col=2)
fig.update_yaxes(title_text="Revenue ($)", row=1, col=2)

# fig.show()
```

Working with Graph Objects provides maximum flexibility for creating sophisticated, highly customized interactive visualizations. While [[Plotly_Express_Quickstarts|Plotly Express]] is great for quick plots, understanding Graph Objects allows you to fine-tune every detail and build complex dashboards or specialized charts.

---