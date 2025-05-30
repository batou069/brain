---
tags:
  - data_science
  - data_visualization
  - eda
  - matplotlib
  - seaborn
  - pandas
  - concept
aliases:
  - EDA Visualization
  - Plotting for EDA
related:
  - "[[Exploratory_Data_Analysis_Workflow]]"
  - "[[Matplotlib]]"
  - "[[Pyplot_API]]"
  - "[[Figure_Subplot_Axes]]"
  - "[[Seaborn]]"
  - "[[140_Data_Science_AI/Pandas/Pandas_Plotting]]"
  - "[[Pandas_DataFrame]]"
  - "[[Matplotlib_Advanced_Styling]]"
  - "[[Matplotlib_Heatmaps]]"
  - "[[Matplotlib_Contour_Plots]]"
  - "[[Matplotlib_3D_Plotting]]"
worksheet:
  - WS_DS_Workflow_Concepts_1
date_created: 2025-05-30
---
# Data Visualization for Exploratory Data Analysis (EDA)

Data visualization is a cornerstone of [[Exploratory_Data_Analysis_Workflow|Exploratory Data Analysis (EDA)]]. It involves creating graphical representations of data to understand trends, patterns, relationships, and outliers that might not be apparent from summary statistics alone. Effective visualizations can significantly accelerate the understanding of a dataset and guide subsequent analysis and modeling steps.

## Why Visualize Data in EDA?
- **Identify Patterns & Trends:** Spot correlations, seasonality, clusters, etc.
- **Detect Outliers & Anomalies:** Unusual data points often stand out visually.
- **Understand Data Distributions:** Assess skewness, modality, and spread of variables.
- **Verify Assumptions:** Visually check assumptions for statistical tests or models (e.g., normality, linearity).
- **Communicate Findings:** Visualizations are powerful tools for sharing insights with others.
- **Guide Feature Engineering:** Visual exploration can suggest new features to create or transformations to apply.

## Key Libraries for Visualization in Python
- **[[Matplotlib]]:** The foundational plotting library in Python. Offers extensive control over every aspect of a plot but can be verbose for complex statistical plots. (See [[Pyplot_API]], [[Figure_Subplot_Axes]])
- **[[Seaborn]]:** Built on top of Matplotlib, Seaborn provides a high-level interface for drawing attractive and informative statistical graphics. It integrates well with [[Pandas_DataFrame|Pandas DataFrames]] and simplifies the creation of common EDA plots.
- **[[140_Data_Science_AI/Pandas/Pandas_Plotting|Pandas Built-in Plotting]]:** DataFrame and Series objects have a `.plot()` method that acts as a convenient wrapper around Matplotlib for quick and easy visualizations.

## Common Plot Types for EDA and Their Uses

