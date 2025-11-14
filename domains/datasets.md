# Datasets & Benchmarks

Large-scale datasets and standardized benchmarks are accelerating robot learning research by enabling researchers to train and evaluate policies on diverse tasks without requiring extensive real-world data collection. These datasets capture varied robot morphologies, tasks, and environments.

## What are Robot Datasets?

Robot datasets consist of demonstrations or trajectories that include sensory observations (RGB images, depth, proprioception), actions, and task metadata. Large-scale datasets enable training generalizable policies that transfer across embodiments and environments.

## Key Datasets

### Cross-Embodiment Datasets
**Open X-Embodiment** aggregates 1M+ demonstrations from 22 robot embodiments across 160+ tasks, enabling training of generalist policies like RT-X that work across different robot morphologies.

### In-The-Wild Datasets
**DROID** provides large-scale manipulation data collected across diverse real-world environments (homes, offices, labs), capturing natural distribution of objects and scenarios.

### Benchmark Suites
**LIBERO** offers a standardized benchmark for lifelong robot learning with 130 tasks across four suites, evaluating knowledge transfer and multi-task learning capabilities.

## Important Considerations

- **Data diversity vs. quality**: Balancing breadth of coverage with demonstration quality
- **Embodiment standardization**: Defining common action/observation spaces across robots
- **Task annotation**: Rich task descriptions enable language-conditioned policies
- **Data licensing**: Ensuring proper attribution and usage rights for shared datasets
- **Reproducibility**: Providing clear evaluation protocols and baseline implementations

## Notable Datasets

- **Open X-Embodiment**: 1M+ demonstrations, 22 embodiments, 160+ tasks
- **DROID**: Large-scale in-the-wild manipulation dataset
- **LIBERO**: 130-task benchmark suite for lifelong learning
- **RoboNet**: Cross-embodiment dataset for visual dynamics


---

## 📄 Papers in This Domain

| Paper | PDF | Date | GitHub | Stars | Citations | Twitter | Summary |
|-------|-----|------|--------|-------|-----------|---------|----------|
| [Open X-Embodiment: Robotic Learning Data...](../papers/2310.08864.md) | [2310.08864](https://arxiv.org/abs/2310.08864) | 2023-10-13 | - | - | - | [❤️1,173 🔄302](https://x.com/GoogleDeepMind/status/1709207886943965648)<br>👁️518,773 | Large, high-capacity models trained on diverse datasets have shown remarkable successes on effici... |
| [DROID: A Large-Scale In-The-Wild Robot M...](../papers/2403.12945.md) | [2403.12945](https://arxiv.org/abs/2403.12945) | 2024-03-19 | - | - | - | - | The creation of large, diverse, high-quality robot manipulation datasets is an important stepping... |
| [LIBERO: Benchmarking Knowledge Transfer ...](../papers/2306.03310.md) | [2306.03310](https://arxiv.org/abs/2306.03310) | 2023-06-05 | [repo](https://github.com/Lifelong-Robot-Learning/LIBERO) | 1,124 | [354](https://www.semanticscholar.org/paper/98cfd7b1b29453c4e82536f5afdc6ddc58bbb1b3) (📈109) | - | Lifelong learning offers a promising paradigm of building a generalist agent that learns and adap... |


---

*This page is automatically updated with the latest research. Last updated: 2025-11-14 00:10 UTC*
