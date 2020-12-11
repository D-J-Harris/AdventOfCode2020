"""Seating System"""
from copy import deepcopy

with open('../inputs/day11.txt', 'r') as f:
    inp = []
    for line in f.read().splitlines():
        inp.append([c for c in line])

adj = [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if not (i == j == 0)]
max_x, max_y = len(inp[0]), len(inp)


def count_visible(g, x, y, first_part):
    result = [0] * 8
    for idx, pair in enumerate(adj):
        scan_range = max(x, y, max_x-x-1, max_y-y-1)
        for mult in range(1, (2 if first_part else scan_range)):
            coords = tuple(mult * x for x in pair)
            dx, dy = coords
            if 0 <= (x + dx) < max_x and 0 <= y + dy < max_y:
                seat =g[y + dy][x + dx]
                if seat == '#':
                    result[idx] = 1
                    break
                if seat == 'L':
                    break
    return sum(result)


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
