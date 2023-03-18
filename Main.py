import MakeBoard as m
import numpy as np

def main():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    mines = int(input("Enter number of mines: "))


    gameBoard = m.makeBoard(rows, cols, mines)
    print(gameBoard)

    userBoard = np.asarray([["_" for i in range(cols)] for j in range(rows)])

    while True:
        if sum((1 for row in userBoard for x in row if x == '_')) == mines:
            break
        row = int(input("Enter guessing row: "))
        col = int(input("Enter guessing column: "))
        mark(row, col, userBoard, gameBoard)
        print(userBoard)


    print(userBoard)
    print("Congrats!")

def mark(row, col, board, gameBoard):
    val = gameBoard[row][col]
    
    if board[row][col] != '_':
        return

    if val == -1:
        print("Game Over")
        board[row][col] = '*'
        print(board)
        exit()
    board[row][col] = val

    if val == 0:
        markNeighbors(row, col, board, gameBoard)

def markNeighbors(r, c, board, gameBoard):
    rows = len(board)
    cols = len(board[0])

    if r > 0:
        mark(r-1, c, board, gameBoard)
        if c > 0:
            mark(r-1, c-1, board, gameBoard)
        if c < cols - 1:
            mark(r - 1, c + 1, board, gameBoard)
    if c > 0:
        mark(r, c - 1, board, gameBoard)
    if c < cols - 1:
        mark(r, c + 1, board, gameBoard)
    if r < rows - 1:
        mark(r + 1, c, board, gameBoard)
        if c > 0:
            mark(r + 1, c - 1, board, gameBoard)
        if c < cols - 1:
            mark(r + 1, c + 1, board, gameBoard)

    




if __name__ == "__main__":
    main()