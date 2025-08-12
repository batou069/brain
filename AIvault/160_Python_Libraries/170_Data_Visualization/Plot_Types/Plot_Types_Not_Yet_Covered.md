---
tags:
  - data_visualization
  - plotting
  - chart_types
  - scatter_plot_matrix
  - parallel_coordinates
  - radar_chart
  - concept
  - example
aliases:
  - Additional Plot Types
  - Advanced Charts
related:
  - "[[_Data_Visualization_MOC]]"
  - "[[Choosing_the_Right_Plot]]"
  - "[[Visualizing_Multidimensional_Data]]"
  - "[[Scatter_Plot_Matrix]]"
  - "[[Parallel_Coordinates_Plot]]"
  - "[[Radar_Chart]]"
worksheet:
  - WS_DataViz_1
date_created: 2025-06-11
---
# Additional Plot Types and Their Use Cases

Beyond the most common charts, several other plot types offer unique ways to visualize data, especially for multidimensional datasets or specific comparison needs. This note explores a few such plots.

>[!question] Come up with 3 types of plots not mentioned above [in the initial keyword list], and answer the same questions [scenario where useful, is it best?].

We will discuss:
1.  [[Scatter_Plot_Matrix|Scatter Plot Matrix (Pair Plot)]]
2.  [[Parallel_Coordinates_Plot|Parallel Coordinates Plot]]
3.  [[Radar_Chart|Radar Chart (Spider Chart)]]

---
## 1. [[Scatter_Plot_Matrix|Scatter Plot Matrix (Pair Plot)]]

-   **Definition:** A scatter plot matrix (often called a pair plot or SPLOM) is a grid (matrix) of scatter plots. For a dataset with $N$ numerical variables, it displays all $N \times N$ pairwise scatter plots. The diagonal typically shows a univariate distribution (histogram or kernel density estimate - KDE) of each variable.
-   **Scenario where useful:** Exploring all pairwise relationships in a multivariate dataset with several numerical features. For example, analyzing an e-commerce dataset with product features like `price`, `customer_rating`, `weight_kg`, and `units_sold` to quickly identify potential correlations, clusters, or outliers across different feature pairings.
-   **Usefulness:**
    -   Provides a comprehensive overview of bivariate relationships in one go.
    -   Helps identify which pairs of variables are correlated (linearly or non-linearly).
    -   Shows the distribution of each individual variable.
    -   Can be enhanced with `hue` encoding to show how relationships differ across a categorical variable.
-   **Is this plot the best way to visualize this scenario?**
    -   **Yes, for initial exploratory analysis of pairwise relationships among multiple numerical variables, it is one of the best and most standard tools.**
    -   **Limitations:** Can become cluttered and hard to interpret if the number of variables is very large (e.g., > 10-15 variables, the grid becomes too big). For very high-dimensional data, dimensionality reduction techniques might be needed first, or other multivariate visualization methods. It primarily shows bivariate relationships; higher-order interactions might be missed.
-   **Tools:**
    -   **Seaborn:** `sns.pairplot()`
    -   **Pandas:** `pandas.plotting.scatter_matrix()`
    -   **Plotly Express:** `px.scatter_matrix()`

**Example (Conceptual with `seaborn.pairplot`):**
```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Conceptual e-commerce product features
np.random.seed(42)
product_features_df = pd.DataFrame({
    'price': np.random.uniform(10, 300, 100),
    'rating': np.random.uniform(2.5, 5.0, 100).round(1),
    'weight_kg': np.random.uniform(0.1, 5.0, 100).round(2),
    'units_sold_monthly': np.random.randint(10, 200, 100),
    'category': np.random.choice(['Electronics', 'Apparel'], 100)
})

# Create a pair plot, colored by category
# pair_plot_fig = sns.pairplot(
#     product_features_df,
#     vars=['price', 'rating', 'weight_kg', 'units_sold_monthly'], # Specify numerical vars to plot
#     hue='category', # Color points by category
#     diag_kind='kde', # Kernel density estimate on diagonal
#     plot_kws={'alpha': 0.6, 's': 40, 'edgecolor': 'k'}, # Keyword args for scatter plots
#     corner=False # Show full matrix; True for lower triangle
# )
# pair_plot_fig.fig.suptitle("Pairwise Relationships of Product Features", y=1.02)
# plt.show()
```

---
## 2. [[Parallel_Coordinates_Plot|Parallel Coordinates Plot]]

-   **Definition:** A visualization technique used for plotting multivariate numerical data. Each variable is given its own parallel vertical axis. An observation (a single data point with multiple feature values) is represented as a polyline that connects its values on each of these parallel axes.
-   **Scenario where useful:** Identifying clusters, patterns, or anomalies in high-dimensional data by observing how lines group or diverge. For example, analyzing customer segmentation data where each customer has multiple numerical attributes (e.g., `age`, `income`, `spending_score`, `items_purchased`). Lines representing customers in the same segment might show similar patterns across the axes.
-   **Usefulness:**
    -   Can display many variables (dimensions) simultaneously.
    -   Helps in spotting correlations and inverse correlations between adjacent axes based on line crossings or parallelisms.
    -   Can reveal clusters or groups of observations that follow similar profiles.
    -   Interactive versions can allow highlighting lines or reordering axes for better exploration.
-   **Is this plot the best way to visualize this scenario?**
    -   **It's a good specialized tool for exploring high-dimensional profiles and identifying clusters or outliers based on overall patterns across variables.**
    -   **Limitations:**
        -   Can become very cluttered and unreadable if there are too many observations (lines). Often requires transparency (`alpha`) or plotting a subset.
        -   The order of axes significantly impacts the visual patterns observed. Experimenting with different orderings is often necessary.
        -   Does not directly show pairwise scatter-plot like correlations for non-adjacent axes.
        -   Less intuitive for very large numbers of dimensions without interaction.
