"""Handy Haversacks"""
from collections import defaultdict
import networkx as nx

graph = nx.DiGraph()
bags = defaultdict(lambda: len(bags))
with open('../inputs/day07.txt', 'r') as f:
    for line in f.readlines():
        inp = line.replace(',', '').rstrip().split(' ')
        num_children = (len(inp) - 4) // 4
        parent_colour = '-'.join(inp[:2])
        for i in range(num_children):
            colour = '-'.join(inp[5+4*i:7+4*i])
            weight = int(inp[4+4*i])
            graph.add_edge(bags[parent_colour], bags[colour], weight=weight)


def bag_total(g, node):
    total = 0
    for child, props in g[node].items():
        total += props['weight'] * (1 + bag_total(g, child))
    return total


print(f'answer to puzzle 1 is {len(nx.ancestors(graph, bags["shiny-gold"]))}')
print(f'answer to puzzle 2 is {bag_total(graph, bags["shiny-gold"])}')
