# Filename: game_parameters.py

import json
import pickle

class GameParameters:
    def __init__(self):
        self.parameters = {
            "user_input": "",
            "previous_summary": "",
            "location": "",
            "ai_roleplayers": []
        }

    def update_user_input(self, user_input):
        self.parameters["user_input"] = user_input

    def update_previous_summary(self, previous_summary):
        self.parameters["previous_summary"] = previous_summary

    def update_location(self, location):
        self.parameters["location"] = location

    def update_ai_roleplayers(self, ai_roleplayers):
        self.parameters["ai_roleplayers"] = ai_roleplayers

    def get_parameters(self):
        return self.parameters

    def save_parameters(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.parameters, f)

    def load_parameters(self, filename):
        with open(filename, 'rb') as f:
            self.parameters = pickle.load(f)
