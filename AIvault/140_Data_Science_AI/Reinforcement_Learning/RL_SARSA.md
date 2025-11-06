---
tags:
  - reinforcement_learning
  - rl
  - sarsa
  - temporal_difference
  - on_policy
  - model_free
  - q_value
  - concept
aliases:
  - SARSA Algorithm
related:
  - "[[140_Data_Science_AI/Reinforcement_Learning/_Reinforcement_Learning_MOC|_Reinforcement_Learning_MOC]]"
  - "[[RL_Temporal_Difference_Learning]]"
  - "[[RL_Q_Learning]]"
  - "[[RL_Policy]]"
  - "[[RL_Exploration_vs_Exploitation]]"
  - "[[RL_Value_Function]]"
worksheet:
  - WS_RL_1
date_created: 2025-09-10
---
# RL: SARSA

## Definition
**SARSA (State-Action-Reward-State-Action)** is a **model-free, on-policy Temporal Difference (TD) control algorithm** in Reinforcement Learning. Like [[RL_Q_Learning|Q-Learning]], its goal is to learn an optimal [[RL_Policy|policy]] by finding the optimal action-value function, $Q(s,a)$.

The name SARSA comes from the tuple of events $(s_t, a_t, r_{t+1}, s_{t+1}, a_{t+1})$ that drives its update rule.

## The SARSA Update Rule
SARSA iteratively updates its estimate of the Q-value for a state-action pair $(s_t, a_t)$ after observing the immediate [[RL_State_Action_Reward|reward]] $r_{t+1}$, the next state $s_{t+1}$, and crucially, the **next action $a_{t+1}$ that the agent *actually takes*** in $s_{t+1}$.

$$ Q(s_t, a_t) \leftarrow Q(s_t, a_t) + \alpha [r_{t+1} + \gamma Q(s_{t+1}, a_{t+1}) - Q(s_t, a_t)] $$
where:
-   $Q(s_t, a_t)$ is the current estimated Q-value for taking action $a_t$ in state $s_t$.
-   $\alpha$ (alpha) is the learning rate ($0 < \alpha \le 1$).
-   $r_{t+1}$ is the immediate reward received.
-   $\gamma$ (gamma) is the discount factor ($0 \le \gamma \le 1$).
-   $Q(s_{t+1}, a_{t+1})$ is the estimated Q-value for the *next state $s_{t+1}$ and the next action $a_{t+1}$ that the agent actually chooses* (according to its behavior policy).
-   The term $[r_{t+1} + \gamma Q(s_{t+1}, a_{t+1}) - Q(s_t, a_t)]$ is the **TD Error**.

## Key Characteristics
-   **On-Policy:** This is the defining characteristic. The update rule uses $Q(s_{t+1}, a_{t+1})$, meaning it learns the value of the policy *currently being followed* (the behavior policy). If the agent is using an $\epsilon$-greedy policy to explore, SARSA will learn the optimal Q-function for *that specific $\epsilon$-greedy policy*, not necessarily the strictly greedy optimal policy.
-   **Model-Free:** It does not require knowledge of the environment's transition probabilities or reward function. It learns directly from experience.
-   **Value-Based:** It learns an action-value function ($Q(s,a)$). The optimal policy is then derived from the optimal Q-function.
-   **Bootstrapping:** It updates its estimates based on the estimated value of the next state-action pair.
-   **Convergence:** SARSA is guaranteed to converge to the optimal Q-function for the behavior policy under certain conditions (e.g., all state-action pairs are visited infinitely often, and the learning rate decays appropriately). If the behavior policy converges to a greedy policy, then SARSA will converge to the optimal Q-function.

## Algorithm (Tabular SARSA)
1.  Initialize a Q-table $Q(s,a)$ for all state-action pairs.
2.  For each episode:
    a.  Initialize state $s$.
    b.  Choose action $a$ from state $s$ using an [[RL_Exploration_vs_Exploitation|$\epsilon$-greedy policy]] (or another behavior policy).
    c.  Repeat for each step of the episode:
        i.   Take action $a$, observe reward $r$ and new state $s'$.
        ii.  Choose **next action $a'$** from state $s'$ using the *same behavior policy*.
        iii. Update Q-value: $Q(s,a) \leftarrow Q(s,a) + \alpha [r + \gamma Q(s', a') - Q(s,a)]$.
        iv.  Set $s \leftarrow s'$, $a \leftarrow a'$.
    d.  Until $s$ is a terminal state.

## Example: Cliff Walking (Conceptual)
-   **Scenario:** An agent navigates a grid world. Some cells are "cliffs" which give a large negative reward and end the episode. The goal is to reach a target cell.
-   **SARSA vs. Q-Learning:**
    -   **Q-Learning (off-policy):** Might learn a path that goes very close to the cliff edge if that path is theoretically shorter, even if the behavior policy sometimes falls off due to exploration. It learns the *optimal greedy path*.
    -   **SARSA (on-policy):** If the agent's $\epsilon$-greedy policy sometimes makes it fall off the cliff (due to exploration), SARSA will learn to value paths that are *safer* (further from the cliff edge) because the $Q(s',a')$ term in its update will reflect the negative consequences of its *actual* exploratory actions. It learns the *optimal path for its exploratory policy*.

## SARSA vs. Q-Learning
See [[RL_Q_Learning#Q-Learning vs. SARSA|Q-Learning vs. SARSA]] for a detailed comparison. In summary, SARSA is on-policy and learns a policy that accounts for its own exploration, making it more conservative or "safer" in environments with penalties. Q-Learning is off-policy and learns the optimal greedy policy regardless of exploration.

## Limitations
-   **Tabular Representation:** Like Q-learning, tabular SARSA struggles with large or continuous state/action spaces. This is addressed by using neural networks as function approximators (e.g., Deep SARSA, though DQN is more common).
-   **Exploration:** Still faces the [[RL_Exploration_vs_Exploitation|exploration-exploitation trade-off]].
-   **Convergence Speed:** Can be slow to converge.

SARSA is a foundational algorithm in RL, providing an on-policy approach to learning optimal behaviors directly from interaction.

---