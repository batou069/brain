---
tags: [<% tp.file.folder(true).toLowerCase().replaceAll(' ', '_') %>, command]
aliases: []
related: []
worksheet: [WS<% tp.file.cursor(1) %>]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# ` <% tp.file.title %> `

## Purpose

<% tp.file.cursor(2) %>

## Syntax

```bash
<% tp.file.title %> [OPTIONS] [ARGUMENTS]
````
# <% tp.file.title %> MOC (Map of Content)

This note serves as a central hub for all topics related to **<% tp.file.title %>**.

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
````
## Common Options

| Option | Description    |
| ------ | -------------- |
| -o     | Example option |

## Examples

**Example 1: Basic Usage**

 `<% tp.file.title %> example_argument`

Explanation of the example.

**Example 2: Usage with Option**

      `<% tp.file.title %> -o example_argument`
    
Explanation of the example.

## Related Commands/Concepts
```

<% tp.file.cursor(3) %>

- [[Command 1]]
    
- [[Concept 1]]
    

## Notes

> [!note] Important Note  
> Something to remember about this command.

---

**Source:** Worksheet <% tp.file.cursor(4) %>