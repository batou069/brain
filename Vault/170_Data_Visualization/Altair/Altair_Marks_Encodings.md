---
tags:
  - altair
  - python
  - data_visualization
  - declarative_plotting
  - marks
  - encodings
  - grammar_of_graphics
  - concept
  - example
aliases:
  - Altair Marks
  - Altair Encodings
  - Visual Channels Altair
related:
  - "[[170_Data_Visualization/Altair/_Altair_MOC|_Altair_MOC]]"
  - "[[Altair_Chart_Object_Data]]"
  - "[[Altair_Data_Types_Scales]]"
  - "[[Grammar_of_Graphics]]"
worksheet:
  - WS_DataViz_1
date_created: 2025-06-11
---
# Altair: Marks and Encodings

In Altair's declarative visualization paradigm, **Marks** define the type of geometric object used to represent data points, and **Encodings** define how data columns (fields) are mapped to the visual properties (channels) of these marks.

## Marks
A **mark** specifies the fundamental geometric shape used in the plot. You set the mark type by calling a method on the `alt.Chart` object, such as `mark_point()`, `mark_line()`, `mark_bar()`, etc.

**Common Mark Types:**
-   `mark_point()`: Creates a scatter plot with individual points.
    -   Relevant encodings: `x`, `y`, `color`, `size`, `shape`, `opacity`, `tooltip`.
-   `mark_line()`: Creates a line plot connecting data points. Points are typically ordered by the x-encoding.
    -   Relevant encodings: `x`, `y`, `color` (for multiple lines), `strokeDash` (for line style), `opacity`, `tooltip`.
    -   Can add markers to the line with `mark_line(point=True)`.
-   `mark_bar()`: Creates bar charts.
    -   Relevant encodings: `x` (categorical or binned quantitative), `y` (quantitative length of bar), `color`, `opacity`, `tooltip`.
    -   For horizontal bars, swap x and y encoding roles or use `mark_bar(orient='horizontal')` if x is quantitative and y is categorical.
-   `mark_area()`: Creates area charts (filled regions under a line).
    -   Relevant encodings: `x`, `y` (defines upper boundary), `y2` (optional, defines lower boundary), `color`, `opacity`.
-   `mark_rect()`: Creates rectangles. Used for heatmaps or 2D histograms.
    -   Relevant encodings: `x`, `y` (often binned), `color` (representing value in the cell).
-   `mark_tick()`: Creates tick marks. Useful for rug plots or simple indicators.
-   `mark_rule()`: Creates horizontal or vertical lines. Useful for reference lines.
-   `mark_text()`: Renders text labels at data points.
-   `mark_circle()`, `mark_square()`: Specific point shapes.
-   `mark_geoshape()`: For geographical maps (often with GeoJSON).

You can also pass mark-specific properties as arguments to the mark method, e.g., `mark_line(strokeWidth=3, opacity=0.7)`.

## Encodings (`.encode()`)
The `.encode()` method is used to specify how columns from your data source (e.g., a Pandas DataFrame) are mapped to the visual properties (channels) of the chosen mark.

**Syntax:**
`chart.encode(channel1='field_name:type', channel2='field_name:type', ...)`

-   `channel`: The visual property to be encoded (e.g., `x`, `y`, `color`, `size`, `shape`, `opacity`, `tooltip`, `order`, `row`, `column`, `text`).
-   `field_name`: The name of the column in your DataFrame.
-   `type`: A shorthand for the data type of the field, which influences how Altair chooses scales and legends. See [[Altair_Data_Types_Scales]]. Common types:
    -   `:Q` for Quantitative (numerical, continuous)
    -   `:N` for Nominal (categorical, unordered)
    -   `:O` for Ordinal (categorical, ordered)
    -   `:T` for Temporal (dates and times)

**Common Encoding Channels:**

