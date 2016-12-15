#!/usr/bin/env python

import logging


def get_num_of_stars(arr):
    weights = map(lambda x: [0, 25, 50, 75, 100][x - 1], arr)
    logging.debug(weights)
    return sum(weights)/20.0/len(weights)


logging.basicConfig(level=logging.DEBUG)

print get_num_of_stars([1, 2, 3, 4, 5, 4, 3, 2, 1])
