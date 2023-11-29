import sys
import pygame

def check_events(ship) :
    #respond to keypress and mouse events
    for event in pygame.event.get():
        movong_right = True
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False        

                              
        


def update_screen (ai_settings, screen, ship) : 

     #redrow the screen during each pass through the loop
            screen.fill(ai_settings.bg_color)
            ship.blitme()
            #Make the most recently drown screen visible
            pygame.display.flip()          