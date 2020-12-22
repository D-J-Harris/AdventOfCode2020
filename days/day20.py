"""Jurassic Jigsaw"""
from collections import defaultdict
import numpy as np
import regex as re


def get_side(tile, side):
    if side == 'top':
        return ''.join(str(x) for x in tile[0])
    if side == 'bottom':
        return ''.join(str(x) for x in tile[-1])
    if side == 'left':
        return ''.join(str(x[0]) for x in tile)
    if side == 'right':
        return ''.join(str(x[-1]) for x in tile)


with open('../inputs/day20.txt', 'r') as f:
    tiles = {}
    for block in f.read().split('\n\n'):
        lines = block.split('\n')
        tile_id = int(lines[0][5:-1])
        tile = np.array([x for x in lines[1]])
        for line in lines[2:]:
            tile = np.concatenate((tile, np.array([x for x in line])))
        tile = tile.reshape(int(np.sqrt(len(tile))), -1)
        tile = np.where(tile == '#', 1, 0)
        tiles[tile_id] = tile
rows = int(np.sqrt(len(tiles)))
tile_width = len(next(iter(tiles.values()))) - 2

# find side options
options = defaultdict(lambda: defaultdict(list))
side_names = ('bottom', 'left', 'top', 'right')
for tile_id, tile in tiles.items():
    for tile_id_other, tile_other in tiles.items():
        for side_name in side_names:
            for side_name_other in side_names:
                if tile_id != tile_id_other and \
                        get_side(tile, side_name) == get_side(tile_other, side_name_other):
                    options[tile_id][side_name].append(int(tile_id_other))
                if tile_id != tile_id_other and \
                        get_side(tile, side_name)[::-1] == get_side(tile_other, side_name_other):
                    options[tile_id][side_name].append(int(tile_id_other))

# find part 1 answer
ans, corner_tile_ids = 1, []
for tile_id, sides in options.items():
    num_sides = sum([len(x) for x in sides.values()])
    if num_sides == 2:
        corner_tile_ids.append(tile_id)
        ans *= tile_id
print(f'answer to puzzle 1 is {ans}')


def transform(tile):
    transformations = []
    for rep in (0, 1, 2, 3):
        transformations.append(np.rot90(tile.copy(), rep))
        tile_ud = np.flipud(tile.copy())
        transformations.append(np.rot90(tile_ud.copy(), rep))
        tile_lr = np.fliplr(tile.copy())
        transformations.append(np.rot90(tile_lr.copy(), rep))
    return transformations


def create_grid(start_tile_id, start_tile):
    grid = np.zeros(shape=(rows * tile_width, rows * tile_width))
    placed_tile_ids = []

    top_tile = start_tile.copy()
    top_tile_id = start_tile_id
    current_tile = start_tile.copy()
    for col_num in range(rows):
        grid[0:tile_width, tile_width*col_num:(tile_width*col_num+tile_width)] = top_tile[1:-1, 1:-1].copy()
        placed_tile_ids.append(top_tile_id)
        for row_num in range(1, rows):
            found = False
            for tile_id, tile, in tiles.items():
                if tile_id not in placed_tile_ids:
                    tile = tiles[tile_id]
                    for t in transform(tile):
                        if get_side(t, 'top') == get_side(current_tile, 'bottom'):
                            grid[tile_width*row_num:(tile_width*row_num+tile_width), tile_width*col_num:(tile_width*col_num+tile_width)] = t[1:-1, 1:-1].copy()
                            placed_tile_ids.append(tile_id)
                            current_tile = t.copy()
                            found = True
                        if found:
                            break
                    if found:
                        break
            if not found:
                raise Exception("configuration not suitable")
        if col_num < rows - 1:
            found = False
            for tile_id, tile, in tiles.items():
                if tile_id not in placed_tile_ids:
                    tile = tiles[tile_id]
                    for t in transform(tile):
                        if get_side(t, 'left') == get_side(top_tile, 'right'):
                            top_tile = t.copy()
                            top_tile_id = tile_id
                            current_tile = t.copy()
                            found = True
                        if found:
                            break
                    if found:
                        break
            if not found:
                raise Exception("configuration not suitable")
    return grid


def get_grid():
    for tile_id in corner_tile_ids:
        tile = tiles[tile_id]
        for transform_tile in transform(tile):
            try:
                grid = create_grid(tile_id, transform_tile)
                return grid
            except:
                print("error with initial configuration, trying a different one")
    raise Exception("something has gone horribly wrong")


monster_width = 20
monster = f"(.{{{(rows*tile_width)-monster_width}}})".join(['..................1.',
                                                            '1....11....11....111',
                                                            '.1..1..1..1..1..1...'])
count, grid = 0, get_grid()
for grid_t in transform(grid):
    flat_grid = ''.join([''.join([str(int(e)) for e in g]) for g in grid_t])
    c = len(re.findall(monster, flat_grid, overlapped=True))
    count += c
print(f"answer to puzzle 2 is {np.sum(grid == 1) - 15*count}")
