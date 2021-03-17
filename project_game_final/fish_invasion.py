import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from submarine import Submarine
from torpedo import Torpedo
from fish import Fish


class FishInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Fish Invasion")

        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.submarine = Submarine(self)
        self.torpedoes = pygame.sprite.Group()
        self.fishes = pygame.sprite.Group()

        self._create_school()

        self.play_button = Button(self, "Play")

        self.screen.fill(self.settings.bg_color)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.submarine.update()
                self._update_torpedoes()
                self._update_fishes()

            self.__update_screen()

            """Most recently drawn screen visible"""
            pygame.display.flip()

    def _check_events(self):
        """repind to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_play_button(self, mouse_pos):
        """start a new game when the player clicks 'Play'"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_submarines()
            pygame.mouse.set_visible(False)

            self.fishes.empty()
            self.torpedoes.empty()

            self._create_school()
            self.settings.increase_speed()
            self.submarine.center_submarine()  

    def _check_keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.submarine.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.submarine.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_torpedo()
    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.submarine.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.submarine.moving_down = False

    def _fire_torpedo(self):
        """Create a new bullet and add it to the torpedoes group"""
        if len(self.torpedoes) < self.settings.torpedoes_allowed:
            new_torpedo = Torpedo(self)
            self.torpedoes.add(new_torpedo)

    def _update_torpedoes(self):
        """Update position of torpedoes and get rid of old torpedoes"""
        self.torpedoes.update()
        screen_rect = self.screen.get_rect()

        for torpedo in self.torpedoes.copy():
            if torpedo.rect.left >= screen_rect.right:
                self.torpedoes.remove(torpedo)
            print(len(self.torpedoes))   

        self._check_torpedo_fish_collisions()

    def _check_torpedo_fish_collisions(self):
        """respond to bullet-fish collisions"""
        collisions = pygame.sprite.groupcollide(self.torpedoes,self.fishes, True,True)

        if collisions:
            for fishes in collisions.values():
                self.stats.score += self.settings.fish_points * len(fishes)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.fishes:
            self.torpedoes.empty()
            self._create_school()
            self.settings.increase_speed()
            self.stats.level += 1
            self.sb.prep_level()

    def _update_fishes(self):
        """update the positions of all fish in the school"""
        self._check_school_edges()
        self.fishes.update()
        self._check_fishes_left()

        if pygame.sprite.spritecollideany(self.submarine, self.fishes):
            print("Submarine hit!")

    def _check_fishes_left(self):
        """check if any fishes have reached the left of the screen"""
        screen_rect = self.screen.get_rect()
        for fish in self.fishes.sprites():
            if fish.rect.left <= screen_rect.left:
                self._submarine_hit()
                break

    def _submarine_hit(self):
        """respond to the submarine being hit by an fish"""
        if self.stats.submarines_left > 0:
            self.stats.submarines_left -= 1
            self.sb.prep_submarines()
            self.fishes.empty()
            self.torpedoes.empty()
            self._create_school()
            self.submarine.center_submarine()
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _create_school(self):
        """create the school"""
        fish = Fish(self)
        self.fishes.add(fish)

        fish_height, fish_width = fish.rect.size
        available_space_y = self.settings.screen_height - (2 * fish_height)
        number_fish_y = available_space_y // (2 * fish_height)

        #num of columns
        submarine_width = self.submarine.rect.width
        available_space_x = (self.settings.screen_width - (3 * fish_width) - (3 * submarine_width))
        number_columns = available_space_x // (3 * fish_width)

        for column_number in range(number_columns):
            for fish_number in range(number_fish_y):
                self._create_fish(fish_number, column_number)

    def _create_fish(self, fish_number, column_number):
        """create an fish and place it in the row"""
        fish = Fish(self)
        fish_width, fish_height = fish.rect.size

        fish.y = fish_height + 2 * fish_height * fish_number
        fish.rect.y = fish.y

        fish.rect.x = (fish.rect.width + 390) + 3 * fish.rect.width * column_number

        self.fishes.add(fish)

    def _check_school_edges(self):
        """Respond appropriately if any values have reached an edge"""
        for fish in self.fishes.sprites():
            if fish.check_edges():
                self._change_school_direction()
                break
    
    def _change_school_direction(self):
        """drop the entire school and change the school's direction"""
        for fish in self.fishes.sprites():
            fish.rect.x -= self.settings.school_drop_speed
        self.settings.school_direction *= -1

    def __update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.submarine.blitme()
        for bullet in self.torpedoes.sprites():
            bullet.draw_bullet()
        self.fishes.draw(self.screen)

        self.sb.show_score()

        #draw the play button if the game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()
        
if __name__ == '__main__':
    ai = FishInvasion()
    ai.run_game()