import pytest
from unittest.mock import patch
from agents.fetchers.google_news import GoogleNewsFetcher
from agents.fetchers.reddit import RedditFetcher
from agents.fetchers.rss import RSSFetcher
from agents.fetchers.newsapi import NewsAPIFetcher

# -----------------------------
# GOOGLE NEWS
# -----------------------------
@patch("agents.fetchers.google_news.requests.get")
def test_google_news_fetch(mock_get):
    mock_get.return_value.json.return_value = {"articles": [{"title": "Sample"}]}
    fetcher = GoogleNewsFetcher()
    result = fetcher.fetch("ai")
    assert "articles" in result
    assert result["articles"][0]["title"] == "Sample"

# -----------------------------
# REDDIT
# -----------------------------
@patch("agents.fetchers.reddit.requests.get")
def test_reddit_fetch(mock_get):
    mock_get.return_value.json.return_value = {"data": {"children": [{"data": {"title": "Reddit Post"}}]}}
    fetcher = RedditFetcher()
    result = fetcher.fetch("technology")
    assert len(result) == 1
    assert result[0]["title"] == "Reddit Post"

# -----------------------------
# RSS
# -----------------------------
@patch("agents.fetchers.rss.feedparser.parse")
def test_rss_fetch(mock_parse):
    mock_parse.return_value.entries = [{"title": "RSS News"}]
    fetcher = RSSFetcher("https://example.com/rss")
    result = fetcher.fetch()
    assert result[0]["title"] == "RSS News"

# -----------------------------
# NEWSAPI
# -----------------------------
@patch("agents.fetchers.newsapi.requests.get")
def test_newsapi_fetch(mock_get):
    mock_get.return_value.json.return_value = {"articles": [{"title": "API News"}]}
    fetcher = NewsAPIFetcher("FAKE_KEY")
    result = fetcher.fetch("sports")
    assert result["articles"][0]["title"] == "API News"
