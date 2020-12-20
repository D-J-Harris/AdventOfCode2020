"""Monster Messages"""
from collections import defaultdict
import regex

rule_map = defaultdict(list)
with open('../inputs/test.txt', 'r') as f:
    rules, strings = f.read().split('\n\n')
    for line in rules.split('\n'):
        rule_key, rule = line.split(': ')
        for rule_option in rule.split(' | '):
            if rule_option in ("\"a\"", "\"b\""):
                rule_map[rule_key] = rule_option[1]
            else:
                rule_map[rule_key].append(rule_option)


def reduce_to_regex(rule, first):
    ban_list = [' ', 'a', 'b', '(', '|',
                ')', '+', '?', '*', 's']
    while not all(x in ban_list for x in rule):
        rule_parts = []
        for x in rule.split():
            if x not in ban_list:
                x = replace(x, first)
            rule_parts.append(f" {x} ")
        rule = "".join(rule_parts)
    return rule


def replace(c, first):
    r = rule_map[c]
    if not first:
        if c == '8':
            return f" ( {r[0]} ) + "
        elif c == '11':
            return "  ( 42 ( ? s ) * 31 ) "
    if len(r) == 1:
        return f" ( {r[0]} ) "
    else:
        return f" ( {r[0]} | {r[1]} ) "


def complete(first):
    starting_rule = rule_map['0'][0]
    reg = reduce_to_regex(starting_rule, True) if first else reduce_to_regex(starting_rule, False)
    pattern = f"^{reg.replace(' ', '')}$"
    print(pattern)
    ans = 0
    for line in strings.split('\n'):
        if regex.match(pattern, line):
            ans += 1
    return ans


print(f'answer to puzzle 1 is {complete(True)}')
print(f'answer to puzzle 1 is {complete(False)}')
