FROM python:3.11-slim

WORKDIR /app

# Dependências de sistema mínimas para sentence-transformers/torch
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# URL do Ollama rodando no host (ajuste conforme seu ambiente).
# No Docker Desktop (Mac/Windows), use http://host.docker.internal:11434
ENV OLLAMA_HOST=http://host.docker.internal:11434

CMD ["python", "main.py"]