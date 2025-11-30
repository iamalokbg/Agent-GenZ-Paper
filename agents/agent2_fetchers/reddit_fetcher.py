import praw
from google import genai
from core.config import Config

class RedditFetcher:
    def __init__(self, client):
        self.client = client
        self.reddit = praw.Reddit(
            client_id=Config.REDDIT_CLIENT_ID,
            client_secret=Config.REDDIT_SECRET,
            user_agent="genz-news-agent"
        )

    def fetch(self, query):
        posts = self.reddit.subreddit("all").search(query, limit=5)

        raw = [{"title": p.title, "score": p.score, "text": p.selftext} for p in posts]

        response = self.client.models.generate_content(
            model="gemini-1.5-flash",
            contents=f"Clean and summarize these reddit posts:\n{raw}"
        )

        return response.text
