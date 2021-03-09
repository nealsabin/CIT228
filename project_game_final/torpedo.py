import pygame
from pygame.sprite import Sprite

class Torpedo(Sprite):
    """A class to manage torpedoes fired from the ship"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.torpedo_color
        
        #create a torpedo rect at (0,0) and then set correct position
        self.rect = pygame.Rect(0,0, self.settings.torpedo_width, self.settings.torpedo_height)
        self.rect.midright = ai_game.submarine.rect.midright

        self.x = float(self.rect.x)
    
    def update(self):
        """Move the torpedo up the screen"""
        self.x +=self.settings.torpedo_speed
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the torpedo to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)