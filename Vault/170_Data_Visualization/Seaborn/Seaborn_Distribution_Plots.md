---
tags:
  - seaborn
  - python
  - plotting
  - data_visualization
  - distribution_plots
  - histogram
  - kdeplot
  - ecdfplot
  - chart
  - concept
  - example
  - kde
  - ecdf
  - displot
aliases:
  - Seaborn Distribution Visualization
  - sns.histplot
  - sns.kdeplot
  - sns.ecdfplot
  - sns.displot
  - Seaborn Histograms
  - Seaborn KDE
  - Seaborn ECDF
related:
  - "[[170_Data_Visualization/Seaborn/_Seaborn_MOC|_Seaborn_MOC]]"
  - "[[Histogram]]"
  - "[[Kernel_Density_Estimate_KDE|Kernel Density Estimate (KDE)]]"
  - "[[Cumulative_Distribution_Function_CDF|Empirical CDF (ECDF)]]"
  - "[[_Pandas_MOC]]"
  - "[[Matplotlib_Overview]]"
  - "[[_Pandas_MOC|Pandas DataFrame]]"
  - "[[Kernel_Density_Estimation_KDE|Kernel Density Estimation (KDE)]]"
worksheet:
  - WS_DataViz_1
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Seaborn: Distribution Plots (`histplot`, `kdeplot`, `ecdfplot`, `displot`)

Seaborn provides several functions to visualize the distribution of a dataset, either for a single variable (univariate) or for two variables (bivariate). These plots help in understanding the central tendency, spread, shape (skewness, modality), and potential outliers of the data.

The figure-level interface for these plots is `displot()`.

## `histplot()` ([[Histogram]])
Visualizes the distribution by showing counts of observations falling within discrete bins.

