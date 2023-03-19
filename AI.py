from MakeBoard import Board

class AI():
    def __init__(self, board) -> None:
        self.obj: Board = board
        self.game_board = self.obj.board

    def run(self):
        """Run the AI."""
        # uncover the starting position 
        startr = self.obj.startr
        startc = self.obj.startc
        self.obj.uncover(startr, startc)

        print(self.obj)

        # loop csp and backtracking until solution is found 
        while not self.obj.has_won():
            # use csp to find squares that are mines
            flaggable = self.get_flaggable()

            # if csp has found everything it can, use backtracking to make a guess
            if not flaggable:
                self.backtrack()
                continue

            # resolve neighbors of the mine 
            for row, col in flaggable:
                print(f"Flagged {row}, {col}")
                neighbors = self.obj.find_neighbors(row, col)
                self.obj.flag_mine(row, col, neighbors)
                self.obj.evaluate_neighbors(row, col, neighbors)
                    
            print(self.obj)

        print("You won!")

    def get_flaggable(self):
        """Finds squares that are mines."""
        vals = set()
        # find squares whose covered neighbors are only mines
        for row in self.game_board:
            for val in row:
                numNeighbors = len(self.obj.find_neighbors(val.r, val.c))
                if val.uncovered and val.number != 0 and val.can_flag(numNeighbors):
                    vals.add((val.r, val.c))

        # add the mines to a set
        flaggable = {neighbor for r,c in vals for neighbor in self.obj.find_neighbors(r,c) if not self.game_board[neighbor[0]][neighbor[1]].uncovered}

        # keep track of the mines that have been found 
        vals = set()
        for val in flaggable:
            if val in self.obj.found_mines:
                vals.add(val)

        for val in vals:
            flaggable.remove(val)
        
        return flaggable

    def backtrack(self):
        """Make guess uncovers until one that is not a mine is found."""
        # guess each uncovered square until we don't find a mine
        for row in self.game_board:
            for val in row:
                if val.uncovered:
                    # if this square is already uncovered, continue
                    continue
                if self.obj.uncover(val.r, val.c):
                    # guess was a mine. re-cover the square and try another one
                    self.obj.cover(val.r, val.c)
                else:
                    # didn't uncover a mine, go back to csp solving
                    print(f"Guessed ({val.r},{val.c})")
                    print(self.obj)
                    return