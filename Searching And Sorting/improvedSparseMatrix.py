# The implementation of the Sparse Matrix ADT from Chapter 4 can be improved 
# by storing the MatrixElement objects in a sorted list and using the
# binary search to locate a specific element. The matrix elements can be sorted
# based on the row and column indices using an index function similar to that
# used with a 2-D array stored in a MultiArray. Implement a new version of
# the Sparse Matrix ADT using a sorted list and the binary search to locate
# elements.

class SparseMatrix :

    # Creates an empty sparse matrix.
    def __init__( self, rows, cols ) :
        self._rows = rows
        self._cols = cols
        self._elementList = list()

    # Returns the number of rows in the matrix.
    def numRows( self ) :
        return self._rows

    # Returns the number of columns in the matrix.
    def numCols( self ) :
        return self._cols

    # Helper method to calculate the offset based on the element's row and column.
    def _calcOffset( self, row, col ) :
        offset = ( row * self._cols ) + col

        return offset

    # Helper method to find the given element or its correct position in the matrix.
    def _findPosition( self, row, col ) :
        low = 0
        high = len( self._elementList ) - 1
        
        # Calculate the target values's offset.
        targetOffset = self._calcOffset( row, col )

        while low <= high :
            mid = ( low + high ) // 2
            # Calculate the middle value's offset value.
            midOffset = self._calcOffset( self._elementList[ mid ].row, self._elementList[ mid ].col )

            # If the item is found in the middle, return its index.
            if midOffset == targetOffset :
                return mid

            # If the middle index is less than the target value's index, shift the low variable.
            elif midOffset < targetOffset :
                low = mid + 1

            # If the middle index is greater than the target value's index, shift the high variable.
            else :
                high = mid - 1

        # Index where the target value should be placed if its not in the matrix.
        return low


    # Gets the value at the given index position.
    def __getitem__( self, indexTuple ) :
        index = self._findPosition( indexTuple[0], indexTuple[1] )
        assert index < len( self._elementList ), "Element not in the matrix."
        return self._elementList[ index ].value

    # Sets the value in the given index position.
    def __setitem__( self, indexTuple, val ) :
        index = self._findPosition( indexTuple[0], indexTuple[1] )

        # If the value is in the matrix and the given value is not zero, add it to the matrix.
        if index < len( self._elementList ) :
            if val != 0.0 :
                if self._elementList[ index ].row == indexTuple[0] and self._elementList[ index ].col == indexTuple[1] :
                    self._elementList[ index ].value = val

                else :
                    item = _MatrixElement( indexTuple[0], indexTuple[1], val )
                    self._elementList.insert( index, item )
                    print( "Created {} and inserted it at {} ".format( (item.row, item.col, item.value ), index ) )

            else :
                self._elementList.pop( index )

        else :
            # If the value is not in the list and val is not zero, add it to its proper position.
            if val != 0.0 :
                item = _MatrixElement( indexTuple[0], indexTuple[1], val )
                self._elementList.insert( index, item )
                print( " Created {} and inserted it at position {} ".format( (item.row, item.col, item.value ), index ) )

    
# Storage class for storing the matrix elements.
class _MatrixElement :
    def __init__( self, row, col, value ) :
        self.row = row
        self.col = col
        self.value = value

matrix1 = SparseMatrix( 5, 5 )
matrix1[ 0, 1 ] = 100
matrix1[ 1, 2 ] = 200
matrix1[ 0, 3 ] = 300
matrix1[ 0, 2 ] = 1
matrix1[ 0, 2 ] = 1000

for element in matrix1._elementList :
    print( element.row, element.col, element.value ) 




        

    