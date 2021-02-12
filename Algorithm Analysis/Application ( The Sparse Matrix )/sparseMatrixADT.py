

# Implementation of the Sparse Matrix ADT using a list.

class SparseMatrix :
    
    # Create a sparse matrix of size numRows * numCols initialized to zero.
    def __init__( self, numRows, numCols ) :
        self._numRows = numRows
        self._numCols = numCols
        self._elementList = list()

    # Return the number of rows in the matrix.
    def numRows( self ) :
        return self._numRows

    # Return the number of columns in the matrix.
    def numCols( self ) :
        return self._numCols

    # Return the value of element (i, j): x[i, j].
    def __getitem__( self, indexTuple ) :
        index = self._findPosition( indexTuple[0], indexTuple[1] )

        if index is not None :  # if the element is found in the list.
            return self._elementList[index].value

        return 0


    # Set the value of element (i, j) to the value s: x[i, j] = s.
    def __setitem__( self, indexTuple, scalar ) :
        index = self._findPosition( indexTuple[0], indexTuple[1] )
        
        if index is not None :  # if the element is found in the List.
            if scalar != 0.0 :
                self._elementList[index].value = scalar
            else :
                self._elementList.pop( index )

        else :   # If the element is not zero and not in the list.
            if scalar != 0.0 :
                element = _MatrixElement( indexTuple[0], indexTuple[1], scalar )
                self._elementList.append( element )

    # Scale the matrix by the given scalar.
    def scaleBy( self, scalar ) :
        for element in self._elementList :
            element.value *= scalar
    
    # Helper method used to find a specific matrix element (row, col) in the list
    # of non-zero entries. None is returned if the element is not found.
    def _findPosition( self, row, col ) :
        n = len( self._elementList )

        for i in range( n ) :
            if row == self._elementList[i].row and \
                col == self._elementList[i].col :
                return i      # Return the index of the element if found.
        
        return None    # Return None when the element is zero.

    # Adds two sparse matrices and returns a new sparse matrix containing the result.
    def __add__( self, rhsMatrix ) :
        # The two matrices must have the same number of rows and columns.
        assert self.numRows() == rhsMatrix.numRows() and \
            self.numCols() == rhsMatrix.numCols(), "Matrix sizes not compatible for add operation."

        # Create a new Sparse Matrix.
        newMatrix = SparseMatrix( self.numRows(), self.numCols () )

        # Duplicate the lhs matrix. The elements are mutable thus we must
        # create new objects and not simply copy the references.
        for element in self._elementList :
            dupElement = _MatrixElement( element.row, element.col, element.value )
            newMatrix._elementList.append( dupElement )

        # Iterate through each non-zero element of the rhsMatrix.
        for element in rhsMatrix._elementList :
            # Get the value of the corresponding element in the new Matrix.
            value = newMatrix[ element.row, element.col ]
            value += element.value
            # Store the new value back to the new matrix.
            newMatrix[ element.row, element.col ] = value

        # Return the new matrix.
        return newMatrix

    # Subtracts two sparse matrices and returns a new sparse matrix containing the result.
    def __sub__( self, rhsMatrix ) :
        assert self.numRows() == rhsMatrix.numRows() and \
            self.numCols() == rhsMatrix.numCols(), "Invalid matrix sizes for subtraction operation."

        # Create a new sparse matrix to hold the result.
        newMatrix = SparseMatrix( self.numRows(), self.numCols() )

        # Copy the elements of the self matrix to the new matrix.
        for element in self._elementList :
            dupElement = _MatrixElement( element.row, element.col, element.value )
            newMatrix._elementList.append( dupElement )

        # Go through the elements in the rhsMatrix.
        for element in rhsMatrix._elementList :
            # Get the corresponding value from the new Matrix.
            value = newMatrix[ element.row, element.col ]
            value -= element.value

            # Store the value back to the new Matrix.
            newMatrix[ element.row, element.col ] = value

        return newMatrix

    # Multiplies two sparse matrices.
    def __mul__( self, rhsMatrix ) :
        # Matrix multiplication is defined for matrices where the number of columns of
        # the matrix on the left hand side is equal to the number of rows of the matrix
        # on the right hand side.
        assert self.numCols() == rhsMatrix.numRows(), "Matrix sizes not compatible for the \
            multiplication operation."

        # Create a new sparse matrix to hold the results.
        newMatrix = SparseMatrix( rhsMatrix.numCols(), self.numRows() )
        # Copy the elements in self to the new matrix.
        for row in range( self.numRows() ) :
            for col in range( rhsMatrix.numCols() ) :
                newMatrix[row, col] = 0
                for k in range( self.numCols() ) :
                    value = self[row, k] * rhsMatrix[k, col]
                    newMatrix[row, col] += value

        return newMatrix





# Storage class for holding the non-zero matrix elements.
class _MatrixElement :
    def __init__( self, row, col, value ) :
        self.row = row
        self.col = col
        self.value = value


myMatrix = SparseMatrix( 5, 8 )
myMatrix[0, 1] = 3
myMatrix[0, 4] = 8
myMatrix[1, 0] = 2
myMatrix[1, 3] = 1
myMatrix[1, 6] = 5
myMatrix[2, 2] = 9
myMatrix[2, 5] = 2
myMatrix[3, 1] = 7
myMatrix[3, 7] = 3
myMatrix[4, 4] = 4


matrix2 = SparseMatrix( 5, 8 )
matrix2[0, 6] = 3
matrix2[1, 0] = 9
matrix2[1, 2] = 4
matrix2[2, 1] = 10
matrix2[2, 3] = 6
matrix2[2, 7] = 7
matrix2[3, 2] = 11
matrix2[3, 4] = 16
matrix2[3, 6] = 20
matrix2[4, 1] = 9
matrix2[4, 3] = 21
matrix2[4, 6] = 22

matrix3 = myMatrix + matrix2
print( matrix3[1, 0] )
print( matrix3[0, 0] )

print( myMatrix[1, 0] )

matrix4 = myMatrix - matrix2
print( matrix4[1, 0] )

matrix5 = SparseMatrix( 4, 2 )
matrix5[0, 1] = 3
matrix5[1, 1] = 5
matrix5[2, 0] = 2
matrix5[3, 1] = 10

matrix6 = SparseMatrix( 2, 4 )
matrix6[0, 1] = 10
matrix6[0, 3] = 11
matrix6[1, 0] = 12
matrix6[1, 3] = 7


matrix7 = matrix5 * matrix6
print( matrix7[0, 0] )
print( matrix7[0, 1] )
print( matrix7[0, 2] )
print( matrix7[0, 3] )