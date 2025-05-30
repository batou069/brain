---
tags:
  - networking
  - concept
  - protocol
  - application_layer
  - infrastructure
aliases:
  - Domain Name System
related:
  - "[[ip]]"
  - "[[URL]]"
  - "[[Domain_Name]]" # Placeholder
  - "[[UDP]]" # Primarily uses UDP
  - "[[TCP]]" # Used for large responses/zone transfers
  - "[[Client_Server_Model]]"
  - "[[Name_Resolution]]" # Placeholder
  - "[[DNS_Record_Types]]" # Placeholder (A, AAAA, CNAME, MX, NS, etc.)
  - "[[Recursive_Resolver]]" # Placeholder
  - "[[Authoritative_Name_Server]]" # Placeholder
worksheet: [WS26]
date_created: 2025-04-21
---
# DNS (Domain Name System)

## Definition

The **Domain Name System (DNS)** is a hierarchical and distributed naming system for computers, services, or other resources connected to the Internet or a private network. It primarily translates human-readable **[[Domain_Name|domain names]]** (like `www.google.com`) into the numerical **[[ip|IP addresses]]** (like `142.250.180.36`) needed for locating and identifying computer services and devices worldwide. DNS also provides other information, such as mail server listings ([[DNS_Record_Types|MX records]]).

## Purpose

- **[[Name_Resolution]]:** The primary function is to resolve domain names into IP addresses (both [[IP_Address_v4|IPv4]] and [[IP_Address_v6|IPv6]]). Humans remember names; computers communicate using IP addresses. DNS bridges this gap.
- **Service Discovery:** Can provide information about available services for a domain (e.g., mail servers via MX records, service discovery via SRV records).
- **Distributed Database:** DNS information is stored across a global hierarchy of authoritative name servers, making the system robust and scalable. No single server holds all information.

## How it Works (Simplified Query Flow)

1.  **User Request:** A user types `www.example.com` into a browser. The browser/OS needs the IP address.
2.  **Local Check:** The OS checks its local cache and `hosts` file first.
3.  **Recursive Resolver Query:** If not found locally, the OS queries its configured **[[Recursive_Resolver]]** (usually provided by the ISP or a public service like Google DNS `8.8.8.8` or Cloudflare `1.1.1.1`).
4.  **Recursive Resolution Process:**
    a.  The Recursive Resolver queries one of the **Root Name Servers** (`.`) to find the authoritative server for the top-level domain (TLD), `.com`.
    b.  The Root Server responds with the address(es) of the `.com` TLD name servers.
    c.  The Recursive Resolver queries a `.com` TLD server for `example.com`.
    d.  The `.com` TLD server responds with the address(es) of the **[[Authoritative_Name_Server|Authoritative Name Server(s)]]** responsible for the `example.com` zone.
    e.  The Recursive Resolver queries the `example.com` Authoritative Name Server for the specific record for `www.example.com` (typically an [[DNS_Record_Types|A record]] for IPv4 or [[DNS_Record_Types|AAAA record]] for IPv6).
    f.  The Authoritative Name Server responds with the IP address(es) associated with `www.example.com`.
5.  **Caching:** The Recursive Resolver caches the result (according to its Time-To-Live or TTL value) and returns the IP address to the user's OS.
6.  **Connection:** The user's browser can now initiate a [[TCP]] connection to the obtained IP address (usually on port 80 or 443).

## Key Aspects

- **Hierarchical Structure:** Domain names form a tree structure (root -> TLD -> domain -> subdomain).
- **Distributed:** Authority and data are delegated down the hierarchy.
- **[[UDP]] Preference:** DNS queries primarily use [[UDP]] on [[Port_(Networking)|port 53]] for speed and efficiency. [[TCP]] is used for larger responses (historically > 512 bytes, now often larger via EDNS) or for zone transfers between servers.
- **Record Types:** Stores various types of resource records ([[DNS_Record_Types]]), including A (IPv4), AAAA (IPv6), CNAME (alias), MX (mail exchange), NS (name server), TXT (text), SRV (service locator), etc.
- **Caching:** Heavily relies on caching at multiple levels (OS, recursive resolver) to reduce load and improve speed.

## Related Concepts
- [[ip]], [[IP_Address_v4]], [[IP_Address_v6]]
- [[Domain_Name]], [[URL]]
- [[Name_Resolution]]
- [[UDP]], [[TCP]], [[Port_(Networking)]] (Port 53)
- [[Client_Server_Model]] (Resolvers are clients, Name Servers are servers)
- [[Recursive_Resolver]], [[Authoritative_Name_Server]], Root Servers
- [[DNS_Record_Types]] (A, AAAA, MX, CNAME, NS, etc.)
- Caching, Time-To-Live (TTL)

---
**Source:** Worksheet WS26