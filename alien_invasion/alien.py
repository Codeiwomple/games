import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien"""

    def __init__(self, ai_game):
        """Initialise alien"""

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load alien and set attributes
        self.image = pygame.image.load('images/alien_pink.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store aliens exact horizontal position
        self.x = float(self.rect.x)

    def update(self):
        """Move aliens right"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Check if aliens have reached end of screen"""
        screen_rect = self.screen.get_rect()

        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
