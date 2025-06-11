---
tags:
  - bokeh
  - python
  - data_visualization
  - interactive_plotting
  - layouts
  - widgets
  - tools
  - interactions
  - concept
  - example
aliases:
  - Bokeh Layouts
  - Bokeh Interactivity
  - Bokeh Widgets
  - Bokeh Tools
  - Bokeh Callbacks
related:
  - "[[170_Data_Visualization/Bokeh/_Bokeh_MOC|_Bokeh_MOC]]"
  - "[[Bokeh_Plotting_Interface]]"
  - "[[Bokeh_Data_Sources_CDS|ColumnDataSource]]"
  - "[[Bokeh_Embedding_Server_Apps]]"
worksheet:
  - WS_DataViz_1
date_created: 2025-06-11
---
# Bokeh: Layouts and Interactivity

Bokeh excels at creating interactive visualizations. This interactivity comes from built-in [[Bokeh_Interactions_Tools|tools]], the ability to link plots, and the integration of [[Bokeh_Widgets|widgets]] that can control plot properties or data. Bokeh also allows for arranging multiple plots and widgets into structured **layouts**.

## Layouts (`bokeh.layouts`)
Bokeh provides functions to arrange multiple plots and widgets together:
-   **`row(*children, **kwargs)`:** Arranges plots/widgets horizontally.
-   **`column(*children, **kwargs)`:** Arranges plots/widgets vertically.
-   **`gridplot(children, ncols=None, nrows=None, toolbar_location='above', sizing_mode=None, ...)`:** Arranges plots in a grid. `children` is a list of lists representing the grid structure.

**Example: Arranging two plots in a column**
```python
from bokeh.plotting import figure, show
from bokeh.layouts import column
from bokeh.io import output_file # output_notebook for Jupyter

# output_file("layout_example.html")

# Create two simple plots
# x_vals = 
# p1 = figure(width=400, height=300, title="Sine Wave")
# p1.line(x_vals, np.sin(x_vals), color="blue", line_width=2)

# p2 = figure(width=400, height=300, title="Cosine Wave", x_range=p1.x_range) # Link x-axes
# p2.line(x_vals, np.cos(x_vals), color="red", line_width=2)

# Arrange them in a column
# layout = column(p1, p2)
# show(layout)
```

## [[Bokeh_Interactions_Tools|Interactive Tools]]
Figures created with `bokeh.plotting.figure()` come with a default set of tools (pan, zoom, save, reset). You can customize this toolbar.
-   **Specifying Tools:**
    ```python
    # p = figure(tools="pan,wheel_zoom,box_select,lasso_select,tap,hover,save,reset")
    ```
-   **Common Tools:**
    -   `PanTool` (`"pan"`): Allows dragging the plot view.
    -   `WheelZoomTool` (`"wheel_zoom"`): Zooms with the mouse wheel.
    -   `BoxZoomTool` (`"box_zoom"`): Allows drawing a rectangle to zoom into a region.
    -   `LassoSelectTool` (`"lasso_select"`), `BoxSelectTool` (`"box_select"`): Select data points.
    -   `TapTool` (`"tap"`): Select single points on click.
    -   `HoverTool` (`"hover"`): Displays tooltips when hovering over data points.
    -   `SaveTool` (`"save"`): Allows saving the plot as a PNG.
    -   `ResetTool` (`"reset"`): Resets the plot to its initial view.
-   **Configuring HoverTool:**
    ```python
    from bokeh.models import HoverTool
    # Assume 'source' is a ColumnDataSource with columns 'product_name', 'price', 'rating'
    # hover = HoverTool(tooltips=[
    #     ("Product", "@product_name"),
    #     ("Price", "$@price{0,0.00}"), # Format price
    #     ("Rating", "@rating{0.0}/5"),
    #     ("(X,Y)", "($x, $y)"), # Special variables for coordinates
    # ])
    # p_hover = figure(tools=[hover, "pan", "wheel_zoom", "reset"])
    # p_hover.circle(x='price', y='rating', source=source, size=10)
    # show(p_hover)
    ```
    -   `@column_name` refers to data from the `ColumnDataSource`.
    -   `$x`, `$y` refer to screen coordinates.
    -   Formatting options like `{0,0.00}` can be used.

