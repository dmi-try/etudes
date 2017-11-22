#!/usr/bin/env python

# Solution for http://adventofcode.com/2016/

from hashlib import md5
from sys import stdout

sample_data = 'abc'
sample_data_result_a = '18f47a30'
sample_data_result_b = '05ace8e3'

real_data = 'ojvtpuvg'

num_of_digits = 8

def crack_password_a(data):
    password = ['_'] * num_of_digits
    i = 0
    while True:
        stdout.write('\r' + str(i))
        digest = md5(data + str(i)).hexdigest()
        if digest.startswith('00000'):
            print ":", digest
            password[password.index('_')] = digest[5]
            print password
            if '_' not in password:
                break
        i += 1
    return "".join(password)

def crack_password_b(data):
    password = ['_'] * num_of_digits
    i = 0
    while True:
        stdout.write('\r' + str(i))
        digest = md5(data + str(i)).hexdigest()
        if digest.startswith('00000'):
            print ":", digest
            position = int(digest[5], 16)
            if position < len(password):
                if password[position] == '_':
                    password[position] = digest[6]
                    print password
                    if '_' not in password:
                        break
        i += 1
    return "".join(password)


print "Solving puzzle (a) on sample data. Expecting to get", sample_data_result_a
assert crack_password_a(sample_data), sample_data_result_a
print "Solving puzzle (a) on real data"
print "Solved! Result is", crack_password_a(real_data)
print "Solving puzzle (b) on sample data. Expecting to get", sample_data_result_b
assert crack_password_b(sample_data), sample_data_result_b
print "Solving puzzle (b) on real data"
print "Solved! Result is", crack_password_b(real_data)

