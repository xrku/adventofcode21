#!/usr/bin/env python3
from collections import defaultdict
from math import prod

with open('input.txt', 'r') as f:
    lines = f.readlines()

heightmap=[]
for i, line in enumerate(lines):
    heightmap.append([])
    for val in line.strip():
        heightmap[i].append(int(val))

## Part 1:
risk = 0
for x,row in enumerate(heightmap):
    for y, val in enumerate(row):
        if ((y-1 >= 0) and (row[y-1] <= val) or
        (y+1 < len(row)) and (row[y+1] <= val) or
        (x-1 >= 0) and (heightmap[x-1][y] <= val) or
        (x+1 < len(heightmap)) and (heightmap[x+1][y] <= val)):
            continue

        risk+=(val+1)

print(f'Part 1: {risk}')


## Part 2:
basins = defaultdict(int)

def check(heightmap, x, y):
    row = heightmap[x]
    basins[(x,y)]=1
    size=1
    if (y-1 >= 0) and (basins[(x,y-1)] == 0) and (row[y-1] < 9):
        basins[(x,y-1)]=1
        size+=check(heightmap,x,y-1)
    if (y+1 < len(row)) and (basins[(x,y+1)] == 0) and (row[y+1] < 9):
        basins[(x,y+1)]=1
        size+=check(heightmap,x,y+1)
    if (x-1 >= 0) and (basins[(x-1,y)] == 0) and (heightmap[x-1][y] < 9):
        basins[(x-1,y)]=1
        size+=check(heightmap,x-1,y)
    if (x+1 < len(heightmap)) and (basins[(x+1,y)] == 0) and (heightmap[x+1][y] < 9):
        basins[(x+1,y)]=1
        size+=check(heightmap,x+1,y)
    
    return size


values = []
for x,row in enumerate(heightmap):
    for y, val in enumerate(row):
        if val == 9 or basins[(x,y)] == 1:
            continue
        values.append(check(heightmap, x, y))

print(f'Part 2: {prod(sorted(values, reverse=True)[:3])}')
        
