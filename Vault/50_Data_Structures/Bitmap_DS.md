---
tags:
  - data_structures
  - concept
  - basic
  - memory
  - bit_manipulation
aliases:
  - Bit Array
  - Bit Vector
  - Bitset
  - Bitstring
related:
  - "[[Data_Structure]]"
  - "[[Array_C]]"
  - "[[bits]]"
  - "[[Bitwise_Operator_C]]"
  - "[[50_Data_Structures/Memory_Management]]"
  - "[[Set_ADT]]"
worksheet:
  - WS7
date_created: 2025-04-12
---
# Bitmap (Bit Array)

## Definition

A **Bitmap** (also known as a **Bit Array**, Bit Vector, Bitset, or Bitstring) is a [[Data_Structure]] that stores individual [[bits]] compactly, typically using an [[Array_C]] of integers (like `unsigned char` or `unsigned int`) where each bit within those integers represents a single boolean value (0 or 1, false or true) or the state of an item.

## Key Aspects / Characteristics

- **Space Efficiency:** Very memory-efficient for storing a large number of boolean flags or representing the presence/absence of items from a dense range, as each item takes only one bit of storage (plus some overhead for the array structure).
- **Implementation:** Usually implemented using an array of unsigned integers (e.g., `unsigned char[]`, `unsigned int[]`, `uint64_t[]`).
- **Bit Manipulation:** Accessing or modifying individual bits requires using [[Bitwise_Operator_C|bitwise operators]]:
    - **Setting a bit:** `array[index / BITS_PER_UNIT] |= (1 << (index % BITS_PER_UNIT));`
    - **Clearing a bit:** `array[index / BITS_PER_UNIT] &= ~(1 << (index % BITS_PER_UNIT));`
    - **Checking a bit:** `(array[index / BITS_PER_UNIT] >> (index % BITS_PER_UNIT)) & 1;`
    (Where `BITS_PER_UNIT` is 8 for `unsigned char`, 32 for `unsigned int`, etc.)
- **Mapping:** An index `k` typically corresponds to the `(k % BITS_PER_UNIT)`-th bit within the `(k / BITS_PER_UNIT)`-th element of the underlying integer array.
- **Use Cases:**
    - Representing sets of integers from a fixed range (e.g., tracking allocated resource IDs).
    - Boolean flags in operating systems or databases (e.g., free block list in file systems).
    - Bloom filters (probabilistic data structure).
    - Simple compression techniques.
    - Representing monochrome images (where each bit is a pixel).

## Visualization (Conceptual)

Mapping index `k` to a bit in an array of `unsigned char` (8 bits per unit):

Index `k`: 0 1 2 3 4 5 6 7 | 8 9 10 11 12 13 14 15 | 16 ...
Array `arr`:
Element `arr[0]` (Byte 0): `| | | | | | | |` (Bits 0-7)
Element `arr[1]` (Byte 1): `| | | | | | | |` (Bits 8-15)
Element `arr[2]` (Byte 2): `| | | | | | | |` (Bits 16-23)
...

- To access index `k=11`:
    - Array index = `11 / 8 = 1` -> `arr[1]`
    - Bit index within byte = `11 % 8 = 3` -> 3rd bit (from right, 0-indexed) of `arr[1]`

## Example (Conceptual C)

```C
#include <stdio.h>
#include <limits.h> // For CHAR_BIT

#define BITMAP_SIZE 100 // We want to represent numbers 0-99

// Calculate array size needed (using unsigned char)
#define ARRAY_SIZE ((BITMAP_SIZE + CHAR_BIT - 1) / CHAR_BIT)

unsigned char bitmap[ARRAY_SIZE] = {0}; // Initialize all bits to 0

// Set bit k
void set_bit(int k) {
    if (k < 0 || k >= BITMAP_SIZE) return; // Bounds check
    bitmap[k / CHAR_BIT] |= (1 << (k % CHAR_BIT));
}

// Clear bit k
void clear_bit(int k) {
    if (k < 0 || k >= BITMAP_SIZE) return;
    bitmap[k / CHAR_BIT] &= ~(1 << (k % CHAR_BIT));
}

// Test bit k (returns 1 if set, 0 if not)
int test_bit(int k) {
    if (k < 0 || k >= BITMAP_SIZE) return 0;
    return (bitmap[k / CHAR_BIT] >> (k % CHAR_BIT)) & 1;
}

int main() {
    set_bit(5);
    set_bit(10);
    set_bit(0);
    set_bit(15);

    printf("Is bit 5 set? %d\n", test_bit(5));   // Output: 1
    printf("Is bit 6 set? %d\n", test_bit(6));   // Output: 0
    printf("Is bit 10 set? %d\n", test_bit(10)); // Output: 1

    clear_bit(10);
    printf("Is bit 10 set after clear? %d\n", test_bit(10)); // Output: 0

    return 0;
}
```

## Related Concepts
- [[Data_Structure]], [[Array_C]] (Underlying storage)
- [[bits]], [[Bitwise_Operator_C]] (Core mechanism for access)
- [[50_Data_Structures/Memory_Management]] (Bitmaps offer space efficiency)
- [[Set_ADT]] (Can be implemented using bitmaps for dense integer sets)

---
**Source:** Worksheet WS7