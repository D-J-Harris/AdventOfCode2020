"""Ticket Translation"""
from collections import defaultdict

with open('../inputs/day16.txt', 'r') as f:
    mode = 'fields'
    fields = defaultdict(list)
    error_rate = 0
    neartickets = []
    for line in f.read().splitlines():
        # switch the parse mode
        if line == 'your ticket:':
            mode = 'yourticket'
            continue
        if line == 'nearby tickets:':
            mode = 'neartickets'
            continue
        if line == '':
            continue

        # parse input line in each parse mode
        if mode == 'fields':
            field, ranges = line.split(': ')
            range_one, range_two = ranges.split(' or ')
            rol, rou = map(int, range_one.split('-'))
            rtl, rtu = map(int, range_two.split('-'))
            fields[field].extend(range(rol, rou+1))
            fields[field].extend(range(rtl, rtu + 1))
        if mode == 'yourticket':
            your_ticket = list(map(int, line.split(',')))
        if mode == 'neartickets':
            ticket_nums = list(map(int, line.split(',')))
            valid = True
            for num in ticket_nums:
                if num not in (item for sublist in fields.values() for item in sublist):
                    error_rate += num
                    valid = False
                    continue
            if valid:
                neartickets.append(ticket_nums)

# get valid fields for each position
num_fields = len(neartickets[0])
fields_map = defaultdict(list)
for field_num in range(num_fields):
    nums = set([x[field_num] for x in neartickets])
    for k, v in fields.items():
        if nums.issubset(set(v)):
            fields_map[field_num].append(k)

# iteratively deduce field mapping
ans = 1
found = set()
lengths = [len(x) for x in fields_map.values()]
for length in range(1, num_fields+1):
    field_key = lengths.index(length)
    possible = set(fields_map[field_key])
    assign = possible - found
    fieldname = next(iter(assign))
    if 'departure' in fieldname:
        ans *= your_ticket[field_key]
    found.update(assign)

print(f"answer to puzzle 1 is {error_rate}")
print(f"answer to puzzle 2 is {ans}")
