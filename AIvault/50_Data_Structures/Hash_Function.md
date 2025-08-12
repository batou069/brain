---
tags:
  - data_structures
  - concept
  - algorithms
  - hashing
aliases:
  - Hashing Function
related:
  - Hash_Table_DS
  - Cryptographic_Hash_Function
  - Checksum
  - Collision_Resolution
  - Modulo_Arithmetic
worksheet:
  - WS7
date_created: 2025-04-14
---
# Hash Function

## Definition

A **Hash Function** is any function that can be used to map data of arbitrary size (the **key**) to fixed-size values (the **hash value**, hash code, digest, or simply hash). In the context of [[Hash_Table_DS|Hash Tables]], the hash function is used to compute an index into the bucket array where the corresponding value should be stored or searched for.

## Key Properties (for Hash Tables)

A good hash function for use in hash tables should ideally have the following properties:

1.  **Deterministic:** The same key must always produce the same hash value.
2.  **Efficiently Computable:** Calculating the hash should be fast (ideally close to [[O_1]] time relative to key size).
3.  **Uniform Distribution:** Should distribute keys as evenly as possible across the available hash table indices (buckets). This minimizes collisions ([[Collision_Resolution]]) and maintains the hash table's average [[O_1]] performance. Poor distribution leads to clustering and degrades performance towards [[O_n]].
4.  **Avalanche Effect (Desirable):** A small change in the input key should ideally result in a large, unpredictable change in the hash value, further helping with uniform distribution.

## Mapping to Index

The raw hash value produced by the hash function (which might be a large integer) needs to be mapped to a valid index within the hash table's array bounds (typically `0` to `capacity - 1`). A common method is using the **modulo operator**:
`index = hash(key) % capacity`
Using a prime number for the `capacity` often helps improve distribution when using the modulo method.

## Examples of Hashing Techniques (Conceptual)

- **For Integers:**
    - Modulo: `hash(key) = key % capacity` (Simple, but can be poor if keys have patterns related to capacity).
    - Multiplication Method: `hash(key) = floor(capacity * (key * A mod 1))` where A is a constant (e.g., golden ratio conjugate).
- **For Strings:**
    - Summation: Add ASCII values of characters (Poor distribution).
    - Polynomial Hashing: Treat string as coefficients of a polynomial and evaluate at a specific point `x`, taking modulo capacity (e.g., `hash = (c1*x^k + c2*x^(k-1) + ... + ck) % capacity`). Horner's method is efficient for calculation. Common and generally good.
    - Folding: Divide key into parts, combine parts (e.g., add them).
- **Other Data Types:** Hashing functions can be designed for various data types (structs, objects) by combining the hashes of their constituent parts.

## Cryptographic vs. Non-Cryptographic

- **Hash Table Hash Functions:** Prioritize speed and good distribution. They do **not** need to be cryptographically secure (i.e., resistant to preimage attacks or collision attacks).
- **[[Cryptographic_Hash_Function|Cryptographic Hash Functions]]** (e.g., SHA-256, MD5 - though MD5 is broken): Designed for security applications. They are computationally infeasible to invert (find key from hash) or to find two different keys that produce the same hash (collision resistance). They are generally much slower than hash functions used for hash tables.

## Related Concepts
- [[Hash_Table_DS]] (Hash functions are essential for hash tables)
- [[Collision_Resolution]] (Needed because hash functions aren't perfect one-to-one mappings)
- [[Cryptographic_Hash_Function]] (Different purpose, security focus)
- [[Checksum]] (Simpler functions often used just for error detection)
- Modulo Arithmetic

---
**Source:** Worksheet WS7