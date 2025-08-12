---
tags:
  - networking
  - concept
  - distinction
  - internet
  - web
aliases:
  - World Wide Web vs Internet
related:
  - "[[Internet]]" # Placeholder
  - "[[World_Wide_Web]]" # Placeholder
  - "[[HTTP]]"
  - "[[HTML]]"
  - "[[URL]]"
  - "[[Web_Browser]]" # Placeholder
  - "[[Web_Server]]" # Placeholder
  - "[[ip]]"
  - "[[TCP]]"
worksheet: [WS26]
date_created: 2025-04-21
---
# WWW vs. Internet Distinction

## Definition

While often used interchangeably in casual conversation, the **Internet** and the **World Wide Web (WWW or Web)** are distinct concepts:

-   **[[Internet]]:** Refers to the vast, global **network infrastructure** – the physical cables (fiber optics, copper), routers, switches, servers, satellites, and the communication protocols ([[TCP_IP_Model|TCP/IP suite]] - [[ip]], [[TCP]], [[UDP]], etc.) that connect billions of computing devices worldwide, allowing them to exchange data. It's the underlying hardware and core networking protocols.

-   **[[World_Wide_Web|World Wide Web (WWW or Web)]]:** Refers to one specific, very popular **information system/service that runs *on top of* the Internet**. The Web consists of interconnected documents (web pages) and other resources, linked by hyperlinks and [[URL|URLs (Uniform Resource Locators)]], accessed primarily using the [[HTTP|Hypertext Transfer Protocol (HTTP)]] or [[HTTPS|HTTPS]]. It relies on technologies like [[HTML]] (for structuring pages) and [[Web_Browser|web browsers]] (for accessing and displaying content).

## Analogy

Think of the Internet as the **global road system** (infrastructure, rules of the road like TCP/IP). The World Wide Web is like **one specific type of vehicle and service** using those roads (like delivery trucks carrying packages - web pages/resources - identified by specific addresses - URLs - using specific delivery protocols - HTTP).

Other services also use the Internet "roads" but are not part of the WWW, such as:
- Email ([[SMTP]], POP3, IMAP)
- File Transfer ([[FTP]])
- Secure Shell ([[SSH]])
- Online Gaming (often using custom protocols over UDP/TCP)
- Voice over IP ([[VoIP]])
- Internet Relay Chat (IRC)
- Peer-to-peer file sharing

## Summary Table

| Feature         | Internet                                   | World Wide Web (WWW)                       |
| :-------------- | :----------------------------------------- | :----------------------------------------- |
| **Nature**      | Global Network Infrastructure              | Information System / Service               |
| **Components**  | Hardware (routers, cables, servers), Core Protocols (TCP/IP) | Web Pages (HTML), Hyperlinks, URLs, HTTP, Web Servers, Web Browsers |
| **Relationship**| Web runs *on* the Internet                 | One application *using* the Internet       |
| **Scope**       | Broader (includes Web, Email, FTP, etc.) | Narrower (Hyperlinked documents via HTTP)  |
| **Primary Tech**| TCP/IP Suite                               | HTTP, HTML, URLs                           |

## Related Concepts
- [[Internet]], [[World_Wide_Web]]
- [[TCP_IP_Model]], [[ip]], [[TCP]], [[UDP]] (Internet protocols)
- [[HTTP]], [[HTTPS]], [[HTML]], [[URL]], [[Web_Browser]], [[Web_Server]] (Web technologies)
- Email, FTP, SSH (Other services using the Internet)

---
**Source:** Worksheet WS26