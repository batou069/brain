---
tags:
  - python
  - tensorflow
  - tf
  - graph_mode
  - eager_execution
  - execution_model
  - tf_function
  - concept_comparison
aliases:
  - TensorFlow Execution Modes
  - TF Eager vs Graph
  - Computation Graphs TF
related:
  - "[[160_Python_Libraries/TensorFlow/_TensorFlow_MOC|_TensorFlow_MOC]]"
  - "[[TensorFlow_Operations]]"
  - "[[tf.function|TensorFlow tf.function]]"
  - "[[Spark_Lazy_vs_Eager_Execution]]"
worksheet:
  - WS_DeepLearning_1
date_created: 2025-06-11
---
# TensorFlow: Graphs and Eager Execution

TensorFlow has evolved in how it executes operations. Understanding both **Eager Execution** (the default in TensorFlow 2.x) and **Graph Execution** (traditional TensorFlow 1.x style, and still used via `tf.function`) is important.

## Eager Execution
-   **Definition:** An imperative programming environment that evaluates [[TensorFlow_Operations|operations]] immediately as they are called from Python. Results are returned directly to Python without needing to build a graph and run it in a session.
-   **Default in TensorFlow 2.x:** When you run TensorFlow 2.x code, it executes eagerly by default.
-   **Characteristics:**
    -   **Intuitive and Pythonic:** Feels more like standard Python programming and NumPy. Easier to debug with standard Python tools (e.g., `pdb`, print statements).
    -   **Immediate Results:** Operations return concrete values immediately.
    -   **Dynamic Control Flow:** Python control flow (if-statements, loops) can be used naturally with tensors.
    -   **No Sessions:** No need to explicitly create and manage `tf.Session` objects (as was required in TF 1.x graph mode).
-   **Example:**
    ```python
    import tensorflow as tf

    # Eager execution is on by default in TF 2.x
    # print(f"Eager execution enabled: {tf.executing_eagerly()}") # True

    a = tf.constant()
    b = tf.constant()
    c = a + b  # Operation is performed immediately
    # print("Result of a + b (eager):", c.numpy()) # c is a tf.Tensor, .numpy() gets value

    # if c.numpy() > 5: # Python control flow
    #     d = c * 2
    #     print("d (c*2):", d.numpy())
    # else:
    #     print("c was not greater than 5")
    ```
-   **When it's good:** Excellent for research, experimentation, debugging, and writing more intuitive code.

## Graph Execution (Graph Mode)
-   **Definition:** In graph execution, TensorFlow operations define a **computation graph** (also called a dataflow graph). This graph represents the computations as a set of nodes (operations) and edges (tensors flowing between ops). The graph is then executed (often in a `tf.Session` in TF 1.x, or implicitly when a `@tf.function`-decorated function is called in TF 2.x).
-   **Traditional TensorFlow 1.x Style:** Required explicit graph building and session execution.
-   **TensorFlow 2.x with `@tf.function`:** The [[tf.function|`@tf.function` decorator]] allows you to write Python code that TensorFlow can then convert into a callable computation graph. This combines the ease of eager-like programming with the benefits of graph execution.
-   **Characteristics:**
    -   **Deferred Execution:** Operations define the graph; computation happens only when the graph (or part of it) is explicitly executed.
    -   **Optimization:** Graphs can be optimized by TensorFlow (e.g., removing redundant computations, fusing operations, parallelizing independent operations) before execution.
    -   **Performance:** Optimized graphs can often run faster and use fewer resources than equivalent eager code, especially for complex models or on specialized hardware (GPUs, TPUs).
    -   **Portability:** Graphs can be saved as `SavedModel` format and deployed to various environments (servers, mobile, web) without needing the original Python code.
    -   **Static Nature (Once Traced):** Once a Python function is traced into a graph by `@tf.function`, the graph structure is generally fixed for a given input signature. Python control flow is converted into graph control flow ops (e.g., `tf.cond`, `tf.while_loop`) by AutoGraph.
-   **Example (using `@tf.function` in TF 2.x):**
    ```python
    import tensorflow as tf

    # @tf.function # Decorate to create a graph
    # def add_and_multiply(x, y, z):
    #     print("Tracing add_and_multiply with x=", x, "y=", y) # Prints only during tracing
    #     sum_val = x + y
    #     product_val = sum_val * z
    #     return product_val

    # a_tf = tf.constant(2.0)
    # b_tf = tf.constant(3.0)
    # c_tf = tf.constant(4.0)

    # First call: Traces the function and creates a graph
    # result1 = add_and_multiply(a_tf, b_tf, c_tf)
    # print("Result 1:", result1.numpy()) # (2+3)*4 = 20

    # Second call (with same input tensor dtypes/shapes): Uses the cached graph
    # result2 = add_and_multiply(a_tf, b_tf, c_tf*2.0) # c_tf*2.0 is a new tensor but same signature
    # print("Result 2:", result2.numpy()) # (2+3)*8 = 40
    # The "Tracing..." message does not print for the second call if signature matches.

    # To see the graph (conceptual)
    # concrete_func = add_and_multiply.get_concrete_function(a_tf, b_tf, c_tf)
    # print(concrete_func.graph.as_graph_def())
    ```

## Interplay: Eager by Default, Graphs for Performance/Deployment
In TensorFlow 2.x:
-   You write code in an eager, Pythonic style.
-   For performance-critical sections or parts of your model that you want to deploy, you can decorate Python functions with `@tf.function`. TensorFlow will then attempt to convert this Python code into an optimized computation graph.
-   [[Keras_API_in_TensorFlow|`tf.keras` models]] automatically leverage `@tf.function` for their `call` methods and training loops when `model.compile(run_eagerly=False)` (which is the default). Setting `run_eagerly=True` forces Keras models to run eagerly, which can be useful for debugging.

## Why Both?

[list2tab|#Eager vs Graph Benefits]
- Eager Execution
    -   **Pros:**
        -   Intuitive, Pythonic programming style.
        -   Easy debugging with standard Python tools.
        -   Immediate feedback and results.
        -   Natural Python control flow.
    -   **Cons:**
        -   Can be less performant than optimized graphs for complex computations due to Python interpreter overhead and less global optimization.
        -   Harder to serialize and deploy models as graphs for some environments.
- Graph Execution (via `@tf.function`)
    -   **Pros:**
        -   **Performance:** Graph optimization (op fusion, pruning), potential for parallel execution, reduced Python overhead.
        -   **Portability:** SavedModel format allows deploying graphs to diverse platforms (TF Serving, TFLite, TF.js).
        -   **Scalability:** Better suited for distributed training and execution on specialized hardware.
    -   **Cons:**
        -   Debugging can be trickier as errors might occur within the graph execution rather than Python.
        -   Understanding tracing behavior and AutoGraph conversions for Python control flow requires some learning.
        -   Side effects in Python code within `@tf.function` might not behave as expected (only run during tracing).

TensorFlow 2.x aims to provide the best of both worlds: the ease of use and interactivity of eager execution for development and debugging, and the performance and deployability of graph execution for production and computationally intensive tasks through `@tf.function`.

---