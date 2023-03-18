from numpy import zeros
from random import randint
import Main

class Square():
    def __init__(self, r, c, number, uncovered=False):
        self.r = r
        self.c = c
        self.number = number
        self.uncovered = uncovered
        self.neighbor_mines = []

    def safe_to_uncover_neighbors(self):
        return self.number == len(self.neighbor_mines)
    
    def __str__(self, reveal=False):
        if not self.uncovered or not reveal:
            return '_'
        if self.number == -1:
            return '*'
        return str(self.number)
    
    def __repr__(self):
        if not self.uncovered:
            return '_'
        if self.number == -1:
            return '*'
        return str(self.number)
    
    def add_neighbor_to_mine_list(self, r, c):
        if (r, c) in self.neighbor_mines:
            # this neighbor is already in the list
            return
        self.neighbor_mines.append((r, c))



def makeBoard(rows, cols, mines, startr, startc):
    board = [[Square(r, c, 0) for r in range(rows)] for c in range(cols)]

    startingPointNeighbors = Main.findNeighbors(startr, startc, rows, cols)
    startingPointNeighbors.append((startr,startc))

    for _ in range(0, mines):
        # find a space that isn't already a mine
        m = (randint(0, rows-1), randint(0, cols-1))
        while board[m[0]][m[1]].number == -1 or m in startingPointNeighbors:
            m = (randint(0, rows-1), randint(0, cols-1))
        
        r = m[0]
        c = m[1]


        board[r][c].number = -1

        neighbors = Main.findNeighbors(r,c, rows, cols)
        for row, col in neighbors:
            board[row][col].number += 1 if board[row][col].number != -1 else 0

    return board



def print_board(board):
    for row in board:
        print(row)