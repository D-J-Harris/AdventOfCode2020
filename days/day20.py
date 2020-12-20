"""Jurassic Jigsaw"""
from collections import defaultdict
import numpy as np

with open('../inputs/day20.txt', 'r') as f:
    tiles = {}
    for block in f.read().split('\n\n'):
        sides = {}
        lines = block.split('\n')
        tile_id = int(lines[0][5:-1])
        sides['top'] = lines[1]
        sides['bottom'] = lines[-1]
        sides['left'] = ''.join(x[0] for x in lines[1:])
        sides['right'] = ''.join(x[-1] for x in lines[1:])
        tiles[tile_id] = sides

# find side options
options = defaultdict(lambda: defaultdict(list))
side_names = ('top', 'right', 'bottom', 'left')
for tile_id, sides in tiles.items():
    for side, pattern in sides.items():
        for tile_id_other, sides_other in tiles.items():
            for side_name in side_names:
                if tile_id != tile_id_other and pattern == sides_other[side_name]:
                    options[tile_id][side].append([int(tile_id_other), side_name, 1])
                if tile_id != tile_id_other and pattern[::-1] == sides_other[side_name]:
                    options[tile_id][side].append([int(tile_id_other), side_name, -1])

# find part 1 answer
ans = 1
for tile_id, sides in options.items():
    num_sides = sum([len(x) for x in sides.values()])
    if num_sides == 2:
        print(tile_id)
        ans *= tile_id
corner = 2909

# create grid
rows = int(np.sqrt(len(tiles)))
grid = []
flipped = 1
first_tile, first_side = corner, list(options[corner].keys())[0]
next_tile, next_side, _ = list(options[corner].values())[0][0]
print(rows)
for row_num in range(rows):
    row = [first_tile]
    for _ in range(rows - 2):
        row.append(next_tile)
        print(next_tile, next_side)
        print(options[next_tile])
        next_side = side_names[(side_names.index(next_side)+2) % 4]
        next_tile, next_side, _ = options[next_tile][next_side][0]
    row.append(next_tile)
    grid.append(row)
    print(grid)
    if row_num < rows - 1:
        if flipped == -1:
            next_row_side = side_names[(side_names.index(first_side)+1) % 4]
        else:
            next_row_side = side_names[(side_names.index(first_side)-1) % 4]
        first_tile, pre_side, flipped_tmp = options[first_tile][next_row_side][0]
        flipped = flipped * flipped_tmp
        if flipped == -1:
            next_side = side_names[(side_names.index(pre_side)+1) % 4]
        else:
            next_side = side_names[(side_names.index(pre_side)-1) % 4]
        next_tile, next_side, _ = options[first_tile][next_side][0]
print(grid)

print(f'answer to puzzle 1 is {ans}')
#print(f'answer to puzzle 1 is {complete(False)}')
