
[list2tab]
- Univariate Analysis
	Analyzing Single Variables
	[list2table]
	 - **Histograms**
	     - **Purpose:** Show the distribution of a single numerical variable by dividing data into bins and counting occurrences.
		     - **Tools:** `plt.hist()`, `df['col'].hist()`, `sns.histplot()`
			      - **Insights:** Shape of distribution (normal, skewed, bimodal), central tendency, spread, presence of outliers.
			       - ```python
			       import matplotlib.pyplot as plt
			       import seaborn as sns
			       import pandas as pd
			       data = pd.Series([1,1,2,2,2,3,3,4,5,6,7,7,7,7,8])
			       sns.histplot(data, kde=True) # kde adds a Kernel Density Estimate
			       plt.title("Histogram with KDE")
			       plt.show()
					```
		- **Density Plots<br>(Kernel Density Estimate - KDE)**
			- **Purpose:** A smoothed version of a histogram, useful for visualizing the shape of a distribution.
				- **Tools:** `df['col'].plot(kind='kde')`, `sns.kdeplot()`
				    - **Insights:** Similar to histograms, but can be better for comparing distributions.
		- **Box Plots<br>(Box-and-Whisker Plots)**
		        - **Purpose:** Display the five-number summary of a numerical variable (minimum, first quartile (Q1), median (Q2), third quartile (Q3), maximum) and potential outliers.
			        - **Tools:** `plt.boxplot()`, `df.boxplot()`, `sns.boxplot()`
				        - **Insights:** Central tendency, spread (IQR = Q3 - Q1), skewness, identification of outliers.
					        ```python
					        sns.boxplot(y=data)
					        plt.title("Box Plot")
					        plt.show()
					        ```
	    - **Bar Charts / Count Plots**
	        - **Purpose:** Show the frequency of each category in a categorical variable.
		        - **Tools:** `df['cat_col'].value_counts().plot(kind='bar')`, `sns.countplot(x='cat_col', data=df)`
			        - **Insights:** Most/least common categories, distribution of categorical data.
- Bivariate Analysis 
	### Analyzing Relationships Between Two Variables
    - **Scatter Plots**
        - **Purpose:** Show the relationship between two numerical variables. Each point represents an observation.
        - **Tools:** `plt.scatter()`, `df.plot(kind='scatter', x='col1', y='col2')`, `sns.scatterplot()`
        - **Insights:** Correlation (positive, negative, none), linearity, clusters, outliers.
        ```python
        df_scatter = pd.DataFrame({'x': range(20), 'y': range(20) + np.random.randn(20)*2})
        sns.scatterplot(x='x', y='y', data=df_scatter)
        plt.title("Scatter Plot")
        plt.show()
        ```
    - **Line Plots**
        - **Purpose:** Typically used to show trends over time (time series data) or the relationship between two ordered numerical variables.
        - **Tools:** `plt.plot()`, `df['col'].plot()`, `sns.lineplot()`
        - **Insights:** Trends, seasonality, cycles.
    - **Heatmaps<br>(for Correlation Matrices)**
        - **Purpose:** Visualize a matrix of values (e.g., a correlation matrix) where colors represent magnitudes. (See [[Matplotlib_Heatmaps]])
        - **Tools:** `sns.heatmap(df.corr(), annot=True, cmap='coolwarm')`
        - **Insights:** Quickly identify strong/weak positive/negative correlations between pairs of numerical variables.
        ```python
        df_corr = pd.DataFrame(np.random.rand(5,3), columns=['A','B','C'])
        correlation_matrix = df_corr.corr()
        sns.heatmap(correlation_matrix, annot=True, cmap='viridis')
        plt.title("Correlation Heatmap")
        plt.show()
        ```
    - **Box Plots per Category**
        - **Purpose:** Compare the distribution of a numerical variable across different categories of a categorical variable.
        - **Tools:** `sns.boxplot(x='cat_col', y='num_col', data=df)`
        - **Insights:** Differences in central tendency, spread, and outliers of the numerical variable for each category.
    - **Violin Plots**
        - **Purpose:** Similar to box plots but also show the probability density of the data at different values (like a density plot mirrored).
        - **Tools:** `sns.violinplot(x='cat_col', y='num_col', data=df)`
        - **Insights:** Provides more detail about the shape of the distribution for each category compared to a box plot.
    - **Stacked/Grouped Bar Charts<br>(for two categorical variables)**
        - **Purpose:** Show the relationship or joint distribution of two categorical variables.
        - **Tools:** `pd.crosstab(df.cat1, df.cat2).plot(kind='bar', stacked=True)`
        - **Insights:** Proportions or counts of one categorical variable within each category of another.
- Multivariate Analysis 
	### (Analyzing More Than Two Variables)
    - **Pair Plots<br>(Scatter Plot Matrix)**
        - **Purpose:** Create a grid of scatter plots for all pairs of numerical variables in a DataFrame. Histograms or density plots are often shown on the diagonal.
        - **Tools:** `sns.pairplot(df, hue='cat_col')` (can use `hue` to add a categorical dimension)
        - **Insights:** Provides a quick overview of pairwise relationships across many variables.
    - **Scatter Plots<br>with Hue/Size/Style Encoding**
        - **Purpose:** Add more dimensions to a scatter plot by encoding additional variables using color (`hue`), marker size (`size`), or marker style (`style`).
        - **Tools:** `sns.scatterplot(x='col1', y='col2', hue='cat_col', size='num_col3', style='cat_col2', data=df)`
    - **3D Plots**
        - **Purpose:** Visualize relationships between three numerical variables. (See [[Matplotlib_3D_Plotting]])
        - **Tools:** `mpl_toolkits.mplot3d`
        - **Insights:** Can reveal complex interactions, but can also be hard to interpret. Use judiciously.
