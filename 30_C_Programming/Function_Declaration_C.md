---
tags: [c, concept, syntax, function]
aliases: [C Function Prototype, Function Signature C]
related:
  - "[[Function_C]]"
  - "[[Function_Definition_C]]"
  - "[[Function_Call_C]]"
  - "[[Header_file_C]]"
  - "[[Compiler_C]]"
  - "[[Linker_C]]"
  - "[[Forward_Declaration_C]]"
worksheet: [C_WS3, C_WS6]
date_created: 2025-04-11
---
# Function Declaration (C)

## Definition

A **Function Declaration**, often called a **Function Prototype**, in C specifies the function's name, its [[Return_Value_C|return type]], and the number and types of its [[Function_Parameters_C|parameters]]. It tells the [[Compiler_C|compiler]] how to correctly interpret and generate code for calls to that function, even if the function's actual [[Function_Definition_C|definition]] (implementation) appears later in the file or in a different source file altogether.

## Key Aspects / Characteristics

- **Interface Specification:** Defines the function's "signature" or interface without providing the implementation details.
- **Syntax:** `return_type function_name(parameter_type_list);`
    - Parameter names in the prototype are optional (only types are required), but including them can improve readability.
    - Ends with a semicolon `;`.
- **Enables Forward Calls:** Allows a function to be called before its definition is encountered by the compiler.
- **Type Checking:** Enables the compiler to check if the arguments passed in a [[Function_Call_C]] match the types specified in the declaration, helping to catch errors at compile time.
- **Header Files:** Function declarations for functions intended to be used across multiple source files are typically placed in [[Header_file_C|header files]] (`.h`), which are then `#include`d where needed.
- **Distinction from Definition:** A declaration lacks the function body (code within `{}`).

## Examples / Use Cases

**Declarations (Prototypes):**
```c
// In a header file (e.g., math_utils.h) or near top of .c file

int calculate_sum(int a, int b); // Prototype with parameter names
double compute_average(double data[], int size); // Array parameter type
void log_message(const char*); // Parameter name omitted, only type needed
void process_input(void); // Indicates function takes no parameters
```

**Usage in another file (e.g., main.c):**
```c
#include <stdio.h>
#include "math_utils.h" // Includes the declarations

int main() {
    int sum = calculate_sum(10, 20); // Compiler knows how to call calculate_sum
    printf("Sum: %d\n", sum);

    double values[] = {1.0, 2.0, 3.0};
    double avg = compute_average(values, 3);
    printf("Average: %f\n", avg);

    log_message("Program started.");
    process_input();

    return 0;
}
```

**Definition (e.g., in math_utils.c):**
```c
#include "math_utils.h" // Good practice to include own header

int calculate_sum(int a, int b) {
    return a + b;
}

// ... other definitions ...
```

## Related Concepts
- [[Function_C]] (The overall concept)
- [[Function_Definition_C]] (Provides the implementation)
- [[Function_Call_C]] (Uses the information from the declaration)
- [[Header_file_C]] (Common location for declarations)
- [[Compiler_C]] (Uses declarations for type checking)
- [[Linker_C]] (Connects function calls to definitions)
- [[Forward_Declaration_C]] (General concept including function prototypes)

## Questions / Further Study
>[!question] What should an .h File contain? (WS6)
> A [[Header_file_C|header file (`.h`)]] should primarily contain **declarations**, not definitions (with some exceptions like inline functions or static const initializations). This typically includes:
> - [[Function_Declaration_C|Function declarations (prototypes)]] for functions defined in the corresponding `.c` file.
> - [[struct_C]], [[union_C]], and [[enum_C]] type definitions.
> - `typedef` definitions.
> - [[Macro_C|Macro definitions]] (`#define`).
> - `extern` declarations for global variables defined in the corresponding `.c` file.
> It should **not** contain function definitions or global variable definitions, as this would violate the One Definition Rule if the header is included in multiple source files.

>[!question] What .h files should be #include in an .h file? (WS6)
> A header file should `#include` only the *minimum* set of other header files necessary to make the declarations *within that header file itself* compile correctly. For example, if your `widget.h` declares a function that takes a `FILE *` parameter, `widget.h` must `#include <stdio.h>`. Avoid including headers just because the corresponding `.c` file needs them – the `.c` file should include its own dependencies directly. Over-including in headers increases compile times and can create complex dependency chains. [[Forward_Declaration_C|Forward declarations]] of types (e.g., `struct AnotherType;`) can sometimes be used in headers instead of including the full header for `AnotherType`, especially if only pointers to that type are used.

---
**Source:** Worksheet C_WS3, C_WS6