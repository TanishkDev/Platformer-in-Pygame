import pygame
from support import import_cut_graphics, import_folder
from setting import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, surface,create_jump_particles):
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
        self.jump_speed = -20
        self.status = "idle"
        self.dust_frame_index = 0
        self.dust_animation_speed = 0.4
        self.display_surface = surface
        self.create_jump_particles = create_jump_particles

        self.on_right = True
        self.on_left = False
        self.on_ground = False

        self.image = self.animations["idle"][self.frame_index]
        self.scale_img()
        self.rect = self.image.get_rect(topleft=(pos))
        self.direction = pygame.math.Vector2(0, 0)

        self.import_dust_animation()

    def scale_img(self):
        self.image = pygame.transform.scale(self.image, (49, 98))

    def import_dust_animation(self):
        self.dust_run_particles = import_folder("game_data/images/Character/dust/run")

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.on_right, self.on_left = True, False
            self.direction.x = 1


        elif keys[pygame.K_LEFT]:
            self.on_right = False
            self.on_left = True
            self.direction.x = -1

        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE] and self.on_ground:
            self.create_jump_particles(self.rect.midbottom)

            self.jump()


    def animate_player(self):
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index > len(animation):
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]

        if self.on_left:
            self.image = pygame.transform.flip(self.image, True, False)

        self.scale_img()

    def get_status(self):
        if self.direction.y < 0:
            self.status = "jump"

        else:
            if self.direction.x != 0:
                self.status = 'run'
            else:
                self.status = "idle"

    def run_particle(self):
        if self.status == "run" and self.on_ground:
            self.dust_frame_index += self.animation_speed
            if self.dust_frame_index >= len(self.dust_run_particles):
                self.dust_frame_index = 0

            dust_particles = self.dust_run_particles[int(self.dust_frame_index)]

            if self.on_right:
                pos = self.rect.bottomleft - pygame.math.Vector2(6, 10)
                self.display_surface.blit(dust_particles,pos)


            else:
                pos = self.rect.bottomright - pygame.math.Vector2(6, 10)
                flipped_dust_particles = pygame.transform.flip(dust_particles, True, False)
                self.display_surface.blit(flipped_dust_particles,pos)


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
        self.run_particle()

        self.rect.x += self.direction.x * self.speed
