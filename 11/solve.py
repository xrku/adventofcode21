#!/usr/bin/env python3

from collections import defaultdict

lvls = defaultdict(list)

with open('input.txt', 'r') as f:
    [lvls[i].append(int(lvl)) for i, lines in enumerate(f.readlines()) for lvl in lines.strip()]
            
ymax = len(lvls)
xmax = len(lvls[0])
count=0
i = 1
max = 99
part_one = True

def find_adjacent(flashes):
    adjacent = defaultdict(int)
    for y,x in flashes:

        if y-1 >= 0 and (y-1,x) not in skip:
            adjacent[(y-1,x)]+=1
        if y+1 < ymax and (y+1,x) not in skip:
            adjacent[(y+1,x)]+=1
        if x-1 >= 0 and (y,x-1) not in skip:
            adjacent[(y,x-1)]+=1
        if x+1 < xmax and (y,x+1) not in skip:
            adjacent[(y,x+1)]+=1
        
        if x-1 >= 0 and y-1 >= 0 and (y-1,x-1) not in skip:
            adjacent[(y-1,x-1)]+=1
        if x-1 >= 0 and y+1 < ymax and (y+1,x-1) not in skip:
            adjacent[(y+1,x-1)]+=1
        if x+1 < xmax and y-1 >= 0 and (y-1,x+1) not in skip:
            adjacent[(y-1,x+1)]+=1
        if x+1 < xmax and y+1 < ymax and (y+1,x+1) not in skip:
            adjacent[(y+1,x+1)]+=1
    
    return adjacent

while True:

    skip = []
    flashes = [(y,x) for y in lvls for x,_ in enumerate(lvls[y]) if lvls[y][x] >= 9]

    while(len(flashes) > 0):
        flashes = [(y,x) for y in lvls for x,_ in enumerate(lvls[y]) if lvls[y][x] >= 9]
        adjacent = find_adjacent(flashes)

        for k in adjacent:
            if k not in flashes:
                y,x = k
                lvls[y][x]+=adjacent[k]

        for y,x in flashes:
            skip.append((y,x))
            lvls[y][x] = 0
            count+=1
        
        flashes = [(y,x) for y in lvls for x,_ in enumerate(lvls[y]) if lvls[y][x] >= 9]

    for y,x in [(y,x) for y in lvls for x,_ in enumerate(lvls[y]) if (y,x) not in skip]:
        lvls[y][x]+=1
    
    if sum([sum(lvls[i]) for i in lvls]) == 0:
        print(f'Part 2: {i}')
        break
    if i > max and part_one:
        print(f'Part 1: {count}')
        part_one = False
    i+=1



