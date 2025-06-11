---
tags:
  - altair
  - python
  - data_visualization
  - declarative_plotting
  - customization
  - saving_charts
  - themes
  - configuration
  - concept
  - example
aliases:
  - Customizing Altair Charts
  - Saving Altair Plots
  - Altair Themes
related:
  - "[[170_Data_Visualization/Altair/_Altair_MOC|_Altair_MOC]]"
  - "[[Altair_Marks_Encodings]]"
  - "[[Altair_Data_Types_Scales]]"
  - "[[Vega_Lite_Grammar]]"
worksheet:
  - WS_DataViz_1
date_created: 2025-06-11
---
# Altair: Customization and Saving Charts

While Altair provides sensible defaults, it also offers extensive options for customizing the appearance of charts and for saving them in various formats.

## Customizing Chart Properties
Most chart-wide properties are set using the `.properties()` method or by configuring individual components like axes, legends, and titles.

[list2tab|#Altair Customization]
- Figure Properties (`.properties()`)
    -   **`width`**: Width of the plot in pixels.
    -   **`height`**: Height of the plot in pixels.
    -   **`title`**: Chart title. Can be a string or an `alt.TitleParams` object for more control.
    -   **`background`**: Background color of the chart.
    -   **Example:**
        ```python
        import altair as alt
        import pandas as pd
        # data = pd.DataFrame({'x': range(5), 'y':})
        # chart = alt.Chart(data).mark_line().encode(x='x:Q', y='y:Q')
        # customized_chart = chart.properties(
        #     title=alt.TitleParams(
        #         text="My Custom Title",
        #         subtitle="A subtitle for the chart",
        #         color="navy",
        #         fontSize=16,
        #         anchor='middle' # 'start', 'middle', 'end'
        #     ),
        #     width=400,
        #     height=250,
        #     background='#f0f0f0' # Light gray background
        # )
        # customized_chart.show()
        ```
- Axis Customization (`alt.X()`, `alt.Y()`, `.configure_axis()`)
    -   Within `encode()`, you can customize axes using `alt.X`, `alt.Y`:
        -   `title`: Axis title string (or `None` to remove).
        -   `axis=alt.Axis(...)`: Provides detailed control.
            -   `format`: D3 format string for tick labels (e.g., `'.2f'`, `'~s'`, `'%Y-%m-%d'`).
            -   `labelAngle`: Angle of tick labels.
            -   `grid`: Boolean to show/hide grid lines.
            -   `ticks`: Boolean to show/hide tick marks.
            -   `values`: Explicitly set tick mark values.
    -   Globally for all axes of a type: `chart.configure_axisX(labelFontSize=12, titleFontSize=14)` or `chart.configure_axis(gridColor='lightgray')`.
    -   **Example:**
        ```python
        # (Using chart from previous example)
        # styled_axes_chart = chart.encode(
        #     x=alt.X('x:Q', title='X-Variable (Units)', axis=alt.Axis(format='~s', grid=False, labelAngle=-45)),
        #     y=alt.Y('y:Q', title='Y-Variable (Values)', scale=alt.Scale(zero=False))
        # ).properties(title="Chart with Styled Axes")
        # styled_axes_chart.show()
        ```
- Legend Customization (`alt.Color()`, `alt.Size()`, etc., `.configure_legend()`)
    -   Within encodings like `alt.Color`, `alt.Size`, `alt.Shape`:
        -   `legend=alt.Legend(...)`:
            -   `title`: Legend title string.
            -   `orient`: `'left'`, `'right'`, `'top'`, `'bottom'`, etc.
            -   `symbolType`: Shape of legend symbols.
            -   `format`: Format string for legend labels if continuous.
    -   Globally: `chart.configure_legend(titleFontSize=14, labelFontSize=10, symbolSize=100)`.
    -   **Example:**
        ```python
        # data_legend = pd.DataFrame({
        #     'x': range(10), 'y': np.random.rand(10), 'category': ['A']*5 + ['B']*5
        # })
        # legend_chart = alt.Chart(data_legend).mark_point(size=100).encode(
        #     x='x:Q', y='y:Q',
        #     color=alt.Color('category:N', legend=alt.Legend(
        #         title='Product Types',
        #         orient='top-left',
        #         fillColor='lightgray',
        #         padding=10,
        #         cornerRadius=5
        #     ))
        # ).properties(title="Chart with Custom Legend")
        # legend_chart.show()
        ```
- Mark Properties Configuration (`.configure_mark()`, `.configure_<marktype>()`)
    -   Globally set default properties for all marks or specific mark types.
    -   `chart.configure_mark(color='green', opacity=0.7)`
    -   `chart.configure_point(size=100, filled=True)`
    -   `chart.configure_bar(fill='steelblue', stroke='black')`
    -   **Example:**
        ```python
        # (Using data from first example)
        # configured_mark_chart = alt.Chart(data).mark_line(point=True).encode(x='x:Q', y='y:Q').properties(
        #     title="Chart with Configured Mark Properties"
        # ).configure_line(
        #     color='firebrick',
        #     strokeWidth=3
        # ).configure_point(
        #     size=80,
        #     fill='orange',
        #     stroke='black'
        # )
        # configured_mark_chart.show()
        ```
- Themes (`alt.themes.enable()`)
    -   Altair supports themes that set a collection of default configurations.
    -   **Built-in themes:** `'default'`, `'dark'`, `'ggplot2'`, `'quartz'`, `'vox'`, `'fivethirtyeight'`.
    -   **Usage:** `alt.themes.enable('fivethirtyeight')` (applies globally for the session).
    -   You can register custom themes.
    -   **Example:**
        ```python
        # alt.themes.enable('ggplot2') # Enable ggplot2 theme
        # themed_chart = alt.Chart(data).mark_bar().encode(x='x:O', y='y:Q').properties(title="Chart with ggplot2 Theme")
        # themed_chart.show()
        # alt.themes.enable('default') # Revert to default
        ```

## Saving and Exporting Charts
Altair charts are ultimately Vega-Lite JSON specifications. To save or export them:

[list2tab|#Altair Saving Methods]
- Saving as JSON
    -   **Purpose:** Saves the Vega-Lite specification of the chart. This can be used with Vega-Lite renderers in other contexts or for debugging.
    -   **Method:** `chart.save("my_chart_spec.json")`
    -   **Example:**
        ```python
        # (Assuming 'chart' is an Altair Chart object)
        # chart.save("ecommerce_plot.json")
        # print("Chart specification saved to ecommerce_plot.json")
        ```
- Saving as HTML
    -   **Purpose:** Creates a self-contained HTML file that can be opened in any web browser to view the interactive chart.
    -   **Method:** `chart.save("my_chart.html", embed_options={'renderer': 'canvas'})` (or `'svg'`)
    -   `embed_options`: Can control how Vega-Embed (the JS library) renders the chart.
    -   **Example:**
        ```python
        # (Assuming 'chart' is an Altair Chart object)
        # chart.save("ecommerce_plot.html")
        # print("Interactive chart saved to ecommerce_plot.html")
        ```
- Exporting as Static Images (PNG, SVG, PDF)
    -   **Purpose:** For embedding in documents, presentations, or publications where interactivity is not needed.
    -   **Requirement:** Requires external tools/drivers because Altair itself doesn't render static images. Common options:
        1.  **`altair_viewer` with a browser engine (chromedriver/geckodriver):**
            -   Install: `pip install altair_viewer selenium Pillow` and a webdriver like `chromedriver`.
            -   Usage: `chart.save("my_chart.png")` or `chart.save("my_chart.svg")`. Altair will try to use `altair_viewer` if installed.
        2.  **`vl-convert` (Vega-Lite Convert):** A newer, more robust command-line utility and Python library for converting Vega-Lite specs.
            -   Install: `pip install vl-convert-python` (and potentially `pip install vl-convert-binary` or ensure `vl-convert` CLI is in PATH).
            -   Usage: `chart.save("my_chart.png")` will often use `vl-convert` if available and `altair_viewer` is not or fails.
    -   **Example (PNG):**
        ```python
        # (Assuming 'chart' is an Altair Chart object and a saver like vl-convert or altair_viewer+webdriver is set up)
        # try:
        #     chart.save("ecommerce_plot.png", scale_factor=2.0) # Increase resolution
        #     print("Chart saved to ecommerce_plot.png")
        # except Exception as e:
        #     print(f"Error saving static image (ensure vl-convert or altair_viewer with webdriver is installed): {e}")
        #     print("Try: pip install vl-convert-python altair_viewer selenium Pillow")
        ```
- Displaying in Environments
    -   **JupyterLab/Notebook:** Requires enabling the appropriate renderer.
        -   `alt.renderers.enable('jupyterlab')` or `'notebook'` or `'default'` (which tries to pick best).
        -   Charts are displayed inline when the `Chart` object is the last expression in a cell.
    -   **Other IDEs (VS Code, Spyder, etc.):** May require specific extensions or renderers (e.g., VS Code has built-in Vega-Lite support). Often, saving to HTML and opening in a browser is a reliable way to view.

Altair's customization options allow for fine-tuning the appearance of charts to meet specific aesthetic or communication needs, and its saving mechanisms provide flexibility for different use cases, from interactive web pages to static publication figures.

---