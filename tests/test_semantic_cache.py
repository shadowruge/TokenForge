from unittest.mock import patch, MagicMock
import numpy as np
import pytest

from semantic_cache import SemanticCache


@pytest.fixture
def semantic_cache():
    """SemanticCache com o modelo de embeddings mockado (não baixa nada da internet)."""
    with patch("semantic_cache.SentenceTransformer") as mock_st:
        mock_model = MagicMock()
        mock_st.return_value = mock_model
        yield SemanticCache(), mock_model


def test_similarity_identical_vectors_is_one():
    cache = SemanticCache.__new__(SemanticCache)  # não chama __init__ (evita carregar modelo)
    v = np.array([1.0, 2.0, 3.0])
    assert cache.similarity(v, v) == pytest.approx(1.0)


def test_similarity_orthogonal_vectors_is_zero():
    cache = SemanticCache.__new__(SemanticCache)
    v1 = np.array([1.0, 0.0])
    v2 = np.array([0.0, 1.0])
    assert cache.similarity(v1, v2) == pytest.approx(0.0)


def test_get_returns_none_on_empty_db(semantic_cache):
    cache, mock_model = semantic_cache
    mock_model.encode.return_value = np.array([1.0, 0.0])
    assert cache.get("qualquer pergunta") is None


def test_set_then_get_similar_query_hits_cache(semantic_cache):
    cache, mock_model = semantic_cache
    same_vector = np.array([1.0, 0.0, 0.0])
    mock_model.encode.return_value = same_vector

    cache.set("qual a capital do brasil", "Brasília")
    result = cache.get("qual eh a capital do brasil")

    assert result == "Brasília"


def test_get_below_threshold_returns_none(semantic_cache):
    cache, mock_model = semantic_cache

    # set usa um vetor, get usa um vetor ortogonal (similaridade 0)
    mock_model.encode.side_effect = [
        np.array([1.0, 0.0]),  # chamada do set()
        np.array([0.0, 1.0]),  # chamada do get()
    ]

    cache.set("pergunta original", "resposta")
    result = cache.get("pergunta totalmente diferente")

    assert result is None