---
tags:
  - windows
  - filesystem
  - concept
  - storage
  - networking
  - protocol
  - distributed_filesystem
aliases:
  - New Technology File System
  - Network File System
related:
  - "[[File_System]]"
  - "[[FAT-16_FAT-32]]"
  - "[[exFAT]]"
  - "[[Journaling]]"
  - "[[Access_Control_List]]"
  - "[[Compression]]"
  - "[[Encryption]]"
  - "[[Windows_OS]]"
  - "[[Client_Server_Model]]"
  - "[[RPC]]"
  - "[[Mounting]]"
  - "[[Distributed_File_System]]"
  - "[[Samba]]"
worksheet:
  - WS1
date_created: 2025-04-20
---
# NTFS (New Technology File System)

## Definition

**NTFS (New Technology File System)** is the standard, proprietary [[Journaling|journaling]] [[File_System]] developed by Microsoft for its Windows NT family of operating systems (including Windows XP, Vista, 7, 8, 10, 11, Windows Server versions). It superseded the older [[FAT-16_FAT-32|FAT]] file system.

## Key Features

- **[[Journaling]]:** Improves reliability and speeds up recovery after system crashes by keeping a log (journal) of changes before they are fully committed to the disk.
- **Large File and Volume Sizes:** Supports very large files (theoretically up to 16 EiB, practically limited by OS) and large volume sizes (up to 256 TiB typically). Overcomes the limitations of FAT32.
- **[[Access_Control_List|Access Control Lists (ACLs)]] & Permissions:** Provides robust, fine-grained security control by allowing permissions (read, write, execute, etc.) to be set for individual users and groups on files and directories.
- **File [[Compression]]:** Supports built-in, transparent compression of files and folders to save disk space.
- **[[Encryption]] (EFS):** Supports Encrypting File System (EFS) for transparent encryption of files at the filesystem level, tied to user accounts.
- **Hard Links & [[Symbolic_link|Symbolic Links]]:** Supports both [[Hard_link|hard links]] (multiple directory entries for the same file) and symbolic links (pointers to other files/directories, including across volumes). Also supports Junction Points.
- **Sparse Files:** Allows efficient storage for files that contain large sections of zeros.
- **Disk Quotas:** Allows administrators to limit the amount of disk space users can consume.
- **Alternate Data Streams (ADS):** Allows storing multiple "streams" of data associated with a single file name (used by some applications, but can also hide data).
- **Self-Healing (Partial):** Includes features to detect and repair certain types of disk corruption automatically (e.g., sector sparing).

## Usage

- The default filesystem for system drives and most internal hard drives/SSDs on modern Windows systems.
- Often used for external drives formatted on Windows, although [[exFAT]] is sometimes preferred for better cross-platform compatibility (especially with macOS) and simplicity.
- Linux and macOS have varying degrees of support for reading and writing NTFS partitions (reading is generally stable, writing often relies on drivers like `ntfs-3g` via FUSE and might be slower or lack full feature support).

## Related Concepts
- [[File_System]]
- [[FAT-16_FAT-32]], [[exFAT]] (Other Microsoft filesystems)
- [[Journaling]] (Reliability feature)
- [[Access_Control_List]] (Security feature)
- [[Compression]], [[Encryption]] (Built-in features)
- [[Hard_link]], [[Symbolic_link]]
- [[Windows_OS]] (Primary operating system using NTFS)

---
**Source:** Worksheet WS1

# NFS (Network File System)

## Definition

**NFS (Network File System)** is a **[[Distributed_File_System]]** protocol originally developed by Sun Microsystems (now Oracle) that allows a user on a client computer to access files over a computer network much like local storage is accessed. It enables sharing of directories and files between computers (typically Unix-like systems) on a network.

## Key Aspects / Characteristics

- **[[Client_Server_Model|Client-Server Architecture]]:**
    - **NFS Server:** Exports (makes available) local directories to specific clients or networks.
    - **NFS Client:** Mounts the exported directories from the server onto a local mount point in its own filesystem hierarchy.
