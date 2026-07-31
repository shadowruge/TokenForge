# TokenForge

Protótipo de camada de otimização e cache para consultas a LLMs locais (via [Ollama](https://ollama.com/)). O objetivo é reduzir chamadas redundantes ao modelo e o volume de tokens enviados, usando cache exato, cache semântico e um roteador simples de categorias.

## Status

🚧 Projeto em estágio inicial / protótipo. Ainda não possui testes automatizados.

## Estrutura

| Arquivo | Responsabilidade |
|---|---|
| `main.py` | Loop principal: recebe a pergunta, consulta os caches, otimiza o texto e chama o LLM local |
| `cache.py` | `AutoCache` — cache exato (chave = texto da query) |
| `semantic_cache.py` | `SemanticCache` — cache por similaridade de embeddings (`sentence-transformers`) |
| `token_optimizer.py` | `TokenOptimizer` — limpeza e compressão/resumo de texto antes de enviar ao modelo |
| `router.py` | `MCPRouter` — roteia a query para uma categoria definida em `registry.json` |
| `benchmark.py` | Mede tempo de resposta e economia estimada de tokens rodando `main.process()` em lote |
| `registry.json` | Categorias usadas pelo `MCPRouter` |

## Requisitos

- Python 3.9+
- [Ollama](https://ollama.com/) rodando localmente com o modelo `qwen2.5:1.5b` disponível

```bash
pip install -r requirements.txt
```

## Uso

```bash
python main.py
```

Digite a pergunta no prompt interativo. O fluxo é:

1. Verifica cache exato (`AutoCache`)
2. Verifica cache semântico (`SemanticCache`, threshold de similaridade 0.85)
3. Se não houver hit, otimiza o texto (`TokenOptimizer`) e envia ao LLM local
4. Salva a resposta em ambos os caches

## Benchmark

```bash
python benchmark.py
```

Roda uma lista fixa de queries (com repetições propositais) e imprime tempo total, tempo médio e uma estimativa simples de economia de tokens.

## Limitações conhecidas

- O cache semântico é mantido em memória (`list`), sem persistência entre execuções.
- A estimativa de "economia de tokens" no benchmark é um valor fixo (`0.7`), não calculada a partir de tokens reais.
- `router.py` depende do endpoint local do Ollama (`http://localhost:11434`) — sem essa dependência rodando, `main.py` falha na chamada ao LLM.

## Licença

Distribuído sob a licença MIT — veja [LICENSE](LICENSE).

👤 Author

Izaias Elias
GitHub: https://github.com/shadowruge

⭐ Final Note

TokenMind AI is not just a tool — it’s a cost-optimization layer for AI systems.
