import json

class MCPRouter:

    def __init__(self, registry_path="registry.json"):
        with open(registry_path) as f:
            self.registry = json.load(f)

    def route(self, query: str):
        query = query.lower()

        if "codigo" in query or "repo" in query:
            return self.registry["categories"]["programming"]

        if "web" in query or "buscar" in query:
            return self.registry["categories"]["token_optimization"]

        if "memoria" in query or "rag" in query:
            return self.registry["categories"]["rag_memory"]

        return self.registry["categories"]["reasoning_agents"]
