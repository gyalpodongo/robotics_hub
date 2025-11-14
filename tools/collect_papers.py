import json
import time
from pathlib import Path
from arxiv import fetch_arxiv_metadata, extract_arxiv_id_from_url
from github import fetch_github_metrics
from twitter import fetch_twitter_metrics
from semantic_scholar import fetch_semantic_scholar_metrics
from schemas import Paper


def collect_paper_data(arxiv_url: str, twitter_url: str, github_url: str, domains: list[str], tags: list[str]) -> Paper:
    print(f"Collecting data for {arxiv_url}...")

    arxiv_data = fetch_arxiv_metadata(arxiv_url)
    print(f"  ✓ arXiv metadata fetched")

    time.sleep(1)

    github_data = fetch_github_metrics(github_url)
    print(f"  ✓ GitHub metrics fetched")

    time.sleep(3)

    twitter_data = fetch_twitter_metrics(twitter_url)
    print(f"  ✓ Twitter metrics fetched")

    time.sleep(3)

    arxiv_id = extract_arxiv_id_from_url(arxiv_url)
    semantic_data = fetch_semantic_scholar_metrics(arxiv_id)
    print(f"  ✓ Semantic Scholar metrics fetched")

    paper = Paper(
        arxiv=arxiv_data,
        github=github_data,
        twitter=twitter_data,
        semantic_scholar=semantic_data,
        domains=domains,
        tags=tags
    )

    print(f"  ✓ Paper data collected: {arxiv_data.title}\n")
    return paper


def load_seed_papers(seed_file: Path) -> list[dict]:
    with open(seed_file, 'r') as f:
        return json.load(f)


def save_papers(papers: list[Paper], output_file: Path):
    papers_dict = [paper.model_dump() for paper in papers]

    with open(output_file, 'w') as f:
        json.dump(papers_dict, f, indent=2)


if __name__ == "__main__":
    seed_file = Path(__file__).parent.parent / "data" / "seed_papers.json"
    output_file = Path(__file__).parent.parent / "data" / "papers.json"

    seed_papers = load_seed_papers(seed_file)

    papers = []
    for seed in seed_papers:
        paper = collect_paper_data(
            arxiv_url=seed["arxiv_url"],
            twitter_url=seed["twitter_url"],
            github_url=seed["github_url"],
            domains=seed["domains"],
            tags=seed.get("tags", [])
        )
        papers.append(paper)

        time.sleep(3)

    save_papers(papers, output_file)
    print(f"✓ Saved {len(papers)} papers to {output_file}")
