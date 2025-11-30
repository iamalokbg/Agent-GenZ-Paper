import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")
    REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
    REDDIT_SECRET = os.getenv("REDDIT_SECRET")
    YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

    MODEL_BRAIN = "gemini-1.5-pro"
    MODEL_REWRITE = "gemini-2.0-flash"
    MODEL_FLASH = "gemini-1.5-flash"