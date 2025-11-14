# HRI & Task Planning

Human-Robot Interaction and task planning enable robots to understand commands and decompose them into actions. Recent breakthroughs use LLMs.

## What is HRI & Task Planning?

HRI systems allow communication via language, gestures, or demonstrations. Task planning translates goals into action sequences.

## Key Approaches

### LLMs for Planning
**Code as Policies** generates Python code for robot control.

### Structured Prompting
**ProgPrompt** generates executable task plans.

### Multi-Robot Collaboration
**RoCo** enables multi-robot coordination via LLMs.

## Important Considerations

- **Grounding**: Mapping language to robot state/actions
- **Safety**: LLM-generated plans must respect constraints
- **Latency**: Quick plan generation for responsive interaction


---

## 🔥 Latest Trends & Research Directions

*Last Updated: 2025-11-14 00:44 UTC*

### 1. Emerging Techniques

The analysis reveals several emerging techniques in HRI and Task Planning, all centered around leveraging Large Language Models (LLMs):

*   **Code as Policies (CaP):** Directly generating robot control code (Python programs) using LLMs from natural language instructions. This moves beyond high-level planning to low-level control implementation. It allows for reacting to perceptual inputs (sensors), parameterizing control APIs, and direct execution.
*   **Multimodal Fusion for HRI:** Combining modalities like voice and deictic posture as parallel inputs to LLMs for richer and more intuitive HRI. This allows for simplifying commands and using natural human cues.
*   **Composable 3D Value Maps:** Using LLMs to compose 3D value maps (VoxPoser) representing rewards or costs in the robot's environment. VLMs provide geometric information that guides motion planning.
*   **Programmatic Prompting (ProgPrompt):** Structuring LLM prompts with program-like specifications of available actions, objects, and example programs to improve plan generation and execution.
*   **Dialectic Multi-Robot Collaboration:** Employing multiple LLM agents, each representing a robot, that engage in dialogues for task coordination, sub-task planning, and motion planning.

### 2. Key Innovations

Several key innovations stand out:

*   **Hierarchical Code Generation:** A key enhancement in CaP. LLMs are used to recursively define functions, improving code complexity and performance on code generation benchmarks.
*   **LLM-Based Trajectory Synthesis:** VoxPoser's use of LLMs to directly generate trajectories, combined with VLM perception, enables zero-shot trajectory synthesis without additional training.
*   **Assertions for Error Recovery:** ProgPrompt's inclusion of assertions in generated code allows the LLM to receive feedback and generate recovery actions when preconditions are violated.
*   **Task Coordination through Dialogue:** RoCo framework's employment of LLM agents that engage in dialogues enables effective task coordination, information exchange, and task reasoning in multi-robot systems.
*   **Open Vocabulary object detection for manipulation:** Enabling object understanding in LLM based methods through VLM models like YOLO-World and ViLD.

### 3. Research Directions

The field is heading towards:

*   **Improved Grounding:** Research focuses on strengthening the connection between LLM-generated plans and the physical world, addressing the brittle nature of grounding.
*   **Online Learning Integration:** Combining LLM-based planning with online learning of dynamics models for contact-rich interactions (VoxPoser) to improve efficiency and robustness.
*   **Comprehensive Benchmarking:** Developing more systematic benchmarks to evaluate multi-robot manipulation capabilities (RoCoBench) and code generation for robotics (RoboCodeGen).
*   **Human-Robot Collaboration:** Designing more flexible and interpretable HRI frameworks that facilitate seamless human-robot collaboration using dialogue agents (RoCo).
*   **LLM parameter optimization:** Using better models and parameters to improve efficiency and ability for complex tasks.

### 4. Open Challenges

Significant unsolved problems remain:

*   **API Understanding:** LLMs can struggle with understanding and correctly using robot APIs, especially complex ones.
*   **Complex Instructions:** Handling complex natural language instructions that require intricate reasoning and planning remains a challenge.
*   **Dynamics Modeling:** Creating general-purpose dynamics models that can be integrated with LLM-based planning for robust control.
*   **Perception Reliance:** Reliance on external perception modules is a limitation, as errors in perception can significantly impact overall performance.
*   **Scalability and Generalization:** Scaling LLM-based approaches to handle more complex tasks and environments while maintaining generalization capabilities.

