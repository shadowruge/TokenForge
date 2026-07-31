class AutoCache:
    """Cache de correspondência exata (chave = string da query)."""

    def __init__(self):
        self.db = {}

    def get(self, query: str):
        return self.db.get(query)

    def set(self, query: str, response: str):
        self.db[query] = {"response": response}