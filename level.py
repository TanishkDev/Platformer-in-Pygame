import pygame
from setting import tile_size
from support import import_csv_layout
from game_data import level_0
from setting import tile_size
from tiles import Tile

class Level:
    def __init__(self,surface):
        self.surface = surface
        self.world_shift = -5

        terrain_layout = import_csv_layout(level_0["terrain"])
        self.terrain = self.create_tile_group(terrain_layout,'terrain')
        print(terrain_layout)

    def create_tile_group(self,layout,type):
        sprite_group = pygame.sprite.Group()

        for row_index,row in enumerate(layout):
            for col_index,val in enumerate(row):
                x = tile_size * col_index
                y = tile_size * row_index
                if val != -1:
                    if type=="terrain":
                        sprite = Tile(tile_size,x,y)
        
                    sprite_group.add(sprite)
    
        return sprite_group
        
    def run(self):
        self.terrain.update(self.world_shift)
        self.terrain.draw(self.surface)
