import pygame
from support import import_cut_graphics
from setting import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.player_idle_img = import_cut_graphics(
            "/home/tanishk/Desktop/Pygame/Platformer/game_data/images/Character/Idle.png")
        self.player_death_img = import_cut_graphics(
            "/home/tanishk/Desktop/Pygame/Platformer/game_data/images/Character/Proto-Death.png")
        self.player_jump_img = import_cut_graphics(
            "/home/tanishk/Desktop/Pygame/Platformer/game_data/images/Character/Proto-jump.png")
        self.player_run_img = import_cut_graphics(
            "/home/tanishk/Desktop/Pygame/Platformer/game_data/images/Character/Proto-run.png")

        self.speed = 5
        self.frame_index = 0
        self.gravity = 0.8
        self.jump_speed = -16

        self.image = self.player_idle_img[self.frame_index]
        self.scale_img()

        self.rect = self.image.get_rect(topleft=(pos))
        self.direction = pygame.math.Vector2(0, 0)

    def scale_img(self):
        self.image = pygame.transform.scale(self.image, (49, 98))

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1

        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            self.jump()
     
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y -= 2
        self.rect.y += self.direction.y

    def update(self):
        self.get_input()    
        self.apply_gravity()
        self.rect.x += self.direction.x * self.speed
