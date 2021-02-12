
class LifeGrid :

    LIVE_CELL = 1
    DEAD_CELL = 0

    def __init__( self ) :
        self._elementList = list()
        # Clear the grid and set all cells to dead.
        self.configure( list() )

    # Returns a 2-tuple (minrow, mincol) that contains the minimum row index and the minimum
    # column index that is currently occupied by a live cell.
    def minRange( self ) :

    
        rowList = list()
        colList = list()

        # Go through all the rows of the values in the grid and add them to the row list.
        for value in self._elementList :
            rowList.append( value.row )

        # Go through all the columns of the values in the grid and add them to the col list.
        for value in self._elementList :
            colList.append( value.col )

        # Determine the minimum values for the row and col.

        minRow = 0
        minCol = 0

        if rowList :
            minRow = min( rowList ) - 1
            if minRow < 0 :
                minRow = 0

        if colList :
            minCol = min( colList ) - 1
            if minCol < 0 :
                minCol = 0
    

        return minRow, minCol

    # Returns a 2-tuple (maxrow, maxcol) that contains the maximum row index and the maximum
    # column index that is currently occupied by a live cell.
    def maxRange( self ) :
        rowList = list()
        colList = list()

        # Go through all the rows of the values in the grid and add them to the row list.
        for value in self._elementList :
            rowList.append( value.row )

        # Go through all the columns of the values in the grid and add them to the col list.
        for value in self._elementList :
            colList.append( value.col )

        # Determine the minimum values for the row and col.
        maxRow = 0
        maxCol = 0

        if rowList :
            maxRow = max( rowList ) + 1

        if colList :
            maxCol = max( colList ) + 1

        return maxRow, maxCol

    def __setitem__( self, indexTuple, value ) :

        # Find the index position within the element list.
        index = self._findPosition( indexTuple[0], indexTuple[1] )

        # If the index is found, go to the next step.
        if index is not None :
            # If value is not zero, modify the existing element.
            if value != 0 :
                self._elementList[index].value = value

            # If the value is zero, remove the element at the given index position from the list.
            else :
                self._elementList.pop( index )

        # If the index is not found and the value is not zero, add it to the list.
        else :
            if value != 0 :
                element = _GridElement( indexTuple[0], indexTuple[1], value )
                self._elementList.append( element )

    def __getitem__( self, indexTuple ) :
        index = self._findPosition( indexTuple[0], indexTuple[1] )
        
        if index is not None :
            return self._elementList[index].value

        return 0

    # Helper method used for finding the index position of an element.
    def _findPosition( self, row, col ) :
        n = len( self._elementList )

        for i in range( n ) :
            if row == self._elementList[i].row and col == self._elementList[i].col :
                return i

        return None

    # Configures the grid for evolving the first generation. The coordList argument is a sequence of 
    # 2-tuples with each tuple representing the coordinates (r, c) of the cells to be set as alive.
    # All remaining cells are cleared or set to dead.
    def configure( self, coordlist ) :

        for row in range( self.minRange()[0], self.maxRange()[0] + 1 ) :
            for col in range( self.minRange()[1], self.maxRange()[1] + 1 ) :
                self.clearCell( row, col )

        
        # Set the indicated cells to be alive.
        for coord in coordlist :
            self[ coord[0], coord[1] ] = LifeGrid.LIVE_CELL

    # Clears the individual cell (row, col) and sets it to dead. The cell indices must be within
    # the valid range of the grid.
    def clearCell( self, row, col ) :
        """
        assert row >= self.minRange()[0] and row <= self.maxRange()[0] and \
            col >= self.minRange()[1] and col <= self.maxRange()[1], \
                "Indices out of range."
        """

        self[row, col] = LifeGrid.DEAD_CELL

    # Sets the indicated cell (row, col) to be alive. The cell indices must be within the 
    # valid range of the grid.
    def setCell( self, row, col ) :
        """
        assert row >= self.minRange()[0] and row <= self.maxRange()[0] and \
            col >= self.minRange()[1] and col <= self.maxRange()[1], \
                "Indices out of range."
        """
        self[row, col] = LifeGrid.LIVE_CELL

    # Returns a boolean value indicating if the given cell (row, col) contains a live organism.
    # The cell indices must be within the valid range of the grid.
    def isLiveCell( self, row, col ) :
        """
        assert row >= self.minRange()[0] and row <= self.maxRange()[0] and \
            col >= self.minRange()[1] and col <= self.maxRange()[1], \
                "Indices out of range."
        """

        
        return self[row, col] == LifeGrid.LIVE_CELL

    # Returns a list containing valid neighbors for the given cell.
    def _validNeighbors( self, theRow, theCol ) :

        neighborsList = list()

        searchMin = -1
        searchMax = 2

        for row in range( searchMin, searchMax ) :
            for col in range( searchMin, searchMax ) :

                validNeighbor = True

                neighborRow = theRow + row
                neighborCol = theCol + col

                # A cell cannot be it's own neighbor.
                if neighborRow == theRow and neighborCol == theCol :
                    validNeighbor = False

                # Row out of range.
                if neighborRow < self.minRange()[0] or neighborRow > self.maxRange()[0] :
                    validNeighbor = False

                # Col out of range.
                if neighborCol < self.minRange()[1] or neighborRow > self.maxRange()[1] :
                    validNeighbor = False

                if validNeighbor :
                    neighborsList.append( (neighborRow, neighborCol) )
        
        return neighborsList

    def numLiveNeighbors( self, row, col ) :
        neighbors = self._validNeighbors( row, col )

        liveNeighbors = 0

        for neighbor in neighbors :
            index = self._findPosition( neighbor[0], neighbor[1] ) 

            if index is not None :
                liveNeighbors += 1

        return liveNeighbors


    
# Storage class.
class _GridElement :
    def __init__( self, row, col, value ) :
        self.row = row
        self.col = col
        self.value = value


