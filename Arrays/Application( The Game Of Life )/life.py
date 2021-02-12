
# Implements the LifeGrid ADT for use with the game of Life.
from array2D import Array2D

class LifeGrid :
    # Defines constants to represent the cell states.
    DEAD_CELL = 0
    LIVE_CELL = 1

    # Creates the game grid and initializes the cells to be dead.
    def __init__( self, numRows, numCols ) :
        # Allocate the 2-D array for the grid.
        self._grid = Array2D( numRows, numCols ) 
        # Clear the grid and set all cells to dead.
        self.configure( list() )

    # Returns the number of rows in the grid.
    def numRows( self ) :
        return self._grid.numRows()

    # Returns the number of columns in the grid.
    def numCols( self ) :
        return self._grid.numCols()

    # Configures the grid to contain the given live cells.
    def configure( self, coordList ) :
        # Clear the game grid.
        for i in range( self.numRows() ) :
            for j in range( self.numCols() ) :
                self.clearCell( i, j )

        # Set the indicated cells to be alive.
        for coord in coordList :
            self.setCell( coord[0], coord[1] )

    # Does the indicated cell contain live organism?
    def isLiveCell( self, row, col ) :
        return self._grid[row, col] == LifeGrid.LIVE_CELL

    # Clears the indicates cell by setting it to dead.
    def clearCell( self, row, col ) :
        self._grid[row, col] = LifeGrid.DEAD_CELL

    # Sets the indicated cell to be alive.
    def setCell( self, row, col ) :
        self._grid[row, col] = LifeGrid.LIVE_CELL


    # OK, now on to what i believe is the trickiest part about the whole code: checking
    # all the neighbors. With checkNeighbors() we have to pass in the coordinates we want
    # to check and then we have to travel within our array to check all the surrounding
    # neighbors.
    # This means we have to jump one row back (-1), check our own row (0) and the next row (1).
    # In Python terms that means going through a range from -1 to 2, range(-1, 2), We have to do
    # the same with the columns.
    # We set start and end range as variables and make it clear how they can be affected.

    # Cycling through a range is easy, but you're probably already wondering how we deal with going
    # outside the board.
    # What we have to do here is to check if we're working in any of the corners or any of the edges.

    # For the check itself, we need to cycle through the array based on what the program puts into check_row
    # and check_column ( the parameters for checkNeighbor.)

    # We will loop through the range we have set, searchMin - searchMax. Since the range starts at -1 normally
    # we add 1, so we check the correct rows. We want to jump 1 unit back, but we also want to work on the
    # correct index. Lists in Python start at 0.

    # The conditions in the loops are to ignore squares outside of the board and itself:
    def _checkNeighbors( self, theRow, theCol ) :

        searchMin = -1
        searchMax = 2

        # Number of valid neighbors.
        numValidNeighbors = list()


        for row in range( searchMin, searchMax ) :
            for col in range( searchMin, searchMax ) :
                neighborRow = theRow + row
                neighborCol = theCol + col

                validNeighbor = True

                # The cell being checked cannot be its own neighbor.
                if ( neighborRow == theRow and neighborCol == theCol ) :
                    validNeighbor = False

                # Row out of range.
                if ( neighborRow < 0 or neighborRow >= self.numRows() ) :
                    validNeighbor = False

                # Column out of range.
                if ( neighborCol < 0 or neighborCol >= self.numCols() ) :
                    validNeighbor = False

                if validNeighbor :
                    numValidNeighbors.append( self._grid[ neighborRow, neighborCol ] )

        return numValidNeighbors

    # Returns the number of live neighbors for the given cell.
    def numLiveNeighbors( self, row, col ) :

        liveNeighbors = 0

        for neighbor in self._checkNeighbors( row, col ) :
            if neighbor == LifeGrid.LIVE_CELL :
                liveNeighbors += 1


        return liveNeighbors 
