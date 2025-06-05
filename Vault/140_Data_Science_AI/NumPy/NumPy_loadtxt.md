---
tags:
  - numpy
  - python
  - file_io
  - function
  - data_loading
aliases:
  - np.loadtxt
related:
  - "[[NumPy_ndarray]]"
  - "[[NumPy_genfromtxt]]"
  - "[[NumPy_save_load]]"
  - "[[Text_File_Processing]]" # Placeholder
worksheet: [WS_NumPy]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# `np.loadtxt()`

## Definition

`numpy.loadtxt()` is a function in [[NumPy]] used to load data from a **text file** into an `ndarray`. It is relatively simple and efficient for reading regularly structured numerical data where all rows have the same number of columns and missing values are handled simply (e.g., by skipping lines or using a default value).

## Syntax

```python
numpy.loadtxt(
    fname,
    dtype=float,
    comments='#',
    delimiter=None,
    converters=None,
    skiprows=0,
    usecols=None,
    unpack=False,
    ndmin=0,
    encoding='bytes',
    max_rows=None,
    *,
    like=None
)
```

## Key Parameters

-   **`fname`**: File, filename, or generator to read. If the filename extension is `.gz` or `.bz2`, the file is first decompressed.
-   **`dtype`**: Data type of the resulting array. Default is `float`. If columns have different types, use structured arrays or [[NumPy_genfromtxt]].
-   **`comments`**: Character or sequence of characters indicating the start of a comment. Default is `'#'`. Lines beginning with this character are ignored.
-   **`delimiter`**: The string used to separate values. By default, any whitespace is a delimiter. Can be set to a specific character (e.g., `,` for CSV, `\t` for TSV).
-   **`skiprows`**: Skip the first `skiprows` lines (e.g., to skip a header row). Default is 0.
-   **`usecols`**: Which columns to read, with 0 being the first. For example, `usecols=(1, 4, 5)` will extract the 2nd, 5th and 6th columns. Default is `None` (read all columns).
-   **`unpack`**: If `True`, the returned array is transposed, so that arguments may be unpacked using `x, y, z = loadtxt(...)`. Default is `False`.
-   **`converters`**: A dictionary mapping column number to a function that will convert that column to a float. E.g., `converters={0: custom_converter_func}`.
-   `ndmin`: Specifies the minimum number of dimensions that the output array should have.
-   `encoding`: Encoding used to decode the inputfile. Does not apply to input streams. Default is `'bytes'` (which means use system default, often UTF-8 on modern systems).
-   `max_rows`: Read `max_rows` lines of content after `skiprows` lines.

## Return Value

- An `ndarray` containing the data read from the file.

## Behavior with Missing Data

- `loadtxt` is **less flexible** with missing data compared to [[NumPy_genfromtxt]]. If it encounters a line with a different number of columns than expected (based on the first non-commented, non-skipped line), or if a value cannot be converted to the specified `dtype`, it will typically raise an error. It does not have built-in mechanisms to fill missing values with `np.nan` or other placeholders automatically like `genfromtxt` does.

## Example

[list2tab]
- data.csv
	```text
	# Example Data File: data.csv
	# ID,Value1,Value2,Category
	1,10.5,20.2,A
	2,11.3,21.5,B
	3,9.8,19.9,A
	# Commented line
	4,12.1,22.0,C
	```
- Python Code
	```python
	import numpy as np

	# Basic loading (skipping header, using first 3 numeric columns)
	try:
	    data = np.loadtxt("data.csv", delimiter=',', skiprows=1, usecols=(0, 1, 2))
	    print("Data loaded with loadtxt:")
	    print(data)
	    print(f"Shape: {data.shape}, Dtype: {data.dtype}")
	except Exception as e:
	    print(f"Error with basic loadtxt: {e}")
	    print("loadtxt is strict about data types in columns being read.")

	# Example with converters (if data needed conversion)
	# def convert_category(val_str):
	#     return float(ord(val_str.strip())) # Simplistic conversion
	# data_converted = np.loadtxt("data.csv", delimiter=',', skiprows=1,
	#                             converters={3: convert_category})
	# print("\nData with category converted (simplistic):")
	# print(data_converted)

	# Example: if file was just numbers, e.g., numbers.txt
	# 1.0 2.0 3.0
	# 4.0 5.0 6.0
	# numbers_data = np.loadtxt("numbers.txt")
	# print("\nNumbers data:\n", numbers_data)
	```
- Output
	For the first part, assuming `data.csv` exists:
	```text
	Data loaded with loadtxt:
	[[ 1.   10.5  20.2]
	 [ 2.   11.3  21.5]
	 [ 3.    9.8  19.9]
	 [ 4.   12.1  22. ]]
	Shape: (4, 3), Dtype: float64
	```
	*(Note: The last column 'Category' with 'A', 'B', 'C' would cause `loadtxt` to fail if `usecols` wasn't restricted to numeric columns or if no converter was provided for it and `dtype` was numeric.)*

## Related Concepts
- [[NumPy_ndarray]], [[NumPy_Data_Types]]
- [[NumPy_genfromtxt]] (More robust alternative for files with missing data or mixed types)
- [[NumPy_save_load]] (For saving/loading NumPy arrays in binary `.npy`/`.npz` format)
- [[Text_File_Processing]], CSV files
- File I/O

## Questions / Further Study
>[!question] What is the difference between `loadtxt` and `genfromtxt`? (WS_NumPy)
> - **`np.loadtxt()`:**
>     - Simpler and generally faster for well-structured, purely numerical data.
>     - Less flexible: It expects all rows to have the same number of columns after skipping comments/header.
>     - **Strict with missing data:** If it encounters a field that cannot be converted to the target `dtype` or a row with a mismatched number of columns, it usually raises an error.
> - **[[NumPy_genfromtxt|`np.genfromtxt()`]]:**
>     - More robust and flexible, designed to handle files with **missing values** and potentially different data types per column (can create structured arrays).
>     - Can automatically convert recognized missing values (e.g., `""`, `"NA"`, `"?"`) to a specified filling value (default is `np.nan` for float types).
>     - Can infer `dtype` per column if desired.
>     - Generally slower than `loadtxt` due to its increased flexibility and error handling.
> **When to use which:** Use `loadtxt` for clean, simple, purely numerical text files. Use `genfromtxt` when dealing with text files that might have missing data, require more complex parsing, or have columns of different types that you want to handle gracefully.

---
**Source:** Worksheet WS_NumPy, NumPy Documentation