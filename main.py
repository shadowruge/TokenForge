import os

import requests

from cache import AutoCache
from router import MCPRouter
from semantic_cache import SemanticCache
from token_optimizer import TokenOptimizer

cache = AutoCache()
semantic = SemanticCache()
optimizer = TokenOptimizer()
router = MCPRouter()

OLLAMA_TIMEOUT_SECONDS = 60


def call_llm(prompt):
    ollama_host = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
    r = requests.post(
        f"{ollama_host}/api/generate",
        json={"model": "qwen2.5:1.5b", "prompt": prompt, "stream": False},
        timeout=OLLAMA_TIMEOUT_SECONDS,
    )
    data = r.json()
    if r.status_code != 200 or "response" not in data:
        raise RuntimeError(f"Erro na resposta do Ollama: {data}")
    return data["response"]


def process(query):

    print("\n[1] INPUT:", query)

    # 🔥 CACHE EXATO
    cached = cache.get(query)
    if cached:
        print("[CACHE HIT - EXACT]")
        return cached["response"]

    # 🔥 CACHE SEMÂNTICO
    sem = semantic.get(query)
    if sem:
        print("[CACHE HIT - SEMANTIC]")
        return sem

    # 🔥 ROTEAMENTO DE CATEGORIA
    category = router.route(query)
    print("[ROTEADO]:", category.get("description", category))

    # 🔥 OTIMIZA TOKEN
    optimized = optimizer.optimize(query)

    print("[OTIMIZADO]:", optimized)

    # 🔥 CHAMA LLM
    response = call_llm(optimized)

    # 🔥 SALVA CACHE
    cache.set(query, response)
    semantic.set(query, response)

    return response


if __name__ == "__main__":
    print("TokenForge iniciado. Digite sua pergunta (Ctrl+C para sair).")
    try:
        while True:
            try:
                q = input("\nPergunta: ")
            except EOFError:
                print("\nEntrada encerrada.")
                break

            if not q.strip():
                continue

            try:
                print("\nResposta:", process(q))
            except Exception as e:
                print(f"\n[ERRO] Falha ao processar a pergunta: {e}")
                continue
    except KeyboardInterrupt:
        print("\n\nEncerrando TokenForge. Até logo!")
