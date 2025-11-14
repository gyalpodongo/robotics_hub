import json
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

from arxiv import fetch_arxiv_metadata
from github import fetch_github_metrics
from twitter import fetch_twitter_metrics_batch, extract_tweet_id_from_url
from semantic_scholar import fetch_semantic_scholar_metrics
from schemas import Paper

def collect_all_papers(seed_file: Path, output_file: Path):
    with open(seed_file, 'r') as f:
        seeds = json.load(f)

    print(f"Loading {len(seeds)} seed papers...")

    papers = []
    twitter_batch = []

    for i, seed in enumerate(seeds, 1):
        print(f"\n[{i}/{len(seeds)}] Processing {seed['arxiv_url']}...")

        try:
            arxiv_data = fetch_arxiv_metadata(seed['arxiv_url'])

            if not arxiv_data:
                print(f"  ⚠️  Failed to fetch arXiv data")
                continue

            github_data = fetch_github_metrics(seed.get('github_url'))
            semantic_data = fetch_semantic_scholar_metrics(arxiv_data.arxiv_id.split('v')[0])

            if seed.get('twitter_url'):
                tweet_id = extract_tweet_id_from_url(seed['twitter_url'])
                twitter_batch.append((seed['twitter_url'], tweet_id, i-1))

            paper = Paper(
                arxiv=arxiv_data,
                github=github_data,
                twitter=None,
                semantic_scholar=semantic_data,
                domains=seed.get('domains', []),
                tags=seed.get('tags', [])
            )

            papers.append(paper)
            print(f"  ✓ arXiv: {arxiv_data.title[:50]}...")
            print(f"  ✓ GitHub: {github_data.stars if github_data.stars else 'N/A'} stars")
            print(f"  ✓ Citations: {semantic_data.citation_count if semantic_data.citation_count else 'N/A'}")

        except Exception as e:
            print(f"  ✗ Error: {str(e)}")
            continue

    print(f"\n\nFetching Twitter metrics in batch for {len(twitter_batch)} tweets...")
    if twitter_batch:
        twitter_data = [(url, tid) for url, tid, _ in twitter_batch]
        twitter_results = fetch_twitter_metrics_batch(twitter_data)

        for url, tid, idx in twitter_batch:
            if idx < len(papers):
                papers[idx].twitter = twitter_results.get(url)
                metrics = twitter_results.get(url)
                if metrics and metrics.likes:
                    print(f"  ✓ Tweet {idx+1}: {metrics.likes} likes, {metrics.views} views")

    print(f"\n\n✓ Successfully collected {len(papers)} papers")

    papers_dict = [paper.model_dump() for paper in papers]

    with open(output_file, 'w') as f:
        json.dump(papers_dict, f, indent=2)

    print(f"✓ Saved to {output_file}")

    return papers

if __name__ == "__main__":
    seed_file = Path(__file__).parent.parent / "data" / "seed_papers.json"
    output_file = Path(__file__).parent.parent / "data" / "papers.json"

    collect_all_papers(seed_file, output_file)
