# Filename: game_mechanics.py
import nltk
import random
from locations_roleplayers import locations

class GameMechanics:
    def __init__(self):
        self.user_actions = []
        self.ai_actions = []
        self.game_state = {
            'location': '',
            'roleplayers': [],
        }
        self.game_over = False

    def user_action(self, action):
        self.user_actions.append(action)
        self.update_game_state()

    def ai_action(self, action):
        self.ai_actions.append(action)
        self.update_game_state()

    def update_game_state(self):
        # Update game state based on user and AI actions
        # This can include updating the location and roleplayers
        pass

    def parse_user_input(self, user_input):
        # Tokenize the user input
        tokens = nltk.word_tokenize(user_input)
        # Tag the tokens with part of speech tags
        tagged = nltk.pos_tag(tokens)
        # Extract the verbs and nouns
        verbs = [word for word, pos in tagged if pos in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']]
        nouns = [word for word, pos in tagged if pos in ['NN', 'NNS', 'NNP', 'NNPS']]
        # Return the verbs and nouns as the action and object
        return verbs, nouns

    def check_game_over(self):
        # The game only ends when the player decides to exit
        if 'exit' in self.user_actions:
            self.game_over = True

    def is_game_over(self):
        return self.game_over
