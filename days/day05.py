"""Binary Boarding"""

with open('../inputs/day05.txt', 'r') as f:
    inp = []
    for line in f.read().split():
        inp.append(line)


def seat_id(board_pass):
    row, col = 0, 0
    row_instr, col_instr = 7, 3
    for j in range(row_instr + col_instr):
        zone = board_pass[j]
        if zone == 'B':
            row += 2 ** ((row_instr-1)-j)
        if zone == 'R':
            col += 2 ** ((col_instr-1)-(j-row_instr))
    return 8 * row + col


seat_ids = sorted([seat_id(line) for line in inp])
print(f'answer to puzzle 1 is {max(seat_ids)}')
for i in range(1, len(seat_ids)):
    if seat_ids[i] - seat_ids[i-1] != 1:
        print(f'answer to puzzle 2 is {seat_ids[i]-1}')
