import requests
from schemas import SemanticScholarMetrics


def fetch_semantic_scholar_metrics(arxiv_id: str) -> SemanticScholarMetrics:
    if not arxiv_id:
        return SemanticScholarMetrics()

    clean_arxiv_id = arxiv_id.replace("arXiv:", "").strip()

    params = {
        "fields": "paperId,citationCount,influentialCitationCount"
    }

    response = requests.get(
        f"https://api.semanticscholar.org/graph/v1/paper/arXiv:{clean_arxiv_id}",
        params=params
    )

    if response.status_code != 200:
        print(f"Semantic Scholar API error: {response.status_code}")
        return SemanticScholarMetrics()

    data = response.json()

    return SemanticScholarMetrics(
        paper_id=data.get("paperId"),
        citation_count=data.get("citationCount"),
        influential_citation_count=data.get("influentialCitationCount")
    )


if __name__ == "__main__":
    test_arxiv_ids = [
        "2402.10329",
        "2406.09246",
        "2504.13165"
    ]

    print("Testing Semantic Scholar API tracker...\n")
    for arxiv_id in test_arxiv_ids:
        print(f"Fetching citations for arXiv:{arxiv_id}")
        metrics = fetch_semantic_scholar_metrics(arxiv_id)
        print(f"  Paper ID: {metrics.paper_id}")
        print(f"  Citations: {metrics.citation_count}")
        print(f"  Influential Citations: {metrics.influential_citation_count}")
        print()
