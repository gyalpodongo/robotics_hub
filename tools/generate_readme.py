import json
from pathlib import Path
from datetime import datetime


def format_number(num):
    if num is None:
        return "—"
    if num >= 1000:
        return f"{num/1000:.1f}k"
    return str(num)


def format_date(date_str):
    from datetime import datetime
    if not date_str:
        return "—"
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.strftime("%b %d, %Y")
    except:
        return date_str


def truncate_title(title, max_len=40):
    if len(title) <= max_len:
        return title
    return title[:max_len-3] + "..."


def extract_summary(abstract, max_len=120):
    if not abstract:
        return "—"

    sentences = abstract.split(". ")
    summary = sentences[0]

    if len(summary) > max_len:
        summary = summary[:max_len-3] + "..."
    return summary


def generate_paper_row(paper):
    arxiv = paper["arxiv"]
    github = paper["github"]
    twitter = paper["twitter"]
    semantic = paper["semantic_scholar"]

    arxiv_id = arxiv["arxiv_id"].split("v")[0]
    title = truncate_title(arxiv["title"])
    paper_md = f"papers/{arxiv_id}.md"

    github_str = "—"
    if github.get("repo_url"):
        repo_url = github["repo_url"]
        stars = format_number(github.get("stars"))
        forks = format_number(github.get("forks"))
        github_str = f"⭐[{stars}]({repo_url}) 🔀[{forks}]({repo_url})"

    citation_str = "—"
    if semantic.get("citation_count") is not None:
        citations = format_number(semantic.get("citation_count"))
        influential = semantic.get("influential_citation_count")

        if semantic.get("paper_id"):
            s2_url = f"https://www.semanticscholar.org/paper/{semantic['paper_id']}"
            if influential and influential > 0:
                citation_str = f"[{citations}]({s2_url}) (📈{influential})"
            else:
                citation_str = f"[{citations}]({s2_url})"
        else:
            citation_str = citations

    twitter_str = "—"
    tweet_url = twitter.get("tweet_url")
    if tweet_url and (twitter.get("likes") or twitter.get("retweets") or twitter.get("views")):
        parts = []
        if twitter.get("likes"):
            parts.append(f"❤️[{format_number(twitter['likes'])}]({tweet_url})")
        if twitter.get("retweets"):
            parts.append(f"🔁[{format_number(twitter['retweets'])}]({tweet_url})")
        if twitter.get("views"):
            parts.append(f"👁️[{format_number(twitter['views'])}]({tweet_url})")

        twitter_str = "<br>".join(parts) if parts else "—"

    date = format_date(arxiv.get("published_date", ""))
    authors_short = arxiv["authors"][0].split()[-1] + " et al." if arxiv["authors"] else "—"

    arxiv_link = f"[{arxiv_id}]({arxiv['arxiv_url']})"

    open_issues = github.get("open_issues", "—")

    latest_changes = f"[{date}]({paper_md})"

    return f"| [{title}]({paper_md}) | {arxiv_link} | {date} | {authors_short} | {github_str} | {citation_str} | {open_issues} | {latest_changes} | {twitter_str} |"


DOMAIN_INFO = {
    "data_collection": {
        "title": "Data Collection & Datasets",
        "link": "domains/data_collection.md"
    },
    "vla": {
        "title": "Vision-Language-Action Models",
        "link": "domains/vla.md"
    },
    "manipulation": {
        "title": "Robot Manipulation",
        "link": "domains/manipulation.md"
    }
}


def generate_domain_section(papers, domain_name):
    domain_papers = [p for p in papers if domain_name in p.get("domains", [])]

    if not domain_papers:
        return ""

    domain_info = DOMAIN_INFO.get(domain_name, {"title": domain_name.replace('_', ' ').title(), "link": None})

    if domain_info.get("link"):
        section = f"### [{domain_info['title']}]({domain_info['link']})\n\n"
    else:
        section = f"### {domain_info['title']}\n\n"

    section += "| Paper | PDF | Date | Authors | GitHub | Citations | Issues | Changes | Twitter |\n"
    section += "|-------|-----|------|---------|--------|-----------|--------|---------|----------|\n"

    for paper in domain_papers:
        section += generate_paper_row(paper) + "\n"

    section += "\n"
    return section


def generate_readme(papers_file: Path, output_file: Path):
    with open(papers_file, 'r') as f:
        papers = json.load(f)

    total_papers = len(papers)
    total_stars = sum(p["github"].get("stars", 0) or 0 for p in papers)
    total_citations = sum(p["semantic_scholar"].get("citation_count", 0) or 0 for p in papers)

    all_domains = set()
    for paper in papers:
        all_domains.update(paper.get("domains", []))

    readme = f"""# 🤖 Robotics Intelligence Hub

> A curated collection of cutting-edge robotics research papers with real-world engagement metrics

[![Papers](https://img.shields.io/badge/Papers-{total_papers}-blue)](.)
[![Stars](https://img.shields.io/badge/GitHub%20Stars-{format_number(total_stars)}-yellow)](.)
[![Citations](https://img.shields.io/badge/Citations-{format_number(total_citations)}-green)](.)
[![Last Updated](https://img.shields.io/badge/Updated-{datetime.now().strftime('%Y--%m--%d')}-lightgrey)](.)

## 📊 Overview

This repository serves two purposes:

1. **Track the latest robotics research** across key domains, enriched with real-world engagement metrics from multiple sources
2. **Help newcomers learn** about different current domains in robotics research to give them a strong foundation

**Data Sources:**
- 📄 **arXiv**: Paper metadata, authors, abstracts
- ⭐ **GitHub**: Stars, forks, PRs, issues, activity
- 🐦 **Twitter**: Social engagement (likes, retweets, replies)
- 📚 **Semantic Scholar**: Citation counts, influential citations

---

## 📑 Papers by Domain

"""

    domains = ["data_collection", "vla", "simulation", "diffusion", "manipulation", "locomotion"]

    for domain in domains:
        section = generate_domain_section(papers, domain)
        if section:
            readme += section

    readme += """---

## 🔧 How It Works

This repository automatically tracks robotics papers through:

1. **Manual Curation**: High-quality seed papers from key domains
2. **API Integration**: Automated metrics collection from:
   - arXiv API (paper metadata)
   - GitHub REST API (repository metrics)
   - Twitter API v2 (social engagement)
   - Semantic Scholar API (citation data)
3. **Daily Updates**: Metrics refreshed automatically

## 📊 Metrics Legend

- ⭐ GitHub Stars
- 🔀 Forks
- 📈 Influential Citations (highly impactful citations)
- ❤️ Tweet Likes
- 🔁 Retweets

## 📝 License

Data aggregated from public sources. Please cite original papers when using this information.

---

## 📖 Citation

If you find this repository useful, please consider citing:

```bibtex
@misc{dongo2025airrepo,
    title = {AIR Intelligence Hub},
    author = {Gyalpo Dongo},
    journal = {GitHub repository},
    url = {https://github.com/gyalpo-dongo/air_repo},
    year = {2025},
}
```

---

**Last Updated:** """ + datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC") + """

**Maintained by:** Gyalpo Dongo
"""

    with open(output_file, 'w') as f:
        f.write(readme)


if __name__ == "__main__":
    papers_file = Path(__file__).parent.parent / "data" / "papers.json"
    output_file = Path(__file__).parent.parent / "README.md"

    print("Generating README.md...")
    generate_readme(papers_file, output_file)
    print(f"✓ README.md generated at {output_file}")
