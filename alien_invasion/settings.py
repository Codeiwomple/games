class Settings:
    """A class to store the settings for Alien Invasion"""

    def __init__(self):
        """Initialise game settings"""

        # Screen/ display settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 57, 70)  # Solarized Dark

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (181, 137, 2)  # Mustard Yellow
        self.bullets_allowed = 3
