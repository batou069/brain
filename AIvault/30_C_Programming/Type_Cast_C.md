---
tags: [c, concept, operator, type_system]
aliases: [C Type Casting, Explicit Type Conversion]
related:
  - "[[Data_Types_C]]"
  - "[[Pointer_C]]"
  - "[[Operator_C]]"
  - "[[Implicit_Type_Conversion_C]]"
worksheet: [C_WS3]
date_created: 2025-04-11
---
# Type Cast (C)

## Definition

A **Type Cast** in C is an explicit conversion of a value from one [[Data_Types_C|data type]] to another. It is performed using the cast operator `(type_name)`, where `type_name` is the target data type you want to convert the expression's value to.

## Key Aspects / Characteristics

- **Explicit Conversion:** Unlike [[Implicit_Type_Conversion_C|implicit conversions]] (which the compiler performs automatically according to rules), type casts are requested explicitly by the programmer.
- **Syntax:** `(target_type) expression`
- **Value Conversion:** Attempts to convert the value of the `expression` into a representation suitable for the `target_type`.
- **Potential Information Loss:** Casting to a type that cannot represent the full range of the original type can lead to loss of information or precision (e.g., casting a `double` to an `int` truncates the fractional part; casting a large `int` to a `short` might overflow).
- **Pointer Casting:** Can be used to convert pointer types (e.g., `void*` to `int*`, or even `int*` to `char*`). This should be done with extreme caution as it can easily break type safety and lead to [[Undefined_Behavior_C]] if not done correctly (e.g., violating alignment rules or accessing memory incorrectly).
- **Uses:**
    - Forcing a specific type of arithmetic (e.g., floating-point division instead of integer division).
    - Converting generic pointers (`void*`) returned by functions like [[malloc]] to specific pointer types.
    - Interfacing with APIs that expect specific types.
    - Suppressing compiler warnings about implicit conversions (though this might hide underlying issues).

## Examples / Use Cases

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int i1 = 10, i2 = 4;
    double result_double;
    int result_int;
    char c;

    // 1. Forcing floating-point division
    result_double = i1 / i2; // Integer division: result_double = 2.0
    printf("Integer division: %f\n", result_double);

    result_double = (double)i1 / i2; // Cast i1 to double BEFORE division
    printf("Floating-point division (cast i1): %f\n", result_double); // Output: 2.5

    result_double = i1 / (double)i2; // Cast i2 to double BEFORE division
    printf("Floating-point division (cast i2): %f\n", result_double); // Output: 2.5

    result_double = (double)i1 / (double)i2; // Cast both
    printf("Floating-point division (cast both): %f\n", result_double); // Output: 2.5

    // 2. Casting double to int (truncation)
    result_double = 3.14159;
    result_int = (int)result_double;
    printf("Casting double %f to int: %d\n", result_double, result_int); // Output: 3

    // 3. Casting int to char (potential data loss if int > char range)
    result_int = 65;
    c = (char)result_int;
    printf("Casting int %d to char: %c\n", result_int, c); // Output: A

    result_int = 300; // Assuming char is 8-bit (-128 to 127 or 0 to 255)
    c = (char)result_int; // Value of c is implementation-defined (often wraps around)
    printf("Casting int %d to char (overflow): %d\n", result_int, c);

    // 4. Casting void* from malloc
    int *arr = (int*)malloc(10 * sizeof(int)); // Cast void* return value
    if (arr == NULL) return 1;
    arr[0] = 100;
    printf("arr[0]: %d\n", arr[0]);
    free(arr);

    return 0;
}
```

## Related Concepts
- [[Data_Types_C]] (The types involved in the conversion)
- [[Implicit_Type_Conversion_C]] (Automatic conversions done by the compiler)
- [[Pointer_C]] (Casting pointers requires care)
- [[malloc]] (Returns `void*` which usually needs casting)
- [[Undefined_Behavior_C]] (Can result from improper casting, especially with pointers)

---
**Source:** Worksheet C_WS3