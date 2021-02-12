# Implements the Maze ADT using a 2-D array.
from array2D import Array2D
from lListStack import Stack


class Maze:
    # Define constants to represent contents of the maze cells.
    MAZE_WALL = '*'
    PATH_TOKEN = '>'
    TRIED_TOKEN = 'o'

    # Creates a maze object with all cells marked as open.
    def __init__(self, numRows, numCols):
        self._mazeCells = Array2D(numRows, numCols)
        self._startCell = None
        self._exitCell = None

    # Returns the number of rows in the maze.
    def numRows(self):
        return self._mazeCells.numRows()

    # Returns the number of columns in the maze.
    def numCols(self):
        return self._mazeCells.numCols()

    def getStartPos( self ) :
        return self._startCell

    # Fills the indicated cell with a "wall" marker.
    def setWall(self, row, col):
        assert row >= 0 and row < self.numRows() and col >= 0 and col < self.numCols(), \
            "Cell index out of range."
        self._mazeCells[row, col] = self.MAZE_WALL

        # Sets the starting cell position.

    def setStart(self, row, col):
        assert row >= 0 and row < self.numRows() and col >= 0 and col < self.numCols(), \
            "Cell index out of range."
        self._startCell = _CellPosition(row, col)

    # Sets the exit cell position.
    def setExit(self, row, col):
        assert row >= 0 and row < self.numRows() and col >= 0 and col < self.numCols(), \
            "Cell index out of range."
        self._exitCell = _CellPosition(row, col)

    # Attempts to solve the maze by finding a path from the starting cell to the exit. Returns True
    # if a path is found and False otherwise.
    def findPath( self, curCell ) :

        # Base case.

        # If the exit is found, draw the path and return True.
        if curCell.row == self._exitCell.row and curCell.col == self._exitCell.col :
            self.draw()
            return True

        else :
            # Find this cell's neighbors.
            neighbors = self._validNeighbors( curCell.row, curCell.col )

            # Go through all the neighbors and find a valid move.
            for neighbor in neighbors :
                if self._isValidMove( neighbor.row, neighbor.col ) :
                    validMove = neighbor

                    # If a valid move is found, meaning this cell does not lead to a dead end,
                    # mark it as a path first then proceed to the cell referenced by "validMove."
                    self._markPath( curCell.row, curCell.col )

                    # If a path is found from this cell, return True otherwise, this cell leads to a dead end
                    # so we need to backtrack. We first mark "this cell" with a tried token and proceed to the
                    # next valid neighbor.
                    if self.findPath( validMove ) :
                        return True

                    else :
                        self._markTried( curCell.row, curCell.col )

            # If the loop terminates, the maze has no path.
            return False

    # Resets the maze by removing all "path" and "tried" tokens.
    def reset(self):

        for row in range(self.numRows()):
            for col in range(self.numCols()):

                # If there is a "path" token at the given cell, remove it.
                if self._mazeCells[row, col] == self.PATH_TOKEN:
                    self._mazeCells[row, col] = None

                # If there is a "tried" token at the given cell, remove it.
                elif self._mazeCells[row, col] == self.TRIED_TOKEN:
                    self._mazeCells[row, col] = None

    # Prints a text-based representation of the maze.
    def draw(self):
        for row in range(self.numRows()):
            for col in range(self.numCols()):

                if self._mazeCells[row, col] == self.MAZE_WALL:
                    print(" *", end=" ")

                elif self._mazeCells[row, col] == self.PATH_TOKEN:
                    print("->", end=" ")

                else:
                    print(" _", end=" ")

            print()

    # Returns True if the given cell position is a valid move.
    def _isValidMove(self, row, col):
        return row >= 0 and row < self.numRows() and col >= 0 and col < self.numCols() and \
               self._mazeCells[row, col] is None

    # helper method to determine if the exit was found.
    def _exitFound(self, row, col):
        return self._exitCell.row == row and self._exitCell.col == col

    # Drops a "tried" token at the given cell.
    def _markTried(self, row, col):
        self._mazeCells[row, col] = self.TRIED_TOKEN

    # Drops a "path" token at the given cell.
    def _markPath(self, row, col):
        self._mazeCells[row, col] = self.PATH_TOKEN

    # Helper method to find all the valid neighbors of the given cell.
    def _validNeighbors(self, theRow, theCol):
        searchMin = -1
        searchMax = 2

        validNeighbors = list()

        for row in range(searchMin, searchMax):
            for col in range(searchMin, searchMax):
                neighborRow = theRow + row
                neighborCol = theCol + col

                validNeighbor = True

                # A cell cannot be its own neighbor.
                if neighborRow == theRow and neighborCol == theCol:
                    validNeighbor = False

                # Row out of range.
                elif neighborRow < 0 or neighborRow >= self.numRows():
                    validNeighbor = False

                # Column out of range.
                elif neighborCol < 0 or neighborCol >= self.numCols():
                    validNeighbor = False

                # Limit the neighbors to the vertical and horizontal cells only.
                elif neighborRow != theRow:
                    if neighborCol != theCol:
                        validNeighbor = False

                # If a neighbor is found, create a cell objects with the given indices and add it to the
                # valid neighbors list.
                if validNeighbor:
                    cell = _CellPosition(neighborRow, neighborCol)
                    validNeighbors.append(cell)

                    # Return the valid neighbors list.
        return validNeighbors


# Private storage class for holding a cell position.
class _CellPosition:
    def __init__(self, row, col):
        self.row = row
        self.col = col


