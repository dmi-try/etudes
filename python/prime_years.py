#!/usr/bin/env python

import logging


def get_trial_devision(n):
    result = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            result.append(i)
            n /= i
            i = 2
        else:
            i += 1
    result.append(n)
    logging.debug("trial(%d)=%s", n, result)
    return result


def devisions_to_str(arr):
    powers = []
    while arr:
        i = arr[0]
        n = arr.count(i)
        powers.append((i, n))
        arr = arr[n:]
    logging.debug("Powers=%s", powers)

    before_mul = []
    for i in powers:
        if i[1] == 1:
            before_mul.append(str(i[0]))
        else:
            before_mul.append("%d^%d" % i)

    return " * ".join(before_mul)


logging.basicConfig(level=logging.INFO)
assert get_trial_devision(15) == [3, 5]
assert get_trial_devision(17) == [17]
assert devisions_to_str(get_trial_devision(48)) == "2^4 * 3"
for year in xrange(1986, 2031):
    print "%d = %s" % (year, devisions_to_str(get_trial_devision(year)))
