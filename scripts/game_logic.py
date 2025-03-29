# Filename: data/scripts/game_logic.py
from dataclasses import dataclass, field
import nltk
from typing import Dict
import random
import json

@dataclass
class Roleplayer:
    name: str
    description: str
    maturity: str

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def get_maturity(self) -> str:
        return self.maturity

@dataclass
class Location:
    name: str
    description: str
    maturity: str
    roleplayers: list[Roleplayer] = field(default_factory=list)
    connections: list[str] = field(default_factory=list)

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def get_maturity(self) -> str:
        return self.maturity

    def get_roleplayers(self) -> list[Roleplayer]:
        return self.roleplayers

    def add_roleplayer(self, roleplayer: Roleplayer) -> None:
        self.roleplayers.append(roleplayer)

    def remove_roleplayer(self, roleplayer: Roleplayer) -> None:
        self.roleplayers.remove(roleplayer)

class GameMechanics:
    def __init__(self):
        self.location_types = {
            "forest": ("A dense forest with tall trees.", "clean"),
            "cave": ("A dark, damp cave.", "moderate"),
            "village": ("A peaceful village.", "clean"),
            "woods": ("A dark and mysterious woods.", "lewd"),
            "pub": ("A lively pub.", "moderate"),
            "lake": ("A serene lake.", "clean")
        }
        self.roleplayer_types = [
            ("villager", "A friendly villager.", "clean"),
            ("bandit", "A dangerous bandit.", "lewd"),
            ("friends", "Your close friends.", "clean"),
            ("gang", "A group of friends.", "moderate"),
            ("strangers", "People you do not know.", "lewd"),
            ("police", "Officers maintaining law and order.", "clean")
        ]
        self.locations = self._initialize_locations()
        self.game_state = {
            'current_location': 'forest_0',  # Adjusted to match generated locations
            'score': 0,
            'inventory': [],
            'health': 100
        }

    def _initialize_locations(self) -> Dict[str, Location]:
        return self._generate_locations(5)  # Use dynamic generation instead of hardcoded

    def _generate_locations(self, num_locations):
        locations = {}
        loc_names = []
        for i in range(num_locations):
            loc_type = random.choice(list(self.location_types.keys()))
            desc, maturity = self.location_types[loc_type]
            loc_name = f"{loc_type}_{i}"
            roleplayers = [Roleplayer(*random.choice(self.roleplayer_types)) 
                         for _ in range(random.randint(1, 3))]
            locations[loc_name] = Location(loc_name, desc, maturity, roleplayers, [])
            loc_names.append(loc_name)
        # Linear connections for simplicity
        for i in range(len(loc_names) - 1):
            locations[loc_names[i]].connections.append(loc_names[i + 1])
            locations[loc_names[i + 1]].connections.append(loc_names[i])
        return locations

    def get_current_location(self) -> Location:
        return self.locations[self.game_state['current_location']]

    def parse_user_input(self, text: str) -> tuple[list[str], list[str]]:
        tokens = nltk.word_tokenize(text)
        tagged = nltk.pos_tag(tokens)
        verbs = [word for word, pos in tagged if pos in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']]
        nouns = [word for word, pos in tagged if pos in ['NN', 'NNS', 'NNP', 'NNPS']]
        return verbs, nouns

    def move_location(self, new_location: str) -> bool:
        if new_location in self.locations:
            self.game_state['current_location'] = new_location
            return True
        return False

    def is_game_over(self) -> bool:
        return self.game_state['health'] <= 0 or 'exit' in self.game_state.get('flags', [])

    def update_score(self, points: int) -> None:
        self.game_state['score'] += points

    def add_inventory(self, item: str) -> None:
        self.game_state['inventory'].append(item)

    def remove_inventory(self, item: str) -> bool:
        if item in self.game_state['inventory']:
            self.game_state['inventory'].remove(item)
            return True
        return False

    def handle_command(self, verbs, nouns):
        """Process player commands based on parsed input."""
        current_location = self.get_current_location()
        
        if "go" in verbs and nouns:
            target = nouns[0].lower()
            if target in current_location.connections:
                if self.move_location(target):
                    return f"You move to {target}."
                return "You can't move there right now."
            return "You can't go there from here."
        
        elif "talk" in verbs and nouns:
            target = nouns[0].lower()
            for rp in current_location.get_roleplayers():
                if target in rp.get_name().lower():
                    return f"{rp.get_name()} says: 'Greetings, traveler!'"
            return "There's no one here by that name."
        
        elif "look" in verbs:
            exits = ", ".join(current_location.connections)
            return f"{current_location.get_name()}: {current_location.get_description()}\nExits: {exits}"
        
        elif "take" in verbs and nouns:
            item = nouns[0].lower()
            self.add_inventory(item)  # Placeholder: Add item availability check later
            return f"You take the {item}."
        
        elif "inventory" in verbs or "i" in verbs:
            items = ", ".join(self.game_state['inventory']) if self.game_state['inventory'] else "nothing"
            return f"You have: {items}"
        
        elif "use" in verbs and nouns:
            item = nouns[0].lower()
            if item in self.game_state['inventory']:
                if item == "potion":
                    self.game_state['health'] = min(100, self.game_state['health'] + 20)
                    self.remove_inventory(item)
                    return "You drink the potion and restore 20 health."
                return f"You can't use the {item}."
            return "You don't have that item."
        
        return "I don't understand that command."

    def update_roamers(self):
        """Move roleplayers between locations randomly."""
        for loc_name, loc in self.locations.items():
            for rp in loc.get_roleplayers():
                if random.random() < 0.1:  # 10% chance to move
                    new_loc = random.choice(list(self.locations.keys()))
                    if new_loc != loc_name:
                        loc.remove_roleplayer(rp)
                        self.locations[new_loc].add_roleplayer(rp)

    def trigger_encounter(self):
        """Randomly trigger an encounter."""
        if random.random() < 0.2:  # 20% chance per turn
            encounter_type = random.choice(["item", "fight", "dialogue"])
            if encounter_type == "item":
                item = random.choice(["coin", "potion"])
                self.add_inventory(item)
                return f"You found a {item}!"
            elif encounter_type == "fight":
                enemy = random.choice(["bandit", "wolf"])
                self.game_state['health'] -= 10
                self.update_score(5)
                return f"A {enemy} attacks! You lose 10 health but gain 5 points."
            elif encounter_type == "dialogue":
                return "A mysterious figure approaches and says, 'Beware the shadows.'"
        return None

    def save_game(self, filepath="data/savegame.json"):
        with open(filepath, "w") as f:
            json.dump({
                "game_state": self.game_state,
                "locations": {k: {
                    "name": v.name, "description": v.description, "maturity": v.maturity,
                    "roleplayers": [{"name": r.name, "description": r.description, "maturity": r.maturity} 
                                   for r in v.roleplayers],
                    "connections": v.connections
                } for k, v in self.locations.items()}
            }, f, indent=2)
    
    def load_game(self, filepath="data/savegame.json"):
        try:
            with open(filepath, "r") as f:
                data = json.load(f)
                self.game_state = data["game_state"]
                self.locations = {
                    k: Location(v["name"], v["description"], v["maturity"],
                                [Roleplayer(r["name"], r["description"], r["maturity"]) for r in v["roleplayers"]],
                                v["connections"])
                    for k, v in data["locations"].items()
                }
        except FileNotFoundError:
            self.locations = self._generate_locations(5)  # Fallback to new game