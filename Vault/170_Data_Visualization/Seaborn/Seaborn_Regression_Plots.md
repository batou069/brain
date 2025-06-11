---
tags:
  - seaborn
  - python
  - plotting
  - data_visualization
  - regression_plots
  - linear_regression
  - scatter_plot
  - concept
  - example
  - chart
  - matrix_plots
  - heatmap
  - clustermap
  - lmplot
  - regplot
aliases:
  - Seaborn Linear Regression Plot
  - sns.regplot
  - sns.lmplot
  - Seaborn Heatmap
  - Seaborn Clustermap
  - sns.heatmap
  - sns.clustermap
  - Seaborn Linear Regression Plots
related:
  - "[[170_Data_Visualization/Seaborn/_Seaborn_MOC|_Seaborn_MOC]]"
  - "[[Scatter_Plot]]"
  - "[[Line_Plot]]"
  - "[[Linear_Regression]]"
  - "[[_Pandas_MOC]]"
  - "[[Heatmap]]"
  - "[[Hierarchical_Clustering]]"
  - "[[Correlation_Matrix_Visualization]]"
  - "[[Trend_Line]]"
worksheet:
  - WS_DataViz_1
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Seaborn: Regression Plots (`regplot`, `lmplot`)

Seaborn's regression plots are designed to visualize linear relationships between two numerical variables. They create a [[Scatter_Plot|scatter plot]] of the data and then fit and plot a linear regression model, often including a confidence interval for the regression line.

`regplot()` is an axes-level function, while `lmplot()` is a figure-level function that combines `regplot()` with `FacetGrid` for creating faceted plots.

## `regplot()`
Plots data and a linear regression model fit.

