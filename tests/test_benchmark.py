from unittest.mock import patch


def test_run_with_empty_queries_does_not_crash(benchmark_module, capsys):
    bench = benchmark_module.Benchmark([])
    bench.run()
    assert bench.results == []
    out = capsys.readouterr().out
    assert "Nenhuma query fornecida" in out


def test_run_processes_each_query(benchmark_module):
    with patch.object(benchmark_module, "process", return_value="resposta") as mock_process:
        bench = benchmark_module.Benchmark(["pergunta 1", "pergunta 2"])
        bench.run()

    assert mock_process.call_count == 2
    assert len(bench.results) == 2
    assert all(r["response_size"] == len("resposta") for r in bench.results)


def test_run_continues_after_a_query_fails(benchmark_module, capsys):
    def side_effect(query):
        if query == "pergunta com erro":
            raise ConnectionError("ollama indisponivel")
        return "ok"

    with patch.object(benchmark_module, "process", side_effect=side_effect):
        bench = benchmark_module.Benchmark(["pergunta com erro", "pergunta boa"])
        bench.run()

    assert len(bench.results) == 1
    assert bench.results[0]["query"] == "pergunta boa"
    assert "[ERRO]" in capsys.readouterr().out


def test_report_with_no_results_does_not_crash(benchmark_module, capsys):
    bench = benchmark_module.Benchmark(["q"])
    bench.results = []
    bench.report(total_time=0.0)
    assert "Nenhum resultado" in capsys.readouterr().out