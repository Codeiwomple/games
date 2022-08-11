import pygame


class Ship:
    """Class to manage the ship"""

    def __init__(self, ai_game):
        """Initialise the ship"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship and get its dimensions
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start at the bottom centre of screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Decimal value for ships x axis position
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Draw ship at current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the ships position based on movement flag"""

        # Calculate ships new position
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update the ships position
        self.rect.x = self.x
