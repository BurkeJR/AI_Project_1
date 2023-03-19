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

    #Grid must be larger than 3x3
    if rows < 4 or cols < 4:
        print("Please ensure both number of rows and number of columns is greater than 3.\n")
        main()
    
    #Mines must be less than number of squares
    if mines > (rows * cols) - 9:
        print("Too many mines, please ensure mines is less than size of grid\n")
        main()

    board = Board(rows, cols, mines, rows // 2, cols // 2)
    ai = AI(board)
    ai.run()



if __name__ == "__main__":
    main()