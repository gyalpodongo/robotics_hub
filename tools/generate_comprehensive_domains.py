import json
from pathlib import Path
from datetime import datetime
from scoring import score_paper

DOMAIN_CONTENT = {
    "vla": {
        "title": "Foundation Models & VLAs",
        "intro": """Vision-Language-Action (VLA) models represent a paradigm shift in robotics by combining visual perception, natural language understanding, and action prediction in a single unified model. These foundation models leverage large-scale pre-training on internet data and robot demonstrations to enable general-purpose robotic manipulation.

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
"""
    },
    "policy_methods": {
        "title": "Policy Learning Methods",
        "intro": """Policy learning methods form the algorithmic backbone of modern robot learning, determining how robots map observations to actions. Recent advances focus on leveraging powerful generative models, particularly diffusion models, to learn complex multimodal action distributions directly from demonstrations.

## What are Policy Learning Methods?

Policy learning methods define how robots learn to perform tasks from data. Unlike traditional control approaches that rely on hand-crafted controllers, learning-based policies automatically discover effective behaviors from demonstrations (imitation learning) or trial-and-error (reinforcement learning).

## Key Approaches

### Diffusion Policies
**Diffusion Policy** treats action generation as a denoising process, learning to iteratively refine noisy actions into precise trajectories. This approach naturally handles multimodal action distributions and achieves state-of-the-art performance on complex visuomotor tasks.

### 3D Representation Learning
Methods like **3D Diffusion Policy** and **3D Diffuser Actor** leverage 3D scene representations (point clouds, voxels) for better spatial reasoning and view-invariant manipulation.

### Consistency Models
**Consistency Policy** accelerates diffusion-based policies by enabling single-step inference, achieving 10x speedup while maintaining performance for real-time robot control.

### Equivariant Policies
**EquiBot** exploits SE(3) symmetries in manipulation tasks, enabling data-efficient learning and better generalization across object poses and camera viewpoints.

### Autoregressive Methods
**ARP (Autoregressive Policy)** models actions as sequential decisions with action chunking, improving temporal consistency in long-horizon tasks.

## Important Considerations

- **Action representation**: Choice of action space (absolute vs. relative, position vs. velocity) significantly impacts performance
- **Temporal consistency**: Policies must generate smooth, dynamically feasible trajectories
- **Multi-modality**: Real-world tasks often have multiple valid solutions; policies should capture this diversity
- **Sample efficiency**: Reducing the number of demonstrations needed remains a key challenge
- **Real-time inference**: Policies must run at control frequencies (10-30 Hz) for reactive behaviors

## Notable Methods

- **Diffusion Policy**: State-of-the-art visuomotor policy using denoising diffusion
- **3D Diffusion Policy**: 3D-aware diffusion for view-invariant manipulation
- **Consistency Policy**: Real-time diffusion policy with single-step inference
- **DPPO**: Combining diffusion models with reinforcement learning via PPO
"""
    },
    "rl": {
        "title": "Reinforcement Learning",
        "intro": """Reinforcement Learning (RL) enables robots to learn behaviors through trial-and-error interaction with their environment, guided by reward signals. Recent breakthroughs combine RL with large language models (LLMs) for automated reward design and open-ended exploration, dramatically accelerating robot learning.

## What is Robot RL?

Robot RL trains policies to maximize cumulative reward by exploring the environment and learning from feedback. Unlike imitation learning which requires expert demonstrations, RL can discover novel strategies and optimize for task success beyond human capabilities.

## Key Approaches

### LLM-Guided Reward Design
**Eureka** uses LLMs to automatically write reward functions as executable code, achieving human-level reward design without manual engineering. This breakthrough enables rapid prototyping of RL tasks.

### Open-Ended Exploration
**Voyager** creates a lifelong learning agent in Minecraft that autonomously discovers skills, stores them as code, and composes them for complex tasks using LLMs as a high-level planner.

### Diffusion RL
Methods like **DPPO** combine diffusion models' expressiveness with RL's ability to optimize for task success, enabling fine-tuning of pre-trained diffusion policies via reinforcement learning.

### Offline RL
Learning from fixed datasets of sub-optimal demonstrations without environment interaction, crucial for real-world robots where exploration is expensive or dangerous.

## Important Considerations

- **Sample efficiency**: RL typically requires millions of environment steps; simulation is essential
- **Reward engineering**: Designing reward functions that capture task intent without unintended behaviors
- **Sim-to-real transfer**: Policies trained in simulation must transfer robustly to real hardware
- **Safety**: Exploration must respect safety constraints to avoid damaging robots or environments
- **Credit assignment**: Determining which actions led to rewards in long-horizon tasks

## Notable Methods

- **Eureka**: LLM-powered automated reward design
- **Voyager**: Open-ended lifelong learning agent with skill library
- **DPPO**: Diffusion policy optimization via PPO
- **SAC/TD3**: State-of-the-art model-free RL algorithms for continuous control
"""
    },
    "data_collection": {
        "title": "Data Collection & Teleoperation",
        "intro": """Data collection is the foundation of modern robot learning. High-quality, diverse datasets enable robots to learn complex behaviors through imitation learning, reinforcement learning, and other data-driven approaches. Recent innovations focus on scalable, low-cost teleoperation systems that allow humans to efficiently provide demonstrations.

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
"""
    },
    "datasets": {
        "title": "Datasets & Benchmarks",
        "intro": """Large-scale datasets and standardized benchmarks are accelerating robot learning research by enabling researchers to train and evaluate policies on diverse tasks without requiring extensive real-world data collection. These datasets capture varied robot morphologies, tasks, and environments.

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
"""
    },
    "sim_to_real": {
        "title": "Sim-to-Real & Transfer",
        "intro": """Sim-to-real transfer bridges the gap between simulated training environments and physical robots, enabling sample-efficient learning and safe policy development. Recent advances leverage photorealistic rendering, domain randomization, and learned dynamics models to minimize the reality gap.

## What is Sim-to-Real?

Sim-to-real transfer trains policies in simulation where data collection is cheap, fast, and safe, then deploys them on real robots. Successful transfer requires handling differences in physics, sensors, and environment dynamics between simulation and reality.

## Key Approaches

### Digital Twins
**Real-is-Sim** creates dynamic digital twins of real environments using 3D Gaussian Splatting, enabling high-fidelity simulation that closely matches reality for robust policy transfer.

### Domain Randomization
**RoboGen** uses procedural generation to create infinite variations of tasks, objects, and environments in simulation, training policies robust to real-world variation.

### Video-to-Reality
**Dreamitate** learns from human videos and translates them into simulation, then trains policies that transfer to real robots, leveraging internet-scale human demonstration data.

### Affordance Transfer
Learning affordances (actionable properties) from human videos as a versatile representation for cross-embodiment transfer between humans and robots.

## Important Considerations

- **Physics fidelity**: Accurate simulation of contact, friction, and dynamics is critical
- **Sensor realism**: Matching camera properties, noise characteristics, and failure modes
- **Latency modeling**: Accounting for control delays and communication lags
- **Domain randomization**: Balancing randomization breadth with policy learning difficulty
- **Real-world validation**: Extensive testing on physical robots to verify transfer success

## Notable Methods

- **Real-is-Sim**: Gaussian splatting-based digital twins
- **RoboGen**: Procedural generation for infinite task diversity
- **Dreamitate**: Learning from human videos via video generation
- **Isaac Gym**: GPU-accelerated parallel simulation for RL
"""
    },
    "manipulation": {
        "title": "Manipulation & Grasping",
        "intro": """Robotic manipulation encompasses grasping, placing, pushing, and contact-rich interactions with objects. Recent advances combine learning-based approaches with geometric reasoning, enabling robots to manipulate diverse objects in cluttered, unstructured environments.

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
"""
    },
    "dexterous": {
        "title": "Dexterous Manipulation",
        "intro": """Dexterous manipulation using multi-fingered hands enables fine-grained, human-like object interactions. Recent progress combines novel hardware designs with learning-based control, unlocking complex manipulation skills like in-hand reorientation and bimanual coordination.

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
"""
    },
    "mobile_manipulation": {
        "title": "Mobile Manipulation & Navigation",
        "intro": """Mobile manipulation combines navigation and manipulation, enabling robots to move through environments to reach objects and perform tasks. This requires coordinating whole-body control, long-horizon planning, and multimodal perception.

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
"""
    },
    "perception": {
        "title": "Perception & Scene Understanding",
        "intro": """Perception systems extract structured information from raw sensory data, enabling robots to understand their environment. Recent advances leverage foundation models pre-trained on massive vision datasets for zero-shot generalization to novel objects and scenes.

## What is Robot Perception?

Robot perception processes camera images, depth sensors, and other modalities to extract actionable representations: object locations, poses, semantic labels, and geometric structure. Modern perception relies heavily on deep learning and foundation models.

## Key Approaches

### Vision Foundation Models
**DINOv2** provides self-supervised visual features without human annotations, learning robust representations that transfer across robotics tasks for object detection, segmentation, and tracking.

### 6D Pose Estimation
**FoundationPose** unifies pose estimation and tracking for novel objects without CAD models, using foundation model features for generalization.

### Scene Understanding
Methods that construct 3D scene graphs, identifying objects, their properties, and spatial relationships for high-level reasoning.

## Important Considerations

- **Lighting robustness**: Handling varied illumination, shadows, and reflections
- **Occlusion handling**: Detecting partially visible objects in clutter
- **Real-time performance**: Running perception at camera frame rates (30+ Hz)
- **Domain transfer**: Generalizing from training datasets to deployment environments
- **Multimodal fusion**: Combining RGB, depth, and tactile sensing

## Notable Methods

- **DINOv2**: Self-supervised vision foundation model
- **FoundationPose**: Model-free 6D pose estimation
- **SAM (Segment Anything)**: Foundation model for image segmentation
- **CLIP**: Vision-language model for zero-shot object recognition
"""
    },
    "hri_planning": {
        "title": "HRI & Task Planning",
        "intro": """Human-Robot Interaction (HRI) and task planning enable robots to understand high-level human commands and decompose them into executable actions. Recent breakthroughs use LLMs for natural language interfaces and automated task planning in complex environments.

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
"""
    }
}

