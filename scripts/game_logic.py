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