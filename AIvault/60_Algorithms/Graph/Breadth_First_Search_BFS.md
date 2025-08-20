---
tags:
  - algorithms
  - searching
  - graph_traversal
  - bfs
  - concept
aliases:
  - BFS
related:
  - "[[Graph_Theory]]"
  - "[[Depth_First_Search_DFS]]"
  - "[[Queue_ADT]]"
  - "[[Shortest_Path_Unweighted]]"
worksheet:
  - WS_Math_Foundations_2
date_created: 2025-08-20
---
# Breadth-First Search (BFS)

## Definition
**Breadth-First Search (BFS)** is an algorithm for traversing or searching tree or [[Graph_Theory|graph]] data structures. It starts at a selected node (the "source" or "root") and explores all of the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level.

It explores the graph "layer by layer," visiting all nodes at distance 1 from the source, then all nodes at distance 2, and so on.

## Data Structure Used
BFS uses a **[[Queue_ADT|Queue]]** (First-In, First-Out) data structure to keep track of the nodes to visit next.

## Algorithm Steps
1.  **Initialization:**
    - Create a [[Queue_ADT|queue]] and add the starting node to it.
    - Create a set or boolean array `visited` to keep track of visited nodes, and mark the starting node as visited.
2.  **Loop:** While the queue is not empty:
    - **Dequeue:** Remove the node at the front of the queue (let's call it `current_node`).
    - **Process:** Process `current_node` (e.g., print it, check if it's the target).
    - **Enqueue Neighbors:** For each neighbor of `current_node`:
        - If the neighbor has not been visited yet:
            - Mark the neighbor as visited.
            - Add the neighbor to the back of the queue.
3.  **Termination:** The algorithm terminates when the queue is empty, meaning all reachable nodes have been visited.

## Complexity Analysis
Let $V$ be the number of vertices (nodes) and $E$ be the number of edges in the graph.
- **Time Complexity:** $O(V + E)$
    - Each vertex is enqueued and dequeued exactly once ($O(V)$).
    - Every edge is explored once when its source vertex is dequeued ($O(E)$).
- **Space Complexity:** $O(V)$
    - In the worst case, the queue can hold all vertices of the graph (e.g., in a star graph, all neighbors of the central node are enqueued). The `visited` set also takes $O(V)$ space.

## Python Implementation

```python
from collections import deque

def bfs(graph, start_node):
    """
    Performs a Breadth-First Search on a graph.
    
    :param graph: A dictionary representing the adjacency list of the graph.
    :param start_node: The node to start the traversal from.
    :return: A list of nodes in the order they were visited.
    """
    if start_node not in graph:
        return []
        
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)
    
    traversal_order = []
    
    while queue:
        current_node = queue.popleft() # Dequeue from the front
        traversal_order.append(current_node)
        
        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor) # Enqueue to the back
                
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
bfs_path = bfs(my_graph, start)
print(f"Graph: {my_graph}")
print(f"BFS traversal starting from node '{start}': {bfs_path}")

# Expected Output:
# Graph: {'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}
# BFS traversal starting from node 'A': ['A', 'B', 'C', 'D', 'E', 'F']
```

## Applications
- **Shortest Path in Unweighted Graphs:** BFS is guaranteed to find the shortest path (in terms of number of edges) from a source node to all other reachable nodes in an unweighted graph.
- **Network Broadcasting:** Simulating the broadcast of a message through a network.
- **Web Crawlers:** Used to discover all pages on a website, exploring level by level starting from a homepage.
- **Finding Connected Components:** Can be used to find all nodes in a connected component of a graph.
- **Social Networks:** Finding all friends at a certain "degree" of connection away from a person.
- **Solving Puzzles:** Finding the shortest solution to puzzles like Rubik's Cubes or mazes, where states are nodes and moves are edges.

---