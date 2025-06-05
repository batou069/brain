---
tags: [MOC, <% tp.file.folder(true).toLowerCase().replaceAll(' ', '_') %>]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---

# <% tp.file.title %> MOC (Map of Content)

## Core Concepts
<% tp.file.cursor(1) %>
- [[Concept 1]]
- [[Concept 2]]

## Commands / Functions / Keywords
<% tp.file.cursor(2) %>
- [[Keyword 1]]
- [[Command 1]]
- [[Function 1]]

## Sub-Topics / Related Areas
<% tp.file.cursor(3) %>
- [[Sub-Topic MOC]]

## Notes in this Section

```dataview
LIST
FROM "<% tp.file.folder() %>"
WHERE file.folder = this.file.folder AND file.name != this.file.name AND !contains(file.name, "MOC")
SORT file.name ASC
```

