import AI
from MakeBoard import Board

#Run Game from here
def main():
    rows = 8
    cols = 8
    mines = 12
    board = Board(rows, cols, mines, rows // 2, cols // 2)
    ai = AI(board)
    ai.run()



if __name__ == "__main__":
    main()