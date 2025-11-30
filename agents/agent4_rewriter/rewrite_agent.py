class RewriteAgent:
    def __init__(self, client):
        self.client = client

    def rewrite(self, cleaned_news):
        return self.client.models.generate_content(
            model="gemini-2.0-flash",
            contents=f"Rewrite this in Gen-Z tone, simple English:\n{cleaned_news}"
        ).text
