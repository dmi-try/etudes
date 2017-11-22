#!/usr/bin/env python

# Solution for http://adventofcode.com/2016/

def is_triange(a, b, c):
    k = sorted([a, b, c])
    return k[2] < k[0] + k[1]


print is_triange(5, 10, 25)

triangles = 0

with open('advent_2016_3.txt') as fp:  
    line = fp.readline()
    while line and line != '':
        print line
        if is_triange(int(line[0:5]), int(line[5:10]), int(line[10:15])):
            triangles += 1
        line = fp.readline()

print triangles
