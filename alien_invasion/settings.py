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
