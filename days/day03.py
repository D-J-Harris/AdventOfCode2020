"""Toboggan Trajectory"""
import numpy as np

with open('inputs/day03.txt', 'r') as f:
    inp = []
    for line in f.read().splitlines():
        inp.append(line)
p2_trajectories = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]


def trees_for_trajectory(tree_map, trajectory):
    pattern_width = len(tree_map[0])
    right, down = trajectory
    x_pos, count = 0, 0
    for y_pos, row in enumerate(tree_map):
        if not y_pos % down:
            count += row[x_pos % pattern_width] == '#'
            x_pos += right
    return count


print(f'answer to puzzle 1 is {trees_for_trajectory(inp, (3, 1))}')
print(f'answer to puzzle 2 is {np.prod([trees_for_trajectory(inp, t) for t in p2_trajectories])}')
