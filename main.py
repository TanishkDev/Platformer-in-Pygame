import pygame, sys
from level import Level

pygame.init()



game_width, game_height = 800, 600

screen = pygame.display.set_mode((game_width, game_height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
