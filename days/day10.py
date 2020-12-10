"""Adapter Array"""
from collections import deque
from copy import deepcopy
import numpy as np
from itertools import groupby

with open('../inputs/day10.txt', 'r') as f:
    inp = sorted([int(x) for x in f.read().split()])
inp_length = len(inp)

diffs = {1: 0, 2: 0, 3: 0}
copy = deque(inp.copy())
for _ in range(inp_length):
    num = copy.popleft()
    diffs[num] += 1
    copy = deque([x-num for x in copy])
print(f'answer to puzzle 1 is {diffs[1] * (diffs[3] + 1)}')

# answer with dynamic programming.
# needed help learning this solution, elegant though.
# initial three inputs are manual depending on no. of paths to each.
dp = [0] * inp_length
dp[0] = 1
dp[1] = 2
dp[2] = 4
for idx in range(3, inp_length):
    for diff in (1, 2, 3):
        if inp[idx] - inp[idx-diff] <= 3:
            dp[idx] += dp[idx-diff]
print(f'answer to puzzle 2 is {dp[-1]}')


# alternative solution with noting there are only ever
# jumps of 1 or 3 - can group the 1s and look at perms.
# got this by peeking the words 'difference' and 'permutation' on reddit
perm_options = {1: 1, 2: 2, 3: 4, 4: 7}
ans = 0
for start in (inp, inp[1:], inp[2:]):
    jumps = np.diff(start)
    groups = groupby(jumps)
    result = [(label, sum(1 for _ in group)) for label, group in groups]
    paths = 1
    for pair in result:
        if pair[0] == 1:
            paths *= perm_options[pair[1]]
    ans += paths
print(f'answer to puzzle 2 is {ans}')
