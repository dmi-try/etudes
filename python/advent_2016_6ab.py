#!/usr/bin/env python

# Solution for http://adventofcode.com/2016/

from collections import defaultdict

sample_data = """
eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar
""".split('\n')[1:-1]

sample_result_a = 'easter'
sample_result_b = 'advent'


class Decryptor:
    def __init__(self, size, method):
        self.stat = []
        self.method = method
        for i in xrange(size):
            self.stat.append({})
    def add_data(self,text):
        for i in xrange(0, len(text)):
            try:
                self.stat[i][text[i]] += 1
            except KeyError:
                self.stat[i][text[i]] = 1
    def dump(self):
        return self.stat
    def decode(self):
        if self.method == 'a':
            return "".join(map(lambda x: max(x, key=x.get), self.stat))
        if self.method == 'b':
            return "".join(map(lambda x: min(x, key=x.get), self.stat))

d = Decryptor(6, 'a')

for l in sample_data:
    d.add_data(l)

assert d.decode(), sample_result_a

d = Decryptor(8, 'a')

with open('advent_2016_6.txt') as fp:  
    line = fp.readline().strip()
    while line and line != '':
        d.add_data(line)
        line = fp.readline().strip()

print d.decode()

d = Decryptor(6, 'b')

for l in sample_data:
    d.add_data(l)

assert d.decode(), sample_result_b

d = Decryptor(8, 'b')

with open('advent_2016_6.txt') as fp:  
    line = fp.readline().strip()
    while line and line != '':
        d.add_data(line)
        line = fp.readline().strip()

print d.decode()
