# Filename: data/scripts/ai_integration.py
from llama_cpp import Llama

class AIResponse:
    def __init__(self):
        self.llm = Llama(
            model_path="models/text-adventure.gguf",
            n_ctx=8192
        )
        
    def generate_response(self, prompt):
        return self.llm(prompt)["choices"][0]["text"]