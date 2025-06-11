---
tags:
  - python
  - library
  - altair
  - data_visualization
  - declarative_visualization
  - vega_lite
  - concept
  - example
aliases:
  - Altair Python
  - Vega-Altair
related:
  - "[[_Data_Visualization_MOC]]"
  - "[[Plotly_and_Plotly_Express]]"
  - "[[_Pandas_MOC]]"
  - "[[Grammar_of_Graphics]]"
worksheet:
  - WS_DataViz_1
date_created: 2025-06-09
---
# Altair Library

## Overview
**Altair** is a declarative statistical visualization library for Python, based on the **Vega-Lite** visualization grammar. "Declarative" means that when using Altair, you describe *what* you want to visualize (the data, the mappings from data columns to visual properties like x-axis, y-axis, color, etc.) rather than *how* to draw it (e.g., drawing circles, lines, and axes explicitly).

Altair produces interactive visualizations that are rendered using Vega-Lite in a web browser.

## Key Features and Philosophy
[list2tab|#Altair Features]
- Declarative Syntax
    -   You specify mappings from data columns to visual **encodings** (e.g., `x`, `y`, `color`, `size`, `shape`).
    -   Altair (via Vega-Lite) then determines how to render the plot.
    -   This often leads to more concise and intuitive code for creating common statistical graphics.
- Based on Vega-Lite and the [[Grammar_of_Graphics|Grammar of Graphics]]
    -   Provides a structured way to think about and build visualizations by combining data, marks, encodings, transformations, and scales.
- Pandas DataFrame Integration
    -   Designed to work directly and seamlessly with [[_Pandas_MOC|Pandas DataFrames]]. Data is typically passed as a DataFrame.
- Interactive Charts
    -   Supports interactive features like tooltips, panning, zooming, and selections (which can be linked across multiple charts).
- JSON Output
    -   Altair charts are fundamentally JSON specifications that conform to the Vega-Lite schema. This JSON is then rendered by Vega-Lite in a JavaScript environment.
- Concise and Expressive
    -   Can create complex and layered visualizations with relatively little code.
- Publication Quality
    -   Can produce high-quality charts suitable for publication.

## Core Concepts in Altair
-   **`Chart` Object:** The fundamental object in Altair, initialized with a data source (usually a Pandas DataFrame).
    ```python
    # alt.Chart(my_dataframe)
    ```
-   **Marks:** Geometric objects used to represent data (e.g., `mark_point()`, `mark_bar()`, `mark_line()`, `mark_area()`, `mark_circle()`, `mark_rect()`).
    ```python
    # .mark_point()
    # .mark_bar()
    ```
-   **Encodings:** Mappings from data columns to visual properties of the marks. Specified using the `encode()` method.
    -   `alt.X('column_name:N')`: Map 'column_name' to x-axis. `:N` specifies nominal (categorical) type.
    -   `alt.Y('column_name:Q')`: Map 'column_name' to y-axis. `:Q` specifies quantitative (numerical) type.
    -   `alt.Color('column_name:N')`: Map 'column_name' to color.
    -   `alt.Size('column_name:Q')`
    -   `alt.Shape('column_name:N')`
    -   `alt.Tooltip(['col1', 'col2'])`
    -   Data types: `:N` (nominal), `:O` (ordinal), `:Q` (quantitative), `:T` (temporal).
-   **Transformations:** Operations applied to the data before encoding (e.g., `transform_filter()`, `transform_aggregate()`, `transform_bin()`, `transform_density()`).
-   **Interactivity (`interactive()`):** Easily add panning and zooming. More complex interactions via `selection_single`, `selection_interval`, `selection_multi`.
-   **Composition:** Charts can be layered, concatenated (horizontally `|` or vertically `&`), or faceted.

## Example Usage

### Scatter Plot with E-commerce Data
```python
import altair as alt
import pandas as pd
import numpy as np

# Conceptual e-commerce customer data
# np.random.seed(42)
# customer_data = pd.DataFrame({
#     'total_spent': np.random.uniform(50, 1000, 100),
#     'items_purchased': np.random.randint(1, 20, 100),
#     'customer_segment': np.random.choice(['A', 'B', 'C'], 100, p=[0.4, 0.4, 0.2]),
#     'days_since_last_purchase': np.random.randint(1, 365, 100)
# })

# Create an interactive scatter plot
# chart_scatter = alt.Chart(customer_data).mark_circle(size=60).encode(
#     x='total_spent:Q',  # Q for Quantitative
#     y='items_purchased:Q',
#     color='customer_segment:N', # N for Nominal (categorical)
#     size='days_since_last_purchase:Q',
#     tooltip=['total_spent', 'items_purchased', 'customer_segment', 'days_since_last_purchase']
# ).properties(
#     title='Customer Spending vs. Items Purchased (Altair)',
#     width=600,
#     height=400
# ).interactive() # Enable basic interactivity (pan, zoom)

# To display in Jupyter Notebook/Lab, this is often enough.
# To save as HTML:
# chart_scatter.save("customer_scatter_altair.html")
# chart_scatter # In Jupyter, this would render the chart
```
**Obsidian Chart Plugin Example / Conceptual Output:**
> [!note] Altair charts are interactive HTML/JavaScript based on Vega-Lite. An Obsidian Chart block cannot directly render this.
> **Conceptual Description:** This Python code would generate an interactive scatter plot specification.
> - Each point represents a customer.
> - X-axis: Total amount spent (quantitative).
> - Y-axis: Number of items purchased (quantitative).
> - Color: Customer segment (nominal/categorical).
> - Size of point: Days since last purchase (quantitative).
> - Hovering over a point would display a tooltip with the specified fields.
> - The chart would be zoomable and pannable.

### Bar Chart
```python
# import altair as alt
# import pandas as pd

# Conceptual: Average order value per product category
# category_data = pd.DataFrame({
#     'category': ['Electronics', 'Books', 'Clothing', 'Home Goods'],
#     'avg_order_value': [150.75, 45.50, 75.20, 95.00]
# })

# chart_bar = alt.Chart(category_data).mark_bar().encode(
#     x='category:N', # N for Nominal
#     y='avg_order_value:Q', # Q for Quantitative
#     color='category:N',
#     tooltip=['category', 'avg_order_value']
# ).properties(
#     title='Average Order Value by Product Category (Altair)',
#     width=alt.Step(80) # Control bar width indirectly
# )

# chart_bar.save("category_bar_altair.html")
# chart_bar
```
**Obsidian Chart Plugin Example / Conceptual Output:**
> **Conceptual Description:** This would generate an interactive bar chart.
> - X-axis: Product categories.
> - Y-axis: Average order value.
> - Each bar would be colored by category.
> - Hovering would show category and average order value.

## When to Use Altair
-   When you prefer a **declarative syntax** for specifying visualizations.
-   For creating a wide range of common **statistical graphics** with interactive capabilities.
-   If you want to generate visualizations based on the **Vega-Lite grammar**, which can then be rendered in any Vega-Lite compatible environment.
-   For quickly exploring Pandas DataFrames with concise code.
-   When building linked interactive charts where selections in one chart affect others.

## Altair vs. Other Libraries
-   **vs. Matplotlib:** Altair is much higher-level and declarative; Matplotlib is lower-level and imperative, offering more fine-grained control but requiring more code for standard plots.
-   **vs. Seaborn:** Both are high-level and good for statistical graphics. Seaborn is built on Matplotlib and outputs Matplotlib objects. Altair generates Vega-Lite JSON specs. Seaborn's API is more object-method oriented (e.g., `sns.scatterplot(...)`), while Altair uses a chained method syntax (`alt.Chart(...).mark_point().encode(...)`).
-   **vs. Plotly Express:** Both Plotly Express and Altair offer very concise, high-level declarative APIs. Plotly Express generates Plotly.js figures, while Altair generates Vega-Lite. The choice can come down to preferred syntax, specific chart types needed, or the target rendering ecosystem.
-   **vs. Bokeh:** Bokeh's `bokeh.plotting` is more imperative (composing glyphs). Altair is declarative. Both produce interactive web-based charts. Bokeh has stronger server capabilities for Python-backed data applications.

Altair provides an elegant and powerful way to create a wide range of statistical visualizations by describing their structure and encodings, leveraging the robust Vega-Lite grammar.

---