import json
import os
import tempfile
import requests
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv
from google import genai
from google.genai import types
from scoring import score_paper

load_dotenv()

gemini_client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

DOMAIN_STATIC_CONTENT = {
    "vla": {
        "title": "Foundation Models & VLAs",
        "intro": """Vision-Language-Action (VLA) models represent a paradigm shift in robotics by combining visual perception, natural language understanding, and action prediction in a single unified model. These foundation models leverage large-scale pre-training on internet data and robot demonstrations to enable general-purpose robotic manipulation.

## What are VLA Models?

VLA models are transformer-based architectures that process visual observations and language instructions to generate low-level robot actions. They bridge the gap between high-level semantic understanding (from vision-language models) and low-level control (for robot actuation), enabling robots to follow natural language commands in diverse environments.

## Key Approaches

### End-to-End VLAs
Models like **OpenVLA** and **RT-2** directly map pixels and language to actions using large transformers trained on millions of robot demonstrations.

### Embodied Multimodal Models
Models like **PaLM-E** inject embodied sensor data into large language models, allowing them to reason about the physical world.

### Cross-Embodiment Transfer
The **Open X-Embodiment** dataset enables training policies that generalize across different robot morphologies.

## Important Considerations

- **Data scale**: VLAs require millions of diverse demonstrations
- **Compute requirements**: Training demands significant GPU resources
- **Sim-to-real gap**: Real-world fine-tuning is essential
- **Safety & robustness**: Verification is critical

## Notable Models & Datasets

- **OpenVLA**: 7B-parameter open-source VLA
- **RT-2**: Google's 55B-parameter VLA
- **Open X-Embodiment**: 1M+ demonstration dataset
"""
    },
    "policy_methods": {
        "title": "Policy Learning Methods",
        "intro": """Policy learning methods form the algorithmic backbone of modern robot learning, determining how robots map observations to actions. Recent advances focus on leveraging powerful generative models, particularly diffusion models, to learn complex multimodal action distributions.

## What are Policy Learning Methods?

Policy learning methods define how robots learn to perform tasks from data through imitation learning or reinforcement learning.

## Key Approaches

### Diffusion Policies
**Diffusion Policy** treats action generation as a denoising process, naturally handling multimodal action distributions.

### 3D Representation Learning
Methods like **3D Diffusion Policy** leverage 3D scene representations for better spatial reasoning.

### Consistency Models
**Consistency Policy** accelerates diffusion policies for real-time robot control.

## Important Considerations

- **Action representation**: Choice of action space impacts performance
- **Temporal consistency**: Smooth, feasible trajectories are essential
- **Multi-modality**: Capturing diverse valid solutions
- **Real-time inference**: 10-30 Hz control frequencies required
"""
    },
    "rl": {
        "title": "Reinforcement Learning",
        "intro": """Reinforcement Learning (RL) enables robots to learn behaviors through trial-and-error, guided by reward signals. Recent breakthroughs combine RL with LLMs for automated reward design and open-ended exploration.

## What is Robot RL?

Robot RL trains policies to maximize cumulative reward by exploring and learning from feedback.

## Key Approaches

### LLM-Guided Reward Design
**Eureka** uses LLMs to automatically write reward functions as executable code.

### Open-Ended Exploration
**Voyager** creates lifelong learning agents that autonomously discover and compose skills.

### Diffusion RL
Methods like **DPPO** combine diffusion models with RL for fine-tuning policies.

## Important Considerations

- **Sample efficiency**: Simulation is essential
- **Reward engineering**: Capturing task intent correctly
- **Sim-to-real transfer**: Robust policy transfer
- **Safety**: Respecting constraints during exploration
"""
    },
    "data_collection": {
        "title": "Data Collection & Teleoperation",
        "intro": """Data collection is the foundation of modern robot learning. Recent innovations focus on scalable, low-cost teleoperation systems that allow efficient human demonstrations.

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
"""
    },
    "datasets": {
        "title": "Datasets & Benchmarks",
        "intro": """Large-scale datasets and standardized benchmarks accelerate robot learning research by enabling diverse task training without extensive data collection.

## What are Robot Datasets?

Robot datasets include demonstrations with observations, actions, and task metadata, enabling generalizable policy training.

## Key Datasets

### Cross-Embodiment Datasets
**Open X-Embodiment** aggregates 1M+ demonstrations from 22 robot embodiments.

### In-The-Wild Datasets
**DROID** provides manipulation data from diverse real-world environments.

### Benchmark Suites
**LIBERO** offers 130 tasks for evaluating lifelong learning.

## Important Considerations

- **Data diversity vs. quality**: Balancing breadth and quality
- **Embodiment standardization**: Common action/observation spaces
- **Task annotation**: Rich descriptions for language-conditioned policies
"""
    },
    "sim_to_real": {
        "title": "Sim-to-Real & Transfer",
        "intro": """Sim-to-real transfer bridges simulation and physical robots, enabling sample-efficient learning. Recent advances leverage photorealistic rendering and domain randomization.

## What is Sim-to-Real?

Sim-to-real transfer trains policies in simulation then deploys them on real robots.

## Key Approaches

### Digital Twins
**Real-is-Sim** creates digital twins using 3D Gaussian Splatting.

### Domain Randomization
**RoboGen** uses procedural generation for infinite task variations.

### Video-to-Reality
**Dreamitate** learns from human videos via video generation.

## Important Considerations

- **Physics fidelity**: Accurate contact and dynamics simulation
- **Sensor realism**: Matching camera properties and noise
- **Domain randomization**: Balancing breadth with learning difficulty
"""
    },
    "manipulation": {
        "title": "Manipulation & Grasping",
        "intro": """Robotic manipulation encompasses grasping, placing, and contact-rich interactions. Recent advances combine learning with geometric reasoning.

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
"""
    },
    "dexterous": {
        "title": "Dexterous Manipulation",
        "intro": """Dexterous manipulation using multi-fingered hands enables human-like object interactions. Recent progress combines novel hardware with learning-based control.

## What is Dexterous Manipulation?

Dexterous manipulation uses articulated hands with 15-20 DoFs for complex grasps and in-hand manipulations.

## Key Approaches

### Low-Cost Hardware
**RUKA** provides affordable, 3D-printed tendon-driven hands.

### Teleoperation
**DexUMI** uses human hands as manipulation interfaces.

## Important Considerations

- **Hardware complexity**: Many actuators and contact points
- **Control difficulty**: High-dimensional action spaces
- **Tactile sensing**: Fingertip force/torque sensors crucial
"""
    },
    "mobile_manipulation": {
        "title": "Mobile Manipulation & Navigation",
        "intro": """Mobile manipulation combines navigation and manipulation, enabling robots to move through environments and perform tasks.

## What is Mobile Manipulation?

Mobile manipulation involves robots with mobility and manipulation capabilities for multi-room tasks.

## Key Approaches

### Language-Guided Systems
**TidyBot** uses LLMs for personalized robot assistance.

### Vision-Based Navigation
**NoMaD** employs diffusion policies for navigation.

## Important Considerations

- **Task decomposition**: Navigation and manipulation subgoals
- **Multi-room reasoning**: Planning across spaces
- **Energy efficiency**: Battery optimization
"""
    },
    "perception": {
        "title": "Perception & Scene Understanding",
        "intro": """Perception systems extract structured information from sensors. Recent advances leverage foundation models for zero-shot generalization.

## What is Robot Perception?

Robot perception processes sensors to extract object locations, poses, and semantic labels.

## Key Approaches

### Vision Foundation Models
**DINOv2** provides self-supervised visual features.

### 6D Pose Estimation
**FoundationPose** unifies pose estimation for novel objects.

## Important Considerations

- **Lighting robustness**: Handling varied illumination
- **Real-time performance**: 30+ Hz processing
- **Multimodal fusion**: RGB, depth, and tactile sensing
"""
    },
    "hri_planning": {
        "title": "HRI & Task Planning",
        "intro": """Human-Robot Interaction and task planning enable robots to understand commands and decompose them into actions. Recent breakthroughs use LLMs.

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
"""
    }
}

