"""Lobby Layout"""
from collections import defaultdict


with open('../inputs/day24.txt', 'r') as f:
    tiles = defaultdict(int)
    for line in f.read().splitlines():
        pos, length = 0, len(line)

        x, y = 0, 0
        while pos < length:
            dir = line[pos]
            if dir == 'e':
                x += 1
                pos += 1
            if dir == 'w':
                x -= 1
                pos += 1
            if dir == 'n':
                if line[pos + 1] == 'e':
                    x += 0.5
                    y += 1
                if line[pos + 1] == 'w':
                    x -= 0.5
                    y += 1
                pos += 2
            if dir == 's':
                if line[pos + 1] == 'e':
                    x += 0.5
                    y -= 1
                if line[pos + 1] == 'w':
                    x -= 0.5
                    y -= 1
                pos += 2
        tiles[(x, y)] += 1


dxs = (-0.5, 0.5)
dys = (-1, 0, 1)
def update_tiles(all_tiles):

    new_tiles = defaultdict(int)
    for tile, flip_count in all_tiles.items():

        black_count = 0
        for dx in dxs:
            for dy in dys:
                adj = (tile[0] + dx, tile[1] + dy)
                if tiles[adj] % 2 == 1:
                    black_count += 1

        if flip_count % 2 == 1:
            ans1 += 1
            if black_count == 0 or black_count > 2:
                flip_count += 1
        else:
            if black_count == 2:
                flip_count += 1
        if flip_count % 2 == 1:

ans1, ans2 = 0, 0
print(f'answer to puzzle 1 is {ans1}')
#print(f'answer to puzzle 2 is {complete(my_input, 10_000_000, False)}')
