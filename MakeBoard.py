from random import randint

class Square():
    def __init__(self, r, c, number, uncovered=False):
        self.r = r
        self.c = c
        self.number = number
        self.uncovered = uncovered
        self.neighbor_mines = []  # list of neighbors that are mines
        self.uncovered_neighbors = 0

    def can_flag(self, numNeighbors):
        """Return true if the uncovered neighbors of this square are all mines. False, otherwise."""
        return numNeighbors - self.uncovered_neighbors == self.number

    def add_neighbor_to_mine_list(self, r, c):
        """Adds a neighbor square to the list of adjacent mines."""
        if (r, c) in self.neighbor_mines:
            # this neighbor is already in the list
            return
        self.neighbor_mines.append((r, c))

    def __str__(self):
        if not self.uncovered:
            return '_'
        if self.number == -1:
            return '*'
        return str(self.number)

    def __repr__(self):
        return str(self)

class Board():
    def __init__(self, rows, cols, mines, startr, startc):
        self.rows: int = rows
        self.cols: int = cols
        self.mines: int = mines
        self.startr: int = startr
        self.startc: int = startc
        
        # verify that the input is valid
        if any(rows < 1, cols < 1, mines < 0):
            raise ValueError("Board sizes must be > 1. Mines must be > 0.")

        if (0 > startr > rows) or (0 > startc > cols):
            raise ValueError(f"Invalid starting space. Must be within the bounds of the game: {rows}x{cols}")

        starting_space_size = self.find_neighbors(startr, startc) + 1
        if (rows * cols) - starting_space_size < mines:
            raise ValueError("Invalid Board size. The board size must be large enough to place all mines, " +
                             f"including spaces designated for starting. You're board size was {rows*cols}, " + 
                             f"with {starting_space_size} spaces being reserved for a starting space. " +
                             f"You had only {(rows * cols) - starting_space_size < mines} valid spaces for mines " + 
                             f"with {mines} mines.")

        self.found_mines = set()
        self.board = self.make_board()

    def has_won(self):
        """Returns true if all of the mines have been found. False, otherwise."""
        return sum((1 for row in self.board for square in row if square.uncovered)) == (self.rows * self.cols) - self.mines

    def make_board(self):
        """
        Creates the game board and places mines in random squares.
        The starting square and its neighbors are exempt from being mines.
        """
        board = [[Square(r, c, 0) for c in range(self.cols)] for r in range(self. rows)]

        starting_point_neighbors = self.find_neighbors(self.startr, self.startc)
        starting_point_neighbors.append((self.startr,self.startc))

        for _ in range(0, self.mines):
            # find a space that isn't already a mine and isn't in the starting space
            m = (randint(0, self.rows-1), randint(0, self.cols-1))
            while board[m[0]][m[1]].number == -1 or m in starting_point_neighbors:
                m = (randint(0, self.rows-1), randint(0, self.cols-1))

            r = m[0]
            c = m[1]

            # assign the square to be a mine
            board[r][c].number = -1

            # increment the number of the mine's neighbors (if they aren't a mine)
            neighbors = self.find_neighbors(r,c)
            for row, col in neighbors:
                board[row][col].number += 1 if board[row][col].number != -1 else 0

        return board

    def uncover(self, row, col):
        """
        Uncover a square. If the square has already been uncovered, returns None.
        If the square is a mine, returns True. If the square is not a mine, returns False. 
        If the number of the square is 0, uncovers its neighbors. 
        """
        val = self.board[row][col].number
    
        # square is already uncovered
        if self.board[row][col].uncovered:
            return

        # square is a mine
        if val == -1:
            return True

        self.board[row][col].uncovered = True

        neighbors = self.find_neighbors(row, col)

        # tell the square's neighbors that it has been uncovered 
        for nrow, ncol in neighbors:
            self.board[nrow][ncol].uncovered_neighbors += 1

        # since the number is 0, it is safe to uncover all neighbors 
        if val == 0:
            self.uncover_neighbors(neighbors)

    def cover(self, row, col):
        """Set a square to be covered."""
        self.board[row][col].uncovered = False

    def uncover_neighbors(self, neighbors):
        """Uncovers the squares in the given list of neighbors."""
        for row, col in neighbors:
            self.uncover(row, col)
    
    def find_neighbors(self, r, c):
        """Returns a list of all of the valid neighbors of a square."""
        neighbors = []
        # above
        if r > 0:
            neighbors.append((r - 1, c))
            if c > 0:
                neighbors.append((r - 1, c - 1))
            if c < self.cols - 1:
                neighbors.append((r - 1, c + 1))
        # left and right
        if c > 0:
            neighbors.append((r, c - 1))
        if c < self.cols - 1:
            neighbors.append((r, c + 1))
        # below
        if r < self.rows - 1:
            neighbors.append((r + 1, c))
            if c > 0:
                neighbors.append((r + 1, c - 1))
            if c < self.cols - 1:
                neighbors.append((r + 1, c + 1))
        
        return neighbors

    def flag_mine(self, r, c, neighbors):
        """Add a square to the found mines list. Tell the square's neighbors that it is a mine."""
        self.found_mines.add((r, c))

        for nrow, ncol in neighbors:
            self.board[nrow][ncol].neighbor_mines.append(self.board[r][c])

    def evaluate_neighbors(self, r, c, neighbors):
        """
        Checks if the squares in the given list of neighbors have all of their adjacent mines flagged.
        Then uncovers its neighbors.
        """
        for nrow, ncol in neighbors:
            square = self.board[nrow][ncol]
            if square.uncovered and square.number == len(square.neighbor_mines):
                neighbors_eval = self.find_neighbors(nrow, ncol)
                neighbors_eval.remove((r,c))
                self.uncover_neighbors(neighbors_eval)

    def __str__(self) -> str:
        """Returns a string representation of the board."""
        s = ""
        for row in self.board:
            s += str(row) + "\n"
        return s

    def __repr__(self):
        return str(self)