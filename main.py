import pygame, sys
from level import Level
from setting import *

pygame.init()

class Game:
    def __init__(self):
        self.level = Level(screen)

    def run(self):
        screen.fill((255, 255, 255))
        self.level.run()


screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

game = Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    game.run()
    clock.tick(60)
    pygame.display.update()

