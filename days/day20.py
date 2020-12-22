"""Jurassic Jigsaw"""
from collections import defaultdict
import numpy as np
import re


def get_side(tile, side):
    if side == 'top':
        return ''.join(str(x) for x in tile[0])
    if side == 'bottom':
        return ''.join(str(x) for x in tile[-1])
    if side == 'left':
        return ''.join(str(x[0]) for x in tile)
    if side == 'right':
        return ''.join(str(x[-1]) for x in tile)


with open('../inputs/test.txt', 'r') as f:
    tile_sides = {}
    tiles = {}
    for block in f.read().split('\n\n'):
        sides = {}
        lines = block.split('\n')
        tile_id = int(lines[0][5:-1])
        tile = np.array([x for x in lines[1]])
        for line in lines[2:]:
            tile = np.concatenate((tile, np.array([x for x in line])))
        tile = tile.reshape(int(np.sqrt(len(tile))), -1)
        tile = np.where(tile == '#', 1, 0)
        sides['top'] = get_side(tile, 'top')
        sides['bottom'] = get_side(tile, 'bottom')
        sides['left'] = get_side(tile, 'left')
        sides['right'] = get_side(tile, 'right')
        tile_sides[tile_id] = sides
        tiles[tile_id] = tile

# find side options
options = defaultdict(lambda: defaultdict(list))
side_names = ('bottom', 'left', 'top', 'right')
for tile_id, sides in tile_sides.items():
    for side, pattern in sides.items():
        for tile_id_other, sides_other in tile_sides.items():
            for side_name in side_names:
                if tile_id != tile_id_other and pattern == sides_other[side_name]:
                    options[tile_id][side].append([int(tile_id_other), side_name])
                if tile_id != tile_id_other and pattern[::-1] == sides_other[side_name]:
                    options[tile_id][side].append([int(tile_id_other), side_name])

# find part 1 answer
ans = 1
corner_tile_ids = []
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


# create grid
def get_grid(start_tile_id, start_tile):
    rows = int(np.sqrt(len(tiles)))
    tile_width = len(next(iter(tiles.values()))) - 2
    grid = np.zeros(shape=(rows * tile_width, rows * tile_width))
    grid_ids = np.zeros(shape=(rows, rows))
    placed_tile_ids = []

    top_tile = start_tile.copy()
    top_tile_id = start_tile_id
    current_tile = start_tile.copy()
    current_tile_id = start_tile_id
    print('heya im here',get_side(current_tile, 'bottom'))
    print(current_tile_id)
    for col_num in range(rows):
        print(col_num, top_tile_id)
        grid[0:tile_width, tile_width*col_num:(tile_width*col_num+tile_width)] = top_tile[1:-1, 1:-1].copy()
        grid_ids[0, col_num] = int(top_tile_id)
        print(grid_ids)
        placed_tile_ids.append(top_tile_id)
        for row_num in range(1, rows):
            print('enter here')
            print('testing against', current_tile_id)
            found = False
            for tile_id, tile, in tiles.items():
                if tile_id not in placed_tile_ids:
                    tile = tiles[tile_id]
                    print('attempt', tile_id)
                    for t in transform(tile):
                        if get_side(t, 'top') == get_side(current_tile, 'bottom'):
                            print('b',tile_id)
                            grid[tile_width*row_num:(tile_width*row_num+tile_width), tile_width*col_num:(tile_width*col_num+tile_width)] = t[1:-1, 1:-1].copy()
                            print('a',tile_id)
                            grid_ids[row_num, col_num] = int(tile_id)
                            print(grid_ids)
                            placed_tile_ids.append(tile_id)
                            current_tile = t.copy()
                            current_tile_id = tile_id
                            found = True
                        if found:
                            break
                    if found:
                        break
            if not found:
                print("error finding a bottom tile")
                raise Exception("configuration not suitable")
        print('time to move')
        if col_num < rows - 1:
            found = False
            for tile_id, tile, in tiles.items():
                if tile_id not in placed_tile_ids:
                    tile = tiles[tile_id]
                    for t in transform(tile):
                        if get_side(t, 'left') == get_side(top_tile, 'right'):
                            print('b', tile_id)
                            print('width',tile_width)
                            #grid[0:tile_width, tile_width*col_num:(tile_width*col_num + tile_width)] = t[1:-1, 1:-1]
                            print('a', tile_id)
                            #grid_ids[0, col_num] = int(tile_id)
                            print(grid_ids)
                            #placed_tile_ids.append(tile_id)
                            top_tile = t.copy()
                            top_tile_id = tile_id
                            current_tile = t.copy()
                            current_tile_id = tile_id
                            found = True
                        if found:
                            break
                    if found:
                        break
            if not found:
                print("error finding an adjacent tile")
                raise Exception("configuration not suitable")
    print(grid_ids)
    return grid


grid = None
for tile_id in corner_tile_ids:
    print(tile_id)
    tile = tiles[tile_id]
    for transform_tile in transform(tile):
        try:
            grid = get_grid(tile_id, transform_tile)
            print(grid)
            break
        except:
            print("error with initial configuration, trying a different one")
    else:
        break


rows = int(np.sqrt(len(tiles)))
tile_width = len(next(iter(tiles.values()))) - 2
monster_width = 20
monster = f"(.{{{(rows*tile_width)-monster_width}}})".join(['..................1.',
                                                            '1....11....11....111',
                                                            '.1..1..1..1..1..1...'])

print(monster)
count = 0
for grid_t in transform(grid):
    print('hmm')
    flat_grid = ''.join([''.join([str(int(e)) for e in g]) for g in grid_t])
    print(flat_grid)
    m = len(re.findall(monster, flat_grid))
    count += m
    print(m)
print(count)
print(f"answer to puzzle 2 is {np.sum(grid == 1) - 15*count}")

