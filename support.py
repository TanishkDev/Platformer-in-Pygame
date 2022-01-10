from game_data import level_0
from csv import reader


def import_csv_layout(path):
    terrain_map = []
    with open(path) as map:
        level_0 = reader(map, delimiter=',')
        for row in level_0:
            terrain_map.append(list(row))
        return terrain_map
