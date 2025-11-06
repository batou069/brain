---
tags:
  - reinforcement_learning
  - rl
  - temporal_difference
  - td_learning
  - bootstrapping
  - model_free
  - q_learning
  - sarsa
  - concept
aliases:
  - Temporal Difference Learning
  - TD Learning
related:
  - "[[140_Data_Science_AI/Reinforcement_Learning/_Reinforcement_Learning_MOC|_Reinforcement_Learning_MOC]]"
  - "[[RL_Monte_Carlo_Methods]]"
  - "[[RL_Q_Learning]]"
  - "[[RL_SARSA]]"
  - "[[RL_Value_Function]]"
worksheet:
  - WS_RL_1
date_created: 2025-09-10
---
# RL: Temporal Difference (TD) Learning

## Definition
**Temporal Difference (TD) learning** is a central concept in Reinforcement Learning (RL) that combines ideas from [[RL_Monte_Carlo_Methods|Monte Carlo (MC) methods]] and dynamic programming. Like MC methods, TD learning is **model-free** (learns directly from experience without a model of the environment). Like dynamic programming, it **bootstraps** (updates estimates based on other estimates).

TD learning updates its value estimates based on *partially observed* episodes, using the estimated value of the next state (or state-action pair) to update the current state's estimate.

## Key Characteristics
-   **Model-Free:** Learns directly from experience, no need for environment dynamics.
-   **Bootstrapping:** Updates its estimates based on other learned estimates (the estimated value of the next state/action). This is the key difference from Monte Carlo methods.
-   **Learning from Incomplete Episodes:** Can learn and update value estimates after each time step, without waiting for the end of an episode. This makes it suitable for continuous tasks (non-episodic) and faster for long episodic tasks.
-   **TD Target:** The target for the update is a combination of the immediate [[RL_State_Action_Reward|reward]] and the discounted estimated value of the next state (or state-action pair).

## The TD(0) Update Rule
The simplest TD algorithm, TD(0), updates the value function for a state $V(s_t)$ after observing a reward $r_{t+1}$ and the next state $s_{t+1}$:

$$ V(s_t) \leftarrow V(s_t) + \alpha [r_{t+1} + \gamma V(s_{t+1}) - V(s_t)] $$
where:
-   $V(s_t)$ is the current estimated value of state $s_t$.
-   $\alpha$ (alpha) is the learning rate ($0 < \alpha \le 1$).
-   $r_{t+1}$ is the immediate reward received after taking an action in $s_t$.
-   $\gamma$ (gamma) is the discount factor ($0 \le \gamma \le 1$).
-   $V(s_{t+1})$ is the current estimated value of the next state $s_{t+1}$.
-   The term $[r_{t+1} + \gamma V(s_{t+1}) - V(s_t)]$ is called the **TD Error**. It represents the difference between the estimated value of the current state and a "better" estimate (the TD target).

## TD vs. Monte Carlo

[list2mdtable|#TD vs. Monte Carlo]
- Feature
    - Temporal Difference (TD)
        - Monte Carlo (MC)
- **Update Timing**
    - After each time step (or a few steps). Can learn from incomplete episodes.
        - Only after a complete episode.
- **Bootstrapping**
    - Yes (updates estimates based on other estimates).
        - No (updates estimates based on actual observed returns).
- **Variance vs. Bias**
    - Generally has lower variance (because it uses a single step's reward and next state's estimate, which is less noisy than a full return). Can have higher bias (if the next state's estimate is inaccurate).
        - Generally has higher variance (due to noisy full returns). Can have lower bias (as it uses actual returns).
- **Applicability**
    - Suitable for continuous tasks (no terminal state) and long episodic tasks.
        - Requires episodic tasks.
- **Model-Free**
    - Yes.
        - Yes.

## TD Control Algorithms
TD learning forms the basis for powerful control algorithms that learn optimal policies. The two most prominent are [[RL_Q_Learning|Q-Learning]] and [[RL_SARSA|SARSA]].

-   **[[RL_Q_Learning|Q-Learning]]:** An **off-policy** TD control algorithm. It learns the optimal action-value function $Q(s,a)$ by taking the maximum over the estimated Q-values of the *next state*, regardless of the action actually taken.
-   **[[RL_SARSA|SARSA]]:** An **on-policy** TD control algorithm. It learns the optimal action-value function $Q(s,a)$ by using the Q-value of the *next action actually taken* by the behavior policy.

## Advantages of TD Learning
-   **Model-Free:** Like MC, it doesn't need a model of the environment.
-   **Online Learning:** Can learn continuously and update estimates after every step, making it suitable for online learning and continuous tasks.
-   **Faster Learning for Long Episodes:** For long episodes, it can learn much faster than MC because it doesn't have to wait until the end of the episode for updates.
-   **Lower Variance:** Often has lower variance than MC methods because it uses a single step's reward and the next state's value estimate, which is less noisy than a full return.

## Disadvantages of TD Learning
-   **Bootstrapping Bias:** Because it bootstraps, it can propagate errors if the estimates of future states are inaccurate.
-   **Requires State Representation:** Needs a way to represent and store value estimates for states or state-action pairs.

TD learning is a cornerstone of modern Reinforcement Learning, providing efficient and flexible ways to learn optimal behaviors directly from interaction.

---