---
tags:
  - c
  - concept
  - operator
  - memory
  - type_system
  - compile_time
aliases:
  - sizeof C
related:
  - "[[Operator_C]]"
  - "[[Data_Types_C]]"
  - "[[Array_C]]"
  - "[[struct_C]]"
  - "[[Pointer_C]]"
  - "[[bytes]]"
  - "[[50_Data_Structures/Memory_Management]]"
  - "[[Dynamic_Allocation_C]]"
worksheet:
  - C_WS4
date_created: 2025-04-12
---
# `sizeof` Operator (C)

## Definition

The `sizeof` operator is a unary [[Operator_C]] in C that yields the size, in [[bytes]], of its operand. The operand can be either a data type name enclosed in parentheses (e.g., `sizeof(int)`) or an expression (e.g., `sizeof x`, `sizeof(my_array)`). Crucially, `sizeof` is evaluated at **compile time** (except for Variable Length Arrays - VLAs), and it does *not* evaluate the expression operand itself (if it's an expression).

## Key Aspects / Characteristics

- **Compile-Time Evaluation:** The size is determined by the compiler based on the type of the operand. No runtime code is executed for `sizeof` itself (except for VLAs).
- **Result Type:** The result is an unsigned integer value of type `size_t` (defined in `<stddef.h>` and other headers). `size_t` is large enough to represent the size of the largest possible object on the system. Use `%zu` format specifier in [[printf]] for `size_t`.
- **Operand Types:**
    - **Type Name:** `sizeof(type_name)` gives the size in bytes of objects of that type (e.g., `sizeof(char)`, `sizeof(double)`, `sizeof(struct MyData)`). Parentheses are required around type names.
    - **Expression:** `sizeof expression` or `sizeof(expression)` gives the size in bytes of the type that the expression *would have* if evaluated. The expression itself is *not* evaluated. Parentheses are optional for expressions unless needed for precedence.
- **Result in Bytes:** The size is always returned in bytes. `sizeof(char)` is guaranteed by the standard to be 1.
- **Arrays:** When applied to a statically sized [[Array_C]] name (not a pointer resulting from [[Array_Decay_C]]), `sizeof` returns the total size of the entire array in bytes (number of elements * size of one element).
- **Pointers:** When applied to a [[Pointer_C]] variable, `sizeof` returns the size of the pointer variable itself (e.g., 4 or 8 bytes), *not* the size of the data it points to.
- **Structs:** Returns the total size of the structure, including any padding bytes added by the compiler for alignment purposes.

## Examples / Use Cases

```c
#include <stdio.h>
#include <stddef.h> // For size_t

struct Data {
    int id;     // 4 bytes (typical)
    char code;  // 1 byte
    // Padding might be added here by compiler (e.g., 3 bytes)
    double value; // 8 bytes (typical)
}; // Total size might be 16 bytes due to padding

int main() {
    int i;
    double d;
    char c;
    int array[10];
    int *ptr = array;
    struct Data my_data;
    int x = 5;

    // Size of types
    printf("sizeof(char)   = %zu\n", sizeof(char));     // Output: 1
    printf("sizeof(int)    = %zu\n", sizeof(int));      // Output: 4 (typical)
    printf("sizeof(double) = %zu\n", sizeof(double));   // Output: 8 (typical)
    printf("sizeof(struct Data) = %zu\n", sizeof(struct Data)); // Output: 16 (typical, includes padding)

    // Size of variables (based on their type)
    printf("sizeof(i)      = %zu\n", sizeof(i));        // Output: 4 (same as sizeof(int))
    printf("sizeof(d)      = %zu\n", sizeof(d));        // Output: 8 (same as sizeof(double))
    printf("sizeof(c)      = %zu\n", sizeof(c));        // Output: 1 (same as sizeof(char))
    printf("sizeof(my_data)= %zu\n", sizeof(my_data));  // Output: 16 (same as sizeof(struct Data))

    // Size of array vs. pointer
    printf("sizeof(array)  = %zu\n", sizeof(array));    // Output: 40 (10 * sizeof(int))
    printf("sizeof(ptr)    = %zu\n", sizeof(ptr));      // Output: 4 or 8 (size of a pointer)

    // Sizeof expression (expression is NOT evaluated)
    printf("sizeof(x + 1.0) = %zu\n", sizeof(x + 1.0)); // Output: 8 (result type is double)
    printf("Value of x remains: %d\n", x); // Output: 5 (x++ not executed if used in sizeof(x++))

    // Calculating array element count
    size_t element_count = sizeof(array) / sizeof(array[0]);
    printf("Number of elements in array: %zu\n", element_count); // Output: 10

    return 0;
}
```

## Related Concepts
- [[Operator_C]] (`sizeof` is an operator)
- [[Data_Types_C]], [[Array_C]], [[struct_C]], [[Pointer_C]] (Operands for `sizeof`)
- [[bytes]] (The unit of the result)
- `size_t` (The type of the result)
- [[50_Data_Structures/Memory_Management]], [[Dynamic_Allocation_C]] (Used to calculate memory sizes for `malloc`, etc.)
- [[Array_Decay_C]] (Why `sizeof` behaves differently for array names vs. pointers derived from them)
- Compile-Time Evaluation

## Questions / Further Study
>[!question] Given `void foo(int a[], int size)` and `int arr[10]; foo(arr, 10);`, what is `sizeof(arr)` vs `sizeof(a)`? Why? (WS4)
> - **`sizeof(arr)`** (inside `main`): `arr` is declared as an array of 10 integers. When `sizeof` is applied directly to the array name *where its size is known* (i.e., in `main`), it returns the total size of the array in bytes. If `sizeof(int)` is 4, then `sizeof(arr)` will be **40** (10 elements * 4 bytes/element).
> - **`sizeof(a)`** (inside `foo`): When an array is passed to a function in C, it undergoes [[Array_Decay_C|array decay]]. The parameter `int a[]` is treated by the compiler exactly as if it were declared `int *a`. Therefore, inside the function `foo`, `a` is a **pointer** to an integer, not an array. `sizeof(a)` will return the size of a pointer variable on that specific architecture (e.g., **4** or **8** bytes), *not* the size of the original array passed from `main`.
> - **Why:** C passes arrays to functions by passing a pointer to their first element (effectively [[Pass_by_Address_C]]). The function loses the original array size information unless it's passed explicitly as another argument (like the `size` parameter in `foo`). `sizeof` inside the function operates on the local pointer parameter `a`.

---
**Source:** Worksheet C_WS4