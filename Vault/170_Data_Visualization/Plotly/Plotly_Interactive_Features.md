---
tags:
  - plotly
  - python
  - data_visualization
  - interactive_plotting
  - hover
  - zoom
  - pan
  - selection
  - buttons
  - sliders
  - concept
  - example
aliases:
  - Plotly Interactivity
  - Interactive Charts Plotly
related:
  - "[[170_Data_Visualization/Plotly/_Plotly_MOC|_Plotly_MOC]]"
  - "[[Plotly_Graph_Objects_Detailed]]"
  - "[[Plotly_Express_Quickstarts]]"
  - "[[Dash_Framework]]"
worksheet:
  - WS_DataViz_1
date_created: 2025-06-11
---
# Plotly: Interactive Features

One of the key strengths of Plotly is its ability to create **interactive visualizations** that can be explored directly in web browsers, Jupyter notebooks, or [[Dash_Framework|Dash applications]]. This interactivity enhances data exploration and understanding.

## Built-in Interactivity
Most Plotly charts come with a set of built-in interactive features by default, accessible via a **modebar** that appears on hover (usually in the top-right corner of the plot).

[list2tab|#Built-in Interactivity]
- Hover Tooltips
    -   **Functionality:** When you hover over data points, a tooltip appears displaying information about that point (e.g., x and y values, trace name, custom data).
    -   **Customization (`hovertemplate`, `hovertext`, `hoverinfo`):**
        -   In [[Plotly_Graph_Objects_Detailed|Graph Objects]], you can customize the hover content using the `hovertemplate` attribute of a trace. This allows for rich HTML formatting and inclusion of various data values.
        -   `hovertext` can provide custom text for each point.
        -   `hoverinfo` can control which parts of the default hover information are shown (e.g., 'x', 'y', 'z', 'text', 'name').
        -   [[Plotly_Express_Quickstarts|Plotly Express]] often generates sensible hover data automatically from the DataFrame columns. The `hover_data` argument in `px` functions allows adding more columns to the hover.
    -   **Example (Custom hover in Plotly Express):**
        ```python
        import plotly.express as px
        import pandas as pd
        # Conceptual e-commerce data
        df_products = pd.DataFrame({
            'product_name': ['Widget A', 'Gadget B', 'Gizmo C'],
            'price': [19.99, 49.50, 120.00],
            'units_sold': [150, 80, 30],
            'category': ['Electronics', 'Electronics', 'Home Goods']
        })

        # fig = px.scatter(df_products, x="price", y="units_sold", color="category",
        #                  size="units_sold", hover_name="product_name", # Shows product_name prominently
        #                  hover_data={'price': ':.2f', # Format price
        #                              'units_sold': True, # Show units_sold
        #                              'category': False} # Don't show category in hover if already in legend
        #                 )
        # fig.update_traces(hovertemplate="<b>%{hovertext}</b><br>Price: $%{x:.2f}<br>Units Sold: %{y}<extra></extra>")
        # # hovertext is set by hover_name, %{x} is x-value, %{y} is y-value. <extra></extra> removes trace info.
        # fig.show()
        ```
- Zoom and Pan
    -   **Functionality:** Allows users to zoom into specific regions of the plot and pan (move) the view around.
    -   **Tools:** Usually available via the modebar (magnifying glass icons for box zoom, lasso zoom; hand icon for pan). Mouse wheel can also be used for zooming.
    -   **Reset:** Double-clicking on the plot or using the "Reset axes" button in the modebar typically resets the zoom/pan.
    -   **Customization:** Axis ranges can be constrained, and default zoom behavior can be set in the `layout` (e.g., `fig.update_layout(xaxis_fixedrange=True)` to disable x-axis zoom).
- Selection Tools
    -   **Functionality:** Allows users to select data points using box select or lasso select tools from the modebar.
    -   **Use Case:** Useful in interactive environments (like Dash) to highlight data or trigger other actions based on selected points. The selected data can be accessed via callbacks in Dash.
- Download Plot
    -   **Functionality:** The modebar typically includes an option to download the current view of the plot as a static image (e.g., PNG). Requires Kaleido or Orca for server-side rendering if running in a non-browser environment.
- Autoscale
    -   **Functionality:** Rescales axes to fit all data after zooming or panning. Often triggered by a double-click or a modebar button.

## Adding Custom Interactivity with UI Elements
Plotly allows for more advanced interactivity by adding UI elements like buttons, dropdowns, and sliders directly to the figure layout. These are primarily configured using the `layout.updatemenus` and `layout.sliders` attributes. This is more common with [[Plotly_Graph_Objects_Detailed|Graph Objects]].

[list2tab|#Custom UI Elements]
- Buttons (`layout.updatemenus`)
    -   **Purpose:** Allow users to trigger changes in the plot, such as updating data, changing trace visibility, or modifying layout attributes (e.g., switching between linear and log scales).
    -   **Configuration:** Each button can be configured to execute one or more "methods" (`'update'`, `'restyle'`, `'relayout'`) with specific arguments.
    -   **Example (Button to toggle y-axis type):**
        ```python
        import plotly.graph_objects as go
        import numpy as np
        # x = np.linspace(1, 100, 100)
        # y = x**2

        # fig = go.Figure(data=[go.Scatter(x=x, y=y, mode='lines')])
        # fig.update_layout(
        #     title_text="Plot with Axis Toggle Button",
        #     updatemenus=[
        #         dict(
        #             type="buttons",
        #             direction="right",
        #             x=0.5, xanchor="center",
        #             y=1.15, yanchor="top",
        #             showactive=True,
        #             buttons=list([
        #                 dict(label="Linear Scale",
        #                      method="relayout",
        #                      args=[{"yaxis.type": "linear"}]),
        #                 dict(label="Log Scale",
        #                      method="relayout",
        #                      args=[{"yaxis.type": "log"}])
        #             ]),
        #         )
        #     ]
        # )
        # fig.show()
        ```
- Dropdowns (`layout.updatemenus`)
    -   **Purpose:** Similar to buttons, but provide a dropdown list of options, each triggering a specific update to the plot.
    -   **Configuration:** Defined within `layout.updatemenus` with `type="dropdown"`.
- Sliders (`layout.sliders`)
    -   **Purpose:** Allow users to control a parameter (e.g., time, threshold) by dragging a slider, which then updates the plot dynamically. Often used for animations or exploring data across a continuous parameter.
    -   **Configuration:** Each step in the slider can be configured to execute updates.
    -   **Example (Slider to update data in a line plot - conceptual):**
        ```python
        # This is a more complex example often used with animations or Dash.
        # fig = go.Figure()
        # # Add initial trace
        # fig.add_trace(go.Scatter(x=np.arange(10), y=np.random.rand(10)))

        # # Create frames for an animation (conceptual)
        # frames = [go.Frame(data=[go.Scatter(x=np.arange(10), y=np.random.rand(10) * (i+1))]) for i in range(3)]
        # fig.frames = frames

        # # Add slider
        # fig.update_layout(
        #     sliders=[dict(
        #         steps=[dict(method='animate', args=[[f.name], dict(mode='immediate', fromcurrent=True)], label=str(i)) for i, f in enumerate(fig.frames)],
        #         active=0,
        #         # ... other slider configurations
        #     )],
        #     # Add play button for animation
        #     updatemenus=[dict(type='buttons', buttons=[dict(label='Play', method='animate', args=[None, dict(frame=dict(duration=500, redraw=True), fromcurrent=True)])])]
        # )
        # fig.show()
        ```
- Range Sliders and Selectors (on Axes)
    -   **Purpose:** Built-in controls on axes (especially time series x-axes) that allow users to select a specific range of data to view.
    -   **Configuration:** `fig.update_xaxes(rangeslider_visible=True)` or `fig.update_xaxes(rangeselector=dict(...buttons...))`.

## Interactivity in Dash
For highly custom and complex interactive applications (e.g., dashboards where user input in one component updates multiple plots or triggers new computations), **[[Dash_Framework|Dash]]** is used. Dash builds on Plotly.js, React, and Flask, allowing you to create full-fledged web applications with Plotly charts as a core component. Interactivity in Dash is managed via **callbacks** that link UI components (sliders, dropdowns, input fields) to Python functions that update figure data or layout.

Plotly's interactive features make data exploration more dynamic and engaging, allowing users to delve deeper into the data beyond static representations.

