# Filename: generate_ai_responses.py

import os
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

def load_model(model_name):
    """
    Function to load the model
    """
    model = GPT2LMHeadModel.from_pretrained(model_name)
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    return model, tokenizer

def generate_response(model, tokenizer, prompt, max_length=384):
    """
    Function to generate response from the model
    """
    inputs = tokenizer.encode(prompt, return_tensors='pt')
    outputs = model.generate(inputs, max_length=max_length, num_return_sequences=1, no_repeat_ngram_size=2)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

def main():
    """
    Main function to generate AI responses
    """
    model_name = "./stablelm-7b-sft-v7-epoch-3/"
    model, tokenizer = load_model(model_name)
    
    prompt = input("Enter the prompt: ")
    response = generate_response(model, tokenizer, prompt)
    print("AI Response: ", response)

if __name__ == "__main__":
    main()
