---
tags:
  - algorithms
  - concept
  - technique
  - paradigm
  - optimization
aliases:
  - Greedy Method
related:
  - "[[Algorithm]]"
  - "[[Optimization_Problem]]"
  - "[[Dynamic_Programming]]"
  - "[[Divide_and_Conquer]]"
  - "[[Huffman_Coding]]"
  - "[[Dijkstra_Algorithm]]"
  - "[[Prim_Algorithm]]"
  - "[[Kruskal_Algorithm]]"
worksheet: [WS25]
date_created: 2025-04-21
---
# Greedy Algorithm

## Definition

A **Greedy Algorithm** is an algorithmic paradigm that builds up a solution piece by piece, always choosing the option that looks best (most optimal or most promising according to some heuristic) at the current moment, without regard for future consequences. It makes a **locally optimal choice** at each stage with the hope of finding a **global optimum**.

## Key Aspects / Characteristics

- **Locally Optimal Choices:** At each step, makes the choice that seems best at that moment based on some greedy criterion.
- **Irrevocable Choices:** Once a choice is made, it is usually not reconsidered or undone later.
- **Simplicity:** Often simpler to design and implement compared to other optimization techniques like [[Dynamic_Programming]].
- **Efficiency:** Typically faster than exhaustive search or dynamic programming if applicable.
- **Correctness Not Guaranteed:** Greedy algorithms do **not** always produce the globally optimal solution for all optimization problems. They work only if the problem exhibits specific properties:
    - **Greedy Choice Property:** A globally optimal solution can be arrived at by making locally optimal (greedy) choices.
    - **Optimal Substructure:** An optimal solution to the problem contains within it optimal solutions to subproblems.
- **Proof of Correctness:** Requires careful mathematical proof to demonstrate that the greedy strategy indeed leads to a global optimum for a specific problem.

## General Structure

```plaintext
GreedyAlgorithm(Input):
  Initialize solution = empty
  While Input is not fully processed:
    Make a greedy choice based on some criterion from remaining Input
    If choice is feasible:
      Add choice to solution
      Update Input (remove chosen element or modify state)
    Else:
      Discard choice (or handle appropriately)
  Return solution
```

## Examples Where Greedy Works

- **Activity Selection Problem:** Choose the maximum number of non-overlapping activities from a set, given start and finish times. (Greedy: Pick activity that finishes earliest).
- **Making Change (Canonical Coin Systems):** Give the minimum number of coins for a given amount using standard coin denominations (e.g., USD quarters, dimes, nickels, pennies). (Greedy: Always take the largest denomination coin possible without exceeding the remaining amount). *Note: This doesn't work for all arbitrary coin systems.*
- **[[Huffman_Coding]]:** Building optimal prefix codes for data compression. (Greedy: Repeatedly merge the two nodes with the lowest frequencies).
- **Minimum Spanning Tree Algorithms:**
    - **[[Prim_Algorithm]]:** Greedily grows the MST by adding the cheapest edge connecting a vertex in the MST to one outside.
    - **[[Kruskal_Algorithm]]:** Greedily adds the next cheapest edge overall, as long as it doesn't form a cycle.
- **[[Dijkstra_Algorithm]]:** Finding the shortest path in a graph with non-negative edge weights. (Greedy: Always explore the unvisited node closest to the source).

## Examples Where Greedy Fails

- **0/1 Knapsack Problem:** Cannot simply pick items with the best value-to-weight ratio; might prevent taking other items that lead to a better overall value.
- **Traveling Salesperson Problem:** Picking the nearest unvisited city at each step does not guarantee the shortest overall tour.

## Related Concepts
- [[Algorithm]] Design Paradigms
- [[Optimization_Problem]]
- [[Dynamic_Programming]] (Often provides optimal solutions where greedy fails, but usually more complex)
- [[Divide_and_Conquer]]
- Heuristics (Greedy choices are often heuristic)

---
**Source:** Worksheet WS25