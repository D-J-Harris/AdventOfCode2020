"""Adapter Array"""
from collections import deque
from copy import deepcopy

with open('../inputs/day10.txt', 'r') as f:
    inp = sorted([int(x) for x in f.read().split()])

diffs = {1: 0, 2: 0, 3: 0}
inp_copy = deque(deepcopy(inp))
for _ in range(len(inp_copy)):
    num = inp_copy.popleft()
    diffs[num] += 1
    inp_copy = deque([x-num for x in inp_copy])

inp_copy2 = deepcopy(inp)
maxi = max(inp_copy2)



def p(l, tot):
    count = 0
    if l[0] != 1:
        return 0

    if len(l) == 1:
        if tot == maxi:
            return 1
        else:
            return 0

    first_diff = l[1] - l[0]
    if first_diff in (1, 2, 3):
        new_l = [x-first_diff for x in l[1:]]
        count += 1 * p(new_l, tot+first_diff)

    if len(l) > 2:
        second_diff = l[2] - l[0]
        if second_diff in (2, 3):
            new_l = [x-second_diff for x in l[2:]]
            count += 1 * p(new_l, tot+second_diff)

    if len(l) > 3:
        third_diff = l[3] - l[0]
        if third_diff == 3:
            new_l = [x-third_diff for x in l[3:]]
            count += 1 * p(new_l, tot+third_diff)

    return count


print(f'answer to puzzle 1 is {diffs[1] * (diffs[3] + 1)}')
a = p(inp_copy2, min(inp))
print(a)
b = p([x-1 for x in inp_copy2[1:]], min(inp)+1)
print(b)
c = p([x-2 for x in inp_copy2[2:]], min(inp)+2)
print(c)

print(f'answer to puzzle 2 is {a + b + c}')
