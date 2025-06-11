
Filename: 170_Data_Visualization/Plot_Types/Box_Plot.md
````markdown
[[Box_Plot]]
````

`````markdown

Filename: 170_Data_Visualization/Plot_Types/Pie_Chart.md````markdown
[[Pie_Chart]]
````

`````markdown

Filename: 170_Data_Visualization/Plot_Types/Heatmap.md
````markdown
---
tags: [data_visualization, plotting, heatmap, matrix, correlation, concept, chart]
aliases: [Heat Map, Density Heatmap]
related:
  - "[[Matplotlib_Image_Display_imshow]]" # imshow is often used to create heatmaps
  - "[[Seaborn_Matrix_Plots]]" # sns.heatmap
  - "[[Choosing_the_Right_Plot]]"
  - "[[Correlation_Matrix_Visualization]]"
worksheet: [WS_DataViz_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Heatmap

## Definition
A **heatmap** is a graphical representation of data where values in a matrix are represented as colors. It's a 2D visualization technique that uses a color scale to show the magnitude of a phenomenon across two discrete variables or dimensions.

Larger values are typically represented by darker or more intense colors, while smaller values are represented by lighter or less intense colors (or vice-versa, depending on the chosen colormap and context).

## Key Characteristics
-   **Matrix Data:** Input is typically a 2D array or matrix.
-   **Color Encoding:** Values in the matrix cells are mapped to colors using a [[Matplotlib_Colormaps|colormap]].
-   **Grid Structure:** The plot consists of colored cells arranged in a grid, corresponding to the rows and columns of the input matrix.
-   **Annotations (Optional):** Numerical values can be displayed within each cell for precise information.
-   **Clustering (Optional):** Rows and/or columns can be reordered using hierarchical clustering to group similar items together, often revealing patterns (see [[Seaborn_Matrix_Plots|`sns.clustermap`]]).

## Purpose
-   **Visualizing Matrices of Values:** To get an intuitive overview of the magnitude of values across a 2D grid.
-   **Identifying Patterns and Clusters:** Patterns, clusters, highs, and lows often become visually apparent through color variations.
-   **[[Correlation_Matrix_Visualization|Visualizing Correlation Matrices]]:** A very common use case to quickly see relationships between many variables.
-   **Showing Co-occurrence or Interaction:** For example, user-item interaction matrices in recommendation systems.
-   **Displaying Confusion Matrices:** In classification, to see how well a model predicts different classes.

## When to Use
-   When you have a 2D matrix of numerical values and want to visualize their magnitudes and patterns.
-   For exploring relationships in correlation matrices.
-   When comparing values across two categorical dimensions (after aggregating data into a matrix, e.g., a pivot table).
-   For visualizing genomic data, web traffic by time/day, etc.

## Matplotlib & Seaborn Implementation
-   **Matplotlib:** `plt.imshow(data_matrix, cmap=..., ...)` or `ax.imshow(...)` is the fundamental function. Additional work is needed for labels, colorbar, annotations. See [[Matplotlib_Image_Display_imshow]].
-   **Seaborn:** `sns.heatmap(data_matrix, annot=True, cmap=..., fmt=".2f", ...)` provides a high-level interface specifically for creating well-formatted heatmaps with good defaults for annotations, colorbars, etc. `sns.clustermap(...)` adds hierarchical clustering.

## Example Scenario & Chart
>[!question]- For Heatmap: Come up with a scenario where it would be useful. Is this plot the best way to visualize this scenario?
>
>**Scenario:** Visualizing the monthly sales performance (e.g., percentage change from previous month) for different product categories over a year for an e-commerce business. Rows are product categories, columns are months, cell color represents sales performance.
>
>**Usefulness:** A heatmap is highly useful to:
>1.  Quickly identify which product categories performed well or poorly in specific months.
>2.  Spot seasonal trends across categories (e.g., all categories doing well in Q4).
>3.  Compare performance across categories for a given month, or across months for a given category.
>4.  Detect anomalies or unusual performance patterns.
>
>**Is this the best way?**
>Yes, for visualizing this type of matrix data where you want to see patterns of intensity across two discrete dimensions (category and month), a heatmap is an **excellent and standard choice**.
>
>**Alternatives & Complements:**
>-   Multiple [[Line_Plot|line plots]] (one per category, with months on x-axis) could show trends but might become cluttered with many categories. A heatmap handles more categories more cleanly.
>-   [[Bar_Chart|Grouped or stacked bar charts]] could compare categories month by month, but the overall yearly pattern across all categories might be less obvious than in a heatmap.

**Obsidian Chart Plugin Example (Illustrative):**
> [!note] True heatmaps with continuous color scales are not a native Chart.js type that the basic Obsidian Charts plugin directly renders as a single "heatmap" chart type. You could simulate it with a matrix of colored cells, but this is complex. Below is a conceptual representation of the *data* for a heatmap. The visualization relies on mapping values to colors.
>
> A common way to implement heatmaps in Chart.js (which Obsidian Charts uses) is via a `matrix` dataset type if supported by the plugin version, or by using a scatter plot where each point is a large square, and its color is mapped to the value. For simplicity here, I'll describe the data structure.

```
Conceptual Data for Monthly Sales Performance Heatmap (% Change):

Product Category | Jan  | Feb  | Mar  | Apr  | May  | Jun
-----------------|------|------|------|------|------|------
Electronics      | +5%  | +3%  | -1%  | +7%  | +4%  | +2%
Books            | +2%  | +1%  | +0%  | +3%  | +2%  | -1%
Clothing         | -3%  | +8%  | +10% | +5%  | +1%  | -2%
Home Goods       | +4%  | +2%  | +1%  | +2%  | +3%  | +0%

(Imagine this table where each cell's background color intensity corresponds to the percentage value, e.g., dark green for high positive %, dark red for high negative %, white/light yellow for near 0%.)
```

**If a `matrix` chart type were available in Obsidian Charts (hypothetical):**
```chart
// This is HYPOTHETICAL for Obsidian Charts basic plugin
// It shows the data structure one might feed to a heatmap library
type: matrix // Assuming a 'matrix' type existed for heatmaps
datasets: [{
  label: 'Monthly Sales % Change',
  data: [ // Array of arrays representing rows
    [5, 3, -1, 7, 4, 2],  // Electronics
    [2, 1, 0, 3, 2, -1],  // Books
    [-3, 8, 10, 5, 1, -2], // Clothing
    [4, 2, 1, 2, 3, 0]    // Home Goods
  ],
  // Colormap settings would be part of options
}]
options: {
  plugins: { title: { display: true, text: 'Sales Performance Heatmap' } },
  scales: {
    y: {
      labels: ['Electronics', 'Books', 'Clothing', 'Home Goods'],
      title: { display: true, text: 'Product Category' }
    },
    x: {
      labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
      title: { display: true, text: 'Month' }
    }
  },
  // colorScale: { type: 'diverging', mid: 0, min: -10, max: 10, lowColor: 'red', highColor: 'green' } // Conceptual
}
```
> **Actual Implementation:** In Python, `sns.heatmap(df_performance)` would directly render this from a Pandas DataFrame `df_performance`.

---
````

`````markdown

Filename: 170_Data_Visualization/Plot_Types/Violin_Plot.md
````markdown
---
tags: [data_visualization, plotting, violin_plot, distribution, categorical_data, concept, chart]
aliases: [Violin Chart]
related:
  - "[[Seaborn_Categorical_Plots]]" # violinplot
  - "[[Box_Plot]]" # Often compared with or combined
  - "[[Kernel_Density_Estimate_KDE|Kernel Density Estimate (KDE)]]" # Core component of violin plot
  - "[[Choosing_the_Right_Plot]]"
worksheet: [WS_DataViz_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Violin Plot

## Definition
A **violin plot** is a method of plotting numerical data that is a hybrid of a [[Box_Plot|box plot]] and a [[Kernel_Density_Estimate_KDE|Kernel Density Estimate (KDE) plot]]. It shows the probability density of the data at different values, typically smoothed by a kernel density estimator.

For each category or group:
-   A KDE is plotted on each side of a central line, creating a "violin" shape.
-   Optionally, a miniature box plot or summary statistics (like median, quartiles, or individual data points) can be displayed inside the violin.

## Purpose
-   **Visualize Distribution Shape:** Like a KDE, it shows the shape of the distribution, including modality (number of peaks) and skewness.
-   **Summarize Key Statistics:** Like a box plot, it can indicate the median, interquartile range.
-   **Compare Distributions Across Categories:** It's particularly effective for comparing the distributions of a numerical variable across different categorical groups.

## Key Characteristics
-   **Violin Shape:** The width of the violin at a particular value represents the estimated density of data points around that value. Wider sections indicate higher probability density.
-   **Symmetry (by default):** The KDE is typically mirrored to create the violin shape, but it represents a single distribution.
-   **Inner Plot:** Can display a box plot, quartile lines, individual points (`'point'`, `'stick'`), or nothing (`None`) inside the violin.
-   **Split Violins:** If a `hue` variable is used, `split=True` can create half-violins for each hue level, allowing direct comparison within the same category.

## When to Use
-   When you want to compare the distributions of a numerical variable across several categories.
-   When understanding the *shape* of the distribution (e.g., if it's bimodal) is important, which a standard box plot might hide.
-   As an alternative or complement to box plots.

## Advantages over Box Plots
-   Shows more details about the distribution's shape (e.g., multimodality).
-   Can be more informative when distributions are not unimodal or symmetric.

## Disadvantages/Considerations
-   Can be less familiar to some audiences compared to box plots.
-   The interpretation of the KDE depends on the choice of bandwidth (smoothing parameter), though Seaborn often handles this well by default.
-   For very small datasets, the KDE might be noisy or misleading.

## Matplotlib & Seaborn Implementation
-   **Matplotlib:** Does not have a direct violin plot function. One could construct it using KDEs and patches, but it's complex.
-   **Seaborn:** `sns.violinplot(x="category_col", y="value_col", data=df, ...)` or `sns.catplot(..., kind="violin", ...)`. Seaborn provides excellent support.

## Example Scenario & Chart
>[!question]- For Violin Plot: Come up with a scenario where it would be useful. Is this plot the best way to visualize this scenario?
>
>**Scenario:** Comparing customer satisfaction scores (numerical, e.g., 1-10 scale) for three different versions of a software product (categorical: 'Version A', 'Version B', 'Version C'). We suspect some versions might have bimodal satisfaction (e.g., some users love it, some hate it).
>
>**Usefulness:** A violin plot is highly useful to:
>1.  Compare the overall satisfaction levels (e.g., median, spread) across versions.
>2.  Visualize the full distribution shape for each version, potentially revealing if satisfaction for a particular version is concentrated at one level, spread out, or has multiple peaks (bimodal).
>
>**Is this the best way?**
>Yes, in this scenario where the *shape* of the distribution (especially potential multimodality) is important for comparison across categories, a violin plot is often **better than a simple box plot** and is a very strong choice.
>
>**Alternatives & Complements:**
>-   [[Box_Plot|Box plots]] would show medians and IQRs but would hide bimodal distributions.
>-   Overlaid [[Kernel_Density_Estimate_KDE|KDE plots]] could show the shapes but might be harder to compare directly if there are many categories.
>-   Strip plots or swarm plots could show individual points, but the overall distribution shape might be less clear for larger N per category.

**Obsidian Chart Plugin Example (Illustrative):**
> [!note] Violin plots are complex shapes based on KDEs and are not a standard Chart.js type that the basic Obsidian Charts plugin directly renders. The visualization below is a conceptual description of what would be shown. In practice, you'd generate this with Python/Seaborn and embed an image or describe it.

```
Conceptual Data for Customer Satisfaction Violin Plot:

Category    | Satisfaction Scores (Sample)
------------|----------------------------------------------------
Version A   | (mostly high)
Version B   | (bimodal: some low, some high)
Version C   | (mostly medium)

(Imagine three violin shapes side-by-side, one for each version.
- Version A's violin would be wide at the top (scores 7-10).
- Version B's violin would have two wide parts, one near scores 2-4 and another near 8-10.
- Version C's violin would be widest around scores 5-7.
Each violin might also show inner quartile lines or a mini box plot.)
```
**To represent this idea with basic charts (very simplified):** One might show multiple histograms or density curves (as line charts) side-by-side, but this loses the compactness of a violin plot.

```chart
// This is a VERY simplified representation using multiple datasets in a bar/line chart
// to hint at distributions, NOT a true violin plot.
type: line // Or bar, to show density 'bins'
labels: // Satisfaction Score
datasets:
  - label: 'Version A Density (Conceptual)'
    data: [0,0,0,0,0.1,0.2,0.8,1.0,0.9,0.5] // Higher density at high scores
    borderColor: 'rgba(255, 99, 132, 1)'
    fill: false
  - label: 'Version B Density (Conceptual)'
    data: [0.3,0.9,0.8,0.3,0.1,0.1,0.2,0.7,1.0,0.6] // Two peaks
    borderColor: 'rgba(54, 162, 235, 1)'
    fill: false
  - label: 'Version C Density (Conceptual)'
    data: [0,0.1,0.2,0.4,0.9,1.0,0.8,0.3,0.1,0] // Peak in middle
    borderColor: 'rgba(75, 192, 192, 1)'
    fill: false
options:
  title: { display: true, text: 'Conceptual Density for Violin Plot Idea' }
  scales: { y: { title: { display: true, text: 'Density (Conceptual)' } } }
```

---
````

`````markdown

Filename: 170_Data_Visualization/Plot_Types/Trend_Line.md
````markdown
---
tags: [data_visualization, plotting, trend_line, regression_line, smoothing, concept]
aliases: [Line of Best Fit, Regression Line Plot]
related:
  - "[[Scatter_Plot]]" # Trend lines are often overlaid on scatter plots
  - "[[Line_Plot]]" # A trend line is a type of line plot
  - "[[Linear_Regression]]" # Statistical method to find linear trend lines
  - "[[Seaborn_Regression_Plots]]" # sns.regplot, sns.lmplot
worksheet: [WS_DataViz_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Trend Line (Regression Line / Line of Best Fit)

## Definition
A **trend line**, often called a **line of best fit** or a **regression line**, is a straight or curved line in a chart that represents the general direction or pattern of a set of data points. It is used to visualize the relationship between variables and can help in identifying trends, making predictions, or understanding the strength of a correlation.

While "trend line" can sometimes refer to manually drawn lines or simple moving averages, in statistical graphics, it most commonly refers to a line derived from a mathematical model, typically [[Linear_Regression|linear regression]] or other regression techniques (e.g., polynomial regression, LOESS/LOWESS smoothing).

## Purpose
-   **Visualize General Trend:** To show the overall direction (increasing, decreasing, or flat) of data points, especially in a [[Scatter_Plot|scatter plot]].
-   **Summarize Relationship:** Provides a simple summary of the relationship between two numerical variables.
-   **Aid in Prediction (Interpolation/Extrapolation):** Can be used to estimate values where no data points exist, though extrapolation beyond the data range should be done with extreme caution.
-   **Identify Deviations:** Helps highlight data points that deviate significantly from the general trend (outliers or interesting cases).
-   **Assess Strength of Relationship:** The closeness of data points to the trend line can give a visual indication of the strength of the relationship (though this should be quantified with metrics like R-squared or correlation coefficient).

## Common Types
1.  **Linear Trend Line:**
    -   A straight line calculated using linear regression ($y = mx + b$).
    -   Assumes a linear relationship between the variables.
2.  **Polynomial Trend Line:**
    -   A curved line calculated using polynomial regression ($y = ax^2 + bx + c$, etc.).
    -   Can capture non-linear relationships.
3.  **Moving Average Trend Line:**
    -   A line created by averaging data points over a specific window or period. Smooths out short-term fluctuations to highlight longer-term trends. Often used in time series data.
4.  **LOESS/LOWESS (Locally Weighted Scatterplot Smoothing):**
    -   A non-parametric regression method that fits simple models to localized subsets of the data to build up a curve that describes the deterministic part of the variation in the data, point by point. Produces a smooth curve.

## When to Use
-   Primarily overlaid on [[Scatter_Plot|scatter plots]] to clarify the relationship between two numerical variables.
-   For time series data ([[Line_Plot|line plots]]), moving averages or LOESS curves are often used to show underlying trends.

## Implementation
-   **Matplotlib:** No direct single function for a regression line on a scatter plot. You would typically:
    1.  Perform the regression calculation yourself (e.g., using `scipy.stats.linregress` or `numpy.polyfit`).
    2.  Generate points for the line using the fitted model.
    3.  Plot this line using `ax.plot()`.
-   **Seaborn:**
    -   `sns.regplot(x=..., y=..., data=...)`: Directly creates a scatter plot with a linear regression line and confidence interval. Can also fit polynomial, logistic, or robust regression.
    -   `sns.lmplot(x=..., y=..., data=...)`: A figure-level function similar to `regplot` but allows for faceting using `hue`, `col`, `row`.
-   **Pandas Plotting:**
    -   Pandas plotting (which uses Matplotlib) doesn't have a direct trend line argument. You'd follow a similar approach to Matplotlib or use Seaborn.

## Example Scenario & Chart (Conceptual)
>[!question]- For Trend Line: Come up with a scenario where it would be useful. Is this plot the best way to visualize this scenario?
>
>**Scenario:** Analyzing an e-commerce dataset with `number_of_ads_shown` and `daily_sales`. We want to see if there's a positive relationship and visualize the general trend.
>
>**Usefulness:** A scatter plot of `ads_shown` vs. `daily_sales` with an overlaid linear trend line would be useful to:
>1.  Visually confirm if sales tend to increase as more ads are shown.
>2.  Get a sense of the strength and direction of this linear relationship.
>3.  Identify days where sales were unusually high or low given the number of ads.
>
>**Is this the best way?**
>Yes, for visualizing a potential linear relationship between two numerical variables and highlighting the overall trend, a **scatter plot with an overlaid regression line (trend line)** is an excellent and standard choice.
>
>**Alternatives & Complements:**
>-   Calculating the correlation coefficient would quantify the linear relationship.
>-   If the relationship is suspected to be non-linear, `sns.regplot` with `order > 1` (polynomial) or `lowess=True` could be used to fit a more flexible curve.

**Obsidian Chart Plugin Example (Illustrative - Scatter with a separate line dataset for trend):**
```chart
type: scatter
labels: ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7', 'Day 8']
datasets:
  - label: 'Daily Sales vs. Ads'
    data: [ # (ads_shown, daily_sales)
        {x: 100, y: 1500}, {x: 120, y: 1800}, {x: 90, y: 1300}, {x: 150, y: 2200},
        {x: 180, y: 2500}, {x: 110, y: 1600}, {x: 200, y: 2800}, {x: 130, y: 1900}
    ]
    backgroundColor: 'rgba(0, 123, 255, 0.6)'
    pointRadius: 6
  - label: 'Linear Trend Line (Conceptual)'
    data: [ {x: 80, y: 1200}, {x: 220, y: 3000} ] # Two points defining the trend
    type: line # Overlay line plot
    borderColor: 'rgba(220, 53, 69, 1)' # Red color for trend
    fill: false
    borderWidth: 2
    pointRadius: 0 # No markers for the line itself
    tension: 0 # Straight line
options:
  title:
    display: true
    text: 'Daily Sales vs. Ads Shown with Trend Line'
  scales:
    x:
      title:
        display: true
        text: 'Number of Ads Shown'
      min: 0
    y:
      title:
        display: true
        text: 'Daily Sales ($)'
      min: 0
```> **Note:** Statistical packages like Seaborn automatically calculate and plot the regression line and its confidence interval. This Chart.js example manually defines a line for illustrative purposes.

---
````

`````markdown

Filename: 170_Data_Visualization/Plot_Types/Scatter_Plot_Matrix.md
````markdown
---
tags: [data_visualization, plotting, scatter_plot_matrix, pair_plot, multivariate, correlation, concept]
aliases: [Pair Plot, Pairs Plot, Scatterplot Matrix]
related:
  - "[[Visualizing_Multidimensional_Data]]"
  - "[[Scatter_Plot]]"
  - "[[Histogram]]" # Often on diagonal
  - "[[Kernel_Density_Estimate_KDE|KDE Plot]]" # Often on diagonal
  - "[[Seaborn_Multi_Plot_Grids]]" # sns.pairplot
  - "[[_Pandas_MOC]]" # pandas.plotting.scatter_matrix
worksheet: [WS_DataViz_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Scatter Plot Matrix (Pair Plot)

## Definition
A **scatter plot matrix**, often called a **pair plot** or **pairs plot**, is a grid (or matrix) of scatter plots used to visualize the pairwise relationships between several numerical variables in a dataset.

Each cell $(i,j)$ in the grid shows a [[Scatter_Plot|scatter plot]] of variable $i$ against variable $j$. The diagonal cells typically display a univariate plot of each variable, such as a [[Histogram|histogram]] or a [[Kernel_Density_Estimate_KDE|Kernel Density Estimate (KDE) plot]].

## Purpose
-   **Explore Pairwise Relationships:** To quickly identify correlations, trends, clusters, and outliers between all pairs of numerical variables in a dataset.
-   **Understand Univariate Distributions:** The diagonal plots help understand the distribution of each individual variable.
-   **Identify Potential Interactions:** Can give clues about how variables might interact with each other.
-   **High-Level Overview of Multivariate Data:** Provides a comprehensive initial look at the structure of moderately high-dimensional numerical data.

## Key Characteristics
-   **Grid Structure:** Forms a square matrix of plots, where the number of rows and columns equals the number of variables being analyzed.
-   **Off-Diagonal Plots:** Scatter plots showing $Variable_i$ vs. $Variable_j$. The plot in cell $(i,j)$ is often the mirror image (axes swapped) of the plot in cell $(j,i)$, though some implementations might show different information (e.g., correlation coefficient) in the upper or lower triangle.
-   **Diagonal Plots:** Univariate distributions (histogram or KDE) of each variable.
-   **Hue Encoding (Optional):** Points in the scatter plots can be colored by a categorical variable to see how relationships differ across groups.

## When to Use
-   When you have multiple numerical variables (e.g., 3 to 10-15 variables) and want to explore all their pairwise relationships simultaneously.
-   As an initial step in [[Exploratory_Data_Analysis_Workflow|Exploratory Data Analysis (EDA)]] for multivariate numerical data.
-   To visually inspect for multicollinearity before building regression models.

## Implementation
-   **Seaborn:** `sns.pairplot(data_df, hue="category_col", diag_kind="kde", kind="scatter", ...)` is a very powerful and convenient function. See [[Seaborn_Multi_Plot_Grids]].
-   **Pandas:** `pandas.plotting.scatter_matrix(data_df, diagonal="kde", ...)` provides a similar functionality.
-   **Matplotlib:** Can be constructed manually using subplots, but it's much more verbose.

## Example Scenario
>[!question]- For Scatter Plot Matrix: Come up with a scenario where it would be useful. Is this plot the best way to visualize this scenario?
>
>**Scenario:** Analyzing an e-commerce dataset containing product features like `price`, `average_customer_rating`, `number_of_reviews`, and `shipping_time_days`. We want to understand how these numerical features relate to each other and see their individual distributions.
>
>**Usefulness:** A scatter plot matrix is highly useful to:
>1.  See if `price` is correlated with `average_customer_rating` or `number_of_reviews`.
>2.  Check if products with more `number_of_reviews` tend to have higher or lower `average_customer_rating`.
>3.  Observe the distribution of each feature (e.g., is `price` skewed? Is `shipping_time_days` normally distributed?).
>4.  If a `hue` variable like `product_category` is added, see if these relationships differ across categories.
>
>**Is this the best way?**
>Yes, for a quick, comprehensive overview of all pairwise relationships and individual distributions among a moderate number of numerical variables, a scatter plot matrix (pair plot) is an **excellent and standard choice**.
>
>**Alternatives & Complements:**
>-   A [[Heatmap|heatmap]] of the correlation matrix provides a quantitative summary of linear relationships but doesn't show the actual data points, clusters, or non-linear patterns like a scatter plot matrix does.
>-   For a very large number of variables, a scatter plot matrix can become too large and cluttered. In such cases, [[Dimensionality_Reduction|dimensionality reduction]] techniques might be used first, or one might focus on a subset of key variables or use a correlation heatmap.

**Obsidian Chart Plugin Example / Conceptual Output:**
> [!note] A full scatter plot matrix is a complex grid of multiple individual plots. It's not feasible to represent this entire structure with a single basic Obsidian Chart block. The description below outlines what one would see. In Python, `sns.pairplot()` generates this entire figure.

**Conceptual Description of a Scatter Plot Matrix for 3 Variables (e.g., Price, Rating, Reviews):**

Imagine a 3x3 grid of plots:

|                     | **Price (X-axis)**                               | **Rating (X-axis)**                              | **Reviews (X-axis)**                             |
| :------------------ | :----------------------------------------------- | :----------------------------------------------- | :----------------------------------------------- |
| **Price (Y-axis)**  | Histogram/KDE of Price                           | Scatter: Price vs. Rating                        | Scatter: Price vs. Reviews                       |
| **Rating (Y-axis)** | Scatter: Rating vs. Price                        | Histogram/KDE of Rating                          | Scatter: Rating vs. Reviews                      |
| **Reviews (Y-axis)**| Scatter: Reviews vs. Price                       | Scatter: Reviews vs. Rating                      | Histogram/KDE of Reviews                         |

-   Each off-diagonal cell $(i,j)$ contains a scatter plot of variable $i$ vs. variable $j$.
-   Each diagonal cell $(i,i)$ contains a histogram or KDE plot of variable $i$.
-   If a `hue` variable (e.g., product category) is used, points/distributions in all plots would be colored by this category.

This provides a rich, dense summary of the multivariate data.

---
`````

This covers the basic plot types. Next, I'll create the Matplotlib-specific concept notes that were identified (`Matplotlib_Object_Oriented_API.md`, `Matplotlib_Customization.md`, `Matplotlib_Saving_Plots.md`, `Matplotlib_Styles.md`, `Matplotlib_3D_Plotting.md`, `Matplotlib_Interactive_Plots.md`) and then update the `_Matplotlib_MOC.md` to ensure all links are valid.

---


Okay, let's create the Matplotlib-specific concept notes.

---
**Creating Matplotlib Concept Notes:**

`````markdown

Filename: 170_Data_Visualization/Matplotlib/Matplotlib_Object_Oriented_API.md
````markdown
---
tags: [matplotlib, python, api, plotting, object_oriented, figure, axes, concept, example]
aliases: [Matplotlib OO API, Object-Based Matplotlib]
related:
  - "[[Matplotlib_Overview]]"
  - "[[Matplotlib_Pyplot_API_vs_OO_API]]" # Comparison
  - "[[Matplotlib_Figure_Subplot_Axes]]" # Core objects used
  - "[[Matplotlib_Pyplot_API]]" # The state-based alternative
worksheet: [WS_DataViz_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Matplotlib: Object-Oriented (OO) API

The **Object-Oriented (OO) API** is one of the two main ways to use [[Matplotlib_Overview|Matplotlib]], the other being the [[Matplotlib_Pyplot_API|pyplot API]]. The OO API is generally considered more powerful, flexible, and Pythonic for complex plots or when embedding Matplotlib in applications.

It involves explicitly creating and manipulating `Figure` and `Axes` objects.

## Core Idea
Instead of relying on a global state managed by `pyplot` (e.g., `plt.plot()` acting on the "current" axes), you explicitly:
1.  Create a **`Figure`** object (the top-level container).
2.  Add one or more **`Axes`** objects (subplots/plotting areas) to the Figure.
3.  Call methods directly on these `Axes` objects to create the plot (e.g., `ax.plot()`, `ax.scatter()`).
4.  Call methods on `Axes` or `Figure` objects for customization (e.g., `ax.set_title()`, `fig.savefig()`).

## Creating Figure and Axes
The most common way to start with the OO API is using `plt.subplots()`:

```python
import matplotlib.pyplot as plt
import numpy as np

# Create a Figure and a single Axes object
fig, ax = plt.subplots() 
# fig is a matplotlib.figure.Figure instance
# ax is a matplotlib.axes.Axes instance (or a single Axes if nrows=1, ncols=1)

# Create a Figure and a 2x2 grid of Axes objects
# fig_multiple, axs = plt.subplots(nrows=2, ncols=2, figsize=(8, 8))
# axs is now a 2D NumPy array of Axes objects:
# axs[0, 0] is the top-left subplot
# axs[0, 1] is the top-right subplot
# ... and so on.
```
-   `plt.subplots()` is a convenience function from `pyplot` that returns a `Figure` instance and an array (or single instance) of `Axes` objects.
-   You can also create a figure first (`fig = plt.figure()`) and then add axes to it (`ax1 = fig.add_subplot(1,2,1)`, `ax2 = fig.add_axes([left, bottom, width, height])`).

## Plotting and Customizing
Once you have an `Axes` object (e.g., `ax`), you use its methods:

[list2tab|#OO API Methods]
- Plotting Data
    -   `ax.plot(x, y, ...)`: For [[170_Data_Visualization/Plot_Types/Line_Plot|line plots]] and basic scatter plots (with line styles).
    -   `ax.scatter(x, y, ...)`: For [[170_Data_Visualization/Plot_Types/Scatter_Plot|scatter plots]] with more control over marker properties.
    -   `ax.bar(x, height, ...)`: For vertical [[170_Data_Visualization/Plot_Types/Bar_Chart|bar charts]].
    -   `ax.barh(y, width, ...)`: For horizontal bar charts.
    -   `ax.hist(data, bins=..., ...)`: For [[170_Data_Visualization/Plot_Types/Histogram|histograms]].
    -   `ax.boxplot(data, ...)`: For [[170_Data_Visualization/Plot_Types/Box_Plot|box plots]].
    -   `ax.pie(sizes, ...)`: For [[170_Data_Visualization/Plot_Types/Pie_Chart|pie charts]].
    -   `ax.imshow(image_data, ...)`: For displaying images or [[170_Data_Visualization/Plot_Types/Heatmap|heatmaps]]. See [[Matplotlib_Image_Display_imshow]].
    -   And many more specialized plotting methods.
- Setting Titles & Labels
    -   `ax.set_title("My Plot Title")`
    -   `ax.set_xlabel("X-axis Label")`
    -   `ax.set_ylabel("Y-axis Label")`
    -   `fig.suptitle("Overall Figure Title")` (called on the Figure object)
- Setting Limits
    -   `ax.set_xlim([xmin, xmax])`
    -   `ax.set_ylim([ymin, ymax])`
- Setting Ticks & Tick Labels
    -   `ax.set_xticks()`
    -   `ax.set_xticklabels()`
    -   `ax.set_yticks()`
    -   `ax.set_yticklabels()`
    -   `ax.tick_params(...)` for detailed tick customization.
- Legends
    -   `ax.legend()` (requires `label` argument in plotting calls like `ax.plot(..., label="Data Series")`).
- Gridlines
    -   `ax.grid(True/False, which='major', axis='both', ...)`
- Annotations & Text
    -   `ax.text(x, y, "my text", ...)`
    -   `ax.annotate("my annotation", xy=(x_point, y_point), xytext=(x_text, y_text), arrowprops=...)`

## Example (Revisiting the Sine/Cosine Plot OO-Style)
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

# Create a figure and one Axes
fig, ax = plt.subplots(figsize=(8, 5))

# Plot on the Axes object
ax.plot(x, y_sin, label='sin(x)', color='blue', linestyle='-')
ax.plot(x, y_cos, label='cos(x)', color='red', linestyle='--')

# Customize the Axes
ax.set_title('Sine and Cosine Waves (OO API)')
ax.set_xlabel('Angle (radians)')
ax.set_ylabel('Value')
ax.legend()
ax.grid(True)
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1.2, 1.2)

# Display the plot (still often uses pyplot's show)
# plt.show()
```

## Advantages
-   **Explicit Control:** You have direct handles to Figure and Axes objects, making it clear what part of the plot you are modifying.
-   **Better for Complex Layouts:** Essential for figures with multiple subplots, insets, or custom arrangements.
-   **Reusability:** Easier to write reusable functions or classes that create and customize plots because you can pass Figure or Axes objects around.
-   **Embedding:** The standard way to embed Matplotlib plots in GUI applications (Tkinter, Qt, WxPython) or web applications.
-   **Clarity in Larger Scripts:** Reduces ambiguity compared to the stateful `pyplot` API when dealing with multiple plots.

While `pyplot` is convenient for quick, interactive plotting, the Object-Oriented API is generally recommended for more structured, complex, or reusable plotting tasks. Often, a hybrid approach is used: `plt.subplots()` to get `fig` and `ax`, then OO methods on `ax`, and `plt.show()` at the end.

---
````

`````markdown

Filename: 170_Data_Visualization/Matplotlib/Matplotlib_Customization.md
````markdown
---
tags: [matplotlib, python, plotting, customization, aesthetics, labels, titles, legends, colors, concept]
aliases: [Customizing Matplotlib Plots, Matplotlib Plot Aesthetics]
related:
  - "[[Matplotlib_Overview]]"
  - "[[Matplotlib_Object_Oriented_API]]" # Customization is done via object methods
  - "[[Matplotlib_Figure_Subplot_Axes]]"
  - "[[Plot_Elements_Anatomy]]"
  - "[[Matplotlib_Colormaps]]"
  - "[[Matplotlib_Styles]]"
worksheet: [WS_DataViz_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Matplotlib: Customizing Plots

Matplotlib offers extensive control over nearly every aspect of a plot, allowing for highly customized and publication-quality visualizations. Customizations are typically applied by calling methods on the [[Matplotlib_Figure_Subplot_Axes|`Figure`]] and [[Matplotlib_Figure_Subplot_Axes|`Axes`]] objects (using the [[Matplotlib_Object_Oriented_API|Object-Oriented API]]) or via `pyplot` functions.

## Common Customization Areas

[list2tab|#Plot Customizations]
- Titles and Labels
    -   **Axes Title:** `ax.set_title("My Plot Title", fontsize=16, color='darkblue')`
    -   **X-Axis Label:** `ax.set_xlabel("Time (seconds)", fontsize=12)`
    -   **Y-Axis Label:** `ax.set_ylabel("Amplitude (Volts)", fontsize=12)`
    -   **Figure Suptitle:** `fig.suptitle("Overall Experiment Results", fontsize=18, fontweight='bold')` (applied to the `Figure` object)
- Lines and Markers (for `ax.plot()`)
    -   **Color:** `color='red'`, `color='#FF5733'`, `color=(0.1, 0.2, 0.5)`
    -   **Linestyle:** `linestyle='--'` (dashed), `'-.'` (dash-dot), `':'` (dotted), `'-'` (solid, default).
    -   **Linewidth:** `linewidth=2.5` (float).
    -   **Marker:** `marker='o'` (circle), `'s'` (square), `'^'` (triangle_up), `'.'` (point), `'*'` (star).
    -   **Markersize:** `markersize=8`.
    -   **Marker Edge Color/Width:** `markeredgecolor='black'`, `markeredgewidth=0.5`.
    -   **Marker Face Color:** `markerfacecolor='lightblue'`.
    - **Example:**
        ```python
        # ax.plot(x, y, color='magenta', linestyle=':', linewidth=1.5,
        #         marker='D', markersize=6, markerfacecolor='yellow',
        #         markeredgecolor='black', label='Data Series')
        ```
- Axis Limits
    -   `ax.set_xlim([xmin, xmax])` or `ax.set_xlim(left=xmin, right=xmax)`
    -   `ax.set_ylim([ymin, ymax])` or `ax.set_ylim(bottom=ymin, top=ymax)`
    -   `ax.axis('equal')`: Sets equal scaling for x and y axes (pixels per data unit).
    -   `ax.axis('tight')`: Sets limits to just encompass the data.
    -   `ax.axis('off')`: Turns off the axis lines and labels.
- Ticks, Tick Labels, and Grid
    -   **Setting Tick Locations:**
        -   `ax.set_xticks()`
        -   `ax.set_yticks()`
    -   **Setting Tick Labels:**
        -   `ax.set_xticklabels(['A', 'B', 'C'])`
        -   `ax.set_yticklabels(['Low', 'Med', 'High'], rotation=45)`
    -   **Tick Parameters (Major/Minor):** `ax.tick_params(axis='x', which='major', labelsize=10, direction='inout', length=6)`
        -   Controls appearance like size, direction, color of ticks and labels.
    -   **Gridlines:**
        -   `ax.grid(True, linestyle='--', linewidth=0.5, color='gray', alpha=0.7, which='major', axis='both')`
        -   `which`: `{'major', 'minor', 'both'}`
        -   `axis`: `{'x', 'y', 'both'}`
- Legends
    -   `ax.legend(loc='best', fontsize='small', title='Legend Title', frameon=True, shadow=True, ncol=2)`
    -   **`loc`:** Location string (e.g., 'upper right', 'lower left', 'center') or code. `'best'` tries to find an optimal location.
    -   **`ncol`:** Number of columns in the legend.
    -   Requires `label` argument in plotting calls (e.g., `ax.plot(..., label="Series A")`).
- Colors and Colormaps
    -   Individual colors for lines, markers, bars, etc. (see "Lines and Markers").
    -   [[Matplotlib_Colormaps|Colormaps (`cmap`)]] for plots like `imshow`, `scatter` (when `c` is an array), `pcolormesh`, `contourf`.
        -   `im = ax.imshow(data, cmap='viridis')`
        -   `fig.colorbar(im, ax=ax, label="Intensity")` to add a colorbar.
- Text and Annotations
    -   **Adding Text:** `ax.text(x_coord, y_coord, "My Text Note", fontsize=10, color='red')`
        -   Coordinates are data coordinates by default. Can use `transform=ax.transAxes` for figure-relative coordinates (0,0 is bottom-left, 1,1 is top-right of axes).
    -   **Annotations with Arrows:** `ax.annotate("Important Point", xy=(data_x, data_y), xytext=(text_x, text_y), arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5))`
        -   `xy`: The point to annotate.
        -   `xytext`: The position of the text.
        -   `arrowprops`: Dictionary to style the arrow.
- Figure Size and DPI
    -   When creating the figure: `fig, ax = plt.subplots(figsize=(width_inches, height_inches), dpi=100)`
    -   `fig.set_size_inches(width, height)`
    -   `fig.set_dpi(value)`
- Spines (Plot Borders)
    -   Access via `ax.spines['top']`, `ax.spines['right']`, etc.
    -   `ax.spines['top'].set_visible(False)`
    -   `ax.spines['right'].set_color('blue')`
- Background Colors
    -   Axes background: `ax.set_facecolor('lightyellow')`
    -   Figure background: `fig.patch.set_facecolor('lightgrey')` (or `fig.set_facecolor(...)`)

## Example of Extensive Customization

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 200)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) * np.cos(x)

# Create figure and axes object
fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor('#f0f0f0') # Light grey figure background

# Plotting data with specific styles
ax.plot(x, y1, color='dodgerblue', linestyle='-', linewidth=2, marker='o', markersize=5, markevery=20, label='sin(x)')
ax.plot(x, y2, color='orangered', linestyle='--', linewidth=2, label='cos(x)')
ax.plot(x, y3, color='green', linestyle=':', linewidth=1.5, marker='s', markevery=25, markersize=4, label='sin(x)cos(x)')

# Titles and Labels
ax.set_title('Highly Customized Matplotlib Plot', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('X-axis (Radians)', fontsize=14, labelpad=10)
ax.set_ylabel('Y-axis (Value)', fontsize=14, labelpad=10)

# Axis Limits and Ticks
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1.2, 1.2)
ax.set_xticks(np.linspace(0, 2 * np.pi, 5)) # Define major tick locations
ax.set_xticklabels(['0', 'π/2', 'π', '3π/2', '2π'], fontsize=10) # Custom labels
ax.tick_params(axis='both', which='major', labelsize=10, direction='out', length=6, width=1, colors='dimgray')

# Grid
ax.grid(True, which='major', linestyle=':', linewidth=0.5, color='darkgray')

# Legend
ax.legend(loc='upper right', fontsize='medium', frameon=True, shadow=True, edgecolor='black', facecolor='whitesmoke')

# Spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['left'].set_color('dimgray')
ax.spines['bottom'].set_color('dimgray')

# Axes background
ax.set_facecolor('#e9e9e9')

# Add an annotation
ax.annotate('Peak of sin(x)', xy=(np.pi/2, 1), xytext=(np.pi/2 + 0.5, 1.1),
            arrowprops=dict(facecolor='black', shrink=0.05, width=0.5, headwidth=4),
            fontsize=9, color='navy')

plt.tight_layout() # Adjust plot to ensure everything fits without overlapping
# plt.show()
```

Matplotlib's extensive customization options allow for precise control over the appearance of plots, making it suitable for a wide range of scientific, engineering, and data analysis visualization needs. For consistent styling across multiple plots, consider using [[Matplotlib_Styles|Stylesheets]].

---
````

`````markdown

Filename: 170_Data_Visualization/Matplotlib/Matplotlib_Saving_Plots.md
````markdown
---
tags: [matplotlib, python, plotting, saving_figures, export, file_formats, concept, example]
aliases: [Saving Matplotlib Figures, plt.savefig, fig.savefig]
related:
  - "[[Matplotlib_Overview]]"
  - "[[Matplotlib_Figure_Subplot_Axes]]" # Figure object has the savefig method
worksheet: [WS_DataViz_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Matplotlib: Saving Plots to Files

Matplotlib allows you to save your generated plots to a wide variety of file formats, suitable for inclusion in documents, presentations, web pages, or for archival purposes. The primary function for this is `savefig()`.

## `savefig()` Method
This method can be called on a [[Matplotlib_Figure_Subplot_Axes|`Figure` object]] (`fig.savefig()`) in the object-oriented API, or as a `pyplot` function (`plt.savefig()`) which acts on the current figure.

**Syntax (Simplified):**
```python
fig.savefig(fname, dpi=None, format=None, bbox_inches=None, pad_inches=0.1, transparent=False, ...)
plt.savefig(fname, ...) # Similar parameters
```

[list2tab|#savefig Parameters]
- `fname` (Filename or File-like object)
    -   A string representing the path and filename (e.g., `'my_plot.png'`, `'../figures/report_figure.pdf'`).
    -   The file format is often inferred from the extension of `fname`.
    -   Can also be a Python file-like object (e.g., `io.BytesIO`).
- `dpi` (Dots Per Inch)
    -   Integer, controls the resolution of rasterized output formats (like PNG, JPG). Higher DPI means higher resolution and larger file size.
    -   Common values: 100 (screen), 300 (print), 600 (high-quality print).
    -   If `None`, uses the figure's DPI or a default.
- `format`
    -   String, explicitly specifies the output format (e.g., `'png'`, `'pdf'`, `'svg'`, `'jpg'`, `'eps'`, `'tiff'`).
    -   If not provided, Matplotlib tries to infer it from the `fname` extension.
- `bbox_inches`
    -   `'tight'`: Adjusts the bounding box of the saved figure to include all artists, removing excess whitespace. Very useful.
    -   Can also be a `Bbox` object to specify a custom bounding box.
- `pad_inches`
    -   Amount of padding around the figure when `bbox_inches='tight'`.
- `transparent`
    -   Boolean. If `True`, the figure and axes backgrounds will be transparent (if the output format supports transparency, like PNG or SVG).
- `facecolor`, `edgecolor`
    -   The color of the figure background and edge. `fig.patch.set_facecolor('w')` can be used before saving for a white background if the default is different.
- `orientation`
    -   `{'landscape', 'portrait'}` (for formats like PDF that support it).
- `metadata`
    -   Dictionary of metadata to embed in supported formats (e.g., PDF, SVG).

## Supported File Formats
Matplotlib supports numerous output formats. Common ones include:
-   **Raster Formats (Pixel-based):**
    -   `png`: Portable Network Graphics (good for web, lossless compression, supports transparency).
    -   `jpg` or `jpeg`: Joint Photographic Experts Group (good for photographs, lossy compression).
    -   `tiff`: Tagged Image File Format (often used for high-quality print, can be lossless or lossy).
    -   `bmp`: Bitmap.
-   **Vector Formats (Scalable):**
    -   `pdf`: Portable Document Format (excellent for documents, scalable, widely supported).
    -   `svg`: Scalable Vector Graphics (good for web, XML-based, scalable, editable in vector graphics software).
    -   `eps`: Encapsulated PostScript (older vector format, common in academic publishing with LaTeX).
    -   `ps`: PostScript.

Vector formats are generally preferred for line art, text, and plots that need to be scaled without loss of quality. Raster formats are suitable for images with complex color gradients or when file size for web display is a concern (e.g., JPG for photos).

## Example Usage

```python
import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a plot (OO API example)
fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(x, y, label='sin(x)')
ax.set_title('Sine Wave Plot')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.legend()
ax.grid(True)

# --- Saving the plot ---

# 1. Save as PNG (common raster format)
# fig.savefig('sine_wave.png', dpi=300) # Save with 300 DPI
# print("Plot saved as sine_wave.png")

# 2. Save as PDF (common vector format for documents)
# fig.savefig('sine_wave.pdf', bbox_inches='tight') # 'tight' removes extra whitespace
# print("Plot saved as sine_wave.pdf")

# 3. Save as SVG (scalable vector format for web/editing)
# fig.savefig('sine_wave.svg', transparent=True) # Save with transparent background
# print("Plot saved as sine_wave.svg")

# 4. Using pyplot interface (acts on the current figure)
# plt.plot(x, np.cos(x)) # Add another plot to the current figure/axes
# plt.title("Another Plot on Current Figure")
# plt.savefig('current_figure_plot.jpg', format='jpeg', quality=90) # Specify format and JPG quality
# print("Plot saved as current_figure_plot.jpg")

# Important: plt.show() often clears the figure in some environments.
# It's generally good practice to save BEFORE calling plt.show() if you are in a script.
# In Jupyter notebooks, figures often persist after show().
# plt.show()
```

## Tips for Saving Figures
-   **Save Before `plt.show()`:** In scripts, `plt.show()` can sometimes clear the figure, so save it before calling `show()`. In interactive environments like Jupyter, this is less of an issue.
-   **`bbox_inches='tight'`:** This is very useful for creating well-cropped figures without excessive whitespace, especially for inclusion in documents.
-   **Choose Appropriate DPI:** For raster formats, select a DPI suitable for the intended use (e.g., 72-100 DPI for web/screen, 300+ DPI for print).
-   **Vector vs. Raster:** Use vector formats (PDF, SVG, EPS) when scalability and crisp lines/text are important (e.g., publications). Use raster formats (PNG, JPG) for web display where file size might be a concern or for images with complex color gradients.
-   **Transparency:** Use `transparent=True` with PNG or SVG if you need the plot background to be transparent (e.g., for overlaying on other content).
-   **Consistent Figure Size:** Set `figsize` when creating the figure (`plt.figure(figsize=(w,h))` or `plt.subplots(figsize=(w,h))`) to control the aspect ratio and initial size, which affects how text and elements are scaled when saved.

Saving plots effectively is crucial for sharing and documenting your data visualizations.

---
````

`````markdown

Filename: 170_Data_Visualization/Matplotlib/Matplotlib_Styles.md
````markdown
---
tags: [matplotlib, python, plotting, styles, themes, aesthetics, concept, example]
aliases: [Matplotlib Stylesheets, Plot Styles, plt.style.use]
related:
  - "[[Matplotlib_Overview]]"
  - "[[Matplotlib_Customization]]"
  - "[[Seaborn_Themes_Styles]]" # Seaborn also offers styling, often built on Matplotlib styles
worksheet: [WS_DataViz_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Matplotlib: Using Stylesheets (`plt.style`)

Matplotlib provides a way to customize the overall look and feel of your plots using **stylesheets**. A stylesheet contains a set of predefined parameters (rcParams) that control various aspects like colors, line widths, font sizes, grid appearance, etc. This allows you to easily switch between different visual themes for your plots without manually changing individual parameters for each plot.

The `plt.style` module is used to manage and apply these styles.

## Key `plt.style` Functionality

[list2tab|#Style Functions]
- `plt.style.available` (Attribute)
    -   A list of strings containing the names of all available built-in styles.
    -   **Example:**
        ```python
        import matplotlib.pyplot as plt
        # print(plt.style.available)
        # Output might include:
        # ['Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid',
        #  'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot',
        #  'grayscale', 'seaborn-v0_8-bright', 'seaborn-v0_8-colorblind', ... many more]
        ```
- `plt.style.use(style_name)`
    -   **Purpose:** Applies a specified style globally to all subsequent plots created in the current Python session or script.
    -   `style_name`: Can be a string (name of a built-in style or path to a custom `.mplstyle` file), a list of style names (styles are applied sequentially, later ones overriding earlier ones), or a dictionary of rcParams.
    -   **Example:**
        ```python
        import matplotlib.pyplot as plt
        import numpy as np

        # Apply the 'ggplot' style (popular R plotting package style)
        # plt.style.use('ggplot')

        x = np.linspace(0, 10, 100)
        # fig, ax = plt.subplots()
        # ax.plot(x, np.sin(x), label='sin(x)')
        # ax.plot(x, np.cos(x), label='cos(x)')
        # ax.set_title("'ggplot' Style Example")
        # ax.legend()
        # plt.show()

        # Revert to default (or apply another style for subsequent plots)
        # plt.style.use('default') # 'default' reverts to Matplotlib's default rcParams
        ```
- `plt.style.context(style_name)` (Context Manager)
    -   **Purpose:** Applies a style temporarily within a `with` block. The style reverts to its previous state after exiting the block. This is useful for applying a specific style to a single plot or a group of plots without affecting global settings.
    -   **Example:**
        ```python
        import matplotlib.pyplot as plt
        import numpy as np
        x = np.linspace(0, 10, 100)

        # Plot 1: Default style
        # fig1, ax1 = plt.subplots()
        # ax1.plot(x, np.sin(x))
        # ax1.set_title("Plot with Default Style")
        # plt.show()

        # Plot 2: Temporarily use 'fivethirtyeight' style
        # with plt.style.context('fivethirtyeight'):
        #     fig2, ax2 = plt.subplots()
        #     ax2.plot(x, np.cos(x))
        #     ax2.set_title("Plot with 'fivethirtyeight' Style (Temporary)")
        #     # plt.show() # Show inside context if needed, or after if fig object is used

        # Plot 3: Back to default style
        # fig3, ax3 = plt.subplots()
        # ax3.plot(x, np.tan(x)) # tan might have discontinuities, be careful with ylim
        # ax3.set_ylim(-5, 5)
        # ax3.set_title("Plot with Default Style (Again)")
        # plt.show()
        ```
- Custom Stylesheets (`.mplstyle` files)
    -   You can create your own stylesheet files (with a `.mplstyle` extension) containing `rcParams` settings.
    -   Example `my_custom_style.mplstyle`:
        ```
        axes.titlesize : 20
        axes.labelsize : 16
        lines.linewidth : 3
        lines.markersize : 10
        xtick.labelsize : 12
        ytick.labelsize : 12
        figure.facecolor : lightgrey
        ```
    -   Then use it with `plt.style.use('./my_custom_style.mplstyle')` (provide path to the file).
    -   Stylesheets can also be placed in `matplotlib.get_configdir() + /stylelib/` to be accessible by name.

## Popular Built-in Styles
Some commonly used styles include:
-   **`'ggplot'`:** Mimics the aesthetics of plots from the popular R library `ggplot2`. Often features a gray background, white gridlines, and distinct colors.
-   **`'fivethirtyeight'`:** Emulates the style of the data journalism website FiveThirtyEight, often with thicker lines, specific fonts, and a characteristic look.
-   **`'seaborn-v0_8-*'` variants (e.g., `'seaborn-v0_8-whitegrid'`, `'seaborn-v0_8-darkgrid'`, `'seaborn-v0_8-colorblind'`):** Provide styles similar to those from the [[170_Data_Visualization/Seaborn/_Seaborn_MOC|Seaborn]] library. Using `sns.set_theme()` from Seaborn itself is now the more direct way to get Seaborn's full styling.
-   **`'dark_background'`:** Useful for plots on dark slides or UIs.
-   **`'grayscale'`:** For producing plots in grayscale.
-   **`'classic'`:** Reverts to the Matplotlib 1.x classic style.
-   **`'default'`:** Matplotlib's current default style.

## Combining Styles
You can apply multiple styles by passing a list of style names to `plt.style.use()`. Styles are applied from left to right, so later styles can override settings from earlier ones.
```python
# plt.style.use(['seaborn-v0_8-whitegrid', 'my_custom_settings'])
# This would first apply seaborn-whitegrid, then overlay 'my_custom_settings'.
```

Using stylesheets is a convenient way to achieve consistent and professional-looking plots with minimal effort, allowing you to focus more on the data and less on individual formatting commands for each plot.

---
````

`````markdown

Filename: 170_Data_Visualization/Matplotlib/Matplotlib_3D_Plotting.md
````markdown
---
tags: [matplotlib, python, plotting, 3d_plots, mplot3d, scatter3d, surface_plot, concept, example]
aliases: [Matplotlib 3D, 3D Scatter Plot Matplotlib, 3D Surface Plot Matplotlib]
related:
  - "[[Matplotlib_Overview]]"
  - "[[Matplotlib_Figure_Subplot_Axes]]"
  - "[[Visualizing_Multidimensional_Data]]"
worksheet: [WS_DataViz_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Matplotlib: 3D Plotting (`mpl_toolkits.mplot3d`)

Matplotlib provides basic capabilities for creating 3D plots through its `mpl_toolkits.mplot3d` toolkit. This toolkit extends Matplotlib's 2D plotting functionality to allow for the creation of 3D scatter plots, surface plots, wireframe plots, contour plots, bar charts, and more.

To create a 3D plot, you need to create a regular [[Matplotlib_Figure_Subplot_Axes|Figure]] and then add an `Axes3D` subplot to it.

## Creating a 3D Axes
The most common way to create a 3D axes object is:```python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D # Necessary for registering the 3D projection

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# Alternatively: ax = plt.axes(projection='3d')
```
The `projection='3d'` argument is key here. Once you have the `ax` (an `Axes3D` object), you can use its specific methods for 3D plotting.

## Common 3D Plot Types

[list2tab|#3D Plot Types]
- 3D Scatter Plot (`ax.scatter` or `ax.scatter3D`)
    - **Purpose:** To visualize the relationship between three numerical variables, where each point is plotted in 3D space. Additional dimensions can be encoded using color (`c`) and size (`s`) of markers.
    - **Example (E-commerce: Price, Rating, Review Count):**
        ```python
        import matplotlib.pyplot as plt
        import numpy as np
        # from mpl_toolkits.mplot3d import Axes3D # Already imported conceptually

        # Conceptual product data
        # np.random.seed(42)
        # n_products = 100
        # price = np.random.uniform(10, 200, n_products)
        # avg_rating = np.random.uniform(1, 5, n_products)
        # review_count = np.random.randint(5, 500, n_products)
        # # Color by a fourth variable, e.g., profit margin (conceptual)
        # profit_margin_ratio = np.random.rand(n_products)

        # fig = plt.figure(figsize=(10, 8))
        # ax = fig.add_subplot(111, projection='3d')

        # scatter = ax.scatter(price, avg_rating, review_count, 
        #                      c=profit_margin_ratio, cmap='viridis', s=50, alpha=0.7)
        
        # ax.set_title('3D Scatter Plot: Product Features')
        # ax.set_xlabel('Price ($)')
        # ax.set_ylabel('Average Rating (1-5)')
        # ax.set_zlabel('Number of Reviews')
        # fig.colorbar(scatter, label='Profit Margin Ratio', shrink=0.5, aspect=10)
        # plt.show()
        ```
    -   **Obsidian Chart Plugin Example:** Basic Obsidian Charts do not support 3D scatter plots directly. This would be described conceptually or an image embedded.
- 3D Surface Plot (`ax.plot_surface`)
    - **Purpose:** To visualize a 3D surface defined by $z = f(x,y)$. Requires X, Y, and Z data to be 2D arrays (grids).
    - **Key Parameters:** `X`, `Y`, `Z`, `cmap` (colormap), `rstride`, `cstride` (row/column stride for downsampling), `linewidth`, `edgecolor`.
    - **Example (Plotting $z = \sin(\sqrt{x^2 + y^2})$):**
        ```python
        import matplotlib.pyplot as plt
        import numpy as np
        # from mpl_toolkits.mplot3d import Axes3D

        # fig = plt.figure(figsize=(10, 8))
        # ax = fig.add_subplot(111, projection='3d')

        # Create X and Y data for the grid
        # x_surf = np.linspace(-5, 5, 50)
        # y_surf = np.linspace(-5, 5, 50)
        # X_surf, Y_surf = np.meshgrid(x_surf, y_surf)
        # Z_surf = np.sin(np.sqrt(X_surf**2 + Y_surf**2))

        # surf = ax.plot_surface(X_surf, Y_surf, Z_surf, cmap='magma', edgecolor='none')
        
        # ax.set_title('3D Surface Plot: $z = sin(\sqrt{x^2+y^2})$')
        # ax.set_xlabel('X axis')
        # ax.set_ylabel('Y axis')
        # ax.set_zlabel('Z axis (sin value)')
        # fig.colorbar(surf, shrink=0.5, aspect=10, label='Z value')
        # plt.show()
        ```
    -   **Obsidian Chart Plugin Example:** Not directly supported.
- 3D Wireframe Plot (`ax.plot_wireframe`)
    - **Purpose:** Similar to `plot_surface` but only draws the wireframe structure of the surface.
    - **Example:**
        ```python
        # (Using X_surf, Y_surf, Z_surf from surface plot example)
        # fig = plt.figure(figsize=(10, 8))
        # ax = fig.add_subplot(111, projection='3d')
        # ax.plot_wireframe(X_surf, Y_surf, Z_surf, rstride=3, cstride=3, color='cyan')
        # ax.set_title('3D Wireframe Plot')
        # plt.show()
        ```- 3D Line Plot (`ax.plot` or `ax.plot3D`)
    - **Purpose:** To plot lines or trajectories in 3D space. Takes 1D arrays for x, y, and z coordinates.
    - **Example (A helix):**
        ```python
        # fig = plt.figure(figsize=(8, 6))
        # ax = fig.add_subplot(111, projection='3d')
        # t = np.linspace(0, 10 * np.pi, 500)
        # x_line = np.sin(t)
        # y_line = np.cos(t)
        # z_line = t / (2*np.pi) # Height increases with t
        # ax.plot(x_line, y_line, z_line, label='Helical Path', color='purple')
        # ax.set_title('3D Line Plot (Helix)')
        # ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
        # ax.legend()
        # plt.show()
        ```
- 3D Bar Chart (`ax.bar3d`)
    - **Purpose:** Creates 3D bar charts. Can be hard to interpret due to occlusion.
- Contour Plots in 3D (`ax.contour3D`, `ax.contourf3D`)
    - **Purpose:** Draws 3D contour lines or filled contours for a function $z = f(x,y)$.

## Customization and Interaction
-   **Setting Axis Labels:** `ax.set_xlabel()`, `ax.set_ylabel()`, `ax.set_zlabel()`.
-   **Setting Axis Limits:** `ax.set_xlim()`, `ax.set_ylim()`, `ax.set_zlim()`.
-   **Setting View Angle:** `ax.view_init(elev, azim)` where `elev` is elevation angle and `azim` is azimuthal angle. This is crucial for finding a good perspective. Interactive rotation is often available in Matplotlib backends (e.g., Qt, Tk, Jupyter with `%matplotlib widget`).
-   **Colormaps (`cmap`):** Used extensively in surface and scatter plots to map values to colors.

## Challenges of 3D Plotting
-   **Occlusion:** Objects in the foreground can hide objects in the background.
-   **Perspective Distortion:** The perception of depth and relative sizes can be tricky.
-   **Difficulty in Reading Exact Values:** Harder to read precise data values compared to 2D plots.
-   **Interactivity is Often Key:** The ability to rotate, zoom, and pan 3D plots interactively is very important for understanding them. Static 3D plots can be less effective.

While Matplotlib's 3D capabilities are useful for basic 3D visualization, for highly interactive and advanced 3D graphics, specialized libraries like Plotly, Mayavi, or PyVista might offer more features.

---
````

`````markdown

Filename: 170_Data_Visualization/Matplotlib/Matplotlib_Interactive_Plots.md
````markdown
---
tags: [matplotlib, python, plotting, interactive_plots, jupyter, ipympl, widgets, concept]
aliases: [Interactive Matplotlib, Matplotlib Widgets]
related:
  - "[[Matplotlib_Overview]]"
  - "[[Matplotlib_Figure_Subplot_Axes]]"
  - "[[Jupyter_Notebook_Lab]]" # Common environment for interactive plotting
worksheet: [WS_DataViz_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Matplotlib: Interactive Plots

While Matplotlib is primarily known for generating static plots, it also supports varying degrees of interactivity, especially when used within certain environments or with specific backends. True web-native interactivity like that found in [[Plotly_and_Plotly_Express|Plotly]] or [[Bokeh_Library|Bokeh]] is not its core strength, but useful interactive features are available.

## Interactivity in Different Environments

1.  **Standard Matplotlib Window (GUI Backends):**
    -   When Matplotlib uses a GUI backend (like Qt5Agg, TkAgg, WXAgg, MacOSX), the plot window that appears typically has built-in interactive tools:
        -   **Pan/Zoom:** Buttons to pan (move the plot around) and zoom into specific regions.
        -   **Save:** Button to save the figure.
        -   **Configure Subplots:** Tool to adjust subplot layout parameters.
        -   **Home/Back/Forward:** Navigate view history.
    -   This is the default behavior when running a Matplotlib script outside of environments like Jupyter.

2.  **Jupyter Notebook / JupyterLab:**
    -   **`%matplotlib inline` (Default):**
        -   Renders static PNG images embedded directly in the notebook. No interactivity beyond the generated image.
    -   **`%matplotlib notebook` (Older, classic Jupyter Notebook):**
        -   Renders interactive plots within the notebook output cell. Provides zoom, pan, and other tools similar to GUI backends.
        -   Can be a bit clunky and is less favored now.
    -   **`%matplotlib widget` (Recommended for JupyterLab, also works in Notebook):**
        -   Uses the `ipympl` backend to provide fully interactive figures directly in the notebook or JupyterLab.
        -   Offers smoother panning, zooming, and the ability to connect Python widgets (from `ipywidgets`) to control plot elements dynamically.
        -   Requires `ipympl` to be installed: `pip install ipympl jupyterlab_widgets`.
        -   **Example (`%matplotlib widget`):**
            ```python
            # In a Jupyter Notebook/Lab cell, run this first:
            # %matplotlib widget 
            
            import matplotlib.pyplot as plt
            import numpy as np

            fig, ax = plt.subplots()
            x = np.linspace(0, 10, 100)
            line, = ax.plot(x, np.sin(x)) # Get the line object

            # Example of updating plot (more complex interactivity involves widgets)
            # def update(change): # Conceptual, would be tied to a widget
            #    line.set_ydata(np.sin(x * change.new))
            #    fig.canvas.draw_idle()
            
            # Simple plot that will be interactive with this backend
            ax.set_title("Interactive Plot with %matplotlib widget")
            ax.grid(True)
            # plt.show() # Often not needed with %matplotlib widget, plot appears directly
            ```

## Event Handling
Matplotlib has an event handling system that allows you to connect to events like mouse clicks, key presses, or pick events (clicking on an artist). This enables building custom interactive behaviors.

-   `fig.canvas.mpl_connect('event_name', callback_function)`
-   **Common Event Names:** `'button_press_event'`, `'button_release_event'`, `'motion_notify_event'`, `'key_press_event'`, `'pick_event'`.
-   **Callback Function:** A Python function that takes an `event` object as an argument and performs actions based on the event (e.g., update plot, print coordinates).

**Conceptual Example (Event Handling):**
```python
import matplotlib.pyplot as plt
import numpy as np

# fig, ax = plt.subplots()
# points, = ax.plot(np.random.rand(10), np.random.rand(10), 'o', picker=5) # picker=5 means pick event within 5 points

# def on_pick(event):
#     artist = event.artist
#     xmouse, ymouse = event.mouseevent.xdata, event.mouseevent.ydata
#     ind = event.ind
#     print(f"Picked point(s) at index: {ind}")
#     print(f"Data coordinates: X={artist.get_xdata()[ind]}, Y={artist.get_ydata()[ind]}")
#     print(f"Mouse coordinates: x={xmouse:.2f}, y={ymouse:.2f}\n")

# fig.canvas.mpl_connect('pick_event', on_pick)

# ax.set_title("Click on points to trigger pick event")
# plt.show()
```

## Matplotlib Widgets
Matplotlib also provides a basic set of GUI-neutral widgets (in `matplotlib.widgets`) like `Slider`, `Button`, `RadioButtons`, `CheckButtons`, `TextBox`. These can be used to control plot parameters interactively, but they are more involved to set up compared to using `ipywidgets` with `%matplotlib widget`.

**Example (Conceptual Slider):**
```python
# from matplotlib.widgets import Slider
# ... (setup plot) ...
# ax_slider = plt.axes([0.25, 0.02, 0.50, 0.03]) # Position for slider
# freq_slider = Slider(
#     ax=ax_slider,
#     label='Frequency',
#     valmin=0.1,
#     valmax=10.0,
#     valinit=1.0
# )
# def update_freq(val):
#     line.set_ydata(np.sin(val * x)) # Assuming 'line' and 'x' are defined
#     fig.canvas.draw_idle()
# freq_slider.on_changed(update_freq)
# plt.show()
```

## Limitations Compared to Web-Native Libraries
-   **Web Embedding:** While plots can be saved as images (PNG, SVG) for web use, creating truly interactive web applications with Matplotlib typically requires integration with frameworks like Flask/Django and potentially custom JavaScript, or using the `ipympl` backend which renders to an HTML5 canvas. Libraries like [[Plotly_and_Plotly_Express|Plotly]], [[Bokeh_Library|Bokeh]], and [[Altair_Library|Altair]] are designed from the ground up for web-native interactivity and are generally easier for this purpose.
-   **Complexity of Advanced Interactivity:** Building complex interactive dashboards with many linked components and custom behaviors can be more involved in Matplotlib than with libraries specifically designed for such applications (e.g., Dash, Bokeh Server, Streamlit).

**Summary:**
Matplotlib offers good basic interactivity through its GUI backends and especially with the `ipympl` backend in Jupyter environments. For highly sophisticated, web-native interactive dashboards or applications, dedicated libraries like Plotly, Bokeh, or Altair are often more suitable. However, for scientific plotting where the primary output might be static figures but some level of exploration is needed, Matplotlib's interactive features are very useful.

---
````

Now I will update the `170_Data_Visualization/Matplotlib/_Matplotlib_MOC.md` to ensure all links are correct and point to the newly created or existing notes.

---
**Revised `170_Data_Visualization/Matplotlib/_Matplotlib_MOC.md`**

`````markdown

Filename: 170_Data_Visualization/Matplotlib/_Matplotlib_MOC.md
````markdown
---
tags: [matplotlib, python, plotting, data_visualization, library, moc, concept]
aliases: [Matplotlib Library MOC]
related:
  - "[[_Data_Visualization_MOC]]"
  - "[[_NumPy_MOC]]"
  - "[[_Pandas_MOC]]"
  - "[[Matplotlib_Overview]]"
  - "[[Matplotlib_Pyplot_API_vs_OO_API]]"
  - "[[Matplotlib_Figure_Subplot_Axes]]"
  - "[[Matplotlib_Basic_Plotting_Functions]]"
  - "[[Matplotlib_Customization]]"
  - "[[Matplotlib_Image_Display_imshow]]"
  - "[[Matplotlib_Colormaps]]"
  - "[[Matplotlib_3D_Plotting]]"
  - "[[Matplotlib_Interactive_Plots]]"
  - "[[Matplotlib_Saving_Plots]]"
  - "[[Matplotlib_Styles]]"
worksheet: [WS_DataViz_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Matplotlib MOC 🎨

**[[Matplotlib_Overview|Matplotlib]]** is a comprehensive library for creating static, animated, and interactive visualizations in Python. It is the foundational plotting library in the Python scientific computing stack.

## Core Concepts & Usage
-   [[Matplotlib_Overview|Overview of Matplotlib]]
-   [[Matplotlib_Pyplot_API_vs_OO_API|Pyplot API vs. Object-Oriented API]]
    -   [[Matplotlib_Pyplot_API|Pyplot API (State-Based)]]
    -   [[Matplotlib_Object_Oriented_API|Object-Oriented API]]
-   [[Matplotlib_Figure_Subplot_Axes|Figure, Axes, and Subplots]]
    -   The fundamental building blocks of a Matplotlib plot.
-   [[Plot_Elements_Anatomy|Anatomy of a Plot]] (General, but heavily applicable here)

## Basic Plotting
-   [[Matplotlib_Basic_Plotting_Functions|Basic Plotting Functions Overview]]
    -   [[170_Data_Visualization/Plot_Types/Line_Plot|Line Plot]] (`plt.plot()` / `ax.plot()`)
    -   [[170_Data_Visualization/Plot_Types/Scatter_Plot|Scatter Plot]] (`plt.scatter()` / `ax.scatter()`)
    -   [[170_Data_Visualization/Plot_Types/Bar_Chart|Bar Chart]] (`plt.bar()` / `ax.bar()`, `plt.barh()` / `ax.barh()`)
    -   [[170_Data_Visualization/Plot_Types/Histogram|Histogram]] (`plt.hist()` / `ax.hist()`)
    -   [[170_Data_Visualization/Plot_Types/Box_Plot|Box Plot]] (`plt.boxplot()` / `ax.boxplot()`)
    -   [[170_Data_Visualization/Plot_Types/Pie_Chart|Pie Chart]] (`plt.pie()` / `ax.pie()`)
-   [[Matplotlib_Image_Display_imshow|Image Display with `imshow`]]

## Customization & Advanced Features
-   [[Matplotlib_Customization|Customizing Plots]]
    -   Titles, Labels, Legends
    -   Colors, Linestyles, Markers
    -   Ticks, Tick Labels, and Gridlines
    -   Text and Annotations
-   [[Matplotlib_Colormaps|Working with Colormaps (`cmap`)]]
-   [[Matplotlib_Saving_Plots|Saving Plots (`savefig`)]]
-   [[Matplotlib_Styles|Using Stylesheets (`plt.style`)]]
-   [[Matplotlib_3D_Plotting|3D Plotting with `mpl_toolkits.mplot3d`]]
-   [[Matplotlib_Interactive_Plots|Interactive Plotting]]

## Notes in this Section
```dataview
LIST
FROM "170_Data_Visualization/Matplotlib"
WHERE file.folder = this.file.folder AND file.name != this.file.name AND !contains(file.name, "MOC")
SORT file.name ASC
```

---
`````

This completes the creation of the Matplotlib-specific concept notes and the revision of the Matplotlib MOC with correct links. All linked notes should now exist.

Next, I will move on to the remaining questions from your "Data Visualization" chapter prompt. I'll create new notes for these or integrate answers into existing ones as appropriate.

---

Okay, let's address the remaining questions from your "Data Visualization" chapter prompt by creating new notes or integrating answers into existing ones.

---
**Addressing Remaining Data Visualization Questions:**

First, I'll create a note for `Tufte_Principles.md` as it was linked in `Data_Visualization_Principles.md`.

`````markdown

Filename: 170_Data_Visualization/Tufte_Principles.md
````markdown
---
tags: [data_visualization, design_principles, tufte, data_ink, chart_junk, concept]
aliases: [Edward Tufte Principles, Data-Ink Ratio, Chartjunk]
related:
  - "[[Data_Visualization_Principles]]"
  - "[[Data_Visualization_Importance]]"
worksheet: [WS_DataViz_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Edward Tufte's Principles of Data Visualization

Edward Tufte is a renowned statistician and professor emeritus of political science, statistics, and computer science at Yale University, famous for his writings on information design and data visualization. His principles emphasize clarity, precision, and efficiency in graphical displays.

## Key Principles and Concepts

[list2tab|#Tufte Principles]
- Data-Ink Ratio
    -   **Concept:** Tufte advocates for maximizing the "data-ink ratio."
        $$ \text{Data-Ink Ratio} = \frac{\text{Data-Ink}}{\text{Total ink used in graphic}} $$
        -   **Data-Ink:** The non-erasable core of a graphic, the ink devoted to representing the actual data values.
        -   **Non-Data-Ink:** Ink that does not represent data information, such as redundant grid lines, excessive decoration, or unnecessary frames.
    -   **Goal:** A large share of the ink on a graphic should present data information. Erase non-data-ink, within reason. Erase redundant data-ink.
    -   **Implication:** Strive for minimalism and avoid "chartjunk." Every visual element should serve a purpose in conveying data.
- Chartjunk
    -   **Concept:** Extraneous visual elements in charts and graphs that are not necessary to comprehend the information represented or that distract the viewer from this information.
    -   **Examples:**
        -   Unnecessary 3D effects (e.g., 3D pie charts, 3D bars when data is 2D).
        -   Moiré patterns or excessive background patterns.
        -   Overly ornate or decorative elements.
        -   Redundant grid lines or tick marks that don't aid interpretation.
    -   **Goal:** Eliminate chartjunk to improve clarity and focus on the data.
- Graphical Integrity
    -   **Concept:** Visual representations of data must be truthful and not misleading.
    -   **Principles:**
        -   The representation of numbers, as physically measured on the surface of the graphic itself, should be directly proportional to the numerical quantities represented. (Avoid lying with scale, e.g., truncated y-axes in bar charts).
        -   Clear, detailed, and thorough labeling should be used to defeat graphical distortion and ambiguity.
        -   Show data variation, not design variation.
        -   In time-series displays of money, deflated and standardized units of monetary measurement are nearly always better than nominal units.
        -   The number of information-carrying (variable) dimensions depicted should not exceed the number of dimensions in the data. (e.g., avoid using 3D for 2D data if it adds no information).
- Small Multiples (Faceting / Trellis Display)
    -   **Concept:** A series of similar small graphs or charts, drawn on the same scale and axes, allowing them to be easily compared. They typically vary along one or two categorical dimensions.
    -   **Usefulness:** Excellent for visualizing multivariate data by showing how relationships or distributions change across different conditions or categories. "Illustrations of postage-stamp size are indexed by category or a label, sequenced over time like the frames of a movie, or ordered by a quantitative variable not used in the single image itself."
    -   See also: [[Seaborn_Multi_Plot_Grids|Seaborn Multi-Plot Grids]].
- Sparklines
    -   **Concept:** Small, intense, word-sized graphics with typographic resolution. They are data-words.
    -   **Usefulness:** Embed rich data directly into text or tables, providing context without taking up much space. For example, a small line graph showing a stock trend next to its ticker symbol.
- Maximize Data Density
    -   **Concept:** Within reason, try to show as much data as possible in a given space, without clutter.
        $$ \text{Data Density of a Graphic} = \frac{\text{Number of entries in data matrix}}{\text{Area of data graphic}} $$
    -   **Goal:** Make efficient use of space to convey information. Small multiples are a good way to increase data density.

## Tufte's Design Goals (Summary)
-   Above all else, show the data.
-   Maximize the data-ink ratio.
-   Erase non-data-ink.
-   Erase redundant data-ink.
-   Revise and edit.

Tufte's principles have been highly influential in the field of data visualization, advocating for clarity, precision, and an elegant minimalism that puts the data first. While some of his stricter rules (like completely avoiding chartjunk) are debated, the core ideas of clarity and maximizing information content remain fundamental.

---
````

Now, addressing the specific questions. Some will go into new notes, others might be integrated if a suitable note already exists or is planned.

**New Notes for Specific Questions:**

`````markdown

Filename: 170_Data_Visualization/Anscombes_Quartet.md
````markdown
---
tags: [data_visualization, statistics, anscombes_quartet, summary_statistics, importance_of_plotting, concept, example]
aliases: [Anscombe's Quartet, Importance of Visualizing Data]
related:
  - "[[Data_Visualization_Importance]]"
  - "[[Descriptive_Statistics_Methods]]" # Summary statistics alone can be misleading
worksheet: [WS_DataViz_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Anscombe's Quartet

## Definition
**Anscombe's Quartet** comprises four datasets that have nearly identical simple descriptive statistics, yet appear very different when graphed. Each dataset consists of eleven $(x,y)$ points. The quartet was constructed in 1973 by the statistician Francis Anscombe to demonstrate the importance of **graphing data before analyzing it** and the effect of outliers and other influential observations on statistical properties.

## The Data
The four datasets are typically presented as follows:

| Dataset | X values (I, II, III) | Y values (I) | Y values (II) | Y values (III) | X values (IV) | Y values (IV) |
|---------|-----------------------|--------------|---------------|----------------|---------------|---------------|
| I       | 10.0                  | 8.04         | 9.14          | 7.46           | 8.0           | 6.58          |
| I       | 8.0                   | 6.95         | 8.14          | 6.77           | 8.0           | 5.76          |
| I       | 13.0                  | 7.58         | 8.74          | 12.74          | 8.0           | 7.71          |
| I       | 9.0                   | 8.81         | 8.77          | 7.11           | 8.0           | 8.84          |
| I       | 11.0                  | 8.33         | 9.26          | 7.81           | 8.0           | 8.47          |
| I       | 14.0                  | 9.96         | 8.10          | 8.84           | 8.0           | 7.04          |
| I       | 6.0                   | 7.24         | 6.13          | 6.08           | 8.0           | 5.25          |
| I       | 4.0                   | 4.26         | 3.10          | 5.39           | 19.0          | 12.50         |
| I       | 12.0                  | 10.84        | 9.13          | 8.15           | 8.0           | 5.56          |
| I       | 7.0                   | 4.82         | 7.26          | 6.42           | 8.0           | 7.91          |
| I       | 5.0                   | 5.68         | 4.74          | 5.73           | 8.0           | 6.89          |

## Nearly Identical Descriptive Statistics
For all four datasets:
-   Mean of $x$: $9.0$
-   Variance of $x$: $11.0$
-   Mean of $y$: $7.50$ (approximately)
-   Variance of $y$: $4.12$ (approximately)
-   Correlation between $x$ and $y$: $0.816$ (approximately)
-   Linear regression line: $y \approx 3.00 + 0.500x$ (approximately)
-   Coefficient of determination ($R^2$): $0.67$ (approximately)

If one were to only look at these summary statistics, one might conclude that the four datasets are very similar.

## Visual Differences
However, when plotted as [[170_Data_Visualization/Plot_Types/Scatter_Plot|scatter plots]], they reveal vastly different structures:

[list2tab|#Dataset Visuals]
- Dataset I
    -   **Appearance:** Consists of points that appear to follow a simple linear relationship with some scatter, fitting typical assumptions for linear regression.
    -   **Obsidian Chart (Conceptual - actual data points vary slightly):**
        ```chart
        type: scatter
        labels: ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10', 'P11']
        datasets:
          - label: 'Dataset I'
            data: [
                {x: 10, y: 8.04}, {x: 8, y: 6.95}, {x: 13, y: 7.58}, {x: 9, y: 8.81}, {x: 11, y: 8.33},
                {x: 14, y: 9.96}, {x: 6, y: 7.24}, {x: 4, y: 4.26}, {x: 12, y: 10.84}, {x: 7, y: 4.82}, {x: 5, y: 5.68}
            ]
            backgroundColor: 'rgba(0, 123, 255, 0.7)'
        options: { title: { display: true, text: 'Anscombe I: Linear with Scatter' } }
        ```
- Dataset II
    -   **Appearance:** The relationship between $x$ and $y$ is clearly non-linear (quadratic). A straight line regression is inappropriate.
    -   **Obsidian Chart (Conceptual):**
        ```chart
        type: scatter
        datasets:
          - label: 'Dataset II'
            data: [
                {x: 10, y: 9.14}, {x: 8, y: 8.14}, {x: 13, y: 8.74}, {x: 9, y: 8.77}, {x: 11, y: 9.26},
                {x: 14, y: 8.10}, {x: 6, y: 6.13}, {x: 4, y: 3.10}, {x: 12, y: 9.13}, {x: 7, y: 7.26}, {x: 5, y: 4.74}
            ]
            backgroundColor: 'rgba(255, 99, 132, 0.7)'
        options: { title: { display: true, text: 'Anscombe II: Non-linear (Quadratic)' } }
        ```
- Dataset III
    -   **Appearance:** The relationship is perfectly linear, but there is one significant outlier that skews the regression line and correlation. Without the outlier, the correlation would be much stronger and the regression line different.
    -   **Obsidian Chart (Conceptual):**
        ```chart
        type: scatter
        datasets:
          - label: 'Dataset III'
            data: [
                {x: 10, y: 7.46}, {x: 8, y: 6.77}, {x: 13, y: 12.74}, {x: 9, y: 7.11}, {x: 11, y: 7.81},
                {x: 14, y: 8.84}, {x: 6, y: 6.08}, {x: 4, y: 5.39}, {x: 12, y: 8.15}, {x: 7, y: 6.42}, {x: 5, y: 5.73}
            ]
            backgroundColor: 'rgba(75, 192, 192, 0.7)'
        options: { title: { display: true, text: 'Anscombe III: Linear with Outlier' } }
        ```
- Dataset IV
    -   **Appearance:** All $x$ values are the same except for one outlier which has a very high $x$ value. This single point exerts high leverage and determines the regression line. There's no clear relationship among the other points.
    -   **Obsidian Chart (Conceptual):**
        ```chart
        type: scatter
        datasets:
          - label: 'Dataset IV'
            data: [
                {x: 8, y: 6.58}, {x: 8, y: 5.76}, {x: 8, y: 7.71}, {x: 8, y: 8.84}, {x: 8, y: 8.47},
                {x: 8, y: 7.04}, {x: 8, y: 5.25}, {x: 19, y: 12.50}, {x: 8, y: 5.56}, {x: 8, y: 7.91}, {x: 8, y: 6.89}
            ]
            backgroundColor: 'rgba(255, 159, 64, 0.7)'
        options: { title: { display: true, text: 'Anscombe IV: High Leverage Point' } }
        ```

## Lesson
Anscombe's Quartet powerfully illustrates that **summary statistics alone are not sufficient to understand a dataset.** Visualizing data is essential to:
-   Identify the underlying structure and relationships.
-   Detect outliers or influential points.
-   Assess the appropriateness of statistical models (e.g., linear regression).
-   Avoid drawing incorrect conclusions based solely on numerical summaries.

It underscores the importance of [[Exploratory_Data_Analysis_Workflow|Exploratory Data Analysis (EDA)]] and the critical role of [[Data_Visualization_Importance|data visualization]] in the analytical process.

---
````

`````markdown

Filename: 170_Data_Visualization/Additional_Plot_Types.md
````markdown
---
tags: [data_visualization, plotting, advanced_plots, area_chart, bubble_chart, treemap, concept]
aliases: [More Plot Types, Other Visualizations]
related:
  - "[[_Data_Visualization_MOC]]"
  - "[[Choosing_the_Right_Plot]]"
worksheet: [WS_DataViz_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Additional Plot Types and Scenarios

Beyond the most common plots, many other visualization types serve specific purposes. Here are three examples not previously detailed, along with scenarios and considerations.

>[!question] Come up with 3 types of plots not mentioned above, and answer the same questions (scenario, usefulness, best way?).

[list2tab|#Additional Plots]
- 1. Area Chart (Stacked Area Chart)
    -   **Definition:** An area chart is like a [[170_Data_Visualization/Plot_Types/Line_Plot|line chart]] but with the area below the line(s) filled with color or shading. A **stacked area chart** displays the contribution of different parts to a whole over time or another continuous variable. Each constituent part is stacked on top of the previous one.
    -   **Scenario:** Visualizing the change in an e-commerce company's revenue sources (e.g., 'Online Sales', 'In-Store Sales', 'Subscription Services') over several quarters. We want to see both the trend of each source and the trend of the total revenue.
    -   **Usefulness:**
        -   Shows the trend of a total and the changing contribution of its parts over a continuous axis (usually time).
        -   Good for illustrating how a whole is divided into parts that change over time.
    -   **Best Way?:**
        -   **Yes, for showing part-to-whole relationships changing over a continuous axis, a stacked area chart is often a very good choice.** It clearly shows the total and the magnitude of each component.
        -   **Considerations:**
            -   Can become cluttered if there are too many categories (parts).
            -   It can be difficult to accurately compare the trends of individual components that are not at the baseline, as their baseline changes.
            -   A 100% stacked area chart (where the y-axis goes up to 100%) is good for showing changing proportions over time, rather than absolute magnitudes.
        -   **Alternatives:** Grouped [[170_Data_Visualization/Plot_Types/Bar_Chart|bar charts]] can show components per time period but might not emphasize the continuous trend or total as well. Multiple line charts can show individual trends but not the part-to-whole composition.
    -   **Obsidian Chart Plugin Example (Illustrative Stacked Area):**
        > [!note] Chart.js (used by Obsidian Charts) supports stacked area charts by setting `fill: true` and `stacked: true` on line chart datasets.
        ```chart
        type: line
        labels: ['Q1 2022', 'Q2 2022', 'Q3 2022', 'Q4 2022', 'Q1 2023']
        datasets:
          - label: 'Online Sales'
            data: # Conceptual data
            backgroundColor: 'rgba(54, 162, 235, 0.5)' # Blue
            borderColor: 'rgba(54, 162, 235, 1)'
            fill: true
            tension: 0.1
          - label: 'In-Store Sales'
            data: 
            backgroundColor: 'rgba(255, 99, 132, 0.5)' # Red
            borderColor: 'rgba(255, 99, 132, 1)'
            fill: true
            tension: 0.1
          - label: 'Subscription Services'
            data: 
            backgroundColor: 'rgba(75, 192, 192, 0.5)' # Teal
            borderColor: 'rgba(75, 192, 192, 1)'
            fill: true
            tension: 0.1
        options:
          responsive: true
          plugins:
            title: { display: true, text: 'Revenue Sources Over Time (Stacked Area)' }
            tooltip: { mode: 'index', intersect: false }
          scales:
            x: { title: { display: true, text: 'Quarter' } }
            y: { stacked: true, title: { display: true, text: 'Revenue ($)' }, min: 0 }
        ```
- 2. Bubble Chart
    -   **Definition:** A bubble chart is a variation of a [[170_Data_Visualization/Plot_Types/Scatter_Plot|scatter plot]] where data points are replaced with bubbles, and an additional dimension of the data is represented by the **size** of the bubbles. It can display three dimensions of data (x-position, y-position, size). A fourth dimension can be added with color.
    -   **Scenario:** Analyzing marketing campaigns for different e-commerce products. We want to visualize `cost_per_campaign` (x-axis), `conversion_rate` (y-axis), and `total_reach` (bubble size) for each campaign. We could also color bubbles by `product_category`.
    -   **Usefulness:**
        -   Allows visualization of three or four dimensions simultaneously on a 2D plot.
        -   Good for comparing entities based on multiple attributes, especially when one attribute represents magnitude or importance (mapped to size).
    -   **Best Way?:**
        -   **Yes, for comparing three numerical variables where one clearly represents a "size" or "weight" aspect, a bubble chart is a very effective choice.** If a fourth categorical dimension needs to be shown, color is a good addition.
        -   **Considerations:**
            -   Too many bubbles or too much overlap can make it hard to read.
            -   Accurate perception of bubble area/size can be tricky for humans; ensure clear scaling and legend for size.
            -   Avoid using bubble size for variables that don't have a clear magnitude interpretation.
        -   **Alternatives:** A [[170_Data_Visualization/Plot_Types/Scatter_Plot_Matrix|scatter plot matrix]] could show all pairwise 2D relationships but wouldn't combine three variables into one view as directly. 3D scatter plots are an option but have their own interpretation challenges.
    -   **Obsidian Chart Plugin Example (Illustrative Bubble Chart):**
        > [!note] Chart.js scatter plots can represent bubble charts by varying `pointRadius` or `pointStyle` properties based on data.
        ```chart
        type: bubble // Or scatter with varying pointRadius
        datasets:
          - label: 'Campaign A (Electronics)'
            data: [ {x: 500, y: 0.05, r: 20} ] # x=cost, y=conversion, r=reach (mapped to radius)
            backgroundColor: 'rgba(255, 99, 132, 0.7)'
          - label: 'Campaign B (Books)'
            data: [ {x: 200, y: 0.08, r: 10} ]
            backgroundColor: 'rgba(54, 162, 235, 0.7)'
          - label: 'Campaign C (Electronics)'
            data: [ {x: 1000, y: 0.03, r: 30} ]
            backgroundColor: 'rgba(255, 99, 132, 0.5)' # Same color as A for same category
          - label: 'Campaign D (Home Goods)'
            data: [ {x: 300, y: 0.06, r: 15} ]
            backgroundColor: 'rgba(75, 192, 192, 0.7)'
        options:
          responsive: true
          plugins:
            title: { display: true, text: 'Marketing Campaign Performance (Bubble Chart)' }
            tooltip: { callbacks: { label: function(c) { return `${c.dataset.label}: Cost $${c.raw.x}, Conv ${c.raw.y*100}%, Reach ${c.raw.r*1000}`; } } }
          scales:
            x: { title: { display: true, text: 'Campaign Cost ($)' } }
            y: { title: { display: true, text: 'Conversion Rate' } }
          elements: { point: { radius: function(ctx) { const size = ctx.raw.r; return size; } } } // Dynamically set radius
        ```
- 3. Treemap
    -   **Definition:** A treemap displays hierarchical (tree-structured) data as a set of nested rectangles. Each branch of the tree is given a rectangle, which is then tiled with smaller rectangles representing sub-branches. The area of each rectangle is typically proportional to a specified dimension of the data.
    -   **Scenario:** Visualizing the sales breakdown of an e-commerce store, starting from overall sales, then by product category (e.g., 'Electronics', 'Clothing'), then by sub-category (e.g., 'Laptops', 'Shirts'), and finally by individual product. The area of each rectangle represents its proportion of sales.
    -   **Usefulness:**
        -   Excellent for showing hierarchical data and part-to-whole relationships at multiple levels simultaneously.
        -   Can effectively display a large number of categories and their relative sizes.
        -   Color can be used to encode another dimension (e.g., sales growth rate).
    -   **Best Way?:**
        -   **Yes, for visualizing hierarchical data where you want to show the proportion of parts within a whole at multiple levels, a treemap is a very strong and often the best choice.**
        -   **Considerations:**
            -   Not good for showing precise comparisons between non-adjacent rectangles, especially if areas are similar.
            -   Can become cluttered if the hierarchy is too deep or there are too many very small items.
            -   Not ideal for showing trends over time.
        -   **Alternatives:** Sunburst charts are similar for hierarchical data but use a radial layout. Nested [[170_Data_Visualization/Plot_Types/Pie_Chart|pie charts]] (donuts) can show a couple of levels but quickly become hard to read. Stacked [[170_Data_Visualization/Plot_Types/Bar_Chart|bar charts]] can show one level of hierarchy well.
    -   **Obsidian Chart Plugin Example (Illustrative Treemap):**
        > [!note] Treemaps are a specialized chart type not directly supported by basic Chart.js (and thus likely not by the standard Obsidian Charts plugin). Libraries like Plotly, Highcharts, or D3.js are typically used. This is a conceptual description.

        ```
        Conceptual Data for Treemap (Sales Hierarchy):

        - Total Sales (Root Rectangle)
            - Electronics (Sub-Rectangle, area proportional to electronics sales)
                - Laptops (Sub-sub-rectangle within Electronics)
                - Smartphones
                - Accessories
            - Clothing (Sub-Rectangle)
                - Shirts
                - Pants
            - Books (Sub-Rectangle)

        (Imagine nested rectangles where the size of each rectangle represents its sales contribution.
        Colors could represent product categories or sales growth.)
        ```
        *Actual treemap requires specialized plotting libraries.*

These additional plot types expand the toolkit for visualizing different kinds of data structures and relationships.

---
`````

I've created notes for "Anscombe's Quartet" and "Additional Plot Types" (Area Chart, Bubble Chart, Treemap), including scenarios, usefulness, and whether they are the best choice, along with illustrative chart examples or descriptions for the Obsidian Charts plugin.

I will now review the remaining questions from your list and integrate answers or create specific notes as needed. Key remaining questions seem to be about Matplotlib API differences (which is partially covered in `Matplotlib_Pyplot_API_vs_OO_API.md` but can be expanded), and general visualization importance/limitations (covered in `Data_Visualization_Importance.md`).

Let me know if you want me to specifically address any other of the original questions in more detail or create dedicated notes for them. Otherwise, I'll assume the current set of notes covers the essence of the "Data Visualization" chapter request.

---

[[altair]]