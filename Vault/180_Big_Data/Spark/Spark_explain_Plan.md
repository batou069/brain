---
tags:
  - spark
  - dataframe
  - sql
  - query_plan
  - optimization
  - catalyst_optimizer
  - performance_tuning
  - concept
aliases:
  - Spark explain()
  - DataFrame explain()
  - Spark Query Optimization
related:
  - "[[Spark_DataFrame_SQL|Spark DataFrame & SQL]]"
  - "[[Spark_DAG_Scheduler|Spark DAG Scheduler]]"
  - "[[Catalyst_Optimizer_Spark]]"
  - "[[Spark_Performance_Tuning]]"
worksheet:
  - WS_Spark_1
date_created: 2025-06-11
---
# Spark: Understanding Query Plans with `explain()`

When working with [[Spark_DataFrame_SQL|Spark DataFrames]] or Spark SQL, understanding how Spark plans to execute your query is crucial for performance tuning and debugging. The `explain()` method (or `EXPLAIN` command in SQL) provides insight into the query execution plan generated by Spark's [[Catalyst_Optimizer_Spark|Catalyst optimizer]].

>[!question] Explain `explain`

## `DataFrame.explain()` Method
The `explain()` method can be called on a Spark DataFrame that has a sequence of transformations defined on it. It shows the different stages of query planning:

-   **Syntax:**
    ```python
    DataFrame.explain(extended=False, mode=None)
    # extended (boolean): If True, prints a more detailed plan (logical and physical).
    # mode (string, optional from Spark 3.0+): Specifies the format of the plan.
    #    - "simple": (Default before 3.0) Physical plan only.
    #    - "extended": Parsed logical, analyzed logical, optimized logical, and physical plan.
    #    - "cost": Optimized logical plan and physical plan with stats (if available via CBO).
    #    - "codegen": Physical plan and generated code (if any).
    #    - "formatted": A formatted output of the extended plan.
    ```

## Stages of a Query Plan Shown by `explain(extended=True)` or `explain(mode="formatted")`

1.  **Parsed Logical Plan (`== Parsed Logical Plan ==`)**:
    -   This is the initial logical plan generated after parsing the DataFrame operations or SQL query.
    -   It represents the query as a tree of unresolved logical operators (e.g., unresolved relations, attributes).
    -   At this stage, Spark hasn't verified if tables or columns exist or if data types are compatible.

2.  **Analyzed Logical Plan (`== Analyzed Logical Plan ==`)**:
    -   The parsed logical plan is resolved against Spark's catalog (which contains information about tables, views, functions, etc.).
    -   Table names are resolved to actual data sources, column names are validated, data types are checked and resolved.
    -   This plan is still logical (describes *what* to compute) but is now semantically correct.

3.  **Optimized Logical Plan (`== Optimized Logical Plan ==`)**:
    -   The [[Catalyst_Optimizer_Spark|Catalyst optimizer]] applies a series of rule-based and cost-based optimizations to the analyzed logical plan to create a more efficient logical plan.
    -   Common optimizations include:
        -   **Predicate Pushdown:** Moving filter conditions (predicates) as close to the data source as possible to reduce the amount of data read and processed.
        -   **Projection Pruning:** Eliminating unnecessary columns early in the plan.
        -   Constant folding, join reordering, expression simplification, etc.
    -   This plan still describes *what* to compute but in a more optimized way.

4.  **Physical Plan (`== Physical Plan ==`)**:
    -   The optimized logical plan is translated into one or more physical execution plans. Spark's cost model may choose the "best" physical plan among several possibilities.
    -   This plan describes *how* to execute the query. It specifies the actual physical operators Spark will use (e.g., `HashAggregate`, `SortMergeJoin`, `BroadcastHashJoin`, `FileScan`).
    -   It details operations like shuffles, broadcasts, and specific join algorithms.
    -   The physical plan is a DAG of RDD operations that will be executed on the cluster. Nodes in the plan often start with `*` (e.g., `*Project`, `*Filter`) indicating code generation might be used for that operator (Tungsten execution engine).

## Example
```python
# from pyspark.sql import SparkSession
# from pyspark.sql.functions import col, count

# spark = SparkSession.builder.appName("ExplainDemo").getOrCreate()

# Create sample DataFrames
# data1 = [(1, "Alice", "HR"), (2, "Bob", "Engineering"), (3, "Charlie", "HR")]
# df1 = spark.createDataFrame(data1, ["id", "name", "department"])

# data2 = [(1, "HR", "New York"), (2, "Engineering", "California")]
# df2 = spark.createDataFrame(data2, ["id_dept", "department", "location"]) # Mistake: dept name is 'department' not 'id_dept' for join key

# df1.createOrReplaceTempView("employees")
# df2.createOrReplaceTempView("departments")

# A query with a filter and a join
# query_result_df = df1.join(df2, df1["department"] == df2["department"], "inner") \
#                      .filter(col("salary") > 50000) # Error: 'salary' not in df1 or df2 in this simple example
#                      .groupBy("location") \
#                      .agg(count("*").alias("num_employees"))

# For a runnable example, let's simplify:
# df_employees = spark.createDataFrame([
#     (1, "Alice", "HR", 60000), (2, "Bob", "Engineering", 80000),
#     (3, "Charlie", "HR", 70000), (4, "David", "Engineering", 90000)
# ], ["id", "name", "department", "salary"])

# df_filtered_agg = df_employees.filter(col("salary") > 65000) \
#                               .groupBy("department") \
#                               .agg(count("id").alias("high_earners_count"))

# print("---- Simple Explain (Physical Plan Only) ----")
# df_filtered_agg.explain()
# Output might look like:
# == Physical Plan ==
# *(2) HashAggregate(keys=[department#xx], functions=[count(id#xx)])
# +- Exchange hashpartitioning(department#xx, 200), ENSURE_REQUIREMENTS, [plan_id=xx]
#    +- *(1) HashAggregate(keys=[department#xx], functions=[partial_count(id#xx)])
#       +- *(1) Project [department#xx, id#xx]
#          +- *(1) Filter (isnotnull(salary#xx) AND (salary#xx > 65000))
#             +- *(1) Scan ExistingRDD[id#xx,name#xx,department#xx,salary#xx]

# print("\n---- Extended Explain (Formatted) ----")
# df_filtered_agg.explain(mode="formatted") # Or explain(extended=True) for older Spark
# This will show Parsed, Analyzed, Optimized Logical Plans, and Physical Plan.
# You would see how 'salary > 65000' is pushed down to be near the data scan.

# spark.stop()
```

## Why Use `explain()`?
-   **Understanding Query Execution:** See how Spark translates your high-level DataFrame/SQL operations into a concrete execution plan.
-   **Performance Tuning:**
    -   Identify bottlenecks: Are there unexpected shuffles? Is predicate pushdown happening effectively? Are inefficient join strategies being used?
    -   Verify optimizations: Check if Catalyst applied expected optimizations.
    -   Compare plans for different ways of writing the same query.
-   **Debugging:** Understand why a query might be slow or producing unexpected results (though `explain()` focuses on the plan, not data issues).
-   **Learning Spark Internals:** Provides insight into the Catalyst optimizer and Spark's execution engine.

When working with complex queries or troubleshooting performance issues in Spark, `explain()` is an invaluable tool for peering under the hood. Reading and interpreting query plans is a key skill for Spark developers.

---