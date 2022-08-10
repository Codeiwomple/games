import sys
import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """Class to manage game assets and behaviour"""

    def __init__(self):
        """Initialise the game and create resources"""

        pygame.init()

        # Apply settings from settings file
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        # Create ship
        self.ship = Ship(self)

    def run_game(self):
        """Main loop for the game"""

        while True:
            # Respond to user input
            self._check_events()
            # Update ship position and display
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        """Watch for keyboard and mouse events"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Move ship right
                    self.ship.moving_right = True
                if event.key == pygame.K_LEFT:
                    # Move ship left
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    # Stop moving
                    self.ship.moving_right = False
                if event.key == pygame.K_LEFT:
                    # Stop moving
                    self.ship.moving_left = False

    def _update_screen(self):
        """Buffer new screen and draw it"""

        # Buffer screen
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Update screen to most recent
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
