---
tags:
  - data_visualization
  - plotting
  - chart_selection
  - best_practices
  - concept
aliases:
  - Selecting Plot Types
  - Chart Chooser
related:
  - "[[_Data_Visualization_MOC]]"
  - "[[Data_Visualization_Principles]]"
  - "[[Categorical_vs_Numerical_Data_Visualization]]"
  - "[[Line_Plot]]"
  - "[[Scatter_Plot]]"
  - "[[Bar_Chart]]"
  - "[[Histogram]]"
  - "[[Box_Plot]]"
  - "[[Pie_Chart]]"
  - "[[Heatmap]]"
  - "[[Violin_Plot]]"
worksheet:
  - WS_DataViz_1
date_created: 2025-06-03
---
# Choosing the Right Plot Type

Selecting the appropriate plot type is crucial for effectively communicating insights from your data. The choice depends on several factors, including:
-   **The type of data you have:** Categorical, numerical, time-series, geospatial, etc. (See [[Categorical_vs_Numerical_Data_Visualization]])
-   **The message you want to convey:** Are you showing a comparison, relationship, distribution, or composition?
-   **Your audience:** Their level of data literacy.
-   **The number of variables** you want to display.

>[!question] For each type of plot mentioned above, come up with a scenario where it would be useful. For each scenario you matched with a plot type, is this plot the best way to visualize this scenario?

Here's an analysis of common plot types, their use cases, and whether they are typically the "best" choice:

