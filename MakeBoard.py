from numpy import zeros
from random import randint

def makeBoard(rows, cols, mines):
    board = zeros((rows, cols), int)

    for _ in range(0, mines):
        # find a space that isn't already a mine
        m = (randint(0, rows-1), randint(0, cols-1))
        while board[m[0]][m[1]] == -1:
            m = (randint(0, rows-1), randint(0, cols-1))

        r = m[0]
        c = m[1]

        # add the mine and increment its neighbors
        board[r][c] = -1
        if r > 0:
            board[r-1][c] += 1 if board[r-1][c] != -1 else 0
            if c > 0:
                board[r-1][c-1] += 1 if board[r-1][c-1] != -1 else 0
            if c < cols - 1:
                board[r-1][c+1] += 1 if board[r-1][c+1] != -1 else 0
        if c > 0:
            board[r][c-1] += 1 if board[r][c-1] != -1 else 0
        if c < cols - 1:
            board[r][c+1] += 1 if board[r][c+1] != -1 else 0
        if r < rows - 1:
            board[r+1][c] += 1 if board[r+1][c] != -1 else 0
            if c > 0:
                board[r+1][c-1] += 1 if board[r+1][c-1] != -1 else 0
            if c < cols - 1:
                board[r+1][c+1] += 1 if board[r+1][c+1] != -1 else 0

    return board
