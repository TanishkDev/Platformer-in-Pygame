import pygame, sys
from level import Level
from setting import *

pygame.init()

class Game:
    def __init__(self):
        self.level = Level(screen) # Initialising Level 

    def run(self):
        screen.blit(background,(0,0))
        self.level.run()


screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock() 
background = pygame.image.load("/home/tanishk/Desktop/Pygame/Platformer/game_data/images/SpriteSheets/background.png").convert_alpha()
background = pygame.transform.scale(background,(screen_width,screen_height))

game = Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    game.run()
    clock.tick(60)#FPS
    pygame.display.update()


