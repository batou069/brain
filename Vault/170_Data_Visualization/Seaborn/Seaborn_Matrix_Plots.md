---
tags:
  - seaborn
  - python
  - plotting
  - data_visualization
  - matrix_plots
  - heatmap
  - clustermap
  - concept
  - example
  - chart
  - correlation
aliases:
  - Seaborn Heatmap
  - Seaborn Clustermap
  - sns.heatmap
  - sns.clustermap
related:
  - "[[170_Data_Visualization/Seaborn/_Seaborn_MOC|_Seaborn_MOC]]"
  - "[[Heatmap]]"
  - "[[Hierarchical_Clustering]]"
  - "[[_Pandas_MOC]]"
  - "[[Correlation_Matrix_Visualization]]"
  - "[[_Pandas_MOC|Pandas DataFrame]]"
worksheet:
  - WS_DataViz_1
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
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

# Seaborn: Matrix Plots (`heatmap`, `clustermap`)

Seaborn provides functions for visualizing matrix data, where the values in a 2D array or DataFrame are represented as colors. These are useful for showing patterns in matrices, such as correlations, co-occurrences, or the structure of datasets.

## `sns.heatmap()`
-   **Purpose:** To plot rectangular data as a color-encoded matrix. This is an excellent way to visualize matrices of values, especially correlation matrices or confusion matrices.
-   **Key Parameters:**
    -   `data`: 2D array or Pandas DataFrame. The data to plot.
    -   `vmin`, `vmax`: Values to anchor the colormap, otherwise inferred from the data.
    -   `cmap`: Colormap to use (e.g., 'viridis', 'coolwarm', 'YlGnBu').
    -   `annot`: If `True`, write the data value in each cell. If an array-like with the same shape as `data`, then use this to annotate the heatmap instead of the data.
    -   `fmt`: String formatting code to use when `annot=True` (e.g., '.2f' for 2 decimal places).
    -   `linewidths`, `linecolor`: Width and color of lines that will divide each cell.
    -   `cbar`: Whether to draw a colorbar (default `True`).
    -   `cbar_kws`: Dictionary of keyword arguments for `fig.colorbar`.
    -   `square`: If `True`, set the Axes aspect to "equal" so cells will be square.
    -   `xticklabels`, `yticklabels`: How to plot ticks and labels. If `True`, plot the column/index names. If `False`, don't plot. If a list, plot these alternate labels. If an int, plot labels every N ticks.
    -   `ax`: Matplotlib Axes object.
-   **Use Cases:** Visualizing correlation matrices, confusion matrices, gene expression data, feature co-occurrence.

**Example (Correlation heatmap for product features):**
```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Conceptual product feature data
# np.random.seed(0)
# data_features = pd.DataFrame(np.random.rand(50, 5), columns=['price', 'rating', 'reviews_count', 'shipping_days', 'weight_kg'])
# # Introduce some correlations
# data_features['price'] = data_features['price'] + data_features['weight_kg'] * 50
# data_features['rating'] = data_features['rating'] - data_features['price'] / 200 + data_features['reviews_count'] / 500
# data_features = data_features.clip(lower=0) # Ensure non-negative where applicable

# Calculate the correlation matrix
# correlation_matrix = data_features.corr()

# plt.figure(figsize=(8, 6))
# sns.heatmap(
#     correlation_matrix,
#     annot=True,          # Show values in cells
#     fmt=".2f",           # Format annotations to 2 decimal places
#     cmap="coolwarm",     # Colormap (diverging for correlations)
#     linewidths=.5,
#     linecolor='gray',
#     cbar_kws={"label": "Correlation Coefficient"}
# )
# plt.title("Correlation Heatmap of Product Features")
# plt.xticks(rotation=45, ha='right')
# plt.yticks(rotation=0)
# plt.tight_layout()
# plt.show()
```

## `sns.clustermap()`
-   **Purpose:** To plot a hierarchically-clustered heatmap. It rearranges the rows and columns of the input matrix based on hierarchical clustering similarity, and displays corresponding dendrograms alongside the heatmap.
-   **Key Parameters:**
    -   `data`: 2D array or Pandas DataFrame.
    -   `pivot_kws`: If `data` is a tidy DataFrame, can pivot it before clustering.
    -   `method`: Linkage method for hierarchical clustering (e.g., 'average', 'ward', 'complete'). See [[Hierarchical_Clustering]].
    -   `metric`: Distance metric for clustering (e.g., 'euclidean', 'correlation').
    -   `standard_scale`: Whether to standardize the data (0 mean, 1 variance) along rows (`0` or `'row'`) or columns (`1` or `'col'`).
    -   `row_cluster`, `col_cluster`: If `True` (default), cluster rows/columns.
    -   `row_colors`, `col_colors`: List or DataFrame of colors to label rows/columns, often used to show group membership.
    -   `cmap`, `annot`, `fmt`, `linewidths`: Similar to `heatmap`.
    -   `figsize`: Size of the figure.
-   **Use Cases:** Exploring patterns in high-dimensional data like gene expression, identifying clusters of similar features and/or samples.

**Example (Clustermap of customer purchase patterns):**
```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Conceptual customer purchase data: customers vs. product categories (binary: bought or not)
# np.random.seed(123)
# customers = [f"Cust_{i}" for i in range(20)]
# product_cats = ['Electronics', 'Books', 'Apparel', 'Home', 'Sports', 'Toys']
# purchase_data = np.random.choice([0, 1], size=(len(customers), len(product_cats)), p=[0.7, 0.3])
# purchase_df = pd.DataFrame(purchase_data, index=customers, columns=product_cats)

# Create a clustermap
# g = sns.clustermap(
#     purchase_df,
#     method="average",      # Linkage method for clustering
#     metric="jaccard",      # Distance metric for binary data
#     cmap="viridis",        # Colormap for the heatmap
#     figsize=(8, 10),
#     linewidths=.5,
#     annot=False # Annotations can be cluttered for binary data
# )
# g.fig.suptitle("Hierarchically Clustered Heatmap of Customer Purchase Patterns", y=1.02)
# plt.setp(g.ax_heatmap.get_xticklabels(), rotation=45, ha='right') # Rotate x-axis labels
# plt.show()
```

Matrix plots are invaluable for understanding the structure and relationships within 2D datasets. `heatmap` provides a direct visualization of the matrix values, while `clustermap` adds another layer of insight by reordering rows and columns based on similarity, revealing underlying groupings.

---