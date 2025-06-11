---
tags:
  - bokeh
  - python
  - data_visualization
  - interactive_plotting
  - architecture
  - figure
  - glyph
  - model
  - document
  - server
  - concept
aliases:
  - Bokeh Core Concepts
  - Bokeh Architecture
related:
  - "[[170_Data_Visualization/Bokeh/_Bokeh_MOC|_Bokeh_MOC]]"
  - "[[Bokeh_Plotting_Interface]]"
  - "[[Bokeh_Data_Sources_CDS]]"
worksheet:
  - WS_DataViz_1
date_created: 2025-06-11
---
# Bokeh: Overview and Core Concepts

**Bokeh** is a Python library designed for creating interactive visualizations targeted at modern web browsers. It empowers data scientists and developers to generate rich, interactive plots, dashboards, and data applications without needing to write JavaScript.

## Core Philosophy
-   **Interactivity:** Bokeh's primary goal is to enable easy creation of interactive graphics. Tools for panning, zooming, selecting data, and hover information are central.
-   **Web-Native:** Output is HTML and JavaScript (using BokehJS, its client-side runtime library), making visualizations easily embeddable in web pages or shareable as standalone HTML files.
-   **Flexibility:** Offers multiple levels of API for varying degrees of control, from quick plotting with `bokeh.plotting` to detailed model manipulation with `bokeh.models`.
-   **Server Capabilities:** Can be used to build full-fledged interactive data applications with Python-backed interactions using the Bokeh server.

## Fundamental Concepts

[list2tab|#Bokeh Concepts]
- Figure (`bokeh.plotting.figure`)
    -   **Definition:** The central object for creating a plot. It's the canvas onto which you add visual elements (glyphs).
    -   **Creation:** Typically `p = figure(...)` from `bokeh.plotting`.
    -   **Contains:** Axes, grids, tools, and glyph renderers.
- Glyphs
    -   **Definition:** The basic visual building blocks of Bokeh plots. Glyphs are vectorized graphical shapes or markers that represent data.
    -   **Examples:** Circles (`circle()`), lines (`line()`), rectangles (`rect()`), bars (`vbar()`, `hbar()`), patches (`patch()`), text (`text()`).
    -   **Adding to Figure:** Glyphs are added to a figure using methods like `p.circle(x_values, y_values, ...)`, `p.line(x_values, y_values, ...)`.
    -   **Properties:** Glyphs have visual properties (e.g., `size`, `color`, `alpha`, `line_width`) that can be set to fixed values or mapped to data columns from a [[Bokeh_Data_Sources_CDS|ColumnDataSource]].
- Models (`bokeh.model.Model`)
    -   **Definition:** The low-level building blocks of Bokeh. Everything in a Bokeh plot, including figures, glyphs, axes, tools, and even data sources, is a `Model` subclass.
    -   **Structure:** Models have properties (attributes) that can be set to define their appearance and behavior.
    -   **Serialization:** Bokeh plots are ultimately serialized as a collection of these Model objects (as JSON), which BokehJS then uses to render the visualization in the browser. Users of `bokeh.plotting` interact with models indirectly, while users of `bokeh.models` manipulate them directly.
- Document (`bokeh.document.Document`)
    -   **Definition:** A container for all Bokeh content (figures, widgets, layouts) that makes up a single visual display or application.
    -   **Role:** When creating standalone HTML files or Bokeh server applications, you are essentially working with one or more Documents.
    -   For simple plots using `bokeh.plotting.show()`, a Document is often created implicitly.
- [[Bokeh_Data_Sources_CDS|ColumnDataSource (`bokeh.models.ColumnDataSource`)]]
    -   **Definition:** The primary way to supply data to Bokeh plots. It's a dictionary-like object that maps string column names to sequences (lists, NumPy arrays, Pandas Series) of data.
    -   **Importance:**
        -   Enables sharing data between multiple glyphs or plots.
        -   Crucial for interactive features where selections or changes in one plot can update another, or where widgets control data views.
        -   Efficiently transfers data to the browser.
    -   When you pass Python lists or Pandas DataFrames directly to glyph methods in `bokeh.plotting`, Bokeh often converts them into a `ColumnDataSource` internally.
- [[Bokeh_Interactions_Tools|Tools]]
    -   **Definition:** Interactive controls that can be added to a plot, usually appearing as a toolbar.
    -   **Examples:** `PanTool`, `WheelZoomTool`, `BoxZoomTool`, `HoverTool`, `TapTool`, `SaveTool`, `ResetTool`.
    -   **Configuration:** Added to a `figure` via the `tools` argument or `fig.add_tools()`.
- [[Bokeh_Layouts_Interactivity|Layouts]]
    -   **Definition:** Functions and objects for arranging multiple plots and [[Bokeh_Widgets|widgets]] together.
    -   **Examples:** `row()`, `column()`, `gridplot()` from `bokeh.layouts`.
- Bokeh Server (`bokeh serve myapp.py`)
    -   **Definition:** A Python server that allows for building more complex interactive applications.
    -   **Functionality:** Python callbacks can be triggered by UI events (widget changes, plot interactions), allowing for server-side computation and dynamic updates to the plot in the browser. This enables building sophisticated data applications.

## Basic Workflow with `bokeh.plotting`
1.  **Import necessary functions:** `from bokeh.plotting import figure, show` and `from bokeh.io import output_notebook, output_file` (for specifying output).
2.  **Prepare Data:** Often as Python lists, NumPy arrays, or Pandas Series/DataFrames. It's good practice to convert to a `ColumnDataSource`.
3.  **Create a Figure:** `p = figure(tools="pan,wheel_zoom,box_zoom,reset,save,hover")`
4.  **Add Glyphs:** Call glyph methods on the figure object: `p.circle(x='x_col', y='y_col', source=my_cds, size=10, color='blue')`.
5.  **Customize:** Set titles, axis labels, styles, etc.: `p.title.text = "My Plot"`, `p.xaxis.axis_label = "X Values"`.
6.  **Arrange Layouts (Optional):** Use `row`, `column`, `gridplot` if multiple plots.
7.  **Show or Save:**
    -   `output_notebook()` (for Jupyter).
    -   `output_file("plot.html")`.
    -   `show(p)` (displays the plot based on the output mode).

Understanding these core concepts provides a solid foundation for creating both simple static plots and complex interactive data applications with Bokeh.

---