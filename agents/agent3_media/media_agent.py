class MediaAgent:
    def __init__(self, client):
        self.client = client

    def select_best_images(self, news_items):
        prompt = f"Pick best images for each story and return URLs only.\n{news_items}"
        return self.client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        ).text
