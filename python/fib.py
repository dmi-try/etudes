#!/usr/bin/env python

def fib(x):
    if type(x) != 'int':
        raise "Integer required"
    if x < 0:
        raise "Negative values are not allowed"
    if x in [0, 1]:
        return 1
    return fib(x - 1) + fib(x - 2)

def iter_fib(x):
    prev = [0, 0]
    for i in xrange(0, x):
        if i == 0:
            val = 1
        else:
            val = sum(prev)
        print i, val
        prev = [prev[1], val]

def iter_pas_tr(x):
    for i in xrange(x):
        if i == 0:
            val = [1]
            prev = [1]
        else:
            v1 = [0] + prev
            v2 = prev + [0]
            val = v1
            for j in xrange(len(prev) + 1):
                val[j] = v1[j] + v2[j]
            prev = val
        print i, val

iter_fib(40)
iter_pas_tr(15)