### 5. Promising Areas for Exploration

Further research should focus on:

*   **Prompt Engineering:** Exploring advanced prompt engineering techniques to improve the quality and reliability of LLM-generated code and plans.
*   **LLM Fine-tuning:** Fine-tuning LLMs on robotics-specific datasets to improve their ability to understand and generate robot control code and plans.
*   **Hybrid Architectures:** Combining LLMs with traditional planning and control algorithms to leverage the strengths of both approaches.
*   **Explainability and Trust:** Developing methods to explain LLM-generated plans and provide guarantees about their safety and reliability to build trust in HRI.
*   **Integrating Common Sense Knowledge:** Incorporating common sense knowledge into LLMs to improve their ability to reason about the world and generate more realistic and effective plans.

---

## 📄 Papers in This Domain

| Paper | PDF | Date | Authors | GitHub | Citations | Issues | Changes | Twitter |
|-------|-----|------|---------|--------|-----------|--------|---------|----------|
| [Natural Multimodal Fusion-Based Human...](../papers/2501.00785.md) | [2501.00785](https://arxiv.org/abs/2501.00785) | Jan 01, 2025 | Lai et al. | — | — | None | [Jan 01, 2025](../papers/2501.00785.md) | — |
| [Code as Policies: Language Model Prog...](../papers/2209.07753.md) | [2209.07753](https://arxiv.org/abs/2209.07753) | Sep 16, 2022 | Liang et al. | — | [1.2k](https://www.semanticscholar.org/paper/91deaf9d324c8feafc189da0da03e60a60287bca)<br>📈93 | None | [Sep 16, 2022](../papers/2209.07753.md) | — |
| [VoxPoser: Composable 3D Value Maps fo...](../papers/2307.05973.md) | [2307.05973](https://arxiv.org/abs/2307.05973) | Jul 12, 2023 | Huang et al. | — | [674](https://www.semanticscholar.org/paper/1cd8373490efc2d74c2796f4b2aa27c7d4415ec9)<br>📈54 | None | [Jul 12, 2023](../papers/2307.05973.md) | — |
| [ProgPrompt: Generating Situated Robot...](../papers/2209.11302.md) | [2209.11302](https://arxiv.org/abs/2209.11302) | Sep 22, 2022 | Singh et al. | — | [799](https://www.semanticscholar.org/paper/c03fa01fbb9c77fe3d10609ba5f1dee33a723867)<br>📈48 | None | [Sep 22, 2022](../papers/2209.11302.md) | — |
| [RoCo: Dialectic Multi-Robot Collabora...](../papers/2307.04738.md) | [2307.04738](https://arxiv.org/abs/2307.04738) | Jul 10, 2023 | Mandi et al. | — | [190](https://www.semanticscholar.org/paper/c5d18dbb92d0cd5393baa1e69de33d6922ac3e57)<br>📈20 | None | [Jul 10, 2023](../papers/2307.04738.md) | — |
| [TidyBot: Personalized Robot Assistanc...](../papers/2305.05658.md) | [2305.05658](https://arxiv.org/abs/2305.05658) | May 09, 2023 | Wu et al. | ⭐[666](https://github.com/jimmyyhwu/tidybot)<br>🔀[84](https://github.com/jimmyyhwu/tidybot) | [364](https://www.semanticscholar.org/paper/e7a4e987dc250ac6a016ee2011bc7a552cfa8e8a)<br>📈16 | 0 | [May 09, 2023](../papers/2305.05658.md) | — |
| [AutoTAMP: Autoregressive Task and Mot...](../papers/2306.06531.md) | [2306.06531](https://arxiv.org/abs/2306.06531) | Jun 10, 2023 | Chen et al. | — | [143](https://www.semanticscholar.org/paper/dc135dabef805c7271f53ec4b212bdf8996cfd9d)<br>📈10 | None | [Jun 10, 2023](../papers/2306.06531.md) | — |

---

*This page is automatically updated with the latest research trends and papers.*
