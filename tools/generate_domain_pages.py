import json
import os
import tempfile
import requests
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv
from google import genai
from google.genai import types
import arxiv

try:
    from googlesearch import search as google_search
    HAS_GOOGLE_SEARCH = True
except ImportError:
    HAS_GOOGLE_SEARCH = False

load_dotenv()

gemini_client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
arxiv_client = arxiv.Client()

DOMAIN_STATIC_CONTENT = {
    "data_collection": {
        "title": "Data Collection & Datasets in Robotics",
        "intro": """Data collection is the foundation of modern robot learning. High-quality, diverse datasets enable robots to learn complex behaviors through imitation learning, reinforcement learning, and other data-driven approaches.

## What is Robot Data Collection?

Robot data collection involves capturing demonstrations, teleoperation sequences, or autonomous exploration data that captures the relationship between sensory inputs (vision, proprioception, force/torque) and robot actions. This data serves as the training material for robot learning algorithms.

## Key Methods

### Teleoperation
Using interfaces like VR controllers, haptic devices, or custom grippers to collect human demonstrations. Examples include:
- **UMI (Universal Manipulation Interface)**: Portable hand-held grippers for in-the-wild data collection
- **ALOHA**: Low-cost bimanual teleoperation system
- **VR Teleoperation**: Immersive control using VR headsets

### Autonomous Data Collection
Robots autonomously explore and collect data through:
- **Self-supervised learning**: Learning from raw sensory data without labels
- **Random exploration**: Collecting diverse interaction data
- **Scripted behaviors**: Pre-programmed routines to gather structured data

### Sim-to-Real Transfer
Generating synthetic data in simulation and transferring to real robots:
- **Domain randomization**: Varying simulation parameters for robustness
- **Realistic rendering**: High-fidelity physics and graphics
- **Sim2Real datasets**: Paired simulation and real-world data

## Important Considerations

- **Data diversity**: Varied environments, objects, and scenarios improve generalization
- **Data quality**: Clean labels, accurate timestamps, and synchronized sensors
- **Data scale**: Larger datasets generally lead to better performance
- **Data efficiency**: Techniques to learn from limited demonstrations
- **Safety**: Ensuring safe data collection without damaging robots or environments

## Notable Datasets

- **Open X-Embodiment**: Large-scale multi-robot dataset
- **DROID**: Distributed robot interaction dataset
- **RoboNet**: Cross-embodiment dataset for robot learning
- **Bridge Data**: Large-scale manipulation dataset
""",
    },
    "vla": {
        "title": "Vision-Language-Action (VLA) Models",
        "intro": """Vision-Language-Action (VLA) models represent a paradigm shift in robot learning, combining visual perception, natural language understanding, and action generation in a single end-to-end model.

## What are VLA Models?

VLAs are neural networks that take visual observations and language instructions as input and directly output low-level robot actions. They leverage large-scale vision-language pretraining (like CLIP, PaLI) to achieve strong generalization to new tasks and environments.

## Architecture

VLAs typically consist of:
- **Vision Encoder**: Processes camera images (e.g., DINOv2, SigLIP, ViT)
- **Language Encoder**: Processes natural language instructions (e.g., T5, LLaMA)
- **Action Decoder**: Generates robot actions (end-effector poses, joint angles, gripper commands)

## Key Advantages

- **Language Grounding**: Natural language provides semantic context and task specification
- **Pretrained Representations**: Leverages internet-scale vision-language data
- **Generalization**: Zero-shot or few-shot transfer to new tasks and objects
- **Multimodal Reasoning**: Combines visual and linguistic information

## Training Approaches

- **Imitation Learning**: Learning from human demonstrations with language annotations
- **Fine-tuning**: Adapting pretrained VLMs to robot control
- **LoRA/Adapter Methods**: Efficient fine-tuning with low-rank adaptations
- **Multi-task Training**: Joint training across diverse tasks and embodiments

## Challenges

- **Compute Requirements**: Large models require significant GPU resources
- **Data Collection**: Need paired vision-language-action demonstrations
- **Real-time Inference**: Latency constraints for robot control
- **Safety**: Ensuring language instructions don't lead to unsafe behaviors

## Notable Models

- **RT-2**: Vision-language-action model from Google DeepMind
- **OpenVLA**: Open-source 7B parameter VLA model
- **PaLM-E**: Embodied multimodal language model
- **GR-1**: Generalist robot agent
""",
    },
    "manipulation": {
        "title": "Robot Manipulation",
        "intro": """Robot manipulation is the core capability enabling robots to interact with and modify their physical environment. From grasping objects to complex bimanual assembly, manipulation research spans hardware design, control, perception, and learning.

## What is Robot Manipulation?

Manipulation encompasses all robot behaviors that involve physical interaction with objects: picking, placing, reorienting, assembling, deforming, and more. It requires coordinating perception (seeing the object), planning (how to grasp it), and control (executing the motion).

## Key Components

### End Effectors
- **Parallel Grippers**: Simple two-finger grippers for basic grasping
- **Multi-fingered Hands**: Dexterous hands with many degrees of freedom (e.g., Shadow Hand, Allegro Hand, RUKA)
- **Suction Grippers**: Vacuum-based grasping for flat objects
- **Soft Grippers**: Compliant materials for delicate objects

### Manipulation Primitives
- **Pick and Place**: Fundamental operation for object rearrangement
- **In-hand Manipulation**: Reorienting objects within the gripper
- **Bimanual Manipulation**: Coordinating two arms for complex tasks
- **Contact-rich Manipulation**: Tasks involving sliding, pushing, or rolling

### Control Approaches
- **Position Control**: Directly commanding end-effector or joint positions
- **Force Control**: Regulating contact forces and torques
- **Impedance Control**: Balancing position and force compliance
- **Hybrid Control**: Combining position and force control

## Learning Paradigms

- **Imitation Learning**: Learning from human or expert demonstrations
- **Reinforcement Learning**: Learning through trial and error
- **Model-based RL**: Using learned dynamics models for planning
- **Diffusion Policies**: Generating action sequences via diffusion models

## Challenges

- **Contact Dynamics**: Modeling and controlling contact interactions
- **Partial Observability**: Occlusions and limited sensor views
- **Generalization**: Adapting to new objects, poses, and environments
- **Long-horizon Tasks**: Planning and executing multi-step behaviors
- **Safety**: Preventing collisions and unsafe forces

## Application Domains

- **Warehouse Automation**: Bin picking, packing, sorting
- **Manufacturing**: Assembly, welding, quality inspection
- **Household Robotics**: Cooking, cleaning, laundry
- **Healthcare**: Surgical assistance, rehabilitation
""",
    },
}


