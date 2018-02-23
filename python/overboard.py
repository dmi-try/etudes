#!/usr/bin/env python
# -*- coding: utf-8 -*-

# На судне находится 20 человек, между ними один негр. Вследствие недостатка в
# продовольствии один из команды должен быть выброшен за борт. Решено
# отсчитывать по семи и каждого седьмого освобождать; дойдя до конца ряда,
# переходить к его началу, не прерывая счёта. Оставшийся последним должен
# умереть. Негр (обозначенный перевернутой спичкой) может стать на любое место
# в ряду. С кого следует начинать счёт, чтобы негр оставался всегда последним?


def pos_of_killed(total, start, step, visualisate=False):
    pool = range(total)
    if visualisate:
        print pool
    pos = start
    while len(pool) > 1:
        pos = (pos + step - 1) % len(pool)
        del pool[pos]
        if visualisate:
            print pool
    return pool[0]


def should_start_from(total, start, step, pos_of_black):
    offset = pos_of_killed(total, start, step)
    good_start = (pos_of_black - offset) % total
    print "Black is at position %d" % pos_of_black
    print "We should start from %d" % good_start
    pos_of_killed(total, good_start, step, True)
    return good_start


assert should_start_from(20, 0, 7, 7) == 5
