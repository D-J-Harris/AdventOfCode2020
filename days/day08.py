"""Handheld Halting"""
from helpers.console import Console
from copy import deepcopy

with open('../inputs/day08.txt', 'r') as f:
    inps = []
    for line in f.readlines():
        inp = line.split()
        op, arg = inp[0], int(inp[1])
        inps.append([op, arg])

console = Console(inps)
_, acc = console.exec(0)
print(f'answer to puzzle 1 is {acc}')

for idx, inp in enumerate(inps):
    op = inp[0]
    instr_copy = deepcopy(inps)
    if op == 'nop':
        instr_copy[idx][0] = 'jmp'
    if op == 'jmp':
        instr_copy[idx][0] = 'nop'
    console.reset()
    console.instr = instr_copy
    success, acc = console.exec(0)
    if success:
        print(f'answer to puzzle 2 is {acc}')
        break
