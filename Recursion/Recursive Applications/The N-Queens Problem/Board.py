
from array2D import Array2D

class Board :

    def __init__( self, n ) :
        self._theBoard = Array2D( n, n )
        self._rowSize = n
        self._size = n * n
        self._numQueens = 0
        self._count = 0

    def size( self ) :
        return self._size

    def numQueens( self ) :
        return self._numQueens

    # Places a queen at position ( row, col ).
    def placeQueen( self, row, col ) :
        self._theBoard[ row, col ] = 1
        self._numQueens += 1

    # Removes the queen from position ( row, col ).
    def removeQueen( self, row, col ) :
        self._theBoard[ row, col ] = None
        self._numQueens -= 1

    # Resets the board to its original state by removing all queens currently placed
    # on the board.
    def reset( self ) :
        for row in range( self._theBoard.numRows() ) :
            for col in range( self._theBoard.numCols() ) :
                self._theBoard[ row, col ] = None

    # Prints the board in a readable format using characters to represent the squares
    # containing the queens and the empty squares.
    def draw( self ) :
        for row in range( self._theBoard.numRows() ) :
            for col in range( self._theBoard.numCols() ) :
                if self._theBoard[ row, col ] == 1 :
                    print( "| Q |", end = "" )

                else :
                    print( "|   |", end = "" )

            print()

    # Returns a boolean value indicating if the given square is currently unguarded.
    # Note that this function is called when "col" queens are already placed in columns
    # from 0 to col - 1. So we need to check only left side for attacking queens.
    def _unGuarded( self, row, col ) :

        # Check this row on the left side.
        for i in range( col ) :
            if self._theBoard[ row, i ] == 1 :
                return False

        # Check the upper diagonal on the left side.
        for i, j in zip( range( row, -1, -1 ), range( col, -1, -1 ) ) :
            if self._theBoard[ i, j ] == 1 :
                return False

        # Check the lower diagonal on the left side.
        for i, j in zip( range( row, self._rowSize, 1 ), range( col, -1, -1 ) ) :
            if self._theBoard[ i, j ] == 1 :
                return False

        return True

    # Finds one solution and prints it.
    def solveNQueens( self, col ) :
        # A solution was found if n queens were placed on the board.
        if self._numQueens == self._rowSize :
            return True

        else :
            # Find the next unguarded square within this column.
            for row in range( self._rowSize ) :
                if self._unGuarded( row, col ) :
                    # Place a queen at that square.
                    self.placeQueen( row, col )
                    # Continue placing queens in the following columns.
                    if self.solveNQueens( col + 1 ) :
                        # We are finished if a solution was found.
                        return True
                    else :
                        # No solution was found with the queen in this square, so it has
                        # to be removed.
                        self.removeQueen( row, col )

            # If the loop terminates, no queen can be placed within this column
            return False

    # Finds all the solutions for the given board size.
    def findAllSolutions( self, col ) :

        # The base case.
        if self._numQueens == self._rowSize :
            # If a solution is found, count it.
            self._count += 1
            return True

        else :
            for row in range( self._rowSize ) :
                # If the given cell is unguarded, place a queen.
                if self._unGuarded( row, col ) :
                    self.placeQueen( row, col )

                    # Continue placing queens in the successive columns.
                    if self.findAllSolutions( col + 1 ) :
                        # If a solution is found with the queen in the given cell, draw the resulting
                        # board, then remove the queen and try the next row on the board.
                        self.draw()
                        self.removeQueen( row, col )
                        print()

                    # If a solution is not found with the queen at the given cell, backtrack.
                    else :
                        self.removeQueen( row, col )

            # If the loop terminate, no queen can be placed at this column.
            return False



myBoard = Board( 8 )

myBoard.findAllSolutions(0)
print( myBoard._count )








