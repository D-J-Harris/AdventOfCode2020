"""Encoding Error"""
import itertools

with open('../inputs/day09.txt', 'r') as f:
    inp = []
    for line in f.read().splitlines():
        inp.append(int(line))

target = 0
preamble_length = 25
for pos in range(preamble_length, len(inp)-1):
    preamble = inp[pos-25:pos]
    num = inp[pos]
    all_sums = set([sum(i) for i in list(itertools.combinations(preamble, 2))])
    if num not in all_sums:
        target = num
        print(f'answer to puzzle 1 is {target}')
        break

for pos, num in enumerate(inp):
    cont_set, sums = [num], num
    progress = 0
    while sums < target and pos < len(inp):
        progress += 1
        next_num = inp[pos+progress]
        sums += next_num
        cont_set.append(next_num)
        if sums == target:
            print(f'answer to puzzle 2 is {max(cont_set)+min(cont_set)}')
            break
    else:
        continue
    break
