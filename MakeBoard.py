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

def makeBoard(rows, cols, mines):
    board = [[Square(r, c, 0) for r in range(rows)] for c in range(cols)]

    for _ in range(0, mines):
        # find a space that isn't already a mine
        m = (randint(0, rows-1), randint(0, cols-1))
        while board[m[0]][m[1]].number == -1:

        r = m[0]
        c = m[1]

        
        # add the mine and increment its neighbors
        board[r][c] = -1

        neighbors = Main.findNeighbors(r,c, rows, cols)
        for row, col in neighbors:
            board[row][col] += 1 if board[row][col] != -1 else 0
        board[r][c].number = -1
        if r > 0:
            board[r-1][c].number += 1 if board[r-1][c].number != -1 else 0
            if c > 0:
                board[r-1][c-1].number += 1 if board[r-1][c-1].number != -1 else 0
            if c < cols - 1:
                board[r-1][c+1].number += 1 if board[r-1][c+1].number != -1 else 0
        if c > 0:
            board[r][c-1].number += 1 if board[r][c-1].number != -1 else 0
        if c < cols - 1:
            board[r][c+1].number += 1 if board[r][c+1].number != -1 else 0
        if r < rows - 1:
            board[r+1][c].number += 1 if board[r+1][c].number != -1 else 0
            if c > 0:
                board[r+1][c-1].number += 1 if board[r+1][c-1].number != -1 else 0
            if c < cols - 1:
                board[r+1][c+1].number += 1 if board[r+1][c+1].number != -1 else 0

    return board

b = makeBoard(5, 5, 5)

for r in range(len(b)):
    s = ""
    for c in range(len(b[r])):
        s += f"{b[r][c].number} "
    print(s)