def get_papers_for_domain(domain: str, papers_file: Path) -> list[dict]:
    with open(papers_file, 'r') as f:
        papers = json.load(f)

    return [p for p in papers if domain in p.get('domains', [])]


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


def download_paper_pdfs(papers: list[dict], temp_dir: str) -> dict[str, str]:
    pdf_paths = {}

    for paper in papers[:10]:
        arxiv_id = paper['arxiv']['arxiv_id'].split('v')[0]
        pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
        pdf_path = os.path.join(temp_dir, f"{arxiv_id}.pdf")

        try:
            response = requests.get(pdf_url, timeout=30)
            response.raise_for_status()

            with open(pdf_path, 'wb') as f:
                f.write(response.content)

            pdf_paths[arxiv_id] = pdf_path
            print(f"  Downloaded {arxiv_id}.pdf")
        except Exception as e:
            print(f"  Failed to download {arxiv_id}: {e}")

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
                model="gemini-2.5-flash",
                contents=[
                    pdf_part,
                    "Extract the key technical content from this paper including: main contributions, methods, experiments, and results. Provide a comprehensive summary (500-800 words) focusing on technical details."
                ]
            )

            paper_contents.append(f"Paper {arxiv_id}:\n{response.text}\n")
            print(f"  Extracted content from {arxiv_id}")
        except Exception as e:
            print(f"  Failed to extract content from {arxiv_id}: {e}")

    return "\n\n".join(paper_contents)


