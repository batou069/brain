---
tags:
  - MOC
  - pandas
  - python
  - data_analysis
  - data_manipulation
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Pandas MOC (Map of Content)

This note serves as a central hub for all topics related to **Pandas**, a powerful Python library for data manipulation and analysis.

## Core Data Structures
- "[[Pandas]]" (Overview)
- "[[Pandas_Series]]" (1D labeled array)
- "[[Pandas_DataFrame]]" (2D labeled table)
- "[[Pandas_Index_Object]]" (Labels for rows/columns)
- "[[Pandas_MultiIndex]]"

## Key Concepts & Properties
- "[[Pandas_Series_vs_NumPy_Array]]"
- "[[Pandas_DataFrame_Mutability]]"

## Data Loading & Saving (I/O)
- "[[Pandas_Data_Loading_IO]]" (General Overview)
- "[[Pandas_IO_Functions]]" (Details on CSV, Excel, SQL I/O: `read_csv`, `to_csv`, `read_excel`, `to_excel`, `read_sql`, `to_sql`)
- Reading from CSV (`pd.read_csv()`)
- Reading from Excel (`pd.read_excel()`)
- Reading from SQL Databases (`pd.read_sql()`)
- Reading from JSON (`pd.read_json()`)
- Writing to CSV (`df.to_csv()`)
- Writing to Excel (`df.to_excel()`)
- Writing to SQL (`df.to_sql()`)
- Other formats (HTML, HDF5, Parquet, Pickle) 

## Data Inspection & Exploration
- "[[Pandas_Data_Inspection]]" (Covers `head`, `tail`, `sample`, `info`, `describe`, `shape`, `index`, `columns`, `dtypes`, `value_counts`, `nunique`, `unique`)
- "[[Pandas_Aggregation_Functions]]" (Covers `sum`, `min`, `max`, `mean`, `median`, `std`, `var`, `count` (as aggregation), `idxmin`, `idxmax`, `quantile`, `agg`)
- `df.head()`, `df.tail()`
- `df.info()`
- `df.describe()`
- `df.shape`, `df.ndim`, `df.size`
- `df.dtypes`
- `df.columns`, `df.index`
- `df.value_counts()`
- `df.nunique()`

## Indexing & Selection
- "[[Pandas_Indexing_Selection]]" (General overview, `[]` operator)
- "[[Pandas_loc_vs_iloc]]" (Detailed comparison)
- "[[Pandas_at_iat]]" (Fast scalar access)
- "[[NumPy_Boolean_Indexing]]" (As applied in Pandas)
- "[[Pandas_df_query]]"
- Selecting Columns (`df['col_name']`, `df[['col1', 'col2']]`)
- Selecting Rows by Label (`df.loc[]`)
- Selecting Rows/Columns by Integer Position (`df.iloc[]`)
- Boolean Indexing (`df[boolean_condition]`)
- Conditional Selection (`df.query()`)
- Setting Values

## Data Cleaning & Transformation
- "[[Pandas_Handling_Missing_Data]]" (Covers `isnull`, `notnull`, `dropna`, `fillna`)
- "[[Pandas_Dealing_with_Duplicates]]" (Covers `duplicated`, `drop_duplicates`)
- "[[Pandas_Data_Type_Conversion]]" (Covers `astype`, `pd.to_numeric`, `pd.to_datetime`)
- "[[Pandas_String_Operations]]" (`.str` accessor)
- "[[Pandas_Apply_Map_Applymap]]" (Covers `df.apply`, `Series.map`, `df.applymap`/`df.map`)
- "[[Pandas_transform]]" (GroupBy transform)
- "[[Pandas_df_replace]]"
- "[[Pandas_df_rename]]"

## Data Manipulation & Reshaping
- Adding/Removing Columns/Rows
- Sorting (`sort_values()`, `sort_index()`)
- Grouping (`groupby()`)
    - Aggregation (`sum()`, `mean()`, `count()`, `agg()`)
    - Transformation (`transform()`)
    - Filtering (`filter()`)
- Merging, Joining, Concatenating DataFrames (`pd.merge()`, `df.join()`, `pd.concat()`)
- Pivoting (`pivot_table()`, `pivot()`)
- Stacking & Unstacking (`stack()`, `unstack()`)
- Handling Time Series Data (DatetimeIndex, resampling)

## Combining & Reshaping Data
- "[[Pandas_df_drop]]"
- "[[Pandas_Join_vs_Merge]]" (Covers `df.join`, `pd.merge`)
- "[[Pandas_concat]]"
- "[[Pandas_groupby]]"
- "[[Pandas_pivot_table]]"
- "[[Pandas_stack_unstack]]" (*Placeholder*)

## Iteration
- "[[Pandas_df_iterrows]]"
- "[[Pandas_df_itertuples]]" (*Placeholder, mentioned as alternative*)
- "[[Pandas_Iteration_Efficiency]]" (*Placeholder, discussed within iterrows*)

## Visualization (Integration)
- "[[140_Data_Science_AI/Pandas/Pandas_Plotting]]" (Covers `df.plot`, `df.hist`)
- Basic Plotting (`df.plot()`)
- Integration with "[[Matplotlib_MOC|Matplotlib]]" and "[[Seaborn_MOC|Seaborn]]"

## Notes in this Section

```dataview
LIST
FROM "140_Data_Science_AI/Pandas"
WHERE file.folder = this.file.folder AND file.name != this.file.name AND !contains(file.name, "MOC")
SORT file.name ASC
```

---
Use this MOC to navigate the Pandas section.
----