[list2tab|#Plot Types & Scenarios]
- Line Plot
	[[Line_Plot|Line Plot]]
    - **Scenario:** Tracking the daily closing price of a particular stock over a year to observe trends, seasonality, or significant events.
    - **Usefulness:** Excellent for showing trends in continuous data over an ordered sequence (especially time). Clearly visualizes increases, decreases, and volatility.
    - **Best Way?:** Yes, for showing trends over time, a line plot is generally the best and most standard choice. Candlestick charts or OHLC charts provide more detail for financial data but are more complex.
- Scatter Plot
	[[Scatter_Plot|Scatter Plot]]
    - **Scenario:** Investigating the relationship between hours spent studying and exam scores for a group of students. Each student is a point.
    - **Usefulness:** Ideal for visualizing the relationship (correlation, clusters, outliers) between two numerical variables.
    - **Best Way?:** Yes, for exploring the relationship between two continuous numerical variables, a scatter plot is the primary choice. Adding a [[Trend_Line|regression line]] can further quantify the relationship.
- Histogram
	[[Histogram|Histogram]]
    - **Scenario:** Understanding the distribution of ages of customers visiting a store.
    - **Usefulness:** Shows the frequency distribution of a single numerical variable by dividing it into bins. Helps identify shape (skewness, modality), central tendency, and spread.
    - **Best Way?:** Yes, for visualizing the distribution of a single numerical variable, a histogram is the standard and most effective method. Kernel Density Estimates (KDEs) can provide a smoother representation but might obscure bin-level details.
- Box Plot
	[[Box_Plot|Box Plot]]
    - **Scenario:** Comparing the distribution of salaries across different departments (e.g., Sales, Engineering, HR) in a company.
    - **Usefulness:** Provides a concise summary of a numerical variable's distribution (median, quartiles, range, outliers) and is excellent for comparing these distributions across multiple categories.
    - **Best Way?:** Very good for comparing distributions, especially when focusing on medians and spread. [[Violin_Plot|Violin plots]] are a good alternative as they also show the shape of the distribution (like a KDE) alongside the box plot summary. For fewer categories or if individual data points are important, strip plots or swarm plots might be considered.
- Heatmap
	[[Heatmap|Heatmap]]
    - **Scenario:** Visualizing a correlation matrix between multiple features in a dataset, where cell color intensity represents the strength and direction of correlation.
    - **Usefulness:** Excellent for displaying the magnitude of a phenomenon across two discrete dimensions (or a matrix). Color intensity makes patterns and clusters apparent.
    - **Best Way?:** Yes, for visualizing matrices of values like correlation matrices, confusion matrices, or co-occurrence data, heatmaps are a very effective and standard choice. Annotating cells with values can enhance readability.
- Bar Chart
	[[Bar_Chart|Bar Chart]]
    - **Scenario:** Comparing the total sales figures for five different product categories in a quarter.
    - **Usefulness:** Ideal for comparing the magnitude of a numerical variable across discrete categories. Easy to read and interpret exact values.
    - **Best Way?:** Yes, for comparing quantities across a manageable number of distinct categories, bar charts (vertical or horizontal) are generally the best. If showing parts of a whole for each category, a stacked or grouped bar chart can be used. [[Pie_Chart|Pie charts]] are an alternative for parts of a whole but are less effective for comparison.
- Pie Chart
	[[Pie_Chart|Pie Chart]]
    - **Scenario:** Showing the percentage breakdown of a website's traffic sources (e.g., Organic Search, Direct, Referral, Social Media) for a specific month, where the total traffic is 100%.
    - **Usefulness:** Represents parts of a whole (proportions or percentages). Each slice's angle is proportional to its value.
    - **Best Way?:** Generally **not the best way** if precise comparison between categories is needed, or if there are more than 3-5 categories. Human perception is poor at accurately comparing angles and areas of slices. A [[Bar_Chart|bar chart]] (especially a horizontal one sorted by value) is often a more effective alternative for showing proportions and allowing easier comparison. Pie charts are best used when emphasizing a simple part-to-whole relationship with very few categories.
- Trend Line
	[[Trend_Line|Trend Line (Regression Line)]]
    - **Scenario:** Added to a [[Scatter_Plot|scatter plot]] of study hours vs. exam scores to visualize the general linear trend and estimate the strength of the linear relationship.
    - **Usefulness:** Helps to visualize the direction and strength of a relationship between two numerical variables, often derived from a regression model.
    - **Best Way?:** When used in conjunction with a scatter plot, yes, it's an excellent way to highlight a linear (or other specified model) trend. It's an augmentation, not a standalone plot type for raw data.
- Violin Plot
	[[Violin_Plot|Violin Plot]]
    - **Scenario:** Comparing the distribution of customer satisfaction scores (e.g., on a 1-10 scale) for different product versions, wanting to see both summary statistics and the shape of the distributions.
    - **Usefulness:** Combines features of a [[Box_Plot|box plot]] (showing median, quartiles) with a Kernel Density Estimate (KDE), providing a richer view of the distribution's shape (modality, skewness).
    - **Best Way?:** Often better than a simple box plot if the shape of the distribution is important, as box plots can hide multimodality. For comparing distributions across categories, it's a very strong choice.

## General Guidance for Plot Selection
1.  **What is the primary message?**
    *   **Comparison:** Bar chart, grouped bar chart, line plot (for trends over categories).
    *   **Relationship/Correlation:** Scatter plot, heatmap (for multiple variables), bubble chart.
    *   **Distribution:** Histogram, KDE plot, box plot, violin plot, ECDF plot.
    *   **Composition (Part-to-whole):** Pie chart (use sparingly), stacked bar chart, treemap, area chart.
2.  **How many variables are involved?**
    *   **One variable (Univariate):** Histogram, box plot, KDE (numerical); bar chart, pie chart (categorical).
    *   **Two variables (Bivariate):** Scatter plot, line plot, bar chart (one categorical, one numerical), heatmap.
    -   **Three or more variables (Multivariate):** Use color, size, shape encoding on scatter/bubble charts, 3D plots (use with caution), facet grids (small multiples), pair plots. See [[Visualizing_Multidimensional_Data]].
3.  **What type of data are the variables?**
    *   See [[Categorical_vs_Numerical_Data_Visualization]].

Always aim for clarity and avoid misleading representations. It's often useful to try a few different plot types for the same data to see which one best conveys the intended insight.

---