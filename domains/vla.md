# Foundation Models & VLAs

Vision-Language-Action (VLA) models represent a paradigm shift in robotics by combining visual perception, natural language understanding, and action prediction in a single unified model. These foundation models leverage large-scale pre-training on internet data and robot demonstrations to enable general-purpose robotic manipulation.

## What are VLA Models?

VLA models are transformer-based architectures that process visual observations and language instructions to generate low-level robot actions. They bridge the gap between high-level semantic understanding (from vision-language models) and low-level control (for robot actuation), enabling robots to follow natural language commands in diverse environments.

## Key Approaches

### End-to-End VLAs
Models like **OpenVLA** and **RT-2** directly map pixels and language to actions using large transformers trained on millions of robot demonstrations. They eliminate the need for separate perception and control modules, enabling true end-to-end learning.

### Embodied Multimodal Models
Models like **PaLM-E** inject embodied sensor data (vision, proprioception) into large language models, allowing them to reason about the physical world and generate executable plans.

### Cross-Embodiment Transfer
The **Open X-Embodiment** dataset enables training policies that generalize across different robot morphologies, from single arms to bimanual systems, by learning shared representations of manipulation skills.

## Important Considerations

- **Data scale**: VLAs require millions of diverse demonstrations for robust generalization
- **Compute requirements**: Training large VLAs demands significant GPU resources (100B+ parameters)
- **Sim-to-real gap**: Pre-training in simulation helps, but real-world fine-tuning is essential
- **Safety & robustness**: Foundation models can exhibit unexpected behaviors; verification is critical
- **Interpretability**: Understanding why VLAs make certain decisions remains challenging

## Notable Models & Datasets

- **OpenVLA**: 7B-parameter open-source VLA trained on 970k demonstrations
- **RT-2 (Robotic Transformer)**: Google's 55B-parameter VLA with web-scale pre-training
- **Open X-Embodiment**: 1M+ demonstration dataset across 22 robot embodiments
- **PaLM-E**: 562B-parameter embodied multimodal model


---

## 📄 Papers in This Domain

| Paper | PDF | Date | GitHub | Stars | Citations | Twitter | Summary |
|-------|-----|------|--------|-------|-----------|---------|----------|
| [GR00T N1: An Open Foundation Model for G...](../papers/2503.14734.md) | [2503.14734](https://arxiv.org/abs/2503.14734) | 2025-03-18 | - | - | - | [❤️1,945 🔄398](https://x.com/DrJimFan/status/1902117478496616642)<br>👁️450,145 | General-purpose robots need a versatile body and an intelligent mind. |
| [Open X-Embodiment: Robotic Learning Data...](../papers/2310.08864.md) | [2310.08864](https://arxiv.org/abs/2310.08864) | 2023-10-13 | - | - | - | [❤️1,173 🔄302](https://x.com/GoogleDeepMind/status/1709207886943965648)<br>👁️518,773 | Large, high-capacity models trained on diverse datasets have shown remarkable successes on effici... |
| [OpenVLA: An Open-Source Vision-Language-...](../papers/2406.09246.md) | [2406.09246](https://arxiv.org/abs/2406.09246) | 2024-06-13 | [repo](https://github.com/openvla/openvla) | 4,415 | - | [❤️695 🔄162](https://x.com/moo_jin_kim/status/1801548441102991771)<br>👁️226,126 | Large policies pretrained on a combination of Internet-scale vision-language data and diverse rob... |
| [CogACT: A Foundational Vision-Language-A...](../papers/2411.19650.md) | [2411.19650](https://arxiv.org/abs/2411.19650) | 2024-11-29 | [repo](https://github.com/microsoft/CogACT) | 374 | - | - | The advancement of large Vision-Language-Action (VLA) models has significantly improved robotic m... |
| [RT-2: Vision-Language-Action Models Tran...](../papers/2307.15818.md) | [2307.15818](https://arxiv.org/abs/2307.15818) | 2023-07-28 | [repo](https://github.com/kyegomez/RT-2) | 528 | - | [❤️1,590 🔄435](https://x.com/GoogleDeepMind/status/1684903412834447360)<br>👁️537,063 | We study how vision-language models trained on Internet-scale data can be incorporated directly i... |
| [Unleashing Large-Scale Video Generative ...](../papers/2312.13139.md) | [2312.13139](https://arxiv.org/abs/2312.13139) | 2023-12-20 | [repo](https://github.com/bytedance/GR-1) | 286 | - | - | Generative pre-trained models have demonstrated remarkable effectiveness in language and vision d... |
| [An Embodied Generalist Agent in 3D World](../papers/2311.12871.md) | [2311.12871](https://arxiv.org/abs/2311.12871) | 2023-11-18 | [repo](https://github.com/embodied-generalist/embodied-generalist) | 465 | - | [❤️199 🔄34](https://x.com/jeasinema/status/1727595460867862930)<br>👁️81,872 | Leveraging massive knowledge from large language models (LLMs), recent machine learning models sh... |
| [AHA: A Vision-Language-Model for Detecti...](../papers/2410.00371.md) | [2410.00371](https://arxiv.org/abs/2410.00371) | 2024-10-01 | [repo](https://github.com/NVlabs/AHA) | 49 | - | [❤️201 🔄43](https://x.com/DJiafei/status/1838562171460161619)<br>👁️48,462 | Robotic manipulation in open-world settings requires not only task execution but also the ability... |
| [PaLM-E: An Embodied Multimodal Language ...](../papers/2303.03378.md) | [2303.03378](https://arxiv.org/abs/2303.03378) | 2023-03-06 | [repo](https://github.com/kyegomez/PALM-E) | 329 | - | [❤️694 🔄210](https://x.com/GoogleAI/status/1634252301303947272)<br>👁️173,053 | Large language models excel at a wide range of complex tasks. |
| [VIMA: General Robot Manipulation with Mu...](../papers/2210.03094.md) | [2210.03094](https://arxiv.org/abs/2210.03094) | 2022-10-06 | [repo](https://github.com/vimalabs/VIMA) | 835 | - | [❤️856 🔄147](https://x.com/DrJimFan/status/1578433493561769984) | Prompt-based learning has emerged as a successful paradigm in natural language processing, where ... |


---

*This page is automatically updated with the latest research. Last updated: 2025-11-14 00:10 UTC*
