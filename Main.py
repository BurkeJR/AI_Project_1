import MakeBoard as m

def main():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    mines = int(input("Enter number of mines: "))



    print(m.makeBoard(rows, cols, mines))




if __name__ == "__main__":
    main()