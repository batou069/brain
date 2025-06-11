---
tags:
  - bokeh
  - python
  - data_visualization
  - interactive_plotting
  - styling
  - theming
  - customization
  - colors
  - fonts
  - concept
  - example
aliases:
  - Bokeh Plot Styling
  - Bokeh Themes
  - Customizing Bokeh Plots
related:
  - "[[170_Data_Visualization/Bokeh/_Bokeh_MOC|_Bokeh_MOC]]"
  - "[[Bokeh_Plotting_Interface]]"
  - "[[Bokeh_Overview_Concepts]]"
worksheet:
  - WS_DataViz_1
date_created: 2025-06-11
---
# Bokeh: Styling and Theming

Bokeh provides extensive options for customizing the visual appearance of plots, from individual glyph properties to overall plot themes. Styling can be applied at different levels: on glyphs, axes, titles, legends, or globally using themes.

## Styling Individual Glyphs
When adding glyphs using methods like `p.circle()`, `p.line()`, etc., you can specify various visual properties as arguments. These properties can be set to fixed values or mapped to data columns in a [[Bokeh_Data_Sources_CDS|ColumnDataSource]].

**Common Visual Properties for Glyphs:**
-   **Color:**
    -   `color`: Fill color for area glyphs (patches, bars, circles if no `fill_color`).
    -   `fill_color`: Fill color for markers, bars, patches.
    -   `line_color`: Color of lines or outlines of markers/patches.
    -   Can be named colors (e.g., 'blue', 'red'), hex codes (e.g., '#FF0000'), RGB/RGBA tuples.
-   **Alpha (Transparency):**
    -   `alpha`: Overall transparency (0.0 to 1.0).
    -   `fill_alpha`: Transparency of the fill.
    -   `line_alpha`: Transparency of the line.
-   **Line Properties (for lines or outlines):**
    -   `line_width`: Thickness of the line.
    -   `line_dash`: Dash pattern (e.g., 'solid', 'dashed', 'dotted', or a list like `[4, 4]`).
    -   `line_cap`: `{'butt', 'round', 'square'}`.
    -   `line_join`: `{'miter', 'round', 'bevel'}`.
-   **Marker Properties (for `circle`, `scatter`, etc.):**
    -   `size`: Size of the marker (in screen units or data units depending on glyph).
    -   `marker` (for `scatter`): Type of marker (e.g., 'circle', 'square', 'triangle').
-   **Text Properties (for `text` glyph or labels/titles):**
    -   `text_font`: Font name (e.g., "arial", "helvetica").
    -   `text_font_size`: e.g., "12pt", "1.5em".
    -   `text_font_style`: `'normal'`, `'italic'`, `'bold'`.
    -   `text_color`.
    -   `text_alpha`.
    -   `text_align`: `'left'`, `'right'`, `'center'`.
    -   `text_baseline`: `'top'`, `'middle'`, `'bottom'`.

**Example: Styling a scatter plot glyph**
```python
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.io import output_file

# output_file("styled_scatter.html")
# data = {'x':, 'y':, 'sizes':, 'colors': ['red','blue','green','yellow','black']}
# source = ColumnDataSource(data)

# p = figure(title="Styled Scatter Plot")
# p.scatter(
#     x='x', y='y', source=source,
#     legend_label="Data Points",
#     size='sizes',           # Map size to 'sizes' column
#     fill_color='colors',    # Map fill_color to 'colors' column
#     fill_alpha=0.6,
#     line_color="navy",      # Outline color for all markers
#     line_width=2,
#     marker="diamond"        # Change marker type
# )
# p.legend.location = "top_left"
# show(p)
```

## Styling Plot Attributes (Axes, Titles, Grid, Legend)
Plot-level attributes are typically modified on the `figure` object (`p`) after its creation.

