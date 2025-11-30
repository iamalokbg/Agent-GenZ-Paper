from google import genai
from agents.agent1_brain.agent1 import Agent1Brain
from agents.agent2_fetchers.google_news_fetcher import GoogleNewsFetcher
from agents.agent2_fetchers.reddit_fetcher import RedditFetcher
from agents.agent2_fetchers.newsapi_fetcher import NewsAPIFetcher
from agents.agent2_fetchers.youtube_fetcher import YouTubeFetcher
from agents.agent2_fetchers.rss_fetcher import RSSFetcher
from agents.agent3_media.media_agent import MediaAgent
from agents.agent4_rewriter.rewrite_agent import RewriteAgent
from agents.agent5_newspaper.final_builder import FinalNewspaperBuilder

from core.config import Config
from core.router import Router


class Orchestrator:
    def __init__(self):
        # Initialize Gemini client
        self.client = genai.Client(api_key=Config.GOOGLE_API_KEY)

        # Agents
        self.agent1 = Agent1Brain(self.client)
        self.agent2_google = GoogleNewsFetcher(self.client, Config.NEWSAPI_KEY)
        self.agent2_reddit = RedditFetcher(self.client)
        self.agent2_newsapi = NewsAPIFetcher(self.client, Config.NEWSAPI_KEY)
        self.agent2_youtube = YouTubeFetcher(self.client, Config.YOUTUBE_API_KEY)
        self.agent2_rss = RSSFetcher(self.client)

        self.agent3 = MediaAgent(self.client)
        self.agent4 = RewriteAgent(self.client)
        self.agent5 = FinalNewspaperBuilder(self.client)

        self.router = Router()


    def run(self, user_interests):
        print("🔵 Agent1: Understanding user...")
        instructions = self.agent1.analyze_user(user_interests)

        print("🟡 Agent2: Fetching news...")
        news_batches = []
        news_batches.append(self.agent2_google.fetch(user_interests))
        news_batches.append(self.agent2_reddit.fetch(user_interests))
        news_batches.append(self.agent2_newsapi.fetch(user_interests))
        news_batches.append(self.agent2_youtube.fetch(user_interests))
        news_batches.append(self.agent2_rss.fetch(user_interests))

        print("🟠 Agent3: Selecting media...")
        media = self.agent3.select_best_images(news_batches)

        print("🟣 Agent4: Rewriting news...")
        merged_news = self.router.route_news_to_rewriter(news_batches)
        rewritten = self.agent4.rewrite(merged_news)

        print("🔴 Agent5: Building final newspaper...")
        final_package = self.router.combine_for_agent5(rewritten, media)
        final_output = self.agent5.build(final_package["stories"], final_package["images"])

        return final_output
