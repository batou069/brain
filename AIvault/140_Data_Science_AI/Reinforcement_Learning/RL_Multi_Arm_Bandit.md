---
tags:
  - reinforcement_learning
  - rl
  - multi_arm_bandit
  - mab
  - exploration
  - exploitation
  - concept
aliases:
  - Multi-Arm Bandit
  - MAB Problem
related:
  - "[[140_Data_Science_AI/Reinforcement_Learning/_Reinforcement_Learning_MOC|_Reinforcement_Learning_MOC]]"
  - "[[RL_Exploration_vs_Exploitation]]"
  - "[[RL_Regret]]"
worksheet:
  - WS_RL_1
date_created: 2025-09-10
---
# RL: Multi-Arm Bandit (MAB)

## Definition
The **Multi-Arm Bandit (MAB)** problem is a classic problem in Reinforcement Learning (RL) and decision theory that serves as a simplified model for the [[RL_Exploration_vs_Exploitation|exploration-exploitation trade-off]].

Imagine a gambler facing a row of slot machines (one-armed bandits), each with a different, unknown probability distribution of payouts. The gambler's goal is to maximize their total winnings over a series of plays. At each turn, the gambler must decide which machine (arm) to play.

-   **Arms:** The available actions (e.g., different slot machines, different ad campaigns, different drug treatments).
-   **Payouts (Rewards):** The feedback received after playing an arm (e.g., money won, click-through rate, patient recovery). These are typically stochastic.
-   **Goal:** Maximize the cumulative reward over a sequence of plays.

The challenge is that the gambler doesn't know the true payout probabilities of each machine. They must **explore** different machines to learn their payout rates, but also **exploit** the machine that currently appears to be the best.

## Key Characteristics
-   **Single State:** Unlike full RL problems, MABs typically involve a single state. The agent's decision at each step does not change the "state" of the environment in a way that affects future decisions beyond updating the agent's knowledge about the arms.
-   **Immediate Rewards:** Rewards are received immediately after an action (playing an arm). There are no [[RL_State_Action_Reward|delayed rewards]].
-   **No Sequential Dynamics:** The environment does not have complex dynamics or transitions between states.
-   **Focus on Exploration-Exploitation:** The MAB problem is a pure distillation of this fundamental dilemma.

## Strategies for Solving MAB Problems
The strategies for balancing exploration and exploitation, as discussed in [[RL_Exploration_vs_Exploitation]], are primarily developed and studied in the context of MABs.

1.  **$\epsilon$-Greedy:**
    -   Play the best-known arm with probability $1-\epsilon$.
    -   Play a random arm with probability $\epsilon$.
    -   $\epsilon$ can be constant or decay over time.
2.  **Upper Confidence Bound (UCB):**
    -   Selects the arm that maximizes an optimistic estimate of its value, which includes both its current estimated reward and a term that quantifies the uncertainty (or how little it has been explored).
3.  **Thompson Sampling:**
    -   A Bayesian approach that maintains a probability distribution over the expected reward of each arm. In each step, it samples from these distributions and plays the arm with the highest sampled value.
4.  **Softmax Action Selection:**
    -   Chooses arms probabilistically based on their estimated values, with higher-value arms having a higher probability of being chosen.

## Example Use Cases
-   **A/B Testing / Online Experimentation:**
    -   **Scenario:** An e-commerce website has multiple versions of an ad banner, a product recommendation algorithm, or a website layout. Which version is best for maximizing clicks, conversions, or engagement?
    -   **MAB Application:** Each version is an "arm." Playing an arm means showing that version to a user. The reward is a click/conversion. MAB algorithms can dynamically allocate traffic to better-performing versions while still exploring suboptimal ones, leading to faster optimization than traditional A/B testing.
-   **Clinical Trials:**
    -   **Scenario:** A pharmaceutical company is testing several experimental drugs for a disease. Which drug is most effective?
    -   **MAB Application:** Each drug is an "arm." The reward is patient recovery or improvement. MAB algorithms can adaptively assign more patients to better-performing drugs, minimizing harm to patients while still learning about all drugs.
-   **News Article Recommendation:**
    -   **Scenario:** A news app wants to show users articles they are most likely to click on.
    -   **MAB Application:** Each article is an "arm." The reward is a click. The challenge is that articles become "stale" (their value changes over time), making it a non-stationary MAB.
-   **Dynamic Pricing:**
    -   **Scenario:** An online retailer wants to find the optimal price for a product.
    -   **MAB Application:** Each price point is an "arm." The reward is revenue.

## MAB vs. Full Reinforcement Learning
-   **MAB:** Focuses purely on action selection in a single state to maximize immediate or cumulative reward. No complex state transitions or long-term planning.
-   **Full RL:** Involves multiple states, state transitions, and the agent must learn a policy to navigate these states to maximize *delayed* cumulative rewards. MABs can be seen as a special case of RL with only one state.

The MAB problem is a foundational concept that helps understand and develop strategies for the exploration-exploitation trade-off, which is central to all of Reinforcement Learning.

---