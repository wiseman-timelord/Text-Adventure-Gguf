# Filename: data/scripts/ai_integration.py
from llama_cpp import Llama

class AIResponse:
    def __init__(self, model_path, n_ctx):
        self.llm = Llama(model_path=model_path, n_ctx=n_ctx)
        
    def generate_response(self, prompt):
        return self.llm(prompt)["choices"][0]["text"]