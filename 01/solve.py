#!/usr/bin/env python3

with open('input.txt', 'r') as f:
    data = list(map(int, f.readlines()))

## Part 1
print(sum([x < y for x,y in zip(data, data[1:])]))

## Part 2
x = list(zip(data, data[1:], data[2:]))
print(sum([(sum(x0) < sum(x1)) for x0,x1 in list(zip(x, x[1:]))]))