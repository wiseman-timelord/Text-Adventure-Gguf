# Filename: game_mechanics.py
import nltk
import random

class GameMechanics:
    def __init__(self):
        self.user_actions = []
        self.ai_actions = []
        self.game_state = {}
        self.game_over = False
        self.score = 0

    def user_action(self, action):
        self.user_actions.append(action)
        self.update_game_state()

    def ai_action(self, action):
        self.ai_actions.append(action)
        self.update_game_state()

    def update_game_state(self):
        self.game_state = {
            'user_actions': self.user_actions,
            'ai_actions': self.ai_actions
        }
        self.check_game_over()
        self.calculate_score()

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
        # Check if the game is over based on the game state
        # For example, if the user has performed a certain action or if a certain event has occurred
        if 'quit' in self.user_actions:
            self.game_over = True

    def calculate_score(self):
        # Calculate the score based on the game state
        # For example, the score can be the number of actions performed by the user
        self.score = len(self.user_actions)

    def get_score(self):
        return self.score

    def is_game_over(self):
        return self.game_over
