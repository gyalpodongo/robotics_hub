# Policy Learning Methods

Policy learning methods form the algorithmic backbone of modern robot learning, determining how robots map observations to actions. Recent advances focus on leveraging powerful generative models, particularly diffusion models, to learn complex multimodal action distributions directly from demonstrations.

## What are Policy Learning Methods?

Policy learning methods define how robots learn to perform tasks from data. Unlike traditional control approaches that rely on hand-crafted controllers, learning-based policies automatically discover effective behaviors from demonstrations (imitation learning) or trial-and-error (reinforcement learning).

## Key Approaches

### Diffusion Policies
**Diffusion Policy** treats action generation as a denoising process, learning to iteratively refine noisy actions into precise trajectories. This approach naturally handles multimodal action distributions and achieves state-of-the-art performance on complex visuomotor tasks.

### 3D Representation Learning
Methods like **3D Diffusion Policy** and **3D Diffuser Actor** leverage 3D scene representations (point clouds, voxels) for better spatial reasoning and view-invariant manipulation.

### Consistency Models
**Consistency Policy** accelerates diffusion-based policies by enabling single-step inference, achieving 10x speedup while maintaining performance for real-time robot control.

### Equivariant Policies
**EquiBot** exploits SE(3) symmetries in manipulation tasks, enabling data-efficient learning and better generalization across object poses and camera viewpoints.

### Autoregressive Methods
**ARP (Autoregressive Policy)** models actions as sequential decisions with action chunking, improving temporal consistency in long-horizon tasks.

## Important Considerations

- **Action representation**: Choice of action space (absolute vs. relative, position vs. velocity) significantly impacts performance
- **Temporal consistency**: Policies must generate smooth, dynamically feasible trajectories
- **Multi-modality**: Real-world tasks often have multiple valid solutions; policies should capture this diversity
- **Sample efficiency**: Reducing the number of demonstrations needed remains a key challenge
- **Real-time inference**: Policies must run at control frequencies (10-30 Hz) for reactive behaviors

## Notable Methods

- **Diffusion Policy**: State-of-the-art visuomotor policy using denoising diffusion
- **3D Diffusion Policy**: 3D-aware diffusion for view-invariant manipulation
- **Consistency Policy**: Real-time diffusion policy with single-step inference
- **DPPO**: Combining diffusion models with reinforcement learning via PPO


---

## 📄 Papers in This Domain

| Paper | PDF | Date | GitHub | Stars | Citations | Twitter | Summary |
|-------|-----|------|--------|-------|-----------|---------|----------|
| [DNAct: Diffusion Guided Multi-Task 3D Po...](../papers/2403.04115.md) | [2403.04115](https://arxiv.org/abs/2403.04115) | 2024-03-07 | - | - | - | [❤️88 🔄19](https://x.com/GeYan_21/status/1766323088562786624)<br>👁️28,802 | This paper presents DNAct, a language-conditioned multi-task policy framework that integrates neu... |
| [Diffusion Policy: Visuomotor Policy Lear...](../papers/2303.04137.md) | [2303.04137](https://arxiv.org/abs/2303.04137) | 2023-03-07 | [repo](https://github.com/real-stanford/diffusion_policy) | 3,338 | - | [❤️534 🔄101](https://x.com/chichengcc/status/1633339455250526213)<br>👁️129,017 | This paper introduces Diffusion Policy, a new way of generating robot behavior by representing a ... |
| [3D Diffusion Policy: Generalizable Visuo...](../papers/2403.03954.md) | [2403.03954](https://arxiv.org/abs/2403.03954) | 2024-03-06 | [repo](https://github.com/YanjieZe/3D-Diffusion-Policy) | 1,121 | - | [❤️299 🔄58](https://x.com/ZeYanjie/status/1765414787775963232)<br>👁️96,877 | Imitation learning provides an efficient way to teach robots dexterous skills; however, learning ... |
| [Autoregressive Action Sequence Learning ...](../papers/2410.03132.md) | [2410.03132](https://arxiv.org/abs/2410.03132) | 2024-10-04 | [repo](https://github.com/mlzxy/arp) | 142 | - | - | Designing a universal policy architecture that performs well across diverse robots and task confi... |
| [Sparse Diffusion Policy: A Sparse, Reusa...](../papers/2407.01531.md) | [2407.01531](https://arxiv.org/abs/2407.01531) | 2024-07-01 | [repo](https://github.com/AnthonyHuo/SDP) | 71 | - | - | The increasing complexity of tasks in robotics demands efficient strategies for multitask and con... |
| [EquiBot: SIM(3)-Equivariant Diffusion Po...](../papers/2407.01479.md) | [2407.01479](https://arxiv.org/abs/2407.01479) | 2024-07-01 | [repo](https://github.com/yjy0625/equibot) | 160 | - | [❤️324 🔄76](https://x.com/yjy0625/status/1808550937885356448)<br>👁️87,804 | Building effective imitation learning methods that enable robots to learn from limited data and s... |
| [Training Diffusion Models with Reinforce...](../papers/2305.13301.md) | [2305.13301](https://arxiv.org/abs/2305.13301) | 2023-05-22 | [repo](https://github.com/jannerm/ddpo) | 529 | - | [❤️823 🔄177](https://x.com/svlevine/status/1660707076946141184)<br>👁️129,377 | Diffusion models are a class of flexible generative models trained with an approximation to the l... |
| [3D Diffuser Actor: Policy Diffusion with...](../papers/2402.10885.md) | [2402.10885](https://arxiv.org/abs/2402.10885) | 2024-02-16 | [repo](https://github.com/nickgkan/3d_diffuser_actor) | 367 | [208](https://www.semanticscholar.org/paper/97fc977b8d167ff648c5c6672aea4d05f98fd79e) (📈35) | [❤️45 🔄11](https://x.com/nikos_gkanats/status/1759679687520100619)<br>👁️4,696 | Diffusion policies are conditional diffusion models that learn robot action distributions conditi... |
| [Diffusion Policy Policy Optimization](../papers/2409.00588.md) | [2409.00588](https://arxiv.org/abs/2409.00588) | 2024-09-01 | [repo](https://github.com/irom-princeton/dppo) | 681 | [109](https://www.semanticscholar.org/paper/e596c98260ec4096eaeb491eb75f91a8339fcf48) (📈16) | [❤️476 🔄93](https://x.com/allenzren/status/1831403337528570132)<br>👁️76,173 | We introduce Diffusion Policy Policy Optimization, DPPO, an algorithmic framework including best ... |
| [Consistency Policy: Accelerated Visuomot...](../papers/2405.07503.md) | [2405.07503](https://arxiv.org/abs/2405.07503) | 2024-05-13 | [repo](https://github.com/Aaditya-Prasad/Consistency-Policy) | 189 | [89](https://www.semanticscholar.org/paper/289906e335e367d363bc2e99d1c04037da7afbf2) (📈11) | [❤️291 🔄61](https://x.com/_Aaditya_Prasad/status/1790501613653917782)<br>👁️78,723 | Many robotic systems, such as mobile manipulators or quadrotors, cannot be equipped with high-end... |


---

*This page is automatically updated with the latest research. Last updated: 2025-11-14 00:10 UTC*
