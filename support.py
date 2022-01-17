from csv import reader
import pygame.image
from setting import *



#Imports Tile map form CSV file and return it as a list
def import_csv_layout(path):
    tile_map = []
    with open(path, 'r') as map:
        level = reader(map, delimiter=",")
        for row in level:
            tile_map.append(list(row))
    return tile_map


# Cuts the image in spritesheet
def import_cut_graphics(path=sprite_sheet_path):
    surface = pygame.image.load(path).convert_alpha()
    tile_num_x = surface.get_size()[0] // sprite_sheet_size
    tile_num_y = surface.get_size()[1] // sprite_sheet_size

    cut_tiles = []
    for row in range(tile_num_y):
        for col in range(tile_num_x):
            x = col * sprite_sheet_size #cordinate for image
            y = row * sprite_sheet_size #coordinate for image
            new_surf = pygame.Surface((sprite_sheet_size, sprite_sheet_size), flags=pygame.SRCALPHA)#creating a image
            new_surf.blit(surface, (0, 0), pygame.Rect(x, y, sprite_sheet_size, sprite_sheet_size))
            cut_tiles.append(new_surf)

    return cut_tiles


