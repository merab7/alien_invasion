import pygame

class Ship () :

    def __init__(self, ai_settings, screen) -> None:
        pass
     #initialising the ship and set its starting position

        self.screen = screen
        self.ai_settings = ai_settings
        #load the ship and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        # new sizes for the ship
        self.new_size = (100,100)
         # Resize the image
        self.image = pygame.transform.scale(self.image, self.new_size)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #start each new ship at the center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        # Store a decimal value for the ship's center.
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        #movment flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
    def update(self):
         # Controlling moving right and left
            if self.moving_right and self.rect.right < self.screen_rect.right:
               self.centerx += self.ai_settings.ship_speed_factor
            if self.moving_left and self.rect.left > 0:
               self.centerx -= self.ai_settings.ship_speed_factor
            
            # Controlling moving up and down
            if self.moving_up and self.rect.top > 0:
               self.centery -= self.ai_settings.ship_speed_factor
            if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
               self.centery += self.ai_settings.ship_speed_factor


            self.rect.centerx = self.centerx
            self.rect.centery = self.centery

    def blitme(self) :

            #draw the ship at its current location
            self.screen.blit(self.image, self.rect)