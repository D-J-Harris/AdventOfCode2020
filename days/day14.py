"""Docking Data"""
from itertools import product


def add_zeros(value):
    return [0] * max(0, 36-len(value)) + value


def complete(first_part):
    memory = {}
    with open('../inputs/day14.txt', 'r') as f:
        for line in f.read().splitlines():

            # line for memory
            if line[:3] == 'mem':
                adrs = int(line.split(' = ')[0][4:-1])
                num = int(line.split(' = ')[1])

                # number that mask is applied to
                if first_part:
                    binary = add_zeros([int(i) for i in bin(num)[2:]])
                else:
                    binary = add_zeros([int(i) for i in bin(adrs)[2:]])

                # override the binary if condition met
                for idx, ovride in enumerate(mask):
                    if ovride == 1 or \
                            (ovride == 0 and first_part) or \
                            (ovride == 'X' and not first_part):
                        binary[idx] = ovride

                # get all memory overrides
                if first_part:
                    decimal = int("".join(str(x) for x in binary), 2)
                    memory[adrs] = decimal
                else:
                    num_x = binary.count('X')
                    combos = list(product(range(2), repeat=num_x))
                    for c in combos:
                        counter = 0
                        binary_float = binary.copy()
                        for idx, i in enumerate(binary_float):
                            if i == 'X':
                                binary_float[idx] = c[counter]
                                counter += 1
                        adrs = int("".join(str(x) for x in binary_float), 2)
                        memory[adrs] = num

            # line for mask
            else:
                mask = [int(x) if x.isnumeric() else x for x in line[7:]]
    return sum(memory.values())


print(f"answer to puzzle 1 is {complete(first_part=True)}")
print(f"answer to puzzle 2 is {complete(first_part=False)}")
