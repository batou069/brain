---
tags:
  - numpy
  - python
  - data_structure
  - comparison
  - performance
  - memory
aliases:
  - NumPy Array vs Python List
related:
  - "[[NumPy_ndarray]]"
  - "[[Python_list]]" # Placeholder
  - "[[NumPy_Data_Types]]"
  - "[[NumPy_Vectorization]]"
  - "[[Memory_Management]]"
worksheet: [WS_NumPy]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# NumPy Array vs. Python List

## Definition

While both Python `list`s and NumPy `ndarray`s can store collections of items, they have fundamental differences in their design, capabilities, performance, and typical use cases.

- **Python `list`:** A built-in, general-purpose sequence type in Python. Lists are versatile, can hold elements of **heterogeneous** data types, and are **dynamically sized**.
- **NumPy `ndarray`:** The core data structure of the [[NumPy]] library. `ndarray`s are designed for numerical computation and store elements of a **homogeneous** data type in a fixed-size, multi-dimensional grid.

## Key Differences

| Feature             | Python `list`                                  | NumPy `ndarray`                                      |
| :------------------ | :--------------------------------------------- | :--------------------------------------------------- |
| **Data Type**       | Heterogeneous (can mix types)                  | Homogeneous (all elements same [[NumPy_Data_Types|type]]) |
| **Size**            | Dynamic (can grow/shrink easily)               | Fixed size upon creation (resizing creates new array)|
| **Storage**         | Stores pointers to objects scattered in memory | Contiguous block of memory for elements               |
| **Performance**     | Slower for numerical operations (Python loops) | Faster due to [[NumPy_Vectorization|vectorized]] C operations |
| **Memory Usage**    | Higher (overhead per element due to pointers and object typing) | Lower (more compact for numerical data)             |
| **Functionality**   | General-purpose sequence operations            | Rich set of mathematical & numerical functions       |
| **Dimensions**      | Primarily 1D (lists of lists for multi-D)      | N-dimensional arrays inherently                    |
| **Arithmetic Ops**  | Element-wise requires loops or comprehensions | Element-wise by default (vectorized)                |
| **Built-in/Library**| Built-in Python type                         | Provided by the external NumPy library             |

## Visualization (Conceptual Memory Layout)

**Python List:** `my_list = [1, "hello", 3.0]`
```mermaid
graph TD
    subgraph Python List Memory
        ListRef --> Obj1_Header(Header); ListRef --> Obj1_Val(1_int);
        ListRef --> Obj2_Header(Header); ListRef --> Obj2_Val("hello"_str);
        ListRef --> Obj3_Header(Header); ListRef --> Obj3_Val(3.0_float);

        my_list[my_list: ptrs] --> Ptr1(ptr_to_Obj1);
        my_list --> Ptr2(ptr_to_Obj2);
        my_list --> Ptr3(ptr_to_Obj3);

        Ptr1 --> Obj1_Val;
        Ptr2 --> Obj2_Val;
        Ptr3 --> Obj3_Val;
    end
    note right of Python List Memory : Elements are objects, potentially scattered. List stores pointers.
```

**NumPy Array:** `my_array = np.array([1, 2, 3], dtype=np.int32)`
```mermaid
graph TD
    subgraph NumPy Array Memory
        my_array[my_array: ndarray header (metadata)] --> DataBuffer["[1_i32 | 2_i32 | 3_i32] (Contiguous Data)"];
    end
    note right of NumPy Array Memory : Elements are raw data of same type, stored contiguously.
```

## When to Use Which

- **Use Python `list` when:**
    - You need to store heterogeneous data types.
    - The size of the collection needs to change frequently and easily.
    - General-purpose, flexible sequence operations are needed, and extreme numerical performance isn't the primary concern.
- **Use NumPy `ndarray` when:**
    - Performing numerical computations on large datasets.
    - You need efficient element-wise mathematical operations.
    - Working with multi-dimensional arrays (matrices, tensors).
    - Memory efficiency for numerical data is important.
    - Interfacing with other scientific Python libraries (Pandas, SciPy, Matplotlib).

## Performance Example (NumPy Exercise 1)

This exercise highlights the performance difference:
- "Perform the following operations with both `list` and `np.array`, and compare their performance: Create a-zero filled array/list, Add a constant to each element, Compute the dot product of two vectors, Apply exponentiation to each element, Merge/concatenate, Print all elements."
- *Expected Outcome:* For adding a constant, dot product, and exponentiation, NumPy arrays will be significantly faster due to [[NumPy_Vectorization|vectorized operations]] avoiding Python loops. List creation might be simpler for basic cases, but zero-filled array creation is direct in NumPy (`np.zeros`). Concatenation for NumPy arrays typically creates a new array. Printing might have similar performance for small sizes but can differ for very large structures.

## Related Concepts
- [[NumPy]], [[NumPy_ndarray]], [[Python_list]]
- [[NumPy_Data_Types]] (Homogeneity in NumPy)
- [[NumPy_Vectorization]] (Key performance benefit of NumPy)
- [[Memory_Management]] (Contiguous vs. scattered storage)
- [[Performance]]

## Questions / Further Study
>[!question] What is the difference between a list and a NumPy array? (WS_NumPy)
> Key differences:
> 1.  **Data Type:** Python lists can hold heterogeneous data types; NumPy arrays are homogeneous (all elements of the same type).
> 2.  **Performance:** NumPy arrays are significantly faster for numerical operations due to [[NumPy_Vectorization|vectorized]] C implementations and contiguous memory. Python lists require loops for element-wise math.
> 3.  **Memory:** NumPy arrays are more memory-efficient for numerical data. Python lists have more overhead per element.
> 4.  **Functionality:** NumPy provides a vast suite of mathematical functions optimized for arrays. Python lists are more general-purpose sequences.
> 5.  **Dimensions:** NumPy arrays inherently support N-dimensions. Python lists require lists-of-lists for multi-D.

---
**Source:** Worksheet WS_NumPy, NumPy Documentation