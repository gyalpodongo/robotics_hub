import json
import time
from pathlib import Path
from arxiv_fetch import fetch_arxiv_metadata
from github import fetch_github_metrics
from twitter import fetch_twitter_metrics_batch, extract_tweet_id_from_url
from semantic_scholar import fetch_semantic_scholar_metrics
from schemas import Paper, TwitterMetrics


def collect_all_papers(seed_file: Path, output_file: Path):
    with open(seed_file, 'r') as f:
        seeds = json.load(f)

    print(f"📚 Loading {len(seeds)} seed papers...\n")

    papers_data = {}

    print("=" * 60)
    print("STEP 1: Fetching arXiv metadata")
    print("=" * 60)
    for i, seed in enumerate(seeds, 1):
        arxiv_url = seed['arxiv_url']
        print(f"[{i}/{len(seeds)}] {arxiv_url}")

        try:
            arxiv_data = fetch_arxiv_metadata(arxiv_url)
            papers_data[arxiv_url] = {
                'arxiv': arxiv_data,
                'github_url': seed.get('github_url'),
                'twitter_url': seed.get('twitter_url'),
                'domains': seed.get('domains', []),
                'tags': seed.get('tags', [])
            }
            print(f"  ✓ {arxiv_data.title[:70]}...")
            time.sleep(1)
        except Exception as e:
            print(f"  ✗ Error: {str(e)}")
            continue

    print(f"\n✓ Collected {len(papers_data)} arXiv papers\n")

    print("=" * 60)
    print("STEP 2: Fetching GitHub metrics")
    print("=" * 60)
    for i, (arxiv_url, data) in enumerate(papers_data.items(), 1):
        github_url = data['github_url']
        if github_url:
            print(f"[{i}/{len(papers_data)}] {github_url}")
            try:
                github_data = fetch_github_metrics(github_url)
                data['github'] = github_data
                if github_data.stars:
                    print(f"  ✓ {github_data.stars} stars, {github_data.forks} forks")
                else:
                    print(f"  ✓ No metrics")
                time.sleep(0.5)
            except Exception as e:
                print(f"  ✗ Error: {str(e)}")
                from schemas import GitHubMetrics
                data['github'] = GitHubMetrics()
        else:
            from schemas import GitHubMetrics
            data['github'] = GitHubMetrics()

    print(f"\n✓ Collected GitHub metrics\n")

    print("=" * 60)
    print("STEP 3: Fetching Semantic Scholar citations")
    print("=" * 60)
    for i, (arxiv_url, data) in enumerate(papers_data.items(), 1):
        arxiv_id = data['arxiv'].arxiv_id.split('v')[0]
        print(f"[{i}/{len(papers_data)}] {arxiv_id}")
        try:
            semantic_data = fetch_semantic_scholar_metrics(arxiv_id)
            data['semantic'] = semantic_data
            if semantic_data.citation_count:
                print(f"  ✓ {semantic_data.citation_count} citations")
            else:
                print(f"  ✓ No citations yet")
            time.sleep(1)
        except Exception as e:
            print(f"  ✗ Error: {str(e)}")
            from schemas import SemanticScholarMetrics
            data['semantic'] = SemanticScholarMetrics()

    print(f"\n✓ Collected Semantic Scholar data\n")

    print("=" * 60)
    print("STEP 4: Fetching Twitter metrics (BATCH - ONCE)")
    print("=" * 60)
    twitter_batch = []
    twitter_url_to_arxiv = {}

    for arxiv_url, data in papers_data.items():
        twitter_url = data['twitter_url']
        if twitter_url:
            tweet_id = extract_tweet_id_from_url(twitter_url)
            twitter_batch.append((twitter_url, tweet_id))
            twitter_url_to_arxiv[twitter_url] = arxiv_url

    if twitter_batch:
        print(f"Fetching {len(twitter_batch)} tweets in batch...")
        twitter_results = fetch_twitter_metrics_batch(twitter_batch)

        for twitter_url, arxiv_url in twitter_url_to_arxiv.items():
            metrics = twitter_results.get(twitter_url, TwitterMetrics())
            papers_data[arxiv_url]['twitter'] = metrics
            if metrics.likes:
                print(f"  ✓ {twitter_url}: {metrics.likes} likes, {metrics.views} views")
    else:
        print("No Twitter URLs to fetch")

    for arxiv_url, data in papers_data.items():
        if 'twitter' not in data:
            data['twitter'] = TwitterMetrics()

    print(f"\n✓ Collected Twitter metrics\n")

    print("=" * 60)
    print("Creating Paper objects...")
    print("=" * 60)
    papers = []
    for arxiv_url, data in papers_data.items():
        paper = Paper(
            arxiv=data['arxiv'],
            github=data['github'],
            twitter=data['twitter'],
            semantic_scholar=data['semantic'],
            domains=data['domains'],
            tags=data['tags']
        )
        papers.append(paper)

    papers_dict = [paper.model_dump() for paper in papers]

    with open(output_file, 'w') as f:
        json.dump(papers_dict, f, indent=2)

    print(f"\n✅ Successfully collected {len(papers)} papers!")
    print(f"✅ Saved to {output_file}")

    return papers


if __name__ == "__main__":
    seed_file = Path(__file__).parent.parent / "data" / "seed_papers.json"
    output_file = Path(__file__).parent.parent / "data" / "papers.json"

    collect_all_papers(seed_file, output_file)
