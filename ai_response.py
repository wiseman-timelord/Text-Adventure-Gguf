# Filename: ai_response.py

from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

class AIResponse:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("./stablelm-7b-sft-v7-epoch-3")
        self.model = AutoModelForCausalLM.from_pretrained("./stablelm-7b-sft-v7-epoch-3")
        self.pipeline = pipeline('text-generation', model=self.model, tokenizer=self.tokenizer)

    def generate_response(self, prompt):
        inputs = self.tokenizer.encode(prompt, return_tensors='pt', truncation=True, max_length=384)
        outputs = self.model.generate(inputs, max_length=384)
        response = self.tokenizer.decode(outputs[0])
        return response

    def generate_response_with_pipeline(self, prompt):
        response = self.pipeline(prompt, max_length=384, do_sample=True, temperature=0.7)
        return response[0]['generated_text']
