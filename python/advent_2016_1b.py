#!/usr/bin/env python

# Solution for http://adventofcode.com/2016/

instruction = "R3, L5, R1, R2, L5, R2, R3, L2, L5, R5, L4, L3, R5, L1, R3, R4, R1, L3, R3, L2, L5, L2, R4, R5, R5, L4, L3, L3, R4, R4, R5, L5, L3, R2, R2, L3, L4, L5, R1, R3, L3, R2, L3, R5, L194, L2, L5, R2, R1, R1, L1, L5, L4, R4, R2, R2, L4, L1, R2, R53, R3, L5, R72, R2, L5, R3, L4, R187, L4, L5, L2, R1, R3, R5, L4, L4, R2, R5, L5, L4, L3, R5, L2, R1, R1, R4, L1, R2, L3, R5, L4, R2, L3, R1, L4, R4, L1, L2, R3, L1, L1, R4, R3, L4, R2, R5, L2, L3, L3, L1, R3, R5, R2, R3, R1, R2, L1, L4, L5, L2, R4, R5, L2, R4, R4, L3, R2, R1, L4, R3, L3, L4, L3, L1, R3, L2, R2, L4, L4, L5, R3, R5, R3, L2, R5, L2, L1, L5, L1, R2, R4, L5, R2, L4, L5, L4, L5, L2, L5, L4, R5, R3, R2, R2, L3, R3, L2, L5".split(', ')

direction = [1, 0]

x = 0
y = 0

def rotate(direction, code):
    if code == 'R':
        if direction == [1, 0]:
            return [0, 1]
        if direction == [0, 1]:
            return [-1, 0]
        if direction == [-1, 0]:
            return [0, -1]
        if direction == [0, -1]:
            return [1, 0]
    if code == 'L':
        if direction == [1, 0]:
            return [0, -1]
        if direction == [0, 1]:
            return [1, 0]
        if direction == [-1, 0]:
            return [0, 1]
        if direction == [0, -1]:
            return [-1, 0]
    raise Exception('Rotation failed for d:%s and c:%s' % (direction, code))

h_traces = []
v_traces = []

def store_trace(x, y, direction, length):
    if direction[0] == 0:
        h_traces.append({'x': x, 'y': y, 'd': direction, 'l': length})
    else:
        v_traces.append({'x': x, 'y': y, 'd': direction, 'l': length})

def get_intersection(x, y, direction, length):
    if direction[0] == 0:
        for trace in v_traces:
            x0 = min(trace['x'], trace['x'] + trace['l'] * trace['d'][0])
            x1 = max(trace['x'], trace['x'] + trace['l'] * trace['d'][0])
            y0 = min(y, y + length * direction[1])
            y1 = max(y, y + length * direction[1])
            if (x0 < x) and (x1 > x) and (y0 < trace['y']) and (y1 > trace['y']):
                print "Intersection! %s, %s" % (x, trace['y'])
    else:
        for trace in h_traces:
            y0 = min(trace['y'], trace['y'] + trace['l'] * trace['d'][1])
            y1 = max(trace['y'], trace['y'] + trace['l'] * trace['d'][1])
            x0 = min(x, x + length * direction[0])
            x1 = max(x, x + length * direction[0])
            if (y0 < y) and (y1 > y) and (x0 < trace['x']) and (x1 > trace['x']):
                print "Intersection! %s, %s" % (trace['x'], y)


#instruction = "R8, R4, R4, R8".split(', ')

for step in instruction:
    code = step[0]
    length = int(step[1:])
    direction = rotate(direction, code)
    get_intersection(x, y, direction, length)
    store_trace(x, y, direction, length)
    x = x + direction[0] * length
    y = y + direction[1] * length
    # print code, length, x, y, abs(x) + abs(y)