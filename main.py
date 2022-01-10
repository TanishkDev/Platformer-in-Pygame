import pygame, sys
from level import Level
from setting import *

pygame.init()

class Game:
    def __init__(self):
        level = Level(screen)
        level.run()


screen = pygame.display.set_mode((screen_width, screen_width))

game = Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
