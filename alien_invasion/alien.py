import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien"""

    def __init__(self, ai_game):
        """Initialise alien"""

        super().__init__()
        self.screen = ai_game.screen

        # Load alien and set attributes
        self.image = pygame.image.load('images/alien_pink.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store aliens exact horizontal position
        self.x = float(self.rect.x)
