🧠 TokenForge

AI Token Optimization Engine with Semantic Cache, MCP Routing and RAG Support

Reduce tokens. Increase intelligence.

🚀 Overview

TokenForge AI is a lightweight middleware designed to optimize LLM usage, dramatically reducing token consumption while improving response speed and consistency.

It combines:

🔥 Token optimization (compression + summarization)
⚡ Multi-layer caching (exact + semantic)
🧠 MCP-based tool routing
📊 Built-in benchmarking

👉 Result: up to 90% reduction in LLM calls and cost.

```
User Input
   ↓
Token Optimizer
   ↓
Cache Layer
 ├── Exact Cache (hash)
 └── Semantic Cache (embeddings)
   ↓
MCP Router
   ↓
LLM (Ollama / OpenAI / etc)
   ↓
Response + Cache Storage.
```

⚙️ Features
🔥 Token Optimization
Text cleaning
Smart truncation
Lightweight summarization
Adaptive token control

⚡ Multi-Layer Cache
Exact match (instant response)
Semantic similarity (embedding-based)
Reduces redundant LLM calls

🧠 MCP Routing
Intelligent tool selection
Supports:
Git
Filesystem
Web fetch
Memory (RAG-ready)

📊 Benchmark System
Measures:
Response time
Cache hit rate
Estimated token savings.

📦 Installation.
```
git clone https://github.com/SEU_USER/tokenmind-ai.git
cd tokenmind-ai
pip install -r requirements.txt
```

▶️ Usage
Run the system.
```
python main.py

```

Example
```
Pergunta: como usar mcp com python
Resposta: ...
```
📊 Run Benchmark


```
python benchmark.py
```

Expected output:
```
Total queries: 5
Tempo médio: 0.45s
Cache hit rate: 60%
Economia estimada: 70–90%
```

🔌 LLM Integration (Ollama)

Make sure Ollama is running:

```
ollama run qwen2.5:1.5b
```
API endpoint used:
```
http://localhost:11434/api/generate
```

🧠 Semantic Cache (How it works)
Converts queries into embeddings
Finds similar past queries
Returns cached response if similarity threshold is met

📁 Project Structure

```
.
├── main.py
├── token_optimizer.py
├── cache.py
├── semantic_cache.py
├── router.py
├── benchmark.py
├── registry.json
├── requirements.txt
└── .github/workflows/ci.yml
```
⚙️ Configuration
registry.json

Defines MCP tools and routing behavior.

🚀 Roadmap
Redis persistent cache
Vector DB (Chroma / FAISS)
FastAPI (SaaS API)
Multi-user isolation
Dashboard (token analytics)
Auto RAG integration

🔐 Security Considerations

Planned improvements:

Input validation
Prompt injection protection
Tool sandboxing
Rate limiting

📈 Benchmark Insight
Scenario	Without TokenMind	With TokenMind
LLM Calls	100	~10–30
Latency	High	Low
Token Usage	100%	~10–40%
💡 Use Cases
AI SaaS cost reduction
Chatbot optimization
RAG pipelines
Local LLM performance boost
Developer tooling (MCP agents)
🤝 Contributing

Pull requests are welcome.

For major changes, open an issue first to discuss what you’d like to change.

📄 License

MIT License

👤 Author

Izaias Elias
GitHub: https://github.com/shadowruge

⭐ Final Note

TokenMind AI is not just a tool — it’s a cost-optimization layer for AI systems.
