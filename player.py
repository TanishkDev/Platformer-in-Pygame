import pygame
from support import import_cut_graphics
from setting import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.animations = {"idle": import_cut_graphics(
            "/home/tanishk/Desktop/Pygame/Platformer/game_data/images/Character/Idle.png"),
            "death": import_cut_graphics(
                "/home/tanishk/Desktop/Pygame/Platformer/game_data/images/Character/Proto-Death.png"),
            "jump": import_cut_graphics(
                "/home/tanishk/Desktop/Pygame/Platformer/game_data/images/Character/Proto-jump.png"),
            "run": import_cut_graphics(
                "/home/tanishk/Desktop/Pygame/Platformer/game_data/images/Character/Proto-run.png")}

        self.speed = 5
        self.frame_index = 0
        self.animation_speed = 0.15
        self.gravity = 0.8
        self.jump_speed = -16
        self.status = "idle"

        self.on_right = True
        self.on_left = False
        self.on_ground = True

        self.image = self.animations["idle"][self.frame_index]
        self.scale_img()
        self.rect = self.image.get_rect(topleft=(pos))
        self.direction = pygame.math.Vector2(0, 0)

    def scale_img(self):
        self.image = pygame.transform.scale(self.image, (49, 98))

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.on_right = True
            self.direction.x = 1


        elif keys[pygame.K_LEFT]:
            self.on_right = False
            self.direction.x = -1

        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            self.on_ground = False
            self.jump()

    def animate_player(self):
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index > len(animation):
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]

        self.scale_img()

    def get_status(self):
        if self.direction.y < 0:
            self.status = "jump"
        else:
            if self.direction.x != 0:
                self.status = 'run'
            else:
                self.status = "idle"

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y -= 2
        self.rect.y += self.direction.y

    def update(self):
        self.get_input()
        self.apply_gravity()
        self.get_status()
        self.animate_player()
        self.rect.x += self.direction.x * self.speed
