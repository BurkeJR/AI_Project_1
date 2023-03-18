import MakeBoard as m
import numpy as np

def main():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    mines = int(input("Enter number of mines: "))


    gameBoard = m.makeBoard(rows, cols, mines, 0, 0)

    userBoard = np.asarray([["_" for i in range(cols)] for j in range(rows)])

    mark(0, 0, userBoard, gameBoard)

    print(userBoard)

    while True:
        if sum((1 for row in userBoard for x in row if x == '_')) == mines:
            break
        row = int(input("Enter guessing row: "))
        col = int(input("Enter guessing column: "))
        if mark(row, col, userBoard, gameBoard):
            print(userBoard)
            print("Hit a mine")
            userBoard[row][col] = '*'
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