---
tags:
  - python
  - data_visualization
  - plotting
  - plotly
  - plotly_express
  - interactive_plots
  - web_based_viz
  - library
  - concept
  - example
aliases:
  - Plotly
  - Plotly.Express
  - Interactive Python Plots
related:
  - "[[_Data_Visualization_MOC]]"
  - "[[_Pandas_MOC]]"
  - "[[_Matplotlib_MOC]]"
  - "[[170_Data_Visualization/Seaborn/_Seaborn_MOC|Seaborn]]"
  - "[[Bokeh_Library]]"
  - "[[Dash_Plotly]]"
worksheet:
  - WS_DataViz_1
date_created: 2025-08-20
---
# Plotly and Plotly Express

**Plotly** is a versatile Python graphing library that makes interactive, publication-quality graphs. Plotly graphs can be rendered in Jupyter notebooks, standalone HTML files, or embedded in web applications using [[Dash_Plotly|Dash]].

**Plotly Express** (`plotly.express` or `px`) is a high-level wrapper for Plotly that provides a simple and concise syntax for creating a wide variety of figures. It's often the recommended starting point for creating Plotly figures, similar to how Seaborn provides a high-level interface for Matplotlib.

## Key Features of Plotly & Plotly Express
-   **Interactivity:** Generated plots are inherently interactive, allowing for zoom, pan, hover-to-see-data, and selection of data points.
-   **Web-Based:** Outputs are typically HTML/JavaScript, making them suitable for web embedding and sharing.
-   **Wide Range of Chart Types:** Supports common charts like scatter, line, bar, histogram, box, violin, pie, as well as more specialized ones like 3D plots, maps (choropleth, scatter_mapbox), sunbursts, treemaps, parallel coordinates, etc.
-   **High-Level API (Plotly Express):** `plotly.express` allows creating complex figures with a single function call, often directly from [[_Pandas_MOC|Pandas DataFrames]]. It automatically handles many details like legends and color mapping.
-   **Lower-Level API (Graph Objects - `plotly.graph_objects` or `go`):** For more fine-grained control and customization, Plotly provides a "Graph Objects" interface. Plotly Express functions actually return `plotly.graph_objects.Figure` instances, which can then be further customized.
-   **Animations and Sliders:** Supports creating animated plots and plots with interactive controls like sliders and dropdowns.
-   **Theming and Templates:** Offers built-in themes for styling plots.
-   **Export Options:** Can export to static image formats (PNG, JPG, SVG, PDF - requires `kaleido` package) and interactive HTML.
-   **Integration with Dash:** Plotly is the core visualization engine for Dash, a Python framework for building analytical web applications.

## Plotly Express (`px`) - Common Usage
Plotly Express functions typically accept a Pandas DataFrame as the first argument and then column names as strings for `x`, `y`, `color`, `size`, `facet_row`, `facet_col`, etc.

**Example: Interactive Scatter Plot of E-commerce Product Data**
```python
import plotly.express as px
import pandas as pd
import numpy as np

# Conceptual product data
# np.random.seed(42)
# product_data = pd.DataFrame({
#     'product_name': [f"Product {i}" for i in range(50)],
#     'price': np.random.uniform(10, 500, 50),
#     'avg_rating': np.random.uniform(1, 5, 50).round(1),
#     'category': np.random.choice(['Electronics', 'Books', 'Apparel', 'Home Goods'], 50),
#     'units_sold': np.random.randint(5, 200, 50)
# })

# Create an interactive scatter plot
# fig_scatter = px.scatter(
#     product_data,
#     x="price",
#     y="avg_rating",
#     color="category",         # Color points by category
#     size="units_sold",        # Size points by units_sold
#     hover_name="product_name",# Show product name on hover
#     title="Product Price vs. Average Rating (Interactive)",
#     labels={"price": "Price ($)", "avg_rating": "Average Customer Rating"}
# )

# To display in a Jupyter Notebook or environment that supports Plotly rendering:
# fig_scatter.show()

# To save as an HTML file:
# fig_scatter.write_html("interactive_product_scatter.html")
```
> This plot would allow hovering over points to see product names, zooming, panning, and filtering by category via the legend.

