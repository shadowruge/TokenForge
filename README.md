# TokenForge

Protótipo de camada de otimização e cache para consultas a LLMs locais (via [Ollama](https://ollama.com/)). O objetivo é reduzir chamadas redundantes ao modelo e o volume de tokens enviados, usando cache exato, cache semântico e um roteador simples de categorias.

## Status

🚧 Projeto em estágio inicial / protótipo. Todos os módulos importam e rodam sem erro de código (verificado); a execução completa de `main.py`/`benchmark.py` ainda depende de dois serviços externos: Ollama local e download do modelo de embeddings na primeira execução.

## Estrutura

| Arquivo                | Responsabilidade                                                                           |
| ---------------------- | ------------------------------------------------------------------------------------------ |
| `main.py`            | Loop principal: recebe a pergunta, consulta os caches, otimiza o texto e chama o LLM local |
| `cache.py`           | `AutoCache` — cache exato (chave = texto da query)                                      |
| `semantic_cache.py`  | `SemanticCache` — cache por similaridade de embeddings (`sentence-transformers`)      |
| `token_optimizer.py` | `TokenOptimizer` — limpeza e compressão/resumo de texto antes de enviar ao modelo      |
| `router.py`          | `MCPRouter` — roteia a query para uma categoria definida em `registry.json`           |
| `benchmark.py`       | Mede tempo de resposta rodando`main.process()` em lote                                   |
| `registry.json`      | Categorias usadas pelo`MCPRouter`                                                        |
| `Dockerfile`         | Imagem Docker da aplicação                                                               |

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

Fluxo:

1. Verifica cache exato (`AutoCache`)
2. Verifica cache semântico (`SemanticCache`, threshold de similaridade 0.85)
3. Se não houver hit, otimiza o texto (`TokenOptimizer`) e envia ao LLM local
4. Salva a resposta em ambos os caches

## Benchmark

```bash
python benchmark.py
```

Roda uma lista fixa de queries (com repetições propositais) e imprime tempo total, tempo médio, tamanho total das respostas e quantidade de entradas no cache exato.

## Docker

```bash
docker build -t tokenforge .
docker run -e OLLAMA_HOST=http://host.docker.internal:11434 tokenforge
```

Em Linux (sem Docker Desktop), pode ser necessário `--add-host=host.docker.internal:host-gateway` ou `--network host`.

## Limitações conhecidas

- O cache semântico é mantido em memória, sem persistência entre execuções.
- `main.py` depende de um Ollama local respondendo em `OLLAMA_HOST` (padrão `http://localhost:11434`).
- O modelo de embeddings (`all-MiniLM-L6-v2`) é baixado do Hugging Face na primeira execução — requer acesso à internet nesse momento.

## Licença

Distribuído sob a licença MIT — veja [LICENSE](LICENSE).

**AUTOR**

Izaias de oliveira elias
