---
tags: [c, concept, design_pattern, behavioral]
aliases: [Chain of Responsibility Pattern]
related:
  - "[[Function_Pointer_C]]"
  - "[[struct_C]]"
  - "[[Pointer_C]]"
  - "[[Design_Patterns_C]]"
worksheet: [C_WS5]
date_created: 2025-04-12
---
# Chain of Responsibility Design Pattern (Conceptual C Implementation)

## Definition

The **Chain of Responsibility** is a behavioral design pattern that lets you pass requests along a chain of handlers. Upon receiving a request, each handler decides either to process the request or to pass it to the next handler in the chain. This avoids coupling the sender of a request to its receiver; multiple objects get a chance to handle the request.

## Key Aspects / Characteristics (Conceptual C Implementation)

- **Handler Interface:** Define a common way for handlers to process requests and potentially pass them on. In C, this often involves:
    - A `struct` representing the handler, possibly containing state and a pointer to the next handler.
    - A [[Function_Pointer_C|function pointer]] type for the handling function.
- **Concrete Handlers:** Implement specific handlers, each capable of handling certain types of requests. Each handler typically:
    - Checks if it can handle the incoming request.
    - If yes, processes the request (and potentially stops the chain).
    - If no, passes the request to the `next` handler in the chain (if one exists).
- **Chain Construction:** Link the handler objects together to form the chain (e.g., by setting the `next` pointer in each handler struct).
- **Client Interaction:** The client sends the request to the *first* handler in the chain, without needing to know which handler will ultimately process it.

## Conceptual C Example

```c
#include <stdio.h>
#include <stdlib.h>

// Forward declaration
typedef struct Handler Handler;

// Define the request type (can be more complex)
typedef struct {
    int type; // e.g., 1 for error, 2 for warning, 3 for info
    const char *message;
} Request;

// Define the handler function pointer type
typedef void (*HandleFunction)(Handler *self, const Request *req);

// Define the Handler structure
struct Handler {
    HandleFunction handle; // Function pointer to the handler logic
    Handler *next;         // Pointer to the next handler in the chain
    // Add any handler-specific state here if needed
};

// --- Concrete Handlers ---

// Handler 1: Handles errors (type 1)
void handleError(Handler *self, const Request *req) {
    if (req->type == 1) {
        printf("ERROR Handler: Processing message: %s\n", req->message);
        // Request handled, stop chain (or could optionally pass on)
    } else if (self->next != NULL) {
        // Pass to the next handler
        printf("ERROR Handler: Passing request type %d on.\n", req->type);
        self->next->handle(self->next, req);
    } else {
        printf("ERROR Handler: End of chain, request type %d unhandled.\n", req->type);
    }
}

// Handler 2: Handles warnings (type 2)
void handleWarning(Handler *self, const Request *req) {
    if (req->type == 2) {
        printf("WARNING Handler: Processing message: %s\n", req->message);
    } else if (self->next != NULL) {
        printf("WARNING Handler: Passing request type %d on.\n", req->type);
        self->next->handle(self->next, req);
    } else {
         printf("WARNING Handler: End of chain, request type %d unhandled.\n", req->type);
    }
}

// Handler 3: Handles info (type 3)
void handleInfo(Handler *self, const Request *req) {
    if (req->type == 3) {
        printf("INFO Handler: Processing message: %s\n", req->message);
    } else if (self->next != NULL) {
         printf("INFO Handler: Passing request type %d on.\n", req->type);
        self->next->handle(self->next, req);
    } else {
         printf("INFO Handler: End of chain, request type %d unhandled.\n", req->type);
    }
}


int main() {
    // Create handler instances (could use malloc for dynamic chains)
    Handler infoHandler = {handleInfo, NULL}; // Last in chain
    Handler warningHandler = {handleWarning, &infoHandler};
    Handler errorHandler = {handleError, &warningHandler}; // First in chain

    Handler *chain_start = &errorHandler;

    // Create some requests
    Request req1 = {1, "Critical system failure!"};
    Request req2 = {2, "Disk space low."};
    Request req3 = {3, "User logged in."};
    Request req4 = {4, "Unknown request."};

    // Send requests to the start of the chain
    printf("--- Sending Request 1 ---\n");
    chain_start->handle(chain_start, &req1);

    printf("\n--- Sending Request 2 ---\n");
    chain_start->handle(chain_start, &req2);

    printf("\n--- Sending Request 3 ---\n");
    chain_start->handle(chain_start, &req3);

    printf("\n--- Sending Request 4 ---\n");
    chain_start->handle(chain_start, &req4);

    return 0;
}
```

## Related Concepts
- [[Design_Patterns_C]] (Category of solution templates - *to be created*)
- [[Function_Pointer_C]] (Often used to implement the handler behavior)
- [[struct_C]], [[Pointer_C]] (Used to build the handler objects and link the chain)
- Decoupling (Sender doesn't know the specific receiver)
- Linked Lists (The chain structure is similar to a linked list)

---
**Source:** Worksheet C_WS5