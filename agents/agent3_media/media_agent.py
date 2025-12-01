class MediaAgent:
    def __init__(self, client, manga_mode=False):
        self.client = client
        self.manga_mode = manga_mode

    def select_best_images(self, news_items):
        """
        Step 1 → Use Flash to pick the best real images (your original method)
        """
        prompt = f"Pick best images for each story and return URLs only.\n{news_items}"
        response = self.client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        ).text

        real_images = response  # keep original behavior

        # If manga mode OFF → return as-is
        if not self.manga_mode:
            return {"mode": "real", "images": real_images}

        """
        Step 2 → Generate manga/anime images using Nano Banana
        (Simple + non-breaking addition)
        """
        try:
            banana_model = self.client.models.get("gemini-nano-image-banana")

            manga_results = []
            for item in news_items:
                title = item.get("title", "news image")
                manga_prompt = f"Manga style illustration: {title}"

                img = banana_model.generate_image(
                    prompt=manga_prompt,
                    size="512x512"
                )
                manga_results.append(img.image_url)

            return {
                "mode": "manga",
                "images": manga_results,
                "fallback": real_images
            }

        except Exception as e:
            # If anything fails → use real images
            return {
                "mode": "real-fallback",
                "images": real_images,
                "error": str(e)
            }
