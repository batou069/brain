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

Pandas [[Pandas_DataFrame|DataFrames]] and [[Pandas_Series|Series]] have a built-in `.plot()` accessor for creating various plots, acting as a wrapper around [[Matplotlib_MOC|Matplotlib]]. `.hist()` is a convenience method for histograms.

## `DataFrame.plot()` / `Series.plot()`

**Syntax (Simplified):**
`df_or_series.plot(kind='line', x=None, y=None, ax=None, figsize=None, title=None, grid=True, **kwargs)`

- **`kind`**: Type of plot (e.g., `'line'`, `'bar'`, `'barh'`, `'hist'`, `'box'`, `'kde'`, `'area'`, `'pie'`, `'scatter'`, `'hexbin'`).
- **`x`, `y`**: Columns for x and y axes (for DataFrame plots like scatter).
- **`ax`**: Matplotlib Axes object to plot on.
- **`**kwargs`**: Passed to Matplotlib's plotting function.

## `DataFrame.hist()` / `Series.hist()`

**Syntax (Simplified):**
`df_or_series.hist(bins=10, ax=None, grid=True, figsize=None, **kwargs)`

- **`bins`**: Number of histogram bins.

## AnyBlock Examples: Pandas Plotting

[list2tab]
- Setup DataFrame
  ```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt # For plt.show() and customization

  ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
  ts_cumulative = ts.cumsum()
  df_cumulative = pd.DataFrame(np.random.randn(100, 4), index=ts.index[:100], columns=list('ABCD')).cumsum()
  ```

- Line Plot (`.plot()`)
  ```python
  ts_cumulative.plot(figsize=(8, 4), title='Cumulative Random Walk (Series)')
  plt.ylabel("Value")
  plt.grid(True)
  # plt.show() # Uncomment to display

  df_cumulative.plot(figsize=(10, 6), title='Cumulative Random Walks (DataFrame)')
  plt.xlabel("Date")
  plt.ylabel("Cumulative Value")
  # plt.show() # Uncomment to display
  ```
  > *Generates line plots. `df_cumulative.plot()` plots each column as a separate line.*

- Bar Plot (`.plot(kind='bar')`)
  ```python
  df_bar = pd.DataFrame(np.random.rand(5, 3) * 10, columns=['X', 'Y', 'Z'], index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri'])
  df_bar.plot(kind='bar', figsize=(8, 5), title='Sample Bar Plot')
  plt.ylabel("Magnitude")
  plt.xticks(rotation=0)
  # plt.show()

  df_bar.plot(kind='bar', stacked=True, figsize=(8, 5), title='Stacked Bar Plot')
  # plt.show()
  ```

- Histogram (`.hist()` or `.plot(kind='hist')`)
  ```python
  s_hist_data = pd.Series(np.random.normal(loc=0, scale=1, size=1000))
  s_hist_data.hist(bins=30, figsize=(8, 5), grid=False)
  plt.title("Histogram of a Series")
  # plt.show()

  # df_for_hist = pd.DataFrame({'Data1': np.random.randn(200), 'Data2': np.random.gamma(2, size=200)})
  # df_for_hist.hist(bins=25, figsize=(10, 4)) # Creates separate subplots
  # plt.tight_layout()
  # plt.show()
  ```

- Scatter Plot (`.plot(kind='scatter')`)
  ```python
  df_scatter = pd.DataFrame(np.random.rand(50, 2), columns=['MetricA', 'MetricB'])
  df_scatter['MetricC_Color'] = np.random.rand(50)
  df_scatter.plot(kind='scatter', x='MetricA', y='MetricB', c='MetricC_Color', colormap='viridis', figsize=(8,5))
  # plt.show()
  ```

## Key Considerations

- **Matplotlib Backend:** Relies on Matplotlib. Import `matplotlib.pyplot as plt` for `show()` and further customization.
- **Convenience:** Quick way to visualize data from Pandas objects. For complex plots, direct Matplotlib usage offers more control.

## Related Concepts
- [[Pandas_DataFrame]], [[Pandas_Series]]
- [[Matplotlib_MOC|Matplotlib]], [[Pyplot_API]]
- [[Data_Visualization]]

---
**Source:** WS_Pandas_Main, Pandas Documentation