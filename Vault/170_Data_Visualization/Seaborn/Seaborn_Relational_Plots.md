---
tags:
  - seaborn
  - python
  - plotting
  - data_visualization
  - relational_plots
  - scatterplot
  - lineplot
  - concept
  - example
  - chart
  - relplot
aliases:
  - Seaborn Scatter Plot
  - Seaborn Line Plot
  - sns.scatterplot
  - sns.lineplot
  - sns.relplot
related:
  - "[[170_Data_Visualization/Seaborn/_Seaborn_MOC|_Seaborn_MOC]]"
  - "[[Scatter_Plot]]"
  - "[[Line_Plot]]"
  - "[[_Pandas_MOC]]"
  - "[[Matplotlib_Overview]]"
  - "[[_Pandas_MOC|Pandas DataFrame]]"
worksheet:
  - WS_DataViz_1
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Seaborn: Relational Plots (`scatterplot`, `lineplot`, `relplot`)

Seaborn's relational plots are used to visualize the statistical relationship between two numerical variables. The main functions are `scatterplot()` and `lineplot()`, with `relplot()` being a figure-level interface that can create faceted versions of these plots.

## `scatterplot()`
Visualizes the relationship between two numerical variables where each point represents an observation. Additional dimensions can be encoded using `hue`, `size`, and `style` semantics.

