"""Crab Cups"""


def complete(inp, moves, first):
    map = {}
    length = len(inp)

    inp = [int(x) for x in inp]
    if not first:
        for num in range(length + 1, 1_000_001):
            inp.append(num)
        length = 1_000_000

    for idx, x in enumerate(inp):
        map[x] = int(inp[(idx + 1) % length])

    current = inp[0]
    for _ in range(moves):
        cup_1 = map[current]
        cup_2 = map[cup_1]
        cup_3 = map[cup_2]

        dest_cup = current - 1 if current != 1 else length
        while dest_cup in (cup_1, cup_2, cup_3):
            dest_cup = (dest_cup - 1) if dest_cup != 1 else length

        map[current] = map[cup_3]
        map[cup_3] = map[dest_cup]
        map[dest_cup] = cup_1
        map[cup_1] = cup_2
        map[cup_2] = cup_3
        current = map[current]

    if first:
        ans = []
        curr = 1
        for _ in range(length - 1):
            curr = map[curr]
            ans.append(curr)
        return ''.join([str(x) for x in ans])
    else:
        one = map[1]
        two = map[one]
        return one * two


my_input = '137826495'
print(f'answer to puzzle 1 is {complete(my_input, 100, True)}')
print(f'answer to puzzle 2 is {complete(my_input, 10_000_000, False)}')
