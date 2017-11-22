#!/usr/bin/env python

# Solution for http://adventofcode.com/2016/

import logging

sample_data = """
aba[bab]xyz
xyx[xyx]xyx
aaa[kek]eke
zazbz[bzb]cdb
""".split('\n')[1:-1]
sample_results = [True, False, True, True]

def iter_aba(text):
    if len(text) < 3:
        return
    for i in xrange(0, len(text) - 2):
        if text[i] != text[i+1] and text[i+2] == text[i]:
            yield text[i:i+3]

def ip_supports_ssl(ip):
    logging.debug("IP: %s" % ip)
    is_hyper_section = False
    new_ip = ip.replace(']', '[')
    sections = new_ip.split('[')
    supernet_sections = []
    hypernet_sections = []
    for t in sections:
        if is_hyper_section:
            hypernet_sections.append(t)
        else:
            supernet_sections.append(t)
        is_hyper_section = not is_hyper_section
    for s in supernet_sections:
        logging.debug("Supernet: %s" % s)
        for t in iter_aba(s):
            logging.debug("Found ABA: %s" % t)
            bab = t[1] + t[0] + t[1]
            for h in hypernet_sections:
                logging.debug("Hypernet: %s" % h)
                if bab in h:
                    logging.debug("Found BAB")
                    return True
    return False

logging.basicConfig(level=logging.DEBUG)

for (ip, result) in zip(sample_data, sample_results):
    assert ip_supports_ssl(ip) == result, "For %s result should be %s" % (ip, result)


count = 0
with open('advent_2016_7.txt') as fp:  
    line = fp.readline().strip()
    while line and line != '':
        if ip_supports_ssl(line):
            count += 1
        line = fp.readline().strip()

print "Number of IPs with SSL:", count