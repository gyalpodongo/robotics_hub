# Data Collection & Teleoperation

Data collection is the foundation of modern robot learning. Recent innovations focus on scalable, low-cost teleoperation systems that allow efficient human demonstrations.

## What is Robot Data Collection?

Robot data collection captures demonstrations that map sensory inputs to robot actions, serving as training material for learning algorithms.

## Key Methods

### Portable Teleoperation
**UMI** uses hand-held grippers for portable, in-the-wild data collection.

### VR-Based Teleoperation
**XRoboToolkit** provides immersive teleoperation using VR headsets.

### Dexterous Data Collection
**DexUMI** uses human hands as interfaces for dexterous manipulation data.

## Important Considerations

- **Data diversity**: Varied environments and objects
- **Data quality**: Clean labels and synchronized sensors
- **Data scale**: 100k+ demonstrations for robust performance
- **Safety**: Protecting robots and environments


---

## 🔥 Latest Trends & Research Directions

*Last Updated: 2025-11-14 00:37 UTC*

### 1. Emerging Techniques

Several new techniques are gaining traction. **XR-based teleoperation** is becoming more sophisticated, with frameworks like XRoboToolkit leveraging OpenXR for cross-platform compatibility and low-latency stereoscopic visual feedback, vital for reducing motion sickness and improving control precision. The use of **compliant, bilateral teleoperation interfaces**, as seen in RoboCopilot, is enabling seamless control switching between humans and autonomous policies, facilitating interactive imitation learning. **Human-Gated DAgger (HG-DAgger)** and similar human-in-the-loop interactive learning paradigms are also gaining prominence for refining robot manipulation policies by incorporating human corrective feedback during policy execution. Finally, **hardware adaptation layers** that use optimization to bridge the kinematic gap between human input devices (like exoskeletons) and robot hands, coupled with **software adaptation layers** that replace human demonstrations with simulated robot hand video, as shown in DexUMI, are proving effective in transferring dexterous manipulation skills.

### 2. Key Innovations

Key innovations include **XRoboToolkit's OpenXR-compliant architecture** for standardized data formats and cross-device compatibility in XR teleoperation. This allows for integration of diverse robot platforms and tracking modalities, demonstrated by the various robot types supported. **RoboCopilot's 20-DOF mobile bimanual robot** with a compliant teleoperation interface and **integrated HG-DAgger** also stands out as a hardware/software system for interactive learning. The **DexUMI framework's bi-level optimization** for designing wearable hand exoskeletons that match target robot hand kinematics, combined with **visual inpainting using SAM2 and ProPainter**, represents a major advancement in minimizing the embodiment gap for dexterous manipulation. This enables policies learned from human demonstrations to be transferred effectively to different robot hands.

### 3. Research Directions

Research is heading towards **more intuitive and effective human-robot collaboration**. This includes improving the fidelity and reducing the latency of XR-based teleoperation systems, as well as the development of more sophisticated control strategies for bimanual manipulation. Researchers are increasingly focused on **interactive imitation learning**, where humans provide corrective feedback to refine robot policies in real-time. There is also a significant push towards **dexterous manipulation**, with a focus on minimizing the embodiment gap between human hands and robot hands. This involves the development of new hardware interfaces (e.g., exoskeletons) and software adaptation techniques (e.g., visual inpainting). A key direction is to increase data collection throughput, specifically DexUMI demonstrating 3.2x over traditional teleoperation.

### 4. Open Challenges

Open challenges include **improving the robustness and reliability of XR-based teleoperation systems**, particularly in the face of network latency and tracking errors. **Scaling interactive imitation learning to more complex and long-horizon tasks** remains a challenge, as does ensuring that human feedback is consistent and reliable. **Generalizing dexterous manipulation skills across different robot hands** is also difficult, as it requires careful consideration of the kinematic and dynamic differences between the human hand and the robot hand. Ensuring the **safety and intuitiveness of teleoperated systems** as they become more complex is also critical for real-world deployment.

### 5. Promising Areas for Exploration

Promising areas for exploration include the **integration of multimodal feedback** (e.g., haptic, visual, auditory) in XR-based teleoperation systems to improve operator situation awareness. This could also involve the **incorporation of AI-based assistance** to help operators make better decisions. **Developing more sophisticated imitation learning algorithms** that can learn from both expert demonstrations and novice corrections is another promising area. The use of **tactile sensing** in dexterous manipulation systems also warrants further investigation. Building datasets that expose the challenges of the real world.

---

## 📄 Papers in This Domain

| Paper | PDF | Date | Authors | GitHub | Citations | Issues | Changes | Twitter |
|-------|-----|------|---------|--------|-----------|--------|---------|----------|
| [Universal Manipulation Interface: In-...](../papers/2402.10329.md) | [2402.10329](https://arxiv.org/abs/2402.10329) | Feb 15, 2024 | Chi et al. | ⭐[1.1k](https://github.com/real-stanford/universal_manipulation_interface)<br>🔀[202](https://github.com/real-stanford/universal_manipulation_interface) | — | 63 | [Feb 15, 2024](../papers/2402.10329.md) | ❤️[1.8k](https://x.com/chichengcc/status/1758539728444629158) 🔁[370](https://x.com/chichengcc/status/1758539728444629158)<br>👁️[432.2k](https://x.com/chichengcc/status/1758539728444629158) |
| [XRoboToolkit: A Cross-Platform Framew...](../papers/2508.00097.md) | [2508.00097](https://arxiv.org/abs/2508.00097) | Jul 31, 2025 | Zhao et al. | — | [2](https://www.semanticscholar.org/paper/f2b6c0a329270d3e90cfaa1604c6861ed563e67c)<br>📈1 | None | [Jul 31, 2025](../papers/2508.00097.md) | — |
| [RoboCopilot: Human-in-the-loop Intera...](../papers/2503.07771.md) | [2503.07771](https://arxiv.org/abs/2503.07771) | Mar 10, 2025 | Wu et al. | — | [12](https://www.semanticscholar.org/paper/dcd99528e6f8d554af00f59821c98f9a12858713)<br>📈1 | None | [Mar 10, 2025](../papers/2503.07771.md) | — |
| [DexUMI: Using Human Hand as the Unive...](../papers/2505.21864.md) | [2505.21864](https://arxiv.org/abs/2505.21864) | May 28, 2025 | Xu et al. | ⭐[145](https://github.com/real-stanford/DexUMI)<br>🔀[13](https://github.com/real-stanford/DexUMI) | [10](https://www.semanticscholar.org/paper/22550cdfb498e0890e75e504d8ab5dd5e0ca8729) | 3 | [May 28, 2025](../papers/2505.21864.md) | — |

---

*This page is automatically updated with the latest research trends and papers.*
