import time
from main import process, cache

class Benchmark:

    def __init__(self, query_list):
        self.queries = query_list
        self.results = []

    def run(self):
        print("\n🚀 Iniciando benchmark...\n")

        if not self.queries:
            print("Nenhuma query fornecida.")
            return

        start_total = time.time()

        for q in self.queries:
            start = time.time()

            try:
                response = process(q)
            except (ValueError, RuntimeError, TypeError, KeyError, AttributeError) as e:
                print(f"[ERRO] Falha ao processar '{q}': {e}")
                continue

            elapsed = time.time() - start

            self.results.append({
                "query": q,
                "time": elapsed,
                "response_size": len(response)
            })

        total_time = time.time() - start_total

        self.report(total_time)

    def report(self, total_time):
        if not self.results:
            print("\nNenhum resultado para reportar (todas as queries falharam).")
            return

        avg_time = sum(r["time"] for r in self.results) / len(self.results)
        total_chars = sum(r["response_size"] for r in self.results)
        cache_entries = len(cache.db) if hasattr(cache, "db") else 0

        print("\n📊 RESULTADO FINAL")
        print(f"Total queries: {len(self.results)}")
        print(f"Tempo total: {total_time:.2f}s")
        print(f"Tempo médio: {avg_time:.2f}s")
        print(f"Total de caracteres nas respostas: {total_chars}")
        print(f"Entradas no cache exato ao final: {cache_entries}")


if __name__ == "__main__":
    queries = [
        "como usar mcp com python",
        "como usar mcp com python",  # repetido (cache)
        "explique rag simples",
        "explique rag simples",      # repetido
        "buscar codigo git mcp"
    ]

    bench = Benchmark(queries)
    bench.run()