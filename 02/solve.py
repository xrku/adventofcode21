#!/usr/bin/env

from collections import defaultdict

file = 'input.txt'

## Part 1 (since the order of the commands is irrelevant, we can use this hacky solution)

dd = defaultdict(list)
with open(file, 'r') as f:
    [(dd[key].append(int(value.strip()))) for key, value in [line.split(' ') for line in f.readlines()]]

print(f'Part One: {(sum(dd["forward"])*(sum(dd["down"]) - sum(dd["up"])))}')

## Part 2

with open(file, 'r') as f:
    data = [(cmd, int(value.strip())) for cmd, value in [line.split(' ') for line in f.readlines()]]

d,h,a = 0,0,0

for c, v in data:
    if c == 'forward':
        d += (v*a)
        h += v
    elif c == 'down':
        a += v
    else:
        a -= v

print(f'Part Two: {d*h}')