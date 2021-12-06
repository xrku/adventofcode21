#!/usr/bin/env python3

from collections import defaultdict

overlap = 0
overlap2 = 0
coords = defaultdict(int)
coords2 = defaultdict(int)

with open('input.txt', 'r') as f:
    lines = f.readlines()

for line in lines:
    c1, c2 = line.split(' -> ')
    c1 = tuple(map(int, c1.split(',')))
    c2 = tuple(map(int, c2.split(','))) 
    c1, c2 = sorted([c1, c2])

    if (c1[0] == c2[0]) or (c1[1] == c2[1]):    
        for x in range(c1[0], c2[0]+1):   
            for y in range(c1[1], c2[1]+1):
                coords[(x,y)]+=1
                coords2[(x,y)]+=1
                if coords[(x,y)] == 2:
                    overlap+=1
                if coords2[(x,y)] == 2:
                    overlap2+=1
    else:
        slope = int((c2[1]-c1[1])/(c2[0]-c1[0]))
        y = c1[1]
        for x in range(c1[0], c2[0]+1):
            coords2[(x,y)]+=1
            if coords2[(x,y)] == 2:
                overlap2+=1
            y+=slope

print(f'Part 1: {overlap}')
print(f'Part 2: {overlap2}')