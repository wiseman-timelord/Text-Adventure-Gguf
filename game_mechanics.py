class GameMechanics:
    def __init__(self):
        self.user_actions = []
        self.ai_actions = []
        self.game_state = {}

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
