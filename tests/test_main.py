from unittest.mock import patch


def test_process_calls_llm_on_full_miss(main_module):
    with patch.object(main_module, "call_llm", return_value="resposta do llm") as mock_llm:
        result = main_module.process("pergunta nova e unica 12345")

    assert result == "resposta do llm"
    mock_llm.assert_called_once()


def test_process_saves_response_in_exact_cache(main_module):
    with patch.object(main_module, "call_llm", return_value="resposta salva"):
        main_module.process("pergunta para salvar no cache")

    cached = main_module.cache.get("pergunta para salvar no cache")
    assert cached == {"response": "resposta salva"}


def test_process_returns_exact_cache_hit_without_calling_llm(main_module):
    main_module.cache.set("pergunta ja respondida", "resposta em cache")

    with patch.object(main_module, "call_llm") as mock_llm:
        result = main_module.process("pergunta ja respondida")

    assert result == "resposta em cache"
    mock_llm.assert_not_called()


def test_process_optimizes_query_before_calling_llm(main_module):
    with patch.object(main_module, "call_llm", return_value="ok") as mock_llm, \
         patch.object(main_module.optimizer, "optimize", return_value="query otimizada") as mock_optimize:
        main_module.process("  query   com   espacos  sobrando  ")

    mock_optimize.assert_called_once()
    mock_llm.assert_called_once_with("query otimizada")