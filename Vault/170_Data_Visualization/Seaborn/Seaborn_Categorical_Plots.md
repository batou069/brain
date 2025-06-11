---
tags:
  - seaborn
  - python
  - plotting
  - data_visualization
  - categorical_plots
  - boxplot
  - violinplot
  - barplot
  - countplot
  - stripplot
  - swarmplot
  - chart
  - concept
  - example
  - pointplot
  - catplot
aliases:
  - Seaborn Categorical Data Visualization
  - sns.catplot
  - sns.boxplot
  - sns.violinplot
  - sns.barplot
  - sns.countplot
related:
  - "[[170_Data_Visualization/Seaborn/_Seaborn_MOC|_Seaborn_MOC]]"
  - "[[Categorical_vs_Numerical_Data_Visualization]]"
  - "[[Box_Plot]]"
  - "[[Violin_Plot]]"
  - "[[Bar_Chart]]"
  - "[[_Pandas_MOC]]"
worksheet:
  - WS_DataViz_1
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Seaborn: Categorical Plots (`boxplot`, `violinplot`, `barplot`, etc. & `catplot`)

Seaborn excels at visualizing relationships involving categorical data. These plots help compare numerical distributions or estimates across different categories. `catplot()` is the figure-level interface.

## Types of Categorical Plots

### 1. Categorical Scatterplots
Show individual observations.
-   **`stripplot()`**: Basic categorical scatter.
-   **`swarmplot()`**: Non-overlapping categorical scatter.

