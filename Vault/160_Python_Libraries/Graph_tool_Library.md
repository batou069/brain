---
tags:
  - python
  - library
  - graph_tool
  - network_analysis
  - graph_theory
  - visualization
  - performance
  - concept
aliases:
  - gt
  - Python Graph-tool
related:
  - "[[_Python_Libraries_MOC]]"
  - "[[_NumPy_MOC]]"
  - "[[Graph_Theory_Concepts]]"
worksheet:
  - WS_Python_Packages_1
date_created: 2025-06-01
---
# Graph-tool Library

## Overview
**Graph-tool** (often imported as `gt`) is a Python library for the creation, manipulation, and analysis of **graphs** (or networks). It is known for its high performance, which is achieved by implementing core data structures and algorithms in C++ using templates and leveraging OpenMP for parallel execution.

Graph-tool aims to provide a combination of Python's ease of use with the performance of a compiled C++ library, making it suitable for analyzing very large graphs. It offers a wide range of functionalities, from basic graph operations to advanced statistical inference on graphs.

> [!warning] Installation
> Graph-tool can sometimes be challenging to install due to its C++ dependencies and compilation requirements. It's often recommended to install it using a package manager like Conda or from pre-compiled binaries if available for your system.

## Key Features and Functionality
[list2tab|#Graph-tool Features]
- **Performance:**
    - Core algorithms and data structures implemented in C++.
    - Parallel execution using OpenMP for many algorithms.
    - Efficient memory usage.
- **Graph Representation:**
    - `Graph` class: Represents directed or undirected graphs.
    - Supports multiple edges between nodes and self-loops.
- **Property Maps:**
    - Flexible system for associating arbitrary data (properties) with vertices, edges, or the graph itself. `PropertyMap` objects behave like dictionaries or NumPy arrays.
- **Graph I/O:**
    - Supports reading and writing graphs in various formats: GraphML, GML, Dot (Graphviz), GT (its own binary format).
- **Graph Algorithms:**
    - **Traversal:** Breadth-First Search (BFS), Depth-First Search (DFS).
    - **Shortest Paths:** Dijkstra, Bellman-Ford, A*.
    - **Connectivity:** Connected components, strongly connected components, articulation points, bridges.
    - **Centrality Measures:** Degree, betweenness, closeness, eigenvector, Katz, PageRank.
    - **Community Detection / Clustering:** Stochastic Block Model (SBM), modularity optimization, Louvain method (via plugins or external calls often).
    - **Flow Algorithms:** Max-flow, min-cut.
    - **Graph Filtering:** Dynamically hide/show vertices and edges based on their properties without modifying the graph.
- **Statistical Inference on Graphs:**
    - A strong focus of the library is on fitting generative graph models, particularly **Stochastic Block Models (SBMs)** and their variants (degree-corrected, overlapping, hierarchical).
    - Provides tools for Bayesian inference of model parameters.
- **Graph Drawing and Visualization:**
    - Powerful layout algorithms (e.g., sfdp, fdp, arf).
    - Interactive drawing capabilities, often leveraging Cairo and GTK+ for high-quality output.
    - Can export to various formats (PNG, PDF, SVG).
- **Network Generation:**
    - Functions to create various types of random graphs (Erdos-Renyi, Barabasi-Albert, Watts-Strogatz) and regular graphs (lattices, trees).

## Example Usage (Conceptual - Requires Installation)

### Creating a Graph and Adding Properties
```python
# This code assumes graph_tool is installed and importable
from graph_tool.all import * # Common way to import, though specific imports are better

try:
    from graph_tool.all import Graph, arf_layout, graph_draw
except ImportError:
    print("Graph-tool library not found. Examples cannot be run.")
    # Define dummy classes/functions if graph_tool is not installed for script to not break
    class Graph: pass
    def arf_layout(g, max_iter): return None
    def graph_draw(g, pos, output): pass
    # This allows the rest of the conceptual example to be written
    # without causing an immediate error if graph_tool is missing.

# Create an empty graph (undirected by default)
g = Graph()
g.set_directed(False)

# Add some vertices
v1 = g.add_vertex()
v2 = g.add_vertex()
v3 = g.add_vertex()
vlist = g.add_vertex(5) # Add 5 vertices at once

# Add edges
e1 = g.add_edge(v1, v2)
g.add_edge(vlist[0], vlist[1])
g.add_edge(vlist[1], vlist[2])

# Add vertex properties
v_prop_name = g.new_vertex_property("string") # Property map for vertex names
v_prop_name[v1] = "Node A"
v_prop_name[v2] = "Node B"
v_prop_name[vlist[0]] = "Node C0"

# Add edge properties
e_prop_weight = g.new_edge_property("double") # Property map for edge weights
e_prop_weight[e1] = 2.5

print(f"Number of vertices: {g.num_vertices()}")
print(f"Number of edges: {g.num_edges()}")
if g.num_vertices() > 0:
    print(f"Name of v1: {v_prop_name[v1] if 'v_prop_name' in locals() and v1 in v_prop_name else 'N/A'}")
if g.num_edges() > 0:
    print(f"Weight of e1: {e_prop_weight[e1] if 'e_prop_weight' in locals() and e1 in e_prop_weight else 'N/A'}")
```

### Calculating Centrality and Drawing
```python
# (Continued from above, assuming 'g' is a graph_tool.Graph object)
try:
    from graph_tool.all import Graph, betweenness, arf_layout, graph_draw # And others as needed

    # Calculate betweenness centrality
    vb, eb = betweenness(g) # Vertex and Edge betweenness

    # Store vertex betweenness as a new property
    g.vertex_properties["betweenness"] = vb

    for v in g.vertices():
        print(f"Vertex {int(v)}: Betweenness = {vb[v]:.2f}")

    # Basic drawing (requires layout algorithm and output)
    if g.num_vertices() > 0:
        pos = arf_layout(g, max_iter=0) # ARF layout algorithm
        graph_draw(g, pos=pos, vertex_text=g.vertex_index, vertex_font_size=10,
                   output_size=(400, 400), output="my_graph.png")
        print("Graph drawn to my_graph.png (if graph_tool and dependencies are correctly set up)")
except NameError: # If g was not defined due to import error
    print("Graph object 'g' not defined due to previous import error.")
except Exception as e:
    print(f"Graph-tool example error (likely needs full setup or simpler graph): {e}")
```

### Fitting a Stochastic Block Model (Conceptual)
```python
# (Conceptual - SBM fitting is more involved)
try:
    from graph_tool.all import Graph, minimize_blockmodel_dl # And others as needed
    # Load or create a graph 'g'
    state = minimize_blockmodel_dl(g) # Infer block structure
    state.draw(output="sbm_partition.png") # Draw graph colored by inferred blocks
except NameError:
    print("Graph object 'g' not defined.")
except Exception as e:
    print(f"SBM example error: {e}")
```

## Common Applications
- **Social Network Analysis:** Identifying communities, influential nodes, information diffusion.
- **Biological Networks:** Analyzing protein-protein interaction networks, gene regulatory networks.
- **Transportation Networks:** Finding shortest paths, analyzing network flow and resilience.
- **Information Networks:** Citation networks, web graphs.
- **Any domain involving relational data that can be modeled as a graph.**
- **Research in network science and statistical graph modeling.**

Graph-tool is particularly favored by researchers and practitioners who need to analyze large-scale networks and require high performance, or who are interested in advanced statistical modeling of graph structures, especially using SBMs. Its Python interface makes it accessible, while its C++ core delivers speed.

---