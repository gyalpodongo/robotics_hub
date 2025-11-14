import os
import requests
from dotenv import load_dotenv
from schemas import GitHubMetrics

load_dotenv()


def extract_repo_info_from_url(github_url: str) -> tuple[str, str]:
    parts = github_url.rstrip("/").split("github.com/")[-1].split("/")
    owner = parts[0]
    repo = parts[1]
    return owner, repo


def get_github_headers() -> dict:
    token = os.getenv("GITHUB_PAT")
    return {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json"
    }


def fetch_github_metrics(github_url: str) -> GitHubMetrics:
    if not github_url:
        return GitHubMetrics()

    owner, repo = extract_repo_info_from_url(github_url)

    headers = get_github_headers()

    repo_response = requests.get(
        f"https://api.github.com/repos/{owner}/{repo}",
        headers=headers
    )

    if repo_response.status_code != 200:
        return GitHubMetrics(repo_url=github_url)

    repo_data = repo_response.json()

    pulls_response = requests.get(
        f"https://api.github.com/repos/{owner}/{repo}/pulls?state=open",
        headers=headers
    )
    open_prs = len(pulls_response.json()) if pulls_response.status_code == 200 else None

    return GitHubMetrics(
        repo_url=github_url,
        stars=repo_data.get("stargazers_count"),
        forks=repo_data.get("forks_count"),
        last_commit=repo_data.get("pushed_at"),
        open_prs=open_prs,
        open_issues=repo_data.get("open_issues_count"),
        watchers=repo_data.get("watchers_count")
    )


def get_github_issues(owner: str, repo: str, state: str = "open", limit: int = 3) -> list[dict]:
    headers = get_github_headers()

    response = requests.get(
        f"https://api.github.com/repos/{owner}/{repo}/issues",
        headers=headers,
        params={"state": state, "per_page": limit, "sort": "created", "direction": "desc"}
    )

    if response.status_code != 200:
        return []

    issues = []
    for issue in response.json():
        if "pull_request" not in issue:
            issues.append({
                "number": issue["number"],
                "title": issue["title"],
                "url": issue["html_url"],
                "created_at": issue["created_at"],
                "state": issue["state"]
            })

    return issues[:limit]


def get_recent_prs(owner: str, repo: str, limit: int = 5) -> list[dict]:
    headers = get_github_headers()

    response = requests.get(
        f"https://api.github.com/repos/{owner}/{repo}/pulls",
        headers=headers,
        params={"state": "closed", "per_page": limit, "sort": "updated", "direction": "desc"}
    )

    if response.status_code != 200:
        return []

    prs = []
    for pr in response.json():
        if pr.get("merged_at"):
            prs.append({
                "number": pr["number"],
                "title": pr["title"],
                "url": pr["html_url"],
                "merged_at": pr["merged_at"],
                "body": pr.get("body", "")[:200]
            })

    return prs[:limit]


def get_latest_commit_date(owner: str, repo: str) -> str:
    headers = get_github_headers()

    response = requests.get(
        f"https://api.github.com/repos/{owner}/{repo}/commits",
        headers=headers,
        params={"per_page": 1}
    )

    if response.status_code != 200:
        return None

    commits = response.json()
    if commits:
        return commits[0]["commit"]["committer"]["date"]

    return None


def get_recent_commits(owner: str, repo: str, limit: int = 10) -> list[dict]:
    headers = get_github_headers()

    response = requests.get(
        f"https://api.github.com/repos/{owner}/{repo}/commits",
        headers=headers,
        params={"per_page": limit, "sha": "main"}
    )

    if response.status_code != 200:
        response = requests.get(
            f"https://api.github.com/repos/{owner}/{repo}/commits",
            headers=headers,
            params={"per_page": limit, "sha": "master"}
        )

    if response.status_code != 200:
        return []

    commits = []
    for commit in response.json():
        commits.append({
            "sha": commit["sha"][:7],
            "message": commit["commit"]["message"].split("\n")[0],
            "author": commit["commit"]["author"]["name"],
            "date": commit["commit"]["author"]["date"],
            "url": commit["html_url"]
        })

    return commits


if __name__ == "__main__":
    test_repos = [
        "https://github.com/real-stanford/universal_manipulation_interface",
        "https://github.com/openvla/openvla",
        "https://github.com/ruka-hand/RUKA"
    ]

    print("Testing GitHub API tracker...\n")
    for repo_url in test_repos:
        print(f"Fetching: {repo_url}")
        metrics = fetch_github_metrics(repo_url)
        print(f"  Stars: {metrics.stars}")
        print(f"  Forks: {metrics.forks}")
        print(f"  Open PRs: {metrics.open_prs}")
        print(f"  Open Issues: {metrics.open_issues}")
        print(f"  Last Commit: {metrics.last_commit}")

        owner, repo = extract_repo_info_from_url(repo_url)

        print(f"\n  Recent Issues:")
        issues = get_github_issues(owner, repo, limit=2)
        for issue in issues:
            print(f"    #{issue['number']}: {issue['title']}")

        print(f"\n  Recent PRs:")
        prs = get_recent_prs(owner, repo, limit=2)
        for pr in prs:
            print(f"    #{pr['number']}: {pr['title']}")

        print("\n" + "="*50 + "\n")
