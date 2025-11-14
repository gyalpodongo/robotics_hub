from datetime import datetime
from typing import Optional

def calculate_relevance_score(
    citations: Optional[int],
    github_stars: Optional[int],
    twitter_views: Optional[int],
    published_date: str,
    recency_weight: float = 0.50,
    citation_weight: float = 0.30,
    github_weight: float = 0.15,
    twitter_weight: float = 0.05
) -> float:
    score = 0.0

    if citations is not None and citations > 0:
        citation_score = min(citations / 1000, 1.0)
        score += citation_score * citation_weight

    if github_stars is not None and github_stars > 0:
        github_score = min(github_stars / 5000, 1.0)
        score += github_score * github_weight

    if twitter_views is not None and twitter_views > 0:
        twitter_score = min(twitter_views / 500000, 1.0)
        score += twitter_score * twitter_weight

    pub_date = datetime.strptime(published_date, "%Y-%m-%d")
    now = datetime.now()
    days_old = (now - pub_date).days

    if days_old < 0:
        recency_score = 1.0
    elif days_old < 30:
        recency_score = 1.0
    elif days_old < 90:
        recency_score = 0.95
    elif days_old < 180:
        recency_score = 0.85
    elif days_old < 365:
        recency_score = 0.70
    elif days_old < 730:
        recency_score = 0.45
    elif days_old < 1095:
        recency_score = 0.25
    else:
        recency_score = max(0.05, 0.25 - (days_old - 1095) / 3650)

    score += recency_score * recency_weight

    return score * 100

def score_paper(paper_dict: dict) -> float:
    citations = paper_dict.get("semantic_scholar", {}).get("citation_count")
    github_stars = paper_dict.get("github", {}).get("stars")
    twitter_views = paper_dict.get("twitter", {}).get("views")
    published_date = paper_dict.get("arxiv", {}).get("published_date", "")

    return calculate_relevance_score(
        citations=citations,
        github_stars=github_stars,
        twitter_views=twitter_views,
        published_date=published_date
    )

if __name__ == "__main__":
    test_papers = [
        {
            "title": "OpenVLA (High engagement, recent)",
            "citations": 1100,
            "github_stars": 4400,
            "twitter_views": 226000,
            "date": "2024-06-13"
        },
        {
            "title": "RT-2 (Older, high citations)",
            "citations": 500,
            "github_stars": 1000,
            "twitter_views": 100000,
            "date": "2023-07-01"
        },
        {
            "title": "New paper (Very recent, low citations)",
            "citations": 5,
            "github_stars": 150,
            "twitter_views": 50000,
            "date": "2025-01-01"
        },
        {
            "title": "Classic (Old, many citations, no GitHub)",
            "citations": 2000,
            "github_stars": None,
            "twitter_views": None,
            "date": "2020-01-01"
        }
    ]

    print("Testing relevance scoring function:\n")
    print(f"{'Paper':<45} {'Score':>6} {'Citations':>10} {'Stars':>8} {'Views':>10} {'Date':>12}")
    print("=" * 100)

    for paper in test_papers:
        score = calculate_relevance_score(
            citations=paper["citations"],
            github_stars=paper["github_stars"],
            twitter_views=paper["twitter_views"],
            published_date=paper["date"]
        )

        print(f"{paper['title']:<45} {score:>6.1f} {paper['citations'] or 0:>10} {paper['github_stars'] or 0:>8} {paper['twitter_views'] or 0:>10} {paper['date']:>12}")
