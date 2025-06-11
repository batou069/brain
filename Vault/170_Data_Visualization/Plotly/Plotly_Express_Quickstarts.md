---
tags:
  - plotly
  - python
  - data_visualization
  - interactive_plotting
  - plotly_express
  - px
  - high_level_api
  - concept
  - example
aliases:
  - Plotly Express
  - px
  - Plotly High-Level API
related:
  - "[[170_Data_Visualization/Plotly/_Plotly_MOC|_Plotly_MOC]]"
  - "[[Plotly_Overview_Architecture]]"
  - "[[_Pandas_MOC|Pandas DataFrame]]"
  - "[[Plotly_Graph_Objects_Detailed]]"
worksheet:
  - WS_DataViz_1
date_created: 2025-06-11
---
# Plotly Express (`px`)

**Plotly Express** is a high-level, concise Python API within the Plotly graphing library, typically imported as `px`. It allows users to create entire, feature-rich [[Plotly_Overview_Architecture|Plotly figures]] with a single function call. Plotly Express is often the recommended starting point for creating Plotly visualizations, especially when working with [[_Pandas_MOC|Pandas DataFrames]].

Each Plotly Express function returns a `plotly.graph_objects.Figure` object, which can be further customized using its `update_traces()` and `update_layout()` methods if needed.

## Key Advantages of Plotly Express
-   **Conciseness:** Create complex, interactive plots with minimal code.
-   **Pandas Integration:** Designed to work seamlessly with Pandas DataFrames. Column names can be passed directly as arguments.
-   **Sensible Defaults:** Produces attractive plots with good default settings.
-   **Automatic Configuration:** Handles many details automatically, like legends, color scales, and hover information based on the input data.
-   **Faceting and Animations:** Easily create faceted plots (small multiples) and animations.
-   **Built-in Chart Types:** Supports a wide range of common chart types.

## Common Plotly Express Functions
Plotly Express functions typically follow a pattern: `px.<chart_type>(data_frame, x, y, color, size, facet_row, facet_col, animation_frame, ...)`

