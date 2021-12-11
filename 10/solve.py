#!/usr/bin/env python3

with open('input.txt', 'r') as f:
    lines = f.readlines()

chars = {
    '(':(')', 3, 1),
    '[':(']', 57, 2),
    '{':('}', 1197, 3),
    '<':('>', 25137, 4),
}

## Part 1
points = 0
incomplete=[]
for line in lines:
    chunks = []
    for char in line.strip():
        if char in chars.keys():
            chunks.append(char)
        else:
            if chars[chunks[-1]][0] == char:
                del chunks[-1]
            else:
                points+=[chars[x][1] for x in chars if chars[x][0] == char][0]
                incomplete.append(line)
                break

print(f'Part 1: {points}')

## Part 2
scores=[]
for line in [line.strip() for line in lines if line not in incomplete]:
    chunks = []
    for i,char in enumerate(line.strip()):
        if char in chars.keys():
            chunks.append(char)
        else:
            if chars[chunks[-1]][0] == char:
                del chunks[-1]
            else:
                import pdb; pdb.set_trace()
    
        if i == len(line.strip())-1:
            points=0
            for char in reversed(chunks):
                points*=5
                points+=chars[char][2]
            scores.append(points)

print(f'Part 2: {sorted(scores)[int((len(scores))/2)]}')