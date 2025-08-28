---
tags:
  - python
  - tsfresh
  - time_series
  - data_format
  - pandas
  - dataframe
  - concept
aliases:
  - tsfresh Data Format
  - tsfresh DataFrame Structure
related:
  - "[[160_Python_Libraries/tsfresh/_tsfresh_MOC|_tsfresh_MOC]]"
  - "[[_Pandas_MOC]]"
worksheet:
  - WS_TimeSeries_1
date_created: 2025-08-27
---
# tsfresh: Data Format Requirements

`tsfresh` is designed to work with time series data stored in a `pandas.DataFrame`. To extract features, the data must be provided in a specific "flat" or "stacked" format.

## The Flat DataFrame Format
This is the primary input format for `tsfresh`. It's a "long" or "tidy" data format where each row represents a single observation at a specific point in time for a specific time series instance.

The DataFrame must contain at least three columns:
1.  **Column for ID (`column_id`):** This column identifies which time series a particular observation belongs to. All rows with the same `id` are part of the same time series sample.
2.  **Column for Time (`column_sort`):** This column specifies the time step or sequence order for each observation. `tsfresh` will sort the data based on this column before extracting features. It can be a numerical index, a datetime, or any other sortable type.
3.  **Value Columns (`column_value`):** One or more columns containing the actual time series measurements.

**Example Structure:**
Imagine we have sensor data from two different machines.

```python
import pandas as pd

# Create a sample flat DataFrame
data = {
    'machine_id': ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B'],
    'timestamp':,
    'temperature': [25.1, 25.3, 25.2, 25.5, 30.2, 30.1, 30.4, 30.3],
    'pressure': [101.2, 101.3, 101.2, 101.4, 98.5, 98.6, 98.5, 98.4]
}
flat_df = pd.DataFrame(data)

print("--- tsfresh Flat DataFrame Format ---")
print(flat_df)
```
**Output:**```
--- tsfresh Flat DataFrame Format ---
  machine_id  timestamp  temperature  pressure
0          A          1         25.1     101.2
1          A          2         25.3     101.3
2          A          3         25.2     101.2
3          A          4         25.5     101.4
4          B          1         30.2      98.5
5          B          2         30.1      98.6
6          B          3         30.4      98.5
7          B          4         30.3      98.4
```
In this example:
-   `column_id` would be `"machine_id"`.
-   `column_sort` would be `"timestamp"`.
-   The value columns are `"temperature"` and `"pressure"`. `tsfresh` can extract features for each of these value columns.

## Target Vector (`y`)
For feature selection and supervised learning tasks (classification/regression), you also need a target vector. This is typically a `pandas.Series` where the **index must correspond to the unique IDs** from the `column_id` in your flat DataFrame.

**Example Target Series:**
Let's say we want to classify if a machine is likely to fail.

```python
# Target Series for our two machines
# The index MUST match the unique values in the 'machine_id' column
y_target = pd.Series(, index=['A', 'B']) # Machine A is normal (0), Machine B is faulty (1)

print("\n--- Target Series (y) Format ---")
print(y_target)
```
**Output:**
```
--- Target Series (y) Format ---
A    0
B    1
dtype: int64
```

## Why this Format?
This "flat" format is very flexible and allows `tsfresh` to:
-   Handle datasets with thousands or millions of individual time series instances.
-   Process time series of varying lengths, as each is identified by its `id`.
-   Work with multivariate time series by simply adding more value columns.
-   Easily map extracted features back to their corresponding `id` and, subsequently, to the target variable for model training.

Correctly formatting your data is the essential first step before using `tsfresh` for feature extraction or selection.

---