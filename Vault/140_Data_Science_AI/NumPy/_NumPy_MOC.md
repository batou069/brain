---
tags:
  - MOC
  - numpy
  - python
  - data_science
  - numerical_computing
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# NumPy MOC (Map of Content)

This note serves as a central hub for all topics related to **NumPy (Numerical Python)**.

## Core Concepts
- "[[NumPy]]" (Overview)
- "[[NumPy_ndarray]]" (The core array object)
- "[[NumPy_Data_Types]]" (dtypes)
- "[[NumPy_Array_vs_List]]" (Comparison)
- "[[NumPy_Dimension_Shape_Axis]]"
- "[[NumPy_Reshaping]]"
- "[[NumPy_Broadcasting]]"
- "[[NumPy_Indexing_Slicing]]"
- "[[NumPy_Boolean_Indexing]]"
- "[[NumPy_Views_vs_Copies]]"
- "[[NumPy_Universal_Functions]]" (ufuncs)
- "[[NumPy_Vectorization]]"
- "[[NumPy_NaN]]" (Not a Number)
- "[[NumPy_Empty_Array]]"

## Array Creation
- `np.array()`
- `np.zeros()`, `np.ones()`, `np.empty()`
- `np.arange()`
- `np.linspace()`, `np.logspace()`
- `np.full()`, `np.eye()`
- `np.random.*` (e.g., `rand`, `randn`, `randint`)
- From existing data, from files

## File I/O
- "[[NumPy_loadtxt]]"
- "[[NumPy_genfromtxt]]"
- "[[NumPy_save_load]]" (`np.save`, `np.savez`, `np.savez_compressed`, `np.load`)
- "[[Pickle_Python]]" (Comparison with `np.save`)

## Operations & Functions
- Element-wise arithmetic
- "[[Dot_Product]]" (`np.dot`, `@` operator)
- Matrix Multiplication (`@` operator, `np.matmul`)
- "[[NumPy_Transpose]]" (`.T` attribute, `np.transpose()`)
- "[[NumPy_Swapaxes]]"
- Aggregation functions (`np.sum`, `np.min`, `np.max`, `np.mean`, `np.std`, etc.)
- "[[NumPy_sum_vs_python_sum]]"
- Mathematical functions (`np.sqrt`, `np.exp`, `np.log`, trigonometric, etc.)
- `np.linalg` module (e.g., "[[NumPy_linalg_inv]]", "[[NumPy_linalg_det]]", "[[NumPy_linalg_solve]]", "[[NumPy_linalg_eig]]") # Placeholder
- "[[NumPy_linalg_norm]]" (for vector magnitude) # Placeholder
- "[[NumPy_Softmax]]" # Placeholder

## Exercises & Questions (from provided worksheet)
- *This section will link to notes discussing specific questions from the worksheet.*
- "[[NumPy_Exercises_WS_Image]]" # For exercise-specific discussions

## Related Libraries
- "[[Matplotlib_MOC|Matplotlib]]" (Plotting)
- "[[Pillow_PIL_MOC|Pillow (PIL)]]" (Image processing)
- "[[Pandas_MOC|Pandas]]" (Data analysis, uses NumPy arrays)
- "[[SciPy_MOC|SciPy]]" (Scientific computing, builds on NumPy - *Placeholder*)

## Notes in this Section

```dataview
LIST
FROM "140_Data_Science_AI/NumPy"
WHERE file.folder = this.file.folder AND file.name != this.file.name AND !contains(file.name, "MOC")
SORT file.name ASC
```

---
Use this MOC to navigate the NumPy section.