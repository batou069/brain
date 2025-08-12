---
tags:
  - numpy
  - python
  - file_io
  - function
  - data_loading
  - missing_data
aliases:
  - np.genfromtxt
related:
  - "[[NumPy_ndarray]]"
  - "[[NumPy_loadtxt]]"
  - "[[NumPy_Data_Types]]"
  - "[[NumPy_NaN]]"
  - "[[Structured_Array_NumPy]]" # Placeholder
  - "[[Text_File_Processing]]"
worksheet: [WS_NumPy]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# `np.genfromtxt()`

## Definition

`numpy.genfromtxt()` is a versatile function in [[NumPy]] used to load data from a text file (or other text stream) into an `ndarray`. It is more robust and flexible than [[NumPy_loadtxt]], particularly in handling files with **missing data** or columns containing **different data types**.

## Syntax

```python
numpy.genfromtxt(
    fname,
    dtype=float,
    comments='#',
    delimiter=None,
    skip_header=0,  # Note: different from skiprows in loadtxt
    skip_footer=0,
    converters=None,
    missing_values=None,
    filling_values=None,
    usecols=None,
    names=None,       # For structured arrays
    excludelist=None,
    deletechars=" !#$%&'()*+,-./:;<=>?@[\\]^{|}~",
    replace_space='_',
    autostrip=False,
    case_sensitive=True,
    unpack=False,
    usemask=False,    # For masked arrays
    loose=True,
    invalid_raise=True,
    max_rows=None,
    encoding='bytes',
    *,
    like=None
)
```

## Key Parameters (Highlights)

-   **`fname`**: File, filename, or generator.
-   **`dtype`**: Data type of the resulting array. Can be a single type, a sequence of types (one per column), or `None` to let NumPy infer types. Default is `float`. If different types are inferred or specified, a [[Structured_Array_NumPy|structured array]] might be created.
-   **`delimiter`**: String used to separate values.
-   **`skip_header`**: Number of lines to skip at the beginning of the file.
-   **`missing_values`**: String(s) or a dictionary mapping column index to string(s) that should be recognized as missing data (e.g., `"NA"`, `"?"`).
-   **`filling_values`**: Value(s) or a dictionary to replace recognized `missing_values`. Default often converts to [[NumPy_NaN|`np.nan`]] for float columns or appropriate defaults for other types.
-   **`usecols`**: Which columns to read.
-   **`names`**: If `True`, reads column names from the first unskipped line (after `skip_header`). If a sequence of strings, these become the names of the fields in a structured array.
-   **`converters`**: Dictionary mapping column index/name to a conversion function.
-   `usemask`: If `True`, returns a masked array where missing values are masked.

## Behavior with Missing/Mixed Data

- **Handles Missing Values:** `genfromtxt` can identify strings specified in `missing_values` and replace them with values from `filling_values` (e.g., `np.nan`).
- **Handles Mixed Data Types:** If `dtype=None`, `genfromtxt` attempts to infer the type of each column individually. If different types are found, it typically returns a 1D array where each element is a tuple (a row), forming a [[Structured_Array_NumPy|structured array]]. You can also explicitly provide a list of `dtype`s per column.

## Example

[list2tab]
- data_mixed.csv
	```text
	# Example Data File: data_mixed.csv
	ID,Name,Value,IsValid
	1,Apple,10.5,True
	2,Banana,,False  # Missing Value for Value
	3,Cherry,9.8,
	4,Date,N/A,True   # N/A as missing
	```
- Python Code
	```python
	import numpy as np

	# Load with handling for missing values and mixed types
	data = np.genfromtxt(
	    "data_mixed.csv",
	    delimiter=',',
	    skip_header=1,         # Skip the header row
	    dtype=None,            # Let NumPy infer types (will create structured array)
	    names=True,            # Use header for field names
	    missing_values={2: "", 3: ""}, # Column 2 (Value) "" is missing, Column 3 (IsValid) "" is missing
	                           # Can also use a global missing_values="N/A" for example
	    filling_values={2: np.nan, 3: False}, # Fill missing Value with NaN, missing IsValid with False
	    encoding='utf-8'       # Specify encoding for text data
	)

	print("Data loaded with genfromtxt:")
	print(data)
	print(f"\nShape: {data.shape}")
	print(f"Dtype: {data.dtype}") # Will be a structured dtype

	if data.ndim > 0 and len(data) > 0 : # Check if data is not empty
	  print(f"\nFirst row: {data[0]}")
	  print(f"Accessing 'Name' of first row: {data[0]['Name']}")
	  print(f"Accessing 'Value' column: {data['Value']}")
	```
- Output
	```text
	Data loaded with genfromtxt:
	[(1, b'Apple', 10.5,  True) (2, b'Banana',  nan, False)
	 (3, b'Cherry',  9.8, False) (4, b'Date',  nan,  True)]

	Shape: (4,)
	Dtype: [('ID', '<i8'), ('Name', 'S6'), ('Value', '<f8'), ('IsValid', '?')]

	First row: (1, b'Apple', 10.5, True)
	Accessing 'Name' of first row: b'Apple'
	Accessing 'Value' column: [10.5  nan  9.8  nan]
	```
	*(Note: String columns like 'Name' are often read as byte strings (`'S6'`) unless a Unicode dtype like `'U6'` is forced or specific converters are used. The `encoding='utf-8'` helps read the file correctly.)*

## Related Concepts
- [[NumPy_ndarray]], [[NumPy_Data_Types]], [[NumPy_NaN]]
- [[NumPy_loadtxt]] (Simpler, less flexible alternative)
- [[Structured_Array_NumPy]] (Often the result when `dtype=None` and columns differ)
- [[Text_File_Processing]], CSV files
- Handling Missing Data

## Questions / Further Study
>[!question] What is the difference between `loadtxt` and `genfromtxt`? (WS_NumPy)
> - **[[NumPy_loadtxt|`np.loadtxt()`]]:** Simpler, faster for clean, purely numerical data. Strict about uniform column counts and data types; usually fails on missing data or mixed types without converters.
> - **`np.genfromtxt()`:** More robust and flexible. Designed to handle missing values gracefully (can replace them with specified fillers like `np.nan`). Can infer different data types per column and create structured arrays. Generally slower due to added flexibility.
>
> **Choose `genfromtxt` when your text file might have missing values or columns of different data types that need intelligent handling.** Choose `loadtxt` for speed with simple, purely numeric, well-formed data.

---
**Source:** Worksheet WS_NumPy, NumPy Documentation