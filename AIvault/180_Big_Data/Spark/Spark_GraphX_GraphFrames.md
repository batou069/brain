---
tags:
  - spark
  - pyspark
  - graphx
  - graphframes
  - graph_processing
  - distributed_graph
  - concept
aliases:
  - Spark Graph Processing
  - GraphX
  - GraphFrames
related:
  - "[[180_Big_Data/Spark/_Spark_MOC|_Spark_MOC]]"
  - "[[RDD_Resilient_Distributed_Dataset|RDD]]"
  - "[[Spark_DataFrame_SQL|Spark DataFrame & SQL]]"
  - "[[Graph_Theory_Concepts]]"
worksheet:
  - WS_Spark_1
date_created: 2025-08-20
---
# Spark: Graph Processing (GraphX and GraphFrames)

Apache Spark provides capabilities for graph processing and analytics through two main libraries/APIs: **GraphX** (the original RDD-based API) and **GraphFrames** (a newer DataFrame-based API). These allow users to model, transform, and query graph-structured data at scale.

Graphs consist of vertices (nodes) and edges (relationships between nodes). Examples include social networks, web graphs, protein interaction networks, and transportation networks.

## 1. GraphX (RDD-based API)
-   **Core Abstraction:** `Graph[VD, ED]`, where `VD` is the type of vertex attributes and `ED` is the type of edge attributes. A graph is represented by two [[RDD_Resilient_Distributed_Dataset|RDDs]]: one for vertices (`graph.vertices`) and one for edges (`graph.edges`). Edges are typically `Edge(srcId, dstId, attribute)` triplets.
-   **Language:** Primarily available in Scala and Java. PySpark has limited support for GraphX, mainly for loading graphs or calling some algorithms, but defining complex graph computations directly in PySpark with GraphX is less common/ergonomic.
-   **Key Features:**
    -   Property graphs (vertices and edges can have attributes).
    -   A rich set of graph operators: `subgraph()`, `mask()`, `joinVertices()`, `aggregateMessages()`.
    -   Implementations of common graph algorithms:
        -   PageRank
        -   Connected Components
        -   Strongly Connected Components
        -   Triangle Counting
        -   Shortest Paths (though often limited to non-negative weights or unweighted)
    -   Pregel API: A vertex-centric bulk-synchronous parallel programming model for iterative graph algorithms.
-   **Status:** While powerful, GraphX development has slowed, and the community focus has somewhat shifted towards GraphFrames for users preferring DataFrame APIs, especially in PySpark.

**Conceptual GraphX Usage (Illustrative - more natural in Scala/Java):**
```scala
// Scala Example for GraphX
// import org.apache.spark.graphx._
// import org.apache.spark.rdd.RDD

// val sc: SparkContext = ... // SparkContext

// Create an RDD for vertices
// val users: RDD[(VertexId, (String, String))] =
//   sc.parallelize(Array((3L, ("rxin", "student")), (7L, ("jgonzal", "postdoc")),
//                        (5L, ("franklin", "prof")), (2L, ("istoica", "prof"))))
// Create an RDD for edges
// val relationships: RDD[Edge[String]] =
//   sc.parallelize(Array(Edge(3L, 7L, "collab"),    Edge(5L, 3L, "advisor"),
//                        Edge(2L, 5L, "colleague"), Edge(5L, 7L, "pi")))
// Define a default user in case some users are only referenced in relationships
// val defaultUser = ("John Doe", "Missing")
// Build the initial Graph
// val graph = Graph(users, relationships, defaultUser)

// Count all users who are postdocs
// val postdocCount = graph.vertices.filter { case (id, (name, pos)) => pos == "postdoc" }.count()
// println(s"Number of postdocs: $postdocCount")

// Run PageRank
// val ranks = graph.pageRank(0.001).vertices
// ranks.join(users).sortBy(_._2._1, ascending=false).map {
//   case (id, (rank, (name, pos))) => s"$name ($pos) has rank $rank."
// }.take(5).foreach(println)
```

## 2. GraphFrames (DataFrame-based API)
-   **Core Abstraction:** Graphs are represented by two [[Spark_DataFrame_SQL|Spark DataFrames]]: one for vertices and one for edges.
    -   **Vertex DataFrame:** Must have a special column named `"id"` specifying unique vertex IDs. Can have other columns for vertex attributes.
    -   **Edge DataFrame:** Must have two special columns: `"src"` (source vertex ID of edge) and `"dst"` (destination vertex ID of edge). Can have other columns for edge attributes.
-   **Language:** Available in Python (PySpark), Scala, and Java. It's the preferred graph API for PySpark users.
-   **Integration:** Built on top of Spark DataFrames, allowing seamless integration with Spark SQL and MLlib. Leverages Catalyst optimizer.
-   **Key Features:**
    -   Motif finding: Searching for structural patterns in the graph (e.g., find all triangles where users A, B, C follow each other).
    -   Standard graph algorithms: PageRank, Connected Components, Strongly Connected Components, Shortest Paths (BFS-based), Label Propagation Algorithm (LPA) for community detection, Triangle Counting.
    -   Graph queries similar to Cypher (from Neo4j) but expressed using DataFrame operations.
    -   Message passing via `aggregateMessages` framework (similar to GraphX but adapted for DataFrames).
