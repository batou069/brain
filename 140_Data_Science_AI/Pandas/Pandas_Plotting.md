---
tags:
  - pandas
  - python
  - data_visualization
  - plotting
  - function
  - concept
aliases:
  - df.plot()
  - Series.plot()
  - Pandas Plotting
  - df.hist()
related:
  - "[[Pandas_DataFrame]]"
  - "[[Pandas_Series]]"
  - "[[Matplotlib_MOC|Matplotlib]]"
  - "[[Pyplot_API]]"
  - "[[Data_Visualization]]"
worksheet: [WS_Pandas_Main]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Pandas Plotting (`.plot()`, `.hist()`)

## Definition

Pandas [[Pandas_DataFrame|DataFrames]] and [[Pandas_Series|Series]] have a built-in `.plot()` accessor that provides a convenient way to create various types of plots directly from the data. These plotting methods are essentially wrappers around [[Matplotlib_MOC|Matplotlib]]'s [[Pyplot_API|`pyplot` API]], making common visualizations quick and easy.

## `DataFrame.plot()` / `Series.plot()`

**General Syntax:**
```python
df_or_series.plot(
    x=None, y=None, kind='line', ax=None, subplots=False, sharex=False, sharey=False,
    layout=None, figsize=None, use_index=True, title=None, grid=None,
    legend=True, style=None, logx=False, logy=False, loglog=False,
    xticks=None, yticks=None, xlim=None, ylim=None, rot=None,
    fontsize=None, colormap=None, table=False, yerr=None, xerr=None,
    stacked=False, sort_columns=False, secondary_y=False, mark_right=True,
    **kwargs
)
```

- **`kind`**: The type of plot to produce. Common values:
    - `'line'` (default): Line plot.
    - `'bar'`: Vertical bar plot.
    - `'barh'`: Horizontal bar plot.
    - `'hist'`: Histogram.
    - `'box'`: Box plot.
    - `'kde'` or `'density'`: Kernel Density Estimate plot.
    - `'area'`: Area plot.
    - `'pie'`: Pie plot.
    - `'scatter'`: Scatter plot (requires `x` and `y` columns for DataFrame).
    - `'hexbin'`: Hexagonal bin plot.
- **`x`, `y`**: For DataFrames, labels or positions of columns to plot. For `kind='scatter'` or `kind='hexbin'`, `x` and `y` are required.
- **`ax`**: A Matplotlib `Axes` object to plot on. If `None`, uses the current `pyplot` axes.
- **`subplots`**: (Default `False`) If `True`, plot each column in a separate subplot.
- **`figsize`**: Tuple `(width, height)` in inches.
- **`title`**: Title for the plot.
- **`grid`**: (Default `None`, often `True` is nice) Whether to show grid lines.
- **`legend`**: (Default `True`) Whether to show the legend.
- **`**kwargs`**: Additional keyword arguments passed directly to the underlying Matplotlib plotting function (e.g., `color`, `linestyle`, `marker`).

## `DataFrame.hist()` / `Series.hist()`

**Syntax (Simplified):**
```python
df_or_series.hist(column=None, by=None, grid=True, xlabelsize=None, xrot=None, ylabelsize=None, yrot=None, ax=None, sharex=False, sharey=False, figsize=None, layout=None, bins=10, **kwargs)
```
- This is a convenience wrapper around `df.plot(kind='hist')` or `plt.hist()`.
- **`bins`**: Number of histogram bins to be used.
- **`by`**: Column to group by and create separate histograms for each group.
- If called on a DataFrame, it creates a histogram for each numerical column.

## AnyBlock Examples: Pandas Plotting

[list2tab]
- Setup DataFrame
  ```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt # Usually needed for plt.show() and further customization

  # Sample data
  ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
  ts_cumulative = ts.cumsum()

  df = pd.DataFrame(np.random.randn(100, 4), index=ts.index[:100], columns=list('ABCD'))
  df_cumulative = df.cumsum()

  print("Setup complete. Examples will generate plots.")
  ```

