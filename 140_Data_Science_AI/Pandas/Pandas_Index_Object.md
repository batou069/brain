---
tags:
  - pandas
  - python
  - data_structure
  - core
  - indexing
  - label
aliases:
  - Pandas Index
  - pd.Index
related:
  - "[[Pandas_Series]]"
  - "[[Pandas_DataFrame]]"
  - "[[Label_Based_Indexing]]" # Placeholder (for .loc)
  - "[[Immutable_Object]]" # Placeholder
worksheet: [WS_Pandas_Intro] # Assuming
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Pandas `Index` Object

## Definition

A Pandas **`Index` object** is a fundamental data structure in [[Pandas]] that holds the **axis labels** (row labels or column labels) for [[Pandas_Series|Series]] and [[Pandas_DataFrame|DataFrames]]. It provides the mechanism for label-based indexing and alignment of data. `Index` objects are **immutable**.

## Key Characteristics

- **Immutable:** Once created, an `Index` object cannot be changed. This ensures consistency and allows for safe sharing across multiple Series/DataFrames. Operations that appear to modify an index (like `set_index`) typically return a new DataFrame with a new Index.
- **Holds Axis Labels:** Stores the labels for rows (accessed via `df.index`) or columns (accessed via `df.columns`).
- **Homogeneous (Typically):** While an `Index` can technically hold mixed types (resulting in an `object` dtype Index), they are most efficient and commonly used with homogeneous labels (e.g., all integers, all strings, all datetimes).
- **Uniqueness (Optional but Recommended):** Index labels do *not* have to be unique, but many operations (like reindexing with `.reindex()` or lookups with `.loc[]` for a single label) behave differently or more efficiently if the index is unique. Duplicate labels can lead to ambiguity.
- **Ordered (Often):** An `Index` maintains the order of its labels.
- **Set-like Operations:** `Index` objects support set-like operations such as union (`|`), intersection (`&`), difference (`difference()`), and symmetric difference (`^`).
- **Data Alignment:** Plays a crucial role in aligning data when performing operations between Series or DataFrames. Operations are performed on elements with matching index labels.

## Common Types of Index Objects

Pandas has several specialized `Index` types:

- **`Index`:** The most general Index object, capable of holding labels of any type.
- **`Int64Index`:** Optimized for integer labels.
- **`RangeIndex`:** A memory-efficient Index for representing a monotonic sequence of integers (like Python's `range`). Default for Series/DataFrames if no index is specified.
- **`Float64Index`:** Optimized for floating-point labels.
- **`MultiIndex`:** Hierarchical index object for representing multiple levels of indexing on an axis (e.g., for grouped data or higher-dimensional data representation in 2D).
- **`DatetimeIndex`:** Specialized for time series data, holding `datetime` objects. Provides powerful time-based indexing and resampling capabilities.
- **`TimedeltaIndex`:** For time differences.
- **`PeriodIndex`:** For time periods (e.g., monthly, quarterly).
- **`CategoricalIndex`:** For categorical data.

## Example

```python
import pandas as pd

# Index for a Series
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print("Series index:", s.index)
# Output: Index(['a', 'b', 'c'], dtype='object')

# Index for a DataFrame (row index and column index)
df_data = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(df_data, index=['rowA', 'rowB'])

print("\nDataFrame row index:", df.index)
# Output: Index(['rowA', 'rowB'], dtype='object')

print("DataFrame column index (which is also an Index object):", df.columns)
# Output: Index(['col1', 'col2'], dtype='object')

# Default RangeIndex
s_default = pd.Series(['x', 'y', 'z'])
print("\nDefault Series index:", s_default.index)
# Output: RangeIndex(start=0, stop=3, step=1)

# Index is immutable
# df.index[0] = 'newRow' # This will raise a TypeError

# Set-like operations
idx1 = pd.Index(['a', 'b', 'c', 'd'])
idx2 = pd.Index(['c', 'd', 'e', 'f'])

print("\nUnion of idx1 and idx2:", idx1.union(idx2))
# Output: Index(['a', 'b', 'c', 'd', 'e', 'f'], dtype='object')
print("Intersection of idx1 and idx2:", idx1.intersection(idx2))
# Output: Index(['c', 'd'], dtype='object')
```

## Related Concepts
- [[Pandas_Series]], [[Pandas_DataFrame]] (Use Index objects for their axes)
- [[Label_Based_Indexing]] (`.loc[]` relies heavily on the Index)
- [[Immutable_Object]]
- Data Alignment
- Hierarchical Indexing (`MultiIndex`)
- Time Series Analysis (`DatetimeIndex`)

---
**Source:** Pandas Documentation