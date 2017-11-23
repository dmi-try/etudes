#!/usr/bin/env python

# Solution for http://adventofcode.com/2016/

from pprint import pprint

sample_data="""
value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2
""".split('\n')[1:-1]

with open('advent_2016_10.txt') as fp:
    real_data = fp.read().split('\n')

def solve(data, v1, v2):
    tree = {}
    for i in data:
        r = i.split()
        if r[0] == 'value':
            v = ' '.join(r[:2])
            b = ' '.join(r[-2:])
            tree[v] = {'node': v, 'targets': [b], 'inputs': [], 'done': False}
            continue
        if r[0] == 'bot':
            b = ' '.join(r[:2])
            t1 = ' '.join(r[5:7])
            t2 = ' '.join(r[-2:])
            tree[b] = {'node': b, 'targets': [t1, t2], 'inputs': [], 'done': False}
            continue

    for v in filter(lambda x: x.startswith('value'), tree):
        print v, tree[v]
        t = tree[v]['targets'][0]
        tree[t]['inputs'].append(int(v.split()[1]))
        tree[v]['done'] = True

    def bot_for_calculation(b):
        return len(tree[b]['inputs']) == 2 and tree[b]['done'] == False

    nodes = filter(bot_for_calculation, tree)
    while nodes:
        for b in nodes:
            tree[b]['inputs'].sort()
            t_low = tree[b]['targets'][0]
            t_high = tree[b]['targets'][1]
            if t_low.startswith('output'):
                assert t_low not in tree
                tree[t_low] = {'node': t_low, 'inputs': [tree[b]['inputs'][0]], 'done': True}
            else:
                tree[t_low]['inputs'].append(tree[b]['inputs'][0])
            if t_high.startswith('output'):
                assert t_high not in tree
                tree[t_high] = {'node': t_low, 'inputs': [tree[b]['inputs'][1]], 'done': True}
            else:
                tree[t_high]['inputs'].append(tree[b]['inputs'][1])
            tree[b]['done'] = True
            pprint([tree[b], tree[t_low], tree[t_high]])
        nodes = filter(bot_for_calculation, tree)

    assert filter(lambda x: tree[x]['done'] == False, tree) == []
    print filter(lambda x: tree[x]['inputs'] == [v1, v2], tree)
    print tree['output 0']['inputs'][0] * tree['output 1']['inputs'][0] * tree['output 2']['inputs'][0]

solve(sample_data, 2, 5)
solve(real_data, 17, 61)