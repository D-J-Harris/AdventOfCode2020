"""Report Repair"""
from itertools import combinations
from math import prod

with open('inputs/day1.txt', 'r') as f:
    inp = [int(x) for x in f.read().split()]

num_inp, target = len(inp), 2020
for ip1 in range(num_inp):
    found = False
    for ip2 in range(ip1+1, num_inp):
        if inp[ip1] + inp[ip2] == target:
            print(f'answer to puzzle 1 is {inp[ip1] * inp[ip2]}')
        for ip3 in range(ip2+1, num_inp):
            if inp[ip1] + inp[ip2] + inp[ip3] == target:
                print(f'answer to puzzle 2 is {inp[ip1] * inp[ip2] * inp[ip3]}')

# solution I wish I'd thought of
print([prod(c) for c in combinations(inp, 2) if sum(c) == 2020])
print([prod(c) for c in combinations(inp, 3) if sum(c) == 2020])
