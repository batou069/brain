---
tags:
  - bokeh
  - python
  - data_visualization
  - interactive_plotting
  - plotting_api
  - figure
  - glyphs
  - concept
  - example
aliases:
  - bokeh.plotting API
  - Bokeh Figure
  - Bokeh Glyphs
related:
  - "[[170_Data_Visualization/Bokeh/_Bokeh_MOC|_Bokeh_MOC]]"
  - "[[Bokeh_Overview_Concepts]]"
  - "[[Bokeh_Data_Sources_CDS|ColumnDataSource]]"
  - "[[Bokeh_Interactions_Tools|Bokeh Tools]]"
  - "[[Bokeh_Styling_Theming]]"
worksheet:
  - WS_DataViz_1
date_created: 2025-06-11
---
# Bokeh: Plotting with `bokeh.plotting`

The `bokeh.plotting` interface is a mid-level API in Bokeh designed for creating common types of plots by composing **glyphs** on a **figure**. It's often the primary way users interact with Bokeh for creating visualizations.

## Creating a Figure (`figure()`)
The first step is usually to create a `figure` object, which acts as the canvas for your plot.

```python
from bokeh.plotting import figure, show
from bokeh.io import output_notebook # For Jupyter, or output_file for HTML

# output_notebook() # Call once per notebook session to enable inline plotting
# output_file("my_bokeh_plot.html") # To save to an HTML file

# Create a new plot with a title and axis labels
p = figure(
    title="Simple E-commerce Product Scatter Plot",
    x_axis_label='Price ($)',
    y_axis_label='Customer Rating (1-5)',
    width=600,  # Width of the plot in pixels
    height=400, # Height of the plot in pixels
    tools="pan,wheel_zoom,box_zoom,reset,save,hover" # Default interactive tools
)
```
-   `title`, `x_axis_label`, `y_axis_label`: Set basic textual elements.
-   `width`, `height`: Control the dimensions of the plot.
-   `tools`: A string specifying which interactive [[Bokeh_Interactions_Tools|tools]] should be available on the plot's toolbar.

## Adding Glyphs
Glyphs are the visual markers used to represent your data (circles, lines, bars, etc.). You add glyphs to a figure by calling methods on the `figure` object, like `p.circle()`, `p.line()`, etc.

These glyph methods typically accept:
-   Coordinates (`x`, `y`).
-   Data source (often a [[Bokeh_Data_Sources_CDS|ColumnDataSource]], or directly lists/arrays/Pandas Series).
-   Visual properties (e.g., `size`, `color`, `alpha`, `line_width`, `legend_label`).

**Common Glyph Methods:**

[list2tab|#Bokeh Glyphs]
- `circle()`
    -   Draws circles as markers.
    -   Key args: `x`, `y`, `size`, `color`, `alpha`, `legend_label`, `source`.
    -   **Example (Product price vs. rating):**
        ```python
        import pandas as pd
        from bokeh.models import ColumnDataSource
        # Conceptual product data
        product_data = pd.DataFrame({
            'price': [19.99, 49.50, 120.00, 25.00, 75.99],
            'rating': [4.5, 3.8, 4.8, 4.1, 3.5],
            'category': ['Electronics', 'Books', 'Electronics', 'Apparel', 'Books'],
            'units_sold': [150, 80, 30, 200, 120]
        })
        # source = ColumnDataSource(product_data)

        # p.circle(
        #     x='price', y='rating', 
        #     source=source, # Use ColumnDataSource
        #     size=10, 
        #     color='royalblue', 
        #     alpha=0.7,
        #     legend_label="Products"
        # )
        ```
- `line()`
    -   Draws lines connecting data points.
    -   Key args: `x`, `y`, `line_width`, `line_color`, `line_dash`, `legend_label`, `source`.
    -   **Example (Monthly sales trend):**
        ```python
        # months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
        # sales = 
        # p_line = figure(title="Monthly Sales", x_range=months, height=300) # x_range for categorical x-axis
        # p_line.line(
        #     x=months, y=sales, 
        #     line_width=3, 
        #     line_color="green", 
        #     legend_label="Sales Trend"
        # )
        # show(p_line)
        ```
- `vbar()` / `hbar()`
    -   Draws vertical (`vbar`) or horizontal (`hbar`) bars.
    -   Key args for `vbar`: `x` (center of bars), `top` (height of bars), `width` (of bars), `bottom` (default 0), `color`, `legend_label`, `source`.
    -   **Example (Sales per product category):**
        ```python
        # categories = ['Electronics', 'Books', 'Apparel']
        # total_sales = 
        # p_bar = figure(x_range=categories, title="Sales by Category", height=350, toolbar_location=None)
        # p_bar.vbar(
        #     x=categories, top=total_sales, 
        #     width=0.8, 
        #     color="coral",
        #     legend_label="Total Sales"
        # )
        # p_bar.xgrid.grid_line_color = None # Remove vertical grid lines
        # p_bar.y_range.start = 0 # Ensure y-axis starts at 0
        # show(p_bar)
        ```
- `rect()`
    -   Draws rectangles.
    -   Key args: `x` (center), `y` (center), `width`, `height`, `angle`, `fill_color`, `line_color`.
- `patch()` / `patches()`
    -   Draws polygons. `patch` for a single polygon, `patches` for multiple.
    -   Key args: `x`, `y` (coordinates of vertices) for `patch`. For `patches`, `xs` and `ys` (lists of lists of coordinates).
- `quad()`
    -   Draws quadrilaterals.
    -   Key args: `left`, `right`, `bottom`, `top`. Useful for heatmaps or histograms if manually binned.
- `oval()` / `ellipse()`
    -   Draws ovals/ellipses.
- `text()`
    -   Renders text at specified x, y locations.
- `image_rgba()` / `image_url()`
    -   Displays images.

## Data Sources
While you can pass Python lists or NumPy arrays directly to glyph methods, it is highly recommended to use a **[[Bokeh_Data_Sources_CDS|ColumnDataSource (CDS)]]** object, especially for interactivity or when multiple glyphs share data.
```python
from bokeh.models import ColumnDataSource

# data = {'x_values': [1, 2, 3, 4], 'y_values': [6, 7, 2, 4], 'sizes': [10, 20, 30, 15]}
# source = ColumnDataSource(data=data)

# p_cds = figure(title="Plot from ColumnDataSource")
# p_cds.scatter(x='x_values', y='y_values', size='sizes', color="navy", source=source)
# show(p_cds)
```Using a CDS allows BokehJS in the browser to efficiently access and update data, which is key for linked plots and interactive widgets.

## Combining Glyphs
You can add multiple glyph renderers to a single figure to create more complex visualizations.
```python
# p_combined = figure(title="Combined Line and Circle Glyphs")
# x_data = 
# y_data_line = 
# y_data_points = 

# p_combined.line(x_data, y_data_line, line_width=2, color="blue", legend_label="Trend")
# p_combined.circle(x_data, y_data_points, size=8, color="red", legend_label="Observations")

# p_combined.legend.location = "top_left"
# show(p_combined)
```

## Displaying Plots (`show()`)
After creating and configuring your figure and adding glyphs, you use `show(plot_object)` to render it. The output destination (Jupyter notebook, HTML file, server application) is typically configured beforehand using `output_notebook()`, `output_file()`, or within a Bokeh server application script.

The `bokeh.plotting` interface provides a balance between ease of use for common plots and the flexibility to customize by composing different glyphs with various visual properties.

---