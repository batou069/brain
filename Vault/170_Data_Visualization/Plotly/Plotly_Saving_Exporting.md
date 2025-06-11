---
tags:
  - plotly
  - python
  - data_visualization
  - interactive_plotting
  - saving
  - exporting
  - html
  - image
  - kaleido
  - orca
  - concept
  - example
aliases:
  - Saving Plotly Charts
  - Exporting Plotly Figures
  - Plotly to HTML
  - Plotly to Image
related:
  - "[[170_Data_Visualization/Plotly/_Plotly_MOC|_Plotly_MOC]]"
  - "[[Plotly_Graph_Objects_Detailed]]"
  - "[[Dash_Framework]]"
worksheet:
  - WS_DataViz_1
date_created: 2025-06-11
---
# Plotly: Saving and Exporting Figures

Plotly figures, created with either [[Plotly_Express_Quickstarts|Plotly Express]] or [[Plotly_Graph_Objects_Detailed|Graph Objects]], can be saved or exported in various formats for sharing, embedding in reports, or web deployment.

## Displaying Figures (`fig.show()`)
Before saving, you typically display a figure using `fig.show()`. The behavior of `fig.show()` depends on the environment:
-   **Jupyter Notebook/Lab:** Renders the interactive figure directly in the output cell.
-   **Python Scripts (outside Jupyter):** May open the figure in a web browser tab.
-   **IDE-specific Viewers:** Some IDEs (like PyCharm, VS Code with Python extension) have built-in Plotly viewers.

`fig.show(renderer="...")` can be used to specify a renderer (e.g., "browser", "jupyterlab", "vscode", "png", "svg").

## Saving to HTML
This is the most common way to save a Plotly figure while preserving its interactivity.
-   **Method:** `fig.write_html("path/to/figure.html", full_html=True, include_plotlyjs='cdn')`
-   **`full_html` (boolean, default `True`):**
    -   If `True`, produces a self-contained HTML file including the Plotly.js JavaScript library.
    -   If `False`, produces an HTML div containing the plot, which can be embedded in an existing HTML page (Plotly.js must be loaded separately on that page).
-   **`include_plotlyjs` (string or boolean, default `'cdn'`):**
    -   `'cdn'`: Includes a script tag that loads Plotly.js from a CDN (Content Delivery Network). File size is smaller, requires internet access to view.
    -   `True` or `'True'`: Embeds the full Plotly.js library into the HTML file. File size is larger (~3MB), but the plot is viewable offline.
    -   `'directory'`: Creates a `plotly.js` file in the same directory.
    -   `False` or `'False'`: Does not include Plotly.js (useful if embedding in a page that already loads it).
-   **Example:**
    ```python
    import plotly.express as px
    # df_stocks = px.data.stocks() # Load sample stock data

    # fig = px.line(df_stocks, x='date', y=['GOOG', 'AAPL'], title='Stock Prices')

    # Save as a self-contained interactive HTML file (Plotly.js from CDN)
    # fig.write_html("stock_prices_interactive.html")

    # Save with Plotly.js embedded for offline viewing
    # fig.write_html("stock_prices_offline.html", include_plotlyjs=True)
    ```

## Exporting to Static Images (PNG, JPG, SVG, PDF, EPS)
To export Plotly figures as static images, you need an external engine because the rendering is done by JavaScript (Plotly.js).
-   **Engine Requirement:** **Kaleido** is the recommended engine for static image export. It's a separate Python package.
    -   Installation: `pip install -U kaleido`
    -   Older versions of Plotly might have used Orca, which is now largely superseded by Kaleido.
-   **Method:** `fig.write_image("path/to/figure.png", format=None, width=None, height=None, scale=None)`
    -   `format`: If not specified, inferred from file extension (e.g., 'png', 'jpeg', 'webp', 'svg', 'pdf', 'eps').
    -   `width`, `height`: Image dimensions in pixels.
    -   `scale`: Factor to scale image resolution.
-   **Example:**
    ```python
    import plotly.express as px
    # df_iris = px.data.iris()
    # fig = px.scatter(df_iris, x="sepal_width", y="sepal_length", color="species",
    #                  title="Iris Dataset Scatter Plot")

    # Ensure Kaleido is installed: pip install -U kaleido
    # try:
    #     # Save as PNG
    #     fig.write_image("iris_scatter.png", width=800, height=600, scale=2)
    #     print("Saved iris_scatter.png")

    #     # Save as SVG (vector format)
    #     fig.write_image("iris_scatter.svg")
    #     print("Saved iris_scatter.svg")

    #     # Save as PDF
    #     fig.write_image("iris_scatter.pdf")
    #     print("Saved iris_scatter.pdf")
    # except ValueError as e:
    #     # This error often occurs if Kaleido is not installed or not found in PATH
    #     print(f"Error saving image (is Kaleido installed and configured?): {e}")
    #     print("Please install Kaleido: pip install -U kaleido")
    ```

## Other Export Options
-   **`fig.to_json()` / `fig.to_dict()`:** Returns the JSON string or Python dictionary representation of the figure, which can be used with Plotly.js directly or stored.
-   **`pio.to_json(fig)` / `pio.from_json(json_str)`:** Utilities in `plotly.io` for JSON serialization.
-   **Embedding in Web Applications ([[Dash_Framework|Dash]]):**
    -   Dash is Plotly's framework for building analytical web applications. Plotly figures are a core component of Dash layouts.
    -   In Dash, you return `go.Figure` objects from callbacks to update graphs in the web app.

## Considerations for Exporting
-   **Interactivity:** Static image formats (PNG, JPG, PDF, SVG) will **lose all interactivity** (hover, zoom, pan, buttons, sliders). Only HTML export preserves full interactivity.
-   **Vector vs. Raster (Static Images):**
    -   **SVG, PDF, EPS:** Vector formats, scalable without loss of quality. Good for publications.
    -   **PNG, JPG:** Raster formats, pixel-based. Can become pixelated if scaled up too much. PNG is good for plots with sharp lines and text; JPG is better for photographic images (though less common for plots).
-   **Dependencies (Kaleido/Orca):** Static image export requires an external engine to be installed and often accessible in the system's PATH or configured correctly. This can sometimes be a hurdle in restricted environments.
-   **File Size:**
    -   HTML with embedded Plotly.js can be large (~3MB+). Using CDN for Plotly.js makes HTML files smaller but requires internet.
    -   Static images vary in size based on complexity and resolution.

Choosing the right export format depends on how you intend to use or share the visualization. HTML is best for preserving interactivity, while static images are suitable for reports, presentations, or publications where interactivity is not needed.

---