[list2tab|#scatterplot]
- Purpose & Use
    -   To understand correlation, clusters, and identify outliers between two numeric variables.
    -   Can show how a third (categorical or numerical) variable influences the relationship using `hue` (color).
    -   Can show how a fourth (numerical or categorical) variable influences the relationship using `size`.
    -   Can show how a fifth (categorical) variable influences the relationship using `style` (marker style).
- Key Parameters
    -   `data`: Pandas DataFrame.
    -   `x`, `y`: Column names for x and y axes.
    -   `hue`: Column name for color encoding (categorical or numeric).
    -   `size`: Column name for marker size encoding (numeric).
    -   `style`: Column name for marker style encoding (categorical).
- Example (E-commerce: Total Bill vs. Tip, colored by Smoker status)
    -
        ```python
        import seaborn as sns
        import matplotlib.pyplot as plt
        import pandas as pd

        # Load the 'tips' dataset from Seaborn
        tips_df = sns.load_dataset("tips")

        plt.figure(figsize=(8, 6))
        sns.scatterplot(x="total_bill", y="tip", hue="smoker", size="size",
                        style="time", data=tips_df, alpha=0.7, palette="viridis")
        plt.title("Tip Amount vs. Total Bill (Seaborn)")
        plt.xlabel("Total Bill ($)")
        plt.ylabel("Tip Amount ($)")
        plt.legend(title="Legend")
        plt.grid(True, linestyle='--', alpha=0.5)
        # plt.show() # In a real script/notebook
        ```
    -   This plot shows each dining party as a point. The x-axis is the total bill, y-axis is the tip. Points are colored by whether the payer was a smoker, sized by the party size, and styled by the time of day (Lunch/Dinner).
    -   **Obsidian Chart Plugin Example (Illustrative):**
        > [!note] The chart below is a simplified representation using Obsidian Charts. Seaborn's actual output would include its specific styling, automatic legend generation for `hue`, `size`, and `style`, and potentially more sophisticated marker handling.
        ```chart
        type: scatter
        labels: ['Bill 1', 'Bill 2', 'Bill 3', 'Bill 4', 'Bill 5', 'Bill 6'] # Conceptual labels for points
        datasets:
          - label: 'Smoker - Lunch'
            data: [ {x: 10, y: 1.5}, {x: 25, y: 3.0} ] # (total_bill, tip)
            backgroundColor: 'rgba(75, 192, 192, 0.7)' # Example color
            pointRadius: 5 # Conceptual size
            pointStyle: 'circle' # Conceptual style
          - label: 'Non-Smoker - Dinner'
            data: [ {x: 15, y: 2.0}, {x: 30, y: 4.5}, {x: 45, y: 5.0} ]
            backgroundColor: 'rgba(255, 99, 132, 0.7)'
            pointRadius: 8
            pointStyle: 'rectRot'
          - label: 'Smoker - Dinner'
            data: [ {x: 20, y: 3.5} ]
            backgroundColor: 'rgba(54, 162, 235, 0.7)'
            pointRadius: 6
            pointStyle: 'triangle'
        options:
          title:
            display: true
            text: 'Illustrative Scatter: Bill vs. Tip'
          scales:
            x:
              title:
                display: true
                text: 'Total Bill ($)'
            y:
              title:
                display: true
                text: 'Tip Amount ($)'
        ```

## `lineplot()`
Draws a line plot with the possibility of several semantic groupings. It is primarily used to visualize the trend of one numerical variable as a function of another, especially when the x-axis variable is ordered (like time or a sequence). It can also show confidence intervals around the estimate of the central tendency (mean by default).

[list2tab|#lineplot]
- Purpose & Use
    -   To show trends, often over time or an ordered sequence.
    -   Can display an estimate of central tendency and a confidence interval.
    -   `hue`, `size`, and `style` can show how the relationship changes across subgroups.
- Key Parameters
    -   `data`, `x`, `y`, `hue`, `size`, `style`, `palette`: Similar to `scatterplot`.
    -   `estimator`, `errorbar`, `markers`, `dashes`, `sort`.
- Example (Conceptual: Average product rating over months)
    -
        ```python
        import seaborn as sns
        import matplotlib.pyplot as plt
        import pandas as pd
        import numpy as np

        # Conceptual monthly average product ratings
        np.random.seed(42)
        months_idx = range(1, 13) # Represent months as 1-12
        product_A_ratings = 4.0 + 0.5 * np.sin(np.linspace(0, 2*np.pi, 12)) + np.random.randn(12) * 0.1
        product_B_ratings = 3.5 + 0.3 * np.cos(np.linspace(0, 2*np.pi, 12)) + np.random.randn(12) * 0.1
        
        ratings_df = pd.DataFrame({
            'month': list(months_idx) * 2,
            'product': ['A']*12 + ['B']*12,
            'avg_rating': np.concatenate([product_A_ratings, product_B_ratings])
        })
        ratings_df['avg_rating'] = ratings_df['avg_rating'].clip(1,5)

        plt.figure(figsize=(10, 6))
        sns.lineplot(x="month", y="avg_rating", hue="product", style="product",
                     markers=True, dashes=False, data=ratings_df, errorbar=('ci', 95))
        plt.title("Average Monthly Product Rating (Seaborn)")
        plt.xlabel("Month")
        plt.ylabel("Average Rating (1-5)")
        plt.xticks(ticks=range(1,13), labels=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
        plt.legend(title="Product")
        # plt.show()
        ```
    -   This plot tracks average ratings for Product A and B over 12 months.
    -   **Obsidian Chart Plugin Example (Illustrative):**
        > [!note] Seaborn's `lineplot` can automatically calculate and display confidence intervals if multiple y-values exist per x-point (or per x-hue combination). The chart below simplifies this to show the lines.
        ```chart
        type: line
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        datasets:
          - label: 'Product A Rating'
            data: [3.9, 4.3, 4.6, 4.4, 4.1, 3.8, 3.9, 4.2, 4.5, 4.3, 4.0, 3.7] # Conceptual data
            borderColor: 'rgba(255, 99, 132, 1)'
            tension: 0.1
            fill: false
          - label: 'Product B Rating'
            data: [3.8, 3.6, 3.3, 3.1, 3.4, 3.6, 3.9, 3.7, 3.5, 3.2, 3.5, 3.8] # Conceptual data
            borderColor: 'rgba(54, 162, 235, 1)'
            tension: 0.1
            fill: false
        options:
          title:
            display: true
            text: 'Illustrative Line Plot: Avg Product Ratings'
          scales:
            y:
              min: 1
              max: 5
              title:
                display: true
                text: 'Average Rating'
            x:
              title:
                display: true
                text: 'Month'
        ```

## `relplot()` (Figure-level Interface)
`relplot()` combines `scatterplot()` and `lineplot()` with `FacetGrid` for faceted plots.
-   `kind`: `'scatter'` (default) or `'line'`.
-   `row`, `col`: Categorical variables for faceting.

**Example (Faceted scatter plot - Chart not easily represented here directly):**
```python
import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset("tips")

# Scatter plot of tip vs total_bill, faceted by 'sex' (columns) and 'time' (rows)
g = sns.relplot(
    x="total_bill", y="tip",
    hue="smoker", style="smoker",
    col="sex", row="time",
    data=tips,
    height=3
)
g.fig.suptitle("Tip vs. Total Bill (Faceted by Sex and Time - Seaborn)", y=1.03)
# plt.show()
```
> A `relplot` creating a grid of scatter plots is complex to represent with a single Obsidian Chart. It would essentially be multiple individual scatter charts arranged in a grid, each corresponding to a facet.

Relational plots are fundamental for exploring how two numerical variables interact, potentially conditioned on other categorical or numerical variables.

---

# Seaborn: Relational Plots (`scatterplot`, `lineplot`, `relplot`)

Seaborn provides functions for visualizing statistical relationships between variables. The primary functions for this are `scatterplot()` and `lineplot()`, which can also be accessed through the figure-level interface `relplot()`. These functions allow for rich visual encoding of multiple variables.

## `sns.scatterplot()`
-   **Purpose:** To show the relationship between two numerical variables. Additional variables can be encoded using `hue`, `size`, and `style` parameters.
-   **Key Parameters:**
    -   `data`: Pandas DataFrame.
    -   `x`, `y`: Column names for x and y axes.
    -   `hue`: Column name for grouping variable that will produce points with different colors.
    -   `size`: Column name for grouping variable that will produce points with different sizes.
    -   `style`: Column name for grouping variable that will produce points with different markers.
    -   `palette`: Colors to use for `hue` levels.
    -   `sizes`: Min and max size for `size` mapping.
    -   `ax`: Matplotlib Axes object to draw the plot onto.
-   **Use Cases:** Identifying correlation, clusters, outliers between two continuous variables, potentially segmented by categorical variables.

**Example:**
```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Conceptual e-commerce data: product price, customer rating, product category, sales volume
np.random.seed(42)
data_products = pd.DataFrame({
    'price': np.random.uniform(10, 500, 100),
    'customer_rating': np.random.uniform(1, 5, 100).round(1),
    'category': np.random.choice(['Electronics', 'Books', 'Apparel'], 100),
    'sales_volume': np.random.randint(10, 1000, 100)
})

# plt.figure(figsize=(10, 6))
# sns.scatterplot(
#     data=data_products,
#     x="price",
#     y="customer_rating",
#     hue="category",          # Color by category
#     size="sales_volume",     # Size by sales volume
#     sizes=(20, 200),         # Range of marker sizes
#     alpha=0.7,
#     palette="viridis"
# )
# plt.title("Product Price vs. Customer Rating (by Category & Sales Volume)")
# plt.xlabel("Price ($)")
# plt.ylabel("Customer Rating (1-5)")
# plt.legend(title="Category & Sales Volume", bbox_to_anchor=(1.05, 1), loc='upper left')
# plt.tight_layout()
# plt.show()
```

## `sns.lineplot()`
-   **Purpose:** To draw a line plot that can show the relationship between `x` and `y`, potentially with confidence intervals around an estimate (e.g., mean) if multiple `y` values exist for an `x` value. Ideal for time series or showing trends.
-   **Key Parameters:**
    -   `data`, `x`, `y`, `hue`, `size`, `style`, `palette`, `ax`: Similar to `scatterplot`.
    -   `estimator`: Aggregate function to estimate the central tendency for `y` at each `x` (e.g., 'mean', 'median', `None` if data is already aggregated or unique y for each x). Default is 'mean'.
    -   `ci`: Size of the confidence interval for the regression estimate (e.g., 95 for 95% CI, 'sd' for standard deviation, `None` to disable). Deprecated in newer versions, use `errorbar`.
    -   `errorbar`: Name of function that computes error bar values, or `('ci', 95)` or `'sd'`.
    -   `units`: Grouping variable identifying sampling units, used for repeated measures data.
    -   `sort`: If `True` (default), sort data by `x` values before plotting.
-   **Use Cases:** Visualizing trends over time, comparing trends for different groups, showing mean response with confidence intervals.

**Example:**
```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Conceptual monthly sales data for different product categories
# np.random.seed(0)
# months = pd.to_datetime([f"2023-{i:02d}-01" for i in range(1, 13)])
# data_sales = []
# for cat in ['Electronics', 'Books', 'Apparel']:
#     # Base sales trend with some noise and category-specific pattern
#     base_trend = np.linspace(100, 150 + np.random.randint(-20, 20), 12)
#     cat_sales = base_trend + np.random.normal(0, 10, 12) * (1 if cat=='Electronics' else 0.5 if cat=='Books' else 0.2)
#     for i, month in enumerate(months):
#         data_sales.append({'month': month, 'category': cat, 'sales': max(0, cat_sales[i])}) # Ensure sales are non-negative
# monthly_sales_df = pd.DataFrame(data_sales)

# plt.figure(figsize=(12, 6))
# sns.lineplot(
#     data=monthly_sales_df,
#     x="month",
#     y="sales",
#     hue="category",        # Different line for each category
#     style="category",      # Different marker/linestyle for each category
#     markers=True,
#     dashes=False,
#     errorbar=('ci', 95)    # Show 95% confidence interval if multiple obs per x-hue
# )
# plt.title("Monthly Sales Trend by Product Category")
# plt.xlabel("Month")
# plt.ylabel("Sales Amount")
# plt.xticks(rotation=45)
# plt.legend(title="Category")
# plt.tight_layout()
# plt.show()
```

## `sns.relplot()` (Figure-level Interface)
-   **Purpose:** A figure-level interface for drawing relational plots onto a `FacetGrid`. This allows creating plots with multiple subplots (facets) based on the levels of other categorical variables.
-   **Key Parameters:**
    -   `data`, `x`, `y`, `hue`, `size`, `style`, `palette`: Similar to `scatterplot` and `lineplot`.
    -   `kind`: `{'scatter', 'line'}` (default 'scatter'). Specifies the type of plot to draw.
    -   `row`, `col`: Column names for faceting variables that define the rows and columns of the subplot grid.
    -   `col_wrap`: "Wrap" the `col` variable at this width, so that the `col` facets span multiple rows.
    -   `height`, `aspect`: Control the size of each facet.
-   **Use Cases:** Comparing relationships or trends across different subsets of the data defined by faceting variables.

**Example (using `relplot` for faceted scatter plots):**
```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Using data_products from scatterplot example
# np.random.seed(42)
# data_products = pd.DataFrame({
#     'price': np.random.uniform(10, 500, 300), # More data for faceting
#     'customer_rating': np.random.uniform(1, 5, 300).round(1),
#     'category': np.random.choice(['Electronics', 'Books', 'Apparel'], 300),
#     'sales_volume': np.random.randint(10, 1000, 300),
#     'region': np.random.choice(['North', 'South', 'East', 'West'], 300) # Faceting variable
# })


# Faceted scatter plot: price vs rating, colored by category, faceted by region
# g = sns.relplot(
#     data=data_products,
#     x="price",
#     y="customer_rating",
#     hue="category",
#     size="sales_volume",
#     sizes=(20, 150),
#     col="region",          # Create subplots for each region
#     col_wrap=2,            # Wrap columns after 2 subplots
#     kind="scatter",        # Explicitly 'scatter'
#     height=4, aspect=1.2
# )
# g.fig.suptitle("Product Price vs. Rating by Category, Region, and Sales Volume", y=1.03) # y to adjust suptitle position
# g.set_axis_labels("Price ($)", "Customer Rating (1-5)")
# plt.tight_layout(rect=[0, 0, 1, 0.97])
# plt.show()
```

Relational plots in Seaborn offer a powerful and convenient way to explore and visualize relationships between variables, with easy options for encoding multiple dimensions and creating faceted views.

---