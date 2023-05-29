# Filename: stablelm_interaction.py

from transformers import AutoTokenizer, AutoModelForCausalLM

class StableLMIntegration:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("./stablelm-7b-sft-v7-epoch-3")
        self.model = AutoModelForCausalLM.from_pretrained("./stablelm-7b-sft-v7-epoch-3", torch_dtype=torch.float16)

    def generate_response(self, prompt, past_key_values=None):
        inputs = self.tokenizer.encode(prompt, return_tensors='pt')
        outputs = self.model.generate(inputs, max_length=384, num_return_sequences=1, no_repeat_ngram_size=2, do_sample=True, temperature=0.7, past_key_values=past_key_values)
        response = self.tokenizer.decode(outputs[0])
        return response, outputs.past_key_values

    def generate_multiple_responses(self, prompt, num_responses=3, past_key_values=None):
        inputs = self.tokenizer.encode(prompt, return_tensors='pt')
        outputs = self.model.generate(inputs, max_length=384, num_return_sequences=num_responses, no_repeat_ngram_size=2, do_sample=True, temperature=0.7, past_key_values=past_key_values)
        responses = [self.tokenizer.decode(output) for output in outputs]
        return responses, outputs.past_key_values
