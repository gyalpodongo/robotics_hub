# Dexterous Manipulation

Dexterous manipulation using multi-fingered hands enables fine-grained, human-like object interactions. Recent progress combines novel hardware designs with learning-based control, unlocking complex manipulation skills like in-hand reorientation and bimanual coordination.

## What is Dexterous Manipulation?

Dexterous manipulation leverages articulated hands with many degrees of freedom (typically 15-20) to perform complex grasps and in-hand manipulations impossible with parallel-jaw grippers. This includes rotating objects, regrasping, and precise fingertip control.

## Key Approaches

### Low-Cost Dexterous Hardware
**RUKA** provides an affordable, 3D-printed tendon-driven humanoid hand with 15 underactuated DoFs, democratizing dexterous manipulation research through open-source hardware.

### Teleoperation for Dexterous Hands
**DexUMI** uses the human hand as a universal manipulation interface, capturing finger motions via motion capture for dexterous policy learning.

### Learning-Based Control
Modern approaches use deep RL or imitation learning to overcome the challenges of high-dimensional dexterous control, learning coordinated finger motions from demonstrations or self-play.

## Important Considerations

- **Hardware complexity**: Multi-fingered hands have many actuators, sensors, and contact points
- **Control difficulty**: High-dimensional action spaces make control challenging
- **Tactile sensing**: Fingertip force/torque sensors crucial for contact-rich manipulation
- **Sim-to-real gap**: Accurately simulating contact-rich dexterous behaviors is difficult
- **Data collection**: Capturing human-quality dexterous demonstrations requires specialized interfaces

## Notable Systems

- **RUKA**: Low-cost open-source tendon-driven hand
- **DexUMI**: Human hand teleoperation for dexterous learning
- **Shadow Hand**: Commercial high-DoF dexterous hand
- **Allegro Hand**: 16-DoF research dexterous hand


---

## 📄 Papers in This Domain

| Paper | PDF | Date | GitHub | Stars | Citations | Twitter | Summary |
|-------|-----|------|--------|-------|-----------|---------|----------|
| [DexUMI: Using Human Hand as the Universa...](../papers/2505.21864.md) | [2505.21864](https://arxiv.org/abs/2505.21864) | 2025-05-28 | [repo](https://github.com/real-stanford/DexUMI) | 145 | - | - | We present DexUMI - a data collection and policy learning framework that uses the human hand as t... |
| [RUKA: Rethinking the Design of Humanoid ...](../papers/2504.13165.md) | [2504.13165](https://arxiv.org/abs/2504.13165) | 2025-04-17 | [repo](https://github.com/ruka-hand/RUKA) | 153 | - | [❤️445 🔄100](https://x.com/irmakkguzey/status/1913276064287305730)<br>👁️109,358 | Dexterous manipulation is a fundamental capability for robotic systems, yet progress has been lim... |
| [CoGrasp: 6-DoF Grasp Generation for Huma...](../papers/2210.03173.md) | [2210.03173](https://arxiv.org/abs/2210.03173) | 2022-10-06 | - | - | - | - | Robot grasping is an actively studied area in robotics, mainly focusing on the quality of generat... |


---

*This page is automatically updated with the latest research. Last updated: 2025-11-14 00:10 UTC*