[list2tab|#Encoding Channels]
- Positional Channels
    -   `x`: Maps a data field to the x-axis position.
    -   `y`: Maps a data field to the y-axis position.
    -   `x2`, `y2`: Define secondary positions, e.g., for `mark_area()` or `mark_rect()`.
- Mark Property Channels
    -   `color`: Maps a data field to the color of marks.
        -   For `:Q` data, often uses a continuous color scale.
        -   For `:N` or `:O` data, uses distinct categorical colors.
    -   `size`: Maps a data field (usually `:Q`) to the size of marks.
    -   `shape`: Maps a data field (usually `:N` or `:O`) to different marker shapes (limited number of distinct shapes).
    -   `opacity`: Maps a data field (usually `:Q`) to the transparency of marks.
    -   `strokeDash`: Maps a data field (usually `:N` or `:O`) to different line dash styles.
- Text and Tooltip Channels
    -   `text`: Maps a data field to text labels displayed on or near marks.
    -   `tooltip`: Maps one or more data fields to be displayed in an interactive tooltip on hover.
        -   `tooltip=['column1', 'column2:Q']`
- Ordering Channel
    -   `order`: Specifies the order of data points, particularly important for `mark_line()` and `mark_area()` if the x-axis data is not already sorted or if plotting multiple stacked/grouped series.
        -   Can map to a field or use `alt.Order(field, sort='ascending'/'descending')`.
- Faceting Channels (for creating small multiples)
    -   `row`: Maps a categorical data field to create rows of subplots.
    -   `column`: Maps a categorical data field to create columns of subplots.
    -   `facet`: A more general faceting channel.

## Example: Combining Marks and Encodings

Let's use a conceptual e-commerce dataset of product sales.
```python
import altair as alt
import pandas as pd
import numpy as np

# Conceptual product sales data
np.random.seed(42)
product_sales_data = pd.DataFrame({
    'month': pd.to_datetime(np.tile([f'2023-{i:02d}-01' for i in range(1, 7)], 3)),
    'category': np.repeat(['Electronics', 'Books', 'Apparel'], 6),
    'units_sold': np.random.randint(50, 500, 18),
    'avg_rating': np.random.uniform(3.0, 5.0, 18).round(1),
    'promotion_active': np.random.choice([True, False], 18)
})
product_sales_data['revenue'] = product_sales_data['units_sold'] * np.random.uniform(10, 50, 18)

# 1. Line plot of units_sold over time, colored by category
# chart1 = alt.Chart(product_sales_data).mark_line(point=True).encode(
#     x='month:T',  # Temporal data for x-axis
#     y='units_sold:Q', # Quantitative data for y-axis
#     color='category:N', # Nominal data for color encoding
#     strokeDash='promotion_active:N', # Different line style if promotion was active
#     tooltip=['month:T', 'category:N', 'units_sold:Q', 'revenue:Q']
# ).properties(
#     title='Monthly Units Sold by Category',
#     width=600,
#     height=300
# )
# chart1.show()

# 2. Scatter plot of revenue vs. avg_rating, sized by units_sold, shaped by promotion
# chart2 = alt.Chart(product_sales_data).mark_point(filled=True).encode(
#     x='revenue:Q',
#     y='avg_rating:Q',
#     size='units_sold:Q',
#     color='category:N',
#     shape='promotion_active:N', # Map boolean to different shapes
#     tooltip=['category:N', 'revenue:Q', 'avg_rating:Q', 'units_sold:Q']
# ).properties(
#     title='Revenue vs. Rating (Size by Units Sold, Shape by Promotion)',
#     width=600
# ).interactive() # Make it zoomable and pannable
# chart2.show()

# 3. Bar chart of total units_sold per category
# chart3 = alt.Chart(product_sales_data).mark_bar().encode(
#     x='category:N',
#     y='sum(units_sold):Q', # Aggregate units_sold within encode
#     color='category:N',
#     tooltip=['category:N', 'sum(units_sold):Q']
# ).properties(
#     title='Total Units Sold per Category'
# )
# chart3.show()
```
In these examples:
-   `mark_line(point=True)` creates a line plot with markers at each data point.
-   `mark_point(filled=True)` creates filled circular markers for the scatter plot.
-   `mark_bar()` creates a bar chart.
-   Encodings like `x='month:T'`, `y='units_sold:Q'`, `color='category:N'`, `size='units_sold:Q'`, `shape='promotion_active:N'` map data columns to visual properties, with their types specified.
-   `sum(units_sold):Q` in the bar chart encoding shows that Altair can perform aggregations directly within the encoding definition.
-   `.interactive()` is a shorthand to enable basic zooming and panning.

The combination of marks and encodings provides a flexible and powerful way to construct a wide variety of statistical visualizations by declaratively mapping data to visual representations.

---