[list2card|addClass(ab-col1)|#Common EDA Plots]
- **Univariate Analysis (Analyzing Single Variables)**
    - **Histograms**
        - **Purpose:** Show the distribution of a single numerical variable by dividing data into bins and counting occurrences.
        - **Tools:** `plt.hist()`, `df['col'].hist()`, `sns.histplot()`
        - **Insights:** Shape of distribution (normal, skewed, bimodal), central tendency, spread, presence of outliers.
        ```python
        # import matplotlib.pyplot as plt
        # import seaborn as sns
        # import pandas as pd
        # data = pd.Series([1,1,2,2,2,3,3,4,5,6,7,7,7,7,8])
        # sns.histplot(data, kde=True) # kde adds a Kernel Density Estimate
        # plt.title("Histogram with KDE")
        # plt.show()
        ```
    - **Density Plots (Kernel Density Estimate - KDE)**
        - **Purpose:** A smoothed version of a histogram, useful for visualizing the shape of a distribution.
        - **Tools:** `df['col'].plot(kind='kde')`, `sns.kdeplot()`
        - **Insights:** Similar to histograms, but can be better for comparing distributions.
    - **Box Plots (Box-and-Whisker Plots)**
        - **Purpose:** Display the five-number summary of a numerical variable (minimum, first quartile (Q1), median (Q2), third quartile (Q3), maximum) and potential outliers.
        - **Tools:** `plt.boxplot()`, `df.boxplot()`, `sns.boxplot()`
        - **Insights:** Central tendency, spread (IQR = Q3 - Q1), skewness, identification of outliers.
        ```python
        # sns.boxplot(y=data)
        # plt.title("Box Plot")
        # plt.show()
        ```
    - **Bar Charts / Count Plots**
        - **Purpose:** Show the frequency of each category in a categorical variable.
        - **Tools:** `df['cat_col'].value_counts().plot(kind='bar')`, `sns.countplot(x='cat_col', data=df)`
        - **Insights:** Most/least common categories, distribution of categorical data.
- **Bivariate Analysis (Analyzing Relationships Between Two Variables)**
    - **Scatter Plots**
        - **Purpose:** Show the relationship between two numerical variables. Each point represents an observation.
        - **Tools:** `plt.scatter()`, `df.plot(kind='scatter', x='col1', y='col2')`, `sns.scatterplot()`
        - **Insights:** Correlation (positive, negative, none), linearity, clusters, outliers.
        ```python
        # df_scatter = pd.DataFrame({'x': range(20), 'y': range(20) + np.random.randn(20)*2})
        # sns.scatterplot(x='x', y='y', data=df_scatter)
        # plt.title("Scatter Plot")
        # plt.show()
        ```
    - **Line Plots**
        - **Purpose:** Typically used to show trends over time (time series data) or the relationship between two ordered numerical variables.
        - **Tools:** `plt.plot()`, `df['col'].plot()`, `sns.lineplot()`
        - **Insights:** Trends, seasonality, cycles.
    - **Heatmaps (for Correlation Matrices)**
        - **Purpose:** Visualize a matrix of values (e.g., a correlation matrix) where colors represent magnitudes. (See [[Matplotlib_Heatmaps]])
        - **Tools:** `sns.heatmap(df.corr(), annot=True, cmap='coolwarm')`
        - **Insights:** Quickly identify strong/weak positive/negative correlations between pairs of numerical variables.
        ```python
        # df_corr = pd.DataFrame(np.random.rand(5,3), columns=['A','B','C'])
        # correlation_matrix = df_corr.corr()
        # sns.heatmap(correlation_matrix, annot=True, cmap='viridis')
        # plt.title("Correlation Heatmap")
        # plt.show()
        ```
    - **Box Plots per Category**
        - **Purpose:** Compare the distribution of a numerical variable across different categories of a categorical variable.
        - **Tools:** `sns.boxplot(x='cat_col', y='num_col', data=df)`
        - **Insights:** Differences in central tendency, spread, and outliers of the numerical variable for each category.
    - **Violin Plots**
        - **Purpose:** Similar to box plots but also show the probability density of the data at different values (like a density plot mirrored).
        - **Tools:** `sns.violinplot(x='cat_col', y='num_col', data=df)`
        - **Insights:** Provides more detail about the shape of the distribution for each category compared to a box plot.
    - **Stacked/Grouped Bar Charts (for two categorical variables)**
        - **Purpose:** Show the relationship or joint distribution of two categorical variables.
        - **Tools:** `pd.crosstab(df.cat1, df.cat2).plot(kind='bar', stacked=True)`
        - **Insights:** Proportions or counts of one categorical variable within each category of another.
- **Multivariate Analysis (Analyzing More Than Two Variables)**
    - **Pair Plots (Scatter Plot Matrix)**
        - **Purpose:** Create a grid of scatter plots for all pairs of numerical variables in a DataFrame. Histograms or density plots are often shown on the diagonal.
        - **Tools:** `sns.pairplot(df, hue='cat_col')` (can use `hue` to add a categorical dimension)
        - **Insights:** Provides a quick overview of pairwise relationships across many variables.
    - **Scatter Plots with Hue/Size/Style Encoding**
        - **Purpose:** Add more dimensions to a scatter plot by encoding additional variables using color (`hue`), marker size (`size`), or marker style (`style`).
        - **Tools:** `sns.scatterplot(x='col1', y='col2', hue='cat_col', size='num_col3', style='cat_col2', data=df)`
    - **3D Plots**
        - **Purpose:** Visualize relationships between three numerical variables. (See [[Matplotlib_3D_Plotting]])
        - **Tools:** `mpl_toolkits.mplot3d`
        - **Insights:** Can reveal complex interactions, but can also be hard to interpret. Use judiciously.

## Principles for Effective EDA Visualization
- **Choose the Right Plot:** Select a plot type appropriate for the data types and the question you are trying to answer.
- **Label Clearly:** Always include titles, axis labels (with units if applicable), and legends.
- **Keep it Simple:** Avoid clutter. Too much information on one plot can be overwhelming.
- **Use Color Effectively:** Use color mudanças to highlight patterns or distinguish categories, but be mindful of color blindness and avoid using too many colors.
- **Iterate:** Don't expect to create the perfect plot on the first try. Experiment with different plot types and parameters.
- **Context is Key:** Interpret visualizations within the context of the data and the problem domain.

By systematically applying these visualization techniques, data scientists can gain deep insights from their data, forming a solid foundation for further analysis and model building. [[Matplotlib_Advanced_Styling]] can be used to further customize plots for reports or presentations.

---