def generate_domain_table(papers: list[dict]) -> str:
    if not papers:
        return "_No papers in this domain yet._\n"

    papers_with_scores = [(p, score_paper(p)) for p in papers]
    papers_with_scores.sort(key=lambda x: x[1], reverse=True)

    table = "| Paper | PDF | Date | GitHub | Stars | Citations | Twitter | Summary |\n"
    table += "|-------|-----|------|--------|-------|-----------|---------|----------|\n"

    for paper, score in papers_with_scores:
        arxiv = paper['arxiv']
        github = paper.get('github', {})
        twitter = paper.get('twitter', {})
        semantic = paper.get('semantic_scholar', {})

        title = arxiv['title'][:40] + "..." if len(arxiv['title']) > 40 else arxiv['title']
        arxiv_id = arxiv['arxiv_id'].split('v')[0]
        arxiv_url = f"https://arxiv.org/abs/{arxiv_id}"
        pub_date = arxiv['published_date']

        paper_md = f"../papers/{arxiv_id}.md"

        github_url = github.get('repo_url')
        stars = github.get('stars')

        if github_url:
            github_cell = f"[repo]({github_url})"
            stars_cell = f"{stars:,}" if stars else "-"
        else:
            github_cell = "-"
            stars_cell = "-"

        citations = semantic.get('citation_count')
        influential = semantic.get('influential_citation_count')
        s2_url = f"https://www.semanticscholar.org/paper/{semantic.get('paper_id')}" if semantic.get('paper_id') else "#"

        if citations:
            citation_cell = f"[{citations:,}]({s2_url})"
            if influential:
                citation_cell += f" (📈{influential})"
        else:
            citation_cell = "-"

        likes = twitter.get('likes')
        retweets = twitter.get('retweets')
        views = twitter.get('views')
        twitter_url = twitter.get('tweet_url')

        twitter_parts = []
        if likes:
            twitter_parts.append(f"❤️{likes:,}")
        if retweets:
            twitter_parts.append(f"🔄{retweets:,}")

        twitter_lines = []
        if twitter_url and twitter_parts:
            line1 = " ".join(twitter_parts)
            twitter_lines.append(f"[{line1}]({twitter_url})")

        if views:
            twitter_lines.append(f"👁️{views:,}")

        twitter_cell = "<br>".join(twitter_lines) if twitter_lines else "-"

        first_sentence = arxiv['summary'].split('.')[0] + '.'
        if len(first_sentence) > 100:
            first_sentence = first_sentence[:97] + "..."

        table += f"| [{title}]({paper_md}) | [{arxiv_id}]({arxiv_url}) | {pub_date} | {github_cell} | {stars_cell} | {citation_cell} | {twitter_cell} | {first_sentence} |\n"

    return table

