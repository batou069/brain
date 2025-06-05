---
tags: [c, concept, syntax, declaration, type_system, function, struct]
aliases: [C Forward Declaration]
related:
  - "[[Declaration_C]]"
  - "[[Definition_C]]"
  - "[[Function_Declaration_C]]"
  - "[[struct_C]]"
  - "[[Header_file_C]]"
  - "[[Compiler_C]]"
  - "[[Linker_C]]"
  - "[[Opaque_Pointer_C]]"
worksheet: [C_WS3]
date_created: 2025-04-11
---
# Forward Declaration (C)

## Definition

A **Forward Declaration** in C is a [[Declaration_C]] of an identifier (typically a function, struct, union, or enum) *before* its full [[Definition_C]] is encountered by the compiler. It informs the compiler about the existence and basic properties (like name and type category, or function signature) of the identifier, allowing it to be used (e.g., in function calls, pointer declarations) before it is completely defined.

## Key Aspects / Characteristics

- **Declare Before Define:** Allows using an identifier before its full definition appears later in the same file or in a different file.
- **Functions:** For functions, a forward declaration is simply a [[Function_Declaration_C|function prototype]].
- **Structs/Unions/Enums:** For aggregate types, a forward declaration introduces the type name but not its members. This creates an *incomplete type*.
    - Syntax: `struct TagName;`, `union TagName;`, `enum TagName;`
- **Incomplete Types:** You can declare pointers to incomplete types (`struct TagName *ptr;`), use them as function parameter types, or function return types. However, you cannot declare variables *of* the incomplete type (as the compiler doesn't know its size) or access its members until the full definition is visible.
- **Breaking Dependencies:** Useful for resolving circular dependencies between data structures or functions defined across different files or within the same file.
- **Header Files:** Function prototypes in header files are a common form of forward declaration. Forward declarations of structs are sometimes used in headers to avoid including another header just to declare a pointer (using [[Opaque_Pointer_C|opaque pointers]]).

## Examples / Use Cases

**1. Forward Declaration of a Function:**
```c
#include <stdio.h>

// Forward declaration (prototype)
void function_b(int);
void function_a(int);

// Definition of function_a (calls function_b)
void function_a(int x) {
    printf("In function_a, x = %d\n", x);
    if (x > 0) {
        function_b(x - 1); // Call is valid due to forward declaration
    }
}

// Definition of function_b (calls function_a)
void function_b(int y) {
    printf("In function_b, y = %d\n", y);
     if (y > 1) {
        function_a(y / 2); // Call is valid (definition or prototype seen before)
    }
}

int main() {
    function_a(5);
    return 0;
}
```

**2. Forward Declaration of Structs (Circular Dependency):**
```c
#include <stdio.h>

// Forward declarations
struct B; // Declare struct B before defining struct A

struct A {
    int data_a;
    struct B *ptr_b; // Pointer to B is okay with forward declaration
};

struct B {
    int data_b;
    struct A *ptr_a; // Pointer to A is okay (A is now defined)
};

int main() {
    struct A instance_a;
    struct B instance_b;

    instance_a.data_a = 10;
    instance_a.ptr_b = &instance_b;

    instance_b.data_b = 20;
    instance_b.ptr_a = &instance_a;

    printf("A points to B's data: %d\n", instance_a.ptr_b->data_b);
    printf("B points to A's data: %d\n", instance_b.ptr_a->data_a);

    // struct B incomplete_b; // ERROR: Cannot declare variable of incomplete type B here
                              // if struct B definition wasn't visible yet.

    return 0;
}
```

## Related Concepts
- [[Declaration_C]], [[Definition_C]] (Forward declaration is a specific type of declaration)
- [[Function_Declaration_C]] (Forward declaration for functions)
- [[struct_C]], [[union_C]], [[enum_C]] (Can be forward-declared)
- [[Incomplete_Type_C]] (Result of forward-declaring structs/unions/enums - *to be created*)
- [[Pointer_C]] (Can be declared to incomplete types)
- [[Header_file_C]] (Common place for forward declarations)
- [[Opaque_Pointer_C]] (Design pattern relying on forward declarations)

---
**Source:** Worksheet C_WS3