- **Transparency:** Once mounted, the remote filesystem appears to users and applications on the client machine largely as if it were a local filesystem (though performance and semantics might differ slightly). Users can navigate, read, write, and manage files on the NFS mount using standard commands (`ls`, `cd`, `cp`, `mv`, `rm`, etc.).
- **[[RPC|Remote Procedure Call (RPC)]]:** NFS typically relies on RPC mechanisms (like ONC RPC) to handle communication between the client and server for file operations.
- **Stateless (Historically):** Early versions of NFS (v2) were largely stateless (server didn't keep track of which clients had which files open), relying on the client to maintain state. Later versions (v3, v4) introduced more stateful features for better performance and consistency (e.g., locking, caching improvements).
- **Versions:** Several versions exist (NFSv2, NFSv3, NFSv4, NFSv4.1, NFSv4.2), each adding features like improved performance, better security, support for locking, statefulness, and parallel access (pNFS). NFSv4 is significantly different and more stateful than v3.
- **Authentication/Security:** Traditionally relied on client IP address/hostname verification and user ID mapping (UID/GID), which could be insecure. NFSv4 introduced stronger security mechanisms like Kerberos and LIPKEY using RPCSEC GSS.
- **Platform:** Primarily used between Unix-like systems (Linux, Solaris, macOS, BSD), although clients/servers exist for other platforms like Windows.

## Use Cases

- Centralized home directories for users accessible from multiple workstations.
- Shared software repositories or build directories accessible by multiple servers.
- Providing access to large datasets stored on a central server from compute clients.
- Simple network file sharing in Unix/Linux environments.

## Related Concepts
- [[File_System]], [[Distributed_File_System]]
- [[Client_Server_Model]]
- [[RPC]] (Remote Procedure Call)
- [[Mounting]] (How clients access NFS shares)
- [[Samba]] (Provides similar functionality using the SMB/CIFS protocol, common for Windows interoperability)
- User ID Mapping, Kerberos (Authentication/Security)

---
**Source:** Worksheet WS1

# NFS (Network File System)

## Definition

**NFS (Network File System)** is a **[[Distributed_File_System]]** protocol originally developed by Sun Microsystems (now Oracle) that allows a user on a client computer to access files over a computer network much like local storage is accessed. It enables sharing of directories and files between computers (typically Unix-like systems) on a network.

## Key Aspects / Characteristics

- **[[Client_Server_Model|Client-Server Architecture]]:**
    - **NFS Server:** Exports (makes available) local directories to specific clients or networks.
    - **NFS Client:** Mounts the exported directories from the server onto a local mount point in its own filesystem hierarchy.
- **Transparency:** Once mounted, the remote filesystem appears to users and applications on the client machine largely as if it were a local filesystem (though performance and semantics might differ slightly). Users can navigate, read, write, and manage files on the NFS mount using standard commands (`ls`, `cd`, `cp`, `mv`, `rm`, etc.).
- **[[RPC|Remote Procedure Call (RPC)]]:** NFS typically relies on RPC mechanisms (like ONC RPC) to handle communication between the client and server for file operations.
- **Stateless (Historically):** Early versions of NFS (v2) were largely stateless (server didn't keep track of which clients had which files open), relying on the client to maintain state. Later versions (v3, v4) introduced more stateful features for better performance and consistency (e.g., locking, caching improvements).
- **Versions:** Several versions exist (NFSv2, NFSv3, NFSv4, NFSv4.1, NFSv4.2), each adding features like improved performance, better security, support for locking, statefulness, and parallel access (pNFS). NFSv4 is significantly different and more stateful than v3.
- **Authentication/Security:** Traditionally relied on client IP address/hostname verification and user ID mapping (UID/GID), which could be insecure. NFSv4 introduced stronger security mechanisms like Kerberos and LIPKEY using RPCSEC GSS.
- **Platform:** Primarily used between Unix-like systems (Linux, Solaris, macOS, BSD), although clients/servers exist for other platforms like Windows.

## Use Cases

- Centralized home directories for users accessible from multiple workstations.
- Shared software repositories or build directories accessible by multiple servers.
- Providing access to large datasets stored on a central server from compute clients.
- Simple network file sharing in Unix/Linux environments.

## Related Concepts
- [[File_System]], [[Distributed_File_System]]
- [[Client_Server_Model]]
- [[RPC]] (Remote Procedure Call)
- [[Mounting]] (How clients access NFS shares)
- [[Samba]] (Provides similar functionality using the SMB/CIFS protocol, common for Windows interoperability)
- User ID Mapping, Kerberos (Authentication/Security)

---
**Source:** Worksheet WS1