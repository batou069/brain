---
tags:
  - seaborn
  - python
  - plotting
  - data_visualization
  - multi_plot_grids
  - facetgrid
  - pairgrid
  - jointgrid
  - concept
  - example
  - faceting
  - pairplot
  - jointplot
aliases:
  - Seaborn Faceting
  - sns.FacetGrid
  - sns.PairGrid
  - sns.JointGrid
  - sns.pairplot
  - sns.jointplot
  - Seaborn FacetGrid
  - Seaborn PairGrid
  - Seaborn JointGrid
  - Small Multiples Seaborn
related:
  - "[[170_Data_Visualization/Seaborn/_Seaborn_MOC|_Seaborn_MOC]]"
  - "[[Matplotlib_Figure_Subplot_Axes]]"
  - "[[Scatter_Plot_Matrix]]"
  - "[[Visualizing_Multidimensional_Data]]"
worksheet:
  - WS_DataViz_1
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Seaborn: Multi-Plot Grids (`FacetGrid`, `PairGrid`, `JointGrid`)

Seaborn offers powerful figure-level functions and classes for creating grids of plots. These allow you to easily visualize data subsets based on categorical variables (faceting) or to explore pairwise relationships and joint/marginal distributions.

The figure-level functions like `relplot()`, `displot()`, `catplot()`, and `lmplot()` are built on top of these grid objects.

## `FacetGrid`
This is the most general multi-plot grid. It allows you to create a grid of subplots based on the levels of up to three categorical variables (assigned to `row`, `col`, and `hue` arguments). You then map a plotting function to this grid.

