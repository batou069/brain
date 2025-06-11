---
tags:
  - altair
  - python
  - data_visualization
  - declarative_plotting
  - compound_charts
  - layering
  - concatenation
  - faceting
  - interactivity
  - selections
  - concept
  - example
aliases:
  - Altair Compound Charts
  - Altair Interactive Plots
  - Altair Selections
  - Layering Altair
  - Faceting Altair
related:
  - "[[170_Data_Visualization/Altair/_Altair_MOC|_Altair_MOC]]"
  - "[[Altair_Marks_Encodings]]"
  - "[[Vega_Lite_Grammar]]"
worksheet:
  - WS_DataViz_1
date_created: 2025-06-11
---
# Altair: Compound Charts & Interactivity

Altair allows for the creation of complex visualizations by combining simpler charts through **layering**, **concatenation**, **faceting**, and **repeating**. It also provides powerful mechanisms for adding **interactivity** through selections.

## Compound Charts

[list2tab|#Compound Chart Types]
- Layering (`+` operator or `alt.layer()`)
    -   **Purpose:** To overlay multiple mark types or charts on top of each other, sharing the same scales and axes. Each layer can have its own mark type and encodings.
    -   **Syntax:** `chart1 + chart2` or `alt.layer(chart1, chart2, ...)`
    -   **Example (Line plot with points and a rule for the mean):**
        ```python
        import altair as alt
        import pandas as pd
        import numpy as np

        # Conceptual e-commerce daily sales data
        # np.random.seed(42)
        # date_rng = pd.date_range(start='2023-01-01', periods=30, freq='D')
        # sales_data = pd.DataFrame({
        #     'date': date_rng,
        #     'daily_sales': np.random.poisson(100, 30) + np.sin(np.arange(30)/5) * 20 + 50
        # })

        # base = alt.Chart(sales_data).encode(x='date:T')
        # line = base.mark_line(color='steelblue').encode(y='daily_sales:Q')
        # points = base.mark_point(color='red', size=50, opacity=0.7).encode(y='daily_sales:Q')
        # mean_rule = alt.Chart(sales_data).mark_rule(color='grey', strokeDash=).encode(
        #     y='mean(daily_sales):Q',
        #     size=alt.value(2) # Explicitly set size for rule
        # )
        
        # layered_chart = (line + points + mean_rule).properties(
        #     title='Daily Sales with Points and Mean Line',
        #     width=600, height=300
        # )
        # layered_chart.show()
        ```
- Horizontal Concatenation (`|` operator or `alt.hconcat()`)
    -   **Purpose:** To place multiple charts side-by-side, sharing the y-axis by default if encodings are compatible.
    -   **Syntax:** `chart1 | chart2` or `alt.hconcat(chart1, chart2, ...)`
- Vertical Concatenation (`&` operator or `alt.vconcat()`)
    -   **Purpose:** To place multiple charts one above another, sharing the x-axis by default if encodings are compatible.
    -   **Syntax:** `chart1 & chart2` or `alt.vconcat(chart1, chart2, ...)`
    -   **Example (Sales histogram and box plot vertically concatenated):**
        ```python
        # (Using sales_data from layering example)
        # hist_sales = alt.Chart(sales_data).mark_bar().encode(
        #     alt.X('daily_sales:Q', bin=alt.Bin(maxbins=15), title='Daily Sales ($)'),
        #     alt.Y('count()', title='Frequency')
        # ).properties(width=500, height=200, title='Sales Distribution (Histogram)')

        # box_sales = alt.Chart(sales_data).mark_boxplot(extent='min-max').encode(
        #     alt.X('daily_sales:Q', title='') # Empty title to align with hist
        # ).properties(width=500, height=100, title='Sales Distribution (Box Plot)')

        # concatenated_chart = hist_sales & box_sales
        # concatenated_chart.show()
        ```
- Faceting (`facet()`)
    -   **Purpose:** To create "small multiples" – a grid of plots where each subplot shows a different subset of the data based on the values of one or more categorical variables.
    -   **Syntax:** `alt.Chart(data).mark_...().encode(...).facet(row='field:N', column='field:N')`
    -   Also available as encoding channels `row` and `column`.
    -   **Example (Sales line plots faceted by product category):**
        ```python
        # Conceptual e-commerce data with categories
        # np.random.seed(10)
        # date_rng_facet = pd.to_datetime(np.tile([f'2023-{i:02d}-01' for i in range(1, 4)], 2)) # 3 months, 2 categories
        # facet_data = pd.DataFrame({
        #     'date': date_rng_facet,
        #     'category': np.repeat(['Electronics', 'Apparel'], 3),
        #     'sales': np.random.randint(100, 500, 6) + np.array([0,50,100, 0,20,40]) # Trend
        # })

        # faceted_lines = alt.Chart(facet_data).mark_line(point=True).encode(
        #     x='month(date):O', # Ordinal month for x-axis
        #     y='sales:Q',
        #     color='category:N'
        # ).properties(
        #     width=250, height=150
        # ).facet(
        #     column='category:N', # Create a column of plots for each category
        #     title="Monthly Sales by Category (Faceted)"
        # )
        # faceted_lines.show()
        ```- Repeating (`repeat()`)
    -   **Purpose:** To create a grid of plots where each plot shows the same type of visualization but for different data fields.
    -   **Syntax:** `alt.Chart(data).mark_...().encode(x=alt.repeat('column'), y='some_field:Q', ...).repeat(column=['field1', 'field2', ...])`
    -   The `alt.repeat('layer')`, `alt.repeat('row')`, or `alt.repeat('column')` specifies which fields to iterate over for which visual channel or facet direction.

## Interactivity with Selections
Altair's interactivity is primarily driven by **selections**. A selection defines an interactive element (like clicking, dragging over an interval) that can then be used to conditionally modify encodings, filter data, or link multiple charts.

[list2tab|#Altair Selections]
- Types of Selections
    -   **`alt.selection_point()` (formerly `selection_single`):** Selects a single point or multiple discrete points (if `toggle=True`).
        -   `fields`: List of fields to project selected values from.
        -   `on`: Event to trigger selection (e.g., 'click', 'mouseover').
        -   `empty`: How to treat empty selection (`'all'` or `'none'`).
        -   `toggle`: Boolean or string expression for toggling selection.
    -   **`alt.selection_interval()`:** Selects a rectangular region (an interval) by clicking and dragging.
        -   `encodings`: List of channels to define the interval (e.g., `['x']`, `['y']`, `['x', 'y']`).
    -   **`alt.selection_legend()`:** Selects based on clicking items in a legend. (Implicitly created when using `color` or `shape` with `interactive()`).
- Using Selections
    -   **Conditional Encodings (`alt.condition()`):** Change visual properties (color, size, opacity) of marks based on whether they are part of a selection.
        -   `alt.condition(selection, value_if_selected, value_if_not_selected)`
    -   **Filtering Data (`transform_filter()`):** Filter the data displayed in a chart based on a selection made in the same or another chart (linked brushing).
        -   `chart.transform_filter(selection_object)`
    -   **Binding to Legend:** Selections can be bound to legends for interactive filtering by clicking legend items. `color=alt.Color('field:N', legend=alt.Legend(title='Click to Select'))` combined with `selection_legend`.

**Example: Interactive Scatter Plot with Linked Histogram (Brushing & Linking)**
```python
import altair as alt
import pandas as pd
import numpy as np
# from vega_datasets import data # For a common dataset if needed

# Conceptual e-commerce product data
# np.random.seed(42)
# product_data_interactive = pd.DataFrame({
#     'price': np.random.uniform(10, 300, 200),
#     'rating': np.random.uniform(2.0, 5.0, 200).round(1),
#     'category': np.random.choice(['Electronics', 'Books', 'Apparel', 'Home Goods'], 200),
#     'units_sold': np.random.randint(1, 100, 200)
# })

# 1. Define an interval selection for brushing on the scatter plot
# brush = alt.selection_interval(encodings=['x', 'y']) # Select a rectangular region

# 2. Create the scatter plot
# scatter = alt.Chart(product_data_interactive).mark_point().encode(
#     x='price:Q',
#     y='rating:Q',
#     color=alt.condition(brush, 'category:N', alt.value('lightgray')), # Color selected points by category, others gray
#     size='units_sold:Q',
#     tooltip=['price', 'rating', 'category', 'units_sold']
# ).add_params( # Use add_params for newer Altair versions
#     brush
# ).properties(
#     title="Price vs. Rating (Brush to filter histogram)",
#     width=400, height=300
# )

# 3. Create a histogram of units_sold, filtered by the brush selection
# histogram_units_sold = alt.Chart(product_data_interactive).mark_bar().encode(
#     alt.X('units_sold:Q', bin=alt.Bin(maxbins=15), title='Units Sold'),
#     alt.Y('count()', title='Number of Products'),
#     tooltip=['count()']
# ).transform_filter(
#     brush # Apply the brush selection as a filter
# ).properties(
#     title="Distribution of Units Sold (for selected products)",
#     width=400, height=150
# )

# 4. Concatenate the charts
# linked_dashboard = scatter & histogram_units_sold
# linked_dashboard.show()
```
In this example:
-   An interval selection `brush` is defined.
-   The `scatter` plot colors points based on this `brush` selection.
-   The `histogram_units_sold` uses `transform_filter(brush)` to only show data for the points selected in the scatter plot.
-   Dragging a rectangle on the scatter plot will dynamically update the histogram.

Altair's approach to compound charts and selections enables the creation of sophisticated, linked visualizations that facilitate data exploration and discovery with a concise and powerful grammar.

---