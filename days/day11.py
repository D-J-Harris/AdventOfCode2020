"""Seating System"""
from copy import deepcopy
import multiprocessing as mp
from itertools import product

with open('../inputs/day11.txt', 'r') as f:
    inp = []
    for line in f.read().splitlines():
        inp.append([c for c in line])
max_x, max_y = len(inp[0]), len(inp)


def get_update(g, x_coord, y_coord, first_part):
    result = {}
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx == 0 and dy == 0:
                continue
            x, y = x_coord + dx, y_coord + dy
            while 0 <= x < max_x and 0 <= y < max_y:
                seat =g[y][x]
                if seat != '.':
                    if seat == '#':
                        result[(dx, dy)] = 1
                    break
                if first_part:
                    break
                else:
                    x, y = x+dx, y+dy
    num_occupied = sum(result.values())
    if g[y_coord][x_coord] == 'L' and num_occupied == 0:
        return x_coord, y_coord, '#'
    if g[y_coord][x_coord] == '#' and num_occupied > (3 if first_part else 4):
        return x_coord, y_coord, 'L'


def one_pass(g, first_part):
    params = product([g], range(max_x), range(max_y), [first_part])
    with mp.Pool() as pool:
        updates = pool.starmap(get_update, params)
    for update in updates:
        if update:
            x, y, val = update
            if val:
                g[y][x] = val
    return any(updates)


def complete_game(first_part):
    grid = deepcopy(inp)
    changed = True
    while changed:
        changed = one_pass(grid, first_part=first_part)
    return sum([x.count('#') for x in grid])


# solution is slower than the non-parallelised version.
# faster version can be found in previous commit for this file.
if __name__ == '__main__':
    print(f'answer to puzzle 1 is {complete_game(first_part=True)}')
    print(f'answer to puzzle 2 is {complete_game(first_part=False)}')
