---
tags:
  - reinforcement_learning
  - rl
  - monte_carlo_tree_search
  - mcts
  - planning
  - game_ai
  - concept
aliases:
  - Monte-Carlo Tree Search
  - MCTS
related:
  - "[[140_Data_Science_AI/Reinforcement_Learning/_Reinforcement_Learning_MOC|_Reinforcement_Learning_MOC]]"
  - "[[RL_Monte_Carlo_Methods]]"
  - "[[RL_Model_Based_vs_Model_Free|Model-Based RL]]"
  - "[[RL_Algorithm_Selection_Criteria]]"
worksheet:
  - WS_RL_1
date_created: 2025-09-10
---
# RL: Monte-Carlo Tree Search (MCTS)

## Definition
**Monte-Carlo Tree Search (MCTS)** is a heuristic search algorithm for finding optimal decisions in complex decision processes, most notably in games. It combines the generality of [[RL_Monte_Carlo_Methods|Monte Carlo simulations]] with the precision of tree search. MCTS is a **planning algorithm** that works by building a search tree based on random simulations.

MCTS has been famously successful in game AI, most notably in AlphaGo, where it was combined with deep neural networks.

## The Four Phases of MCTS
MCTS iteratively builds a search tree by repeating four phases:

```mermaid
graph TD
    Root[Root Node (Current State)] --> Selection[1. Selection];
    Selection --> Expansion[2. Expansion];
    Expansion --> Simulation[3. Simulation (Rollout)];
    Simulation --> Backpropagation[4. Backpropagation];
    Backpropagation --> Root; % Loop back for next iteration
```

1.  **Selection:**
    -   Starting from the root node (the current game state), the algorithm traverses down the existing search tree.
    -   At each node, it selects the child node that maximizes an **Upper Confidence Bound (UCB1)** score. UCB1 balances exploitation (choosing nodes that have led to good results) and exploration (choosing nodes that haven't been visited much).
    -   This continues until a node is reached that has unvisited children (i.e., actions not yet explored from that state).
2.  **Expansion:**
    -   If the selected node is not a terminal state and has unvisited (unexpanded) children, one of these unvisited children is chosen and added to the search tree. This new child node represents a new state-action pair.
3.  **Simulation (Rollout):**
    -   From the newly expanded node (or any node that has no more children to expand), a **playout** (or rollout) is performed.
    -   This involves simulating the game (or decision process) from that node to a terminal state, usually by choosing actions randomly (or using a simple heuristic policy).
    -   The outcome (reward) of this simulated game is recorded.
4.  **Backpropagation:**
    -   The result (reward) from the simulation is "backpropagated" up the tree, from the expanded node back to the root.
    -   Each node along the path updates its statistics (e.g., total reward received, number of times visited). These statistics are used in the Selection phase (UCB1 score) for future iterations.

These four phases are repeated many times (thousands or millions of iterations) to build a robust search tree.

## Making a Decision
After a sufficient number of iterations, the algorithm chooses the best action from the root node. This is typically the action that leads to the child node with the highest average reward or the highest visit count.

## Advantages of MCTS
-   **Generality:** Can be applied to any game or decision process that can be simulated, even those with very large state spaces and complex rules (e.g., Go).
-   **Asymmetry:** Focuses computational effort on the most promising areas of the search space, expanding the tree more deeply in relevant branches.
-   **No Domain Knowledge Required (Basic MCTS):** A basic MCTS implementation can work without any explicit domain-specific heuristics, relying purely on random playouts.
-   **Anytime Algorithm:** It can be stopped at any time and still provide a "best guess" answer, which improves with more computation time.

## Disadvantages of MCTS
-   **Requires Simulation:** Needs a way to simulate the environment/game quickly.
-   **Performance of Rollouts:** The quality of the random playouts can significantly impact performance. Using a more informed (but still fast) rollout policy can help.
-   **Exploration-Exploitation Balance:** The UCB1 formula is crucial, and its parameters might need tuning.
-   **Memory Usage:** For very large search spaces, the tree can consume a lot of memory.
-   **Not Directly an RL Algorithm:** MCTS is a **planning algorithm**; it uses a model (the game rules/simulator) to search for the best action *in the current state*. It doesn't directly learn a general [[RL_Policy|policy]] for all states in the same way Q-learning or policy gradients do, unless combined with a learning algorithm (as in AlphaGo).

>[!question]- In what setting would you use MCST? Give an example.
>
>You would use **Monte-Carlo Tree Search (MCTS)** in settings that involve **complex sequential decision-making problems, especially those with large state and action spaces, where a simulator or game engine is available, and where the goal is to find the best immediate action in a given state through planning.**
>
>**Ideal Settings for MCTS:**
>1.  **Games with Large Branching Factors:** Games like Chess, Go, or even many video games where the number of possible moves from any given state is very large, making exhaustive search infeasible.
>2.  **Deterministic or Stochastic Environments:** MCTS can handle both. For stochastic environments, simulations naturally account for randomness.
>3.  **Episodic Tasks:** Problems that have a clear start and end (episodes), as simulations run to completion.
>4.  **Availability of a Simulator/Model:** MCTS is a model-based planning algorithm, so it requires a way to simulate the environment's dynamics (the game rules).
>5.  **Time-Constrained Decision-Making:** As an "anytime" algorithm, it can provide a good decision even if interrupted, and its quality improves with more computation time.
>
>**Example: Developing an AI for the game of Go**
>
>-   **Setting:** Go is a board game with an enormous state space and branching factor, making traditional minimax search impractical.
>-   **MCTS Application:**
>    1.  **Root Node:** The current state of the Go board.
>    2.  **Selection:** The AI traverses the existing MCTS tree, using UCB1 to select promising moves (branches) that have led to good outcomes in past simulations or haven't been explored much.
>    3.  **Expansion:** When it reaches a new, unvisited board state, it adds a new node to the tree for a possible next move.
>    4.  **Simulation:** From this new node, it performs a "rollout" – a simulated game played out to the end, often using a fast, random (or simple heuristic) policy.
>    5.  **Backpropagation:** The result of the simulated game (win/loss) is propagated back up the tree, updating the win/loss statistics and visit counts for all nodes along the path.
>-   **Decision:** After many thousands or millions of these iterations (given a few seconds or minutes of thinking time), the AI chooses the move from the current board state that has the highest win rate (or other metric) among its children in the MCTS tree.
>-   **Combination with Deep Learning (AlphaGo):** AlphaGo famously enhanced MCTS by using deep neural networks to:
>    -   Guide the **Selection** phase (a "policy network" suggests promising moves, making the search more intelligent).
>    -   Improve the **Simulation** phase (a "value network" estimates the win probability from a given state, allowing for shallower but more informed rollouts).
>
>This combination made MCTS incredibly effective for Go, demonstrating its power in complex game AI.

---