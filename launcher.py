# Filename: launcher.py
from scripts.game_logic import GameMechanics
from scripts.user_interface import InterfaceLayout
from scripts.ai_integration import AIResponse
from scripts.input_handling import parse_user_input
import json
from pathlib import Path

def load_config():
    config_path = Path(__file__).parent / "data" / "persistent.json"
    with open(config_path) as f:
        return json.load(f)

def main():
    config = load_config()
    game_mechanics = GameMechanics()
    interface = InterfaceLayout()
    ai = AIResponse()
    
    # Load saved game state or set starting location from config
    game_mechanics.load_game()  # Attempts to load from savegame.json, generates new if not found
    if "location" not in game_mechanics.game_state:  # If no saved location
        game_mechanics.game_state["location"] = config["model_settings"].get(
            "starting_location", list(game_mechanics.locations.keys())[0]
        )
    
    while not game_mechanics.is_game_over():
        # Display current game status
        interface.display_status(
            time_left="10:00",  # Static for now, could be dynamic
            location=game_mechanics.game_state["current_location"],
            score=game_mechanics.game_state["score"]
        )
        
        # Prompt for and get user input
        interface.display_input_prompt()
        user_input = parse_user_input()
        verbs, nouns = game_mechanics.parse_user_input(user_input)
        
        # Handle command first
        command_result = game_mechanics.handle_command(verbs, nouns)
        
        # Update roamers and check for encounters
        game_mechanics.update_roamers()
        encounter_result = game_mechanics.trigger_encounter()
        
        # Handle save command explicitly
        if "save" in user_input.lower():
            game_mechanics.save_game()
            interface.display_conversation("Game saved!")
            continue  # Skip AI response for save command
        
        # Combine results for AI context
        context = f"Game state: {game_mechanics.game_state}\nPlayer input: {user_input}"
        if command_result:
            context += f"\nCommand result: {command_result}"
        if encounter_result:
            context += f"\nEncounter: {encounter_result}"
        
        # Generate and display AI response
        ai_response = ai.generate_response(context)
        interface.display_conversation(
            f"{command_result or ''}\n{encounter_result or ''}\nAI: {ai_response}"
        )
    
    # Clean up on game over
    interface.display_conversation("Game Over! Thanks for playing.")

if __name__ == "__main__":
    main()