import json
from pathlib import Path

def generate_paper_markdown(paper: dict) -> str:
    arxiv = paper['arxiv']
    github = paper.get('github', {})
    twitter = paper.get('twitter', {})
    semantic = paper.get('semantic_scholar', {})

    title = arxiv['title']
    authors = ', '.join(arxiv['authors'])
    summary = arxiv['summary']
    pub_date = arxiv['published_date']
    arxiv_id = arxiv['arxiv_id'].split('v')[0]
    arxiv_url = f"https://arxiv.org/abs/{arxiv_id}"

    github_url = github.get('repo_url')
    stars = github.get('stars')
    forks = github.get('forks')

    twitter_url = twitter.get('tweet_url')
    likes = twitter.get('likes')
    retweets = twitter.get('retweets')
    views = twitter.get('views')

    citations = semantic.get('citation_count')
    influential = semantic.get('influential_citation_count')

    domains = ', '.join(paper.get('domains', []))
    tags = ', '.join([f'`{tag}`' for tag in paper.get('tags', [])])

    relevance_score = paper.get('relevance_score', 0)

    md = f"""# {title}

**Authors**: {authors}

**Published**: {pub_date}

**arXiv**: [{arxiv_id}]({arxiv_url})
"""

    if github_url:
        md += f"\n**GitHub**: [{github_url}]({github_url})"
        if stars:
            md += f" ⭐ {stars:,}"
        if forks:
            md += f" 🔀 {forks:,}"

    if twitter_url:
        md += f"\n\n**Twitter**: [Announcement Tweet]({twitter_url})"
        if likes:
            md += f" ❤️ {likes:,}"
        if retweets:
            md += f" 🔄 {retweets:,}"
        if views:
            md += f" 👁️ {views:,}"

    if citations:
        s2_url = f"https://www.semanticscholar.org/paper/{semantic.get('paper_id')}"
        md += f"\n\n**Citations**: [{citations:,}]({s2_url})"
        if influential:
            md += f" (📈 {influential} influential)"

    md += f"\n\n**Relevance Score**: {relevance_score:.1f}/100\n"
    md += f"\n**Domains**: {domains}\n"
    md += f"\n**Tags**: {tags}\n"
    md += f"\n---\n\n## Summary\n\n{summary}\n"

    return md

def generate_all_paper_files(papers_file: Path, output_dir: Path):
    with open(papers_file, 'r') as f:
        papers = json.load(f)

    output_dir.mkdir(exist_ok=True)

    print(f"Generating markdown files for {len(papers)} papers...\n")

    for i, paper in enumerate(papers, 1):
        arxiv_id = paper['arxiv']['arxiv_id'].split('v')[0]
        title = paper['arxiv']['title']

        filename = f"{arxiv_id}.md"
        filepath = output_dir / filename

        md_content = generate_paper_markdown(paper)

        with open(filepath, 'w') as f:
            f.write(md_content)

        print(f"[{i}/{len(papers)}] Generated {filename}")
        print(f"  {title[:70]}...")

    print(f"\n✅ Generated {len(papers)} paper files in {output_dir}")

if __name__ == "__main__":
    papers_file = Path(__file__).parent.parent / "data" / "papers.json"
    output_dir = Path(__file__).parent.parent / "papers"

    generate_all_paper_files(papers_file, output_dir)
