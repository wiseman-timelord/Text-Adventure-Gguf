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
    
    # Initialize game state
    game_mechanics.game_state["location"] = config["model_settings"].get("starting_location", "house")
    
    while not game_mechanics.is_game_over():
        interface.display_input_prompt()
        user_input = parse_user_input()
        verbs, nouns = game_mechanics.parse_user_input(user_input)
        ai_response = ai.generate_response(f"Game context: {game_mechanics.game_state}\nPlayer says: {user_input}")
        interface.display_conversation(ai_response)
        interface.display_status(
            time_left="10:00",
            location=game_mechanics.game_state["location"],
            score=game_mechanics.game_state["score"]
        )

if __name__ == "__main__":
    main()