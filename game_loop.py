import json
from user_interaction import handle_user_input, generate_ai_response, generate_ai_summary
from game_mechanics import GameMechanics

def game_loop(game_parameters):
    game_mechanics = GameMechanics()
    while not game_mechanics.is_game_over():
        # Prompt the user for input
        user_input = input('> ')

        # Handle the user's input
        handle_user_input(user_input, game_parameters, game_mechanics)

        # Generate the AI's response
        ai_response = generate_ai_response(game_parameters)

        # Print the AI's response
        print(ai_response)

        # Generate the AI's summary
        ai_summary = generate_ai_summary(game_parameters)

        # Print the AI's summary
        print(ai_summary)
