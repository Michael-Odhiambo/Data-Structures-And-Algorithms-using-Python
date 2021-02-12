
# Implementation of the Matrix ADT using a 2-D array.

from array2D import Array2D

class Matrix :
    # Creates a new matrix of size numRows * numCols initialized to zero.
    def __init__( self, numRows, numCols ) :
        self._theGrid = Array2D( numRows, numCols )
        self._theGrid.clear( 0 )

    # Returns the number of rows in the matrix.
    def numRows( self ) :
        return self._theGrid.numRows()

    # Returns the number of columns in the matrix.
    def numCols( self ) :
        return self._theGrid.numCols()

    # Returns the value of element (i, j): x[i, j].
    def __getitem__( self, indexTuple ) :
        return self._theGrid[ indexTuple[0], indexTuple[1] ]

    # Sets the value of element (i, j) to the value s: x[i, j] = s.
    def __setitem__( self, indexTuple, value ) :
        self._theGrid[ indexTuple[0], indexTuple[1] ] = value

    # Scales the matrix by the given scalar.
    def scaleBy( self, scalar ) :
        for r in range( self.numRows() ) :
            for c in range( self.numCols() ) :
                self[r, c] *= scalar

    # Creates and returns a new matrix that is the transpose of this matrix.
    def transpose( self ) :
        # Create a new Matrix.
        newMatrix = Matrix( self.numCols(), self.numRows() )

        for row in range( self.numRows() ) :
            for col in range( self.numCols() ) :
                newMatrix[ col, row ] = self[ row, col ]

        return newMatrix



    # Creates and returns a new matrix that results from matrix addition.
    def __add__( self, rhsMatrix ) :
        assert rhsMatrix.numRows() == self.numRows() and \
            rhsMatrix.numCols() == self.numCols(), \
                "Matrix sizes not compatible for the add operation."

        # Create a new matrix.
        newMatrix = Matrix( self.numRows(), self.numCols() )
        # Add the corresponding elements in the two matrices.
        for r in range( self.numRows() ) :
            for c in range( self.numCols() ) :
                newMatrix[ r, c ] = self[ r, c ] + rhsMatrix[ r, c ]

        return newMatrix

    # Creates and returns a new Matrix that is the result of matrix subtraction.
    def __sub__( self, rhsMatrix ) :
        assert rhsMatrix.numRows() == self.numRows() and \
            rhsMatrix.numCols() == self.numCols(), \
                "Matrix sizes not compatible for subtraction operation."

        # Create a new matrix.
        newMatrix = Matrix( self.numRows(), self.numCols() )
        # Subtract the corresponding elements of the two matrices.
        for r in range( self.numRows() ) :
            for c in range( self.numCols() ) :
                newMatrix[ r, c ] = self[ r, c ] - rhsMatrix[ r, c ]

        return newMatrix

    # Creates and returns a new matrix resulting from matrix multiplication.
    def __mul__( self, rhsMatrix ) :
        # Matrix multiplication is only defined for matrices where the number of columns in the matrix on the
        # lefthand side is equal to the number of rows in the matrix on the righthand side.
        assert self.numCols() == rhsMatrix.numRows(), \
            "Matrix sizes not compatible for multiplication operation."
        
        # Create a new matrix.
        newMatrix = Matrix( self.numRows(), rhsMatrix.numCols() )

        for i in range( self.numRows() ) :
            for j in range( rhsMatrix.numCols() ) :
                newMatrix[ i, j ] = 0
                for k in range( self.numCols() ) :
                    value = self[ i, k ] * rhsMatrix[ k, j ]
                    newMatrix[ i, j ] += value
            

        return newMatrix



