#!/usr/env/bin python3

def array_to_int(arr):
    return int(''.join([str(x) for x in arr]),2)

rate = []
with open('input.txt', 'r') as f:
   [rate.append(list(map(int, line.strip()))) for line in f.readlines()]

## Part 1
zipped = list(zip(*rate))
block = [max(x, key=x.count) for x in zipped]
gamma = array_to_int(block)
epsilon = int(bin(gamma ^ int('1'*len(block),2)),2)
print(f'Part 1: {gamma*epsilon}')

## Part 2
def find_max(input, mode):
    ma = max(input, key=input.count)
    mi = min(input, key=input.count)
    if mode == 1:
        if ma == mi:
            return 1
        return ma
    else:
        if ma == mi:
            return 0
        return mi

def iterate(arr, mode):
    pos = 0
    while len(arr) != 1:
        ref = find_max(list(zip(*arr))[pos], mode)
        arr = [block for block in arr if block[pos] == ref]
        pos+=1
    return array_to_int(arr[0])

oxygen = iterate(rate, 1)
scrubber = iterate(rate, 0)
print(f'Part 2: {oxygen*scrubber}')