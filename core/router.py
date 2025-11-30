class Router:
    def __init__(self):
        pass

    def route_news_to_rewriter(self, cleaned_batches):
        merged = "\n\n".join(cleaned_batches)
        return merged

    def route_media_to_builder(self, images):
        return images

    def combine_for_agent5(self, rewritten, images):
        return {
            "stories": rewritten,
            "images": images
        }
