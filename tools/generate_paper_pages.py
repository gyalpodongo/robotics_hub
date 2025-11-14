import json
from pathlib import Path
from datetime import datetime
from github import get_github_issues, get_recent_prs, get_recent_commits


def format_number(num):
    if num is None:
        return "—"
    if num >= 1000:
        return f"{num/1000:.1f}k"
    return str(num)


def format_date(date_str):
    if not date_str:
        return "—"
    try:
        date_obj = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
        return date_obj.strftime("%b %d, %Y")
    except:
        return date_str


def extract_repo_info(github_url):
    if not github_url:
        return None, None
    parts = github_url.rstrip("/").split("github.com/")[-1].split("/")
    return parts[0], parts[1]


def generate_paper_page(paper: dict, output_dir: Path):
    arxiv = paper["arxiv"]
    github = paper["github"]
    twitter = paper["twitter"]
    semantic = paper["semantic_scholar"]

    arxiv_id = arxiv["arxiv_id"].split("v")[0]
    paper_file = output_dir / f"{arxiv_id}.md"

    owner, repo = extract_repo_info(github.get("repo_url"))

    issues = []
    prs = []
    commits = []
    if owner and repo:
        issues = get_github_issues(owner, repo, limit=3)
        prs = get_recent_prs(owner, repo, limit=5)
        commits = get_recent_commits(owner, repo, limit=10)

    content = f"""# {arxiv['title']}

arXiv: [{arxiv_id}]({arxiv['arxiv_url']}) | Published: {format_date(arxiv['published_date'])}

**Authors**: {', '.join(arxiv['authors'])}

---

## 📊 Metrics Summary

| 📄 PDF | ⭐ Stars | 🔀 Forks | 📚 Citations | 📈 Influential | ❤️ Likes | 🔁 Retweets | 👁️ Views | 🔧 Issues | 📝 PRs |
|---------|---------|---------|-------------|---------------|----------|------------|----------|----------|---------|
| [{arxiv_id}]({arxiv['arxiv_url']}) | {format_number(github.get('stars'))} | {format_number(github.get('forks'))} | {format_number(semantic.get('citation_count'))} | {semantic.get('influential_citation_count') or '—'} | {format_number(twitter.get('likes'))} | {format_number(twitter.get('retweets'))} | {format_number(twitter.get('views'))} | {github.get('open_issues') or '—'} | {github.get('open_prs') or '—'} |

**Links**: [GitHub]({github.get('repo_url')}) • [Twitter]({twitter.get('tweet_url')}) • [Semantic Scholar]({f"https://www.semanticscholar.org/paper/{semantic.get('paper_id')}" if semantic.get('paper_id') else '#'})

---

## 📝 Abstract

{arxiv.get('summary', 'No summary available.')}

---

## 🐛 Latest Issues

"""

    if issues:
        content += "| # | Issue | Created |\n"
        content += "|---|-------|----------|\n"
        for issue in issues:
            content += f"| [#{issue['number']}]({issue['url']}) | {issue['title']} | {format_date(issue['created_at'])} |\n"
        content += f"\n[View all issues →]({github.get('repo_url')}/issues)\n\n"
    else:
        content += "No recent issues found.\n\n"

    content += "---\n\n## 🔄 Recent Activity\n\n"

    activity_items = []

    for pr in prs:
        activity_items.append({
            'type': 'PR',
            'date': pr['merged_at'],
            'title': pr['title'],
            'number': pr['number'],
            'url': pr['url'],
            'author': None
        })

    for commit in commits:
        activity_items.append({
            'type': 'Commit',
            'date': commit['date'],
            'title': commit['message'],
            'sha': commit['sha'],
            'url': commit['url'],
            'author': commit['author']
        })

    activity_items.sort(key=lambda x: x['date'], reverse=True)
    activity_items = activity_items[:5]

    if activity_items:
        content += "| Type | Activity | Author | Date |\n"
        content += "|------|----------|--------|------|\n"
        for item in activity_items:
            activity_date = format_date(item['date'])
            if item['type'] == 'PR':
                title = item['title'][:50] + "..." if len(item['title']) > 50 else item['title']
                content += f"| 🔀 PR | [#{item['number']}]({item['url']}) {title} | — | {activity_date} |\n"
            else:
                message = item['title'][:50] + "..." if len(item['title']) > 50 else item['title']
                content += f"| 📝 Commit | [`{item['sha']}`]({item['url']}) {message} | {item['author']} | {activity_date} |\n"
        content += f"\n[View all activity →]({github.get('repo_url')}/commits)\n\n"
    else:
        content += "No recent activity found.\n\n"

    content += f"""---

**Last Updated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}
"""

    with open(paper_file, 'w') as f:
        f.write(content)

    return paper_file


def generate_all_paper_pages(papers_file: Path, output_dir: Path):
    output_dir.mkdir(exist_ok=True)

    with open(papers_file, 'r') as f:
        papers = json.load(f)

    generated_files = []
    for paper in papers:
        paper_file = generate_paper_page(paper, output_dir)
        arxiv_id = paper["arxiv"]["arxiv_id"].split("v")[0]
        print(f"✓ Generated {arxiv_id}.md")
        generated_files.append(paper_file)

    return generated_files


if __name__ == "__main__":
    papers_file = Path(__file__).parent.parent / "data" / "papers.json"
    output_dir = Path(__file__).parent.parent / "papers"

    print("Generating paper pages...\n")
    generated_files = generate_all_paper_pages(papers_file, output_dir)
    print(f"\n✓ Generated {len(generated_files)} paper pages in {output_dir}")
