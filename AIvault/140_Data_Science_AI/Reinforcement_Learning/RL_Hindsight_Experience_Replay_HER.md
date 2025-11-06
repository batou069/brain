---
tags:
  - reinforcement_learning
  - rl
  - deep_reinforcement_learning
  - her
  - experience_replay
  - sparse_rewards
  - concept
aliases:
  - Hindsight Experience Replay
  - HER
related:
  - "[[140_Data_Science_AI/Reinforcement_Learning/_Reinforcement_Learning_MOC|_Reinforcement_Learning_MOC]]"
  - "[[RL_Deep_Reinforcement_Learning]]"
  - "[[RL_Universal_Value_Function_Approximator_UVFA]]"
  - "[[RL_Experience_Memory]]"
  - "[[RL_Limitations]]"
worksheet:
  - WS_RL_1
date_created: 2025-09-10
---
# RL: Hindsight Experience Replay (HER)

## Definition
**Hindsight Experience Replay (HER)** is a technique in Reinforcement Learning (RL) that significantly improves sample efficiency in environments with **sparse and binary rewards**, especially when combined with [[RL_Universal_Value_Function_Approximator_UVFA|Universal Value Function Approximators (UVFAs)]].

The core idea of HER is to learn from "failed" attempts by pretending that the agent's actual outcome was the goal it was trying to achieve. Even if an agent fails to reach its desired goal, it *did* achieve *some* goal. HER re-labels past experiences with these "achieved goals," turning failures into successes from a different perspective.

## The Problem HER Addresses
-   **Sparse Rewards:** In many complex tasks (e.g., robotic manipulation), the agent only receives a positive [[RL_State_Action_Reward|reward]] (e.g., +1) if it perfectly achieves a specific goal, and 0 otherwise. This makes learning very difficult because the agent rarely gets positive feedback.
-   **Credit Assignment:** With sparse rewards, it's hard for the agent to understand which actions contributed to a distant success or why a sequence of actions led to a failure.

## How HER Works
HER is typically used in conjunction with an off-policy RL algorithm (like [[RL_Q_Learning|DQN]] or DDPG) and a [[RL_Universal_Value_Function_Approximator_UVFA|UVFA]].

1.  **Goal-Conditioned Policy/Value Function:** The agent's policy and/or value function takes the desired goal $g_{desired}$ as an additional input: $\pi(s, g_{desired})$ or $Q(s, a, g_{desired})$.
2.  **Experience Collection:** The agent interacts with the environment for an episode, trying to achieve $g_{desired}$. It collects a trajectory of experiences: $(s_t, a_t, r_{t+1}, s_{t+1})$.
3.  **Achieved Goal:** At the end of the episode (or at any point during the episode), the agent observes the final state $s_{final}$ and determines what goal it *actually achieved* in that episode. Let's call this $g_{achieved}$.
4.  **Re-labeling Experience:** For each transition $(s_t, a_t, r_{t+1}, s_{t+1})$ in the collected trajectory, HER creates **additional "hindsight" transitions** by:
    -   Replacing the original `g_{desired}` with `g_{achieved}`.
    -   Recomputing the reward $r'_{t+1}$ *as if* $g_{achieved}$ was the original desired goal. If the agent achieved $g_{achieved}$ from $s_{t+1}$, the reward $r'_{t+1}$ would now be positive (e.g., +1).
5.  **Storing in Replay Buffer:** Both the original experience transitions (with $g_{desired}$) and the hindsight experience transitions (with $g_{achieved}$) are stored in the [[RL_Experience_Memory|experience replay buffer]].
6.  **Training:** The RL algorithm then samples from this augmented replay buffer to train the UVFA.

## Example: Robot Arm Reaching Task
>[!question]- Give an example of how UVFA and HER work together.
>
>**Scenario:** A robot arm needs to learn to reach a specific target location in 3D space. The reward is +1 only if the end-effector is within a small tolerance of the target, and 0 otherwise.
>
>**Problem:** The robot might randomly flail for a very long time before ever hitting the exact target, making learning from sparse rewards extremely inefficient.
>
>**Solution: UVFA + HER**
>
>1.  **UVFA Setup:**
>    -   The robot's Q-network (or policy network) is a [[RL_Universal_Value_Function_Approximator_UVFA|UVFA]]. It takes the current state (arm joint angles, end-effector position) and the *desired target coordinates* (the goal) as input.
>    -   $Q(s, a, g_{desired})$
>
>2.  **Experience Collection (Original):**
>    -   The robot is given a desired target $g_{desired} = (x_{target}, y_{target}, z_{target})$.
>    -   It attempts to reach this target, taking actions $a_t$ from states $s_t$.
>    -   It collects a trajectory: $(s_0, a_0, r_1, s_1), (s_1, a_1, r_2, s_2), \dots, (s_T, a_T, r_{T+1}, s_{T+1})$.
>    -   Since the reward is sparse, most $r_t$ will be 0, unless it happens to hit $g_{desired}$.
>
>3.  **Achieved Goal ($g_{achieved}$):**
>    -   At the end of the episode, the robot's end-effector is at some final position $s_{final\_pos} = (x_{final}, y_{final}, z_{final})$.
>    -   This $s_{final\_pos}$ is the goal it *actually achieved*. So, $g_{achieved} = (x_{final}, y_{final}, z_{final})$.
>
>4.  **Hindsight Experience Generation:**
>    -   For *every transition* $(s_t, a_t, r_{t+1}, s_{t+1})$ in the original trajectory, HER creates a new hindsight transition:
>        -   The original desired goal $g_{desired}$ is replaced with $g_{achieved}$.
>        -   The reward $r'_{t+1}$ is recomputed: if $s_{t+1}$ is close to $g_{achieved}$, then $r'_{t+1}=+1$; otherwise, $r'_{t+1}=0$.
>    -   **Example:** If the robot tried to reach (1,1,1) but ended up at (0.8, 0.9, 0.7), then for all transitions in that episode, HER generates a new transition where the goal is (0.8, 0.9, 0.7), and the reward for the final step is +1 (because it *did* achieve that goal).
>
>5.  **Training:** The UVFA (Q-network) is trained on both the original and hindsight experiences.
>
>**Impact:**
>-   Even if the robot fails to reach the *desired* goal, it now has many "successful" experiences (from the perspective of the *achieved* goal).
>-   This provides a much denser reward signal, allowing the UVFA to learn much faster about the dynamics of reaching *any* goal, even if it's not the one initially intended.
>-   The robot learns from its "failures" by understanding what it *did* accomplish, which drastically improves sample efficiency in sparse reward environments.

## Advantages of HER
-   **Massive Sample Efficiency Improvement:** Especially in sparse reward environments, HER can turn almost every failed episode into a useful learning experience.
-   **Addresses Sparse Rewards:** Directly tackles one of the biggest challenges in RL.
-   **Generalization Across Goals:** When combined with UVFAs, it allows the agent to learn a general skill of achieving goals, rather than just one specific task.
-   **Off-Policy Compatibility:** Works well with off-policy RL algorithms, which can leverage the re-labeled experiences effectively.

## Limitations
-   **Requires Goal-Conditioned RL:** Needs a UVFA or a goal-conditioned policy/value function.
-   **Defining Achieved Goals:** Requires a way to reliably determine what goal was actually achieved from any given state.
-   **Not a Universal Fix:** While powerful, it doesn't solve all RL problems. It's most effective for tasks where achieving *any* goal provides useful learning signal for other goals.

HER is a significant advancement in DRL, enabling agents to learn complex tasks in environments that were previously intractable due to sparse rewards.

---