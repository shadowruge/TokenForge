from cache import AutoCache


def test_get_miss_returns_none():
    cache = AutoCache()
    assert cache.get("pergunta nunca vista") is None


def test_set_then_get_returns_response():
    cache = AutoCache()
    cache.set("qual a capital do brasil", "Brasília")
    result = cache.get("qual a capital do brasil")
    assert result == {"response": "Brasília"}


def test_get_is_exact_match_only():
    cache = AutoCache()
    cache.set("qual a capital do brasil", "Brasília")
    # variação da mesma pergunta não deve dar hit (isso é papel do SemanticCache)
    assert cache.get("qual eh a capital do brasil") is None


def test_set_overwrites_previous_response():
    cache = AutoCache()
    cache.set("oi", "resposta 1")
    cache.set("oi", "resposta 2")
    assert cache.get("oi") == {"response": "resposta 2"}


def test_multiple_keys_are_independent():
    cache = AutoCache()
    cache.set("pergunta a", "resposta a")
    cache.set("pergunta b", "resposta b")
    assert cache.get("pergunta a") == {"response": "resposta a"}
    assert cache.get("pergunta b") == {"response": "resposta b"}