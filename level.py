import pygame
from setting import tile_size
from support import import_csv_layout, import_cut_graphics
from game_data import level_0
from setting import *
from tiles import StaticTile
from player import Player


class Level:
    def __init__(self, surface):
        self.surface = surface

        self.world_shift = 0  # world shift value
        self.sprite_surface_list = import_cut_graphics()  # importing sprite surfaces
        self.coin_surf = pygame.image.load("game_data/images/SpriteSheets/coin.png").convert_alpha()

        # Player
        self.player = pygame.sprite.GroupSingle()
        player_sprite = Player((100, 100))
        self.player.add(player_sprite)

        # terrain
        terrain_layout = import_csv_layout(level_0["terrain"])  # layout
        self.terrain = self.create_tile_group(terrain_layout, 'terrain')

        # grass
        grass_layout = import_csv_layout(level_0["grass"])
        self.grass = self.create_tile_group(grass_layout, "grass")

        # water
        water_layout = import_csv_layout(level_0["water"])
        self.water = self.create_tile_group(water_layout, "water")

        # coin
        coin_layout = import_csv_layout(level_0["coin"])
        self.coin = self.create_tile_group(coin_layout, "coin")

    # Creates Tile Group
    def create_tile_group(self, layout, type):
        sprite_group = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                if val != '-1':
                    x = col_index * tile_size  # x value of tile
                    y = row_index * tile_size  # y value of tile

                    if type == "terrain":
                        terrain_tile = int(val)
                        sprite = StaticTile(tile_size, x, y,
                                            self.sprite_surface_list[terrain_tile])  # Creating a tile sprite

                    if type == "grass":
                        grass_tile = int(val)
                        sprite = StaticTile(tile_size, x, y, self.sprite_surface_list[grass_tile])

                    if type == "water":
                        water_tile = int(val)
                        sprite = StaticTile(tile_size, x, y, self.sprite_surface_list[water_tile])

                    if type == "coin":
                        sprite = StaticTile(tile_size, x, y, self.coin_surf)

                    sprite_group.add(sprite)

        return sprite_group

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screen_width // 3 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif (player_x > screen_width - (screen_width // 3)) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.terrain.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.terrain.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

    def run(self):
        # Terrain
        self.terrain.update(self.world_shift)
        self.terrain.draw(self.surface)

        # Grass
        self.grass.update(self.world_shift)
        self.grass.draw(self.surface)

        # Coin
        self.coin.update(self.world_shift)
        self.coin.draw(self.surface)

        # water
        self.water.update(self.world_shift)
        self.water.draw(self.surface)

        # Player
        self.player.update()
        self.vertical_movement_collision()
        self.horizontal_movement_collision()
        self.player.draw(self.surface)
        self.scroll_x()
