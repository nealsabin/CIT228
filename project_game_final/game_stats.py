class GameStats:
    """Track stats for Fish Invasion"""
    def __init__(self,ai_game):
        """Init stats"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.high_score = 0
        self.game_active = False

    def reset_stats(self):
        """Init stats that can change during the game"""
        self.submarines_left = self.settings.submarine_limit
        self.score = 0
        self.level = 1