- Line Plot (`.plot()`)
  ```python
  # Plot a Series
  ts_cumulative.plot(figsize=(8, 4), title='Cumulative Random Walk (Series)')
  plt.ylabel("Value")
  plt.grid(True)
  plt.show()

  # Plot all columns of a DataFrame
  df_cumulative.plot(figsize=(10, 6), title='Cumulative Random Walks (DataFrame)')
  plt.xlabel("Date")
  plt.ylabel("Cumulative Value")
  plt.show()
  ```
  > *These will generate line plots. `ts_cumulative.plot()` plots the Series. `df_cumulative.plot()` plots each column of the DataFrame as a separate line on the same Axes.*

- Bar Plot (`.plot(kind='bar')`)
  ```python
  df_bar = pd.DataFrame(np.random.rand(5, 3) * 10, columns=['X', 'Y', 'Z'], index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri'])
  
  # Vertical bar plot
  df_bar.plot(kind='bar', figsize=(8, 5), title='Sample Bar Plot')
  plt.ylabel("Magnitude")
  plt.xticks(rotation=0) # Keep x-axis labels horizontal
  plt.show()

  # Stacked bar plot
  df_bar.plot(kind='bar', stacked=True, figsize=(8, 5), title='Stacked Bar Plot')
  plt.ylabel("Magnitude")
  plt.xticks(rotation=0)
  plt.show()
  ```

- Histogram (`.hist()` or `.plot(kind='hist')`)
  ```python
  # Histogram for a Series
  s_hist_data = pd.Series(np.random.normal(loc=0, scale=1, size=1000))
  s_hist_data.hist(bins=30, figsize=(8, 5), grid=False) # Direct .hist()
  plt.title("Histogram of a Series")
  plt.xlabel("Value")
  plt.ylabel("Frequency")
  plt.show()

  # Histograms for all numerical columns in a DataFrame
  df_for_hist = pd.DataFrame({
      'Data1': np.random.randn(200),
      'Data2': np.random.gamma(2, size=200)
  })
  df_for_hist.hist(bins=25, figsize=(10, 4)) # Creates separate subplots
  plt.suptitle("Histograms for DataFrame Columns", y=1.02)
  plt.tight_layout()
  plt.show()
  ```

- Scatter Plot (`.plot(kind='scatter')`)
  ```python
  # For DataFrame, need to specify x and y columns
  df_scatter = pd.DataFrame(np.random.rand(50, 2), columns=['MetricA', 'MetricB'])
  df_scatter['MetricC_Color'] = np.random.rand(50) # For color
  df_scatter['MetricD_Size'] = np.random.rand(50) * 100 # For size

  df_scatter.plot(kind='scatter', x='MetricA', y='MetricB',
                  c='MetricC_Color', s='MetricD_Size',
                  colormap='viridis', alpha=0.7,
                  figsize=(8, 5), title='Scatter Plot from DataFrame')
  plt.show()
  ```

## Key Considerations

- **Matplotlib Backend:** Pandas plotting uses Matplotlib. You often need `import matplotlib.pyplot as plt` for `plt.show()` and for more advanced customizations (e.g., accessing Figure and Axes objects).
- **Customization:** While `.plot()` offers many parameters, for highly customized plots, you might get the Matplotlib `Axes` object (e.g., `ax = df.plot(...)`) and then use Matplotlib's OO API methods on `ax`.
- **Convenience:** Provides a quick way to visualize data directly from Pandas objects without needing to manually set up Matplotlib plots from scratch for common chart types.

## Related Concepts
- [[Pandas_DataFrame]], [[Pandas_Series]]
- [[Matplotlib_MOC|Matplotlib]], [[Pyplot_API]], [[Figure_Subplot_Axes]] (The underlying plotting library)
- [[Data_Visualization]], [[Exploratory_Data_Analysis]] (Plotting is a key part)
- Different plot types (line, bar, hist, scatter, box, kde, area, pie)

---
**Source:** WS_Pandas_Main, Pandas Documentation