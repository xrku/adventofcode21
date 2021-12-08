#!/usr/bin/env python3

with open('input.txt', 'r') as f:
    data = list(map(int, f.readline().split(',')))

# Part 1:
gas = []
for i in range(1, max(data)):
    gas.append(0)
    for value in data:
        if value == i:
            continue
        gas[i-1]+=(max(value,i)-min(value,i))

print(min(gas))

# Part 2:
gas = []
for i in range(1, max(data)):
    gas.append(0)
    for value in data:
        if value == i:
            continue
        gas[i-1]+=(sum(range(max(value,i)-min(value,i)+1)))

print(min(gas))