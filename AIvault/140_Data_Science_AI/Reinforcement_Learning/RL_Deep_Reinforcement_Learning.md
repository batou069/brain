---
tags:
  - reinforcement_learning
  - rl
  - deep_reinforcement_learning
  - drl
  - deep_learning
  - neural_networks
  - function_approximation
  - concept
aliases:
  - Deep Reinforcement Learning
  - DRL
related:
  - "[[140_Data_Science_AI/Reinforcement_Learning/_Reinforcement_Learning_MOC|_Reinforcement_Learning_MOC]]"
  - "[[Neural_Networks]]"
  - "[[RL_Q_Learning]]"
  - "[[RL_Policy_Gradient_Methods]]"
  - "[[RL_Universal_Value_Function_Approximator_UVFA]]"
worksheet:
  - WS_RL_1
date_created: 2025-09-10
---
# RL: Deep Reinforcement Learning (DRL)

## Definition
**Deep Reinforcement Learning (DRL)** is a subfield of Reinforcement Learning (RL) that combines the principles of RL with [[Neural_Networks|deep learning]]. In DRL, deep neural networks are used as **function approximators** to represent the [[RL_Policy|policy]], the [[RL_Value_Function|value function]], or the [[RL_Model_Based_vs_Model_Free|environment model]] of an [[RL_Agent|agent]].

This combination allows RL agents to learn directly from high-dimensional, raw sensory inputs (like pixels from images or raw audio) and to handle problems with very large or continuous state and action spaces, which were intractable for traditional tabular RL methods.

## Why Deep Learning for RL?
Traditional tabular RL algorithms (like basic [[RL_Q_Learning|Q-Learning]] or [[RL_SARSA|SARSA]]) require storing Q-values or state values for every possible state-action pair in a table. This becomes infeasible when:
-   **Large State Spaces:** The number of possible states is enormous (e.g., pixels in a video game, positions in a complex board game).
-   **Continuous State Spaces:** States are continuous (e.g., joint angles of a robot, velocity of a car).
-   **Continuous Action Spaces:** Actions are continuous (e.g., steering angle, motor torque).

Deep neural networks excel at **[[RL_Universal_Value_Function_Approximator_UVFA|function approximation]]** and **generalization**. They can learn complex, non-linear mappings from high-dimensional inputs to outputs, making them ideal for:
-   **Representing Value Functions:** A neural network can take a state (e.g., raw pixels) as input and output the Q-values for all possible actions in that state.
-   **Representing Policies:** A neural network can take a state as input and output the probabilities of taking each action (for stochastic policies) or directly output the optimal action (for deterministic policies).
-   **Representing Environment Models:** A neural network can learn to predict the next state and reward given the current state and action.

## Key DRL Algorithms and Concepts

[list2tab|#DRL Algorithms & Concepts]
- Deep Q-Networks (DQN)
    -   **Concept:** An extension of [[RL_Q_Learning|Q-Learning]] where a deep neural network (a "Q-network") is used to approximate the Q-function, $Q(s,a)$.
    -   **Innovations:** Introduced techniques like **experience replay** (storing and sampling past transitions) and **fixed Q-targets** (using a separate, older Q-network to calculate target values) to stabilize training.
    -   **Use Case:** Achieved human-level performance in many Atari games.
- Policy Gradient Methods
    -   **Concept:** Instead of learning a value function and deriving a policy, these methods directly learn a parameterized [[RL_Policy|policy]] function ($\pi(a|s; \theta)$) using gradient ascent on a measure of policy performance (the expected cumulative reward).
    -   **Examples:** REINFORCE, Actor-Critic methods (e.g., A2C, A3C, A2C, PPO, SAC).
    -   **Advantages:** Can handle continuous action spaces more naturally, can learn stochastic policies.
- Actor-Critic Methods
    -   **Concept:** Combine value-based (critic) and policy-based (actor) approaches.
    -   **Actor:** A neural network that learns the policy (what action to take).
    -   **Critic:** A neural network that learns the value function (how good a state or state-action pair is).
    -   The critic helps the actor learn by providing a low-variance estimate of the policy gradient.
    -   **Examples:** A2C (Advantage Actor-Critic), A3C (Asynchronous Advantage Actor-Critic), DDPG (Deep Deterministic Policy Gradient), SAC (Soft Actor-Critic), PPO (Proximal Policy Optimization).
- [[RL_Universal_Value_Function_Approximator_UVFA|Universal Value Function Approximator (UVFA)]]
    -   **Concept:** A single neural network that learns a value function conditioned on the desired goal, allowing generalization across multiple tasks.
- [[RL_Hindsight_Experience_Replay_HER|Hindsight Experience Replay (HER)]]
    -   **Concept:** A technique to improve sample efficiency in sparse reward environments by re-labeling failed experiences with achieved goals. Often used with UVFAs.
- [[RL_Monte_Carlo_Tree_Search|Monte-Carlo Tree Search (MCTS)]] with Deep Learning
    -   **Concept:** As seen in AlphaGo, deep neural networks (policy network and value network) can significantly enhance MCTS by guiding the search and evaluating states more effectively.
- [[RL_Adversarial_DRL|Adversarial Deep Reinforcement Learning]]
    -   **Concept:** Using Generative Adversarial Networks (GANs) or adversarial training techniques within RL, often for imitation learning or robust policy learning.

## Challenges in DRL
-   **Sample Efficiency:** DRL algorithms often require millions or billions of interactions with the environment, making them expensive for real-world applications.
-   **Exploration:** Effective exploration in high-dimensional state spaces remains a significant challenge. [[RL_Curiosity_Regret|Curiosity-driven exploration]] is an active research area.
-   **Instability:** Training deep neural networks in an RL setting can be unstable due to non-stationary targets, correlation in samples, and high variance in gradients.
-   **Hyperparameter Sensitivity:** DRL algorithms are often very sensitive to hyperparameter choices.
-   **Interpretability:** DRL policies are often black boxes.

## Applications of DRL
-   **Game Playing:** Achieved superhuman performance in Atari games (DQN), Go (AlphaGo), Chess (AlphaZero), StarCraft II.
-   **Robotics:** Learning complex manipulation tasks, locomotion, navigation.
-   **Autonomous Driving:** Learning driving policies, path planning, decision-making in traffic.
-   **Resource Management:** Optimizing data center cooling, energy management.
-   **Financial Trading:** Developing automated trading strategies.
-   **Drug Discovery:** Optimizing molecular structures.

DRL is a rapidly evolving field that has demonstrated remarkable successes in solving complex problems that were previously beyond the reach of traditional AI methods.

---