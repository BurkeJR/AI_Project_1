from MakeBoard import Board

class AI():
    def __init__(self, board) -> None:
        self.obj = board
        self.game_board = self.obj.board




if __name__ == "__main__":
    rows = 10
    cols = 10
    mines = 18
    board = Board(rows, cols, mines, rows // 2, cols // 2)
    ai = AI(board)