import json
import pytest

from router import MCPRouter

REGISTRY_CONTENT = {
    "categories": {
        "programming": {"description": "programacao"},
        "token_optimization": {"description": "otimizacao"},
        "rag_memory": {"description": "memoria"},
        "reasoning_agents": {"description": "raciocinio"},
    }
}


@pytest.fixture
def registry_path(tmp_path):
    path = tmp_path / "registry.json"
    path.write_text(json.dumps(REGISTRY_CONTENT), encoding="utf-8")
    return str(path)


def test_missing_registry_raises_file_not_found(tmp_path):
    missing_path = str(tmp_path / "nao_existe.json")
    with pytest.raises(FileNotFoundError):
        MCPRouter(registry_path=missing_path)


def test_route_to_programming(registry_path):
    router = MCPRouter(registry_path=registry_path)
    assert router.route("mostrar o codigo do repo") == REGISTRY_CONTENT["categories"]["programming"]


def test_route_to_token_optimization(registry_path):
    router = MCPRouter(registry_path=registry_path)
    assert router.route("buscar na web") == REGISTRY_CONTENT["categories"]["token_optimization"]


def test_route_to_rag_memory(registry_path):
    router = MCPRouter(registry_path=registry_path)
    assert router.route("preciso de memoria de longo prazo") == REGISTRY_CONTENT["categories"]["rag_memory"]


def test_route_default_is_reasoning_agents(registry_path):
    router = MCPRouter(registry_path=registry_path)
    assert router.route("qualquer coisa sem palavra-chave") == REGISTRY_CONTENT["categories"]["reasoning_agents"]


def test_route_is_case_insensitive(registry_path):
    router = MCPRouter(registry_path=registry_path)
    assert router.route("MOSTRAR O REPO") == REGISTRY_CONTENT["categories"]["programming"]