---
tags:
  - bokeh
  - python
  - data_visualization
  - interactive_plotting
  - columndatasource
  - cds
  - data_model
  - concept
  - example
aliases:
  - ColumnDataSource
  - Bokeh CDS
  - Bokeh Data Model
related:
  - "[[170_Data_Visualization/Bokeh/_Bokeh_MOC|_Bokeh_MOC]]"
  - "[[Bokeh_Plotting_Interface]]"
  - "[[Bokeh_Layouts_Interactivity]]"
  - "[[_Pandas_MOC|Pandas DataFrame]]"
  - "[[_NumPy_MOC|NumPy ndarray]]"
worksheet:
  - WS_DataViz_1
date_created: 2025-06-11
---
# Bokeh: Data Sources (`ColumnDataSource`)

The **`ColumnDataSource` (CDS)** is the fundamental data structure for Bokeh plots. It provides the data to the glyphs that render the visual marks on your plot. While Bokeh's `bokeh.plotting` interface can often implicitly convert Python lists, NumPy arrays, or Pandas DataFrames/Series into a `ColumnDataSource`, explicitly using a CDS offers more power and flexibility, especially for creating interactive visualizations.

## Definition and Structure
A `ColumnDataSource` is essentially a dictionary-like object that maps string column names to sequences (lists, NumPy arrays, Pandas Series) of data. All columns in a CDS must have the same length.

```python
from bokeh.models import ColumnDataSource
import pandas as pd
import numpy as np

# Example 1: Creating from a Python dictionary
data_dict = {
    'x_coords': [1, 2, 3, 4, 5],
    'y_coords': [6, 7, 2, 4, 5],
    'sizes': [10, 20, 15, 25, 12],
    'colors': ['red', 'blue', 'green', 'yellow', 'purple'],
    'labels': ['A', 'B', 'C', 'D', 'E']
}
source_from_dict = ColumnDataSource(data=data_dict)
# print("CDS from dict, data for 'x_coords':", source_from_dict.data['x_coords'])

# Example 2: Creating from a Pandas DataFrame
# Conceptual e-commerce product data
product_data = pd.DataFrame({
    'product_name': ['WidgetA', 'GadgetB', 'GizmoC'],
    'price': [19.99, 49.50, 120.00],
    'rating': [4.5, 3.8, 4.8]
})
source_from_pandas = ColumnDataSource(data=product_data)
# print("\nCDS from Pandas DataFrame, data for 'price':", source_from_pandas.data['price'])
# Note: Pandas index is also included by default if not dropped.
```

## Why Use `ColumnDataSource`?

[list2tab|#CDS Advantages]
- Shared Data
    -   Multiple glyph renderers (e.g., circles and lines) can share the same `ColumnDataSource`. If the data in the CDS changes, all glyphs referencing it will update automatically. This is crucial for linked plots or complex visualizations.
- Interactivity
    -   **Selections:** When data points are selected on a plot (e.g., using `BoxSelectTool` or `TapTool`), the `selected` attribute of the `ColumnDataSource` is updated with the indices of the selected points. This can be used to trigger callbacks or highlight data in other linked plots.
    -   **Widget Interactions:** Widgets (like sliders or dropdowns) can modify data within a `ColumnDataSource` (often via [[Bokeh_Linking_Interactions|CustomJS callbacks]] or Bokeh server Python callbacks), causing plots to update dynamically.
- Efficiency with BokehJS
    -   BokehJS (the client-side JavaScript library) is optimized to work with data in this columnar format. When data changes, only the changed data needs to be sent to the browser, rather than re-transmitting the entire plot.
- Streaming Data
    -   The `stream()` method of `ColumnDataSource` allows for efficiently appending new data to a plot, useful for real-time or streaming visualizations.
- Patching Data
    -   The `patch()` method allows for updating specific parts of a data column without re-sending the entire column, useful for interactive updates to specific points.

## Using `ColumnDataSource` in Glyphs
When adding glyphs to a `bokeh.plotting.figure`, you pass the `ColumnDataSource` object to the `source` argument and refer to column names (as strings) for `x`, `y`, and other visual properties.

```python
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.io import output_file # output_notebook for Jupyter

# output_file("cds_glyph_example.html")

# Data for e-commerce product clicks vs. time on page
data = {
    'time_on_page_sec': [30, 60, 90, 120, 150, 45, 75, 100],
    'clicks_on_ads': [1, 2, 3, 2, 4, 1, 3, 2],
    'product_category': ['Electronics', 'Books', 'Electronics', 'Apparel', 'Electronics', 'Books', 'Apparel', 'Books'],
    'bubble_size': [10, 15, 20, 15, 25, 12, 22, 18] # For bubble size
}
source = ColumnDataSource(data=data)

# Create a figure
p = figure(
    title="Product Ad Clicks vs. Time on Page",
    x_axis_label="Time on Page (seconds)",
    y_axis_label="Ad Clicks",
    tools="pan,wheel_zoom,box_select,tap,hover,reset,save"
)

# Add a circle glyph using the ColumnDataSource
# Visual properties can also be mapped to columns in the CDS
from bokeh.transform import factor_cmap # For color mapping
categories = list(set(data['product_category']))
color_map = factor_cmap(field_name='product_category', palette='Category10_3', factors=categories)

p.circle(
    x='time_on_page_sec',  # Name of the column in 'source' for x-coordinates
    y='clicks_on_ads',     # Name of the column in 'source' for y-coordinates
    source=source,         # The ColumnDataSource object
    size='bubble_size',    # Map 'bubble_size' column to marker size
    color=color_map,       # Map 'product_category' to color
    legend_field='product_category', # Create legend based on this column
    alpha=0.7
)

# Configure hover tool to use data from the source
hover = p.select_one(dict(type=HoverTool))
if hover: # Check if HoverTool is present (it is by default if not specified otherwise)
    hover.tooltips = [
        ("Category", "@product_category"),
        ("Time on Page", "@time_on_page_sec s"),
        ("Ad Clicks", "@clicks_on_ads"),
    ]

p.legend.location = "top_left"
# show(p)
```

## Modifying `ColumnDataSource` Data
Data in a `ColumnDataSource` can be updated, which will automatically trigger updates in any plots using that source. This is fundamental for Bokeh server applications or `CustomJS` callbacks.

-   **Updating entire columns:**
    ```python
    # source.data = new_data_dict # Replace all data
    # source.data['x_coords'] = [5,6,7,8,9] # Replace a specific column
    ```
-   **Streaming new data (appending):**
    ```python
    # new_data_to_stream = {'x_coords': [6, 7], 'y_coords': [8, 3], ...}
    # source.stream(new_data_to_stream)
    ```
-   **Patching existing data (updating specific indices):**
    ```python
    # Patches to update the first point's y_coord and color
    # patches_to_apply = {
    #     'y_coords': [(0, 10)],  # (index, new_value)
    #     'colors': [(0, 'black')] # (index, new_value)
    # }
    # source.patch(patches_to_apply)
    ```
    These modifications, when done in the context of a Bokeh server app or `CustomJS`, will reflect live in the browser.

Using `ColumnDataSource` is a best practice in Bokeh for managing data, especially when building interactive visualizations or applications where data needs to be shared or updated dynamically.

---