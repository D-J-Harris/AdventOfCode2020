"""Seating System"""
from copy import deepcopy

with open('../inputs/day11.txt', 'r') as f:
    inp = []
    for line in f.read().splitlines():
        inp.append([c for c in line])

adj = [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if not (i == j == 0)]
max_x, max_y = len(inp[0]), len(inp)


def get_adjacent_cells(g, x, y):
    result = []
    for pair in adj:
        dx, dy = pair
        if 0 <= (x + dx) < max_x and 0 <= y + dy < max_y:
            result.append(g[y + dy][x + dx])
    return result


def count_visible_cells(g, x, y):
    result = [0] * 8
    for idx, pair in enumerate(adj):
        dx_orig, dy_orig = pair
        for mult in range(1, max(x, y, max_x-1-x, max_y-1-y)):
            dy = dy_orig * mult
            dx = dx_orig * mult
            if 0 <= (x + dx) < max_x and 0 <= y + dy < max_y:
                seat =g[y + dy][x + dx]
                if seat == '#':
                    result[idx] = 1
                    break
                if seat == 'L':
                    break
    return result


def one_pass(g):
    grid = deepcopy(g)
    for y in range(max_y):
        for x in range(max_x):
            num_occupied = get_adjacent_cells(g, x, y).count('#')
            if g[y][x] == 'L' and num_occupied == 0:
                grid[y][x] = '#'
            if g[y][x] == '#' and num_occupied > 3:
                grid[y][x] = 'L'
    return grid

grid = deepcopy(inp)
while True:
    new_grid = one_pass(grid)
    #for i in new_grid:
    #    print(i)
    #print("\n")
    if new_grid == grid:
        print(f"answer to puzzle 1 is {sum([x.count('#') for x in new_grid])}")
        break
    grid = new_grid

def one_pass_new(g):
    grid = deepcopy(g)
    for y in range(max_y):
        for x in range(max_x):
            a = count_visible_cells(g, x, y)
            num_occupied = sum(a)
            if g[y][x] == 'L' and num_occupied == 0:
                grid[y][x] = '#'
            if g[y][x] == '#' and num_occupied > 4:
                grid[y][x] = 'L'
    return grid

grid = deepcopy(inp)
while True:
    new_grid = one_pass_new(grid)
    #print(adj)
    #for i in new_grid:
    #    print(i)
    #print("\n")
    if new_grid == grid:
        print(f"answer to puzzle 2 is {sum([x.count('#') for x in new_grid])}")
        break
    grid = new_grid

#print(f'answer to puzzle 2 is {np.prod([trees_for_trajectory(inp, t) for t in p2_trajectories])}')
