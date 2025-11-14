from pydantic import BaseModel, Field
from datetime import datetime


class ArxivPaper(BaseModel):
    arxiv_id: str
    title: str
    authors: list[str]
    summary: str
    published_date: str
    pdf_url: str | None = None
    arxiv_url: str
    categories: list[str]


class GitHubMetrics(BaseModel):
    repo_url: str | None = None
    stars: int | None = None
    forks: int | None = None
    last_commit: str | None = None
    open_prs: int | None = None
    open_issues: int | None = None
    watchers: int | None = None
    latest_pr_date: str | None = None


class TwitterMetrics(BaseModel):
    tweet_url: str | None = None
    tweet_id: str | None = None
    likes: int | None = None
    retweets: int | None = None
    replies: int | None = None
    quotes: int | None = None
    views: int | None = None


class SemanticScholarMetrics(BaseModel):
    paper_id: str | None = None
    citation_count: int | None = None
    influential_citation_count: int | None = None


class Paper(BaseModel):
    arxiv: ArxivPaper
    github: GitHubMetrics
    twitter: TwitterMetrics
    semantic_scholar: SemanticScholarMetrics
    domains: list[str]
    tags: list[str] = Field(default_factory=list)
    added_date: str = Field(default_factory=lambda: datetime.now().isoformat())
    relevance_score: float = 0.0
    gemini_analysis: str | None = None
    future_directions: list[str] = Field(default_factory=list)
