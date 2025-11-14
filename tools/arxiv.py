import arxiv
from schemas import ArxivPaper


def extract_arxiv_id_from_url(arxiv_url: str) -> str:
    if "arxiv.org/abs/" in arxiv_url:
        return arxiv_url.split("arxiv.org/abs/")[-1].strip()
    return arxiv_url.strip()


def fetch_arxiv_metadata(arxiv_url: str) -> ArxivPaper:
    arxiv_id = extract_arxiv_id_from_url(arxiv_url)

    client = arxiv.Client()
    search = arxiv.Search(id_list=[arxiv_id])

    result = next(client.results(search))

    return ArxivPaper(
        arxiv_id=result.get_short_id(),
        title=result.title,
        authors=[author.name for author in result.authors],
        summary=result.summary.replace("\n", " ").strip(),
        published_date=result.published.strftime("%Y-%m-%d"),
        pdf_url=result.pdf_url,
        arxiv_url=f"https://arxiv.org/abs/{result.get_short_id()}",
        categories=result.categories
    )


if __name__ == "__main__":
    test_urls = [
        "https://arxiv.org/abs/2402.10329",
        "https://arxiv.org/abs/2406.09246",
        "https://arxiv.org/abs/2504.13165"
    ]

    print("Testing arXiv API tracker...\n")
    for url in test_urls:
        print(f"Fetching: {url}")
        paper = fetch_arxiv_metadata(url)
        print(f"  Title: {paper.title}")
        print(f"  Authors: {', '.join(paper.authors[:3])}...")
        print(f"  Date: {paper.published_date}")
        print(f"  arXiv ID: {paper.arxiv_id}")
        print()
        print()
        
