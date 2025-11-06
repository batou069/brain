### What is Sample Efficiency in Reinforcement Learning?

**Sample efficiency** refers to how well a reinforcement learning (RL) algorithm learns from a limited number of experiences or interactions with the environment. It measures how effectively the algorithm extracts useful information from each data point (or sample) it collects while trying to solve a task.

- A **high sample efficiency** means the agent learns a good policy after few interactions.
- A **low sample efficiency** means the agent requires many environment interactions, which can be time-consuming, costly, or impractical in real-life scenarios (e.g., robotics or expensive simulations).

---

### Why Does Relabeling Failed Experiences as Successful Ones Boost Sample Efficiency?

In some RL tasks, especially **sparse reward environments**, the agent rarely receives positive feedback (rewards), so many collected samples provide little useful learning signal. This makes learning inefficient and slow.

**Hindsight Experience Replay (HER)** is a technique that addresses this by **relabeling failed trajectories as successful** for alternative goals that the agent accidentally achieved. For example, if the agent intended to reach goal A but instead reached goal B, HER treats the experience as if goal B was the target.

- This effectively **creates additional meaningful training samples** from the same data because the agent learns from both successes and failures (viewed from different goals).
- By augmenting the data this way, the agent can learn useful behaviors faster without needing more environment interactions.
- This **boosts sample efficiency** because each interaction yields more informative learning opportunities.

---

### Intuitive Example

Imagine trying to pick fruits from different trees. Suppose the goal was to pick apple from tree A but ended up picking a pear from tree B. Instead of discarding this attempt as failure, HER would consider the pear-picking successful for goal B — so you learn from the experience even if it didn't achieve the original goal. This way, you gain knowledge from every action you take, reducing wasted effort.

---

### Summary

- **Sample efficiency** is crucial for reducing training time and costs in RL.
- Relabeling failed experiences as successful ones for different goals increases the amount of *useful* data extracted from each interaction.
- This leads to faster learning with fewer environment samples, especially valuable in tasks with sparse rewards or expensive data collection.

[web:58][web:59][web:63][web:64]
```
