---
tags:
  - networking
  - concept
  - web
  - api
  - rest
  - architecture
aliases:
  - REST Resource
  - Resource (REST context)
related:
  - "[[RESTful_API]]"
  - "[[URL]]"
  - "[[HTTP]]"
  - "[[HTTP_Methods]]"
  - "[[Representation]]" # Placeholder
  - "[[Noun_Based_URI]]" # Placeholder
worksheet: [WS26]
date_created: 2025-04-21
---
# REST Resource

## Definition

In the context of **[[RESTful_API|REST (Representational State Transfer)]]**, a **Resource** is the fundamental abstraction of information or entity that can be addressed and manipulated. Anything that can be named and represented can be a resource: a document, an image, a collection of other resources (e.g., a list of users), a service, a user object, an order, etc.

## Key Aspects / Characteristics

- **Conceptual Entity:** A resource is a concept (e.g., "user number 123", "the collection of all current orders"), not necessarily a specific file or database record directly, although it often maps closely to one.
- **Identified by URI:** Every resource is uniquely identified by a [[URI]] (Uniform Resource Identifier), typically a [[URL]] in web-based REST APIs (e.g., `/users/123`, `/orders`, `/products?category=electronics`). These URIs act as the address of the resource.
- **[[Representation|Representations]]:** Clients interact with resources *indirectly* through their **representations**. A representation captures the current or intended state of a resource in a specific format ([[MIME_type]]), such as [[JSON]] or [[XML]]. A single resource can have multiple representations (e.g., a user resource might be representable as JSON or XML). The client can request a specific representation using [[HTTP_Headers|HTTP headers]] like `Accept`.
- **Manipulation via HTTP Methods:** Clients manipulate resources by sending [[HTTP_Request|HTTP requests]] to the resource's URI, using standard [[HTTP_Methods]] (verbs) to indicate the desired action on the resource (e.g., `GET` to retrieve a representation, `PUT` to update/replace the resource state, `DELETE` to remove the resource, `POST` to create a new resource within a collection resource or perform other actions).
- **Stateless Interaction:** Interactions with resources are [[Stateless_Protocol|stateless]]. Each request contains all necessary information.

## Example

- **Resource:** The user account with ID `45`.
- **URI:** `/api/users/45`
- **Representations:**
    - JSON: `{"id": 45, "name": "Bob", "email": "bob@example.com"}` (`Content-Type: application/json`)
    - XML: `<user><id>45</id><name>Bob</name><email>bob@example.com</email></user>` (`Content-Type: application/xml`)
- **Interactions:**
    - `GET /api/users/45`: Retrieve a representation of user 45.
    - `PUT /api/users/45` (with updated JSON in body): Replace the state of user 45.
    - `DELETE /api/users/45`: Delete user 45.

- **Resource:** The collection of all users.
- **URI:** `/api/users`
- **Interactions:**
    - `GET /api/users`: Retrieve a representation of the list of users.
    - `POST /api/users` (with new user JSON in body): Create a new user within the collection.

## Related Concepts
- [[RESTful_API]] (Resources are central to REST)
- [[URL]], [[URI]] (Resource identifiers)
- [[Representation]] (How resource state is exchanged)
- [[HTTP]], [[HTTP_Methods]] (Used to interact with resources)
- [[JSON]], [[XML]], [[MIME_type]] (Representation formats)
- [[Noun_Based_URI]] (URIs identify resources/nouns)

---
**Source:** Worksheet WS26, Roy Fielding's Dissertation