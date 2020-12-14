"""Docking Data"""
from itertools import product


def add_zeros(value):
    return [0] * max(0, 36-len(value)) + value


memory = {}
with open('../inputs/day14.txt', 'r') as f:
    for line in f.read().splitlines():

        # line for memory
        if line[1] == 'e':
            ovr_adrs = int(line.split(' = ')[0][4:-1])
            num = int(line.split(' = ')[1])
            binary = add_zeros([int(i) for i in bin(num)[2:]])
            for idx, ovr_num in enumerate(mask):
                if isinstance(ovr_num, int):
                    binary[idx] = ovr_num
            decimal = int("".join(str(x) for x in binary), 2)
            memory[ovr_adrs] = decimal

        # line for mask
        else:
            mask = [int(x) if x.isnumeric() else x for x in line[7:]]
print(f"answer to puzzle 1 is {sum(memory.values())}")

memory = {}
with open('../inputs/day14.txt', 'r') as f:
    for line in f.read().splitlines():
        if line[1] == 'e':
            final_val = int(line.split(' = ')[1])
            ovr_adrs = int(line.split(' = ')[0][4:-1])
            binary = add_zeros([int(i) for i in bin(ovr_adrs)[2:]])
            for idx, ovr_num in enumerate(mask):
                if ovr_num == 'X' or ovr_num == 1:
                    binary[idx] = ovr_num
            num_x = binary.count('X')
            combos = list(product(range(2), repeat=num_x))
            for c in combos:
                counter = 0
                new_binary = binary.copy()
                for idx, i in enumerate(binary):
                    if i == 'X':
                        new_binary[idx] = c[counter]
                        counter += 1
                decimal = int("".join(str(x) for x in new_binary), 2)
                memory[decimal] = final_val
        else:
            mask = [int(x) if x.isnumeric() else x for x in line[7:]]
print(f"answer to puzzle 2 is {sum(memory.values())}")
