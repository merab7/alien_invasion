class Settings () :
    # A class to store all settings for Alien Invasion

    def __init__(self) -> None:
        pass
        #initialising game settings
        self.ship_speed_factor = 1.5
        self.screen_width = 1500
        self.screen_heigth = 900
        self.bg_color = (230, 230, 230)
        #bulet setting
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60