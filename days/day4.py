"""Passport Processing"""
from helpers.passport import Passport

with open('../inputs/day4.txt', 'r') as f:
    inp = []
    for block in f.read().split('\n\n'):
        passport_dict = {}
        for pair in block.split():
            key, val = pair.split(':')
            passport_dict[key] = val
        inp.append(Passport(passport_dict))

count_1, count_2 = 0, 0
for passport in inp:
    count_1 += passport.is_valid()
    count_2 += passport.is_valid_with_checks()

print(f'answer to puzzle 1 is {count_1}')
print(f'answer to puzzle 2 is {count_2}')
