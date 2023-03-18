from MakeBoard import Board



class AI():
    def __init__(self, board) -> None:
        self.obj: Board = board
        self.game_board = self.obj.board

    def run(self):

        startr = self.obj.startr
        startc = self.obj.startc

        self.obj.uncover(startr, startc)

        print(self.obj)

        while not self.obj.hasWon():
            flaggable = self.getFlaggable()

            if not flaggable:
                print(self.obj)
                print("Need backtracking search")
                return


            for row, col in flaggable:
                neighbors = self.obj.findNeighbors(row, col)
                self.obj.flagMine(row, col, neighbors)
                self.obj.evaluateNeighbors(row, col, neighbors)




            print(self.obj)

        print("You won!")

    def getFlaggable(self):
        vals = set()
        for row in self.game_board:
            for val in row:
                numNeighbors = len(self.obj.findNeighbors(val.r, val.c))
                if val.uncovered and val.number != 0 and val.safe_to_uncover_neighbors(numNeighbors):
                    vals.add((val.r, val.c))

        flaggable = {neighbor for r,c in vals for neighbor in self.obj.findNeighbors(r,c) if not self.game_board[neighbor[0]][neighbor[1]].uncovered}
                    

        return flaggable

    
    




if __name__ == "__main__":
    rows = 5
    cols = 5
    mines = 5
    board = Board(rows, cols, mines, rows // 2, cols // 2)
    ai = AI(board)
    ai.run()