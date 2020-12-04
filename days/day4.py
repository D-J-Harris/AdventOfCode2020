"""Passport Processing"""
from helpers.passport import Passport
import re

with open('../inputs/day4.txt', 'r') as f:
    inp = []
    for block in f.read().split('\n\n'):
        passport = {}
        for pair in block.split():
            key, val = pair.split(':')
            passport[key] = val
        inp.append(passport)

count_1, count_2 = 0, 0
for passport in inp:
    num_fields = len(passport)
    if num_fields == 8 or (num_fields == 7 and 'cid' not in passport):
        count_1 += 1
        hgt_unit = passport['hgt'][-2:]
        if hgt_unit in ['cm', 'in']:
            if (1920 <= (int(passport['byr'])) <= 2002) and (2010 <= (int(passport['iyr'])) <= 2020) and (2020 <= (int(passport['eyr'])) <= 2030) and (((150 <= (int(passport['hgt'][:-2])) <= 193) and hgt_unit == 'cm') or ((59 <= (int(passport['hgt'][:-2])) <= 76) and hgt_unit == 'in')) and (passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']) and (len(passport['pid']) == 9) and (re.match("^[A-Za-z0-9]*$", passport['hcl'][1:])) and (passport['hcl'][0] == '#') and (len(passport['hcl']) == 7):
                count_2 += 1
print(f'answer to puzzle 1 is {count_1}')
print(f'answer to puzzle 2 is {count_2}')
