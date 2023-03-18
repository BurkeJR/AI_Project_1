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

        flaggable = self.getFlaggable()

        print(flaggable)

        for row, col in flaggable:
            self.obj.flagMine(row, col, self.obj.findNeighbors(row, col))

        print(self.obj)

    def getFlaggable(self):
        vals = {(val.r, val.c) for row in self.game_board for val in row if val.uncovered and val.safe_to_uncover_neighbors(len(self.obj.findNeighbors(val.r, val.c)))}
        
        flaggable = set()

        for row, col in vals:
            neighbors = self.obj.findNeighbors(row, col)
            for nrow, ncol in neighbors:
                if not self.game_board[nrow][ncol].uncovered:
                    flaggable.add((nrow, ncol))
                    

        return flaggable

    
    




if __name__ == "__main__":
    rows = 5
    cols = 5
    mines = 5
    board = Board(rows, cols, mines, rows // 2, cols // 2)
    ai = AI(board)
    ai.run()