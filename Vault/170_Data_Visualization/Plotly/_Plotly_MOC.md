---
tags:
  - plotly
  - python
  - data_visualization
  - interactive_plotting
  - plotly_express
  - graph_objects
  - dash
  - moc
  - concept
aliases:
  - Plotly MOC
  - Plotly Express MOC
  - Interactive Visualizations Python
related:
  - "[[_Data_Visualization_MOC]]"
  - "[[Matplotlib_Overview]]"
  - "[[170_Data_Visualization/Seaborn/_Seaborn_MOC|Seaborn MOC]]"
  - "[[Bokeh_Library]]"
  - "[[Altair_Library]]"
worksheet:
  - WS_DataViz_1
date_created: 2025-06-11
---
# Plotly & Plotly Express MOC 📈🌐

**Plotly Python (`plotly`)** is an open-source interactive graphing library that allows users to create a wide variety of publication-quality, interactive charts. Plotly graphs can be displayed in Jupyter notebooks, saved to HTML files, embedded in web applications (often using [[Dash_Framework|Dash]]), or rendered as static images.

It offers two main APIs:
1.  **[[Plotly_Express_Quickstarts|Plotly Express (`plotly.express` or `px`)]]:** A high-level, concise API for creating entire figures quickly. It's often the recommended starting point.
2.  **[[Plotly_Graph_Objects_Detailed|Graph Objects (`plotly.graph_objects` or `go`)]]:** A lower-level API that provides more control over every aspect of the figure, including traces, layout, and individual elements.

## Core Philosophy & Features
-   **Interactivity:** Graphs are inherently interactive (hover tooltips, zoom, pan, selection) when rendered in HTML or a Dash app.
-   **Publication Quality:** Produces visually appealing charts suitable for reports and presentations.
-   **Wide Range of Chart Types:** Supports common charts (scatter, line, bar, histogram, pie, box) as well as specialized charts (3D plots, maps, financial charts, Sankey diagrams, sunburst charts, treemaps).
-   **Declarative Syntax (especially Plotly Express):** Focus on specifying *what* you want to plot from your data rather than the step-by-step drawing process.
-   **Integration with Pandas:** Works seamlessly with Pandas DataFrames.
-   **Web-Based:** Renders graphs using JavaScript (Plotly.js) under the hood, making them suitable for web environments.
-   **[[Dash_Framework|Dash Integration]]:** Plotly is the core graphing library for Dash, a Python framework for building analytical web applications.

## Key Concepts & Components
-   [[Plotly_Overview_Architecture|Plotly Overview & Architecture]] (Figures, Traces, Layout)
-   [[Plotly_Express_Quickstarts|Plotly Express (`px`)]] - High-level interface.
    -   Creating common charts with minimal code.
    -   Faceting and animations.
-   [[Plotly_Graph_Objects_Detailed|Graph Objects (`go`)]] - Lower-level interface.
    -   Defining `go.Figure()`
    -   Adding `go.Scatter()`, `go.Bar()`, etc. (traces).
    -   Customizing `fig.update_layout()`, `fig.update_xaxes()`, `fig.update_yaxes()`.
-   [[Plotly_Interactive_Features|Interactive Features]] (Hover, Zoom, Pan, Selections, Buttons, Sliders)
-   [[Plotly_Styling_Customization|Styling and Customization]] (Colors, Templates, Fonts, Annotations)
-   [[Plotly_Saving_Exporting|Saving and Exporting Plots]] (HTML, static images via Orca/Kaleido, Dash apps)
-   [[Plotly_Maps|Plotting Maps with Plotly]] (Scattergeo, Choropleth, Mapbox)
-   [[Plotly_3D_Plots|3D Plotting with Plotly]] (Scatter3d, Surface, Mesh)

## Notes in this Plotly Section
```dataview
LIST
FROM "170_Data_Visualization/Plotly"
WHERE file.folder = this.file.folder AND file.name != this.file.name AND !contains(file.name, "MOC")
SORT file.name ASC
```

---