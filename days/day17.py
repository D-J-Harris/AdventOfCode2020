"""Conway Cubes"""
from copy import deepcopy
import numpy as np
import numpy
import sys
numpy.set_printoptions(threshold=sys.maxsize)

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
max_x, max_y, max_z = len(inp[0]) + 2*num_cycles, len(inp) + 2*num_cycles, 1 + 2*num_cycles

cube = np.array([[['.' for row in range(max_x)] for col in range(max_y)] for layer in range(max_z)])
cube[num_cycles] = np.pad(inp, 6, pad_with, padder='.')
#print(cube)


def count_active(c, x_coord, y_coord, z_coord, first_part):
    result = {}
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            for dz in (-1, 0, 1):
                if dx == 0 and dy == 0 and dz == 0:
                    continue
                x, y, z = x_coord + dx, y_coord + dy, z_coord + dz
                if 0 <= x < max_x and 0 <= y < max_y and 0 <= z < max_z:
                    cube = c[z][y][x]
                    if cube == '#':
                        result[(dx, dy, dz)] = 1
    return sum(result.values())


def one_pass(c, first_part):
    updates = []
    for z in range(max_z):
        for y in range(max_y):
            for x in range(max_x):
                num_active = count_active(c, x, y, z, first_part=first_part)
                if c[z][y][x] == '#' and (num_active < 2 or num_active > 3):
                    updates.append([x, y, z, '.'])
                if c[z][y][x] == '.' and num_active == 3:
                    updates.append([x, y, z, '#'])
    for update in updates:
        x, y, z, val = update
        c[z][y][x] = val
    return True if updates else False


def complete_game(first_part):
    game_cube = deepcopy(cube)
    for i in range(num_cycles):
        one_pass(game_cube, first_part=first_part)
        #print(f'======= cycle {i} ========')
        #print(game_cube)
    print(np.count_nonzero(game_cube == '#'))

complete_game(True)
#print(f'answer to puzzle 1 is {complete_game(first_part=True)}')
#print(f'answer to puzzle 2 is {complete_game(first_part=False)}')