def generate_comprehensive_domain_md(domain_key: str, papers: list[dict]) -> str:
    content = DOMAIN_CONTENT[domain_key]

    md = f"""# {content['title']}

{content['intro']}

---

## 📄 Papers in This Domain

{generate_domain_table(papers)}

---

*This page is automatically updated with the latest research. Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}*
"""
    return md

def generate_all_comprehensive_domains(papers_file: Path, output_dir: Path):
    with open(papers_file, 'r') as f:
        papers = json.load(f)

    output_dir.mkdir(exist_ok=True)

    papers_by_domain = {}
    for paper in papers:
        for domain in paper.get('domains', []):
            if domain not in papers_by_domain:
                papers_by_domain[domain] = []
            papers_by_domain[domain].append(paper)

    print(f"Generating comprehensive domain files...\n")

    for domain_key in DOMAIN_CONTENT.keys():
        domain_papers = papers_by_domain.get(domain_key, [])

        filename = f"{domain_key}.md"
        filepath = output_dir / filename

        md_content = generate_comprehensive_domain_md(domain_key, domain_papers)

        with open(filepath, 'w') as f:
            f.write(md_content)

        print(f"✓ Generated {filename} ({len(domain_papers)} papers)")

    print(f"\n✅ Generated {len(DOMAIN_CONTENT)} comprehensive domain files")

if __name__ == "__main__":
    papers_file = Path(__file__).parent.parent / "data" / "papers.json"
    output_dir = Path(__file__).parent.parent / "domains"

    generate_all_comprehensive_domains(papers_file, output_dir)