[list2tab|#Cat Scatter]
- `stripplot`
    - **Purpose:** Show distribution with individual points, jitter helps with overlap.
    - **Example (Tip amount by day):**
        ```python
        import seaborn as sns
        import matplotlib.pyplot as plt
        tips = sns.load_dataset("tips")
        plt.figure(figsize=(8, 6))
        sns.stripplot(x="day", y="tip", data=tips, jitter=0.2, hue="sex", dodge=True, palette="Set2")
        plt.title("Tip Amounts by Day (Strip Plot - Seaborn)")
        # plt.show()
        ```
    -   **Obsidian Chart Plugin Example (Illustrative Strip Plot - simplified):**
        > [!note] This chart simplifies; Seaborn's `stripplot` handles jitter and hue more gracefully.
        ```chart
        type: scatter
        datasets:
          - label: 'Thur - Male' # Conceptual data, actual stripplot shows individual points
            data: [ {x: 'Thur', y: 2.0}, {x: 'Thur', y: 2.5}, {x: 'Thur', y: 1.5} ]
            backgroundColor: 'rgba(100, 150, 255, 0.7)'
          - label: 'Thur - Female'
            data: [ {x: 'Thur', y: 2.2}, {x: 'Thur', y: 1.8} ]
            backgroundColor: 'rgba(255, 100, 150, 0.7)'
          - label: 'Fri - Male'
            data: [ {x: 'Fri', y: 3.0}, {x: 'Fri', y: 2.0} ]
            backgroundColor: 'rgba(100, 200, 100, 0.7)'
        options:
          title: { display: true, text: 'Illustrative Strip Plot: Tip by Day' }
          scales: { y: { title: { display: true, text: 'Tip ($)' } } }
        ```
- `swarmplot`
    - **Purpose:** Non-overlapping points, better reveals distribution shape.
    - **Example (Total bill by time):**
        ```python
        import seaborn as sns
        import matplotlib.pyplot as plt
        tips = sns.load_dataset("tips")
        plt.figure(figsize=(8, 6))
        sns.swarmplot(x="time", y="total_bill", data=tips, hue="smoker", dodge=True, palette="coolwarm")
        plt.title("Total Bill by Time (Swarm Plot - Seaborn)")
        # plt.show()
        ```
    -   **Obsidian Chart Plugin Example:** Swarm plots are hard to replicate simply with basic chart types. The key is the non-overlapping nature. A scatter plot with carefully positioned points would be needed.

### 2. Categorical Distribution Plots
Abstract representations of distributions.
-   **`boxplot()` ([[Box_Plot]]):** Quartiles, median, outliers.
-   **`violinplot()` ([[Violin_Plot]]):** Box plot + KDE.
-   **`boxenplot()`:** Enhanced box plot for larger datasets.

[list2tab|#Cat Dist]
- `boxplot`
    - **Purpose:** Compare distributions across categories using quartiles.
    - **Example (Total bill by day):**
        ```python
        import seaborn as sns
        import matplotlib.pyplot as plt
        tips = sns.load_dataset("tips")
        plt.figure(figsize=(8, 6))
        sns.boxplot(x="day", y="total_bill", data=tips, hue="time", palette="pastel")
        plt.title("Total Bill by Day & Time (Box Plot - Seaborn)")
        # plt.show()
        ```    -   **Obsidian Chart Plugin Example (Illustrative Box Plot):**
        > [!note] Obsidian Charts has direct box plot support. Data format is `[min, q1, median, q3, max]`. Outliers would need separate scatter datasets if desired.
        ```chart
        type:boxplot
        labels: ['Thur-Lunch', 'Thur-Dinner', 'Fri-Lunch', 'Fri-Dinner'] # Conceptual combined categories
        datasets:
          - label: 'Total Bill'
            backgroundColor: 'rgba(255, 99, 132, 0.5)'
            borderColor: 'rgb(255, 99, 132)'
            borderWidth: 1
            data: [
              [10, 15, 20, 25, 30], # Min, Q1, Median, Q3, Max for Thur-Lunch
              [15, 22, 28, 35, 45], # Thur-Dinner
              [8, 12, 16, 20, 24],  # Fri-Lunch
              [12, 18, 25, 33, 50]  # Fri-Dinner
            ]
        options:
          title: { display: true, text: 'Illustrative Box Plot: Total Bill' }
          scales: { y: { title: { display: true, text: 'Total Bill ($)' } } }
        ```
- `violinplot`
    - **Purpose:** Shows distribution shape (KDE) along with box plot elements.
    - **Example (Tip amount by sex, split by smoker):**
        ```python
        import seaborn as sns
        import matplotlib.pyplot as plt
        tips = sns.load_dataset("tips")
        plt.figure(figsize=(8, 6))
        sns.violinplot(x="sex", y="tip", data=tips, hue="smoker", split=True, palette="muted", inner="quartile")
        plt.title("Tip Distribution by Sex & Smoker (Violin Plot - Seaborn)")
        # plt.show()
        ```
    -   **Obsidian Chart Plugin Example:** Violin plots are complex. A simplified representation might involve overlaid KDEs (as line charts) or a textual description of what it shows. True violin shape isn't a standard Chart.js type.

### 3. Categorical Estimate Plots
Show point estimates and confidence intervals.
-   **`barplot()` ([[Bar_Chart]]):** Mean (default) and CI as bars.
-   **`pointplot()`:** Point estimates and CIs with lines. Good for interactions.
-   **`countplot()`:** Counts of observations in categories.

[list2tab|#Cat Est]
- `barplot`
    - **Purpose:** Show central tendency and confidence interval.
    - **Example (Average tip by day):**
        ```python
        import seaborn as sns
        import matplotlib.pyplot as plt
        tips = sns.load_dataset("tips")
        plt.figure(figsize=(8, 6))
        sns.barplot(x="day", y="tip", data=tips, hue="sex", palette="viridis", errorbar=('ci', 95))
        plt.title("Average Tip by Day & Sex (Bar Plot - Seaborn)")
        # plt.show()
        ```
    -   **Obsidian Chart Plugin Example (Illustrative Bar Plot for Averages):**
        > [!note] Seaborn's barplot automatically computes means and CIs. This chart shows pre-calculated means. Error bars are not directly supported in basic Obsidian Charts bar type.
        ```chart
        type: bar
        labels: ['Thur', 'Fri', 'Sat', 'Sun']
        datasets:
          - label: 'Avg Tip - Male'
            data: [2.9, 2.7, 3.1, 3.2] # Conceptual average tip values
            backgroundColor: 'rgba(75, 192, 192, 0.7)'
          - label: 'Avg Tip - Female'
            data: [2.6, 2.8, 2.9, 3.0] # Conceptual average tip values
            backgroundColor: 'rgba(255, 159, 64, 0.7)'
        options:
          title: { display: true, text: 'Illustrative Bar Plot: Average Tip by Day & Sex' }
          scales: { y: { title: { display: true, text: 'Average Tip ($)' }, min: 0 } }
        ```
- `countplot`
    - **Purpose:** Show counts of observations per category.
    - **Example (Count of diners by day):**
        ```python
        import seaborn as sns
        import matplotlib.pyplot as plt
        tips = sns.load_dataset("tips")
        plt.figure(figsize=(8, 6))
        sns.countplot(x="day", data=tips, hue="time", palette="Set1")
        plt.title("Number of Diners by Day & Time (Count Plot - Seaborn)")
        # plt.show()
        ```
    -   **Obsidian Chart Plugin Example (Illustrative Count Plot):**
        ```chart
        type: bar
        labels: ['Thur', 'Fri', 'Sat', 'Sun']
        datasets:
          - label: 'Lunch Count'
            data: [60, 15, 0, 0]  # Conceptual counts
            backgroundColor: 'rgba(201, 203, 207, 0.7)'
          - label: 'Dinner Count'
            data: [2, 10, 87, 76] # Conceptual counts
            backgroundColor: 'rgba(255, 205, 86, 0.7)'
        options:
          title: { display: true, text: 'Illustrative Count Plot: Diners by Day & Time' }
          scales: { y: { title: { display: true, text: 'Count' }, beginAtZero: true } }
        ```

## `catplot()` (Figure-level Interface)
Combines these categorical plots with `FacetGrid`.
-   `kind`: `{'strip', 'swarm', 'box', 'violin', 'boxen', 'point', 'bar', 'count'}`.

**Example (Faceted box plots - Chart not easily represented here):**
```python
import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset("tips")

g = sns.catplot(
    x="day", y="total_bill",
    kind="box",
    col="time", row="smoker",
    data=tips,
    height=3, aspect=1.1, palette="husl"
)
# plt.show()
```
> A `catplot` creating a grid of plots is complex for a single Obsidian Chart.

Seaborn's categorical plots offer powerful ways to explore data with categorical dimensions.

---

# Seaborn: Categorical Plots (`catplot` and axes-level functions)

Seaborn excels at visualizing relationships that involve one or more categorical variables. The `catplot()` function is a figure-level interface for accessing several axes-level functions that show the relationship between a numerical and one or more categorical variables or the distribution of a numerical variable across categories.

## Main Categories of Categorical Plots (accessed via `kind` in `catplot` or directly)

[list2tab|#Categorical Plot Kinds]
- Categorical Scatterplots
    - **Purpose:** Show the distribution of a numerical variable for each category, displaying individual data points.
    - **Functions:**
        -   **`sns.stripplot()` / `catplot(kind="strip")`:** Draws a scatter plot where one variable is categorical. Can add jitter to avoid overlapping points.
        -   **`sns.swarmplot()` / `catplot(kind="swarm")`:** Similar to a strip plot, but points are adjusted along the categorical axis so that they don't overlap. Gives a better representation of the distribution, especially for smaller datasets. Can be computationally intensive for large datasets.
    - **Example (Product ratings by category using stripplot):**
        ```python
        import seaborn as sns
        import matplotlib.pyplot as plt
        import pandas as pd
        import numpy as np

        # Conceptual product data: ratings and category
        # np.random.seed(42)
        # ratings_data_cat = pd.DataFrame({
        #     'rating': np.concatenate([np.random.normal(4.2, 0.5, 50).clip(1,5),
        #                               np.random.normal(3.8, 0.8, 40).clip(1,5),
        #                               np.random.normal(4.5, 0.3, 60).clip(1,5)]),
        #     'category': ['Electronics'] * 50 + ['Books'] * 40 + ['Apparel'] * 60,
        #     'is_new_product': np.random.choice([True, False], 150) # For hue
        # })

        # plt.figure(figsize=(10, 6))
        # sns.stripplot(data=ratings_data_cat, x="category", y="rating", hue="is_new_product", jitter=0.1, dodge=True, palette="Set2")
        # plt.title("Product Ratings by Category (Strip Plot with Jitter & Hue)")
        # plt.ylabel("Customer Rating (1-5)")
        # plt.xlabel("Product Category")
        # plt.show()

        # Using swarmplot
        # plt.figure(figsize=(10, 6))
        # sns.swarmplot(data=ratings_data_cat, x="category", y="rating", hue="is_new_product", dodge=True, palette="husl", s=4) # s for size
        # plt.title("Product Ratings by Category (Swarm Plot with Hue)")
        # plt.ylabel("Customer Rating (1-5)")
        # plt.xlabel("Product Category")
        # plt.show()
        ```
- Categorical Distribution Plots
    - **Purpose:** Show an abstract representation of the distribution of a numerical variable for each category.
    - **Functions:**
        -   **`sns.boxplot()` / `catplot(kind="box")`:** Classic [[Box_Plot|box-and-whisker plot]]. Shows median, quartiles, whiskers, and outliers.
        -   **`sns.violinplot()` / `catplot(kind="violin")`:** Combines a box plot with a [[Kernel_Density_Estimation_KDE|Kernel Density Estimate (KDE)]]. Shows distribution shape. Can include inner boxplot or quartiles.
        -   **`sns.boxenplot()` / `catplot(kind="boxen")`:** (Letter-value plot) Enhanced box plot for larger datasets, showing more quantiles.
    - **Example (Product price distribution by category using violinplot):**
        ```python
        # Conceptual product data
        # np.random.seed(1)
        # price_data_cat = pd.DataFrame({
        #     'price': np.concatenate([np.random.lognormal(np.log(150), 0.5, 70),
        #                              np.random.lognormal(np.log(30), 0.3, 50),
        #                              np.random.lognormal(np.log(80), 0.4, 60)]).clip(5, 1000),
        #     'category': ['Electronics'] * 70 + ['Books'] * 50 + ['Apparel'] * 60
        # })

        # plt.figure(figsize=(10, 6))
        # sns.violinplot(data=price_data_cat, x="category", y="price", hue="category", palette="muted", inner="quartile", legend=False)
        # plt.title("Product Price Distribution by Category (Violin Plot)")
        # plt.ylabel("Price ($)")
        # plt.xlabel("Product Category")
        # plt.yscale('log') # Prices are often skewed
        # plt.show()
        ```
- Categorical Estimate Plots
    - **Purpose:** Show a central tendency estimate (e.g., mean, median) and confidence interval for a numerical variable within each category.
    - **Functions:**
        -   **`sns.barplot()` / `catplot(kind="bar")`:** Represents an estimate of central tendency for a numeric variable with the height of each rectangle and provides some indication of the uncertainty around that estimate using error bars (typically confidence intervals).
        -   **`sns.pointplot()` / `catplot(kind="point")`:** Shows point estimates and confidence intervals using scatter plot glyphs. Good for comparing changes in levels of one categorical variable across another.
        -   **`sns.countplot()` / `catplot(kind="count")`:** Shows the counts of observations in each categorical bin using bars (essentially a histogram for categorical data). Only requires `x` or `y` (not both).
    - **Example (Average customer rating per product category using barplot):**
        ```python
        # Using ratings_data_cat from the stripplot example
        # plt.figure(figsize=(10, 6))
        # sns.barplot(data=ratings_data_cat, x="category", y="rating", hue="is_new_product", palette="coolwarm", errorbar=('ci', 95))
        # plt.title("Average Customer Rating by Product Category and New Status")
        # plt.ylabel("Average Rating (1-5)")
        # plt.xlabel("Product Category")
        # plt.ylim(0, 5.5)
        # plt.show()

        # Example with countplot for 'category'
        # plt.figure(figsize=(8, 5))
        # sns.countplot(data=ratings_data_cat, x="category", hue="is_new_product", palette="viridis")
        # plt.title("Number of Products per Category by New Status")
        # plt.ylabel("Count")
        # plt.xlabel("Product Category")
        # plt.show()
        ```

## `sns.catplot()` (Figure-level Interface)
-   **Purpose:** A figure-level interface for drawing categorical plots onto a `FacetGrid`. It unifies access to the axes-level functions mentioned above via the `kind` parameter.
-   **Key Parameters:**
    -   `data`, `x`, `y`, `hue`, `palette`: Similar to axes-level functions.
    -   `kind`: `{'strip', 'swarm', 'box', 'violin', 'boxen', 'point', 'bar', 'count'}`.
    -   `row`, `col`, `col_wrap`: For faceting.
    -   `height`, `aspect`: Control size of each facet.
-   **Use Cases:** Creating complex visualizations with multiple subplots (facets) showing categorical relationships for different subsets of data.

**Example (Faceted box plots using `catplot`):**
```python
# Using ratings_data_cat from stripplot example, adding a 'region' column
# np.random.seed(99)
# ratings_data_cat['region'] = np.random.choice(['North', 'South'], 150)

# g = sns.catplot(
#     data=ratings_data_cat,
#     x="category",
#     y="rating",
#     hue="is_new_product",
#     col="region",          # Facet by region
#     kind="box",            # Plot box plots
#     palette="pastel",
#     height=5, aspect=0.8
# )
# g.fig.suptitle("Product Ratings by Category, New Status, and Region", y=1.03)
# g.set_axis_labels("Product Category", "Customer Rating (1-5)")
# plt.tight_layout(rect=[0, 0, 1, 0.97])
# plt.show()
```

Seaborn's categorical plots are highly effective for understanding how numerical distributions or estimates vary across different groups defined by one or more categorical variables. They often provide more insight than simple summary statistics alone.

---