import requests
import xml.etree.ElementTree as ET
from datetime import datetime
from schemas import ArxivPaper


def extract_arxiv_id_from_url(arxiv_url: str) -> str:
    if "arxiv.org/abs/" in arxiv_url:
        return arxiv_url.split("arxiv.org/abs/")[-1].strip()
    return arxiv_url.strip()


def fetch_arxiv_metadata(arxiv_url: str) -> ArxivPaper:
    arxiv_id = extract_arxiv_id_from_url(arxiv_url)

    response = requests.get(
        "http://export.arxiv.org/api/query",
        params={"id_list": arxiv_id, "max_results": 1}
    )

    if response.status_code != 200:
        raise Exception(f"arXiv API error: {response.status_code}")

    root = ET.fromstring(response.content)
    ns = {"atom": "http://www.w3.org/2005/Atom"}

    entry = root.find("atom:entry", ns)
    if entry is None:
        raise Exception(f"Paper not found: {arxiv_id}")

    title = entry.find("atom:title", ns).text.replace("\n", " ").strip()
    summary = entry.find("atom:summary", ns).text.replace("\n", " ").strip()
    published = entry.find("atom:published", ns).text
    published_date = datetime.fromisoformat(published.replace("Z", "+00:00")).strftime("%Y-%m-%d")

    authors = []
    for author in entry.findall("atom:author", ns):
        name = author.find("atom:name", ns)
        if name is not None:
            authors.append(name.text)

    categories = []
    for category in entry.findall("atom:category", ns):
        term = category.get("term")
        if term:
            categories.append(term)

    arxiv_id_clean = arxiv_id.split("v")[0]

    return ArxivPaper(
        arxiv_id=arxiv_id,
        title=title,
        authors=authors,
        summary=summary,
        published_date=published_date,
        pdf_url=f"https://arxiv.org/pdf/{arxiv_id}.pdf",
        arxiv_url=f"https://arxiv.org/abs/{arxiv_id_clean}",
        categories=categories
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
        
