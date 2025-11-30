import requests
from google import genai

class NewsAPIFetcher:
    def __init__(self, client, api_key):
        self.client = client
        self.api_key = api_key

    def fetch(self, query):
        url = f"https://newsapi.org/v2/everything?q={query}&pageSize=5&apiKey={self.api_key}"
        data = requests.get(url).json()

        response = self.client.models.generate_content(
            model="gemini-1.5-flash",
            contents=f"Clean and summarize these newsapi results:\n{data}"
        )

        return response.text
