from transformers import GPT2LMHeadModel, GPT2Tokenizer

class AIResponse:
    def __init__(self):
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        self.model = GPT2LMHeadModel.from_pretrained("gpt2")

    def generate_response(self, prompt):
        inputs = self.tokenizer.encode(prompt, return_tensors='pt')
        outputs = self.model.generate(inputs, max_length=384)
        response = self.tokenizer.decode(outputs[0])
        return response
