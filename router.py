import json
import os

class MCPRouter:

    def __init__(self, registry_path: str = None):
        if registry_path is None:
            # Resolve o caminho relativo ao modulo, nao ao diretorio de execucao
            registry_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "registry.json")
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
