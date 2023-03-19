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
    board.uncover(startr, startc)
    
    print(board)

    while not board.has_won():

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