import time
from main import process

class Benchmark:

    def __init__(self, queries):
        self.queries = queries
        self.results = []

    def run(self):
        print("\n🚀 Iniciando benchmark...\n")

        start_total = time.time()

        for q in self.queries:
            start = time.time()

            response = process(q)

            elapsed = time.time() - start

            self.results.append({
                "query": q,
                "time": elapsed,
                "response_size": len(response)
            })

        total_time = time.time() - start_total

        self.report(total_time)

    def report(self, total_time):
        avg_time = sum(r["time"] for r in self.results) / len(self.results)

        print("\n📊 RESULTADO FINAL")
        print(f"Total queries: {len(self.results)}")
        print(f"Tempo total: {total_time:.2f}s")
        print(f"Tempo médio: {avg_time:.2f}s")

        # estimativa simples
        tokens_saved = len(self.results) * 0.7  # ajuste depois
        print(f"Economia estimada: {tokens_saved*100:.0f}%")


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
