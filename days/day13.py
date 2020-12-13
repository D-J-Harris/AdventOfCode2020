"""Shuttle Search"""
from functools import reduce

with open('../inputs/day13.txt', 'r') as f:
    lines = f.readlines()
    earliest = int(lines[0])
    buses = []
    for idx, x in enumerate(lines[1].split(',')):
        if x.isnumeric():
            buses.append((int(x), idx))

wait = 0
found = False
while not found:
    for bus in buses:
        bus_id, pos = bus
        if isinstance(bus_id, int):
            if (earliest+wait) % bus_id == 0:
                print(f"answer to puzzle 1 is {wait * bus_id}")
                found = True
    wait += 1


# following methods found online.
# chinese remainder theorem for solving
# systems of linear congruent equations.
def chinese_remainder(n, a):
    _sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        _sum += a_i * mul_inv(p, n_i) * p
    return _sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


modulos = [x[0] for x in buses]
remainders = [x[0]-x[1] for x in buses]
remainders[0] = 0
print(f"answer to puzzle 2 is {chinese_remainder(modulos, remainders)}")