def get_papers_for_domain(domain: str, papers_file: Path) -> list[dict]:
    with open(papers_file, 'r') as f:
        papers = json.load(f)

    domain_papers = [p for p in papers if domain in p.get('domains', [])]
    papers_with_scores = [(p, score_paper(p)) for p in domain_papers]
    papers_with_scores.sort(key=lambda x: x[1], reverse=True)

    return [p for p, _ in papers_with_scores]

def load_previous_trends(domain: str, data_dir: Path) -> str | None:
    trends_file = data_dir / f"trends_{domain}.txt"
    if trends_file.exists():
        with open(trends_file, 'r') as f:
            return f.read()
    return None

def save_trends(domain: str, trends: str, data_dir: Path):
    trends_file = data_dir / f"trends_{domain}.txt"
    with open(trends_file, 'w') as f:
        f.write(trends)

def download_paper_pdfs(papers: list[dict], temp_dir: str, max_papers: int = 5) -> dict[str, str]:
    pdf_paths = {}

    for paper in papers[:max_papers]:
        arxiv_id = paper['arxiv']['arxiv_id'].split('v')[0]
        pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
        pdf_path = os.path.join(temp_dir, f"{arxiv_id}.pdf")

        try:
            response = requests.get(pdf_url, timeout=30)
            response.raise_for_status()

            with open(pdf_path, 'wb') as f:
                f.write(response.content)

            pdf_paths[arxiv_id] = pdf_path
            print(f"    Downloaded {arxiv_id}.pdf")
        except Exception as e:
            print(f"    Failed to download {arxiv_id}: {e}")

    return pdf_paths

