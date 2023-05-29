# Filename: stablelm_interaction.py

from transformers import AutoTokenizer, AutoModelForCausalLM

class StableLMIntegration:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("./stablelm-7b-sft-v7-epoch-3")
        self.model = AutoModelForCausalLM.from_pretrained("./stablelm-7b-sft-v7-epoch-3")

    def generate_response(self, prompt):
        inputs = self.tokenizer.encode(prompt, return_tensors='pt')
        outputs = self.model.generate(inputs, max_length=384, num_return_sequences=1, no_repeat_ngram_size=2, do_sample=True, temperature=0.7)
        response = self.tokenizer.decode(outputs[0])
        return response

    def generate_multiple_responses(self, prompt, num_responses=3):
        inputs = self.tokenizer.encode(prompt, return_tensors='pt')
        outputs = self.model.generate(inputs, max_length=384, num_return_sequences=num_responses, no_repeat_ngram_size=2, do_sample=True, temperature=0.7)
        responses = [self.tokenizer.decode(output) for output in outputs]
        return responses
