---
tags:
  - numpy
  - python
  - file_io
  - serialization
  - comparison
aliases:
  - NumPy Save vs Pickle
related:
  - "[[NumPy_save_load]]"
  - "[[Pickle_Python]]"
  - "[[Data_Serialization]]"
  - "[[NumPy_ndarray]]"
  - "[[Performance]]"
  - "[[Security]]"
worksheet: [WS_NumPy]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# NumPy `.npy`/`.npz` vs. Python Pickle

## Definition

Both NumPy's native binary formats (`.npy` for single arrays, `.npz` for multiple arrays) and Python's [[Pickle_Python|`pickle`]] module provide mechanisms for **[[Data_Serialization|serializing]]** Python objects to disk and deserializing them back into memory. However, they have different design goals, strengths, and weaknesses, especially concerning [[NumPy_ndarray|NumPy arrays]].

## Comparison: `np.save`/`np.load` vs. `pickle` for NumPy Arrays


| Feature                           | `np.save`/`np.load` (`.npy`/`.npz`)                                                                                               | `pickle.dump`/`pickle.load`                                                                     |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| **Primary Purpose**               | Efficient serialization of NumPy arrays                                                                                           | General Python object serialization                                                             |
| **Data Format**                   | Custom binary format (NPY/NPZ) for arrays                                                                                         | Pickle protocol (Python-specific binary format)                                                 |
| **NumPy Array Support**           | Excellent, native, optimized                                                                                                      | Can serialize ndarrays as Python objects                                                        |
| **Performance (Arrays)**          | Generally **faster** for saving/loading arrays                                                                                    | Generally slower for arrays                                                                     |
| **File Size (Arrays)**            | Usually **smaller** (stores raw data efficiently)                                                                                 | Potentially larger (stores object overhead)                                                     |
| **Metadata**                      | Stores shape, dtype, order efficiently                                                                                            | Stores general object state                                                                     |
| **Memory Mapping**                | Supported by `np.load(mmap_mode=...)`                                                                                             | Not directly supported                                                                          |
| **Language Indep. (Data)**        | Raw numerical data is somewhat portable                                                                                           | Highly Python-specific format                                                                   |
| **Security**                      | Safer for loading array data if `allow_pickle=False` (default for `np.load`). The `.npy` format itself is just data and metadata. | **Potential security risk:** Unpickling data from untrusted sources can execute arbitrary code. |
| **Object Types**                  | Primarily `ndarray`. Can save object arrays using pickle if `allow_pickle=True` during `np.save`.                                 | Can serialize almost any Python object (lists, dicts, custom classes, functions, etc.)          |
| **Portability (Python versions)** | Good for numerical data. Pickled object arrays might have Python version issues.                                                  | Can have issues between major Python versions or with changes in class definitions.             |


## Key Advantages of `np.save`/`np.load` for NumPy Arrays (WS_NumPy Question)

1.  **Performance:** Optimized for reading and writing the contiguous data blocks and metadata (`shape`, `dtype`, `order`) of `ndarray`s. This is typically much faster than the generic object serialization done by `pickle`.
2.  **Memory Efficiency (File Size):** The `.npy` format is designed to be compact for numerical data, storing the raw bytes along with essential metadata. Pickle adds more overhead for serializing the Python object structure of an array.
3.  **Memory Mapping:** `np.load`'s `mmap_mode` allows large arrays to be accessed from disk without loading the entire array into RAM at once, which is crucial for out-of-core processing. Pickle loads the entire object.
4.  **Simplicity for Arrays:** The API is straightforward for its specific purpose.
5.  **Security (when `allow_pickle=False`):** When loading `.npy` files (which are not supposed to contain arbitrary pickled objects unless `allow_pickle=True` was used at save time), `np.load` with its default `allow_pickle=False` is safer than blindly unpickling arbitrary files. The `.npy` structure itself is just data and simple metadata.

## When to Use Pickle

- When you need to serialize **general Python objects** that are not NumPy arrays (e.g., custom class instances, lists of mixed types, dictionaries containing various objects).
- When you need to serialize a collection of diverse Python objects where NumPy arrays might be just one part.
- If `np.save` is used with `allow_pickle=True` for object arrays, it internally uses pickle for those objects.

## Conclusion

- For **serializing and deserializing NumPy arrays**, `np.save`, `np.savez`, `np.savez_compressed`, and `np.load` are generally the **preferred, more efficient, and safer** methods.
- For **general Python object serialization**, `pickle` is the standard tool.

## Related Concepts
- [[NumPy_save_load]], [[NumPy_ndarray]]
- [[Pickle_Python]]
- [[Data_Serialization]]
- [[Performance]], [[Memory_Management]], [[Security]]

---
**Source:** Worksheet WS_NumPy, NumPy & Python Documentation