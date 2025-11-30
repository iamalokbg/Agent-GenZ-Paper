"""
Agent 2 — Multi-Source Fetchers (Parallel Workers)
Each agent uses Gemini Flash to clean + validate raw data.
"""

from .google_news import Agent2Google
from .reddit_fetcher import Agent2Reddit
from .newsapi_fetcher import Agent2NewsAPI
from .youtube_fetcher import Agent2YouTube
from .rss_fetcher import Agent2RSS

__all__ = [
    "Agent2Google",
    "Agent2Reddit",
    "Agent2NewsAPI",
    "Agent2YouTube",
    "Agent2RSS"
]