
# Implementation of the sparse matrix ADT using a list.
class SparseMatrix :
    # Creates an empty sparse matrix instance.
    def __init__( self, numRows, numCols ) :
        self._numRows = numRows
        self._numCols = numCols
        # A list to hold the sparse matrix elements.
        self._elementList = list()

    # Returns the number of rows of the sparse matrix.
    def numRows( self ) :
        return self._numRows

    # Returns the number of columns of the sparse matrix.
    def numCols( self ) :
        return self._numCols

    # Helper method used to find a given matrix element. It returns the index of 
    # the element if found and None otherwise.
    def _findPosition( self, row, col ) :
        # Traverse through the elements in the element list.
        n = len( self._elementList )
        
        for i in range( n ) :
            if self._elementList[i].row == row and self._elementList[i].col == col :
                return i

        # Return None if the element is not found.
        return None

    # Get the item at position [i, j].
    def __getitem__( self, indexTuple ) :
        index = self._findPosition( indexTuple[0], indexTuple[1] )

        # If the element is found, return its value.
        if index is not None :
            return self._elementList[index].value

    # Set the item at position [i, j] to the given value.
    def __setitem__( self, indexTuple, scalar ) :
        index = self._findPosition( indexTuple[0], indexTuple[1] )

        # If the element is found in the list and scalar is not zero:
        if index is not None :
            if scalar != 0.0 :
                self._elementList.value = scalar

            # if scalar is zero, remove the element from the list.
            else :
                self._elementList.pop( index )

        # If index is None and scalar is not zero, create the element and add it to the list.
        else :
            element = _MatrixElement( indexTuple[0], indexTuple[1], scalar )
            self._elementList.append( element )

    # Scale the matrix by the given scalar.
    def scaleBy( self, scalar ) :
        for element in self._elementList :
            element.value *= scalar

    # Add this matrix with matrix B.
    def __add__( self, matrixB ) :
        # For the add operation to be performed, the two matrices must have the same number
        # of rows and columns.
        assert self.numRows() == matrixB.numRows() and self.numCols() == matrixB.numCols, \
            "Matrix sizes not compatible for the add operation."

        # Create a new sparse matrix for storing the results.
        newMatrix = SparseMatrix( self.numRows, self.numCols )

        # Duplicate the elements in self to the new matrix.
        for element in self._elementList :
            dupElement = _MatrixElement( element.row, element.col, element.value )
            newMatrix._elementList.append( dupElement )

        # Go through the non-zero elements in matrixB.
        for element in matrixB._elementList :
            # Get the corresponding value from the new matrix.
            value = newMatrix[ element.row, element.col ]
            value += element.value

            # Store the new value back to the new matrix.
            newMatrix[ element.row, element.col ] = value

        # Return the new matrix.
        return newMatrix  

      







# Storage class used to store the matrix elements.
class _MatrixElement :
    def __init__( self, row, col, value ) :
        self.row = row
        self.col = col
        self.value = value
        