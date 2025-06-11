---
tags:
  - altair
  - python
  - data_visualization
  - declarative_plotting
  - data_types
  - scales
  - binning
  - concept
  - example
aliases:
  - Altair Data Types
  - Altair Scales
  - Altair Binning
related:
  - "[[170_Data_Visualization/Altair/_Altair_MOC|_Altair_MOC]]"
  - "[[Altair_Marks_Encodings]]"
  - "[[Vega_Lite_Grammar]]"
worksheet:
  - WS_DataViz_1
date_created: 2025-06-11
---
# Altair: Data Types and Scales

In Altair, explicitly specifying the **data type** for each encoded field is crucial. This information guides Altair (and Vega-Lite) in choosing appropriate default **scales**, axes, legends, and mark properties.

## Data Type Shorthands
When defining an encoding (e.g., `alt.X('my_column:Q')`), you append a shorthand code to the field name to indicate its data type:
-   **`:Q` (Quantitative):** For continuous numerical data (e.g., temperature, price, height).
    -   Default scale: Linear.
    -   Default aggregation (if used in a channel like `y` with a categorical `x`): `mean`.
-   **`:N` (Nominal):** For categorical data where categories have no inherent order (e.g., product category, country name, gender).
    -   Default scale: Discrete (point scale for position, categorical color scheme for color).
    -   No default aggregation (typically used for grouping).
-   **`:O` (Ordinal):** For categorical data where categories have a meaningful order or ranking, but the differences between categories are not necessarily uniform (e.g., t-shirt size: Small, Medium, Large; satisfaction rating: Low, Medium, High).
    -   Default scale: Discrete with ordering preserved.
    -   Can specify `sort` order in encoding if not inferred from data.
-   **`:T` (Temporal):** For date and time values.
    -   Default scale: Time scale.
    -   Supports time unit transformations (e.g., year, month, day, hours).
-   **`:G` (GeoJSON feature):** For geographic shapes, used with `mark_geoshape`.

**Example:**
```python
# chart.encode(
#     x='temperature:Q',  # Temperature is quantitative
#     y='city:N',         # City is nominal (categorical)
#     color='month:O',    # Month is ordinal (ordered categories)
#     size='rainfall:Q'
# )
```

## Scales (`alt.Scale`)
A **scale** in visualization defines how a range of data values (the **domain**) is mapped to a range of visual values (the **range**, e.g., pixel positions, colors, sizes). Altair generally infers appropriate scales based on the data type of the encoded field, but you can customize them explicitly using `alt.Scale`.

Scales are specified within an encoding channel:
`alt.X('field:Q', scale=alt.Scale(type='log', domain=, range=))`

**Common Scale Properties:**
-   `type`: The type of scale.
    -   For quantitative data: `'linear'` (default), `'log'`, `'pow'`, `'sqrt'`, `'symlog'`.
    -   For temporal data: `'time'`, `'utc'`.
    -   For ordinal/nominal data (position): `'point'` (discrete points), `'band'` (for bars).
    -   For color: `'sequential'`, `'diverging'`, `'ordinal'`, `'nominal'`.
-   `domain`: A list `[,]` specifying the input data range to map. If not specified, inferred from data.
-   `range`: A list `[,]` specifying the output visual range (e.g., pixel range for position, color range for color).
-   `zero`: Boolean. If `True` (often default for bar charts), forces the scale domain to include zero.
-   `scheme`: For color scales, a string naming a Vega color scheme (e.g., `'viridis'`, `'blues'`, `'category10'`).
-   `padding`, `paddingInner`, `paddingOuter`: For band/point scales (e.g., spacing for bar charts).

**Example: Customizing scales for an e-commerce scatter plot**
```python
import altair as alt
import pandas as pd
import numpy as np

# Conceptual product data
# product_sales_data = pd.DataFrame({
#     'product_id': range(50),
#     'price': np.random.lognormal(mean=np.log(50), sigma=1, size=50).clip(1, 1000),
#     'units_sold': np.random.randint(1, 200, 50),
#     'category': np.random.choice(['Gadget', 'Accessory', 'Software'], 50)
# })

# chart_scales = alt.Chart(product_sales_data).mark_circle(opacity=0.7).encode(
#     x=alt.X('price:Q',
#             scale=alt.Scale(type='log', domain=), # Log scale for price, explicit domain
#             title='Product Price (USD, Log Scale)'),
#     y=alt.Y('units_sold:Q',
#             scale=alt.Scale(zero=False), # Don't force y-axis to include zero
#             title='Units Sold'),
#     color=alt.Color('category:N',
#                     scale=alt.Scale(scheme='viridis'), # Use 'viridis' color scheme
#                     legend=alt.Legend(title='Product Category')),
#     size=alt.Size('units_sold:Q',
#                   scale=alt.Scale(range=), # Map units_sold to marker size range
#                   legend=alt.Legend(title='Units Sold (Size)'))
# ).properties(
#     title='Product Sales Analysis with Custom Scales',
#     width=500, height=350
# ).interactive()

# chart_scales.show()
```

## Binning (`bin=True` or `alt.Bin(...)`)
For quantitative fields, Altair can automatically bin the data before mapping it to a visual channel. This is how histograms are created or how a continuous variable can be used to color bars.

-   Simple binning: `alt.X('price:Q', bin=True)` (Altair chooses default bin parameters)
-   Customized binning: `alt.X('price:Q', bin=alt.Bin(maxbins=10, step=50))`
    -   `maxbins`: Desired number of bins.
    -   `step`: Desired step size between bins.
    -   `extent`: Domain for binning.

**Example: Histogram of product prices with custom bins**
```python
# (Using product_sales_data from above)
# hist_binned = alt.Chart(product_sales_data).mark_bar().encode(
#     alt.X('price:Q', bin=alt.Bin(maxbins=20), title='Price Bins ($)'), # Max 20 bins
#     alt.Y('count()', title='Number of Products') # count() is a built-in aggregate
# ).properties(
#     title='Distribution of Product Prices (Custom Bins)'
# )
# hist_binned.show()
```

## Time Unit Transformations (`timeUnit=...`)
For temporal fields (`:T`), you can extract specific time units for aggregation or axis labeling.
-   `alt.X('order_date:T', timeUnit='yearmonth')`
-   Common time units: `year`, `quarter`, `month`, `date` (day of month), `day` (day of week), `hours`, `minutes`, `seconds`.

**Example: Monthly total units sold**
```python
# product_sales_data['order_date'] = pd.to_datetime('2023-01-01') + pd.to_timedelta(np.random.randint(0, 180, 50), unit='D')

# monthly_sales_trend = alt.Chart(product_sales_data).mark_line(point=True).encode(
#     alt.X('order_date:T', timeUnit='yearmonth', title='Month'),
#     alt.Y('sum(units_sold):Q', title='Total Units Sold'),
#     tooltip=['yearmonth(order_date):T', 'sum(units_sold):Q']
# ).properties(
#     title='Monthly Sales Trend'
# )
# monthly_sales_trend.show()
```

By correctly specifying data types and customizing scales, binning, and time units, you can create precise and meaningful visualizations with Altair that accurately reflect the nature of your data.

---