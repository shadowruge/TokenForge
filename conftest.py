import sys
from unittest.mock import patch, MagicMock

import numpy as np
import pytest


@pytest.fixture
def main_module():
    """
    Importa main.py com o SentenceTransformer mockado.

    main.py instancia SemanticCache() (que baixa um modelo do Hugging Face)
    assim que é importado. Para testar main.py sem depender de rede, mockamos
    a classe antes do import e forçamos um import "fresco" do módulo.
    """
    sys.modules.pop("main", None)

    with patch("semantic_cache.SentenceTransformer") as mock_st:
        mock_model = MagicMock()
        mock_model.encode.return_value = np.array([1.0, 0.0, 0.0])
        mock_st.return_value = mock_model

        import main as main_mod
        yield main_mod

    sys.modules.pop("main", None)


@pytest.fixture
def benchmark_module(main_module):
    """Importa benchmark.py reaproveitando o main.py já mockado (sem rede)."""
    sys.modules.pop("benchmark", None)
    import benchmark as benchmark_mod
    yield benchmark_mod
    sys.modules.pop("benchmark", None)