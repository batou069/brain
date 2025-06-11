---
tags:
  - plotly
  - python
  - data_visualization
  - interactive_plotting
  - architecture
  - figure
  - trace
  - layout
  - concept
aliases:
  - Plotly Architecture
  - Plotly Figure Object
  - Plotly Traces
  - Plotly Layout
related:
  - "[[170_Data_Visualization/Plotly/_Plotly_MOC|_Plotly_MOC]]"
  - "[[Plotly_Express_Quickstarts]]"
  - "[[Plotly_Graph_Objects_Detailed]]"
worksheet:
  - WS_DataViz_1
date_created: 2025-06-11
---
# Plotly: Overview and Architecture (Figures, Traces, Layout)

Plotly is a versatile Python graphing library that generates interactive, publication-quality visualizations. Understanding its core architecture, centered around **Figures**, **Traces**, and **Layouts**, is key to effectively using both its high-level ([[Plotly_Express_Quickstarts|Plotly Express]]) and low-level ([[Plotly_Graph_Objects_Detailed|Graph Objects]]) APIs.

## Core Components of a Plotly Figure

A Plotly visualization is represented by a **Figure object**. This Figure object is essentially a dictionary-like structure containing two main keys:
1.  **`data` (Traces):** A list of "traces." Each trace represents a collection of data points and their visual representation (e.g., a scatter plot, a line plot, a bar chart).
2.  **`layout`:** An object (dictionary-like) that defines the appearance and non-data-related attributes of the figure (e.g., title, axis labels, colors, fonts, annotations, shapes, sliders, buttons).

[d2]
```d2
direction: down
shape: sequence_diagram

Figure: "Plotly Figure (go.Figure)" {
  shape: package
  style.fill: "#E0F2F7"
  
  DataList: "`data`: List of Traces" {
    shape: process
    style.fill: "#FFF9C4"
    Trace1: "Trace 1 (e.g., go.Scatter)"
    Trace2: "Trace 2 (e.g., go.Bar)"
    TraceN: "Trace N ..."
  }

  LayoutObj: "`layout`: Layout Object" {
    shape: process
    style.fill: "#C8E6C9"
    Title: "Title"
    XAxis: "X-Axis Properties"
    YAxis: "Y-Axis Properties"
    Legend: "Legend Properties"
    Annotations: "Annotations"
    Shapes: "Shapes"
    UIControls: "Buttons, Sliders"
  }
}

Figure.DataList -> Figure.Trace1
Figure.DataList -> Figure.Trace2
Figure.DataList -> Figure.TraceN

style Figure { icon: "📊" }
style DataList { icon: "📦" }
style LayoutObj { icon: "⚙️" }
```

[list2tab|#Figure Components]
- Figure (`plotly.graph_objects.Figure`)
    -   **Definition:** The top-level object representing the entire chart or visualization.
    -   **Contains:**
        -   A list of one or more **traces** (the `data` attribute).
        -   A **layout** object that controls the appearance of the figure.
    -   When you use [[Plotly_Express_Quickstarts|Plotly Express]] (e.g., `px.scatter(...)`), it conveniently creates and returns a `go.Figure` object configured with appropriate traces and layout.
    -   With [[Plotly_Graph_Objects_Detailed|Graph Objects]], you typically create a `go.Figure` explicitly and then add traces and update its layout.
- Traces (Elements of the `data` list)
    -   **Definition:** A trace is a dictionary-like object that defines a single series of data and its visual representation. Each trace corresponds to a specific chart type.
    -   **Examples of Trace Types (`plotly.graph_objects`):**
        -   `go.Scatter`: For line plots and scatter plots.
        -   `go.Bar`: For bar charts.
        -   `go.Pie`: For pie charts.
        -   `go.Histogram`: For histograms.
        -   `go.Box`: For box plots.
        -   `go.Heatmap`: For heatmaps.
        -   `go.Scatter3d`, `go.Surface`: For 3D plots.
        -   `go.Choropleth`, `go.Scattergeo`, `go.Scattermapbox`: For maps.
    -   **Key Attributes of a Trace:**
        -   `type`: Specifies the chart type (e.g., 'scatter', 'bar').
        -   `x`, `y`, `z`: Data coordinates.
        -   `mode`: For scatter plots (e.g., 'markers', 'lines', 'lines+markers').
        -   `marker`: Dictionary for styling markers (color, size, symbol).
        -   `line`: Dictionary for styling lines (color, width, dash).
        -   `name`: Name of the trace (appears in legend).
        -   Many other type-specific attributes.
    -   A single Figure can contain multiple traces, allowing for overlaying different chart types or data series.
- Layout (`layout` attribute of Figure)
    -   **Definition:** A dictionary-like object that controls the overall appearance and non-data elements of the figure.
    -   **Key Attributes of Layout:**
        -   `title`: Figure title.
        -   `xaxis`, `yaxis`, `zaxis`: Objects for configuring axes (title, range, ticks, gridlines). For multiple subplots, these can be `xaxis1`, `xaxis2`, etc.
        -   `legend`: Configuration for the legend.
        -   `width`, `height`: Dimensions of the figure.
        -   `margin`: Margins around the plotting area.
        -   `paper_bgcolor`, `plot_bgcolor`: Background colors.
        -   `font`: Default font settings.
        -   `annotations`: List of text annotations.
        -   `shapes`: List of geometric shapes to draw on the plot.
        -   `sliders`, `updatemenus` (buttons): For adding UI controls for interactivity.
        -   `template`: Predefined styling template (e.g., 'plotly_white', 'ggplot2', 'seaborn').

## How Plotly Renders
1.  The `go.Figure` object (containing `data` and `layout`) is essentially a JSON-serializable structure.
2.  This structure is passed to the **Plotly.js** JavaScript library.
3.  Plotly.js renders the figure as an interactive HTML/SVG graphic in a web browser, Jupyter notebook output cell, or within a Dash application.
4.  For static image export, tools like Kaleido (or previously Orca) are used to render the Plotly.js output to an image format (PNG, JPG, SVG, PDF).

## Using Plotly Express vs. Graph Objects
-   **[[Plotly_Express_Quickstarts|Plotly Express (`px`)]]:**
    -   Creates a fully populated `go.Figure` object with a single function call.
    -   Excellent for rapid exploration and creating common chart types quickly, especially from Pandas DataFrames.
    -   Example: `fig = px.scatter(data_frame=df, x="col_x", y="col_y", color="col_category")`
-   **[[Plotly_Graph_Objects_Detailed|Graph Objects (`go`)]]:**
    -   Provides fine-grained control. You build the figure by creating `go.Figure()`, then adding traces (`fig.add_trace(go.Scatter(...))`), and updating the layout (`fig.update_layout(...)`).
    -   Necessary for highly customized plots, plots with multiple subplot types, or when more complex interactions are needed.

Understanding this Figure-Trace-Layout architecture helps in customizing plots created by Plotly Express (as they are just `go.Figure` objects) and in building complex visualizations from scratch using Graph Objects.

---