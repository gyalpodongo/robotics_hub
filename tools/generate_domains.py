import json
from pathlib import Path
from datetime import datetime
from scoring import score_paper

DOMAIN_INFO = {
    "vla": {
        "title": "Foundation Models & VLAs",
        "description": "Vision-Language-Action models and foundation models for robotics. These models combine vision, language, and action to enable versatile robotic manipulation and decision-making."
    },
    "policy_methods": {
        "title": "Policy Learning Methods",
        "description": "Advanced methods for learning robot policies, including diffusion policies, consistency models, and autoregressive approaches. Focus on imitation learning and visuomotor control."
    },
    "rl": {
        "title": "Reinforcement Learning",
        "description": "Reinforcement learning approaches for robotics, including reward design, LLM-guided RL, and open-ended exploration."
    },
    "data_collection": {
        "title": "Data Collection & Teleoperation",
        "description": "Hardware and software systems for collecting high-quality robot demonstration data, including teleoperation interfaces and data collection frameworks."
    },
    "datasets": {
        "title": "Datasets & Benchmarks",
        "description": "Large-scale datasets and benchmarks for robot learning, enabling cross-embodiment transfer and standardized evaluation."
    },
    "sim_to_real": {
        "title": "Simulation & Sim-to-Real",
        "description": "Bridging the gap between simulation and reality through domain randomization, digital twins, procedural generation, and video-to-reality techniques."
    },
    "manipulation": {
        "title": "Manipulation",
        "description": "General manipulation research including grasping, contact-rich tasks, compliance control, and object manipulation."
    },
    "dexterous": {
        "title": "Dexterous Manipulation",
        "description": "Dexterous manipulation using robotic hands and multi-fingered grippers for complex, precise manipulation tasks."
    },
    "mobile_manipulation": {
        "title": "Mobile Manipulation",
        "description": "Combining navigation and manipulation for mobile robots, including whole-body control and task planning."
    },
    "perception": {
        "title": "Perception",
        "description": "Vision and perception systems for robotics, including object detection, pose estimation, and foundation vision models."
    },
    "hri_planning": {
        "title": "HRI & Task Planning",
        "description": "Human-robot interaction, natural language interfaces, and high-level task planning using LLMs and classical planning methods."
    }
}

def generate_domain_table(papers: list[dict]) -> str:
    if not papers:
        return "_No papers in this domain yet._\n"

    papers_with_scores = [(p, score_paper(p)) for p in papers]
    papers_with_scores.sort(key=lambda x: x[1], reverse=True)

    table = "| Paper | arXiv | Date | GitHub | Stars | Citations | Twitter | Summary |\n"
    table += "|-------|-------|------|--------|-------|-----------|---------|----------|\n"

    for paper, score in papers_with_scores:
        arxiv = paper['arxiv']
        github = paper.get('github', {})
        twitter = paper.get('twitter', {})
        semantic = paper.get('semantic_scholar', {})

        title = arxiv['title'][:35] + "..." if len(arxiv['title']) > 35 else arxiv['title']
        arxiv_id = arxiv['arxiv_id'].split('v')[0]
        arxiv_url = f"https://arxiv.org/abs/{arxiv_id}"
        pub_date = arxiv['published_date']

        authors = ", ".join(arxiv['authors'][:2])
        if len(arxiv['authors']) > 2:
            authors += " et al."

        summary_lines = []
        summary_lines.append(f"[{title}]({arxiv_url})")
        summary_lines.append(f"_{authors}_")
        summary = "<br>".join(summary_lines)

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
        s2_url = f"https://www.semanticscholar.org/paper/{semantic.get('paper_id')}"

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
            twitter_parts.append(f"❤️ {likes:,}")
        if retweets:
            twitter_parts.append(f"🔄 {retweets:,}")

        twitter_lines = []
        if twitter_url and twitter_parts:
            line1 = " ".join(twitter_parts)
            twitter_lines.append(f"[{line1}]({twitter_url})")

        if views:
            twitter_lines.append(f"👁️ {views:,}")

        twitter_cell = "<br>".join(twitter_lines) if twitter_lines else "-"

        first_sentence = arxiv['summary'].split('.')[0] + '.'
        if len(first_sentence) > 100:
            first_sentence = first_sentence[:97] + "..."

        table += f"| {summary} | {arxiv_id} | {pub_date} | {github_cell} | {stars_cell} | {citation_cell} | {twitter_cell} | {first_sentence} |\n"

    return table

def generate_domain_markdown(domain_key: str, papers: list[dict]) -> str:
    info = DOMAIN_INFO[domain_key]

    md = f"""# {info['title']}

{info['description']}

**Total Papers**: {len(papers)}

---

## Papers

{generate_domain_table(papers)}

---

_Last updated: {datetime.now().strftime('%Y-%m-%d')}_
"""
    return md

def generate_all_domain_files(papers_file: Path, output_dir: Path):
    with open(papers_file, 'r') as f:
        papers = json.load(f)

    output_dir.mkdir(exist_ok=True)

    papers_by_domain = {}
    for paper in papers:
        for domain in paper.get('domains', []):
            if domain not in papers_by_domain:
                papers_by_domain[domain] = []
            papers_by_domain[domain].append(paper)

    print(f"Generating domain markdown files...\n")

    for domain_key, domain_papers in papers_by_domain.items():
        if domain_key not in DOMAIN_INFO:
            print(f"⚠️  Unknown domain: {domain_key}, skipping...")
            continue

        filename = f"{domain_key}.md"
        filepath = output_dir / filename

        md_content = generate_domain_markdown(domain_key, domain_papers)

        with open(filepath, 'w') as f:
            f.write(md_content)

        print(f"✓ Generated {filename} ({len(domain_papers)} papers)")

    print(f"\n✅ Generated {len(papers_by_domain)} domain files in {output_dir}")

if __name__ == "__main__":
    papers_file = Path(__file__).parent.parent / "data" / "papers.json"
    output_dir = Path(__file__).parent.parent / "domains"

    generate_all_domain_files(papers_file, output_dir)
