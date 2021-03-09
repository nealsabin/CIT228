import pygame

from pygame.sprite import Sprite

class Submarine(Sprite):
    """class to manage the sub"""

    def __init__(self, ai_game):
        """Init the sub and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('project_game_final/images/submarine.png')
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft

        self.y = float(self.rect.y)

        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the subs position based on the movement flag"""
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.submarine_speed
        if self.moving_down and self.rect.bottom < 700:
            self.y += self.settings.submarine_speed

        #update rect object from self.x
        self.rect.y = self.y

    def blitme(self):
        """draw the sub at its current location"""
        self.screen.blit(self.image, self.rect)

    def center_submarine(self):
        """center the sub on the screen"""
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)