import re

class TokenOptimizer:

    def __init__(self):
        self.max_chars = 4000

    def clean_text(self, text: str) -> str:
        # remove lixo comum
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'<.*?>', '', text)  # remove HTML
        return text.strip()

    def compress(self, text: str) -> str:
        # compressão simples (pode evoluir pra LLM)
        if len(text) > self.max_chars:
            return text[:self.max_chars] + "..."
        return text

    def summarize(self, text: str) -> str:
        # versão simples (depois você liga no Ollama)
        sentences = text.split(".")
        return ".".join(sentences[:3]) + "."

    def optimize(self, text: str, mode="auto") -> str:
        text = self.clean_text(text)

        if mode == "compress":
            return self.compress(text)

        if mode == "summary":
            return self.summarize(text)

        # auto mode
        if len(text) > self.max_chars:
            return self.summarize(text)

        return text
