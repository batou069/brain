---
tags:
  - version_control
  - git
  - concept
  - cryptography
  - hashing
aliases:
  - SHA-1 Hash
  - Secure Hash Algorithm 1
related:
  - "[[Git]]"
  - "[[Commit_object]]"
  - "[[Tree_Object]]"
  - "[[Blob_Object]]"
  - "[[Repository]]"
  - "[[Hashing]]"
  - "[[Cryptographic_Hash_Function]]"
  - "[[Data_Integrity]]"
worksheet:
  - WS2
date_created: 2025-04-20
---
# SHA-1 Hashing in Git

## Definition

**SHA-1 (Secure Hash Algorithm 1)** is a [[Cryptographic_Hash_Function|cryptographic hash function]] that takes an input and produces a 160-bit (20-byte) hash value, typically rendered as a 40-digit hexadecimal number. **Git uses SHA-1 extensively** to generate unique identifiers (hashes) for every object stored in its database: [[Blob_Object|blobs]] (file content), [[Tree_Object|trees]] (directory structure), [[Commit_object|commits]], and tags.

## Role in Git

- **Unique Object Identification:** Every object in the Git repository (commit, tree, blob) is identified by its unique SHA-1 hash. This hash is calculated based on the object's content plus a small header (identifying the object type and size).
- **Content-Addressable Storage:** Git essentially acts as a content-addressable filesystem. The SHA-1 hash serves as the "address" or key for retrieving an object. If two files have the exact same content, they will be stored only once as a single blob object with the same SHA-1 hash.
- **Data Integrity:** Because the hash depends on the content, any accidental or malicious corruption of a Git object (e.g., due to disk errors or tampering) will change its content and therefore its SHA-1 hash. When Git retrieves an object, it re-calculates the hash and compares it to the expected hash (used as its identifier/filename). If they don't match, Git knows the object is corrupt. This ensures the integrity of the entire project history.
- **Commit IDs:** The 40-character hexadecimal strings you see in `git log` (e.g., `a1b2c3d4e5f6...`) are the SHA-1 hashes identifying specific [[Commit_object|commit objects]].
- **Relationships:** Commit objects contain the SHA-1 hashes of the tree object representing the project snapshot and the SHA-1 hashes of their parent commit(s), forming the linked history graph. Tree objects contain hashes of the blobs and other trees they reference.

## SHA-1 Security Concerns (and Git's Mitigation)

- While SHA-1 is known to be cryptographically weakened regarding **collision resistance** (finding two *different* inputs that produce the same hash), this is generally **not considered a practical threat** for Git's usage model.
- Exploiting SHA-1 collisions to maliciously tamper with a Git repository in a meaningful way is extremely difficult and highly unlikely in practice.
- Git is transitioning towards SHA-256 for future-proofing, but SHA-1 remains the standard identifier for existing repositories and objects.

## Related Concepts
- [[Git]] (Uses SHA-1 fundamentally)
- [[Commit_object]], [[Tree_Object]], [[Blob_Object]] (Objects identified by SHA-1)
- [[Repository]] (Git's object database uses SHA-1)
- [[Hashing]], [[Cryptographic_Hash_Function]]
- [[Data_Integrity]] (Ensured by SHA-1 checks)

---
**Source:** Worksheet WS2 (Implied), Git Documentation