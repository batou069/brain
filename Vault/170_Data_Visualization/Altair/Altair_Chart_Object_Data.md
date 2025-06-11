---
tags:
  - altair
  - python
  - data_visualization
  - declarative_plotting
  - chart_object
  - data_input
  - pandas
  - concept
  - example
aliases:
  - Altair Chart
  - Altair Data Input
  - alt.Chart
related:
  - "[[170_Data_Visualization/Altair/_Altair_MOC|_Altair_MOC]]"
  - "[[Altair_Overview_Declarative_Viz]]"
  - "[[_Pandas_MOC|Pandas DataFrame]]"
  - "[[Altair_Marks_Encodings]]"
worksheet:
  - WS_DataViz_1
date_created: 2025-06-11
---
# Altair: The Chart Object and Data Input

The fundamental object in Altair is the **`Chart` object**. All Altair visualizations begin by creating an instance of `alt.Chart`. This object serves as the top-level container for your visualization specification.

## Creating a `Chart` Object
A `Chart` object is typically initialized with a data source.

```python
import altair as alt
import pandas as pd

# The primary way to pass data is as a Pandas DataFrame
# Conceptual e-commerce product data
product_data = pd.DataFrame({
    'product_name': ['Widget A', 'Gadget B', 'Gizmo C', 'Thingamajig D'],
    'category': ['Electronics', 'Electronics', 'Home Goods', 'Apparel'],
    'price': [19.99, 49.50, 120.00, 35.75],
    'rating': [4.5, 3.8, 4.8, 4.1],
    'units_sold': [150, 80, 30, 110]
})

# Create a Chart object with the DataFrame
chart = alt.Chart(product_data)

# At this point, 'chart' is an Altair Chart object, but it doesn't yet know
# what to draw (marks) or how to map data to visual properties (encodings).
# print(type(chart)) # <class 'altair.vegalite.v5.api.Chart'>
```

## Data Input Formats
Altair is designed to work most seamlessly with **[[_Pandas_MOC|Pandas DataFrames]]**.

1.  **Pandas DataFrame (Recommended):**
    -   This is the most common and idiomatic way to provide data to Altair.
    -   Altair automatically handles the conversion of the DataFrame into a JSON representation suitable for Vega-Lite.
    -   Column names from the DataFrame are directly used when specifying [[Altair_Marks_Encodings|encodings]].

2.  **URL to JSON or CSV File:**
    -   Altair can directly load data from a URL that points to a JSON or CSV file. Vega-Lite handles fetching and parsing this data in the browser.
    ```python
    # data_url_csv = "https://raw.githubusercontent.com/plotly/datasets/master/auto-mpg.csv"
    # chart_from_url = alt.Chart(data_url_csv).mark_point().encode(
    #     x='horsepower:Q',
    #     y='mpg:Q',
    #     color='origin:N'
    # )
    # chart_from_url.show() # Renderer needed (e.g., in Jupyter or save to HTML)
    ```

3.  **Dictionary / List of Dictionaries (JSON serializable):**
    -   You can pass data in a format that is directly serializable to JSON, like a dictionary representing columnar data or a list of dictionaries representing row-oriented data.
    ```python
    # data_dict_columnar = {
    #     'a': list('ABCDEFG'),
    #     'b': [28, 55, 43, 91, 81, 53, 19]
    # }
    # chart_from_dict = alt.Chart(data_dict_columnar).mark_bar().encode(x='a:N', y='b:Q')

    # data_list_of_dicts_row_oriented = [
    #     {'product': 'X', 'sales': 100},
    #     {'product': 'Y', 'sales': 150},
    # ]
    # chart_from_list_dicts = alt.Chart(pd.DataFrame(data_list_of_dicts_row_oriented)).mark_bar().encode(x='product:N', y='sales:Q')
    # Using pd.DataFrame() is often cleaner for list of dicts.
    ```

4.  **`alt.Data` object or `alt.UrlData`:**
    -   For more explicit control over data specification, especially when dealing with named datasets in Vega-Lite or more complex data loading scenarios.
    ```python
    # from vega_datasets import data as vega_data_source # Example source of URLs
    # cars_url = vega_data_source.cars.url
    # chart_alt_urldata = alt.Chart(alt.UrlData(cars_url)).mark_point().encode(x='Horsepower:Q', y='Miles_per_Gallon:Q')
    ```

## Data Size Considerations and Transformers
-   **Default Behavior:** By default, Altair embeds the data directly into the JSON specification of the chart. This is convenient for smaller datasets.
-   **Large Datasets (`alt.data_transformers.enable('json')` or `'csv'`):**
    -   For DataFrames with more than 5000 rows (by default), Altair will raise a `MaxRowsError` to prevent creating overly large JSON specifications that can crash browsers or notebooks.
    -   To handle this, you can enable a **data transformer**:
        -   `alt.data_transformers.enable('json')`: Saves the data to a temporary local JSON file and the chart specification references this file.
        -   `alt.data_transformers.enable('csv')`: Saves data to a temporary local CSV file.
        -   When sharing such charts (e.g., as HTML), you'd need to ensure the data file is also accessible or use a URL.
    -   Alternatively, for very large data, consider pre-aggregation in Pandas/Spark before plotting, or use tools designed for server-side rendering of large datasets (like Datashader with Bokeh/HoloViews).

```python
# import altair as alt
# import pandas as pd
# import numpy as np

# # Create a larger DataFrame
# large_data = pd.DataFrame({
#     'x': np.random.rand(10000),
#     'y': np.random.rand(10000)
# })

# # This would likely raise MaxRowsError without a data transformer
# # chart_large_default = alt.Chart(large_data).mark_circle().encode(x='x:Q', y='y:Q')
# # try:
# #     chart_large_default.show()
# # except alt.MaxRowsError as e:
# #     print(f"Caught expected error: {e}")


# # Enable a data transformer (e.g., save data to a local JSON file)
# alt.data_transformers.enable('json') # Or 'csv'
# # This will now work by saving data to a temporary file
# chart_large_transformed = alt.Chart(large_data).mark_circle(size=5, opacity=0.2).encode(x='x:Q', y='y:Q')
# # chart_large_transformed.show()
# print("Chart with 'json' data transformer enabled can handle larger data.")

# # To disable data transformers and revert to default (embedding data):
# # alt.data_transformers.disable_ zowel()
```

The `Chart` object, initialized with data (preferably a Pandas DataFrame), is the starting point for all Altair visualizations. Subsequent calls to methods like `mark_*()` and `encode()` build upon this `Chart` object to define the complete visualization specification.

---