[list2tab|#histplot]
- Purpose & Use
    -   Understand frequency distribution of numerical data.
    -   Can use `hue` for subgroups, `kde` for density overlay.
- Key Parameters
    -   `data`, `x`, `y`, `hue`, `bins`, `kde`, `stat`, `multiple`, `element`, `cumulative`.
- Example (Distribution of total bill amounts from e-commerce transactions)
    -
        ```python
        import seaborn as sns
        import matplotlib.pyplot as plt
        tips = sns.load_dataset("tips")

        plt.figure(figsize=(8, 6))
        sns.histplot(data=tips, x="total_bill", hue="time", kde=True, element="step")
        plt.title("Distribution of Total Bill by Time (Seaborn)")
        plt.xlabel("Total Bill ($)")
        plt.ylabel("Frequency / Density")
        # plt.show()
        ```
    -   Shows histograms for total bills, separated by 'time', with KDEs.
    -   **Obsidian Chart Plugin Example (Illustrative Histogram):**
        > [!note] This chart simplifies; Seaborn's `histplot` with `hue` and `kde` is richer. This shows a basic histogram concept.
        ```chart
        type: bar # Histograms are bar charts of binned data
        labels: ['10-20', '20-30', '30-40', '40-50'] # Conceptual Bins for total_bill
        datasets:
          - label: 'Lunch Bills'
            data: # Conceptual counts for Lunch
            backgroundColor: 'rgba(255, 99, 132, 0.5)'
          - label: 'Dinner Bills'
            data: # Conceptual counts for Dinner
            backgroundColor: 'rgba(54, 162, 235, 0.5)'
        options:
          title:
            display: true
            text: 'Illustrative Histogram: Total Bill by Time'
          scales:
            x:
              title:
                display: true
                text: 'Total Bill Bins ($)'
              stacked: false # Set to true for stacked histogram
            y:
              title:
                display: true
                text: 'Frequency'
              stacked: false
        ```

## `kdeplot()` ([[Kernel_Density_Estimate_KDE|Kernel Density Estimate]])
Plots a smoothed representation of the data's distribution.

[list2tab|#kdeplot]
- Purpose & Use
    -   Visualize probability density of continuous variables.
    -   Good for observing distribution shape (modality, skewness).
    -   Can do bivariate KDEs (contour plots).
- Key Parameters
    -   `data`, `x`, `y`, `hue`, `fill`, `bw_method`, `levels`, `cumulative`.
- Example (Density of tip amounts)
    -
        ```python
        import seaborn as sns
        import matplotlib.pyplot as plt
        tips = sns.load_dataset("tips")

        plt.figure(figsize=(8, 6))
        sns.kdeplot(data=tips, x="tip", hue="sex", fill=True, alpha=0.5, linewidth=2)
        plt.title("Density of Tip Amounts by Sex (Seaborn)")
        plt.xlabel("Tip Amount ($)")
        plt.ylabel("Density")
        # plt.show()
        ```
    -   Shows smoothed density curves for tip amounts, separated by 'sex'.
    -   **Obsidian Chart Plugin Example (Illustrative KDE - simplified as line chart):**
        > [!note] True KDE involves smoothing. This chart uses line segments for a conceptual representation. Seaborn's `kdeplot` provides the actual smoothing.
        ```chart
        type: line
        labels: # Conceptual Tip Amounts
        datasets:
          - label: 'Male Tip Density'
            data: [0.1, 0.3, 0.5, 0.4, 0.2, 0.1, 0.05, 0.02, 0.01, 0.0] # Conceptual density values
            borderColor: 'rgba(75, 192, 192, 1)'
            backgroundColor: 'rgba(75, 192, 192, 0.2)'
            fill: true
            tension: 0.4
          - label: 'Female Tip Density'
            data: [0.05, 0.2, 0.4, 0.6, 0.3, 0.15, 0.08, 0.03, 0.01, 0.0] # Conceptual density values
            borderColor: 'rgba(255, 159, 64, 1)'
            backgroundColor: 'rgba(255, 159, 64, 0.2)'
            fill: true
            tension: 0.4
        options:
          title:
            display: true
            text: 'Illustrative KDE: Tip Density by Sex'
          scales:
            y:
              title:
                display: true
                text: 'Density'
            x:
              title:
                display: true
                text: 'Tip Amount ($)'
        ```

## `ecdfplot()` ([[Cumulative_Distribution_Function_CDF|Empirical Cumulative Distribution Function]])
Plots the proportion of data points less than or equal to a given value.

[list2tab|#ecdfplot]
- Purpose & Use
    -   Visualize cumulative distribution, understand percentiles.
    -   Less sensitive to binning than histograms.
- Key Parameters
    -   `data`, `x`, `y`, `hue`, `stat`, `complementary`.
- Example (ECDF of total bill amounts)
    -
        ```python
        import seaborn as sns
        import matplotlib.pyplot as plt
        tips = sns.load_dataset("tips")

        plt.figure(figsize=(8, 6))
        sns.ecdfplot(data=tips, x="total_bill", hue="day")
        plt.title("ECDF of Total Bill by Day (Seaborn)")
        plt.xlabel("Total Bill ($)")
        plt.ylabel("Proportion (ECDF)")
        # plt.show()
        ```
    -   Shows how the proportion of bills accumulates for different total bill amounts, by day.
    -   **Obsidian Chart Plugin Example (Illustrative ECDF):**
        ```chart
        type: line
        labels: # Conceptual Total Bill values
        datasets:
          - label: 'Thur ECDF'
            data: [0.05, 0.15, 0.30, 0.50, 0.70, 0.85, 0.92, 0.97, 0.99, 1.0] # Conceptual ECDF values
            borderColor: 'rgba(153, 102, 255, 1)'
            fill: false
            stepped: true # ECDFs are step functions
          - label: 'Fri ECDF'
            data: [0.1, 0.25, 0.45, 0.65, 0.80, 0.90, 0.95, 0.98, 1.0, 1.0] # Conceptual ECDF values
            borderColor: 'rgba(255, 205, 86, 1)'
            fill: false
            stepped: true
        options:
          title:
            display: true
            text: 'Illustrative ECDF: Total Bill by Day'
          scales:
            y:
              min: 0
              max: 1
              title:
                display: true
                text: 'Proportion (ECDF)'
            x:
              title:
                display: true
                text: 'Total Bill ($)'
        ```

## `displot()` (Figure-level Interface)
Figure-level function for drawing distribution plots (`histplot`, `kdeplot`, `ecdfplot`) onto a `FacetGrid`.
-   `kind`: `{'hist', 'kde', 'ecdf'}`.
-   `row`, `col`: Categorical variables for faceting.

**Example (Faceted histograms - Chart not easily represented here):**
```python
import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset("tips")

g = sns.displot(
    data=tips, x="total_bill",
    col="time", row="sex",
    kind="hist", kde=True,
    height=3, aspect=1.2
)
g.fig.suptitle("Distribution of Total Bill (Faceted - Seaborn)", y=1.03)
# plt.show()```
> A `displot` creating a grid of histograms is complex for a single Obsidian Chart. It represents multiple individual histogram/KDE plots.

Distribution plots are essential for initial data exploration.

---

# Seaborn: Distribution Plots (`histplot`, `kdeplot`, `ecdfplot`, `displot`)

Seaborn provides several functions for visualizing the distribution of univariate or bivariate data. These plots help in understanding the shape, central tendency, spread, and potential multimodality of datasets. The main functions are `histplot()`, `kdeplot()`, and `ecdfplot()`, which can also be accessed via the figure-level interface `displot()`.

## `sns.histplot()`
-   **Purpose:** To plot histograms, which represent the distribution of a dataset by dividing the data range into bins and showing the frequency (or density/probability) of observations falling into each bin.
-   **Key Parameters:**
    -   `data`: Pandas DataFrame or NumPy array.
    -   `x`, `y`: Variables for univariate or bivariate histograms. If `y` is provided, a 2D histogram (or heatmap) is created.
    -   `hue`: Semantic variable that is mapped to determine the color of plot elements.
    -   `bins`: Specification of hist bins. Can be an integer (number of bins), a list of bin edges, or a string (e.g., 'auto').
    -   `stat`: Aggregate statistic to compute in each bin (`'count'`, `'frequency'`, `'density'`, `'probability'`).
    -   `kde`: If `True`, compute a kernel density estimate to smooth the histogram.
    -   `element`: `{'bars', 'step', 'poly'}`. Visual representation of the histogram.
    -   `cumulative`: If `True`, plot the cumulative histogram.
    -   `multiple`: `{'layer', 'dodge', 'stack', 'fill'}`. Approach to resolving multiple elements when `hue` is used.
-   **Use Cases:** Understanding the underlying frequency distribution of a set of continuous or discrete data points.

**Example (Distribution of product prices):**
```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Conceptual product data
# np.random.seed(10)
# product_prices = np.random.lognormal(mean=np.log(100), sigma=0.5, size=500) # Skewed data
# product_prices = product_prices[product_prices < 1000] # Cap extreme values for better viz
# price_df = pd.DataFrame({'price': product_prices})

# plt.figure(figsize=(10, 6))
# sns.histplot(data=price_df, x="price", bins=30, kde=True, color="skyblue")
# plt.title("Distribution of Product Prices")
# plt.xlabel("Price ($)")
# plt.ylabel("Frequency")
# plt.show()
```

## `sns.kdeplot()` (Kernel Density Estimate)
-   **Purpose:** To plot the probability density function (PDF) of a continuous variable, estimated using a kernel density estimate. It provides a smoothed representation of the data's distribution.
-   **Key Parameters:**
    -   `data`, `x`, `y`, `hue`: Similar to `histplot`. Can plot 1D or 2D KDEs.
    -   `bw_method`: Method for determining the smoothing bandwidth (e.g., 'scott', 'silverman', or a scalar).
    -   `fill`: If `True`, fill the area under the KDE curve.
    -   `cumulative`: If `True`, plot the cumulative distribution function.
    -   `levels`: Number of contour levels or list of levels for 2D KDE.
-   **Use Cases:** Visualizing the shape of a distribution, identifying modes, comparing distributions smoothly.

**Example (KDE of customer ratings):**
```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Conceptual customer ratings for two product categories
# np.random.seed(42)
# ratings_electronics = np.random.normal(loc=4.2, scale=0.5, size=200).clip(1, 5)
# ratings_books = np.random.normal(loc=3.8, scale=0.8, size=150).clip(1, 5)
# ratings_data = pd.DataFrame({
#     'rating': np.concatenate([ratings_electronics, ratings_books]),
#     'category': ['Electronics'] * 200 + ['Books'] * 150
# })

# plt.figure(figsize=(10, 6))
# sns.kdeplot(data=ratings_data, x="rating", hue="category", fill=True, alpha=0.5, linewidth=2)
# plt.title("Distribution of Customer Ratings by Product Category (KDE)")
# plt.xlabel("Customer Rating (1-5)")
# plt.ylabel("Density")
# plt.legend(title="Category")
# plt.show()
```

## `sns.ecdfplot()` (Empirical Cumulative Distribution Function)
-   **Purpose:** To plot the empirical cumulative distribution function (ECDF). For each value on the x-axis, the ECDF shows the proportion of data points that are less than or equal to that value.
-   **Key Parameters:**
    -   `data`, `x`, `y` (for bivariate ECDF, less common), `hue`.
    -   `stat`: `{'proportion', 'count'}`. Whether to show proportions or counts on the y-axis.
    -   `complementary`: If `True`, plot the complementary CDF (1 - ECDF).
-   **Use Cases:** Understanding probabilities, comparing distributions in terms of quantiles, checking for dominance between distributions.

**Example (ECDF of product sales volume):**
```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Conceptual sales volume data
# np.random.seed(123)
# sales_volumes = np.random.poisson(lam=50, size=300) # Number of units sold
# sales_df = pd.DataFrame({'volume': sales_volumes})

# plt.figure(figsize=(10, 6))
# sns.ecdfplot(data=sales_df, x="volume", stat="proportion")
# plt.title("ECDF of Product Sales Volume")
# plt.xlabel("Sales Volume (Units)")
# plt.ylabel("Proportion of Products")
# plt.grid(True, linestyle=':')
# plt.show()
```

## `sns.displot()` (Figure-level Interface)
-   **Purpose:** A figure-level interface for drawing distribution plots onto a `FacetGrid`. It can produce histograms, KDE plots, or ECDF plots, and allows for faceting by other variables.
-   **Key Parameters:**
    -   `data`, `x`, `y`, `hue`: Similar to the axes-level functions.
    -   `kind`: `{'hist', 'kde', 'ecdf'}` (default 'hist'). Specifies the type of plot.
    -   `rug`: If `True`, show a rug plot on the x-axis (small ticks for each data point).
    -   `row`, `col`, `col_wrap`: For faceting.
    -   Other parameters specific to `histplot`, `kdeplot`, or `ecdfplot` can be passed.
-   **Use Cases:** Quickly visualizing distributions for different subsets of data or comparing different types of distribution plots.

**Example (Faceted Histograms using `displot`):**
```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Using ratings_data from KDE example
# np.random.seed(42)
# ratings_electronics = np.random.normal(loc=4.2, scale=0.5, size=200).clip(1, 5)
# ratings_books = np.random.normal(loc=3.8, scale=0.8, size=150).clip(1, 5)
# ratings_apparel = np.random.normal(loc=4.0, scale=0.6, size=180).clip(1, 5) # Added another category
# ratings_data = pd.DataFrame({
#     'rating': np.concatenate([ratings_electronics, ratings_books, ratings_apparel]),
#     'category': ['Electronics'] * 200 + ['Books'] * 150 + ['Apparel'] * 180
# })

# Create faceted histograms for each category
# g = sns.displot(
#     data=ratings_data,
#     x="rating",
#     col="category",   # Facet by category
#     kind="hist",      # Plot histograms
#     kde=True,         # Add KDE overlay
#     col_wrap=2,       # Wrap columns after 2 plots
#     height=4, aspect=1.2
# )
# g.fig.suptitle("Distribution of Customer Ratings (Faceted by Category)", y=1.03)
# g.set_axis_labels("Customer Rating (1-5)", "Frequency")
# plt.tight_layout(rect=[0, 0, 1, 0.97])
# plt.show()
```

Seaborn's distribution plots provide comprehensive tools for understanding and comparing the distributions of variables in your dataset, often with convenient options for semantic mapping (`hue`) and faceting.

---