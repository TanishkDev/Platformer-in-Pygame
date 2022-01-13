import pygame
from setting import tile_size
from support import import_csv_layout,import_cut_graphics
from game_data import level_0
from setting import *
from tiles import Tile,StaticTile


class Level:
    def __init__(self, surface):
        self.surface = surface
        self.world_shift = -5
        self.sprite_surface_list = import_cut_graphics()

        terrain_layout = import_csv_layout(level_0["terrain"])
        self.terrain = self.create_tile_group(terrain_layout, 'terrain')

    def create_tile_group(self, layout, type):
        sprite_group = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                if val != '-1':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    if type == "terrain":
                        terrain_tile = int(val)
                        sprite = StaticTile(tile_size,x,y,self.sprite_surface_list[terrain_tile])

                    sprite_group.add(sprite)
        return sprite_group

    def run(self):
        # Terrain
        self.terrain.draw(self.surface)
        self.terrain.update(self.world_shift)

#