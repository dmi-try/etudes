#!/usr/bin/env python

# Solution for http://adventofcode.com/2016/

import string

rooms_list_sample = """
aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]
""".split('\n')[1:-1]
sample_result = 123 + 987 + 404


def decode_room_name(enc_name, sector_id):
    shift = sector_id % 26
    source = string.ascii_lowercase
    target = source[shift:] + source[:shift]
    return enc_name.translate(string.maketrans(source + '-', target + ' '))

def parse_room_code(room):
    def stats_compare(a, b):
        if a[1] == b[1]:
            return cmp(a[0], b[0])
        return cmp(b[1], a[1])
    checksum = room[room.find('[')+1:-1]
    sector_id = int(room[room.rfind('-')+1:room.find('[')])
    enc_name = room[:room.rfind('-')]
    letters = set(enc_name)
    letters.remove('-')
    stats = map(lambda x: [x, enc_name.count(x)], letters)
    sorted_stats = sorted(stats, cmp=stats_compare)
    real_sum = ''.join(map(lambda x: x[0], sorted_stats[:5]))
    real_name = decode_room_name(enc_name, sector_id)
    return {
      'checksum': checksum,
      'sector_id': sector_id,
      'enc_name': enc_name,
      'real_sum': real_sum,
      'real_name': real_name,
      'sum_ok': real_sum == checksum
    }

sum = 0
for i in rooms_list_sample:
    d = parse_room_code(i)
    if d['sum_ok']:
        sum += d['sector_id']

assert(sum == sample_result)

sum = 0
with open('advent_2016_4.txt') as fp:  
    line = fp.readline().strip()
    while line and line != '':
        d = parse_room_code(line)
        if d['sum_ok']:
            sum += d['sector_id']
            if 'north' in d['real_name']:
                print "Sector %d: %s" % (d['sector_id'], d['real_name'])
        line = fp.readline().strip()

print "Sum of sector IDs is", sum
