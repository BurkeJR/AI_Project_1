from AI import AI
from MakeBoard import Board

#Run Game from here
def main():
    #Accounts for non int input
    try:
        rows = int(input("Enter number of rows (must be greater than 3): "))
        cols = int(input("Enter number of columns (must be greater than 3):"))
        mines = int(input("Enter number of mines (must be less than rows * columns): "))
        print("")
    except ValueError:
        print("\nPlease enter integers for rows, columns, and mines.\n")
        main()

    try:
        board = Board(rows, cols, mines, rows // 2, cols // 2)
        ai = AI(board)
        ai.run()
    except ValueError as e:
        print(e)
        main()



if __name__ == "__main__":
    main()