[list2tab|#Plot Attribute Styling]
- Titles and Labels
    -   `p.title.text = "New Title"`
    -   `p.title.text_font_size = "16pt"`
    -   `p.xaxis.axis_label = "X-Axis Label"`
    -   `p.yaxis.axis_label_text_color = "blue"`
- Axes Lines and Ticks
    -   `p.xaxis.axis_line_width = 3`
    -   `p.yaxis.axis_line_color = "green"`
    -   `p.xaxis.major_label_orientation = "vertical"` (or radians)
    -   `p.yaxis.major_tick_line_color = "orange"`
    -   `p.xaxis.minor_tick_in = -3` (negative for outside)
    -   `p.xaxis.minor_tick_out = 6`
- Grid Lines
    -   `p.xgrid.grid_line_color = "lightgray"`
    -   `p.ygrid.grid_line_dash = [4, 4]` # Dashed grid
    -   `p.xgrid.grid_line_alpha = 0.5`
    -   `p.grid.grid_line_color = None` # Turn off all grid lines
- Background Colors
    -   `p.background_fill_color = "beige"` (area outside plot frame)
    -   `p.border_fill_color = "whitesmoke"` (area inside plot frame but outside grid)
    -   `p.outline_line_color = "black"` (plot frame outline)
- Legend
    -   `p.legend.location = "top_right"` (`'top_left'`, `'bottom_right'`, etc.)
    -   `p.legend.title = "My Legend"`
    -   `p.legend.background_fill_alpha = 0.5`
    -   `p.legend.border_line_color = "black"`
    -   `p.legend.label_text_font_size = "10pt"`
    -   `p.legend.click_policy = "hide"` (`'mute'` to dim, `'hide'` to hide trace on click)

**Example: Customizing plot attributes**
```python
from bokeh.plotting import figure, show
from bokeh.io import output_file

# output_file("custom_plot_attrs.html")
# x = 
# y = 

# p = figure(width=500, height=400, title="Highly Customized Plot")
# p.line(x, y, line_width=3, color="purple", legend_label="Trend")

# Title styling
# p.title.text_font_size = "20pt"
# p.title.align = "center"
# p.title.text_color = "darkblue"

# X-axis styling
# p.xaxis.axis_label = "Time (seconds)"
# p.xaxis.axis_label_text_font_style = "italic"
# p.xaxis.major_label_orientation = 0.8 # Radians for rotation

# Y-axis styling
# p.yaxis.axis_label = "Value"
# p.yaxis.minor_tick_line_color = "red"
# p.yaxis.major_tick_in = 10

# Grid styling
# p.xgrid.grid_line_dash =
# p.ygrid.grid_line_alpha = 0.3

# Background
# p.background_fill_color = "#F0F0F0" # Light gray
# p.border_fill_color = None # Transparent border fill

# Legend
# p.legend.location = "bottom_right"
# p.legend.background_fill_color = "ivory"
# p.legend.border_line_color = "gray"

# show(p)
```

## Using Themes
Bokeh provides a way to apply a consistent set of styling attributes across multiple plots using **Themes**. A theme is a JSON file or a Python dictionary that defines default values for various Bokeh model properties.

-   **Built-in Themes:** Bokeh comes with a few pre-defined themes:
    -   `caliber`
    -   `dark_minimal`
    -   `light_minimal`
    -   `night_sky`
    -   `contrast`
-   **Applying a Theme:**
    ```python
    from bokeh.themes import DARK_MINIMAL # Or other built-in themes
    from bokeh.io import curdoc # For setting theme on current document

    # curdoc().theme = DARK_MINIMAL # Apply globally to current document/session

    # Or, apply when creating a figure (less common for global theme)
    # p = figure(..., theme=DARK_MINIMAL)
    ```
    When running a Bokeh server application, themes can be applied using `curdoc().theme = Theme(json=yaml.safe_load(Path("mytheme.yaml").read_text()))` if you have a custom theme YAML file.

-   **Custom Themes:** You can create your own theme by defining a JSON or YAML file specifying property values for different Bokeh models.

Themes are powerful for maintaining a consistent visual style across a project or an entire application.

By combining direct property modifications on glyphs and plot objects with the use of themes, you can achieve a high degree of control over the appearance of your Bokeh visualizations.

---