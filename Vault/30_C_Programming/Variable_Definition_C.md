---
tags: [c, concept, keyword, variable, memory]
aliases: [C Definition]
related:
  - "[[Variable_Declaration_C]]"
  - "[[Data_Types_C]]"
  - "[[Scope_C]]"
  - "[[Memory_Segments_C]]"
  - "[[Initialization_C]]"
worksheet: [C_WS1]
date_created: 2025-04-12
---
# Variable Definition (C)

## Definition

In C, a **definition** is a [[Variable_Declaration_C|declaration]] that also reserves storage (allocates memory) for the variable. For functions, a definition provides the actual body (implementation) of the function. Every variable or function used in a program must have exactly one definition within the entire program (across all source files linked together), although it can be declared multiple times (e.g., via [[Header_file_C|header files]]).

## Key Aspects / Characteristics

- **Allocates Memory:** Reserves space in the appropriate memory segment ([[Data_Segment_C]], [[BSS_Segment_C]], [[Stack_Memory_C]]) based on the variable's type and storage class.
- **Is Also a Declaration:** A definition implicitly declares the variable or function.
- **Initialization:** A definition can optionally include an initializer to provide an initial value. If omitted, the initial value depends on the variable's storage duration (e.g., static/global variables are zero-initialized, automatic/local variables have indeterminate 'garbage' values).
- **One Definition Rule (ODR):** A variable or function can only be defined once in a program. Multiple definitions typically lead to a [[Linker_C|linker]] error.

## Examples / Use Cases

**Variable Definitions**
```c
int count;             // Definition of an integer (global/static: zero-initialized, local: indeterminate)
double price = 99.95;  // Definition and initialization
char initial = 'J';    // Definition and initialization
int coordinates[3];    // Definition of an integer array (allocates space for 3 ints)

void setup() {
    static int setup_called = 0; // Definition of a static local variable
    int local_temp;              // Definition of an automatic local variable
    // ...
}
```

**Function Definition**

```c
int add(int a, int b) { // Definition of function 'add'
    return a + b;
}
```

## Related Concepts

- [[Variable_Declaration_C]] (Introduces name/type without necessarily allocating memory)
- [[Initialization_C]] (Providing an initial value during definition)
- [[Memory_Segments_C]] (Where the allocated memory resides)
- [[Scope_C]] (Determines visibility)
- [[Storage_Duration_C]] (static, automatic - affects initialization and lifetime - to be created)
- [[Linker_C]] (Enforces the One Definition Rule)
## Questions / Further Study

> [!question] Which variables are initialized automatically? How? Why? (WS6)  
> Variables with static storage duration are initialized automatically before program startup (or the first time their defining block is entered for static locals).
> 
> - **How:** If no explicit initializer is provided, they are zero-initialized (integers/floats to 0, pointers to NULL, etc.). If an initializer is provided, they are initialized with that constant value.
>     
> - **Why:** These variables exist for the entire lifetime of the program (or function call for static locals across calls) and reside in fixed memory locations ([[Data_Segment_C]] or [[BSS_Segment_C]]). The runtime environment or compiler ensures they have a predictable state before being used.  
>     [[Automatic_Variable_C|Automatic (local) variables]] (on the [[Stack_Memory_C|stack]]) are **not** automatically initialized by the C standard. Their initial value is indeterminate ("garbage") unless explicitly initialized in the definition.
>     

> [!question] What is the 'garbage' that you get when you don't initialize a variable? (WS6)  
> The "garbage" value in an uninitialized [[Automatic_Variable_C|automatic (local) variable]] is simply the sequence of [[bits]] that happen to be present in the memory location ([[Stack_Memory_C|stack frame]]) allocated for that variable when it comes into scope. This memory might have been used previously by other function calls or data, and its contents were not cleared before being assigned to the new variable. Accessing this indeterminate value leads to undefined behavior.

---

**Source:** Worksheet C_WS1, C_WS6