"""Conway Cubes"""
from copy import deepcopy
import numpy as np
num_cycles = 6


def pad_with(vector, pad_width, iaxis, kwargs):
    pad_value = kwargs.get('padder', num_cycles)
    vector[:pad_width[0]] = pad_value
    vector[-pad_width[1]:] = pad_value


with open('../inputs/day17.txt', 'r') as f:
    inp = []
    for line in f.read().splitlines():
        inp.append([c for c in line])
    inp = np.array(inp)
max_x, max_y, max_z, max_w = len(inp[0]) + 2*num_cycles, len(inp) + 2*num_cycles, 1 + 2*num_cycles, 1 + 2*num_cycles

cube = np.array([[[['.' for row in range(max_x)] for col in range(max_y)] for layer in range(max_z)] for hyp in range(max_w)])
cube[num_cycles][num_cycles] = np.pad(inp, 6, pad_with, padder='.')


def count_active(c, x_coord, y_coord, z_coord, w_coord):
    result = {}
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            for dz in (-1, 0, 1):
                for dw in (-1, 0, 1):
                    if dx == 0 and dy == 0 and dz == 0 and dw == 0:
                        continue
                    x, y, z, w = x_coord + dx, y_coord + dy, z_coord + dz, w_coord + dw
                    if 0 <= x < max_x and 0 <= y < max_y and 0 <= z < max_z and 0 <= w < max_w:
                        cube = c[w][z][y][x]
                        if cube == '#':
                            result[(dx, dy, dz, dw)] = 1
    return sum(result.values())


def one_pass(c):
    updates = []
    for w in range(max_w):
        for z in range(max_z):
            for y in range(max_y):
                for x in range(max_x):
                    num_active = count_active(c, x, y, z, w)
                    if c[w][z][y][x] == '#' and (num_active < 2 or num_active > 3):
                        updates.append([x, y, z, w, '.'])
                    if c[w][z][y][x] == '.' and num_active == 3:
                        updates.append([x, y, z, w, '#'])
    for update in updates:
        x, y, z, w, val = update
        c[w][z][y][x] = val
    return True if updates else False


def complete_game():
    game_cube = deepcopy(cube)
    for i in range(num_cycles):
        one_pass(game_cube)
    print(np.count_nonzero(game_cube == '#'))


# could optimise by dynamically setting ranges lines 42-45
# based on cycle number, but life is too short.
print(f'answer to puzzle 2 is {complete_game()}')