-   **Tools:**
    -   **Pandas:** `pandas.plotting.parallel_coordinates()`
    -   **Plotly Express:** `px.parallel_coordinates()`
    -   **Matplotlib** (more manual setup).

**Example (Conceptual with `plotly.express.parallel_coordinates`):**
```python
import plotly.express as px
import pandas as pd
import numpy as np

# Conceptual customer segment data for an e-commerce site
# np.random.seed(10)
# customer_segments_df = pd.DataFrame({
#     'segment_id': np.repeat([0, 1, 2], 50), # Three segments
#     'avg_order_value': np.concatenate([np.random.normal(50,10,50), np.random.normal(150,30,50), np.random.normal(80,20,50)]).clip(10),
#     'purchase_frequency_monthly': np.concatenate([np.random.normal(2,0.5,50), np.random.normal(5,1,50), np.random.normal(10,2,50)]).clip(1),
#     'avg_rating_given': np.concatenate([np.random.normal(4.5,0.2,50), np.random.normal(3.5,0.5,50), np.random.normal(4.0,0.3,50)]).clip(1,5),
#     'time_on_site_min': np.concatenate([np.random.normal(10,3,50), np.random.normal(20,5,50), np.random.normal(15,4,50)]).clip(1)
# })
# customer_segments_df['segment_id'] = customer_segments_df['segment_id'].astype(str) # For discrete color mapping

# fig_parallel = px.parallel_coordinates(
#     customer_segments_df,
#     color="segment_id", # Color lines by segment
#     dimensions=['avg_order_value', 'purchase_frequency_monthly', 'avg_rating_given', 'time_on_site_min'],
#     color_continuous_scale=px.colors.diverging.Tealrose, # If color var was continuous
#     labels={
#         "avg_order_value": "Avg Order Value ($)",
#         "purchase_frequency_monthly": "Monthly Purchases",
#         "avg_rating_given": "Avg Rating Given",
#         "time_on_site_min": "Time on Site (min)"
#     },
#     title="Customer Segment Profiles (Parallel Coordinates)"
# )
# fig_parallel.show()
```

---
## 3. [[Radar_Chart|Radar Chart (Spider Chart or Star Plot)]]

-   **Definition:** A graphical method of displaying multivariate data in the form of a two-dimensional chart of three or more quantitative variables represented on axes starting from the same point. The axes are usually arranged radially, and data points are connected to form a polygon.
-   **Scenario where useful:** Comparing multiple quantitative attributes for a single item or a small number of items. For example, comparing key performance indicators (KPIs) for different e-commerce marketing campaigns (e.g., `reach`, `engagement_rate`, `conversion_rate`, `cost_per_acquisition`). Or, comparing feature sets of a few competing products.
-   **Usefulness:**
    -   Provides a quick visual comparison of the "profile" or "shape" of different items across multiple variables.
    -   Can highlight which items are strong or weak on particular attributes.
    -   Good for showing balance or imbalance across variables.
-   **Is this plot the best way to visualize this scenario?**
    -   **It can be effective for comparing a small number of entities (e.g., 2-5) across a moderate number of common variables (e.g., 5-10).**
    -   **Limitations:**
        -   Becomes cluttered and hard to interpret with too many variables (axes) or too many items (polygons).
        -   The area of the polygon can be misleading, as it depends on the order of axes and the scales. Comparisons should focus on the values along the axes.
        -   All variables are typically normalized to a common scale (e.g., 0-100 or z-scores) for fair comparison, which can obscure absolute magnitudes.
        -   Comparing exact values can be harder than on a bar chart.
        -   [[Bar_Chart|Bar charts]] or grouped bar charts might be better for precise comparisons of individual variables if the "overall profile shape" is not the primary goal.
-   **Tools:**
    -   **Matplotlib** (requires more manual setup for polar projection and connecting points).
    -   **Plotly Express:** `px.line_polar()` can be adapted.
    -   **Plotly Graph Objects:** `go.Scatterpolar()` is the direct way.
    -   Some specialized libraries or manual implementations.

**Example (Conceptual with `plotly.graph_objects.Scatterpolar`):**
```python
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Conceptual performance metrics for two e-commerce ad campaigns
campaign_data = pd.DataFrame({
    'metric': ['Reach (K)', 'Click-Through Rate (%)', 'Conversion Rate (%)', 'Engagement Score (1-10)', 'Cost Efficiency (1-10)'],
    'Campaign_A': [80, 2.5, 5, 7, 6],
    'Campaign_B': [65, 3.1, 4, 8, 7.5]
})

# fig_radar = go.Figure()

# fig_radar.add_trace(go.Scatterpolar(
#       r=campaign_data['Campaign_A'],
#       theta=campaign_data['metric'],
#       fill='toself', # Fill area
#       name='Campaign A',
#       line_color='blue'
# ))
# fig_radar.add_trace(go.Scatterpolar(
#       r=campaign_data['Campaign_B'],
#       theta=campaign_data['metric'],
#       fill='toself',
#       name='Campaign B',
#       line_color='red'
# ))

# fig_radar.update_layout(
#   polar=dict(
#     radialaxis=dict(
#       visible=True,
#       range= # Normalize or set appropriate range, e.g., [0, max_val_across_all_metrics_if_not_normalized]
#     )
#   ),
#   showlegend=True,
#   title="Ad Campaign Performance Comparison (Radar Chart)"
# )
# fig_radar.show()
```
*(Note: For a proper radar chart, data values often need to be normalized to a common scale if their original scales differ significantly.)*

These additional plot types expand the toolkit for visualizing complex data, each with its own strengths and ideal use cases.

---