---
tags:
  - numpy
  - python
  - file_io
  - function
  - data_persistence
  - binary_format
aliases:
  - np.save
  - np.load
  - np.savez
  - np.savez_compressed
  - NPY format
  - NPZ format
related:
  - "[[NumPy_ndarray]]"
  - "[[NumPy_loadtxt]]"
  - "[[NumPy_genfromtxt]]"
  - "[[Pickle_Python]]"
  - "[[Data_Serialization]]" # Placeholder
worksheet: [WS_NumPy]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# NumPy `save` and `load` (`.npy`, `.npz`)

## Definition

NumPy provides functions for saving and loading `ndarray` objects to and from disk in efficient **binary formats**:

-   **`.npy` format:** Used for saving a **single** NumPy array. Created by `np.save()`.
-   **`.npz` format:** Used for saving **multiple** NumPy arrays into a single, uncompressed archive file. Created by `np.savez()`.
-   **Compressed `.npz` format:** Similar to `.npz` but uses compression to save disk space. Created by `np.savez_compressed()`.

Loading from these formats is done using `np.load()`.

## `np.save(file, arr, allow_pickle=True, fix_imports=True)`

- **Purpose:** Saves a single array to a binary file in `.npy` format.
- **Parameters:**
    - `file`: Filename (string or file object). If a string, `.npy` is automatically appended if not present.
    - `arr`: Array to be saved.
    - `allow_pickle`: (Default `True`) Allows saving object arrays using Python's [[Pickle_Python|pickle]]. If `False`, saving object arrays will raise an error. For security, set to `False` if not pickling arbitrary objects.
    - `fix_imports`: For loading pickled object arrays on Python 2 from Python 3.
- **Format:** The `.npy` format stores array metadata (dtype, shape, etc.) and the raw array data in a simple binary structure.

## `np.load(file, mmap_mode=None, allow_pickle=False, fix_imports=True, encoding='ASCII')`

- **Purpose:** Loads arrays or pickled objects from `.npy`, `.npz`, or pickled files.
- **Parameters:**
    - `file`: Filename (string or file object).
    - `mmap_mode`: (Optional) If not `None`, memory-map the file. Useful for very large arrays as it doesn't load the entire array into memory at once. Options: `'r+'` (read/write), `'r'` (read-only), `'w+'` (write, copy-on-write), `'c'` (copy-on-write).
    - `allow_pickle`: (Default `False` for security since NumPy 1.16.3) Set to `True` to allow loading pickled object arrays. Use with caution if loading files from untrusted sources.
- **Return Value:**
    - For `.npy` files: Returns the single array.
    - For `.npz` files: Returns an `NpzFile` object (acts like a dictionary) from which individual arrays can be accessed by their saved names.

## `np.savez(file, *args, **kwds)`

- **Purpose:** Saves multiple arrays into a single uncompressed `.npz` archive.
- **Parameters:**
    - `file`: Filename (string or file object). If a string, `.npz` is appended if not present.
    - `*args`: Arrays to save using default names (`arr_0`, `arr_1`, etc.).
    - `**kwds`: Arrays to save using specified keyword names (e.g., `np.savez("data.npz", array_one=a, array_two=b)`).

## `np.savez_compressed(file, *args, **kwds)`

- **Purpose:** Same as `np.savez()`, but saves the arrays into a compressed `.npz` archive (using ZIP DEFLATE).
- **Benefit:** Reduces file size on disk, especially for arrays that compress well.
- **Trade-off:** Slower to save and load compared to uncompressed `np.savez()`.

## Example

```python
import numpy as np
import os

# Create some arrays
arr1 = np.arange(10)
arr2 = np.array([, , ])
arr_complex = np.array([1+2j, 3+4j])

# --- Using np.save and np.load (.npy) ---
print("--- .npy format ---")
np.save("single_array.npy", arr1)
loaded_arr1 = np.load("single_array.npy")
print(f"Loaded arr1: {loaded_arr1}")

# --- Using np.savez and np.load (.npz) ---
print("\n--- .npz format (uncompressed) ---")
np.savez("multiple_arrays.npz", first=arr1, matrix=arr2, complex_nums=arr_complex)
data_archive = np.load("multiple_arrays.npz")

print(f"Keys in archive: {list(data_archive.keys())}")
loaded_arr1_from_npz = data_archive['first']
loaded_matrix_from_npz = data_archive['matrix']
loaded_complex_from_npz = data_archive['complex_nums']

print(f"Loaded 'first' from npz: {loaded_arr1_from_npz}")
print(f"Loaded 'matrix' from npz:\n{loaded_matrix_from_npz}")
print(f"Loaded 'complex_nums' from npz: {loaded_complex_from_npz}")
data_archive.close() # Good practice for NpzFile objects

# --- Using np.savez_compressed and np.load (.npz) ---
print("\n--- .npz format (compressed) ---")
np.savez_compressed("multiple_arrays_compressed.npz", first=arr1, matrix=arr2)
data_archive_compressed = np.load("multiple_arrays_compressed.npz")
print(f"Keys in compressed archive: {list(data_archive_compressed.keys())}")
print(f"Loaded 'matrix' from compressed npz:\n{data_archive_compressed['matrix']}")
data_archive_compressed.close()

# --- Clean up ---
os.remove("single_array.npy")
os.remove("multiple_arrays.npz")
os.remove("multiple_arrays_compressed.npz")
```

## Related Concepts
- [[NumPy_ndarray]]
- [[NumPy_loadtxt]], [[NumPy_genfromtxt]] (For text files)
- [[Pickle_Python]] (General Python object serialization)
- [[Data_Serialization]], File I/O
- Binary file formats

## Questions / Further Study
>[!question] What are the advantages of `np.save` over Pickle? (WS_NumPy)
> 1.  **Optimized for NumPy Arrays:** The `.npy`/`.npz` formats are specifically designed for NumPy arrays. They store metadata like `shape`, `dtype`, and memory layout (`order`) efficiently, allowing for very fast loading directly into a NumPy array without extra parsing or conversion overhead.
> 2.  **Performance:** Generally faster for saving and loading large numerical arrays compared to pickling, which involves more generic object serialization.
> 3.  **Memory Mapping (`mmap_mode`):** `np.load` supports memory mapping, allowing parts of very large arrays to be accessed without loading the entire file into RAM. Pickle doesn't offer this directly.
> 4.  **Language Independence (for data):** While the metadata is NumPy-specific, the raw numerical data in `.npy` files is stored in a simple binary format that could potentially be read by other languages/tools if the format is understood (though this is not its primary design goal). Pickled objects are highly Python-specific.
> 5.  **Portability (Numerical Data):** The `.npy` format handles endianness and data type information, making numerical data more portable across different machine architectures compared to raw binary dumps.
> 6.  **Security (with `allow_pickle=False`):** When loading `.npy` files (which don't store arbitrary objects unless `allow_pickle` was true during save), `np.load()` with `allow_pickle=False` (the default since NumPy 1.16.3) is safer than unpickling arbitrary files from untrusted sources, as unpickling can execute arbitrary code.
>
> [[Pickle_Python|Pickle]] is more general and can serialize almost any Python object, including complex custom classes and their state, while `np.save` is tailored for `ndarray`s. For `ndarray`s, `np.save`/`np.load` is usually preferred.

---
**Source:** Worksheet WS_NumPy, NumPy Documentation