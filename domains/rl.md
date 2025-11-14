# Reinforcement Learning

Reinforcement Learning (RL) enables robots to learn behaviors through trial-and-error interaction with their environment, guided by reward signals. Recent breakthroughs combine RL with large language models (LLMs) for automated reward design and open-ended exploration, dramatically accelerating robot learning.

## What is Robot RL?

Robot RL trains policies to maximize cumulative reward by exploring the environment and learning from feedback. Unlike imitation learning which requires expert demonstrations, RL can discover novel strategies and optimize for task success beyond human capabilities.

## Key Approaches

### LLM-Guided Reward Design
**Eureka** uses LLMs to automatically write reward functions as executable code, achieving human-level reward design without manual engineering. This breakthrough enables rapid prototyping of RL tasks.

### Open-Ended Exploration
**Voyager** creates a lifelong learning agent in Minecraft that autonomously discovers skills, stores them as code, and composes them for complex tasks using LLMs as a high-level planner.

### Diffusion RL
Methods like **DPPO** combine diffusion models' expressiveness with RL's ability to optimize for task success, enabling fine-tuning of pre-trained diffusion policies via reinforcement learning.

### Offline RL
Learning from fixed datasets of sub-optimal demonstrations without environment interaction, crucial for real-world robots where exploration is expensive or dangerous.

## Important Considerations

- **Sample efficiency**: RL typically requires millions of environment steps; simulation is essential
- **Reward engineering**: Designing reward functions that capture task intent without unintended behaviors
- **Sim-to-real transfer**: Policies trained in simulation must transfer robustly to real hardware
- **Safety**: Exploration must respect safety constraints to avoid damaging robots or environments
- **Credit assignment**: Determining which actions led to rewards in long-horizon tasks

## Notable Methods

- **Eureka**: LLM-powered automated reward design
- **Voyager**: Open-ended lifelong learning agent with skill library
- **DPPO**: Diffusion policy optimization via PPO
- **SAC/TD3**: State-of-the-art model-free RL algorithms for continuous control


---

## 📄 Papers in This Domain

| Paper | PDF | Date | GitHub | Stars | Citations | Twitter | Summary |
|-------|-----|------|--------|-------|-----------|---------|----------|
| [A Survey of Reinforcement Learning for L...](../papers/2509.08827.md) | [2509.08827](https://arxiv.org/abs/2509.08827) | 2025-09-10 | [repo](https://github.com/TsinghuaC3I/Awesome-RL-for-LRMs) | 2,036 | - | - | In this paper, we survey recent advances in Reinforcement Learning (RL) for reasoning with Large ... |
| [Voyager: An Open-Ended Embodied Agent wi...](../papers/2305.16291.md) | [2305.16291](https://arxiv.org/abs/2305.16291) | 2023-05-25 | [repo](https://github.com/MineDojo/Voyager) | 6,454 | - | - | We introduce Voyager, the first LLM-powered embodied lifelong learning agent in Minecraft that co... |
| [Eureka: Human-Level Reward Design via Co...](../papers/2310.12931.md) | [2310.12931](https://arxiv.org/abs/2310.12931) | 2023-10-19 | [repo](https://github.com/eureka-research/Eureka) | 3,062 | [429](https://www.semanticscholar.org/paper/6ca16c1c2c60ceda87242c8f8e522d12cc4a13bc) (📈51) | - | Large Language Models (LLMs) have excelled as high-level semantic planners for sequential decisio... |
| [Training Diffusion Models with Reinforce...](../papers/2305.13301.md) | [2305.13301](https://arxiv.org/abs/2305.13301) | 2023-05-22 | [repo](https://github.com/jannerm/ddpo) | 529 | - | [❤️823 🔄177](https://x.com/svlevine/status/1660707076946141184)<br>👁️129,377 | Diffusion models are a class of flexible generative models trained with an approximation to the l... |
| [Diffusion Policy Policy Optimization](../papers/2409.00588.md) | [2409.00588](https://arxiv.org/abs/2409.00588) | 2024-09-01 | [repo](https://github.com/irom-princeton/dppo) | 681 | [109](https://www.semanticscholar.org/paper/e596c98260ec4096eaeb491eb75f91a8339fcf48) (📈16) | [❤️476 🔄93](https://x.com/allenzren/status/1831403337528570132)<br>👁️76,173 | We introduce Diffusion Policy Policy Optimization, DPPO, an algorithmic framework including best ... |


---

*This page is automatically updated with the latest research. Last updated: 2025-11-14 00:10 UTC*
