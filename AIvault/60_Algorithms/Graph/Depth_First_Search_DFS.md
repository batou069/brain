---
tags:
  - algorithms
  - searching
  - graph_traversal
  - dfs
  - concept
aliases:
  - DFS
related:
  - "[[Graph_Theory]]"
  - "[[Breadth_First_Search_BFS]]"
  - "[[Stack_ADT]]"
  - "[[Recursion]]"
  - "[[Topological_Sort]]"
worksheet:
  - WS_Math_Foundations_2
date_created: 2025-08-20
---
# Depth-First Search (DFS)

## Definition
**Depth-First Search (DFS)** is an algorithm for traversing or searching tree or [[Graph_Theory|graph]] data structures. The algorithm starts at a selected node (the "source" or "root") and explores as far as possible along each branch before backtracking.

It goes "deep" into the graph first, following one path to its end, then backtracks to explore other paths.

## Data Structure Used
DFS implicitly uses a **[[Stack_ADT|Stack]]** (Last-In, First-Out). This is often implemented using [[Recursion|recursion]] (which uses the call stack), but can also be implemented iteratively with an explicit stack.

## Algorithm Steps (Recursive)
1.  **Initialization:**
    - Create a set or boolean array `visited` to keep track of visited nodes.
2.  **DFS Function (`dfs_visit(node)`):**
    - Mark the current `node` as visited.
    - Process the `node` (e.g., print it).
    - For each neighbor of the `node`:
        - If the neighbor has not been visited, recursively call `dfs_visit(neighbor)`.
3.  **Start:** Call `dfs_visit(start_node)`. If the graph might be disconnected, loop through all nodes and call `dfs_visit` if the node hasn't been visited yet.

## Complexity Analysis
Let $V$ be the number of vertices (nodes) and $E$ be the number of edges in the graph.
- **Time Complexity:** $O(V + E)$
    - Each vertex is visited exactly once ($O(V)$).
    - Every edge is explored once ($O(E)$).
- **Space Complexity:** $O(V)$
    - In the worst case, the recursion depth (call stack) can be up to $V$ for a path-like graph. The `visited` set also takes $O(V)$ space.

## Python Implementation (Recursive)

```python
def dfs_recursive(graph, node, visited, traversal_order):
    """
    Recursive helper function for DFS.
    """
    visited.add(node)
    traversal_order.append(node)
    
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, traversal_order)

def dfs(graph, start_node):
    """
    Performs a Depth-First Search on a graph.
    
    :param graph: A dictionary representing the adjacency list of the graph.
    :param start_node: The node to start the traversal from.
    :return: A list of nodes in the order they were visited.
    """
    if start_node not in graph:
        return []
        
    visited = set()
    traversal_order = []
    dfs_recursive(graph, start_node, visited, traversal_order)
    return traversal_order

# Example usage
# Graph represented as an adjacency list
my_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start = 'A'
dfs_path = dfs(my_graph, start)
print(f"Graph: {my_graph}")
print(f"DFS traversal starting from node '{start}': {dfs_path}")

# Expected Output:
# Graph: {'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}
# DFS traversal starting from node 'A': ['A', 'B', 'D', 'E', 'F', 'C']
# Note: The exact traversal order can vary depending on the order of neighbors in the adjacency list.
# For example, ['A', 'C', 'F', 'E', 'B', 'D'] is also a valid DFS path.
```

## Applications
- **Cycle Detection:** Detecting cycles in a graph.
- **[[Topological_Sort|Topological Sorting]]:** For Directed Acyclic Graphs (DAGs), DFS is the basis for topological sorting, which provides a linear ordering of vertices.
- **Path Finding:** Finding a path between two nodes in a graph.
- **Solving Puzzles with a Single Solution Path:** Such as mazes. DFS will explore one path to its conclusion.
- **Finding Connected Components:** Can be used to find all nodes in a connected component.
- **Flood Fill Algorithm:** Used in paint programs to fill a contiguous area with a color.

## BFS vs. DFS
- **Structure:** BFS explores layer by layer; DFS explores branch by branch.
- **Data Structure:** BFS uses a queue; DFS uses a stack (often via recursion).
- **Path Finding:** BFS is guaranteed to find the shortest path in an unweighted graph. DFS is not.
- **Space:** BFS can use a lot of memory if the branching factor is large. DFS can use a lot of memory (stack depth) if the paths are very long.

---