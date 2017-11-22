#!/usr/bin/env python

# Solution for http://adventofcode.com/2016/


import re


class Screen:
    def __init__(self, width=50, height=6):
        self.width = width
        self.height = height
        self.pixels = []
        for i in xrange(self.height):
            self.pixels.append(['.'] * self.width)
    def show(self):
        return '\n'.join(map(lambda x: ''.join(x), self.pixels))
    def count_lit_pixels(self):
        return sum(map(lambda x: x.count('#'), self.pixels))
    def get_row(self, a):
        return self.pixels[a]
    def get_column(self, a):
        return [self.pixels[x][a] for x in xrange(self.height)]
    def set_row(self, a, row):
        self.pixels[a] = row
    def set_column(self, a, column):
        for i in xrange(self.height):
            self.pixels[i][a] = column[i]
    def rect(self, a, b):
        for i in xrange(b):
            for j in xrange(a):
                self.pixels[i][j] = '#'
    def rotate_row(self, a, b):
        row = self.get_row(a)
        new_row = row[-b % self.width:] + row[:-b % self.width]
        self.set_row(a, new_row)
    def rotate_column(self, a, b):
        column = self.get_column(a)
        new_column = column[-b % self.height:] + column[:-b % self.height]
        self.set_column(a, new_column)
    def cmd(self, cmd):
        m = re.match(r"rect (\d+)x(\d+)", cmd)
        if m:
            return self.rect(int(m.group(1)), int(m.group(2)))
        m = re.match(r"rotate column x=(\d+) by (\d+)", cmd)
        if m:
            return self.rotate_column(int(m.group(1)), int(m.group(2)))
        m = re.match(r"rotate row y=(\d+) by (\d+)", cmd)
        if m:
            return self.rotate_row(int(m.group(1)), int(m.group(2)))
        raise Exception("Bad command or file name: %s" % cmd)

print "Work with sample data"
s = Screen(7, 3)
s.cmd('rect 3x2')
s.cmd('rotate column x=1 by 1')
s.cmd('rotate row y=0 by 4')
s.cmd('rotate column x=1 by 1')
print s.show()
print "Number of pixels lit is", s.count_lit_pixels()

print "Work with real data"
s = Screen()
with open('advent_2016_8.txt') as fp:  
    line = fp.readline().strip()
    while line and line != '':
        s.cmd(line)
        line = fp.readline().strip()
print s.show()
print "Number of pixels lit is", s.count_lit_pixels()
