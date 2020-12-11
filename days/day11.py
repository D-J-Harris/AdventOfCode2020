"""Seating System"""
from copy import deepcopy

with open('../inputs/day11.txt', 'r') as f:
    inp = []
    for line in f.read().splitlines():
        inp.append([c for c in line])
max_x, max_y = len(inp[0]), len(inp)


def count_visible(g, x_coord, y_coord, first_part):
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
    return sum(result.values())


def one_pass(g, first_part):
    updates = []
    for y in range(max_y):
        for x in range(max_x):
            num_occupied = count_visible(g, x, y, first_part=first_part)
            if g[y][x] == 'L' and num_occupied == 0:
                updates.append([x, y, '#'])
            if g[y][x] == '#' and num_occupied > (3 if first_part else 4):
                updates.append([x, y, 'L'])

    for update in updates:
        x, y, val = update
        g[y][x] = val
    return True if updates else False


def complete_game(first_part):
    grid = deepcopy(inp)
    while True:
        changed = one_pass(grid, first_part=first_part)
        if not changed:
            return sum([x.count('#') for x in grid])


print(f'answer to puzzle 1 is {complete_game(first_part=True)}')
print(f'answer to puzzle 2 is {complete_game(first_part=False)}')
