import feedparser
from google import genai

class RSSFetcher:
    def __init__(self, client):
        self.client = client

    def fetch(self, feed_url="https://news.google.com/rss"):
        raw = feedparser.parse(feed_url)

        items = [{"title": e.title, "summary": e.summary} for e in raw.entries[:5]]

        response = self.client.models.generate_content(
            model="gemini-1.5-flash",
            contents=f"Clean RSS items and return summaries:\n{items}"
        )

        return response.text
