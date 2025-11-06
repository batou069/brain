---
tags:
  - reinforcement_learning
  - rl
  - curiosity
  - regret
  - exploration
  - concept
aliases:
  - Curiosity in RL
  - Regret in RL
related:
  - "[[140_Data_Science_AI/Reinforcement_Learning/_Reinforcement_Learning_MOC|_Reinforcement_Learning_MOC]]"
  - "[[RL_Exploration_vs_Exploitation]]"
  - "[[RL_Multi_Arm_Bandit]]"
worksheet:
  - WS_RL_1
date_created: 2025-09-10
---
# RL: Curiosity and Regret

**Curiosity** and **Regret** are two important concepts in Reinforcement Learning (RL) that relate to how an [[RL_Agent|agent]] explores its [[RL_Environment|environment]] and evaluates its performance.

## Curiosity
-   **Definition:** In RL, **curiosity** refers to an intrinsic motivation mechanism that encourages an [[RL_Agent|agent]] to explore novel or surprising states, even when there is no immediate external [[RL_State_Action_Reward|reward]] signal. It's a way to drive [[RL_Exploration_vs_Exploitation|exploration]] in environments with sparse or delayed rewards.
-   **Why it's Needed:**
    -   **Sparse Rewards:** In many complex environments (e.g., a long maze, a difficult video game), the agent might receive very few positive rewards (e.g., only at the end of the maze). A purely reward-driven agent might struggle to learn anything useful because it rarely encounters external rewards.
    -   **Local Optima:** Without sufficient exploration, an agent might get stuck in a suboptimal [[RL_Policy|policy]].
-   **How it's Implemented (Intrinsic Reward):**
    -   Curiosity is often implemented by giving the agent an **intrinsic reward** for actions that lead to novel or unpredictable states. This intrinsic reward is added to the external reward from the environment.
    -   **Prediction Error:** A common approach is to train a separate "prediction model" that tries to predict the next state given the current state and action. The agent's intrinsic reward is then proportional to the **prediction error** of this model. If the agent encounters a state it cannot predict well, it gets a high intrinsic reward, encouraging it to explore that state further.
    -   **Novelty Detection:** Other methods involve giving rewards for visiting states that have been visited infrequently.
-   **Example:** A robot in a new room might get an intrinsic reward for opening a door it hasn't opened before, even if opening the door doesn't immediately lead to a treasure (external reward). This encourages it to map out its environment.

## Regret
-   **Definition:** In RL and decision theory, **regret** is a measure of how much cumulative reward an [[RL_Agent|agent]] has "missed out on" by not always choosing the optimal action. It quantifies the difference between the cumulative reward obtained by the agent's chosen [[RL_Policy|policy]] and the cumulative reward that would have been obtained by always choosing the optimal policy.
-   **Types of Regret:**
    -   **Simple Regret:** The difference between the reward of the best action found so far and the reward of the truly optimal action.
    -   **Cumulative Regret:** The sum of the differences between the reward of the optimal action and the reward of the chosen action at each time step, accumulated over all time steps. This is the more common measure in contexts like [[RL_Multi_Arm_Bandit|Multi-Arm Bandit]] problems.
-   **Goal of Learning:** A good RL algorithm aims to **minimize cumulative regret** over time. This means it wants to learn the optimal policy as quickly as possible and then exploit it effectively.
-   **Relationship to Exploration-Exploitation:** Regret is a direct consequence of the [[RL_Exploration_vs_Exploitation|exploration-exploitation trade-off]].
    -   **Exploration** inherently increases immediate regret (by trying suboptimal actions) but aims to reduce long-term cumulative regret (by finding better actions).
    -   **Exploitation** minimizes immediate regret (by taking the best-known action) but risks high long-term cumulative regret if the truly optimal action has not yet been discovered.
-   **Example:** In a [[RL_Multi_Arm_Bandit|Multi-Arm Bandit]] problem, if the optimal arm yields 10 points per play, and the agent plays a suboptimal arm yielding 5 points, it incurs a regret of 5 points for that play. The goal is to minimize the total points lost over many plays.

## Summary Table

[list2mdtable|#Curiosity vs. Regret]
- Feature
    - Curiosity
        - Regret
- **Concept**
    - Intrinsic motivation to explore novel/surprising states.
        - Measure of cumulative reward missed by not choosing optimal actions.
- **Role in Learning**
    - Drives exploration, especially with sparse external rewards.
        - Metric to evaluate the effectiveness of an exploration-exploitation strategy.
- **Direction**
    - Forward-looking (encourages trying new things).
        - Backward-looking (quantifies past suboptimal decisions).
- **Impact on Agent**
    - Agent seeks out information/novelty.
        - Agent aims to minimize this value over time.

Curiosity and regret are crucial concepts for designing effective exploration strategies and evaluating the long-term performance of RL agents.

---