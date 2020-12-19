"""Monster Messages"""
from collections import defaultdict

rule_map = defaultdict(list)
rule_map['a'] = 'a'
rule_map['b'] = 'b'
with open('../inputs/test.txt', 'r') as f:
    for line in f.read().splitlines():
        if not line:
            continue
        if line[0].isdigit():
            rules = []
            for rule in line[3:].split(' | '):
                if rule in ("\"a\"", "\"b\""):
                    rule_map[int(line[0])] = rule[1]
                else:
                    rule_map[int(line[0])].append(list(map(int, rule.rsplit())))
        elif line[0].isalpha():
            b=1


def check_string_list(obj):
    return bool(obj) and all(isinstance(elem, str) for elem in obj)

# transform rule_map codes into permutations of allowed codes
rules = rule_map[0]
while not all(check_string_list(x) for x in rules):
    rules_2 = []
    for rule_idx, rule in enumerate(rules):
        print(rule)
        num_perms = 2**sum([len(rule_map[x])-1 for x in rule])
        new_rules = [[] for _ in range(num_perms)]
        combo_indexer = 2
        for perm_idx in range(num_perms):
            for c in rule:
                if isinstance(c, str):
                    new_rules[perm_idx].append(c)
                else:
                    val = rule_map[c]
                    if isinstance(val, str):
                        new_rules[perm_idx].append(val)
                    else:
                        print(perm_idx, combo_indexer, perm_idx%combo_indexer)
                        print(val)

                        new_rules[perm_idx].append(val[perm_idx % combo_indexer])
            combo_indexer *= 2

        # flatten each new rule
        new_rule = [[item for sublist in x for item in sublist] for x in new_rules]
        print(new_rule)
        for r in new_rule:
            rules_2.append(r)
    rules = rules_2
    print('huh', rules)


#print(f'answer to puzzle 1 is {ans1}')
#print(f'answer to puzzle 2 is {ans2}')
