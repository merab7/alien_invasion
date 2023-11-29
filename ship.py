import pygame

class Ship () :

    def __init__(self, screen) -> None:
        pass
     #initialising the ship and set its starting position

        self.screen = screen

        #load the ship and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        # new sizes for the ship
        self.new_size = (100,100)
         # Resize the image
        self.image = pygame.transform.scale(self.image, self.new_size)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #start each new ship at the bootom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        #movment flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
    def update(self):
        if self.moving_right :
         self.rect.centerx += 1
        if self.moving_left :
         self.rect.centerx -= 1  
        if self.moving_up :
           self.rect.centery += 1
        if self.moving_down :
           self.rect.centery -= 1 

    def blitme(self) :

            #draw the ship at its current location
            self.screen.blit(self.image, self.rect)