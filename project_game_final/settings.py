class Settings:
    """A class to store all settings for Fish Invasion"""

    def __init__(self):
        """Initialize the game settings"""
        self.screen_width = 1000
        self.screen_height = 700
        self.bg_color = (148,195,234)
        
        self.torpedo_width = 20
        self.torpedo_height = 6
        self.torpedo_color = (202,205,215)
        self.torpedoes_allowed = 3
        
        self.school_drop_speed = 10
        
        self.submarine_limit = 3

        self.speedup_scale = 1.1

        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """init settings that change throughout the game"""
        self.submarine_speed = 1.5
        self.torpedo_speed = 1.5
        self.fish_speed = 1.0
        self.school_direction = 1 
        self.fish_points = 50

    def increase_speed(self):
        """increase speed settings"""
        self.submarine_speed *= self.speedup_scale
        self.torpedo_speed *= self.speedup_scale
        self.fish_speed *= self.speedup_scale
        self.fish_points = int(self.fish_points * self.score_scale)
        print(self.fish_points)