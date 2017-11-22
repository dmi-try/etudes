#!/usr/bin/env python

# Solution for http://adventofcode.com/2016/

import logging

sample_data = """
abba[mnop]qrst
abcd[bddb]xyyx
aaaa[qwer]tyui
ioxxoj[asdfgh]zxcvbn
""".split('\n')[1:-1]
sample_results = [True, False, False, True]

def text_has_abba(text):
    if len(text) < 4:
        return False
    for i in xrange(0, len(text) - 3):
        if text[i] != text[i+1] and text[i+1] == text[i+2] and text[i] == text[i+3]:
            return True
    return False

def ip_supports_tls(ip):
    logging.debug("IP: %s" % ip)
    has_abba = False
    is_hyper_section = False
    new_ip = ip.replace(']', '[')
    sections = new_ip.split('[')
    for t in sections:
        logging.debug("Section: %s", t)
        if text_has_abba(t):
            if is_hyper_section:
                logging.debug("Hybernet with ABBA. No TLS")
                return False
            logging.debug("ABBA")
            has_abba = True
        is_hyper_section = not is_hyper_section
    logging.debug("Decision: %s" % has_abba)
    return has_abba

logging.basicConfig(level=logging.DEBUG)

for (ip, result) in zip(sample_data, sample_results):
    assert ip_supports_tls(ip) == result, "For %s result should be %s" % (ip, result)

count = 0
with open('advent_2016_7.txt') as fp:  
    line = fp.readline().strip()
    while line and line != '':
        if ip_supports_tls(line):
            count += 1
        line = fp.readline().strip()

print "Number of IPs with TLS:", count