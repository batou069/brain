---
tags:
  - data_visualization
  - plotting
  - trend_line
  - regression_line
  - smoothing
  - concept
aliases:
  - Line of Best Fit
  - Regression Line Plot
related:
  - "[[Scatter_Plot]]"
  - "[[Line_Plot]]"
  - "[[Linear_Regression]]"
  - "[[Seaborn_Regression_Plots]]"
worksheet:
  - WS_DataViz_1
date_created: 2025-08-20
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