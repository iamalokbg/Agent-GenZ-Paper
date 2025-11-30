class FinalNewspaperBuilder:
    def __init__(self, client):
        self.client = client

    def build(self, rewritten_news, images):
        prompt = f"""
You are Agent 5 — Newspaper Builder.
Merge all content into final formatted Gen-Z newspaper layout.

News:
{rewritten_news}

Images:
{images}

Output:
- Section-wise layout
- Top Story
- Trending section
- Short bites
- Videos if any
"""
        return self.client.models.generate_content(
            model="gemini-1.5-pro",
            contents=prompt
        ).text
