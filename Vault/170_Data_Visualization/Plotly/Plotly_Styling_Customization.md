---
tags:
  - plotly
  - python
  - data_visualization
  - interactive_plotting
  - styling
  - customization
  - themes
  - templates
  - colors
  - fonts
  - concept
  - example
aliases:
  - Plotly Chart Styling
  - Customizing Plotly Plots
  - Plotly Templates
related:
  - "[[170_Data_Visualization/Plotly/_Plotly_MOC|_Plotly_MOC]]"
  - "[[Plotly_Graph_Objects_Detailed]]"
  - "[[Plotly_Express_Quickstarts]]"
worksheet:
  - WS_DataViz_1
date_created: 2025-06-11
---
# Plotly: Styling and Customization

Plotly offers extensive options for styling and customizing the appearance of your visualizations. This can be done by modifying attributes of the **traces** (data elements) and the **layout** (non-data elements like titles, axes, legends).

## Key Areas of Customization

[list2tab|#Styling Areas]
- Templates
    -   **Purpose:** Plotly includes several built-in themes or "templates" that define a consistent look and feel for figures (colors, fonts, backgrounds, etc.). You can also create custom templates.
    -   **Usage:**
        -   Apply globally: `import plotly.io as pio; pio.templates.default = "plotly_white"`
        -   Apply per figure in [[Plotly_Express_Quickstarts|Plotly Express]]: `fig = px.scatter(..., template="plotly_dark")`
        -   Apply per figure in [[Plotly_Graph_Objects_Detailed|Graph Objects]]: `fig = go.Figure(layout=go.Layout(template=go.layout.Template(data=..., layout=...)))` or `fig.update_layout(template=...)`.
    -   **Common Built-in Templates:** `'plotly'`, `'plotly_white'`, `'plotly_dark'`, `'ggplot2'`, `'seaborn'`, `'simple_white'`, `'none'`.
    -   **Example:**
        ```python
        import plotly.express as px
        import pandas as pd
        # df_example = px.data.iris() # Load sample iris dataset

        # fig_styled = px.scatter(df_example, x="sepal_width", y="sepal_length", color="species",
        #                         template="plotly_dark", # Apply a dark theme
        #                         title="Iris Dataset with 'plotly_dark' Template")
        # fig_styled.show()
        ```
- Colors
    -   **Purpose:** Control colors of markers, lines, fills, backgrounds, text, etc.
    -   **Usage:**
        -   **Traces:**
            -   `marker_color` (for scatter, bar, pie, etc.)
            -   `line_color` (for scatter lines, line plots)
            -   Can be a single color name (e.g., 'red', 'blue'), hex code (e.g., '#FF0000'), RGB/RGBA string (e.g., 'rgb(255,0,0)'), or an array/list of colors to map to data points.
        -   **Color Scales/Sequences (for `color` argument in Plotly Express or `marker_colorscale` in `go` traces):**
            -   Plotly Express: `color_continuous_scale` (for numerical color mapping), `color_discrete_map` or `color_discrete_sequence` (for categorical color mapping).
            -   `plotly.colors` module provides named color scales and sequences (e.g., `px.colors.qualitative.Plotly`, `px.colors.sequential.Viridis`).
        -   **Layout:** `paper_bgcolor` (figure background), `plot_bgcolor` (plotting area background).
    -   **Example:**
        ```python
        import plotly.express as px
        import pandas as pd
        # df_tips = px.data.tips()

        # fig_colors = px.bar(df_tips, x="day", y="total_bill", color="sex",
        #                     title="Total Bill by Day and Sex",
        #                     color_discrete_map={"Male": "blue", "Female": "pink"}, # Custom colors for 'sex'
        #                     template="simple_white"
        #                    )
        # fig_colors.update_layout(plot_bgcolor="lightyellow")
        # fig_colors.show()
        ```
- Fonts
    -   **Purpose:** Customize font family, size, and color for titles, axis labels, tick labels, legends, annotations.
    -   **Usage (in `update_layout` or specific components):**
        -   `font=dict(family="Arial", size=12, color="black")` (global font)
        -   `title_font_family`, `title_font_size`, `title_font_color`
        -   `xaxis_title_font=dict(...)`, `yaxis_tickfont=dict(...)`
    -   **Example:**
        ```python
        # fig.update_layout(
        #     title_text="Customized Title Font",
        #     title_font=dict(family="Courier New, monospace", size=24, color="darkred"),
        #     xaxis=dict(title_text="X Axis with Custom Font", title_font_size=16),
        #     yaxis=dict(tickfont=dict(family="Georgia, serif", size=10, color="green"))
        # )
        ```
- Titles and Labels
    -   **Purpose:** Provide context and describe elements of the plot.
    -   **Usage:**
        -   `fig.update_layout(title_text="My Figure Title", title_x=0.5)`
        -   `fig.update_xaxes(title_text="X Axis Label")`
        -   `fig.update_yaxes(title_text="Y Axis Label")`
        -   Plotly Express: `title`, `labels={'col_name': 'New Label'}` arguments.
- Legends
    -   **Purpose:** Explain the mapping of visual properties (color, symbol, size) to data categories or series.
    -   **Usage (`fig.update_layout(legend=dict(...))`):**
        -   `title_text`: Legend title.
        -   `orientation`: `'v'` (vertical) or `'h'` (horizontal).
        -   `x`, `y`, `xanchor`, `yanchor`: Position of the legend.
        -   `bgcolor`, `bordercolor`, `borderwidth`.
        -   `traceorder`: `'normal'`, `'reversed'`, `'grouped'`.
- Axes Customization
    -   **Purpose:** Control the appearance and behavior of x, y (and z) axes.
    -   **Usage (`fig.update_xaxes(...)`, `fig.update_yaxes(...)`):**
        -   `visible`: Show/hide axis.
        -   `range`: Set axis range `[,]`.
        -   `type`: `'-'`, `'linear'`, `'log'`, `'date'`, `'category'`.
        -   `showgrid`, `gridwidth`, `gridcolor`.
        -   `showline`, `linewidth`, `linecolor`.
        -   `ticks`, `tickmode`, `tickvals`, `ticktext`, `tickangle`, `tickfont`.
        -   `zeroline`, `zerolinewidth`, `zerolinecolor`.
- Annotations and Shapes
    -   **Purpose:** Add textual annotations or geometric shapes (lines, rectangles, circles) to highlight specific features or regions.
    -   **Usage:**
        -   `fig.add_annotation(x=..., y=..., text="Note", showarrow=True, arrowhead=1, ...)`
        -   `fig.add_shape(type="line", x0=.., y0=.., x1=.., y1=.., line=dict(color="Red", width=2, dash="dash"), ...)`
        -   `fig.add_vline(x=value, ...)` , `fig.add_hline(y=value, ...)`
- Size and Margins
    -   **Purpose:** Control overall figure dimensions and spacing.
    -   **Usage (`fig.update_layout(...)`):**
        -   `width`, `height`: Figure dimensions in pixels.
        -   `margin=dict(l=50, r=50, t=100, b=50)`: Left, right, top, bottom margins.
        -   `autosize=False` (if setting width/height).

## Updating Traces (`fig.update_traces()`)
This method allows modifying properties of already existing traces in a figure.
-   **`patch`:** A dictionary of attributes to update (e.g., `marker_color='red'`, `line_width=3`).
-   **`selector`:** A dictionary or function to select which traces to apply the update to (e.g., `selector={'name': 'Product A'}`). If `None`, applies to all traces.
-   **`row`, `col`:** To target traces in specific subplots.

**Example:**
```python
import plotly.graph_objects as go
# Assume fig is an existing go.Figure with multiple scatter traces
# fig = go.Figure()
# fig.add_trace(go.Scatter(y=, name="Alpha"))
# fig.add_trace(go.Scatter(y=, name="Beta"))

# Update all scatter traces to have larger markers
# fig.update_traces(marker=dict(size=12, line=dict(width=2, color='DarkSlateGrey')))

# Update only the 'Beta' trace to have a dashed line
# fig.update_traces(selector=dict(name="Beta"), line=dict(dash='dash'))
# fig.show()
```

Plotly's system of Figure, Traces, and Layout, combined with the `update_*` methods, provides a deeply customizable environment for creating tailored visualizations. Plotly Express simplifies many common styling choices, but understanding Graph Objects allows for ultimate control.

---