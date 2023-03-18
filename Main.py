import MakeBoard as m
import numpy as np

def main():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    mines = int(input("Enter number of mines: "))


    startr = rows // 2
    startc = cols // 2

    gameBoard = m.makeBoard(rows, cols, mines, startr, startc)
    revealed_board = np.asarray([[(gameBoard[j][i].number if gameBoard[j][i].number != -1 else '*') for i in range(cols)] for j in range(rows)])

    uncover(startr, startc, gameBoard)

    print(revealed_board)
    m.print_board(gameBoard)

    while True:
        if sum((1 for row in gameBoard for x in row if not x.uncovered)) == mines:
            break

        val = input("g for guess, f for flag: ")


        row = int(input("Enter row: "))
        col = int(input("Enter column: "))

        neighbors = findNeighbors(row, col, gameBoard)

        if val == "g":
            if uncover(row, col, gameBoard):
                m.print_board(gameBoard)
                print("Hit a mine")
            return
        else:
            gameBoard[row][col].uncovered == True
            flagMine(row, col, gameBoard, neighbors)
            evaluateNeighbors(row, col, gameBoard, neighbors)
        
        m.print_board(gameBoard)
        print()

    m.print_board(gameBoard)
    print("Congrats!")

def uncover(row, col, gameBoard):
    val = gameBoard[row][col].number
    
    if gameBoard[row][col].uncovered:
        return

    if val == -1:
        return True
    
    gameBoard[row][col].uncovered = True

    if val == 0:
        neighbors = findNeighbors(row, col, gameBoard)
        uncover_neighbors(gameBoard, neighbors)

def uncover_neighbors(gameBoard, neighbors):

    for row, col in neighbors:
        uncover(row, col, gameBoard)

def findNeighbors(r, c, gameBoard):
    rows = len(gameBoard)
    cols = len(gameBoard[0])

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

def flagMine(r, c, gameBoard, neighbors):
    for nrow,ncol in neighbors:
        gameBoard[nrow][ncol].neighbor_mines.append(gameBoard[r][c])
        
def evaluateNeighbors(r,c, gameBoard, neighbors):
    for nrow,ncol in neighbors:
        square = gameBoard[nrow][ncol]
        if square.uncovered and square.number == len(square.neighbor_mines):
            neighborsEval = findNeighbors(nrow, ncol, gameBoard)
            neighborsEval.remove((r,c))
            uncover_neighbors(gameBoard, neighborsEval)

    




if __name__ == "__main__":
    main()