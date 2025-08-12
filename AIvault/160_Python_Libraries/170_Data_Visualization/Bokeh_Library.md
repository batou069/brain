---
tags:
  - python
  - library
  - bokeh
  - data_visualization
  - interactive_plots
  - web_based_charts
  - concept
  - example
aliases:
  - Bokeh Python
related:
  - "[[_Data_Visualization_MOC]]"
  - "[[Plotly_and_Plotly_Express]]"
  - "[[Matplotlib_Overview]]"
  - "[[_Pandas_MOC]]"
worksheet:
  - WS_DataViz_1
date_created: 2025-06-09
---
# Bokeh Library

## Overview
**Bokeh** is a Python library for creating interactive visualizations for modern web browsers. It provides an elegant and concise way to construct versatile graphics, and it can extend this capability with high-performance interactivity over very large or streaming datasets. Bokeh renders its plots using HTML and JavaScript.

Bokeh can be used to create:
-   Interactive charts and plots.
-   Dashboards and data applications.
-   Visualizations for streaming data.

## Key Features and Philosophy
[list2tab|#Bokeh Features]
- Interactivity
    -   Focus on interactive tools: pan, zoom, selection, hover tooltips, clickable legends.
    -   Supports linking plots (e.g., selection in one plot updates another).
    -   Can build data applications with widgets (sliders, dropdowns, buttons) that drive plot updates via Python callbacks (when using Bokeh server).
- Web-Based Output
    -   Generates HTML/JavaScript, making plots easily embeddable in web pages or viewable as standalone HTML files.
- Multiple API Levels
    -   **`bokeh.plotting`:** A mid-level interface for creating plots by assembling glyphs (markers, lines, patches). You define a figure and add glyphs to it. This is the most common interface.
    -   **`bokeh.charts` (Deprecated):** Was a high-level interface similar to Plotly Express or Seaborn, but is no longer actively developed.
    -   **`bokeh.models`:** A low-level interface giving explicit control over all plot objects and their properties. Used for advanced customization or building custom interactive applications.
- Server Capability (`bokeh server`)
    -   Allows creation of interactive data applications where Python code can respond to UI events (widget changes, selections) and update plots dynamically. This enables building complex dashboards and apps.
- Large Data Handling
    -   Designed to handle large datasets efficiently, including server-side downsampling or streaming data to the browser.
- Versatile Glyphs
    -   Plots are constructed by adding glyphs (e.g., `circle`, `line`, `rect`, `quad`, `patch`) to a figure. Each glyph can have its properties (color, size, alpha) mapped to data columns.

## Example Usage (`bokeh.plotting` interface)

### Interactive Scatter Plot
```python
from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource, HoverTool
import pandas as pd
import numpy as np

# Conceptual e-commerce customer data
# np.random.seed(42)
# customer_data = pd.DataFrame({
#     'total_spent': np.random.uniform(50, 1000, 100),
#     'items_purchased': np.random.randint(1, 20, 100),
#     'customer_segment': np.random.choice(['A', 'B', 'C'], 100, p=[0.4, 0.4, 0.2]),
#     'recency_days': np.random.randint(1, 365, 100)
# })

# Output to static HTML file (can also output to Jupyter notebook)
# output_file("customer_scatter_bokeh.html")

# Create a ColumnDataSource (Bokeh's preferred way to pass data)
# source = ColumnDataSource(data=customer_data)

# Define tools for interactivity
# TOOLS = "pan,wheel_zoom,box_zoom,reset,save,hover"

# Create a new plot with tools
# p_scatter = figure(
#     tools=TOOLS,
#     width=700, height=500,
#     title="Customer Spending vs. Items Purchased (Bokeh)",
#     x_axis_label="Total Amount Spent ($)",
#     y_axis_label="Number of Items Purchased"
# )

# Add a circle glyph
# renderer = p_scatter.circle(
#     x='total_spent', y='items_purchased',
#     source=source,
#     size=10, # Can also map 'size' to a data column
#     # Color mapping requires more setup (e.g., CategoricalColorMapper)
#     # For simplicity, using a single color here
#     color="navy", alpha=0.6,
#     legend_label="Customers" 
# )

# Add HoverTool
# hover = HoverTool()
# hover.tooltips = [
#     ("Segment", "@customer_segment"),
#     ("Spent", "@total_spent{($0,0.00)}"), # Format as currency
#     ("Items", "@items_purchased"),
#     ("Recency", "@recency_days days")
# ]
# p_scatter.add_tools(hover)

# Customize legend
# p_scatter.legend.location = "top_right"
# p_scatter.legend.click_policy = "hide" # Click legend to hide/show glyphs

# Show the results
# show(p_scatter)
```
**Obsidian Chart Plugin Example / Conceptual Output:**
> [!note] Bokeh charts are interactive HTML/JavaScript. An Obsidian Chart block cannot directly render this.
> **Conceptual Description:** This Python code would generate an interactive HTML file (`customer_scatter_bokeh.html`).
> - The plot would be a scatter plot.
> - X-axis: Total amount spent.
> - Y-axis: Number of items purchased.
> - Points would be navy circles.
> - Interactive tools for panning, zooming, boxing zoom, resetting, and saving the plot would be available.
> - Hovering over a data point would display a tooltip with: Customer Segment, Total Spent (formatted), Items Purchased, and Recency.
> - The legend would allow toggling visibility of the "Customers" glyphs.

### Line Plot with Multiple Lines
```python
from bokeh.plotting import figure, show, output_file
from bokeh.palettes import Category10 # For distinct colors
import pandas as pd
import numpy as np

# Conceptual monthly sales data for two products
# np.random.seed(10)
# months = pd.to_datetime([f"2023-{m:02d}-01" for m in range(1, 13)])
# sales_A = 100 + np.arange(12)*10 + np.random.randn(12)*20
# sales_B = 150 + np.arange(12)*5 + np.sin(np.arange(12)/2)*30 + np.random.randn(12)*15
# sales_df = pd.DataFrame({'month': months, 'Product_A_Sales': sales_A, 'Product_B_Sales': sales_B})

# output_file("product_sales_bokeh.html")

# p_line = figure(
#     width=700, height=400, x_axis_type="datetime",
#     title="Monthly Product Sales (Bokeh)",
#     x_axis_label="Month", y_axis_label="Sales ($)"
# )

# Add line glyphs for each product
# p_line.line(x='month', y='Product_A_Sales', source=sales_df, 
#             line_width=2, color=Category10, legend_label="Product A")
# p_line.line(x='month', y='Product_B_Sales', source=sales_df,
#             line_width=2, color=Category10, legend_label="Product B", line_dash="dashed")

# p_line.legend.location = "top_left"
# p_line.legend.click_policy = "hide"

# show(p_line)
```
**Obsidian Chart Plugin Example / Conceptual Output:**
> **Conceptual Description:** This code would generate an interactive HTML line chart.
> - X-axis: Months (datetime).
> - Y-axis: Sales amount.
> - Two lines would be plotted: one for Product A (solid, one color) and one for Product B (dashed, another color).
> - Interactive tools (pan, zoom, etc.) would be available.
> - A legend would allow toggling the visibility of each product's sales line.
> - Hovering could be configured to show exact sales values and dates.

## When to Use Bokeh
-   When **rich interactivity** in a web browser is a primary goal.
-   For building **custom interactive dashboards and data applications**, especially with Bokeh server for Python-driven updates.
-   Visualizing **streaming or very large datasets** where client-side rendering needs to be efficient or server-side processing is involved.
-   When you need fine-grained control over plot elements and interactions (using `bokeh.models`).
-   If you prefer a more programmatic approach to building visualizations by composing glyphs.

## Bokeh vs. Plotly
-   **API Style:**
    -   Plotly (especially Plotly Express) often feels more "declarative" for common charts.
    -   Bokeh's `bokeh.plotting` is more "imperative" – you create a figure, then add glyphs one by one.
-   **Server Capabilities:** Both have server components (Dash for Plotly, Bokeh Server for Bokeh) for building web apps, but their architectures and ease of use for different types of apps can vary. Bokeh server is known for its ability to connect Python callbacks directly to UI events.
-   **Community & Ecosystem:** Both have strong communities. Plotly has a wider range of chart types out-of-the-box with Plotly Express.
-   **Learning Curve:** Plotly Express can be very quick to pick up. Bokeh's `bokeh.plotting` is also quite accessible. The lower-level `bokeh.models` or Plotly Graph Objects require more learning.

Bokeh is a powerful choice for creating sophisticated, interactive visualizations and data applications for the web.

---