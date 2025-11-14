# Data Collection & Teleoperation

Data collection is the foundation of modern robot learning. High-quality, diverse datasets enable robots to learn complex behaviors through imitation learning, reinforcement learning, and other data-driven approaches. Recent innovations focus on scalable, low-cost teleoperation systems that allow humans to efficiently provide demonstrations.

## What is Robot Data Collection?

Robot data collection involves capturing demonstrations, teleoperation sequences, or autonomous exploration data that captures the relationship between sensory inputs (vision, proprioception, force/torque) and robot actions. This data serves as the training material for robot learning algorithms.

## Key Methods

### Portable Teleoperation
**UMI (Universal Manipulation Interface)** uses hand-held grippers with wide-FoV cameras for portable, "in-the-wild" data collection. Its hardware-agnostic design enables deployment across diverse environments without lab infrastructure.

### VR-Based Teleoperation
**XRoboToolkit** provides cross-platform frameworks for immersive teleoperation using VR headsets, enabling intuitive 6-DoF control for bimanual manipulation.

### Dexterous Data Collection
**DexUMI** extends UMI to dexterous manipulation using the human hand as a universal interface, capturing fine-grained finger motions for learning complex hand behaviors.

### Interactive Learning
**RoboCopilot** combines teleoperation with interactive imitation learning, allowing humans to provide real-time corrective feedback to improve policies during data collection.

## Important Considerations

- **Data diversity**: Varied environments, objects, and scenarios improve generalization
- **Data quality**: Clean labels, accurate timestamps, and synchronized sensors are critical
- **Data scale**: Larger datasets generally lead to better performance (100k+ demonstrations)
- **Data efficiency**: Techniques to learn from limited demonstrations reduce collection burden
- **Safety**: Ensuring safe data collection without damaging robots or environments

## Notable Systems

- **UMI**: Portable hand-held gripper system for in-the-wild data collection
- **DexUMI**: Dexterous manipulation data collection using human hands
- **XRoboToolkit**: VR-based teleoperation framework
- **ALOHA**: Low-cost bimanual teleoperation system


---

## 📄 Papers in This Domain

| Paper | PDF | Date | GitHub | Stars | Citations | Twitter | Summary |
|-------|-----|------|--------|-------|-----------|---------|----------|
| [XRoboToolkit: A Cross-Platform Framework...](../papers/2508.00097.md) | [2508.00097](https://arxiv.org/abs/2508.00097) | 2025-07-31 | - | - | - | - | The rapid advancement of Vision-Language-Action models has created an urgent need for large-scale... |
| [DexUMI: Using Human Hand as the Universa...](../papers/2505.21864.md) | [2505.21864](https://arxiv.org/abs/2505.21864) | 2025-05-28 | [repo](https://github.com/real-stanford/DexUMI) | 145 | - | - | We present DexUMI - a data collection and policy learning framework that uses the human hand as t... |
| [Universal Manipulation Interface: In-The...](../papers/2402.10329.md) | [2402.10329](https://arxiv.org/abs/2402.10329) | 2024-02-15 | [repo](https://github.com/real-stanford/universal_manipulation_interface) | 1,065 | - | [❤️1,790 🔄370](https://x.com/chichengcc/status/1758539728444629158)<br>👁️432,238 | We present Universal Manipulation Interface (UMI) -- a data collection and policy learning framew... |
| [RoboCopilot: Human-in-the-loop Interacti...](../papers/2503.07771.md) | [2503.07771](https://arxiv.org/abs/2503.07771) | 2025-03-10 | - | - | [12](https://www.semanticscholar.org/paper/dcd99528e6f8d554af00f59821c98f9a12858713) (📈1) | - | Learning from human demonstration is an effective approach for learning complex manipulation skills. |


---

*This page is automatically updated with the latest research. Last updated: 2025-11-14 00:10 UTC*
