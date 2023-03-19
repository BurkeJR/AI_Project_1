from random import randint

class Square():
    def __init__(self, r, c, number, uncovered=False):
        self.r = r
        self.c = c
        self.number = number
        self.uncovered = uncovered
        self.neighbor_mines = []
        self.uncoveredNeighbors = 0

    def safe_to_uncover_neighbors(self, numNeighbors):
        return numNeighbors - self.uncoveredNeighbors == self.number

    def __str__(self):
        if not self.uncovered:
            return '_'
        if self.number == -1:
            return '*'
        return str(self.number)

    def __repr__(self):
        return str(self)

    def add_neighbor_to_mine_list(self, r, c):
        if (r, c) in self.neighbor_mines:
            # this neighbor is already in the list
            return
        self.neighbor_mines.append((r, c))

class Board():
    def __init__(self, rows, cols, mines, startr, startc):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.startr = startr
        self.startc = startc
        self.uncovered_mines = []
        self.board = self.make_board()

    def hasWon(self):
        return len(self.uncovered_mines) == self.mines

    def make_board(self):
        board = [[Square(r, c, 0) for c in range(self.cols)] for r in range(self. rows)]

        startingPointNeighbors = self.findNeighbors(self.startr, self.startc)
        startingPointNeighbors.append((self.startr,self.startc))

        for _ in range(0, self.mines):
            # find a space that isn't already a mine
            m = (randint(0, self.rows-1), randint(0, self.cols-1))
            while board[m[0]][m[1]].number == -1 or m in startingPointNeighbors:
                m = (randint(0, self.rows-1), randint(0, self.cols-1))

            r = m[0]
            c = m[1]

            board[r][c].number = -1

            neighbors = self.findNeighbors(r,c)
            for row, col in neighbors:
                board[row][col].number += 1 if board[row][col].number != -1 else 0

        return board

    def uncover(self, row, col):
        val = self.board[row][col].number
    
        if self.board[row][col].uncovered:
            return

        if val == -1:
            return True

        self.board[row][col].uncovered = True

        neighbors = self.findNeighbors(row, col)

        for nrow, ncol in neighbors:
            self.board[nrow][ncol].uncoveredNeighbors += 1

        if val == 0:
            self.uncover_neighbors(neighbors)

    def cover(self, row, col):
        self.board[row][col].uncovered = False

    def uncover_neighbors(self, neighbors):
        for row, col in neighbors:
            self.uncover(row, col)
    
    def findNeighbors(self, r, c):
        neighbors = []
        if r > 0:
            neighbors.append((r - 1,c))
            if c > 0:
                neighbors.append((r - 1, c - 1))
            if c < self.cols - 1:
                neighbors.append((r - 1, c + 1))
        if c > 0:
            neighbors.append((r, c - 1))
        if c < self.cols - 1:
            neighbors.append((r, c + 1))
        if r < self.rows - 1:
            neighbors.append((r + 1, c))
            if c > 0:
                neighbors.append((r + 1, c - 1))
            if c < self.cols - 1:
                neighbors.append((r + 1, c + 1))
        return neighbors

    def flagMine(self, r, c, neighbors):
        if (r, c) not in self.uncovered_mines:
            self.uncovered_mines.append((r, c))

        for nrow, ncol in neighbors:
            self.board[nrow][ncol].neighbor_mines.append(self.board[r][c])

    def evaluateNeighbors(self, r, c, neighbors):
        for nrow,ncol in neighbors:
            square = self.board[nrow][ncol]
            if square.uncovered and square.number == len(square.neighbor_mines):
                neighborsEval = self.findNeighbors(nrow, ncol)
                neighborsEval.remove((r,c))
                self.uncover_neighbors(neighborsEval)

    def __str__(self) -> str:
        s = ""
        for row in self.board:
            s += str(row) + "\n"
        return s

    def __repr__(self):
        return str(self)