[list2tab|#regplot]
- Purpose & Use
    -   To visualize the linear relationship between two numerical variables (`x` and `y`).
    -   Shows a scatter plot of the data points.
    -   Fits a linear regression model and plots the regression line.
    -   Can display a confidence interval around the regression line (typically 95% CI).
    -   Can also fit polynomial regression models or use robust regression.
- Key Parameters
    -   `data`: Pandas DataFrame.
    -   `x`, `y`: Column names for x and y axes.
    -   `scatter`: Boolean, if True (default), draw the scatter plot.
    -   `fit_reg`: Boolean, if True (default), estimate and plot a regression model.
    -   `ci`: Size of the confidence interval for the regression estimate (e.g., 95 for 95% CI). If `None`, no CI is drawn.
    -   `order`: If `order > 1`, estimate a polynomial regression.
    -   `logistic`: If True, assume `y` is binary and estimate a logistic regression.
    -   `lowess`: If True, use LOWESS (Locally Weighted Scatterplot Smoothing) to fit a nonparametric regression.
    -   `robust`: If True, use robust regression (less sensitive to outliers).
    -   `scatter_kws`, `line_kws`: Dictionaries of keyword arguments for customizing scatter points and the regression line.
    -   `color`: Color for all plot elements.
    -   `marker`: Scatter plot marker.
    -   `ax`: Matplotlib Axes object.
- Example (E-commerce: Tip vs. Total Bill)
    -
        ```python
        import seaborn as sns
        import matplotlib.pyplot as plt
        tips = sns.load_dataset("tips")

        plt.figure(figsize=(8, 6))
        sns.regplot(x="total_bill", y="tip", data=tips,
                    scatter_kws={'alpha':0.5, 's':50}, # Customize scatter points
                    line_kws={'color':'red', 'linewidth':2}) # Customize regression line
        plt.title("Tip Amount vs. Total Bill with Regression Line (Seaborn regplot)")
        plt.xlabel("Total Bill ($)")
        plt.ylabel("Tip Amount ($)")
        # plt.show()
        ```
    -   This plot shows individual tips vs. total bill amounts, with a linear regression line and its 95% confidence interval.
    -   **Obsidian Chart Plugin Example (Illustrative Scatter with Trend):**
        > [!note] This chart shows a scatter plot and a conceptual trend line. Seaborn's `regplot` automatically calculates and plots the regression line and confidence interval.
        ```chart
        type: scatter
        labels: ['Bill 1', 'Bill 2', 'Bill 3', 'Bill 4', 'Bill 5', 'Bill 6', 'Bill 7', 'Bill 8'] # Conceptual labels
        datasets:
          - label: 'Tip Data'
            data: [ # Conceptual (total_bill, tip) pairs
                {x: 10, y: 1.5}, {x: 15, y: 2.0}, {x: 20, y: 3.5}, {x: 25, y: 3.0},
                {x: 30, y: 4.5}, {x: 35, y: 4.0}, {x: 40, y: 5.5}, {x: 45, y: 5.0}
            ]
            backgroundColor: 'rgba(75, 192, 192, 0.6)'
            pointRadius: 6
          - label: 'Regression Line (Conceptual)'
            data: [ {x: 5, y: 1.2}, {x: 50, y: 6.0} ] # Two points defining a line
            type: line # Overlay line plot
            borderColor: 'rgba(255, 99, 132, 1)'
            fill: false
            borderWidth: 2
            pointRadius: 0 # No markers for the line itself
        options:
          title:
            display: true
            text: 'Illustrative: Tip vs. Total Bill with Trend'
          scales:
            x: { title: { display: true, text: 'Total Bill ($)' } }
            y: { title: { display: true, text: 'Tip Amount ($)' } }
        ```

## `lmplot()` (Figure-level Interface)
`lmplot()` is a more powerful function that combines `regplot()` with `FacetGrid`. This allows you to easily create faceted plots, showing the regression relationship across different subsets of your data defined by `hue`, `col`, and `row` parameters.

[list2tab|#lmplot]
- Purpose & Use
    -   Similar to `regplot()` but allows for faceting.
    -   Excellent for exploring how linear relationships vary across different categorical subgroups.
- Key Parameters
    -   `data`, `x`, `y`, `ci`, `order`, `logistic`, `lowess`, `robust`, `scatter_kws`, `line_kws`, `marker`: Similar to `regplot`.
    -   `hue`, `col`, `row`: Categorical variables to create facets and/or color-code points.
    -   `palette`: Color palette for `hue`.
    -   `height`: Height (in inches) of each facet.
    -   `aspect`: Aspect ratio of each facet.
    -   `col_wrap`: "Wrap" the column variable at this width, so that the column facets span multiple rows.
- Example (Tip vs. Total Bill, faceted by 'smoker' and colored by 'sex')
    -
        ```python
        import seaborn as sns
        import matplotlib.pyplot as plt
        tips = sns.load_dataset("tips")

        g = sns.lmplot(x="total_bill", y="tip", hue="sex", col="smoker", row="time",
                       data=tips, height=4, aspect=1,
                       palette="Set1",
                       scatter_kws={'alpha':0.6})
        g.fig.suptitle("Tip vs. Bill: Regression by Sex, Smoker, Time (Seaborn lmplot)", y=1.03)
        g.set_axis_labels("Total Bill ($)", "Tip Amount ($)")
        # plt.show()
        ```
    -   This creates a grid of plots. Each plot shows the tip vs. total bill relationship for a specific combination of `time` (row facet) and `smoker` (column facet), with points colored by `sex`.
    -   **Obsidian Chart Plugin Example:** An `lmplot` with facets is a collection of multiple `regplot`-like charts. It's not feasible to represent this complex faceted structure with a single basic Obsidian Chart block. One would conceptually create multiple individual charts, one for each facet.

## When to Use
-   Use `regplot()` for a single plot on a specific Matplotlib `Axes`.
-   Use `lmplot()` when you want to explore relationships across different subsets of your data using faceting. `lmplot` always creates its own figure.

Regression plots are powerful tools for initial exploration of linear relationships and how they might be influenced by other variables.

---

# Seaborn: Matrix Plots (`heatmap`, `clustermap`)

Seaborn's matrix plots are designed to visualize matrix-like data, where values are encoded as colors. These are particularly useful for displaying correlation matrices, confusion matrices, or any 2D dataset where you want to find patterns or clusters based on value intensity.

## `heatmap()`
Plots rectangular data as a color-encoded matrix.

[list2tab|#heatmap]
- Purpose & Use
    -   To visualize the magnitude of values in a 2D matrix as colors.
    -   Commonly used for correlation matrices, confusion matrices, or showing relationships between two categorical variables based on a third numerical variable (after creating a pivot table).
- Key Parameters
    -   `data`: 2D array or Pandas DataFrame that will be plotted.
    -   `vmin`, `vmax`: Values to anchor the colormap, otherwise inferred from the data.
    -   `cmap`: Colormap to use (e.g., 'viridis', 'coolwarm', 'YlGnBu').
    -   `center`: The value at which to center the colormap when plotting divergent data.
    -   `annot`: If True, write the data value in each cell. If an array-like with the same shape as `data`, then use this to annotate the heatmap instead of the raw data.
    -   `fmt`: String formatting code to use when adding annotations (e.g., `'.2f'` for 2 decimal places).
    -   `linewidths`, `linecolor`: Width and color of lines that will divide each cell.
    -   `cbar`: Boolean, whether to draw a colorbar.
    -   `cbar_kws`: Dictionary of keyword arguments for `fig.colorbar`.
    -   `square`: If True, set the Axes aspect to "equal" so each cell will be square-shaped.
    -   `xticklabels`, `yticklabels`: How to plot ticks and labels for x and y axes. Can be boolean, int, list of strings, or 'auto'.
- Example (Correlation matrix of e-commerce product features)
    -
        ```python
        import seaborn as sns
        import matplotlib.pyplot as plt
        import pandas as pd
        import numpy as np

        # Conceptual product feature data
        np.random.seed(42)
        data = {
            'price': np.random.rand(50) * 100 + 50,
            'avg_rating': np.random.rand(50) * 4 + 1,
            'num_reviews': np.random.randint(5, 500, 50),
            'shipping_cost': np.random.rand(50) * 10 + 5
        }
        # Introduce some correlations
        data['price'] += data['shipping_cost'] * 3
        data['num_reviews'] += data['avg_rating'] * 50
        products_df = pd.DataFrame(data)
        
        # Calculate correlation matrix
        correlation_matrix = products_df.corr()

        plt.figure(figsize=(8, 6))
        sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=.5)
        plt.title("Correlation Matrix of Product Features (Seaborn Heatmap)")
        # plt.show()
        ```
    -   This plot visualizes the pairwise correlations between product features. `annot=True` displays the correlation values on the cells. `cmap="coolwarm"` is good for divergent data like correlations.
    -   **Obsidian Chart Plugin Example (Illustrative Heatmap):**
        > [!note] True heatmaps are not a standard Chart.js type. This could be represented conceptually as a table with cell background colors, or more advanced plugins might support it. For simplicity, a textual representation of the matrix is often clear. The key is the color encoding of values.
        ```
        Conceptual Heatmap Data (Correlation Matrix):
                       price  avg_rating  num_reviews  shipping_cost
        price           1.00        0.15         0.20           0.85  <-- Strong positive with shipping_cost
        avg_rating      0.15        1.00         0.75           0.10  <-- Strong positive with num_reviews
        num_reviews     0.20        0.75         1.00           0.12
        shipping_cost   0.85        0.10         0.12           1.00
        
        (Imagine cells colored based on these values, e.g., dark red for high positive, dark blue for high negative, white for near zero)
        ```
        *Actual heatmap requires graphical rendering not directly supported by basic chart plugin in this way.*

## `clustermap()`
Plots a hierarchically-clustered heatmap. It reorders the rows and columns of the input matrix based on hierarchical clustering to group similar rows/columns together, often revealing structures in the data.

[list2tab|#clustermap]
- Purpose & Use
    -   To visualize matrix data where the ordering of rows and columns is not fixed and you want to discover underlying clusters or patterns by reordering them.
    -   Combines a heatmap with [[Hierarchical_Clustering|hierarchical clustering]] dendrograms for rows and/or columns.
- Key Parameters
    -   `data`: 2D array-like data.
    -   `pivot_kws`: If `data` is a tidy DataFrame, can pivot it before clustering.
    -   `method`: Linkage method for hierarchical clustering (e.g., 'average', 'ward', 'complete').
    -   `metric`: Distance metric for clustering (e.g., 'euclidean', 'correlation').
    -   `cmap`, `annot`, `fmt`, `linewidths`: Similar to `heatmap`.
    -   `row_cluster`, `col_cluster`: Booleans, whether to cluster rows and columns.
    -   `standard_scale`: `None`, `0` (rows), or `1` (columns). Whether to standardize data (subtract mean, divide by std. dev.) before clustering. `0` for rows, `1` for columns.
    -   `z_score`: `None`, `0` (rows), or `1` (columns). Whether to compute Z-scores (subtract mean, divide by std. dev.) for rows or columns. Applied after `standard_scale`.
- Example (Clustering gene expression data or customer purchase patterns)
    -
        ```python
        import seaborn as sns
        import matplotlib.pyplot as plt
        import pandas as pd
        import numpy as np

        # Conceptual customer-product purchase matrix (1 if purchased, 0 otherwise)
        np.random.seed(10)
        customers = [f'Cust_{i}' for i in range(10)]
        products = [f'Prod_{chr(65+j)}' for j in range(8)]
        purchase_data = np.random.choice(, size=(10, 8), p=[0.7, 0.3])
        purchase_df = pd.DataFrame(purchase_data, index=customers, columns=products)

        # Create a clustermap
        # Standardize rows to see relative purchase patterns per customer
        # g = sns.clustermap(purchase_df, cmap="viridis", standard_scale=0,
        #                    linewidths=.5, figsize=(8,8))
        # g.fig.suptitle("Customer Purchase Patterns (Seaborn Clustermap)", y=1.02)
        # plt.show()
        ```
    -   This plot would show the purchase matrix as a heatmap, but with rows (customers) and columns (products) reordered based on similarity, with dendrograms indicating the clustering hierarchy.
    -   **Obsidian Chart Plugin Example:** Clustermaps are highly specialized and not reproducible with basic chart types. They involve dendrograms + a heatmap. The output is inherently graphical and complex.

Matrix plots are excellent for getting a high-level overview of relationships and structures within 2D datasets.

---

# Seaborn: Regression Plots (`regplot`, `lmplot`)

Seaborn provides functions to visualize linear relationships as determined through regression. `regplot()` and `lmplot()` are the main functions for this. They draw a [[Scatter_Plot|scatter plot]] of two variables, `x` and `y`, and then fit and plot a linear regression model, along with a confidence interval for that regression.

## `sns.regplot()` (Axes-level)
-   **Purpose:** Plots data and a linear regression model fit. It's an axes-level function, meaning it plots onto a specific Matplotlib Axes.
-   **Key Parameters:**
    -   `data`: Pandas DataFrame.
    -   `x`, `y`: Column names for x and y variables.
    -   `scatter`: If `True` (default), draw the scatter plot.
    -   `fit_reg`: If `True` (default), estimate and plot a regression model.
    -   `ci`: Size of the confidence interval for the regression estimate (e.g., 95 for 95% CI). Set to `None` to disable.
    -   `order`: If `order` > 1, estimate a polynomial regression.
    -   `logistic`: If `True`, estimate a logistic regression (y should be binary or proportions).
    -   `lowess`: If `True`, estimate a nonparametric LOWESS model (locally weighted scatterplot smoothing).
    -   `scatter_kws`, `line_kws`: Dictionaries of keyword arguments for `plt.scatter` and `plt.plot`.
    -   `color`, `marker`: For scatter plot points.
    -   `ax`: Matplotlib Axes object.
-   **Use Cases:** Quickly visualizing a linear relationship and its uncertainty for a pair of variables.

**Example (Relationship between product price and customer rating):**
```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Conceptual product data
# np.random.seed(42)
# data_products_reg = pd.DataFrame({
#     'price': np.random.uniform(10, 200, 80),
#     # Simulate a weak negative correlation: higher price, slightly lower rating
#     'customer_rating': 4.5 - (np.random.uniform(10, 200, 80) / 150) + np.random.normal(0, 0.5, 80)
# })
# data_products_reg['customer_rating'] = data_products_reg['customer_rating'].clip(1, 5)


# plt.figure(figsize=(8, 6))
# sns.regplot(
#     data=data_products_reg,
#     x="price",
#     y="customer_rating",
#     scatter_kws={'s': 50, 'alpha': 0.6, 'color': 'skyblue'}, # Customize scatter points
#     line_kws={'color': 'red', 'linewidth': 2},               # Customize regression line
#     ci=95 # Show 95% confidence interval
# )
# plt.title("Customer Rating vs. Product Price with Regression Line")
# plt.xlabel("Price ($)")
# plt.ylabel("Customer Rating (1-5)")
# plt.grid(True, linestyle=':')
# plt.show()
```

## `sns.lmplot()` (Figure-level Interface)
-   **Purpose:** A figure-level interface for `regplot()` that combines it with `FacetGrid`. This makes it easy to plot regression models conditioned on other categorical variables (using `hue`, `col`, `row`).
-   **Key Parameters:**
    -   `data`, `x`, `y`: Similar to `regplot`.
    -   `hue`, `col`, `row`: Categorical variables for faceting or coloring different regression lines.
    -   `palette`: Colors for `hue` levels.
    -   `col_wrap`: Wrap `col` facets.
    -   `height`, `aspect`: Size of facets.
    -   All parameters of `regplot()` can also be passed (e.g., `ci`, `order`, `logistic`, `scatter_kws`, `line_kws`).
-   **Use Cases:** Exploring how linear relationships vary across different subsets of data.

**Example (Price vs. Rating, faceted by product category and conditioned by a 'premium_brand' flag):**
```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Conceptual product data with more dimensions
# np.random.seed(1)
# n_samples = 150
# data_lm = pd.DataFrame({
#     'price': np.random.uniform(20, 300, n_samples),
#     'customer_rating': np.random.uniform(2.5, 5, n_samples),
#     'category': np.random.choice(['Electronics', 'Apparel'], n_samples),
#     'is_premium_brand': np.random.choice([True, False], n_samples)
# })
# Simulate some relationship
# data_lm['customer_rating'] = data_lm['customer_rating'] - (data_lm['price'] / 200) \
#                              + (data_lm['is_premium_brand'] * 0.5) \
#                              + ( (data_lm['category'] == 'Electronics') * 0.3)
# data_lm['customer_rating'] = data_lm['customer_rating'].clip(1, 5)


# Create faceted regression plots
# g = sns.lmplot(
#     data=data_lm,
#     x="price",
#     y="customer_rating",
#     hue="is_premium_brand",  # Different color lines for premium/non-premium
#     col="category",          # Separate plots for each category
#     palette={"True": "green", "False": "blue"},
#     height=5, aspect=1,
#     scatter_kws={'alpha':0.5, 's':30},
#     ci=None # Disable confidence interval for cleaner look in this example
# )
# g.fig.suptitle("Price vs. Rating: Regression by Brand Type and Category", y=1.03)
# g.set_axis_labels("Price ($)", "Customer Rating (1-5)")
# plt.tight_layout(rect=[0, 0, 1, 0.97])
# plt.show()
```

## Key Differences: `regplot()` vs. `lmplot()`
-   **Level:** `regplot()` is axes-level; `lmplot()` is figure-level (creates its own figure and `FacetGrid`).
-   **Faceting:** `lmplot()` directly supports faceting via `row`, `col`, and `hue`. To achieve faceting with `regplot()`, you would need to manually create subplots and iterate.
-   **Input Data Format:** `regplot()` is more flexible and can accept `x` and `y` as NumPy arrays, Pandas Series, or column names if `data` is provided. `lmplot()` typically requires `data` to be a Pandas DataFrame and `x`, `y` to be column names.
-   **Return Value:** `regplot()` returns the Matplotlib `Axes` object it plotted on. `lmplot()` returns a `FacetGrid` instance.

Both functions are powerful tools for visualizing linear relationships and are often a good first step in exploring bivariate numerical data. They can highlight trends, suggest correlations, and indicate where linear models might be appropriate or where non-linearities exist.

---