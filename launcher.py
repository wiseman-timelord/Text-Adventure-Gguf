# Filename: launcher.py
from scripts.game_logic import GameMechanics
from scripts.user_interface import InterfaceLayout
from scripts.ai_integration import AIResponse
from scripts.input_handling import parse_user_input
import json
from pathlib import Path
from scripts.temporary import DATA_DIR  # Import DATA_DIR for model path

def load_config():
    config_path = Path(__file__).parent / "data" / "persistent.json"
    with open(config_path) as f:
        return json.load(f)

def main():
    config = load_config()
    game_mechanics = GameMechanics()
    interface = InterfaceLayout()
    
    # Initialize AI with configurable model path and context size
    model_settings = config["model_settings"]
    model_path = str(DATA_DIR / model_settings["model_dir"] / model_settings["model_file"])
    ai = AIResponse(model_path=model_path, n_ctx=model_settings["context_size"])
    
    # Load saved game state or set starting location from config
    game_mechanics.load_game()  # Attempts to load from savegame.json, generates new if not found
    if "current_location" not in game_mechanics.game_state:  # Adjusted key to match game_state
        game_mechanics.game_state["current_location"] = config["model_settings"].get(
            "starting_location", list(game_mechanics.locations.keys())[0]
        )
    
    while not game_mechanics.is_game_over():
        # Display current game status with expanded parameters
        interface.display_status(
            time_left="10:00",  # Static for now, could be dynamic
            location=game_mechanics.game_state["current_location"],
            score=game_mechanics.game_state["score"],
            health=game_mechanics.game_state["health"],
            inventory=game_mechanics.game_state["inventory"]
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
        
        # Improved AI prompt with richer context
        prompt = (
            f"You are the game master of a text-based RPG. "
            f"The player is at {game_mechanics.game_state['current_location']}. "
            f"Their health is {game_mechanics.game_state['health']}, score is {game_mechanics.game_state['score']}. "
            f"Inventory: {', '.join(game_mechanics.game_state['inventory']) if game_mechanics.game_state['inventory'] else 'none'}. "
        )
        if command_result:
            prompt += f"The player attempted '{user_input}', resulting in: {command_result}. "
        else:
            prompt += f"The player says: '{user_input}'. "
        if encounter_result:
            prompt += f"Also, {encounter_result}. "
        prompt += "Respond as the game master, describing what happens next."
        
        # Generate and display AI response
        ai_response = ai.generate_response(prompt)
        interface.display_conversation(
            f"{command_result or ''}\n{encounter_result or ''}\nAI: {ai_response}"
        )
    
    # Clean up on game over
    interface.display_conversation("Game Over! Thanks for playing.")

if __name__ == "__main__":
    main()