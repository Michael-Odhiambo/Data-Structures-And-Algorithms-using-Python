
from arrayADT import Array

# Implementation of the MultiArray ADT using a 1-D array.

class MultiArray :

    # Creates a multi-dimensional array.
    def __init__( self, *dimensions ) :
        assert len( dimensions ) > 1, "The array must have 2 or more dimensions."
        # The variable argument tuple contains the dim sizes.
        self._dims = dimensions

        # Compute the total number of elements in the array.
        size = 1
        for d in dimensions :
            assert d > 0, "Dimensions must be greater than 0."
            size *= d

        # Create the 1-D array to store the elements.
        self._elements = Array( size )
        # Create a 1-D array to store the equation factors.
        self._factors = Array( len( dimensions ) )
        self._computeFactors()

    # Returns the number of dimensions in the array.
    def numDims( self ) :
        return len( self._dims )

    # Returns the length of the given dimension.
    def length( self, dim ) :
        assert dim >= 1 and dim <= len( self._dims ), \
            "Dimension component out of range."

        return self._dims[ dim - 1 ]

    # Clears the array by setting all elements to the given value.
    def clear( self, value ) :
        self._elements.clear( value )

    # Returns the contents of element ( i_1, i_2, ..., i_n ).
    def __getitem__( self, indexTuple ) :
        assert len( indexTuple ) == self.numDims(), "Invalid number of array subscripts."
        index = self._computeIndex( indexTuple )
        assert index is not None, "Array subscript out of range."

        return self._elements[ index ]

    # Sets the contents of element ( i_1, i_2, ..., i_n ).
    def __setitem__( self, indexTuple, value ) :
        assert len( indexTuple ) == self.numDims(), "Invalid number of array subscripts."
        index = self._computeIndex( indexTuple )
        assert index is not None, "Array subscript out of range."
        
        self._elements[ index ] = value

    # Computes the 1-D array offset for element ( i_1, i_2, .., i_n )
    # using the equation i_1 * f_1 + i_2 * f_2 + ... + i_n * f_n.
    def _computeIndex( self, index ) :
        offset = 0
        for j in range( len( index ) ) :
            # Make sure the index components are within the legal range.
            if index[j] < 0 or index[j] >= self._dims[j] :
                return None

            else :
                # sum the product of i_j * f_j.
                offset += index[j] * self._factors[j]

        return offset

    # Computes the factor values used in the index equation.
    def _computeFactors( self ) :

        size = self.numDims()
        n = 1
        count = 0

        while n <= size :
            prod = 1

            if n == size :
                self._factors[count] = prod
                break
            
            for i in range( n, size ) :
                prod *= self._dims[i]

            self._factors[ count ] = prod 

            n += 1
            count += 1