## Plotly Graph Objects (`go`) - For More Control
If Plotly Express doesn't offer enough customization, you can use `plotly.graph_objects` to build figures from scratch or modify figures created by Plotly Express.

**Example: Creating a Line Chart with Graph Objects**
```python
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Conceptual monthly sales data for two product categories
# dates = pd.to_datetime(['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01'])
# sales_electronics = 
# sales_books = 

# fig_line_go = go.Figure()

# Add traces (lines)
# fig_line_go.add_trace(go.Scatter(x=dates, y=sales_electronics, mode='lines+markers', name='Electronics Sales'))
# fig_line_go.add_trace(go.Scatter(x=dates, y=sales_books, mode='lines+markers', name='Book Sales'))

# Update layout
# fig_line_go.update_layout(
#     title_text="Monthly Sales by Category (Graph Objects)",
#     xaxis_title="Month",
#     yaxis_title="Sales Amount ($)",
#     legend_title_text="Category"
# )

# fig_line_go.show()
```

## Common Plot Types with Plotly Express

[list2tab|#Plotly Express Plots]
- Scatter & Line
    -   `px.scatter(df, x, y, color, size, symbol, hover_data, trendline, facet_row, facet_col)`
    -   `px.line(df, x, y, color, line_group, symbol, hover_data, facet_row, facet_col)`
    -   `px.scatter_3d()`, `px.line_3d()`
- Bar Charts
    -   `px.bar(df, x, y, color, orientation, barmode, hover_data, facet_row, facet_col)` (`barmode`: 'group', 'stack', 'relative')
- Histograms & Box Plots
    -   `px.histogram(df, x, y, color, marginal, cumulative, histnorm, nbins)`
    -   `px.box(df, x, y, color, notched, points, orientation)`
    -   `px.violin(df, x, y, color, box, points, orientation)`
- Pie Charts & Sunbursts
    -   `px.pie(df, names, values, color, hole)`
    -   `px.sunburst(df, path, values, color)` (for hierarchical data)
    -   `px.treemap(df, path, values, color)`
- Maps
    -   `px.scatter_geo(df, lat, lon, color, size, hover_name, projection)`
    -   `px.line_geo()`
    -   `px.choropleth(df, geojson, locations, color, featureidkey, projection)`
    -   `px.scatter_mapbox(df, lat, lon, color, size, zoom, mapbox_style)` (requires Mapbox token for some styles)
    -   `px.choropleth_mapbox()`
- Specialized
    -   `px.imshow()` (for heatmaps from 2D arrays)
    -   `px.parallel_coordinates(df, dimensions, color)`
    -   `px.scatter_matrix(df, dimensions, color)` (similar to pair plot)

## Advantages
-   **Interactivity:** Rich built-in interactivity is a major strength.
-   **Ease of Use (Plotly Express):** Quickly create complex, attractive plots.
-   **Web-Native:** Ideal for embedding in web pages and dashboards ([[Dash_Plotly|Dash]]).
-   **Wide Chart Variety:** Supports a very broad range of chart types.
-   **Good Aesthetics:** Default styles are generally modern and visually appealing.

## Considerations
-   **Performance with Very Large Datasets (in Browser):** While Plotly can handle large datasets for backend rendering or aggregation, rendering tens of thousands of interactive points directly in a web browser can sometimes become slow. Techniques like Datashader can be used with Plotly for visualizing massive datasets.
-   **Offline Use:** While plots can be saved as HTML, full interactivity in some environments (like static HTML without an internet connection for certain map tiles) might have limitations. JupyterLab/Notebook rendering is excellent.
-   **Dependencies for Exporting Static Images:** Requires `kaleido` for static image export (PNG, SVG, PDF).

Plotly and Plotly Express provide a powerful and user-friendly way to create rich, interactive visualizations in Python, bridging the gap between static scientific plotting and dynamic web-based data exploration.

---