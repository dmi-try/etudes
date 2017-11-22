#!/usr/bin/env python

# Solution for http://adventofcode.com/2016/

def unpack(data, version=1):
    seek = 0
    text = ''
    while seek < len(data):
        if data[seek] != '(':
            text += data[seek]
            seek += 1
            continue
        x_pos = data.find('x', seek)
        p_pos = data.find(')', x_pos)
        size = int(data[seek + 1: x_pos])
        count = int(data[x_pos + 1: p_pos])
        if version == 1:
            text += data[p_pos + 1: p_pos + 1 + size] * count
        if version == 2:
            text += unpack(data[p_pos + 1: p_pos + 1 + size], 2) * count
        seek = p_pos + size + 1
    return text

def calc_size(data, version=2):
    seek = 0
    text_size = 0
    while seek < len(data):
        if data[seek] != '(':
            text_size += 1
            seek += 1
            continue
        x_pos = data.find('x', seek)
        p_pos = data.find(')', x_pos)
        size = int(data[seek + 1: x_pos])
        count = int(data[x_pos + 1: p_pos])
        if version == 1:
            text_size += size * count
        if version == 2:
            text_size += calc_size(data[p_pos + 1: p_pos + 1 + size], 2) * count
        seek = p_pos + size + 1
    return text_size


sample_data_a = """
ADVENT
A(1x5)BC
(3x3)XYZ
A(2x2)BCD(2x2)EFG
(6x1)(1x3)A
X(8x2)(3x3)ABCY
""".split('\n')[1:-1]

sample_result_a = """
ADVENT
ABBBBBC
XYZXYZXYZ
ABCBCDEFEFG
(1x3)A
X(3x3)ABC(3x3)ABCY
""".split('\n')[1:-1]

sample_sizes_a = [6, 7, 9, 11, 6, 18]


sample_sizes_b = [9, ]

for (data, text, size) in zip(sample_data_a, sample_result_a, sample_sizes_a):
    assert unpack(data) == text
    assert len(unpack(data)) == size

size = 0
with open('advent_2016_9.txt') as fp:  
    line = fp.readline().strip()
    while line and line != '':
        size += len(unpack(line))
        line = fp.readline().strip()

print "Size of unpacked data (a) is", size

assert unpack("(3x3)XYZ", 2) == "XYZXYZXYZ"
assert unpack("X(8x2)(3x3)ABCY", 2) == "XABCABCABCABCABCABCY"
assert len(unpack("(27x12)(20x12)(13x14)(7x10)(1x12)A", 2)) == 241920
assert len(unpack("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN", 2)) == 445

size = 0
with open('advent_2016_9.txt') as fp:  
    line = fp.readline().strip()
    while line and line != '':
        size += calc_size(line, 2)
        line = fp.readline().strip()
print "Size of unpacked data (b) is", size
