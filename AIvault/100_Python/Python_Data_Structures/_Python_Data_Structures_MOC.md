---
tags:
  - python
  - data_structures
  - list
  - tuple
  - set
  - dictionary
  - mutability
  - immutability
  - moc
  - concept
aliases:
  - Python Data Structures MOC
  - Python Collections MOC
related:
  - "[[100_Python/_Python_Programming_MOC|_Python_Programming_MOC]]"
  - "[[Python_Primitive_Types]]"
  - "[[Python_Mutability_Immutability|Mutability and Immutability in Python]]"
  - "[[Python_List]]"
  - "[[Python_Tuple]]"
  - "[[Python_Set_Frozenset|Python Set and Frozenset]]"
  - "[[Python_Dictionary]]"
  - "[[Python_Slicing]]"
  - "[[Python_Loops_Iteration|Looping and Iteration]]"
worksheet:
  - WS17
date_created: 2025-06-11
---
# Python Data Structures MOC 🧱

This section covers Python's built-in data structures, which are used to store and organize collections of data. Understanding their characteristics, common operations, and when to use each is fundamental to effective Python programming.

## Core Concepts
-   [[Python_Mutability_Immutability|Mutability and Immutability in Python]]
    -   Understanding which data structures can be changed in place and which cannot.
-   [[Python_Loops_Iteration|Looping Over Data Structures]]
-   [[Python_Slicing|Slicing]] (for sequence types like lists, tuples, strings)
-   [[Python_Data_Structures_Type_Mixing|Mixing Element Types in Data Structures]]
-   [[Python_Data_Structures_Ordered_Unordered|Ordered vs. Unordered Data Structures]]
-   [[Python_Data_Structures_Identity_vs_Equality|Identity (`is`) vs. Equality (`==`)]]

## Built-in Data Structures
[list2card|addClass(ab-col2)|#Python Data Structures]
- **[[Python_List|Lists (`list`)]]** 📝
  - Ordered, mutable sequences.
  - Defined with `[]`.
  - Common methods: `append()`, `extend()`, `insert()`, `remove()`, `pop()`, `sort()`, `reverse()`, `index()`, `count()`.
- **[[Python_Tuple|Tuples (`tuple`)]]**  ثابت
  - Ordered, immutable sequences.
  - Defined with `()`.
  - Often used for fixed collections of items or where immutability is desired (e.g., dictionary keys).
- **[[Python_Set_Frozenset|Sets (`set`)]]** ❄️
  - Unordered collections of unique, immutable elements.
  - Defined with `{}` (e.g., `{1, 2, 3}`) or `set()`. An empty set must be created with `set()`.
  - Support mathematical set operations (union, intersection, difference).
- **[[Python_Set_Frozenset|Frozen Sets (`frozenset`)]]** 🧊
  - Immutable version of a set. Can be used as dictionary keys or elements of other sets.
- **[[Python_Dictionary|Dictionaries (`dict`)]]** 📖
  - Unordered (in Python < 3.7, ordered in Python 3.7+) collections of key-value pairs. Keys must be unique and immutable.
  - Defined with `{}` (e.g., `{'key1': 'value1', 'key2': 'value2'}`).
  - Common methods: `get()`, `keys()`, `values()`, `items()`, `update()`, `pop()`, `popitem()`.

## Built-in Functions Relevant to Data Structures
-   [[Built_In_Functions_Python#id()|`id()`]]
-   [[Built_In_Functions_Python#len()|`len()`]]
-   [[Built_In_Functions_Python#max()|`max()`]], [[Built_In_Functions_Python#min()|`min()`]] (for ordered types or types with comparable elements)
-   [[Built_In_Functions_Python#slice()|`slice()`]] (less common than slice notation `[:]`)

## Notes in this Section
```dataview
LIST
FROM "100_Python/Python_Data_Structures"
WHERE file.folder = this.file.folder AND file.name != this.file.name AND !contains(file.name, "MOC")
SORT file.name ASC
```

---