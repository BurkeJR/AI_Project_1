import MakeBoard as m
import numpy as np

def main():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    mines = int(input("Enter number of mines: "))


    startr = rows // 2
    startc = cols // 2

    gameBoard = m.makeBoard(rows, cols, mines, startr, startc)

    userBoard = np.asarray([["_" for i in range(cols)] for j in range(rows)])

    mark(startr, startc, userBoard, gameBoard)

    print(userBoard)

    while True:
        if sum((1 for row in userBoard for x in row if x == '_')) == mines:
            break
        row = int(input("Enter guessing row: "))
        col = int(input("Enter guessing column: "))
        if mark(row, col, userBoard, gameBoard):
            userBoard[row][col] = '*'
            print(userBoard)
            print("Hit a mine")
            return
        print(userBoard)


    print(userBoard)
    print("Congrats!")

def mark(row, col, board, gameBoard):
    val = gameBoard[row][col].number
    
    if board[row][col] != '_':
        return

    if val == -1:
        return True
    
    board[row][col] = val

    if val == 0:
        markNeighbors(row, col, board, gameBoard)

def markNeighbors(r, c, board, gameBoard):
    rows = len(board)
    cols = len(board[0])

    neigbhors = findNeighbors(r, c, rows, cols)

    for row, col in neigbhors:
        mark(row, col, board, gameBoard)

def findNeighbors(r, c, rows, cols):
    neighbors = []
    if r > 0:
        neighbors.append((r - 1,c))
        if c > 0:
            neighbors.append((r - 1, c - 1))
        if c < cols - 1:
            neighbors.append((r - 1, c + 1))
    if c > 0:
        neighbors.append((r, c - 1))
    if c < cols - 1:
        neighbors.append((r, c + 1))
    if r < rows - 1:
        neighbors.append((r + 1, c))
        if c > 0:
            neighbors.append((r + 1, c - 1))
        if c < cols - 1:
            neighbors.append((r + 1, c + 1))
    return neighbors
    




if __name__ == "__main__":
    main()