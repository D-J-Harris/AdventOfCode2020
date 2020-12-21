"""Allergen Assessment"""
import re

allergen_options_map = {}
all_ingredients = []
with open('../inputs/day21.txt', 'r') as f:
    for line in f.read().splitlines():
        ingredients = [x for x in line[:line.index(' (')].split()]
        for ingr in ingredients:
            all_ingredients.append(ingr)
        allergen_pattern = re.search(r"\(([A-Za-z, ]+)\)", line).group(0)
        allergens = [x for x in allergen_pattern[10:-1].split(', ')]
        for allergen in allergens:
            if allergen in allergen_options_map:
                allergen_options_map[allergen] = allergen_options_map[allergen].intersection(set(ingredients))
            else:
                allergen_options_map[allergen] = set(ingredients)

ans1 = 0
for non_allergen_ingr in set(all_ingredients) - set().union(*allergen_options_map.values()):
    ans1 += all_ingredients.count(non_allergen_ingr)
print(f'answer to puzzle 1 is {ans1}')

to_remove = set()
allergen_map = {}
while len(allergen_map) != len(allergen_options_map):
    for allergen in sorted(allergen_options_map, key=lambda k: len(allergen_options_map[k])):
        if allergen not in allergen_map:
            potential = allergen_options_map[allergen] - to_remove
            if len(potential) == 1:
                allergen_map[allergen] = potential
                to_remove = to_remove.union(allergen_options_map[allergen])

sorted_allergens = dict(sorted(allergen_map.items(), key=lambda x: x[0].lower()))
ans2 = ','.join(ingrs.pop() for ingrs in sorted_allergens.values())
print(f'answer to puzzle 2 is {ans2}')
