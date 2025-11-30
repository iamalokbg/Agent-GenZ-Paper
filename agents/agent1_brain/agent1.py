from google import genai

class Agent1Brain:
    def __init__(self, client):
        self.client = client

    def analyze_user(self, user_topics):
        prompt = f"""
You are Agent 1 (Brain).
User Interests: {user_topics}

Define:
1. Priority order for news
2. Instructions for Agent2 fetchers
3. Instructions for Agent3 media
4. Tone/style hints for Agent4
5. Layout rules for Agent5
"""
        response = self.client.models.generate_content(
            model="gemini-1.5-pro",
            contents=prompt
        )
        return response.text
