#!/usr/bin/env python

# Implementation of https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm

import logging


def get_max_vote_2(arr):
    """
    Get value that appears at least in n/2 + 1 places in list
    """
    i = 0
    m = 0
    for x in arr:
        if i == 0:
            m = x
            i = 1
        elif m == x:
            i += 1
        else:
            i -= 1
    if arr.count(m) > len(arr) / 2:
        return m
    return None


def get_max_vote_3(arr):
    """
    Get any of values that appears at least in n/3 places in list
    """
    counters = {0: 0, 1: 0}
    for x in arr:
        logging.debug("X=%d, C=%s", x, counters)
        if x in counters.keys():
            counters[x] += 1
            logging.debug("IN, C=%s", counters)
        elif 0 in counters.values():
            zero_key = counters.keys()[counters.values().index(0)]
            del counters[zero_key]
            counters[x] = 1
            logging.debug("Z, C=%s", counters)
        else:
            counters = {k: v - 1 for k, v in counters.items()}
            logging.debug("SUB, C=%s", counters)
    for k in counters.keys():
        if arr.count(k) > len(arr) / 3:
            return k
    return None


logging.basicConfig(level=logging.DEBUG)
assert get_max_vote_2([1, 2, 2, 3, 2, 4, 2, 6]) is None
assert get_max_vote_2([1, 2, 2, 3, 2, 4, 2, 6, 2]) == 2
assert get_max_vote_3([1, 2, 3, 2, 1, 3, 1]) == 1
assert get_max_vote_3([1, 2, 3, 1, 2, 3]) is None
