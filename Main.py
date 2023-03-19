from MakeBoard import Board
import numpy as np

def main():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    mines = int(input("Enter number of mines: "))

    startr = rows // 2
    startc = cols // 2

    board = Board(rows, cols, mines, startr, startc)
    game_board = board.board
    revealed_board = np.asarray([[(game_board[j][i].number if game_board[j][i].number != -1 else '*') for i in range(cols)] for j in range(rows)])

    board.uncover(startr, startc)

    print(revealed_board)
    print(board)

    while True:
        if sum((1 for row in game_board for x in row if not x.uncovered)) == mines:
            break

        val = input("g for guess, f for flag: ")

        row = int(input("Enter row: "))
        col = int(input("Enter column: "))

        neighbors = board.find_neighbors(row, col)

        if val == "g":
            if board.uncover(row, col):
                print(board)
                print("Hit a mine")
                return
        else:
            game_board[row][col].uncovered == True
            board.flag_mine(row, col, neighbors)
            board.evaluate_neighbors(row, col, neighbors)

        print(board)

    print(board)
    print("Congrats!")

if __name__ == "__main__":
    main()