-   **Installation:** GraphFrames is a separate package that needs to be added to Spark applications (e.g., using `--packages graphframes:graphframes:0.8.x-spark3.y-s_2.12` when submitting a job, or configured in `SparkSession`).

**PySpark GraphFrames Example (Conceptual E-commerce: Customers and Co-purchased Products):**
```python
# from pyspark.sql import SparkSession
# from pyspark.sql.functions import col
# # Assuming GraphFrames package is available to SparkSession

# spark = SparkSession.builder \
#     .appName("GraphFramesExample") \
#     .master("local[*]") \
#     .config("spark.jars.packages", "graphframes:graphframes:0.8.2-spark3.2-s_2.12") \ # Adjust version as needed
#     .getOrCreate()

# # Create Vertex DataFrame (e.g., customers and products)
# # Nodes can be customers or products
# vertices_data = [
#     ("c1", "Alice", "customer"), ("c2", "Bob", "customer"), ("c3", "Carol", "customer"),
#     ("p1", "Laptop", "product"), ("p2", "Mouse", "product"), ("p3", "Keyboard", "product")
# ]
# v_df = spark.createDataFrame(vertices_data, ["id", "name", "type"])

# # Create Edge DataFrame (e.g., customer 'purchased' product)
# edges_data = [
#     ("c1", "p1", "purchased"), ("c1", "p2", "purchased"), # Alice bought Laptop, Mouse
#     ("c2", "p1", "purchased"), ("c2", "p3", "purchased"), # Bob bought Laptop, Keyboard
#     ("c3", "p2", "purchased")                            # Carol bought Mouse
# ]
# e_df = spark.createDataFrame(edges_data, ["src", "dst", "relationship"])

# # Create a GraphFrame
# try:
#     from graphframes import GraphFrame # Import after SparkSession with package is created
#     g = GraphFrame(v_df, e_df)
# except ImportError:
#     print("GraphFrames package not found or not configured correctly with SparkSession.")
#     g = None # So rest of conceptual example doesn't break immediately

# if g:
    # Display vertices and edges
    # print("--- Vertices ---")
    # g.vertices.show()
    # print("--- Edges ---")
    # g.edges.show()

    # Query: Find customers who purchased a "Laptop"
    # laptop_buyers = g.filterEdges("relationship = 'purchased'") \
    #                  .filterVertices("type = 'customer'") \
    #                  .find("(a)-[e]->(b)") \
    #                  .filter("b.name = 'Laptop' AND a.type = 'customer'") \
    #                  .select("a.name as customer_name") \
    #                  .distinct()
    # print("--- Customers who bought a Laptop ---")
    # laptop_buyers.show()

    # Run PageRank (conceptual, might need more specific graph structure for meaningful PageRank)
    # results_pagerank = g.pageRank(resetProbability=0.15, tol=0.01)
    # print("--- PageRank Vertices (sample) ---")
    # results_pagerank.vertices.select("id", "name", "pagerank").orderBy(col("pagerank").desc()).show(5)
    # print("--- PageRank Edges (sample) ---")
    # results_pagerank.edges.select("src", "dst", "weight").show(5) # 'weight' is added by PageRank

    # Find connected components
    # connected_components_df = g.connectedComponents()
    # print("--- Connected Components ---")
    # connected_components_df.select("id", "name", "component").orderBy("component", "id").show()

# spark.stop()
```
> **Note:** Running GraphFrames examples requires the GraphFrames package to be correctly linked with your Spark session.

## Choosing Between GraphX and GraphFrames
-   **Language Preference:**
    -   **GraphX:** Primarily for Scala/Java users. PySpark API is limited.
    -   **GraphFrames:** First-class support for Python (PySpark), Scala, and Java. More natural for PySpark users.
-   **API Style:**
    -   **GraphX:** RDD-based, lower-level, offers fine-grained control (e.g., Pregel API).
    -   **GraphFrames:** DataFrame-based, higher-level, benefits from Catalyst optimizations, allows SQL-like queries on graph motifs.
-   **Performance:**
    -   GraphX can sometimes be more performant for highly iterative, low-level graph algorithms due to direct RDD manipulation and less overhead than DataFrames for certain operations.
    -   GraphFrames can leverage Catalyst query optimizations and Tungsten execution, which can be very efficient for queries and algorithms expressible in DataFrame operations.
-   **Ease of Use:**
    -   GraphFrames are often considered easier to use for those already familiar with Spark DataFrames and SQL.
-   **Community and Development:**
    -   GraphFrames has seen more active development and community focus in recent years compared to GraphX.

For most new graph processing tasks in PySpark, **GraphFrames is generally the recommended choice** due to its Python-friendliness and integration with the DataFrame ecosystem. GraphX remains relevant for complex, low-level graph algorithms primarily in Scala/Java environments.

---