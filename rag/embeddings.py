class CustomEmbeddings:
    def __init__(self):
        # Lazy import to keep module import fast (torch can be slow to import).
        from sentence_transformers import SentenceTransformer

        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def embed_documents(self, texts):
        return self.model.encode(texts).tolist()

    def embed_query(self, text):
        return self.model.encode([text])[0].tolist()

    # 🔥 ADD THIS (important)
    def __call__(self, text):
        return self.embed_query(text)


def get_embeddings():
    return CustomEmbeddings()