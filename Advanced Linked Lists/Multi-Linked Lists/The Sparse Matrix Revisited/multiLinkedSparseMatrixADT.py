
from arrayADT import Array

class SparseMatrix :

    # Creates an empty sparse matrix.
    def __init__( self, rows, cols ) :
        self._rows = rows
        self._cols = cols

        # Store the rows.
        self._theRows = Array( self._rows )
        # Store the columns.
        self._theCols = Array( self._cols )

    # Return the number of rows in the matrix.
    def numRows( self ) :
        return self._rows

    # Return the number of columns in the matrix.
    def numCols( self ) :
        return self._cols

    # Gets the value stored at the position given by [ row, col ]
    def __getitem__( self, indexTuple ) :
        curNode = self._theRows[ indexTuple[0] ]

        while curNode is not None and curNode.col < indexTuple[1] :
            curNode = curNode.nextRow

        if curNode is not None and curNode.col == indexTuple[1] :
            return curNode.value

        return 0

    # Sets the value at the given index position to the given value.
    def __setitem__( self, indexTuple, val ) :

        # Handle the Rows.
        preNode = None
        curNode = self._theRows[ indexTuple[0] ]

        while curNode is not None and curNode.col < indexTuple[1] :
            preNode = curNode
            curNode = curNode.nextRow

        if curNode is not None and curNode.col == indexTuple[1] :
            if val == 0.0 :
                if curNode == self._theRows[ indexTuple[0] ] :
                    self._theRows[ indexTuple[0] ] = curNode.nextRow  # None
                else :
                    preNode.nextRow = curNode.nextRow

            else :
                curNode.value = val

        else :
            if val != 0.0 :
                newNode = _MatrixNode( indexTuple[0], indexTuple[1], val )
                newNode.nextRow = curNode


                if curNode == self._theRows[ indexTuple[0] ] :
                    self._theRows[ indexTuple[0] ] = newNode

                else :
                    preNode.nextRow = newNode

        # Handle the columns.
        preNode = None
        curNode = self._theCols[ indexTuple[1] ]

        while curNode is not None and curNode.row < indexTuple[0] :
            preNode = curNode
            curNode = curNode.nextCol

        if curNode is not None and curNode.row == indexTuple[0] :
            if val == 0.0 :
                if curNode == self._theCols[ indexTuple[1] ] :
                    self._theCols[ indexTuple[1] ] = curNode.nextCol
                else :
                    preNode.nextCol = curNode.nextCol

        else :
            if val != 0.0 :
                newNode = _MatrixNode( indexTuple[0], indexTuple[1], val )
                newNode.nextCol = curNode

                if curNode == self._theCols[ indexTuple[1] ] :
                    self._theCols[ indexTuple[1] ] = newNode

                else :
                    preNode.nextCol = newNode



    def scaleBy(self, scalar):
        for row in range( self.numRows() ):
            curNode = self._theRows[row]
            while curNode is not None:
                curNode.value *= scalar
                curNode = curNode.nextRow

    # Creates and returns a new matrix that is the transpose of this matrix.
    def transpose(self):
        newMatrix = SparseMatrix(self.numCols(), self.numRows())

        for row in range(self.numRows()):
            curNode = self._theRows[row]
            while curNode is not None:
                newMatrix[curNode.col, row] = self[row, curNode.col]
                curNode = curNode.nextRow

        return newMatrix

    # Matrix addition: newMatrix = self + rhsMatrix.
    def __add__(self, rhsMatrix):
        # Make sure the two matrices have the correct sizes.
        assert self.numRows() == rhsMatrix.numRows() and \
               self.numCols() == rhsMatrix.numCols(), \
            "Matrix sizes not compatible for the add operation."

        # Create a new sparse matrix of the same size.
        newMatrix = SparseMatrix(self.numRows(), self.numCols())

        # Add the elements of this matrix to the new matrix.
        for row in range(self.numRows()):
            curNode = self._theRows[row]
            while curNode is not None:
                newMatrix[row, curNode.col] = curNode.value
                # print( "Value is {}".format( curNode.value ) )
                # print( newMatrix[ row, curNode.col ] )
                curNode = curNode.nextRow

        # Add the elements of the rhsMatrix to the new matrix.
        for row in range(rhsMatrix.numRows()):
            curNode = rhsMatrix._theRows[row]
            while curNode is not None:
                value = newMatrix[row, curNode.col]
                #print( "Value is {}".format( value ) )  { debugging }
                value += curNode.value
                newMatrix[row, curNode.col] = value
                #print( "Added {}".format( value ) )      { debugging }

                curNode = curNode.nextRow

        # Return the new matrix.
        return newMatrix

    # Matrix subtraction and multiplication.
    def __sub__(self, rhsMatrix):
        # Make sure the matrices have the right number of rows and columns.
        assert self.numRows() == rhsMatrix.numRows() and self.numCols() == \
               rhsMatrix.numCols(), "Matrix sizes not compatible for the subtraction operation."

        # Create a new sparse matrix to store the results.
        newMatrix = SparseMatrix(self.numRows(), self.numCols())

        # Copy the items of self to the new matrix.
        for row in range(self.numRows()):
            curNode = self._theRows[row]
            while curNode is not None:
                newMatrix[row, curNode.col] = curNode.value
                curNode = curNode.next

        # Add the corresponding elements of the rhsMatrix to the new Matrix.
        for row in range(rhsMatrix.numRows()):
            curNode = rhsMatrix._theRows[row]
            while curNode is not None:
                value = newMatrix[row, curNode.col]
                value -= curNode.value
                newMatrix[row, curNode.col] = value

                curNode = curNode.nextRow

        return newMatrix

    def __mul__(self, rhsMatrix):
        # Matrix multiplication is defined for matrices where the number of columns of
        # the matrix on the left hand side is equal to the number of rows of the matrix
        # on the right hand side.

        newMatrix = SparseMatrix(rhsMatrix.numCols(), self.numRows())

        for row in range(self.numRows()):
            for col in range(rhsMatrix.numCols()):
                newMatrix[row, col] = 0
                for k in range(self.numCols()):
                    value = self[row, k] * rhsMatrix[k, col]
                    newMatrix[row, col] += value

        return newMatrix


# Storage class.
class _MatrixNode :
    def __init__( self, row, col, value ) :
        self.row = row
        self.col = col
        self.value = value
        self.nextCol = None
        self.nextRow = None


matrix1 = SparseMatrix( 5, 8 )
matrix1[0, 1] = 0
matrix1[0, 4] = 8
matrix1[1, 0] = 2
matrix1[1, 3] = 1
matrix1[1, 6] = 5
matrix1[2, 2] = 9
matrix1[2, 5] = 2
matrix1[3, 1] = 7
matrix1[3, 7] = 3
matrix1[4, 4] = 4

curNode = matrix1._theCols[4]
while curNode is not None :
    print( curNode.value)
    curNode = curNode.nextCol

