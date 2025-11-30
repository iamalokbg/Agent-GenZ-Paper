import requests
from google import genai

class GoogleNewsFetcher:
    def __init__(self, client, api_key):
        self.client = client
        self.api_key = api_key

    def fetch(self, query):
        url = f"https://newsapi.org/v2/everything?q={query}&apiKey={self.api_key}"
        raw = requests.get(url).json()

        # Clean using Gemini Flash
        response = self.client.models.generate_content(
            model="gemini-1.5-flash",
            contents=f"Clean this news data and return top 5:\n{raw}"
        )
        return response.text
