import pygame
from pygame.sprite import Sprite

class Fish(Sprite):
    """A class to represent a single fish in the school"""

    def __init__(self, ai_game):
        """Init the fish and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = self.screen.get_rect()

        #load the fish image and set its rect attr
        self.image = pygame.image.load('project_game_final/images/fish.png')
        self.image = pygame.transform.scale(self.image,(40,40))
        self.rect = self.image.get_rect()

        self.rect.x = 950 - self.rect.width
        self.rect.y = self.rect.height

        self.y = float(self.rect.y)

    def check_edges(self):
        """retrun True if fish is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.top <= screen_rect.top or self.rect.bottom >= screen_rect.bottom:
            return True

    def update(self):
        """Move the fish to the up"""
        self.y += (self.settings.fish_speed * self.settings.school_direction)
        self.rect.y = self.y