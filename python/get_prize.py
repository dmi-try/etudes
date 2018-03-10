#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Симуляция выбора одной из трёх шкатулок, когда приз в одной из них.
# При выборе ведущий не открывает выбранную, а показывает, в которой
# из оставшихся ничего нет, и предлагает поменять свой выбор. Идея
# в том, что при смене выбора шансы на успех 2/3, то есть возрастают
# в два раза по сравнению с изначальными 1/3.


import logging
import random


class Game:
    def __init__(self, n=3):
        self.wins = 0
        self.loses = 0
        self.boxes_number = n

    def play_round(self, player_func):
        self.prepare_boxes()
        logging.debug("Round start: %s" % self.boxes)
        player_choice = player_func(self)
        logging.debug("Final choice: %d" % player_choice)
        if self.boxes[player_choice] == 'prize':
            self.wins += 1
        else:
            self.loses += 1

    def prepare_boxes(self):
        winning_box = random.randint(1, self.boxes_number)
        self.boxes = {n: 'empty' for n in xrange(1, self.boxes_number + 1)}
        self.boxes[winning_box] = 'prize'

    def ping_choice(self, n):
        logging.debug("First choice: %d" % n)
        other_empty_boxes = [k for k, v in self.boxes.items() if v != 'prize' and k != n]
        box_to_remove = random.choice(other_empty_boxes)
        del self.boxes[box_to_remove]
        return self.box_numbers

    @property
    def box_numbers(self):
        return self.boxes.keys()


def choose_box_wisely(game):
    my_choice = random.choice(game.box_numbers)
    box_numbers = game.ping_choice(my_choice)
    box_numbers.remove(my_choice)
    my_choice = random.choice(box_numbers)
    return my_choice


def choose_box_firmly(game):
    my_choice = random.choice(game.box_numbers)
    return my_choice

logging.basicConfig(level=logging.INFO)

n = 10000
logging.info("Playing %d rounds with firm strategy" % n)
game = Game()
for i in xrange(n):
    game.play_round(choose_box_firmly)
logging.info("Wins: %d, Loses: %d" % (game.wins, game.loses))
assert game.wins * 1.9 < game.loses

logging.info("Playing %d rounds with wise strategy" % n)
game = Game()
for i in xrange(n):
    game.play_round(choose_box_wisely)
logging.info("Wins: %d, Loses: %d" % (game.wins, game.loses))
assert game.wins > game.loses * 1.9
