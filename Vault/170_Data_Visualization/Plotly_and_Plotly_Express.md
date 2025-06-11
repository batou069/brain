---
tags:
  - python
  - library
  - plotly
  - plotly_express
  - data_visualization
  - interactive_plots
  - web_based_charts
  - concept
  - example
aliases:
  - Plotly
  - Plotly Express
  - px
  - go (plotly.graph_objects)
related:
  - "[[_Data_Visualization_MOC]]"
  - "[[Dash_Framework]]"
  - "[[Matplotlib_Overview]]"
  - "[[Seaborn_MOC|_Seaborn_MOC]]"
worksheet:
  - WS_DataViz_1
date_created: 2025-06-09
---
# Plotly and Plotly Express

## Overview
**Plotly** is a versatile Python graphing library that makes interactive, publication-quality graphs online and offline. Plotly figures are inherently interactive: users can zoom, pan, hover over data points to see values, and toggle series visibility.

**Plotly Express** (`plotly.express` or `px`) is a high-level wrapper for Plotly that provides a simple and concise syntax for creating a wide variety of common figures. It's similar in spirit to [[170_Data_Visualization/Seaborn/_Seaborn_MOC|Seaborn]] but produces interactive Plotly figures. For more complex or customized figures, one can use the lower-level **Plotly Graph Objects** (`plotly.graph_objects` or `go`).

## Key Features
[list2tab|#Plotly Features]
- Interactivity
    -   Built-in zooming, panning, hovering, data point selection.
    -   Animations and sliders can be added.
- Wide Range of Chart Types
    -   Basic charts: [[Scatter_Plot|scatter]], [[Line_Plot|line]], [[Bar_Chart|bar]], [[Pie_Chart|pie]], [[Histogram|histogram]], [[Box_Plot|box]].
    -   Statistical charts: violin plots, ECDF, distplots.
    -   Financial charts: candlestick, OHLC.
    -   3D charts: scatter3d, surface, mesh.
    -   Maps: scatter_mapbox, choropleth_mapbox, scatter_geo, choropleth.
    -   Specialized charts: sunburst, treemap, sankey diagrams, parallel coordinates.
- Publication Quality & Customization
    -   Highly customizable appearance (layout, traces, annotations).
    -   Figures can be exported as static images (PNG, JPEG, SVG, PDF) or interactive HTML files.
- Pandas Integration
    -   Plotly Express works seamlessly with Pandas DataFrames.
- Web-Based & Offline Use
    -   Figures can be embedded in Jupyter notebooks, web applications (e.g., using [[Dash_Framework|Dash]]), or saved as standalone HTML files.
    -   Offline mode allows creating figures without needing an internet connection or Plotly account.
- Plotly Express (`px`)
    -   Provides a very concise, high-level API for creating figures. A single function call can often generate a complex, interactive plot.
    -   Example: `px.scatter(data_frame, x="col_x", y="col_y", color="col_cat", size="col_num")`
- Plotly Graph Objects (`go`)
    -   A lower-level, object-oriented API that gives fine-grained control over every aspect of the figure. Figures are composed of "traces" (like scatter markers, lines) and a "layout".
    -   `fig = go.Figure(data=[go.Scatter(...)], layout=go.Layout(...))`

## Example Usage (Plotly Express)

### Scatter Plot with E-commerce Data```python
import plotly.express as px
import pandas as pd
import numpy as np

# Conceptual e-commerce customer data
# np.random.seed(42)
# customer_data = pd.DataFrame({
#     'customer_id': range(100),
#     'total_spent': np.random.uniform(50, 1000, 100),
#     'items_purchased': np.random.randint(1, 20, 100),
#     'customer_segment': np.random.choice(['A', 'B', 'C'], 100, p=[0.4, 0.4, 0.2]),
#     'days_since_last_purchase': np.random.randint(1, 365, 100)
# })

# Create an interactive scatter plot
# fig_scatter = px.scatter(customer_data,
#                          x="total_spent",
#                          y="items_purchased",
#                          color="customer_segment",
#                          size="days_since_last_purchase", # Size of marker by recency
#                          hover_name="customer_id", # Show customer_id on hover
#                          title="Customer Spending vs. Items Purchased by Segment",
#                          labels={'total_spent': 'Total Amount Spent ($)', 
#                                  'items_purchased': 'Number of Items Purchased'},
#                          color_discrete_map={'A': 'blue', 'B': 'green', 'C': 'red'})

# fig_scatter.update_layout(legend_title_text='Segment')
# To display in a Jupyter notebook or save:
# fig_scatter.show()
# fig_scatter.write_html("customer_scatter.html")
```
**Obsidian Chart Plugin Example / Conceptual Output:**
> [!note] Plotly charts are interactive HTML/JavaScript. An Obsidian Chart block cannot directly render this.
> **Conceptual Description:** This would generate an interactive scatter plot.
> - Each point represents a customer.
> - X-axis: Total amount spent.
> - Y-axis: Number of items purchased.
> - Color: Customer segment (A, B, or C).
> - Size of point: Days since last purchase (larger means longer ago).
> - Hovering over a point would show details like `customer_id`, total spent, items purchased, segment, and recency.
> - Users could zoom, pan, and filter by clicking on legend items.

### Bar Chart
```python
# import plotly.express as px
# import pandas as pd

# Conceptual: Average order value per product category
# category_data = pd.DataFrame({
#     'category': ['Electronics', 'Books', 'Clothing', 'Home Goods'],
#     'avg_order_value': [150.75, 45.50, 75.20, 95.00]
# })

# fig_bar = px.bar(category_data,
#                  x="category",
#                  y="avg_order_value",
#                  color="category", # Color bars by category
#                  title="Average Order Value by Product Category",
#                  labels={'avg_order_value': 'Average Order Value ($)'},
#                  text_auto=True) # Display values on bars

# fig_bar.update_layout(showlegend=False) # Hide legend if color is just for distinction
# fig_bar.show()
```
**Obsidian Chart Plugin Example / Conceptual Output:**
> **Conceptual Description:** This would generate an interactive bar chart.
> - X-axis: Product categories.
> - Y-axis: Average order value.
> - Each bar would be colored, and the value ($) would be displayed on or above the bar.
> - Hovering would show exact values.

## When to Use Plotly
-   When **interactivity** is a primary requirement (zooming, panning, tooltips on hover).
-   For creating web-based dashboards and reports (especially with [[Dash_Framework|Dash]]).
-   When needing a wide variety of modern chart types out-of-the-box.
-   For presentations where users can explore the data live.
-   `Plotly Express` is excellent for quick, interactive EDA with Pandas DataFrames.
-   `Plotly Graph Objects` offers deep customization for complex, bespoke visualizations.

## Plotly vs. Matplotlib/Seaborn
-   **Interactivity:** Plotly's core strength. Matplotlib/Seaborn are primarily for static plots, though some interactivity can be added in specific environments (like Jupyter with `ipympl`).
-   **Output:** Plotly outputs HTML/JavaScript. Matplotlib outputs various static formats (PNG, PDF, SVG) and can render in GUI backends.
-   **Ease of Use (High-Level):** Plotly Express is comparable to Seaborn in ease of use for common plots.
-   **Customization (Low-Level):** Both Plotly Graph Objects and Matplotlib's OO API offer extensive customization, but their APIs differ significantly.

Plotly provides a powerful suite of tools for creating rich, interactive data visualizations suitable for modern web environments and exploratory analysis.

---