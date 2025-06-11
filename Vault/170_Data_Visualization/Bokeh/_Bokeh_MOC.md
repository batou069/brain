---
tags:
  - bokeh
  - python
  - data_visualization
  - interactive_plotting
  - web_based
  - library
  - moc
  - concept
aliases:
  - Bokeh MOC
  - Bokeh Library
related:
  - "[[_Data_Visualization_MOC]]"
  - "[[Matplotlib_Overview]]"
  - "[[170_Data_Visualization/Plotly/_Plotly_MOC|Plotly MOC]]"
  - "[[_Pandas_MOC|Pandas DataFrame]]"
worksheet:
  - WS_DataViz_1
date_created: 2025-06-11
---
# Bokeh MOC ✨📊

**Bokeh** is a Python library for creating interactive visualizations for modern web browsers. It provides an elegant and concise way to construct versatile graphics, ranging from simple plots to complex dashboards and data applications.

Bokeh's strength lies in its ability to generate interactive HTML/JavaScript-based visualizations without requiring the user to write any JavaScript directly.

## Core Philosophy & Features
-   **Interactivity First:** Designed from the ground up for creating interactive plots (zoom, pan, hover, selection, widgets).
-   **Web-Based Output:** Renders graphics using HTML, JavaScript, and CSS, making them suitable for embedding in web pages, Jupyter notebooks, or standalone HTML files.
-   **Multiple API Levels:**
    -   **`bokeh.plotting`:** A mid-level interface for creating common chart types by composing glyphs. This is often the primary interface used.
    -   **`bokeh.models`:** A low-level interface that provides maximum flexibility by allowing direct construction and manipulation of Bokeh's plot objects (models).
    -   High-level charting interfaces (like `bokeh.charts`, now deprecated) have been superseded by integration with libraries like HoloViews.
-   **Glyph-Based System:** Plots are constructed by adding "glyphs" (visual markers like circles, lines, rectangles, patches) to a figure. Each glyph has properties that can be mapped to data columns.
-   **Server Capability (`bokeh serve`):** Allows for building interactive data applications where Python code can react to UI events (e.g., widget changes, selections) and update plots dynamically.
-   **Handles Large Datasets (with Datashader):** Can integrate with Datashader for rendering very large datasets effectively by performing server-side aggregation before visualization.
-   **Extensible:** Allows for creating custom extensions and components.

## Key Concepts & Components
-   [[Bokeh_Overview_Concepts|Bokeh Overview & Core Concepts]] (Figures, Glyphs, Models, Documents, Server)
-   [[Bokeh_Plotting_Interface|Plotting with `bokeh.plotting`]]
    -   Creating figures (`figure()`).
    -   Adding glyphs (`fig.circle()`, `fig.line()`, `fig.vbar()`, etc.).
    -   Data sources (`ColumnDataSource`).
-   [[Bokeh_Layouts_Interactivity|Layouts and Interactivity]]
    -   Arranging plots (`row`, `column`, `gridplot`).
    -   Adding [[Bokeh_Widgets|Widgets]] (`Slider`, `Button`, `Select`).
    -   [[Bokeh_Interactions_Tools|Tools]] (HoverTool, PanTool, WheelZoomTool, TapTool, BoxSelectTool).
    -   [[Bokeh_Linking_Interactions|Linking Plots and Custom Interactions]] (JavaScript Callbacks, Python Callbacks with Bokeh Server).
-   [[Bokeh_Data_Sources_CDS|Data Sources (ColumnDataSource)]]
    -   The primary way to supply data to Bokeh plots, enabling shared data and linked interactions.
-   [[Bokeh_Styling_Theming|Styling and Theming]]
    -   Customizing visual attributes of glyphs, axes, titles, etc.
    -   Using built-in themes.
-   [[Bokeh_Embedding_Server_Apps|Embedding Plots and Bokeh Server Applications]]
    -   Generating standalone HTML files.
    -   Embedding in web pages.
    -   Building interactive applications with `bokeh serve`.

## Notes in this Bokeh Section
```dataview
LIST
FROM "170_Data_Visualization/Bokeh"
WHERE file.folder = this.file.folder AND file.name != this.file.name AND !contains(file.name, "MOC")
SORT file.name ASC
```

---