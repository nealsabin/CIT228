import pygame.font
from pygame.sprite import Group

from submarine import Submarine

class Scoreboard:
    """a class to report scoring information"""
    def __init__(self, ai_game):
        """Init scorekeeping attr"""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_submarines()

    def prep_score(self):
        """turn the score into a rendered image"""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True,self.text_color, self.settings.bg_color)
        
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """draw score to the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.submarines.draw(self.screen)

    def prep_high_score(self):
        """turn the high score into a rendered image"""
        high_score = round(self.stats.high_score,-1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,self.text_color, self.settings.bg_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centery = self.screen_rect.centery
        self.high_score_rect.right = self.score_rect.right

    def check_high_score(self):
        """check to see if there's a new high score"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        """turn the level into a rendered image"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_submarines(self):
        """show how many submarines are left"""
        self.submarines = Group()
        for submarine_number in range(self.stats.submarines_left):
            submarine = Submarine(self.ai_game)
            submarine.rect.x = 780 + submarine_number * submarine.rect.width
            submarine.rect.y = 650
            self.submarines.add(submarine)