def generate_trends_with_gemini(domain: str, papers: list[dict], previous_trends: str | None, web_search_results: str = "", paper_full_content: str = "") -> str:
    domain_title = DOMAIN_STATIC_CONTENT.get(domain, {}).get('title', domain)

    papers_summary = "\n".join([
        f"- {p['arxiv']['title']} ({p['arxiv']['published_date']})\n  Citations: {p['semantic_scholar'].get('citation_count', 0)}, Stars: {p['github'].get('stars', 0)}"
        for p in papers[:10]
    ])

    previous_context = ""
    if previous_trends:
        previous_context = f"\n\nPREVIOUS TREND ANALYSIS (use this to provide continuity and identify NEW developments):\n{previous_trends}"

    web_context = ""
    if web_search_results:
        web_context = f"\n\nWEB SEARCH RESULTS (latest research trends):\n{web_search_results}"

    full_content_context = ""
    if paper_full_content:
        full_content_context = f"\n\nFULL PAPER CONTENT (use this detailed technical content for deeper analysis):\n{paper_full_content}"

    prompt = f"""You are a robotics research analyst. Analyze the latest papers in {domain_title} and generate a comprehensive trends report.

PAPERS IN THIS DOMAIN:
{papers_summary}
{full_content_context}
{previous_context}
{web_context}

Generate a detailed trends analysis covering:

1. **Emerging Techniques**: What new methods or approaches are gaining traction?
2. **Key Innovations**: What breakthroughs or novel ideas stand out?
3. **Research Directions**: Where is the field heading? What problems are researchers focused on?
4. **Open Challenges**: What unsolved problems or gaps exist?
5. **Promising Areas for Exploration**: What areas need more research or could yield significant impact?

Write in a clear, informative style suitable for researchers. Focus on actionable insights and concrete technical details from the papers. Keep the analysis concise but comprehensive (400-600 words).

Return ONLY the trends analysis text, no preamble or meta-commentary.
"""

    response = gemini_client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text.strip()


def google_search_trends(domain: str) -> str:
    if not HAS_GOOGLE_SEARCH:
        return ""

    domain_keywords = {
        "data_collection": "robotics data collection datasets teleoperation",
        "vla": "vision language action models VLA robotics",
        "manipulation": "robot manipulation dexterous grasping",
    }

    query = domain_keywords.get(domain, f"robotics {domain}")

    try:
        results = []
        for url in google_search(f"{query} latest research 2025", num_results=5):
            results.append(url)
        return f"Latest research URLs:\n" + "\n".join(results)
    except:
        return ""


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


def truncate_title(title, max_len=60):
    if len(title) <= max_len:
        return title
    return title[:max_len-3] + "..."


def generate_paper_row(paper):
    arxiv = paper["arxiv"]
    github = paper["github"]
    twitter = paper["twitter"]
    semantic = paper["semantic_scholar"]

    arxiv_id = arxiv["arxiv_id"].split("v")[0]
    title = truncate_title(arxiv["title"], 45)
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


def generate_domain_page(domain: str, papers_file: Path, output_dir: Path, data_dir: Path, use_search: bool = True):
    output_dir.mkdir(exist_ok=True)
    data_dir.mkdir(exist_ok=True)

    static_content = DOMAIN_STATIC_CONTENT.get(domain)
    if not static_content:
        print(f"Warning: No static content for domain '{domain}'")
        return

    papers = get_papers_for_domain(domain, papers_file)
    previous_trends = load_previous_trends(domain, data_dir)

    web_results = ""
    if use_search:
        web_results = google_search_trends(domain)

    paper_full_content = ""
    with tempfile.TemporaryDirectory() as temp_dir:
        print(f"  Downloading PDFs for {domain}...")
        pdf_paths = download_paper_pdfs(papers, temp_dir)

        if pdf_paths:
            print(f"  Extracting content from {len(pdf_paths)} PDFs...")
            paper_full_content = extract_paper_content_from_pdfs(pdf_paths)

    print(f"  Generating trends analysis for {domain}...")
    trends = generate_trends_with_gemini(domain, papers, previous_trends, web_results, paper_full_content)
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

*This page is automatically updated daily with the latest research trends and papers.*
"""

    domain_file = output_dir / f"{domain}.md"
    with open(domain_file, 'w') as f:
        f.write(content)

    return domain_file


def generate_all_domain_pages(papers_file: Path, output_dir: Path, data_dir: Path):
    domains = ["data_collection", "vla", "manipulation"]

    generated_files = []
    for domain in domains:
        domain_file = generate_domain_page(domain, papers_file, output_dir, data_dir)
        print(f"✓ Generated {domain}.md")
        generated_files.append(domain_file)

    return generated_files


if __name__ == "__main__":
    papers_file = Path(__file__).parent.parent / "data" / "papers.json"
    output_dir = Path(__file__).parent.parent / "domains"
    data_dir = Path(__file__).parent.parent / "data"

    print("Generating domain pages...\n")
    generated_files = generate_all_domain_pages(papers_file, output_dir, data_dir)
    print(f"\n✓ Generated {len(generated_files)} domain pages in {output_dir}")
