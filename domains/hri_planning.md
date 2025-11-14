# HRI & Task Planning

Human-Robot Interaction (HRI) and task planning enable robots to understand high-level human commands and decompose them into executable actions. Recent breakthroughs use LLMs for natural language interfaces and automated task planning in complex environments.

## What is HRI & Task Planning?

HRI systems allow humans to communicate with robots via natural language, gestures, or demonstrations. Task planning translates high-level goals ("clean the kitchen") into sequences of low-level actions, handling constraints, preconditions, and environmental uncertainty.

## Key Approaches

### LLMs for Task Planning
**Code as Policies** uses LLMs to generate Python code that controls robots, enabling complex task composition and reasoning about spatial relationships and object properties.

### Structured Prompting
**ProgPrompt** generates situated robot task plans using structured prompting of LLMs, ensuring syntactic correctness and executable action sequences.

### LLM + Classical Planning
**AutoTAMP** combines LLMs with Task and Motion Planning (TAMP), using LLMs to translate language to symbolic goals and classical planners for kinematically feasible execution.

### Multi-Robot Collaboration
**RoCo** enables dialectic multi-robot collaboration where LLMs coordinate multiple robots through natural language, assigning subtasks and resolving conflicts.

### Multimodal HRI
Recent work integrates gestures, gaze, and language for natural multimodal human-robot communication.

## Important Considerations

- **Grounding**: Mapping language to robot state/action spaces
- **Error handling**: Detecting and recovering from execution failures
- **Safety**: Ensuring LLM-generated plans respect safety constraints
- **Interpretability**: Explaining robot decisions to human users
- **Latency**: Generating plans quickly enough for responsive interaction

## Notable Methods

- **Code as Policies**: LLM-generated Python code for robot control
- **ProgPrompt**: Structured LLM prompting for task planning
- **AutoTAMP**: LLM + classical TAMP integration
- **RoCo**: LLM-based multi-robot collaboration
- **VoxPoser**: LLM-guided 3D value maps


---

## 📄 Papers in This Domain

| Paper | PDF | Date | GitHub | Stars | Citations | Twitter | Summary |
|-------|-----|------|--------|-------|-----------|---------|----------|
| [Natural Multimodal Fusion-Based Human-Ro...](../papers/2501.00785.md) | [2501.00785](https://arxiv.org/abs/2501.00785) | 2025-01-01 | - | - | - | - | Translating human intent into robot commands is crucial for the future of service robots in an ag... |
| [Code as Policies: Language Model Program...](../papers/2209.07753.md) | [2209.07753](https://arxiv.org/abs/2209.07753) | 2022-09-16 | - | - | [1,178](https://www.semanticscholar.org/paper/91deaf9d324c8feafc189da0da03e60a60287bca) (📈93) | - | Large language models (LLMs) trained on code completion have been shown to be capable of synthesi... |
| [VoxPoser: Composable 3D Value Maps for R...](../papers/2307.05973.md) | [2307.05973](https://arxiv.org/abs/2307.05973) | 2023-07-12 | - | - | [674](https://www.semanticscholar.org/paper/1cd8373490efc2d74c2796f4b2aa27c7d4415ec9) (📈54) | - | Large language models (LLMs) are shown to possess a wealth of actionable knowledge that can be ex... |
| [RoCo: Dialectic Multi-Robot Collaboratio...](../papers/2307.04738.md) | [2307.04738](https://arxiv.org/abs/2307.04738) | 2023-07-10 | - | - | - | - | We propose a novel approach to multi-robot collaboration that harnesses the power of pre-trained ... |
| [ProgPrompt: Generating Situated Robot Ta...](../papers/2209.11302.md) | [2209.11302](https://arxiv.org/abs/2209.11302) | 2022-09-22 | - | - | [799](https://www.semanticscholar.org/paper/c03fa01fbb9c77fe3d10609ba5f1dee33a723867) (📈48) | - | Task planning can require defining myriad domain knowledge about the world in which a robot needs... |
| [AutoTAMP: Autoregressive Task and Motion...](../papers/2306.06531.md) | [2306.06531](https://arxiv.org/abs/2306.06531) | 2023-06-10 | - | - | - | - | For effective human-robot interaction, robots need to understand, plan, and execute complex, long... |
| [TidyBot: Personalized Robot Assistance w...](../papers/2305.05658.md) | [2305.05658](https://arxiv.org/abs/2305.05658) | 2023-05-09 | [repo](https://github.com/jimmyyhwu/tidybot) | 666 | - | - | For a robot to personalize physical assistance effectively, it must learn user preferences that c... |


---

*This page is automatically updated with the latest research. Last updated: 2025-11-14 00:10 UTC*
