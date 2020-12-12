"""Rain Risk"""

with open('../inputs/day12.txt', 'r') as f:
    inp = []
    for line in f.readlines():
        dir = line[0]
        num = int(line[1:])
        inp.append([dir, num])

rules = {'E': 1 + 0j,
         'N': 0 + 1j,
         'W': -1 + 0j,
         'S': 0 - 1j,
         'L': 0 + 1j,
         'R': 0 - 1j}
rules_rev = {v: k for k, v in rules.items()}


def update(pos_ship, pos_wp, orient_ship, instr, first):
    dir, num = instr
    if first:
        if dir == 'F':
            pos_ship += rules[orient_ship] * num
        elif dir in ('L', 'R'):
            for _ in range(num // 90):
                orient_ship = rules_rev[rules[orient_ship] * rules[dir]]
        else:
            pos_ship += rules[dir] * num
    else:
        if dir == 'F':
            pos_ship += pos_wp * num
        elif dir in ('L', 'R'):
            for _ in range(num // 90):
                pos_wp *= rules[dir]
        else:
            pos_wp += rules[dir] * num
    return pos_ship, pos_wp, orient_ship


def complete(pos_ship, pos_wp, orient_ship, first):
    for instr in inp:
        pos_ship, pos_wp, orient_ship = update(pos_ship, pos_wp, orient_ship, instr, first)
    return abs(pos_ship.real) + abs(pos_ship.imag)


print(f"answer to puzzle 1 is {complete(0 + 0j, 0, 'E', first=True)}")
print(f"answer to puzzle 1 is {complete(0 + 0j, 10 + 1j, '', first=False)}")