def extract_paper_content_from_pdfs(pdf_paths: dict[str, str]) -> str:
    if not pdf_paths:
        return ""

    paper_contents = []

    for arxiv_id, pdf_path in pdf_paths.items():
        try:
            with open(pdf_path, 'rb') as f:
                pdf_data = f.read()

            pdf_part = types.Part.from_bytes(
                data=pdf_data,
                mime_type="application/pdf"
            )

            response = gemini_client.models.generate_content(
                model="gemini-2.0-flash-exp",
                contents=[
                    pdf_part,
                    "Extract key technical content: contributions, methods, experiments, results. Provide 500-800 word summary with technical details."
                ]
            )

            paper_contents.append(f"Paper {arxiv_id}:\n{response.text}\n")
            print(f"    Extracted content from {arxiv_id}")
        except Exception as e:
            print(f"    Failed to extract {arxiv_id}: {e}")

    return "\n\n".join(paper_contents)

def generate_trends_with_gemini(domain: str, papers: list[dict], previous_trends: str | None, paper_full_content: str = "") -> str:
    domain_title = DOMAIN_STATIC_CONTENT.get(domain, {}).get('title', domain)

    papers_summary = "\n".join([
        f"- {p['arxiv']['title']} ({p['arxiv']['published_date']})\n  Citations: {p['semantic_scholar'].get('citation_count', 0)}, Stars: {p['github'].get('stars', 0)}"
        for p in papers[:10]
    ])

    previous_context = ""
    if previous_trends:
        previous_context = f"\n\nPREVIOUS TRENDS:\n{previous_trends}"

    full_content_context = ""
    if paper_full_content:
        full_content_context = f"\n\nFULL PAPER CONTENT:\n{paper_full_content}"

    prompt = f"""Analyze latest papers in {domain_title} and generate trends report.

PAPERS:
{papers_summary}
{full_content_context}
{previous_context}

Generate analysis covering:

### 1. Emerging Techniques
What new methods are gaining traction?

### 2. Key Innovations
What breakthroughs stand out?

### 3. Research Directions
Where is the field heading?

### 4. Open Challenges
What unsolved problems exist?

### 5. Promising Areas for Exploration
What needs more research?

Write clearly for researchers. Focus on concrete technical details. Keep concise (400-600 words).

Return ONLY the analysis with section headers, no preamble.
"""

    response = gemini_client.models.generate_content(
        model="gemini-2.0-flash-exp",
        contents=prompt
    )

    return response.text.strip()

def format_number(num):
    if num is None:
        return "—"
    if num >= 1000:
        return f"{num/1000:.1f}k"
    return str(num)

def format_date(date_str):
    if not date_str:
        return "—"
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.strftime("%b %d, %Y")
    except:
        return date_str

def truncate_title(title, max_len=40):
    if len(title) <= max_len:
        return title
    return title[:max_len-3] + "..."

