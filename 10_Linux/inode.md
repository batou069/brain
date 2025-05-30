---
tags:
  - 10_linux
  - concept
  - storage
  - filesystem
aliases:
  - Index Node
related:
  - "[[File_System]]"
  - "[[File]]"
  - "[[Directory]]"
  - "[[Metadata]]"
  - "[[Hard_link]]"
  - "[[Symbolic_link]]"
  - "[[ext2]]"
  - "[[ext3]]"
  - "[[ext4]]"
  - "[[BTRFS]]"
  - "[[JFS]]"
worksheet:
  - WS<% tp.file.cursor(1) %>
date_created: 2025-04-10
---
# inode

## Definition

An **inode** (index node) is a data structure used in many Unix-style [[File_System|file systems]] (like [[ext4]], [[BTRFS]], [[JFS]], HFS+, APFS) to store basic information (metadata) about a [[File]], [[Directory]], or other file system object, *except* for its name and actual data content.

## Key Aspects / Characteristics

- **Metadata Storage:** Each inode stores attributes like:
    - File type (regular file, directory, link, device file, etc.)
    - Owner (User ID, Group ID)
    - Permissions (read, write, execute)
    - Timestamps (creation, last access, last modification)
    - File size
    - Link count (number of [[Hard_link|hard links]] pointing to this inode)
    - Pointers to the actual data blocks on the storage device where the file's content resides.
- **Inode Number:** Each inode has a unique identification number within the file system.
- **Name Separation:** The filename(s) are stored in [[Directory]] entries, which map the name(s) to the corresponding inode number. This allows multiple names ([[Hard_link|hard links]]) to point to the same inode (and thus the same file data and metadata).
- **Fixed Number:** File systems are typically created with a fixed maximum number of inodes, which can limit the total number of files that can be created, regardless of available disk space.

## Examples / Use Cases

- When you access a file `/home/user/document.txt`, the file system:
    1. Looks up `/` (root directory inode).
    2. Reads the root directory data blocks to find the entry for `home`, getting its inode number.
    3. Reads the `home` inode.
    4. Reads the `home` directory data blocks to find the entry for `user`, getting its inode number.
    5. Reads the `user` inode.
    6. Reads the `user` directory data blocks to find the entry for `document.txt`, getting its inode number.
    7. Reads the `document.txt` inode to get permissions, size, and pointers to data blocks.
    8. Reads the actual data blocks based on the pointers in the inode.

## Related Concepts
- [[File_System]] (Inodes are a core part of many file systems)
- [[File]], [[Directory]] (Represented by inodes)
- [[Metadata]] (The information stored in the inode)
- [[Hard_link]] (Multiple directory entries pointing to the same inode)
- [[Symbolic_link]] (A special file *containing* a path, has its own inode)
- [[ext4]], [[BTRFS]], [[JFS]] (File systems that use inodes)
- Data Blocks (Where the actual file content is stored, pointed to by the inode)

## Questions / Further Study
>[!question] How do hard links relate to inodes?
> A [[Hard_link]] is essentially another directory entry that points to the *same* [[inode]] number as an existing file name. This means multiple file names can refer to the exact same file data and metadata. The inode itself contains a "link count" which tracks how many directory entries point to it. The file's data is only deleted when the link count drops to zero (meaning `rm` has been called on the last hard link).

---
**Source:** Worksheet WS1, WS12
