import sys
import pygame

from time import sleep

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats


class AlienInvasion:
    """Class to manage game assets and behaviour"""

    def __init__(self):
        """Initialise the game and create resources"""

        pygame.init()

        # Apply settings from settings file
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")

        self.stats = GameStats(self)

        # Create ship
        self.ship = Ship(self)

        # Create bullets and aliens groups
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_alien_fleet()

    def run_game(self):
        """Main loop for the game"""

        while True:
            # Respond to user input
            self._check_events()

            if self.stats.game_active:
                # Update components and display
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    def _check_events(self):
        """Watch for keyboard and mouse events"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Key presses"""
        if event.key == pygame.K_RIGHT:
            # Move ship right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move ship left
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Key releases"""
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
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Update screen to most recent
        pygame.display.flip()

    def _fire_bullet(self):
        """Create new bullet and add to group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Create and remove bullets"""

        # Update position
        self.bullets.update()

        # Remove off screen bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        # Check for collisions and remove
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

    def _create_alien_fleet(self):
        """Create fleet of aliens"""
        alien = Alien(self)

        alien_width, alien_height = alien.rect.size
        # Available space on x axis of screen with a margin on either side
        available_space_x = self.settings.screen_width - (2 * alien_width)
        # Leave a gap of 1 aliend width
        number_aliens_x = available_space_x // (2 * alien_width)

        # Calculate number of rows that will fit on screen
        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - \
            (3 * alien_height) - ship_height
        number_rows = available_space_y // (2 * alien_height)

        # Create a row of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Create and place alien"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_aliens(self):
        """Update position of all aliens in fleet"""
        self._check_fleet_edges()
        self.aliens.update()

        # Check for ship collision and reaching bottom of screen
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        """Change alien direction when at edge of screen"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop fleet and change movement direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1  # Change direction/ sign

    def _ship_hit(self):
        """Respond to ship being hit by alien"""

        if self.stats.ships_left > 0:
            print("active")
            self.stats.ships_left -= 1
            print(self.stats.ships_left)

            self.aliens.empty()
            self.bullets.empty()

            self._create_alien_fleet()
            self.ship.center_ship()

            sleep(0.5)
        else:
            print("inactive")
            self.stats.game_active = False

    def _check_aliens_bottom(self):
        """Check aliens reach bottom of screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
