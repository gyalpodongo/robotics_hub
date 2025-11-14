# Manipulation & Grasping

Robotic manipulation encompasses grasping, placing, and contact-rich interactions. Recent advances combine learning with geometric reasoning.

## What is Robotic Manipulation?

Manipulation requires coordinating perception, planning, and control for object interactions.

## Key Approaches

### Language-Conditioned Manipulation
**VoxPoser** uses LLMs to generate 3D value maps for manipulation.

### Contact-Rich Manipulation
**Adaptive Compliance Policy** handles contact-rich tasks like insertion.

### 6-DoF Grasping
**CoGrasp** generates grasps for human-robot collaboration.

## Important Considerations

- **Grasp stability**: Reliable grasps under uncertainty
- **Contact modeling**: Friction and multi-contact interactions
- **Object diversity**: Generalizing to novel objects


---

## 🔥 Latest Trends & Research Directions

*Last Updated: 2025-11-14 00:41 UTC*

### 1. Emerging Techniques

Recent papers highlight several emerging techniques in robotic manipulation and grasping. **Language-conditioned manipulation using LLMs and VLMs** is gaining significant traction, exemplified by VoxPoser. It involves generating 3D value maps from language instructions to guide robot trajectories, eliminating the need for predefined motion primitives. This approach leverages LLMs for high-level task decomposition and VLM integration for scene understanding.

Another technique is **learning adaptive compliance policies**, as seen in "Adaptive Compliance Policy." It involves enabling robots to dynamically adjust their compliance spatially and temporally, crucial for robust contact-rich manipulation. This includes using diffusion models for policy learning and FFT to encode force/torque data for better control. Kinesthetic teaching is used to transfer human compliance to robots.

Data-driven control using **motion capture and LSTM networks** to control tendon-driven hands, like RUKA, is also emerging. This approach enables robust control of underactuated systems by learning the complex mapping between motor positions and joint angles, bypassing the need for precise kinematic models and in-hand sensors.

### 2. Key Innovations

A standout innovation is **VoxPoser's composable 3D value maps**, which provide a flexible and interpretable way to represent manipulation tasks specified by language. The use of LLMs to generate Python code that interacts with VLMs and Numpy for voxel grid manipulation is a novel approach to grounding language instructions in robot actions.

The **adaptive compliance formulation** that simplifies human compliance extraction for learning is also a key innovation. Instead of attempting to learn the full, likely ill-conditioned human compliance profile directly, the method focuses on finding a stiffness matrix that minimizes internal forces while enabling accurate motion tracking.

RUKA's **combination of low-cost, 3D-printed hardware with a learning-based controller** is another breakthrough. Achieving high dexterity and strength with affordable components opens up new possibilities for widespread robotic adoption. The autonomous data collection method using motion capture to train LSTMs is central to this innovation.

### 3. Research Directions

The field is pushing towards **general-purpose robots capable of performing a wide variety of manipulation tasks in unstructured environments**. LLMs and VLMs provide flexibility when defining manipulation goals for robot systems. The trend of using learning-based compliance policies for robotic systems is rising. Furthermore, **human-robot collaboration** is emphasized with the desire to design collaborative robotic systems that can assist humans with manipulation tasks.

Another key research direction is **creating robots that can quickly learn manipulation skills through imitation or reinforcement learning**. Teleoperation and policy learning frameworks are demonstrating the potential for robots to adapt to new tasks and environments. The goal is to reduce the cost and effort required to train robots for specific applications.

### 4. Open Challenges

Several open challenges remain:

*   **Robustness to environment changes** for LLM-based manipulation. These methods often rely on the ability of VLMs to accurately sense the environment.
*   **Limited Tactile Sensing:** Tactile sensing still remains an open challenge in robotic hands to increase contact sensitivity and robustness.
*   **Data Collection:** High-quality manipulation data collection remains a bottleneck, hindering the development of more sophisticated learning-based controllers. Sim-to-real transfer techniques need to be improved to reduce reliance on real-world data.
*   **Affordability vs. Durability:** Balancing affordability with durability in robotic hardware, especially for tendon-driven systems with many moving parts, continues to be a challenge. Low-cost components are often prone to wear and tear.
*   **Safety and Trust:** Ensuring the safety and trustworthiness of robots working in close proximity to humans is critical.
### 5. Promising Areas for Exploration

Promising areas for exploration include:

*   **Incorporating Force/Torque Feedback:** Integrating force/torque feedback into LLM-based manipulation frameworks could improve robustness and precision in contact-rich tasks.
*   **Multimodal Perception:** Combining visual, tactile, and auditory sensing could provide a more complete understanding of the environment and improve manipulation performance.
*   **Self-Supervised Learning:** Exploring self-supervised learning techniques for manipulation could reduce the need for labeled data and enable robots to learn from their own experience.
*   **Hybrid Control Architectures:** Blending learning-based control with traditional control strategies could offer a balance between adaptability and robustness.
*   **Open-Source Hardware and Software:** Continued development and sharing of open-source hardware and software platforms is essential for accelerating research and innovation in the field.

---

## 📄 Papers in This Domain

| Paper | PDF | Date | Authors | GitHub | Citations | Issues | Changes | Twitter |
|-------|-----|------|---------|--------|-----------|--------|---------|----------|
| [VoxPoser: Composable 3D Value Maps fo...](../papers/2307.05973.md) | [2307.05973](https://arxiv.org/abs/2307.05973) | Jul 12, 2023 | Huang et al. | — | [674](https://www.semanticscholar.org/paper/1cd8373490efc2d74c2796f4b2aa27c7d4415ec9)<br>📈54 | None | [Jul 12, 2023](../papers/2307.05973.md) | — |
| [Adaptive Compliance Policy: Learning ...](../papers/2410.09309.md) | [2410.09309](https://arxiv.org/abs/2410.09309) | Oct 12, 2024 | Hou et al. | ⭐[92](https://github.com/yifan-hou/adaptive_compliance_policy)<br>🔀[8](https://github.com/yifan-hou/adaptive_compliance_policy) | — | 1 | [Oct 12, 2024](../papers/2410.09309.md) | — |
| [RUKA: Rethinking the Design of Humano...](../papers/2504.13165.md) | [2504.13165](https://arxiv.org/abs/2504.13165) | Apr 17, 2025 | Zorin et al. | ⭐[153](https://github.com/ruka-hand/RUKA)<br>🔀[20](https://github.com/ruka-hand/RUKA) | [4](https://www.semanticscholar.org/paper/dd9e6a02ba61cb4839a22c6f53eb867f95828ef8) | 3 | [Apr 17, 2025](../papers/2504.13165.md) | ❤️[445](https://x.com/irmakkguzey/status/1913276064287305730) 🔁[100](https://x.com/irmakkguzey/status/1913276064287305730)<br>👁️[109.4k](https://x.com/irmakkguzey/status/1913276064287305730) |
| [CoGrasp: 6-DoF Grasp Generation for H...](../papers/2210.03173.md) | [2210.03173](https://arxiv.org/abs/2210.03173) | Oct 06, 2022 | Keshari et al. | — | [8](https://www.semanticscholar.org/paper/33b5b1ad60f5f647208b75e8d2f5069bc2c4bc52) | None | [Oct 06, 2022](../papers/2210.03173.md) | — |

---

*This page is automatically updated with the latest research trends and papers.*
