import sys
import pygame
from bullet import Bullet



def check_events(ai_settings, screen, ship, bullets) :
    #respond to keypress and mouse events
    for event in pygame.event.get():
      
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
            elif event.key == pygame.K_UP:
                ship.moving_up = True
            elif event.key == pygame.K_DOWN:
                ship.moving_down = True
            elif event.key == pygame.K_SPACE:
                # Create a new bullet and add it to the bullets group.
                new_bullet = Bullet(ai_settings, screen, ship)
                bullets.add(new_bullet)    

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False
            elif event.key == pygame.K_UP:
                ship.moving_up = False
            elif event.key == pygame.K_DOWN:
                ship.moving_down = False
  
                              
        


def update_screen (ai_settings, screen, ship, bullets) : 

     #redrow the screen during each pass through the loop
            screen.fill(ai_settings.bg_color)
            for bullet in bullets.sprites():
                 bullet.draw_bullet()
            ship.blitme()
            #Make the most recently drown screen visible
            pygame.display.flip()          