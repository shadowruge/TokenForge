from sentence_transformers import SentenceTransformer
import numpy as np

class SemanticCache:

    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.db = []

    def similarity(self, v1, v2):
        return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

    def get(self, query, threshold=0.85):
        q_vec = self.model.encode(query)

        for item in self.db:
            sim = self.similarity(q_vec, item["vector"])
            if sim > threshold:
                return item["response"]

        return None

    def set(self, query, response):
        vec = self.model.encode(query)
        self.db.append({
            "query": query,
            "response": response,
            "vector": vec
        })
