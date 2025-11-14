# Mobile Manipulation & Navigation

Mobile manipulation combines navigation and manipulation, enabling robots to move through environments to reach objects and perform tasks. This requires coordinating whole-body control, long-horizon planning, and multimodal perception.

## What is Mobile Manipulation?

Mobile manipulation involves robots with both mobility (wheeled bases, legs) and manipulation capabilities (arms, grippers). Tasks include fetching objects from different rooms, tidying, and delivery, requiring navigation to target locations followed by manipulation.

## Key Approaches

### Language-Guided Mobile Manipulation
**TidyBot** uses LLMs for personalized robot assistance, learning user preferences for object placement and generating navigation plans to tidy rooms according to individual preferences.

### Vision-Based Navigation
**NoMaD** employs goal-masked diffusion policies for navigation and exploration, learning robust visuomotor policies that generalize across indoor environments.

### Whole-Body Control
Coordinating base motion with arm control for mobile manipulation, including approaches that optimize joint base-arm trajectories.

## Important Considerations

- **Task decomposition**: Breaking mobile manipulation into navigation and manipulation subgoals
- **Failure recovery**: Handling navigation failures or manipulation errors during long tasks
- **Multi-room reasoning**: Planning across multiple rooms and doorways
- **Dynamic environments**: Adapting to moving obstacles and changing layouts
- **Energy efficiency**: Optimizing battery usage for long-duration mobile tasks

## Notable Methods

- **TidyBot**: LLM-based personalized mobile manipulation
- **NoMaD**: Diffusion policies for navigation and exploration
- **HAB (Habitat)**: Simulation platform for embodied AI with mobile manipulation


---

## 📄 Papers in This Domain

| Paper | PDF | Date | GitHub | Stars | Citations | Twitter | Summary |
|-------|-----|------|--------|-------|-----------|---------|----------|
| [NoMaD: Goal Masked Diffusion Policies fo...](../papers/2310.07896.md) | [2310.07896](https://arxiv.org/abs/2310.07896) | 2023-10-11 | - | - | - | - | Robotic learning for navigation in unfamiliar environments needs to provide policies for both tas... |
| [TidyBot: Personalized Robot Assistance w...](../papers/2305.05658.md) | [2305.05658](https://arxiv.org/abs/2305.05658) | 2023-05-09 | [repo](https://github.com/jimmyyhwu/tidybot) | 666 | - | - | For a robot to personalize physical assistance effectively, it must learn user preferences that c... |


---

*This page is automatically updated with the latest research. Last updated: 2025-11-14 00:10 UTC*
