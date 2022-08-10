import pygame


class Ship:
    """Class to manage the ship"""

    def __init__(self, ai_game):
        """Initialise the ship"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship and get its dimensions
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start at the bottom centre of screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Draw ship at current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the ships position based on movement flag"""

        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1
