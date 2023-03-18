from numpy import zeros
from random import randint
import Main

def makeBoard(self, rows, cols, mines):
    board = zeros((rows, cols), int)

    for _ in range(0, mines):
        # find a space that isn't already a mine
        m = (randint(0, rows-1), randint(0, cols-1))

        while board[m[0]][m[1]] == -1 or (m[0],m[1]):
            m = (randint(0, rows-1), randint(0, cols-1))

        r = m[0]
        c = m[1]

        
        # add the mine and increment its neighbors
        board[r][c] = -1

        neighbors = Main.findNeighbors(r,c, rows, cols)
        for row, col in neighbors:
            board[row][col] if board[row][col] != -1 else 0

    return board
