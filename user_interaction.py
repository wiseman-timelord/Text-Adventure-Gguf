# Filename: user_interaction.py

from transformers import AutoTokenizer, AutoModelForCausalLM
from game_mechanics import GameMechanics
from locations_roleplayers import locations

class Action:
    def __init__(self, action_name, action_method):
        self.action_name = action_name
        self.action_method = action_method

    def execute(self, game_parameters):
        self.action_method(game_parameters)

def handle_user_input(user_input, game_mechanics):
    # Parse the user's input and update the game parameters
    actions = {
        'quit': Action('quit', game_mechanics.user_action),
        # Add more actions here
    }

    if user_input in actions:
        actions[user_input].execute(user_input)
    else:
        print(f"Invalid command: {user_input}")

def generate_ai_response(game_mechanics):
    # Generate the AI's response using the StableLM model
    tokenizer = AutoTokenizer.from_pretrained("./stablelm-7b-sft-v7-epoch-3")
    model = AutoModelForCausalLM.from_pretrained("./stablelm-7b-sft-v7-epoch-3")
    inputs = tokenizer.encode(game_mechanics.user_actions[-1], return_tensors='pt')
    outputs = model.generate(inputs, max_length=384)
    response = tokenizer.decode(outputs[0])
    return response

def play_game():
    game_mechanics = GameMechanics()
    while True:
        user_input = input('> ')
        user_input = user_input.strip()
        handle_user_input(user_input, game_mechanics)
        ai_response = generate_ai_response(game_mechanics)
        print(ai_response)
        if game_mechanics.is_game_over():
            break
