# Filename: data/scripts/game_logic.py
from dataclasses import dataclass, field
import nltk
from typing import Dict

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
        self.locations = self._initialize_locations()
        self.game_state = {
            'current_location': 'house',
            'score': 0,
            'inventory': [],
            'health': 100
        }

    def _initialize_locations(self) -> Dict[str, Location]:
        return {
            'house': Location('House', 'A cozy little house.', 'clean', [
                Roleplayer('gang', 'A group of friends.', 'moderate'),
                Roleplayer('friends', 'Your close friends.', 'clean'),
                Roleplayer('strangers', 'People you do not know.', 'lewd')
            ]),
            'street': Location('Street', 'A busy city street.', 'moderate', [
                Roleplayer('police', 'Officers maintaining law and order.', 'clean'),
                Roleplayer('gang', 'A group of friends.', 'moderate'),
                Roleplayer('strangers', 'People you do not know.', 'lewd')
            ]),
            'park': Location('Park', 'A peaceful city park.', 'clean', [
                Roleplayer('friends', 'Your close friends.', 'clean'),
                Roleplayer('strangers', 'People you do not know.', 'lewd')
            ]),
            'woods': Location('Woods', 'A dark and mysterious woods.', 'lewd', [
                Roleplayer('gang', 'A group of friends.', 'moderate'),
                Roleplayer('strangers', 'People you do not know.', 'lewd')
            ]),
            'pub': Location('Pub', 'A lively pub.', 'moderate', [
                Roleplayer('friends', 'Your close friends.', 'clean'),
                Roleplayer('police', 'Officers maintaining law and order.', 'clean'),
                Roleplayer('strangers', 'People you do not know.', 'lewd')
            ]),
            'lake': Location('Lake', 'A serene lake.', 'clean', [
                Roleplayer('friends', 'Your close friends.', 'clean'),
                Roleplayer('strangers', 'People you do not know.', 'lewd')
            ]),
            'car': Location('Car', 'A fast-moving car.', 'moderate', [
                Roleplayer('friends', 'Your close friends.', 'clean'),
                Roleplayer('police', 'Officers maintaining law and order.', 'clean'),
                Roleplayer('gang', 'A group of friends.', 'moderate')
            ]),
            'van': Location('Van', 'A suspicious van.', 'lewd', [
                Roleplayer('gang', 'A group of friends.', 'moderate'),
                Roleplayer('strangers', 'People you do not know.', 'lewd')
            ])
        }

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
            direction = nouns[0].lower()
            if direction in self.locations:
                if self.move_location(direction):
                    return f"You move to the {direction}."
                return "You can't move there right now."
            return "Where do you want to go?"
        
        elif "talk" in verbs and nouns:
            target = nouns[0].lower()
            for rp in current_location.get_roleplayers():
                if target in rp.get_name().lower():
                    return f"{rp.get_name()} says: 'Greetings, traveler!'"
            return "There's no one here by that name."
        
        elif "look" in verbs:
            return f"{current_location.get_name()}: {current_location.get_description()}"
        
        elif "take" in verbs and nouns:
            item = nouns[0].lower()
            # Placeholder: Add items to locations later
            self.add_inventory(item)
            return f"You take the {item}."
        
        return "I don't understand that command."
        
    def _generate_locations(self, num_locations):
        locations = {}
        for i in range(num_locations):
            name, (desc, maturity) = random.choice(list(self.location_types.items()))
            loc_name = f"{name}_{i}"
            roleplayers = [
                Roleplayer(*random.choice(self.roleplayer_types))
                for _ in range(random.randint(1, 3))
            ]
            locations[loc_name] = Location(loc_name, desc, maturity, roleplayers)
        return locations

    def update_roamers(self):
        """Move roleplayers between locations randomly."""
        for loc_name, loc in self.locations.items():
            for rp in loc.get_roleplayers():
                if random.random() < 0.1:  # 10% chance to move
                    new_loc = random.choice(list(self.locations.keys()))
                    if new_loc != loc_name:
                        loc.remove_roleplayer(rp)
                        self.locations[new_loc].add_roleplayer(rp)
                        # Could log this for narrative: f"{rp.get_name()} moved to {new_loc}"
                        
    def trigger_encounter(self):
        """Randomly trigger an encounter."""
        if random.random() < 0.2:  # 20% chance per turn
            encounter_type = random.choice(["item", "fight"])
            if encounter_type == "item":
                item = random.choice(["coin", "potion"])
                self.add_inventory(item)
                return f"You found a {item}!"
            elif encounter_type == "fight":
                enemy = random.choice(["bandit", "wolf"])
                self.game_state['health'] -= 10
                self.update_score(5)
                return f"A {enemy} attacks! You lose 10 health but gain 5 points."
        return None
        
    def save_game(self, filepath="data/savegame.json"):
        with open(filepath, "w") as f:
            json.dump({
                "game_state": self.game_state,
                "locations": {k: {
                    "name": v.name, "description": v.description, "maturity": v.maturity,
                    "roleplayers": [{"name": r.name, "description": r.description, "maturity": r.maturity} for r in v.roleplayers]
                } for k, v in self.locations.items()}
            }, f, indent=2)
    
    def load_game(self, filepath="data/savegame.json"):
        try:
            with open(filepath, "r") as f:
                data = json.load(f)
                self.game_state = data["game_state"]
                self.locations = {
                    k: Location(v["name"], v["description"], v["maturity"],
                                [Roleplayer(r["name"], r["description"], r["maturity"]) for r in v["roleplayers"]])
                    for k, v in data["locations"].items()
                }
        except FileNotFoundError:
            self.locations = self._generate_locations(5)  # Fallback to new game