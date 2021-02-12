
from arrayADT import Array

class Vector :

    # Creates a new empty vector with an initial capacity of two elements.
    def __init__( self, size = 2 ) :

        self._theArray = Array( size * 2 )

        self._theArrayCapacity = len( self._theArray )

    # Returns the number of items contained in the Vector.
    def __len__( self ) :

        count = 0 

        for element in self._theArray :
            if element != None :
                count += 1

        return count


    # Determines if the given item is contained in the vector.
    def __contains__( self, theItem ) :
        for item in range( len( self ) ) :
            if item in self._theArray :
                return True

        return False

    # Returns the item stored in the index element of the list. The value of index must be within
    # the valid range.
    def __getitem__( self, index ) :
        assert index >= 0 and index < len( self ), "Index out of range."
        return self._theArray[ index ]

    # Sets the element at potition index to contain the given item. The value of index must be within
    # the valid range, which includes the first position past the last item.
    def __setitem__( self, index, item ) :
        assert index >= 0 and index <= len( self ), "Index out of range."
        self._theArray[ index ] = item

    # Adds the given item to the end of the list.
    def append( self, item ) :
        # If the array is out of capacity, Create a new array, add the items in the old array
        # to the new one, add the "item" to the end of the new array and destroy the old array.

        # If the array is full,
        if len( self ) >= self._theArrayCapacity :
            # Create a new one,
            newArray = Array( self._theArrayCapacity * 2 )
            # Add the items in the old array to the new one.
            for element in range( len( self._theArray ) ) :
                newArray[ element ] = self._theArray[ element ]
            
            # Destroy the old array.
            self._theArray = newArray
            # Update the array capacity.
            self._theArrayCapacity = len( self._theArray )

            # Then add the item to the end of the vector.
            self._theArray[ len(self) ] = item

        # If there is still space in the array, just add the item.
        else :
            self._theArray[ len(self) ] = item

    
    # Inserts the given item i the element at position index. The items in the elements at and
    # following the given position are shifted down to make room for the new item. Index must
    # be within the valid range.
    def insert( self, index, item ) :

        assert index >= 0 and index <= len( self ), "Index out of range."

        n = len( self )

        while n > index :
            self._theArray[n] = self._theArray[ n - 1 ]

            n -= 1

        self._theArray[ index ] = item
        
            

    def __iter__( self ) :
        return _vectorIterator( self )


    # Removes and returns the item from the given index position. The items in the elements at and following
    # the given position are shifted up to close the gap created by the removed item. Index must be within the
    # valid range.
    def remove( self, index ) :
        assert index >= 0 and index < len( self ), "Index out of range."

        item = self._theArray[ index ]

        for element in range( index, len( self ) ) :
            self._theArray[ element ] = self._theArray[ element + 1 ]

        # The size of the underlying array decreases after a sufficient number of items have been removed.
        if ( self._theArrayCapacity // 2 ) > len( self ) :
            # reduce the array by half.
            self._theArrayCapacity = self._theArrayCapacity // 2

        return item

    # Returns the index of the vector element containing containing the given item. The item must be
    # in the list.
    def indexOf( self, item ) :
        assert item in self._theArray, "Item not in the vector."
        index = 0

        for element in self._theArray :
            if element == item :
                return index

            else :
                index += 1

    # Extends this vector by appending the entire contents of the otherVector to this vector.
    def extend( self, otherVector ) :

        for element in otherVector :
            self.append( element )

    # Creates and returns a new vector that contains a subsequence of the items in the vector between
    # and including those indicated by the given from and to positions. Both the from and to positions
    # must be within the valid range.
    def subVector( self, start, end ) :
        theVector = Vector()

        for element in range( start, end + 1 ) :
            theVector.append( self._theArray[ element ] )

        return theVector



# An iterator for the Array ADT.
class _vectorIterator :

    def __init__( self, theArray ) :
        self._arrayRef = theArray
        self._curIndex = 0

    def __iter__( self ) :
        return self

    def __next__( self ) :
        if self._curIndex < len( self._arrayRef ) :
            entry = self._arrayRef[ self._curIndex ]
            self._curIndex += 1

            return entry

        else :
            raise StopIteration