## [[Bokeh_Widgets|Widgets (`bokeh.models.widgets`)]]
Widgets are interactive controls like sliders, buttons, dropdowns, etc., that can be added to a Bokeh layout. They allow users to manipulate aspects of the plot or trigger Python callbacks (if using Bokeh server).

-   **Common Widgets:**
    -   `Button`
    -   `CheckboxGroup`, `RadioGroup`, `RadioButtonGroup`
    -   `Dropdown`, `Select` (for single selection)
    -   `MultiSelect` (for multiple selections)
    -   `Slider`, `RangeSlider`, `DateRangeSlider`
    -   `TextInput`, `TextAreaInput`
    -   `DataTable` (for displaying tabular data)
-   **Example (Conceptual - interactivity often requires JavaScript callbacks or Bokeh server):**
    ```python
    from bokeh.models.widgets import Slider, Button
    from bokeh.layouts import column
    # Assume p is an existing plot
    # slider = Slider(start=0, end=10, value=1, step=0.1, title="Multiplier")
    # button = Button(label="Apply", button_type="success")

    # Layout with plot and widgets
    # layout_with_widgets = column(slider, button, p)
    # show(layout_with_widgets)
    # To make these widgets *do* something to the plot, you'd typically use
    # CustomJS callbacks (browser-side) or a Bokeh server application (Python-side).
    ```

## [[Bokeh_Linking_Interactions|Linking Plots and Custom Interactions]]
Bokeh allows for more complex interactions, such as linking panning/zooming between plots, or having selections in one plot affect another.

[list2tab|#Linking & Custom Interactions]
- Linked Panning and Zooming
    -   If plots share an `x_range` or `y_range` object, panning/zooming in one plot will automatically update the others.
    -   **Example:** In the layout example above, `p2 = figure(..., x_range=p1.x_range)` links their x-axes.
- CustomJS Callbacks (`bokeh.models.CustomJS`)
    -   **Purpose:** Allows you to write small snippets of JavaScript code that execute in the browser in response to events (e.g., widget value change, data selection, tap on plot).
    -   **Use Case:** For client-side interactions that don't require Python server computation (e.g., highlighting selected points, filtering data visible in a plot based on a widget, updating plot attributes directly in the browser).
    -   **Example (Slider updating a glyph's alpha - conceptual):**
        ```python
        from bokeh.models import CustomJS, Slider, ColumnDataSource
        from bokeh.plotting import figure, show
        from bokeh.layouts import column

        # x = 
        # y = 
        # source = ColumnDataSource(data=dict(x=x, y=y))
        # plot = figure()
        # circle_renderer = plot.circle(x='x', y='y', source=source, size=10, alpha=0.5)
        # slider = Slider(start=0.1, end=1.0, value=0.5, step=0.05, title="Alpha")

        # JavaScript callback
        # callback = CustomJS(args=dict(circle=circle_renderer, slider=slider), code="""
        #     // circle here refers to the glyph renderer, not the glyph itself
        #     circle.glyph.fill_alpha = slider.value;
        #     circle.glyph.line_alpha = slider.value;
        #     // For CDS changes, you'd do: source.change.emit(); after modifying source.data
        # """)
        # slider.js_on_change('value', callback) # Execute JS when slider value changes

        # layout = column(slider, plot)
        # show(layout)
        ```
- Bokeh Server Applications (Python Callbacks)
    -   **Purpose:** For interactions that require Python computation (e.g., running a simulation, querying a database, complex data processing based on user input).
    -   **How it Works:** You write a Python script that defines the Bokeh document. This script is run with `bokeh serve myapp.py`. The Bokeh server keeps Python objects alive, and Python callback functions can be registered to widget events or plot interactions. These Python functions can modify Bokeh models, and the changes are automatically synchronized to the browser.
    -   See [[Bokeh_Embedding_Server_Apps]].

Bokeh's rich interactivity features, from built-in tools to custom JavaScript and Python-backed server applications, make it a powerful choice for creating dynamic and exploratory data visualizations.

---