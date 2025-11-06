---
tags:
  - reinforcement_learning
  - rl
  - monte_carlo
  - model_free
  - policy_evaluation
  - control
  - concept
aliases:
  - Monte Carlo RL
  - MC Methods
related:
  - "[[140_Data_Science_AI/Reinforcement_Learning/_Reinforcement_Learning_MOC|_Reinforcement_Learning_MOC]]"
  - "[[RL_Temporal_Difference_Learning]]"
  - "[[RL_Policy]]"
  - "[[RL_Value_Function]]"
worksheet:
  - WS_RL_1
date_created: 2025-09-10
---
# RL: Monte Carlo Methods

## Definition
**Monte Carlo (MC) methods** in Reinforcement Learning (RL) are a class of algorithms that learn optimal [[RL_Policy|policies]] by averaging sample returns (cumulative [[RL_State_Action_Reward|rewards]]) from complete episodes of interaction with the [[RL_Environment|environment]]. They are **model-free** methods, meaning they do not require knowledge of the environment's dynamics (transition probabilities or reward function).

The core idea is to learn from *experience* by running many episodes and observing the actual outcomes.

## Key Characteristics
-   **Learning from Complete Episodes:** MC methods only update value estimates *after* an entire episode has completed. An episode starts from an initial state and ends in a terminal state.
-   **Model-Free:** They do not need a model of the environment. They learn directly from samples of experience.
-   **Averaging Returns:** Value estimates (e.g., for states or state-action pairs) are updated by averaging the actual returns (total discounted rewards) observed following visits to those states or state-action pairs.
-   **No Bootstrapping:** Unlike [[RL_Temporal_Difference_Learning|Temporal Difference (TD) learning]], MC methods do not "bootstrap" (they do not update estimates based on other estimates). They rely solely on actual, observed returns.

## Monte Carlo Policy Evaluation
-   **Purpose:** To estimate the value function ($V(s)$ for states or $Q(s,a)$ for state-action pairs) for a given [[RL_Policy|policy]] $\pi$.
-   **How it Works:**
    1.  Generate many episodes by following policy $\pi$.
    2.  For each state $s$ (or state-action pair $(s,a)$) visited in an episode:
        -   Calculate the **return** (total discounted reward) $G_t$ from that point onwards until the end of the episode.
        -   Update the estimate $V(s)$ (or $Q(s,a)$) by averaging all observed returns for that state (or state-action pair).
    -   **First-Visit MC:** Averages returns only for the *first time* a state is visited in an episode.
    -   **Every-Visit MC:** Averages returns for *every time* a state is visited in an episode.

## Monte Carlo Control
-   **Purpose:** To find an optimal [[RL_Policy|policy]] ($\pi^*$) that maximizes the expected cumulative reward.
-   **Approach:** Often uses a generalized policy iteration (GPI) approach, alternating between policy evaluation and policy improvement.
    1.  **Policy Evaluation:** Estimate $Q(s,a)$ for the current policy $\pi$ using MC methods.
    2.  **Policy Improvement:** Update the policy $\pi$ to be greedy with respect to the current $Q(s,a)$ estimates.
-   **Exploration:** Since MC methods learn from experience, they need to ensure sufficient [[RL_Exploration_vs_Exploitation|exploration]]. Common techniques include:
    -   **$\epsilon$-Greedy Policies:** The agent acts greedily most of the time but takes a random action with probability $\epsilon$.
    -   **Exploring Starts:** Ensuring that every state-action pair has a non-zero probability of being the starting point of an episode.
-   **On-Policy vs. Off-Policy:**
    -   **On-Policy MC Control:** Learns the value of the policy being followed (e.g., MC $\epsilon$-greedy control).
    -   **Off-Policy MC Control:** Learns the value of an optimal policy while following a different, more exploratory behavior policy (e.g., using importance sampling).

## Advantages of Monte Carlo Methods
-   **Model-Free:** No need to learn or estimate the environment's dynamics. Can be used in complex environments where a model is unavailable or too difficult to learn.
-   **Directly from Experience:** Learns directly from actual interactions, which can be robust to violations of the Markov property (though still assumes episodic tasks).
-   **Handles Non-Markovian Tasks:** Can be applied to tasks where the state is not fully observable (partially observable Markov decision processes - POMDPs) by learning from histories of observations.
-   **No Bootstrapping:** Avoids potential issues with bootstrapping (e.g., bias from using potentially inaccurate estimates to update other estimates).

## Disadvantages of Monte Carlo Methods
-   **Requires Complete Episodes:** Updates only occur at the end of an episode. This can be slow for long episodes or if episodes are rare.
-   **High Variance:** Returns from single episodes can be noisy, leading to high variance in value estimates. Averaging over many episodes is necessary.
-   **Inefficient for Continuous Tasks:** Not directly applicable to continuous tasks (where there are no terminal states) unless truncated.
-   **Exploration Challenge:** Ensuring all state-action pairs are sufficiently explored can be difficult.

## Example: Blackjack (Conceptual)
-   **Agent:** Player.
-   **Environment:** Blackjack game.
-   **State:** Player's hand, dealer's upcard.
-   **Actions:** Hit, Stand.
-   **Rewards:** +1 for win, -1 for loss, 0 for draw.
-   **MC Application:** The agent plays many hands (episodes). After each hand, it looks back at the states and actions it took and updates its Q-values by averaging the actual winnings/losses from those points. For example, if it was in state (Player Hand=18, Dealer Upcard=7) and chose "Stand" and won, it would update $Q(\text{18, 7, Stand})$.

Monte Carlo methods are foundational in RL, providing a clear, model-free way to learn from complete experiences, particularly useful in episodic tasks.

---