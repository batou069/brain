---
tags:
  - MOC
  - c_programming
  - c
date_created: 2025-04-11
---
# C Programming MOC (Map of Content)

This note serves as a central hub for all topics related to the **C Programming Language** covered in the course.

## Core Concepts
- [[C_Language]] (Overview - *to be created*)
- [[Variable_Declaration_C]] vs [[Variable_Definition_C]]
- [[Data_Types_C]] (int, char, float, double, etc. - *to be created*)
- [[Expression_C]]
- [[Operator_C]] & [[Operator_Precedence_C]]
- [[Sequence_Point_C]]
- [[Control_Flow_C]] (if, else, switch, for, while, do-while - *to be created*)
- [[Function_C]]
- [[Pointer_C]]
- [[Array_C]]
- [[String_in_C]]
- [[struct_C]]
- [[enum_C]]
- [[Type_Cast_C]]
- [[Preprocessor_C]]
- [[Header_file_C]]
- [[Static_C]] (Variables & Functions)
- [[Interface_C]] vs [[Implementation_C]]

## Memory Management
- [[Memory_Segments_C]] ([[Code_Segment_C]], [[Data_Segment_C]], [[BSS_Segment_C]], [[Heap_Memory_C]], [[Stack_Memory_C]])
- [[Scope_C]] & Lifetime
- [[Local_Variable_C]] / [[Automatic_Variable_C]]
- [[Static_Variable_C]]
- [[Dynamic_Allocation_C]] ([[malloc]], [[free]], [[realloc]] - *realloc to be added*)
- [[Dangling_Pointer_C]]
- [[NULL_C]]

## Build Process & Tools
- [[Build_Process_C]]
- [[Compiler_C]]
- [[Linker_C]]
- [[Loader_C]]
- [[Symbol_C]] ([[Strong_Symbol_C]], [[Weak_Symbol_C]])
- [[Static_Library_C]] (`ar` - *to be created*)
- [[Shared_Library_C]] (*to be created*)
- [[ar_command]]
- [[nm_command]]
- [[objdump_command]]

## File Handling
- [[File_Handling_C]] (*to be created*)
- [[FILE_pointer_C]]
- [[stdin_stdout_stderr_C]]
- [[fopen]], [[fclose]], [[fread]], [[fwrite]], [[fseek]], [[ftell]], [[fflush]], [[fgets]], [[fgetc]], [[fputs]], [[fputc]]

## Input/Output Functions
- [[printf]]
- [[scanf]]
- [[sprintf]]
- [[fgets]], [[fgetc]], [[fputs]], [[fputc]]

## Keywords & Identifiers
- `auto`, `break`, `case`, `char`, `const`, `continue`, `default`, `do`, `double`, `else`, `enum`, `extern`, `float`, `for`, `goto`, `if`, `int`, `long`, `register`, `return`, `short`, `signed`, `sizeof`, `static`, `struct`, `switch`, `typedef`, `union`, `unsigned`, `void`, `volatile`, `while` (*Individual files not typically needed unless specific behavior is discussed*)
- [[sizeof_operator_C]]

## Character Encoding & Representation
- [[bits]], [[bytes]]
- [[wchar]]
- [[Number_Systems]] (Binary, Octal, Decimal, Hexadecimal)
- [[ASCII]]
- [[Unicode]]
- [[UTF-8]]
- [[Escape_Characters_C]]

## Notes in this Section

```dataview
LIST
FROM "30_C_Programming"
WHERE file.folder = this.file.folder AND file.name != this.file.name AND !contains(file.name, "MOC")
SORT file.name ASC
```

