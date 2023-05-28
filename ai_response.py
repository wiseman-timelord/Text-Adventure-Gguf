from transformers import AutoModel, AutoTokenizer

class AIResponse:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("./stablelm-7b-sft-v7-epoch-3")
        self.model = AutoModel.from_pretrained("./stablelm-7b-sft-v7-epoch-3")

    def generate_response(self, prompt):
        inputs = self.tokenizer.encode(prompt, return_tensors='pt')
        outputs = self.model.generate(inputs, max_length=384)
        response = self.tokenizer.decode(outputs[0])
        return response
