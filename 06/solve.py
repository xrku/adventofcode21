#!/usr/bin/env python3

with open('input.txt', 'r') as f:
    init = list(map(int, f.readline().split(',')))

## Part 1 & 2:

buffer = 0
fish = [0,0,0,0,0,0,0,0,0]
for i in init:
    fish[i]+=1

for day in range(256):
    for i in range(len(fish)):
        if i == 0:
            buffer = fish[i]
        if i != 8:
            fish[i] = fish[i+1]
    fish[6] += buffer
    fish[8] = buffer

    if day == 79:
        print(f'Part 1: {sum(fish)}')

print(f'Part 2: {sum(fish)}')