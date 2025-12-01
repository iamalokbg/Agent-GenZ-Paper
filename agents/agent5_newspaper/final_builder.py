class FinalNewspaperBuilder:
    def __init__(self, client, style="normal"):
        """
        style = "normal" → use real images
        style = "manga"  → use manga/anime images if available
        """
        self.client = client
        self.style = style

    def build(self, rewritten_news, images):
        """
        rewritten_news → list/dict of rewritten articles from Agent 4
        images → dict of:
            {
                article_id: {
                    "original_image": url,
                    "manga_image": url or None
                }
            }
        """

        # Convert images to a readable text table for the LLM
        image_descriptions = []
        for key, media in images.items():
            chosen = (
                media.get("manga_image")
                if (self.style == "manga" and media.get("manga_image"))
                else media.get("original_image")
            )
            image_descriptions.append(
                f"- {key}: {chosen if chosen else 'No image available'}"
            )

        images_text = "\n".join(image_descriptions)

        prompt = f"""
You are Agent 5 — Newspaper Builder.
Your job: Merge all rewritten news content + selected images into a final modern Gen-Z newspaper layout.

STYLE MODE: {self.style.upper()}
- "NORMAL"  → Use realistic images.
- "MANGA"   → Use anime/manga-style images.
Choose the appropriate image for each section.

---

### NEWS CONTENT (Rewritten Articles)
{rewritten_news}

---

### SELECTED IMAGES (Already Chosen)
{images_text}

---

### OUTPUT FORMAT (STRICT GUIDELINES)

Create a final newspaper with these sections:

🟥 **1. FRONT PAGE**
- Top Story (big title, short hype intro, one image)
- 3 Key Highlights (bullet points)

🟧 **2. TRENDING NOW**
- 4–6 short trending summaries
- Emoji-friendly
- Each with one image or thumbnail

🟩 **3. QUICK BITES (30-Second Reads)**
- Ultra-short stories
- Up to 2 lines each

🟦 **4. VIDEO ZONE (If YouTube stories exist)**
- List videos + thumbnails
- Very short description

🟪 **5. MANGA MODE SPECIAL** (only if style=manga)
- Caption: “Illustrated in Anime/Manga Style by Gemini Nano 🍌”
- Use manga images only

---

### RULES
- Keep formatting tight and readable.
- Use spacing and section dividers.
- Keep consistent Gen-Z tone.
- Never hallucinate news — use only provided content.
- If any section has no items, omit it cleanly.
- Return ONLY the formatted newspaper. No explanation.

Now generate the final newspaper.
"""

        response = self.client.models.generate_content(
            model="gemini-1.5-pro",
            contents=prompt
        )

        return response.text
