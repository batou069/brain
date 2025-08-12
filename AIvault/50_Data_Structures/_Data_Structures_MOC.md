---
tags:
  - MOC
  - data_structures
  - concept
  - core
date_created: 2025-04-12
aliases:
  - Data Structures
related:
  - "[[Abstract_Data_Type]]"
  - "[[Algorithm]]"
  - "[[Computational_Complexity]]"
  - "[[50_Data_Structures/Memory_Management]]"
  - "[[Array_C]]"
  - "[[Linked_List_ADT]]"
  - "[[Stack_ADT]]"
  - "[[Queue_ADT]]"
  - "[[Tree_DS]]"
  - "[[Graph_DS]]"
worksheet:
  - WS7
---
# Data Structures MOC (Map of Content)

This note serves as a central hub for all topics related to **Data Structures**.

## Core Concepts
- [[Data_Structure]]
- [[Abstract_Data_Type]] (ADT)
- [[Computational_Complexity]] (Big O Notation: [[O_1]], [[O_log_n]], [[O_n]], [[O_n_log_n]], [[O_n_c]], [[O_c_n]])
- [[Time_Complexity]] vs [[Space_Complexity]]
- [[Amortized_Complexity]]
- [[Efficiency_vs_Performance]]
- Linear vs Non-Linear Data Structures (*Implied*)
- Direct Access vs Sequential Access

## Basic Structures & ADTs
- [[Record_DS]] (Struct)
- [[Union_DS]]
- [[Variant_DS]]
- [[Array_C]] (Static Array)
- [[Vector_DS]] (Dynamic Array)
- [[Bitmap_DS]] (Bit Array)
- [[Matrix_DS]]

## Linear Abstract Data Types
- [[Stack_ADT]] (LIFO)
- [[Queue_ADT]] (FIFO)
- [[Circular_Queue_DS]]
- [[Circular_Buffer_DS]]
- [[Linked_List_ADT]]
- [[Priority_Queue_ADT]]
- [[Double-Ended_Queue_ADT]] (Deque)

## Linked List Implementations
- [[Singly_Linked_List_DS]]
- [[Doubly_Linked_List_DS]]
- [[Circular_Linked_List_DS]]
- [[Skip_List_DS]]

## Associative Structures
- [[Hash_Table_DS]]
- [[Hash_Function]]

## Trees & Heaps (Placeholders)
- [[Tree_DS]]
- [[Binary_Search_Tree_DS]]
- [[Heap_DS]]

## Graphs (Placeholders)
- [[Graph_DS]]

## Notes in this Section

```dataview
LIST
FROM "50_Data_Structures"
WHERE file.folder = this.file.folder AND file.name != this.file.name AND !contains(file.name, "MOC")
SORT file.name ASC
```