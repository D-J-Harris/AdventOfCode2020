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
                x += 2
                pos += 1
            if dir == 'w':
                x -= 2
                pos += 1
            if dir == 'n':
                if line[pos + 1] == 'e':
                    x += 1
                    y += 1
                if line[pos + 1] == 'w':
                    x -= 1
                    y += 1
                pos += 2
            if dir == 's':
                if line[pos + 1] == 'e':
                    x += 1
                    y -= 1
                if line[pos + 1] == 'w':
                    x -= 1
                    y -= 1
                pos += 2
        tiles[(x, y)] += 1


def update_tiles(t):
    max_x = max([abs(i[0]) for i in t.keys()]) + 1
    max_y = max([abs(i[1]) for i in t.keys()]) + 1
    changes = [(-2, 0), (2, 0), (-1, 1), (-1, -1), (1, -1), (1, 1)]
    update_t = defaultdict(int)

    # check x and y one further out than maxes
    for x in range(-1 * max_x, max_x + 1):
        for y in range(-1 * max_y, max_y + 1):
            black_count = 0
            for change in changes:
                dx, dy = change[0], change[1]
                adj = (x + dx, y + dy)
                if t[adj] % 2 == 1:
                    black_count += 1

            flip_count = t[(x, y)]
            if flip_count % 2 == 1:
                if black_count == 0 or black_count > 2:
                    flip_count += 1
            else:
                if black_count == 2:
                    flip_count += 1
            update_t[(x, y)] = flip_count
    return update_t


def complete(alL_tiles, updates):
    for _ in range(updates):
        alL_tiles = update_tiles(alL_tiles)

    ans = 0
    for tile, flip_count in alL_tiles.items():
        if flip_count % 2 == 1:
            ans += 1
    return ans


print(f'answer to puzzle 1 is {complete(tiles, 0)}')
print(f'answer to puzzle 2 is {complete(tiles, 100)}')
