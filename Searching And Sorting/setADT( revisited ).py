# Implementation of the set ADT using a sorted list.
class Set :
    # Creates an empty set instance.
    def __init__( self, *initElements ) :
        self._elementList = list()

        for element in initElements :
            if element in self :
                continue

            else :
                self._elementList.append( element )


    # Returns the number of elements in the set.
    def __len__( self ) :
        return len( self._elementList )

    # Determines if the element is in the list. The index returned by the _findPosition helper
    # method indicates the location where the element should be within the sorted list, but it
    # says nothing about the existence of the element. To determine if the element is in the set,
    # we can compare the element at the ndx position within the list to the target element. 
    # Note the inclusion of the condition ndx < len(self) within the compound expression. This is needed
    # since the value returned by findPosition() can be one larger than the number
    # of items in the list, which occurs when the target should be located at the end
    # of the list. If this value were directly used in examining the contents of the list
    # without making sure it was in range, an out-of-range exception could be raised.
    def __contains__( self, value ) :
        index = self._findPosition( value )
        return index < len( self ) and self._elementList[ index ] == value

    # Helper method used to find the index of the given element within the sorted element list.
    def _findPosition( self, value ) :
        low = 0
        high = len( self._elementList ) - 1
        
        while low <= high :
            mid = ( high + low ) // 2
            if self._elementList[mid] == value :
                return mid

            elif self._elementList[mid] < value :
                high = mid - 1

            else :
                low = mid + 1

        return low

    # Adds a unique element to the set.
    def add( self, value ) :
        if value not in self :
            index = self._findPosition( value )
            self._elementList.insert( index, value )


    # Removes an element from the set.
    def remove( self, value ) :
        assert value in self, "The given value must be in the set."
        index = self._findPosition( value )
        self._elementList.pop( index )

    # Determines if this set is a subset of setB.
    def isSubsetOf( self, setB ) :
        for i in range( len( self ) ) :
            if self._elementList[i] != setB._elementList[i] :
                return False

        return True

    # Returns an iterator for traversing over the elements of the set.
    def __iter__( self ) :
        return _SetIterator( self._elementList )

    # Determines if two sets are equal.
    def __eq__( self, setB ) :
        if len( self ) != len( setB ) :
            return False

        else :
            for i in range( len( self ) ) :
                if self._elementList[i] != setB._elementList[i] :
                    return False

        return True

    # Adds to sets.
    def __add__( self, setB ) :
        # Create a new set to hold the unique elements from both sets.
        newSet = set()
        a = 0
        b = 0

        while a < len( self ) and b < len( setB ) :
            valueA = self._elementList[a]
            valueB = self._elementList[b]

            if valueA < valueB :
                newSet._elementList.append( valueA )
                a += 1

            elif valueA > valueB :
                newSet._elementList.append( valueB )
                b += 1

            else :  # They are the same.
                newSet._elementList.append( valueA ) # In that case, only one value is appended.
                a += 1
                b += 1

        # If self contains more values, add them.
        while a < len( self ) :
            newSet._elementList.append( self._elementList[a] )
            a += 1

        # Or if setB contains more values, add them.
        while b < len( self ) :
            newSet._elementList.append( self._elementList[b] )
            b += 1

        return newSet

    # Creates and returns a new set that is the intersection of this set and setB. The intersection
    # of sets A and B contains only those elements that are in both A and B. Neither set A nor set B
    # is modified by this operation.
    def __mul__( self, setB ) :
        newSet = Set()
        a = 0
        b = 0

        while a < len( self ) and b < len( setB ) :
            if self._elementList[a] != setB._elementList[b] :
                if self._elementList[a] < setB._elementList[b] :
                    a += 1
                else :
                    b += 1

            else :
                newSet._elementList.append( self._elementList[a] )
                a += 1
                b += 1

        return newSet

    # Returns a string representation of the set.
    def __str__( self ) :
        return str( self._elementList )

    # Creates and returns a new set that is the difference of this set and setB. The set difference, A - B,
    # contains only those elements that are in A but not in B. Neither set A nor set B is modified by this
    # operation.
    def __sub__( self, setB ) :
        newSet = Set()
        a = 0
        b = 0

        while a < len( self ) and b < len( setB ) :
            if self._elementList[a] != setB._elementList[b] :
                newSet._elementList.append( self._elementList[a] )
                a += 1
            else :
                a += 1
                b += 1
        # If there are more items in self, add them to the new set.
        while a < len( self ) :
            newSet._elementList.append( self._elementList[a] )
            a += 1


        return newSet 





class _SetIterator :
    def __init__( self, theList ) :
        self.theList = theList
        self.curIndex = 0

    def __iter__( self ) :
        return self

    def __next__( self ) :
        if self._curIndex < len( self.theList ) :
            item = self.theList[ self._curIndex ]
            self.curIndex += 1

            return item

        else :
            raise StopIteration


mySet = Set( 1, 2, 3, 4, 5, 6, 20, 21, 22, 32 )
set2 = Set( 2, 3, 4, 5, 10, 12, 13, 14, 15 )
print( mySet )
print( mySet * set2 )
print( mySet - set2 )