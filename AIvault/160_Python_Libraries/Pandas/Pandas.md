---
tags:
  - pandas
  - python
  - library
  - data_analysis
  - data_manipulation
  - core
aliases:
  - Python Pandas
  - Pandas Library
related:
  - "[[Python]]"
  - "[[NumPy]]"
  - "[[Pandas_Series]]"
  - "[[Pandas_DataFrame]]"
  - "[[Data_Science_AI_MOC|Data Science]]"
  - "[[Matplotlib_MOC|Matplotlib]]"
worksheet: [WS_Pandas_Intro] # Assuming a generic name
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Pandas

## Definition

**Pandas** is an open-source [[Python]] library providing high-performance, easy-to-use data structures and data analysis tools. It is built on top of [[NumPy]] and is a cornerstone of the Python [[Data_Science_AI_MOC|data science]] ecosystem. The name "Pandas" is derived from "Panel Data" – an econometrics term for multidimensional structured datasets.

## Core Data Structures

Pandas introduces two primary data structures:

1.  **[[Pandas_Series|Series]]:** A one-dimensional labeled array capable of holding data of any type (integers, strings, floating-point numbers, Python objects, etc.). It's similar to a column in a spreadsheet or a SQL table, or a 1D [[NumPy_ndarray|NumPy array]] with an associated index.
2.  **[[Pandas_DataFrame|DataFrame]]:** A two-dimensional, size-mutable, and potentially heterogeneous tabular data structure with labeled rows and columns. It can be thought of as a dictionary of Series, a spreadsheet, an SQL table, or a 2D NumPy array with both row and column labels.

## Key Features & Capabilities

- **Efficient Data Structures:** Provides `Series` and `DataFrame` for handling structured data.
- **Data Handling:** Easy handling of missing data (represented as `NaN` in numerical arrays), data alignment, and type conversion.
- **Data I/O:** Powerful tools for reading and writing data from/to various file formats (CSV, Excel, SQL databases, JSON, HTML, HDF5, Parquet, etc.).
- **Indexing & Selection:** Flexible and powerful ways to select and subset data (label-based indexing with `.loc`, integer-position based indexing with `.iloc`, boolean indexing).
- **Data Cleaning & Preprocessing:** Tools for cleaning messy data, handling duplicates, transforming data.
- **Data Manipulation:** Grouping (`groupby`), merging, joining, concatenating, reshaping (pivoting, stacking/unstacking).
- **Time Series Functionality:** Robust tools for working with time series data (date ranges, frequency conversion, moving window statistics, date shifting, and lagging).
- **Performance:** Many operations are optimized and implemented in C or Cython for speed.
- **Integration:** Works seamlessly with other libraries in the Python scientific stack like [[NumPy]], [[Matplotlib_MOC|Matplotlib]], and Scikit-learn.

## Installation

```bash
pip install pandas
```

## Basic Usage Example

```python
import pandas as pd
import numpy as np

# --- Creating a Series ---
s = pd.Series([1, 3, 5, np.nan, 6, 8], name='MyNumbers')
print("Pandas Series s:")
print(s)
print(f"s.dtype: {s.dtype}") # float64 due to np.nan
print(f"s.index: {s.index}")

# --- Creating a DataFrame ---
# From a dictionary of lists
data = {
    'col1': [1, 2, 3, 4],
    'col2': ['A', 'B', 'C', 'D'],
    'col3': np.random.rand(4)
}
df = pd.DataFrame(data, index=['row1', 'row2', 'row3', 'row4'])
print("\nPandas DataFrame df:")
print(df)

# --- Basic Inspection ---
print(f"\ndf.head(2):\n{df.head(2)}")
print(f"\ndf.dtypes:\n{df.dtypes}")
print(f"\ndf.describe():\n{df.describe()}") # Stats for numerical columns

# --- Selection ---
print(f"\nSelecting column 'col2':\n{df['col2']}")
print(f"\nSelecting row by label 'row2' (using .loc):\n{df.loc['row2']}")
print(f"\nSelecting row by integer position 1 (using .iloc):\n{df.iloc[1]}")
print(f"\nBoolean indexing (col3 > 0.5):\n{df[df['col3'] > 0.5]}")

# --- Basic Operation ---
df['col4'] = df['col1'] * 2 # Add a new column
print(f"\nDataFrame with new column 'col4':\n{df}")
```

## Related Concepts
- [[Python]], [[NumPy]] (Pandas builds on NumPy)
- [[Pandas_Series]], [[Pandas_DataFrame]] (Core data structures)
- [[Data_Analysis]], [[Data_Manipulation]], Data Cleaning
- [[Data_Science_AI_MOC|Data Science]] ecosystem

---
**Source:** Pandas Documentation