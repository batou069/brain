---
tags:
  - reinforcement_learning
  - rl
  - machine_learning
  - ai
  - agent
  - environment
  - policy
  - moc
  - concept
aliases:
  - Reinforcement Learning MOC
  - RL MOC
related:
  - "[[_Data_Science_AI_MOC]]"
  - "[[_Machine_Learning_MOC]]"
  - "[[Supervised_Learning]]"
  - "[[Unsupervised_Learning]]"
worksheet:
  - WS_RL_1
date_created: 2025-09-10
---
# Reinforcement Learning MOC 🤖🎮

**Reinforcement Learning (RL)** is a paradigm of machine learning where an **[[RL_Agent|agent]]** learns to make decisions by performing actions in an **[[RL_Environment|environment]]** to maximize a cumulative reward. Unlike supervised learning (which learns from labeled data) or unsupervised learning (which finds patterns in unlabeled data), RL learns through trial and error, receiving feedback in the form of rewards or penalties.

## Core Concepts
-   [[RL_Agent_Environment|Agent and Environment]]
-   [[RL_State_Action_Reward|State, Action, Reward]]
-   [[RL_Policy|Policy (on-policy vs. off-policy)]]
-   [[RL_Exploration_vs_Exploitation|Exploration vs. Exploitation Trade-off]]
-   [[RL_Curiosity_Regret|Curiosity and Regret]]
-   [[RL_When_to_Choose_RL|When to Choose RL over Supervised/Unsupervised Learning]]
-   [[RL_Limitations|Limitations of Reinforcement Learning]]
-   [[RL_Algorithm_Selection_Criteria|Criteria for Choosing an RL Algorithm]]

## Learning Paradigms & Algorithms
-   [[RL_Multi_Arm_Bandit|Multi-Arm Bandit (MAB)]]
-   [[RL_Monte_Carlo_Methods|Monte Carlo Methods]]
-   [[RL_Temporal_Difference_Learning|Temporal Difference (TD) Learning]]
    -   [[RL_Q_Learning|Q-Learning]]
    -   [[RL_SARSA|SARSA]]
-   [[RL_Model_Based_vs_Model_Free|Model-Based vs. Model-Free RL]]
-   [[RL_Policy_Gradient_Methods|Policy Gradient Methods]] # Placeholder
-   [[RL_Actor_Critic_Methods|Actor-Critic Methods]] # Placeholder

## Advanced Topics & Extensions
-   [[RL_Deep_Reinforcement_Learning|Deep Reinforcement Learning (DRL)]]
    -   [[RL_Universal_Value_Function_Approximator_UVFA|Universal Value Function Approximator (UVFA)]]
    -   [[RL_Hindsight_Experience_Replay_HER|Hindsight Experience Replay (HER)]]
-   [[RL_Monte_Carlo_Tree_Search|Monte-Carlo Tree Search (MCTS)]]
-   [[RL_Experience_Memory|Experience and Memory in RL]]
-   [[RL_Multi_Agent_RL|Multi-Agent Reinforcement Learning (MARL)]]
-   [[RL_Adversarial_DRL|Adversarial Deep Reinforcement Learning]]
-   [[RL_Curiosity_Driven_Exploration|Curiosity-Driven Exploration]]

## Notes in this Section
```dataview
LIST
FROM "140_Data_Science_AI/Reinforcement_Learning"
WHERE file.folder = this.file.folder AND file.name != this.file.name AND !contains(file.name, "MOC")
SORT file.name ASC
```

---