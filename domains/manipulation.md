# Manipulation & Grasping

Robotic manipulation encompasses grasping, placing, pushing, and contact-rich interactions with objects. Recent advances combine learning-based approaches with geometric reasoning, enabling robots to manipulate diverse objects in cluttered, unstructured environments.

## What is Robotic Manipulation?

Manipulation involves controlling a robot arm or gripper to interact with objects, requiring coordination of perception (where is the object?), planning (how to grasp it?), and control (execute the motion). Modern approaches increasingly rely on learned policies from demonstrations or reinforcement learning.

## Key Approaches

### Language-Conditioned Manipulation
**VoxPoser** uses LLMs to generate 3D value maps for manipulation, enabling zero-shot generalization to novel objects and instructions by composing geometric affordances with language understanding.

### Contact-Rich Manipulation
**Adaptive Compliance Policy** learns approximate compliance for diffusion-based manipulation, handling contact-rich tasks like insertion and assembly without explicit force control.

### 6-DoF Grasping
**CoGrasp** generates 6-DoF grasps for human-robot collaboration, enabling cooperative manipulation where humans and robots jointly manipulate objects.

### Pose Estimation
**FoundationPose** provides unified 6D pose estimation and tracking for novel objects without CAD models, essential for manipulation in the wild.

## Important Considerations

- **Grasp stability**: Ensuring reliable grasps under object uncertainty and dynamics
- **Contact modeling**: Handling friction, slipping, and multi-contact interactions
- **Object diversity**: Generalizing to novel object geometries, materials, and weights
- **Clutter handling**: Manipulating objects in cluttered scenes with occlusions
- **Dynamic manipulation**: Performing non-prehensile actions like pushing, throwing

## Notable Methods

- **VoxPoser**: LLM-guided 3D value maps for manipulation
- **Adaptive Compliance Policy**: Learning compliance for contact-rich tasks
- **FoundationPose**: Model-free 6D pose estimation
- **CoGrasp**: Human-robot collaborative 6-DoF grasping


---

## 📄 Papers in This Domain

| Paper | PDF | Date | GitHub | Stars | Citations | Twitter | Summary |
|-------|-----|------|--------|-------|-----------|---------|----------|
| [VoxPoser: Composable 3D Value Maps for R...](../papers/2307.05973.md) | [2307.05973](https://arxiv.org/abs/2307.05973) | 2023-07-12 | - | - | [674](https://www.semanticscholar.org/paper/1cd8373490efc2d74c2796f4b2aa27c7d4415ec9) (📈54) | - | Large language models (LLMs) are shown to possess a wealth of actionable knowledge that can be ex... |
| [RUKA: Rethinking the Design of Humanoid ...](../papers/2504.13165.md) | [2504.13165](https://arxiv.org/abs/2504.13165) | 2025-04-17 | [repo](https://github.com/ruka-hand/RUKA) | 153 | - | [❤️445 🔄100](https://x.com/irmakkguzey/status/1913276064287305730)<br>👁️109,358 | Dexterous manipulation is a fundamental capability for robotic systems, yet progress has been lim... |
| [Adaptive Compliance Policy: Learning App...](../papers/2410.09309.md) | [2410.09309](https://arxiv.org/abs/2410.09309) | 2024-10-12 | [repo](https://github.com/yifan-hou/adaptive_compliance_policy) | 92 | - | - | Compliance plays a crucial role in manipulation, as it balances between the concurrent control of... |
| [CoGrasp: 6-DoF Grasp Generation for Huma...](../papers/2210.03173.md) | [2210.03173](https://arxiv.org/abs/2210.03173) | 2022-10-06 | - | - | - | - | Robot grasping is an actively studied area in robotics, mainly focusing on the quality of generat... |


---

*This page is automatically updated with the latest research. Last updated: 2025-11-14 00:10 UTC*
