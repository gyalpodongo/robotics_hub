# Sim-to-Real & Transfer

Sim-to-real transfer bridges the gap between simulated training environments and physical robots, enabling sample-efficient learning and safe policy development. Recent advances leverage photorealistic rendering, domain randomization, and learned dynamics models to minimize the reality gap.

## What is Sim-to-Real?

Sim-to-real transfer trains policies in simulation where data collection is cheap, fast, and safe, then deploys them on real robots. Successful transfer requires handling differences in physics, sensors, and environment dynamics between simulation and reality.

## Key Approaches

### Digital Twins
**Real-is-Sim** creates dynamic digital twins of real environments using 3D Gaussian Splatting, enabling high-fidelity simulation that closely matches reality for robust policy transfer.

### Domain Randomization
**RoboGen** uses procedural generation to create infinite variations of tasks, objects, and environments in simulation, training policies robust to real-world variation.

### Video-to-Reality
**Dreamitate** learns from human videos and translates them into simulation, then trains policies that transfer to real robots, leveraging internet-scale human demonstration data.

### Affordance Transfer
Learning affordances (actionable properties) from human videos as a versatile representation for cross-embodiment transfer between humans and robots.

## Important Considerations

- **Physics fidelity**: Accurate simulation of contact, friction, and dynamics is critical
- **Sensor realism**: Matching camera properties, noise characteristics, and failure modes
- **Latency modeling**: Accounting for control delays and communication lags
- **Domain randomization**: Balancing randomization breadth with policy learning difficulty
- **Real-world validation**: Extensive testing on physical robots to verify transfer success

## Notable Methods

- **Real-is-Sim**: Gaussian splatting-based digital twins
- **RoboGen**: Procedural generation for infinite task diversity
- **Dreamitate**: Learning from human videos via video generation
- **Isaac Gym**: GPU-accelerated parallel simulation for RL


---

## 📄 Papers in This Domain

| Paper | PDF | Date | GitHub | Stars | Citations | Twitter | Summary |
|-------|-----|------|--------|-------|-----------|---------|----------|
| [Real-is-Sim: Bridging the Sim-to-Real Ga...](../papers/2504.03597.md) | [2504.03597](https://arxiv.org/abs/2504.03597) | 2025-04-04 | - | - | - | - | We introduce real-is-sim, a new approach to integrating simulation into behavior cloning pipelines. |
| [RoboGen: Towards Unleashing Infinite Dat...](../papers/2311.01455.md) | [2311.01455](https://arxiv.org/abs/2311.01455) | 2023-11-02 | [repo](https://github.com/robogen-ai/robogen) | - | - | - | We present RoboGen, a generative robotic agent that automatically learns diverse robotic skills a... |
| [Affordances from Human Videos as a Versa...](../papers/2304.08488.md) | [2304.08488](https://arxiv.org/abs/2304.08488) | 2023-04-17 | - | - | - | - | Building a robot that can understand and learn to interact by watching humans has inspired severa... |
| [Dreamitate: Real-World Visuomotor Policy...](../papers/2406.16862.md) | [2406.16862](https://arxiv.org/abs/2406.16862) | 2024-06-24 | - | - | [49](https://www.semanticscholar.org/paper/b0ac4f62f55bcf0427008e18f1b4b5bf7ee43df2) (📈3) | - | A key challenge in manipulation is learning a policy that can robustly generalize to diverse visu... |


---

*This page is automatically updated with the latest research. Last updated: 2025-11-14 00:10 UTC*
