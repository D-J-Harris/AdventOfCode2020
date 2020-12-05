"""Binary Boarding"""

with open('../inputs/day05.txt', 'r') as f:
    inp = []
    for line in f.read().split():
        inp.append(line)


def seat_id(board_pass):
    row, col = 0, 0
    for j in range(7):
        zone = board_pass[j]
        if zone == 'B':
            row += 2 ** (6-j)
    for k in range(3):
        zone = board_pass[k + 7]
        if zone == 'R':
            col += 2 ** (2-k)
    return 8 * row + col


seat_ids = sorted([seat_id(line) for line in inp])
print(f'answer to puzzle 1 is {max(seat_ids)}')
for i in range(1, len(seat_ids)):
    if seat_ids[i] - seat_ids[i-1] - 1 != 0:
        print(f'answer to puzzle 2 is {seat_ids[i]-1}')
