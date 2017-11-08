#!/usr/bin/env python

# Generate ideal 2048

from random import randint

def new_item():
	if randint(0, 9) < 9:
		return 2
	return 4

def merge_field(field):
	new_field = []
	while field:
		n = field[0]
		field.remove(n)
		if n in field:
			field.remove(n)
			new_field.append(n*2)
		else:
			new_field.append(n)
	return new_field

def do_step(field):
	new_field = merge_field(field)
	new_field.append(new_item())
	return new_field

def run_field():
	field = [new_item(), new_item()]
	i = 0
	while 2048 not in field:
		i += 1
		field = do_step(field)
	return i

n = 0
sum = 0
while n < 100000:
	sum += run_field()
	n += 1
	print(n, sum/float(n)) 
