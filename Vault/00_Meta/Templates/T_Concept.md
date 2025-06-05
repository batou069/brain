---
tags: [<% tp.file.folder(true).toLowerCase().replaceAll(' ', '_') %>, concept]
aliases: []
related: []
worksheet: [WS<% tp.file.cursor(1) %>]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# <% tp.file.title %>

## Definition

<% tp.file.cursor(2) %>

## Key Aspects / Characteristics

- Aspect 1
- Aspect 2

## Examples / Use Cases

- Example 1
- Example 2

## Related Concepts
<% tp.file.cursor(3) %>
- [[Link 1]]
- [[Link 2]]

## Diagrams (Optional)
<% tp.file.cursor(4) %>

```puml
@startuml
' PlantUML diagram here
@enduml
```

## Questions / Further Study

> [!question] Question Title  
> Answer or discussion point.
> 
> - Follow-up task related to this concept @today
>     

---

**Source:** Worksheet <% tp.file.cursor(5) %>