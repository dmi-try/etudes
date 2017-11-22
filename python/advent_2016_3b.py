#!/usr/bin/env python

# Solution for http://adventofcode.com/2016/

def is_triange(a, b, c):
    k = sorted([a, b, c])
    return k[2] < k[0] + k[1]


print is_triange(5, 10, 25)

triangles = 0

with open('advent_2016_3.txt') as fp:  
    line1 = fp.readline()
    line2 = fp.readline()
    line3 = fp.readline()

    while line1 and line1 != '':
        if is_triange(int(line1[0:5]), int(line2[0:5]), int(line3[0:5])):
            triangles += 1
        if is_triange(int(line1[5:10]), int(line2[5:10]), int(line3[5:10])):
            triangles += 1
        if is_triange(int(line1[10:15]), int(line2[10:15]), int(line3[10:15])):
            triangles += 1
        line1 = fp.readline()
        line2 = fp.readline()
        line3 = fp.readline()

print triangles
