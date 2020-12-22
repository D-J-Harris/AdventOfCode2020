"""Jurassic Jigsaw"""
from collections import defaultdict
import numpy as np


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
                    options[tile_id][side].append([int(tile_id_other), side_name, True])
                if tile_id != tile_id_other and pattern[::-1] == sides_other[side_name]:
                    options[tile_id][side].append([int(tile_id_other), side_name, False])

# find part 1 answer
ans1 = 1
corner_tile_ids = []
for tile_id, sides in options.items():
    num_sides = sum([len(x) for x in sides.values()])
    if num_sides == 2:
        corner_tile_ids.append(tile_id)
        ans1 *= tile_id


def opposite_side(side):
    return side_names[(side_names.index(side) + 2) % 4]


# create grid
# need to check each of the possible flip states of the starting corner
# 0=normal, 1=flip_left_right, 2=flip_up_down, 3=flip_udlr
def get_grid(state, start_corner_id, edge=0):
    rows = int(np.sqrt(len(tiles)))
    grid = np.zeros(shape=(rows, rows, (10-2), (10-2)))
    grid_ids = np.zeros(shape=(rows, rows, 1, 1))
    completed_ids = []
    flip_lr = 1
    flip_lr_tmp = 1
    flip_ud = 1

    row_tile_id = start_corner_id
    row_tile = tiles[row_tile_id]
    row_side = list(options[row_tile_id].keys())[edge]
    if state == 1:
        row_tile = np.fliplr(row_tile)
        if row_side in ('left', 'right'):
            row_side = opposite_side(row_side)
        flip_lr = -1
        flip_lr_tmp = -1
    if state == 2:
        row_tile = np.flipud(row_tile)
        if row_side in ('top', 'bottom'):
            row_side = opposite_side(row_side)
        flip_ud = -1
    if state == 3:
        row_tile = np.fliplr(row_tile)
        row_tile = np.flipup(row_tile)
        row_side = opposite_side(row_side)
        flip_lr = -1
        flip_lr_tmp = -1
        flip_ud = -1
    # rotate to face downwards
    row_tile = np.rot90(row_tile, side_names.index(row_side))
    next_tile_id, received_side, matched = list(options[row_tile_id].values())[edge][0]
    next_tile = tiles[next_tile_id]
    if not matched:
        if received_side == 'right':
            next_tile = np.flipud(next_tile)
        if received_side == 'top':
            flip_lr_tmp = -1 * flip_lr
    else:
        if received_side == 'bottom':
            flip_lr_tmp = -1 * flip_lr
        if received_side == 'left':
            next_tile = np.flipud(next_tile)
    if flip_lr_tmp == -1:
        next_tile = np.fliplr(next_tile)
    next_tile = np.rot90(next_tile, 2 + side_names.index(received_side))
    for col_num in range(rows):
        grid[0][col_num] = row_tile[1:-1, 1:-1]
        grid_ids[0][col_num] = int(row_tile_id)
        completed_ids.append(row_tile_id)
        for row_num in range(1, rows - 1):
            grid[row_num][col_num] = next_tile[1:-1, 1:-1]
            grid_ids[row_num][col_num] = int(next_tile_id)
            completed_ids.append(next_tile_id)
            next_side = opposite_side(received_side)
            next_tile_id, received_side, matched = options[next_tile_id][next_side][0]
            next_tile = tiles[next_tile_id]
            if not matched:
                if received_side == 'right':
                    next_tile = np.flipud(next_tile)
                if received_side == 'top':
                    flip_lr_tmp = -1 * flip_lr_tmp
            else:
                if received_side == 'bottom':
                    flip_lr_tmp = -1 * flip_lr_tmp
                if received_side == 'left':
                    next_tile = np.flipud(next_tile)
            if flip_lr_tmp == -1:
                next_tile = np.fliplr(next_tile)

            next_tile = np.rot90(next_tile, 2 + side_names.index(received_side))
        grid[-1][col_num] = next_tile[1:-1, 1:-1]
        grid_ids[-1][col_num] = int(next_tile_id)
        completed_ids.append(next_tile_id)
        if col_num < rows - 1:
            next_row_side = side_names[(side_names.index(row_side) + 1) % 4]
            try:
                row_tile_id, received_side, matched = options[row_tile_id][next_row_side][0]
                if row_tile_id in completed_ids:
                    next_row_side = side_names[(side_names.index(row_side) - 1) % 4]
                    row_tile_id, received_side, matched = options[row_tile_id][next_row_side][0]
            except:
                next_row_side = side_names[(side_names.index(row_side) - 1) % 4]
                row_tile_id, received_side, matched = options[row_tile_id][next_row_side][0]

            row_tile = tiles[row_tile_id]
            if not matched:
                if received_side == 'bottom':
                    row_tile = np.fliplr(row_tile)
                    flip_lr = -1
                if received_side == 'left':
                    flip_ud = -1 * flip_ud
            else:
                if received_side == 'right':
                    flip_ud = -1 * flip_ud
                if received_side == 'top':
                    row_tile = np.fliplr(row_tile)
                    flip_lr = -1
            if flip_ud == -1:
                row_tile = np.flipud(row_tile)

            # rotate to face left
            row_tile = np.rot90(row_tile, 3 + side_names.index(received_side))
            row_side = side_names[(side_names.index(received_side) + 1) % 4]
            try:
                next_tile_id, received_side, matched = options[row_tile_id][row_side][0]
                if next_tile_id in completed_ids:
                    row_side = side_names[(side_names.index(received_side) - 1) % 4]
                    next_tile_id, received_side, matched = options[row_tile_id][row_side][0]
            except:
                row_side = side_names[(side_names.index(received_side) - 1) % 4]
                next_tile_id, received_side, matched = options[row_tile_id][row_side][0]

            next_tile = tiles[next_tile_id]
            next_tile = np.rot90(next_tile, 2 + side_names.index(received_side))
    print(grid_ids.reshape((rows, rows)))
    #return grid.reshape((rows * (10-2), rows * (10-2)))
    return grid


option = 0  # 3
edge = 0
state = 2  # 1
print(corner_tile_ids[option])
print(get_grid(state, corner_tile_ids[option], edge=edge))
print(f'answer to puzzle 1 is {ans1}')
#print(f'answer to puzzle 1 is {complete(False)}')