def generate_paper_row(paper):
    arxiv = paper["arxiv"]
    github = paper["github"]
    twitter = paper["twitter"]
    semantic = paper["semantic_scholar"]

    arxiv_id = arxiv["arxiv_id"].split("v")[0]
    title = truncate_title(arxiv["title"])
    paper_md = f"../papers/{arxiv_id}.md"

    github_str = "—"
    if github.get("repo_url"):
        repo_url = github["repo_url"]
        stars = format_number(github.get("stars"))
        forks = format_number(github.get("forks"))
        github_str = f"⭐[{stars}]({repo_url})<br>🔀[{forks}]({repo_url})"

    citation_str = "—"
    if semantic.get("citation_count") is not None:
        citations = format_number(semantic.get("citation_count"))
        influential = semantic.get("influential_citation_count")

        if semantic.get("paper_id"):
            s2_url = f"https://www.semanticscholar.org/paper/{semantic['paper_id']}"
            if influential and influential > 0:
                citation_str = f"[{citations}]({s2_url})<br>📈{influential}"
            else:
                citation_str = f"[{citations}]({s2_url})"
        else:
            citation_str = citations

    twitter_str = "—"
    tweet_url = twitter.get("tweet_url")
    if tweet_url and (twitter.get("likes") or twitter.get("retweets") or twitter.get("views")):
        likes = f"❤️[{format_number(twitter['likes'])}]({tweet_url})" if twitter.get("likes") else ""
        retweets = f"🔁[{format_number(twitter['retweets'])}]({tweet_url})" if twitter.get("retweets") else ""
        views = f"👁️[{format_number(twitter['views'])}]({tweet_url})" if twitter.get("views") else ""

        line1 = " ".join(filter(None, [likes, retweets]))
        line2 = views
        twitter_str = f"{line1}<br>{line2}" if line2 else line1

    date = format_date(arxiv.get("published_date", ""))
    authors_short = arxiv["authors"][0].split()[-1] + " et al." if arxiv["authors"] else "—"

    arxiv_link = f"[{arxiv_id}]({arxiv['arxiv_url']})"

    open_issues = github.get("open_issues", "—")

    latest_changes = f"[{date}]({paper_md})"

    return f"| [{title}]({paper_md}) | {arxiv_link} | {date} | {authors_short} | {github_str} | {citation_str} | {open_issues} | {latest_changes} | {twitter_str} |"

def generate_domain_page(domain: str, papers_file: Path, output_dir: Path, data_dir: Path):
    output_dir.mkdir(exist_ok=True)
    data_dir.mkdir(exist_ok=True)

    static_content = DOMAIN_STATIC_CONTENT.get(domain)
    if not static_content:
        print(f"  Warning: No static content for domain '{domain}'")
        return

    print(f"  Processing {domain}...")
    papers = get_papers_for_domain(domain, papers_file)
    previous_trends = load_previous_trends(domain, data_dir)

    paper_full_content = ""
    with tempfile.TemporaryDirectory() as temp_dir:
        print(f"    Downloading PDFs...")
        pdf_paths = download_paper_pdfs(papers, temp_dir, max_papers=5)

        if pdf_paths:
            print(f"    Extracting content from {len(pdf_paths)} PDFs...")
            paper_full_content = extract_paper_content_from_pdfs(pdf_paths)

    print(f"    Generating trends analysis...")
    trends = generate_trends_with_gemini(domain, papers, previous_trends, paper_full_content)
    save_trends(domain, trends, data_dir)

    content = f"""# {static_content['title']}

{static_content['intro']}

---

## 🔥 Latest Trends & Research Directions

*Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}*

{trends}

---

## 📄 Papers in This Domain

| Paper | PDF | Date | Authors | GitHub | Citations | Issues | Changes | Twitter |
|-------|-----|------|---------|--------|-----------|--------|---------|----------|
"""

    for paper in papers:
        content += generate_paper_row(paper) + "\n"

    content += """
---

*This page is automatically updated with the latest research trends and papers.*
"""

    domain_file = output_dir / f"{domain}.md"
    with open(domain_file, 'w') as f:
        f.write(content)

    print(f"  ✓ Generated {domain}.md")
    return domain_file

def generate_all_domain_pages(papers_file: Path, output_dir: Path, data_dir: Path):
    domains = list(DOMAIN_STATIC_CONTENT.keys())

    print(f"Generating {len(domains)} domain pages...\n")

    generated_files = []
    for domain in domains:
        try:
            domain_file = generate_domain_page(domain, papers_file, output_dir, data_dir)
            generated_files.append(domain_file)
        except Exception as e:
            print(f"  ✗ Error generating {domain}: {e}")

    print(f"\n✅ Generated {len(generated_files)} domain pages")
    return generated_files

if __name__ == "__main__":
    papers_file = Path(__file__).parent.parent / "data" / "papers.json"
    output_dir = Path(__file__).parent.parent / "domains"
    data_dir = Path(__file__).parent.parent / "data"

    generate_all_domain_pages(papers_file, output_dir, data_dir)
