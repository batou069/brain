---
tags: [c_programming, concept, c, keyword, variable]
aliases: []
related:
  - "[[Variable_Definition_C]]"
  - "[[Data_Types_C]]"
  - "[[Scope_C]]"
  - "[[Forward_Declaration_C]]"
worksheet: [WS]
date_created: 2025-04-12
---
# Variable Declaration (C)

## Definition

In C, a **declaration** introduces an identifier (like a variable or function name) and specifies its type to the [[Compiler_C]]. For variables, a declaration tells the compiler about the variable's name and type, but it does *not* allocate memory or assign an initial value (unless it's also a definition). Declarations are often used to make a variable or function visible in a scope before its actual definition appears, especially when using multiple source files or [[Forward_Declaration_C|forward declarations]].

## Key Aspects / Characteristics

- **Introduces Name & Type:** Tells the compiler "this name exists, and this is its type".
- **No Memory Allocation (Typically):** A pure declaration (especially using `extern`) doesn't reserve storage space.
- **Scope:** Makes the identifier known within the current scope.
- **`extern` Keyword:** The `extern` keyword is explicitly used to declare a variable without defining it. It signals that the variable is defined elsewhere (in the same file later, or in a different file).

## Examples / Use Cases

**Pure Declaration (using `extern`)**
```c
// In file1.c (or header file)
extern int global_counter; // Declares global_counter, defined elsewhere
extern const char* app_name; // Declares app_name

void process_data(); // Function declaration (prototype)
```

**Declaration combined with Definition**```c  
int local_value; // This is both a declaration AND a definition (allocates memory)
## Related Concepts
- [[Variable_Definition_C]] (Declaration that *also* allocates memory)
- [[Data_Types_C]] (Specifies the type being declared)
- [[Scope_C]] (Where the declaration is valid)
- [[Forward_Declaration_C]] (Declaring something before its full definition)
- [[extern_keyword_C]] (Keyword used for pure declarations of global variables)
- [[Linker_C]] (Resolves references to externally declared variables/functions)

## Questions / Further Study
>[!question] What is the difference between declaration and definition?
> A **declaration** introduces a name and type to the compiler (`extern int x;`, `void func();`). A **[[Variable_Definition_C|definition]]** is a declaration that also allocates storage (`int x;`, `int y = 10;`, `void func() { /* body */ }`). You can declare something multiple times (e.g., in multiple files via a header), but you can only *define* it once in the entire program.

---
**Source:** Worksheet C_WS1
