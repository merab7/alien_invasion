import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    #initialize game and create a screen object.
    pygame.init()
    #set the background color
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_heigth))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in.
    bullets = Group()
    #start the main loop for the game
    while True :
            gf.check_events(ship, ai_settings, screen, bullets) 
            ship.update() 
            gf.update_screen(ai_settings, screen, ship, bullets)
            
            
run_game()