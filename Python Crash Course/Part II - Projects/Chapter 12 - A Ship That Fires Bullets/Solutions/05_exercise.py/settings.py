# Creatting a Settings Class
class Settings:
    """A class to store all settings for Pygame."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 500
        self.screen_height = 500
        self.bg_color = ("#004aad")

        # Ship settings
        self.ship_speed = 2.5