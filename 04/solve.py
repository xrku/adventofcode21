#!/usr/bin/env python3

import copy

class Board():
    
    def __init__(self, arr):
        self.pos = {}
        self.pool = self.create_board(arr)
        self.bingo = {
            'row': [0,0,0,0,0],
            'col': [0,0,0,0,0]
        }
        self.last = -1
        self.finished = False

    def create_board(self, arr):
        board = []
        for rows in arr:
            row = [int(a) for a in rows.split(' ') if a.strip() != '']
            board.append(row)

        for x in range(5):
            for y in range(5):
                self.pos[board[x][y]] = (x,y)
        
        return board

    def update(self, number):
        if number in self.pos:
            x,y = self.pos[number]
            self.bingo['row'][x]+=1
            self.bingo['col'][y]+=1
            self.pool[x][y] = -1
            self.last = number
        self.finished = 5 in self.bingo['row'] or 5 in self.bingo['col']
        return self.finished
    
    def calc_unmarked(self):
        return sum([row for rows in self.pool for row in rows if row > -1])

with open('input.txt', 'r') as f:
    numbers = [int(n.strip()) for n in f.readline().split(',')]
    lines = [l for line in f.readlines() for l in line.split('\n') if l.strip('\n') != '']

boards = []
for i in range(0, len(lines), 5):
    boards.append(Board(lines[i:i+5]))

## Part 1
def play2win(boards):
    for number in numbers:
        for board in boards:
            if board.update(number):
                return number * board.calc_unmarked()

b = copy.deepcopy(boards)
print(f'Part 1: {play2win(b)}')

## Part 2
def play2lose(boards):
    last_board=None
    for number in numbers:
        for board in boards:
            if board.finished:
                continue
            if board.update(number):
                last_board = board

    return last_board.last * last_board.calc_unmarked()

print(f'Part 2: {play2lose(boards)}')
