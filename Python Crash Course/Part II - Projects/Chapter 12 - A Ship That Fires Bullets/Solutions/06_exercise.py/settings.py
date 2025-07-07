# Creatting a Settings Class
class Settings:
    """A class to store all settings for Pygame."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = ("#000000")

        # Ship settings
        self.ship_speed = 5.0

        # Bullet settings
        self.bullet_speed = 5
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = ("#FFFFFF")
        self.bullets_allowed = 5