[list2tab|#PX Functions]
- Scatter Plots
    -   `px.scatter(data_frame, x, y, color, size, symbol, hover_data, facet_row, facet_col, ...)`
    -   **Example (E-commerce: Product price vs. rating, colored by category):**
        ```python
        import plotly.express as px
        import pandas as pd
        import numpy as np

        # Conceptual product data
        # np.random.seed(42)
        # product_data_px = pd.DataFrame({
        #     'price': np.random.uniform(10, 200, 100),
        #     'rating': np.random.uniform(2.5, 5, 100).round(1),
        #     'category': np.random.choice(['Electronics', 'Books', 'Apparel'], 100),
        #     'sales_count': np.random.randint(10, 500, 100)
        # })

        # fig_scatter = px.scatter(
        #     product_data_px,
        #     x="price",
        #     y="rating",
        #     color="category",              # Color points by category
        #     size="sales_count",            # Size points by sales_count
        #     hover_data=['product_name'], # Assuming a 'product_name' column for hover (add to df if needed)
        #     title="Product Price vs. Rating by Category and Sales Count",
        #     labels={'price': 'Price ($)', 'rating': 'Customer Rating (1-5)'}
        # )
        # fig_scatter.update_layout(legend_title_text='Category')
        # fig_scatter.show() # In a Jupyter environment or opens browser
        ```
- Line Plots
    -   `px.line(data_frame, x, y, color, line_group, symbol, line_dash, hover_data, ...)`
    -   **Example (Monthly sales trend for different product lines):**
        ```python
        import plotly.express as px
        import pandas as pd
        import numpy as np

        # Conceptual monthly sales data
        # months = pd.to_datetime([f"2023-{i:02d}-01" for i in range(1, 7)])
        # sales_trends_px = pd.DataFrame({
        #     'month': np.tile(months, 3),
        #     'product_line': np.repeat(['Widgets', 'Gadgets', 'Gizmos'], 6),
        #     'sales': np.concatenate([
        #         np.array() * 1.1,
        #         np.array() * 0.9,
        #         np.array() * 1.3
        #     ]) + np.random.randn(18) * 10
        # })
        # sales_trends_px['sales'] = sales_trends_px['sales'].clip(lower=10)

        # fig_line = px.line(
        #     sales_trends_px,
        #     x="month",
        #     y="sales",
        #     color="product_line",       # Different line for each product line
        #     markers=True,               # Add markers to points
        #     symbol="product_line",      # Different marker symbol per line
        #     title="Monthly Sales Trend by Product Line",
        #     labels={'sales': 'Sales ($)', 'month': 'Month'}
        # )
        # fig_line.show()
        ```
- Bar Charts
    -   `px.bar(data_frame, x, y, color, barmode='relative', facet_row, facet_col, ...)`
        -   `barmode`: `{'relative', 'group', 'overlay'}` (default 'relative' for stacked).
    -   **Example (Total sales per e-commerce category):**
        ```python
        # Using product_data_px from scatter example, aggregate first
        # category_sales_sum = product_data_px.groupby('category')['sales_count'].sum().reset_index()

        # fig_bar = px.bar(
        #     category_sales_sum,
        #     x="category",
        #     y="sales_count",
        #     color="category",
        #     title="Total Sales Volume by Product Category",
        #     labels={'sales_count': 'Total Units Sold', 'category': 'Product Category'},
        #     text_auto=True # Display values on bars
        # )
        # fig_bar.update_layout(showlegend=False)
        # fig_bar.show()
        ```
- Histograms
    -   `px.histogram(data_frame, x, y, color, marginal, nbins, ...)`
        -   `marginal`: `{'rug', 'box', 'violin'}` to add marginal plots.
    -   **Example (Distribution of product prices):**
        ```python
        # Using product_data_px from scatter example
        # fig_hist = px.histogram(
        #     product_data_px,
        #     x="price",
        #     color="category",       # Show separate histograms for each category
        #     marginal="box",         # Add box plots on the margin
        #     nbins=30,
        #     title="Distribution of Product Prices by Category",
        #     labels={'price': 'Price ($)'}
        # )
        # fig_hist.show()
        ```
- Pie Charts
    -   `px.pie(data_frame, names, values, color, hole, ...)`
    -   **Example (Market share of product categories):**
        ```python
        # Using category_sales_sum from bar chart example
        # fig_pie = px.pie(
        #     category_sales_sum,
        #     names="category",
        #     values="sales_count",
        #     title="Market Share by Product Category (Sales Volume)",
        #     hole=0.3 # For a donut chart
        # )
        # fig_pie.update_traces(textposition='inside', textinfo='percent+label')
        # fig_pie.show()
        ```
- Box Plots
    -   `px.box(data_frame, x, y, color, notched, points, ...)`
    -   **Example (Distribution of customer ratings per category):**
        ```python
        # Using product_data_px from scatter example
        # fig_box = px.box(
        #     product_data_px,
        #     x="category",
        #     y="rating",
        #     color="category",
        #     notched=True, # Show notches for median CI
        #     points="all", # Show all underlying data points
        #     title="Customer Rating Distribution by Category",
        #     labels={'rating': 'Customer Rating (1-5)', 'category': 'Product Category'}
        # )
        # fig_box.show()
        ```
- And many more...
    -   `px.violin()`, `px.strip()`, `px.funnel()`, `px.timeline()`
    -   Geographical maps: `px.scatter_geo()`, `px.line_geo()`, `px.choropleth()`, `px.scatter_mapbox()`, `px.choropleth_mapbox()`.
    -   3D plots: `px.scatter_3d()`, `px.line_3d()`, `px.surface()`.
    -   Polar charts: `px.scatter_polar()`, `px.line_polar()`, `px.bar_polar()`.
    -   Treemaps: `px.treemap()`.
    -   Sunburst charts: `px.sunburst()`.

## Faceting and Animation
Plotly Express makes it very easy to create faceted plots (small multiples) and animations:
-   **Faceting:** Use `facet_row` and/or `facet_col` arguments.
    ```python
    # fig_facet = px.scatter(product_data_px, x="price", y="rating", color="category",
    #                        facet_col="another_categorical_column", # e.g., 'region'
    #                        title="Price vs Rating, Faceted by Region")
    # fig_facet.show()
    ```
-   **Animation:** Use `animation_frame` (for discrete frames, e.g., year) and `animation_group` (to identify objects across frames).
    ```python
    # Assuming a 'year' column in sales_trends_px
    # sales_trends_px['year'] = sales_trends_px['month'].dt.year 
    # fig_anim = px.bar(sales_trends_px, x="product_line", y="sales", color="product_line",
    #                   animation_frame="year", animation_group="product_line",
    #                   range_y=[0, sales_trends_px['sales'].max() * 1.1], # Fix y-axis range
    #                   title="Animated Yearly Sales by Product Line")
    # fig_anim.show()
    ```

## Customization
While Plotly Express provides quick figures, the returned `fig` object is a standard `plotly.graph_objects.Figure`. You can customize it further:
-   `fig.update_layout(...)`: For titles, axis labels, fonts, legends, margins, etc.
-   `fig.update_traces(...)`: For modifying properties of the traces (lines, markers).
-   `fig.add_trace(...)`: To add new Graph Objects traces to a figure created by Plotly Express.

Plotly Express significantly lowers the barrier to creating rich, interactive visualizations in Python, acting as a powerful wrapper around Plotly's Graph Objects system.

---