import json
from user_interaction import handle_user_input, generate_ai_response, generate_ai_summary

def game_loop(game_parameters):
    while True:
        # Prompt the user for input
        user_input = input('> ')

        # Handle the user's input
        handle_user_input(user_input, game_parameters)

        # Generate the AI's response
        ai_response = generate_ai_response(game_parameters)

        # Print the AI's response
        print(ai_response)

        # Generate the AI's summary
        ai_summary = generate_ai_summary(game_parameters)

        # Print the AI's summary
        print(ai_summary)

        # Check if the game has ended
        if game_parameters['game_end']:
            break

def game_end(game_parameters):
    # Determine if the game has ended
    # This is a placeholder and should be replaced with actual code
    return False
