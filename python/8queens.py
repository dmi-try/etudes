#!/usr/bin/env python

# https://en.wikipedia.org/wiki/Eight_queens_puzzle

import copy
import logging

class State:
    def __init__(self, n):
        assert n > 0
        self.n = n
        self.rows = [] # Position in each row, [0, 0] is upper left
        self.cols = [0] * n
        self.slash_diag = [0] * (2 * n - 1) # 0 is upper left
        self.back_diag = [0] * (2 * n - 1) # 0 is lower left

    def put(self, col):
        row = len(self.rows)
        assert row < self.n
        assert col < self.n
        slash_diag = row + col
        back_diag = self.n - 1 - row + col
        assert self.cols[col] == 0
        assert self.slash_diag[slash_diag] == 0
        assert self.back_diag[back_diag] == 0
        self.rows.append(col)
        self.cols[col] = 1
        self.slash_diag[slash_diag] = 1
        self.back_diag[back_diag] = 1
        return self.get_options(row + 1)

    def get_threats(self, row):
        assert row < self.n
        threats = [self.cols[col] or self.slash_diag[col + row] or self.back_diag[self.n - 1 - row + col] for col in xrange(self.n)]
        return threats

    def get_options(self, row=None):
        if row is None:
            row = len(self.rows)
        if row == self.n:
            return 'Solved!'
        threats = self.get_threats(row)
        opts = []
        for i in xrange(self.n):
            if threats[i] == 0:
                opts.append(i)
        return opts

    def get_field(self):
        matrix = [] # [row, col]
        for i in self.rows:
            cols = [0] * self.n
            cols[i] = 1
            matrix.append(cols)
        return matrix

    def print_field(self):
        matrix = self.get_field()
        for i in matrix:
            print i

def count_solutions(n):
    states_stack = [State(n)]
    options_stack = [states_stack[0].get_options()]
    # solutions = []
    solutions_count = 0
    while states_stack:
        logging.debug('Working with %s' % options_stack[-1])
        if not options_stack[-1]:
            logging.debug('Going back')
            states_stack.pop()
            options_stack.pop()
        else:
            pos = options_stack[-1].pop(0)
            new_state = copy.deepcopy(states_stack[-1])
            new_options = new_state.put(pos)
            if new_options == 'Solved!':
                logging.debug('Found solution')
                print "Solved:"
                new_state.print_field()
                # solutions.append(new_state)
                solutions_count += 1
            elif new_options:
                options_stack.append(new_options)
                states_stack.append(new_state)
    return solutions_count

logging.basicConfig(level=logging.INFO)
state = State(5)                        
assert state.get_options() == [0, 1, 2, 3, 4] # 1 0 0 0 0
assert state.put(0) ==        [      2, 3, 4] # 0 0 0 0 1
assert state.put(4) ==        [   1         ] # 0 1 0 0 0
assert state.put(1) ==        [             ] # No more option

assert state.get_threats(1) == [1, 1, 1, 0, 1] # We ignore queen on the same row

assert [count_solutions(n) for n in xrange(1, 11)] == [1, 0, 0, 2, 10, 4, 40, 92, 352, 724]
