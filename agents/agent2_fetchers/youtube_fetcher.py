import requests
from google import genai

class YouTubeFetcher:
    def __init__(self, client, api_key):
        self.client = client
        self.api_key = api_key

    def fetch(self, query):
        url = (
            "https://www.googleapis.com/youtube/v3/search?"
            f"part=snippet&q={query}&maxResults=5&type=video&key={self.api_key}"
        )
        data = requests.get(url).json()

        response = self.client.models.generate_content(
            model="gemini-1.5-flash",
            contents=f"Extract top 5 thumbnails and titles:\n{data}"
        )

        return response.text
