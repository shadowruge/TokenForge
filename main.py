from cache import AutoCache
from semantic_cache import SemanticCache
from token_optimizer import TokenOptimizer

cache = AutoCache()
semantic = SemanticCache()
optimizer = TokenOptimizer()

def call_llm(prompt):
    import os
    import requests
    ollama_host = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
    r = requests.post(
        f"{ollama_host}/api/generate",
        json={"model": "qwen2.5:1.5b", "prompt": prompt, "stream": False}
    )
    return r.json()["response"]

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
    while True:
        q = input("\nPergunta: ")
        print("\nResposta:", process(q))