[list2tab|#FacetGrid]
- Purpose & Use
    -   To create a matrix of plots where each plot shows a subset of the data defined by the levels of `row` and/or `col` variables.
    -   A `hue` variable can further subdivide data within each facet.
    -   You initialize `FacetGrid` with your data and the faceting variables, then use its `.map()` or `.map_dataframe()` method to apply a plotting function to each subset.
- Key Parameters (`FacetGrid` constructor)
    -   `data`: Pandas DataFrame.
    -   `row`, `col`, `hue`: Column names for faceting variables.
    -   `col_wrap`: "Wrap" the column variable at this width.
    -   `height`: Height of each facet.
    -   `aspect`: Aspect ratio of each facet.
    -   `sharex`, `sharey`: Whether facets share x or y axes.
- `.map(plotting_func, x_var_name, y_var_name_optional, **kwargs)`
    -   Applies `plotting_func` (e.g., `plt.scatter`, `sns.histplot`) to each facet.
- Example (Distribution of tips faceted by 'sex' and 'time')
    -
        ```python
        import seaborn as sns
        import matplotlib.pyplot as plt
        tips = sns.load_dataset("tips")

        # Initialize FacetGrid
        # g = sns.FacetGrid(tips, col="time", row="sex", hue="smoker", margin_titles=True, height=3)
        # Map a plotting function (e.g., histplot for distribution)
        # g.map(sns.histplot, "tip", kde=False, bins=10, alpha=0.7)
        # g.add_legend()
        # g.fig.suptitle("Distribution of Tips (Faceted by Sex and Time)", y=1.03)
        # plt.show()
        ```
    -   This creates a 2x2 grid of histograms (sex on rows, time on columns), with tips for smokers/non-smokers colored differently within each histogram.
    -   **Obsidian Chart Plugin Example:** FacetGrids are collections of multiple plots. It's not feasible to represent the entire grid with a single basic Obsidian Chart block. You'd conceptually describe the individual plots that make up the grid.

## `PairGrid` and `pairplot()`
Used to plot pairwise relationships between multiple variables in a dataset. `pairplot()` is a high-level wrapper for `PairGrid`.

[list2tab|#PairGrid]
- Purpose & Use
    -   Creates a matrix of axes such that each numerical variable in `data` will be shared across the y-axes across a single row and the x-axes across a single column.
    -   The diagonal plots typically show the univariate distribution of each variable (e.g., histogram or KDE).
    -   Off-diagonal plots show the bivariate relationship between pairs of variables (e.g., scatter plot).
- Key Parameters (`PairGrid` / `pairplot`)
    -   `data`: Pandas DataFrame.
    -   `vars`: Variables in `data` to use, otherwise use every column with a numeric datatype.
    -   `hue`: Categorical variable in `data` to map plot aspects to different colors.
    -   `diag_kind`: `{'auto', 'hist', 'kde', None}`. Kind of plot for the diagonal subplots.
    -   `kind`: `{'scatter', 'kde', 'hist', 'reg'}`. Kind of plot for the off-diagonal subplots. (For `pairplot`).
    -   `markers`, `palette`.
- `.map_diag(func, **kwargs)`, `.map_offdiag(func, **kwargs)`, `.map_lower(func, **kwargs)`, `.map_upper(func, **kwargs)`: Methods of `PairGrid` to map specific plotting functions to different parts of the grid.
- Example ([[Scatter_Plot_Matrix|Scatter Plot Matrix]] for e-commerce product features)
    -
        ```python
        import seaborn as sns
        import matplotlib.pyplot as plt
        import pandas as pd
        import numpy as np

        # Conceptual product feature data
        # np.random.seed(42)
        # products_df = pd.DataFrame({
        #     'price': np.random.rand(100) * 100 + 50,
        #     'avg_rating': np.random.rand(100) * 4 + 1,
        #     'num_reviews': np.random.randint(5, 500, 100),
        #     'category': np.random.choice(['Electronics', 'Books', 'Home'], 100)
        # })

        # Create a pairplot
        # sns.pairplot(products_df, hue="category", diag_kind="kde",
        #              plot_kws={'alpha':0.6, 's':40}, # kwargs for off-diagonal plots
        #              diag_kws={'fill':True, 'alpha':0.5}) # kwargs for diagonal plots
        # plt.suptitle("Pairwise Relationships of Product Features by Category (Seaborn pairplot)", y=1.02)
        # plt.show()
        ```
    -   This creates a grid where diagonal plots show KDEs of price, avg_rating, and num_reviews for each category. Off-diagonal plots show scatter plots of each pair of these variables, colored by category.
    -   **Obsidian Chart Plugin Example:** A `pairplot` is a collection of multiple scatter and distribution plots. Not representable as a single basic chart.

## `JointGrid` and `jointplot()`
Used to draw a plot of two variables with bivariate and univariate graphs. `jointplot()` is a high-level wrapper for `JointGrid`.

[list2tab|#JointGrid]
- Purpose & Use
    -   Visualizes the relationship between two numerical variables (bivariate distribution, typically a scatter plot or KDE) along with their individual (univariate) distributions on the marginal axes (typically histograms or KDEs).
- Key Parameters (`JointGrid` / `jointplot`)
    -   `data`, `x`, `y`.
    -   `kind`: `{'scatter', 'kde', 'hist', 'reg', 'resid'}`. Kind of plot for the main joint view.
    -   `hue`: Categorical variable for coloring.
    -   `marginal_ticks`: If True, draw ticks on the marginal axes.
    -   `marginal_kws`: Keyword arguments for the marginal plots.
- `.plot_joint(func, **kwargs)`, `.plot_marginals(func, **kwargs)`: Methods of `JointGrid`.
- Example (Joint distribution of total bill and tip)
    -
        ```python
        import seaborn as sns
        import matplotlib.pyplot as plt
        tips = sns.load_dataset("tips")

        # Joint plot with scatter for joint distribution and histograms for marginals
        # sns.jointplot(data=tips, x="total_bill", y="tip", kind="scatter", # or "kde", "hist", "reg"
        #               marginal_kws=dict(bins=15, fill=True),
        #               hue="smoker", palette="Set2")
        # plt.suptitle("Joint Distribution of Total Bill and Tip (Seaborn jointplot)", y=1.03)
        # plt.show()

        # Another example with KDE
        # sns.jointplot(data=tips, x="total_bill", y="tip", kind="kde", fill=True, cmap="Blues", hue="time")
        # plt.show()
        ```
    -   This plot shows a central scatter plot (or KDE) of total bill vs. tip, with histograms (or KDEs) of total bill along the top margin and tip amounts along the right margin.
    -   **Obsidian Chart Plugin Example:** A `jointplot` is essentially three plots combined (one main bivariate, two marginal univariate). This is hard to represent as a single basic chart. It would be conceptualized as separate, related charts.

Multi-plot grids are extremely useful for comparative analysis and exploring complex datasets by breaking them down into manageable, related views.

---

# Seaborn: Multi-Plot Grids (`FacetGrid`, `PairGrid`, `JointGrid`)

Seaborn provides powerful figure-level interfaces for creating grids of plots. These allow you to easily visualize data subsets based on categorical variables (faceting) or to explore pairwise relationships and joint/marginal distributions.

## `FacetGrid`
-   **Purpose:** The most general multi-plot grid. It allows you to map a dataset onto multiple axes arrayed in a grid of rows and columns that correspond to levels of variables in your dataset.
-   **How it Works:**
    1.  Initialize a `FacetGrid` object with a DataFrame and variables for `row`, `col`, and `hue`.
    2.  Use the `map()` method (or `map_dataframe()`) to apply a plotting function to each subset of the data, drawing a subplot on each facet.
-   **Key Parameters for `FacetGrid()`:**
    -   `data`: Pandas DataFrame.
    -   `row`, `col`: Categorical variables to define the grid rows and columns.
    -   `hue`: Categorical variable for color encoding within each facet.
    -   `col_wrap`: "Wrap" the `col` variable at this width.
    -   `height`, `aspect`: Control size of each facet.
    -   `sharex`, `sharey`: Whether facets share axes.
-   **`FacetGrid.map(plotting_func, "x_col_name", "y_col_name", ...)`:**
    -   `plotting_func`: A function that takes data and keyword arguments (like `color`, `label`) and draws onto the "current" Matplotlib axes (e.g., `plt.scatter`, `sns.histplot`, custom functions).
-   **Use Cases:** Creating conditional views of data, comparing distributions or relationships across many subgroups. The figure-level functions `relplot()`, `displot()`, `catplot()` are built on top of `FacetGrid`.

**Example (Histograms of product ratings faceted by category and region):**
```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Conceptual product data
# np.random.seed(1)
# n_samples = 300
# data_facet = pd.DataFrame({
#     'rating': np.random.uniform(1, 5, n_samples).round(1),
#     'category': np.random.choice(['Electronics', 'Books', 'Apparel'], n_samples),
#     'region': np.random.choice(['North', 'South'], n_samples)
# })

# Create a FacetGrid
# g = sns.FacetGrid(data_facet, col="region", row="category", hue="category", height=3, aspect=1.5, margin_titles=True)
# Map a plotting function (e.g., histplot) to each facet
# g.map(sns.histplot, "rating", kde=False, bins=8) # Pass column name for x-axis
# g.add_legend()
# g.fig.suptitle("Distribution of Product Ratings by Category and Region", y=1.03)
# g.set_axis_labels("Customer Rating", "Frequency")
# plt.tight_layout(rect=[0, 0, 1, 0.97])
# plt.show()
```

## `PairGrid` and `sns.pairplot()`
-   **Purpose:** To plot pairwise relationships between variables in a dataset. `sns.pairplot()` is a high-level wrapper for `PairGrid`.
-   **How it Works:** Creates a matrix of axes such that each variable in `data` will be shared in the y-axis across a single row and in the x-axis across a single column.
    -   **Diagonal:** Typically shows univariate distributions (histogram or KDE) for each variable.
    -   **Off-Diagonal:** Shows bivariate relationships (scatter plots by default) between pairs of variables.
-   **Key Parameters for `pairplot()`:**
    -   `data`: Pandas DataFrame.
    -   `vars`: Variables in `data` to use, otherwise use every column with a numeric datatype.
    -   `hue`: Categorical variable for color encoding.
    -   `kind`: `{'scatter', 'kde', 'hist', 'reg'}`. Kind of plot for the off-diagonal subplots.
    -   `diag_kind`: `{'auto', 'hist', 'kde', None}`. Kind of plot for the diagonal subplots.
    -   `corner`: If `True`, don't draw symmetric (upper triangle) subplots.
-   **Use Cases:** Quickly visualizing all pairwise relationships and individual distributions in a multivariate dataset. Excellent for initial exploratory data analysis. See [[Scatter_Plot_Matrix]].

**Example (`pairplot` for product features):**
```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Conceptual product feature data
# np.random.seed(0)
# data_pair = pd.DataFrame(np.random.rand(100, 4), columns=['price', 'rating', 'weight', 'reviews'])
# data_pair['category'] = np.random.choice(['A', 'B'], 100) # For hue

# Create a pair plot
# sns.pairplot(data_pair, hue="category", diag_kind="kde",
#              plot_kws={'alpha': 0.6, 's': 40, 'edgecolor': 'k'}, # Kws for off-diagonal
#              corner=False) # Show full matrix
# plt.suptitle("Pairwise Relationships of Product Features by Category", y=1.02)
# plt.show()
```

## `JointGrid` and `sns.jointplot()`
-   **Purpose:** To draw a plot of two variables with bivariate and univariate graphs. `sns.jointplot()` is a high-level wrapper for `JointGrid`.
-   **How it Works:** Creates a figure with a main central plot showing the bivariate relationship (e.g., scatter, KDE, hexbin) and marginal plots on the top (x-axis distribution) and right (y-axis distribution).
-   **Key Parameters for `jointplot()`:**
    -   `data`, `x`, `y`: Variables to plot.
    -   `kind`: `{'scatter', 'kde', 'hist', 'reg', 'resid', 'hex'}`. Kind of plot for the main joint view.
    -   `hue`: Categorical variable for color encoding (works with some kinds like 'scatter', 'kde').
    -   `color`: Single color for plot elements.
    -   `marginal_kws`: Dict of arguments for the marginal plots.
    -   `joint_kws`: Dict of arguments for the joint plot.
-   **Use Cases:** Detailed exploration of the relationship between two variables, including their individual distributions.

**Example (`jointplot` for price vs. rating):**
```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Using data_pair from PairGrid example
# np.random.seed(0)
# data_pair = pd.DataFrame(np.random.rand(100, 4), columns=['price', 'rating', 'weight', 'reviews'])
# data_pair['category'] = np.random.choice(['A', 'B'], 100)

# Create a joint plot
# g = sns.jointplot(
#     data=data_pair,
#     x="price",
#     y="rating",
#     hue="category", # Can add hue for some kinds
#     kind="kde",     # Bivariate KDE in center, univariate KDEs on margins
#     fill=True,
#     height=6
# )
# g.fig.suptitle("Joint Distribution of Price and Rating by Category", y=1.03)
# plt.tight_layout(rect=[0, 0, 1, 0.97])
# plt.show()

# Another example with kind="reg"
# sns.jointplot(data=data_pair, x="price", y="rating", kind="reg",
#               joint_kws={'scatter_kws': {'s': 30, 'alpha': 0.5}},
#               marginal_kws={'bins': 15, 'kde': True}, height=6)
# plt.suptitle("Joint Plot with Regression and Marginal Hist/KDEs", y=1.02)
# plt.show()
```

Seaborn's multi-plot grids provide a structured and powerful way to create complex visualizations that reveal deeper insights by conditioning on or comparing across different subsets of data. They automate much of the subplot creation and linking logic that would be manual with Matplotlib alone.

---