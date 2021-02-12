
# Implementation of the Set ADT using a Python list.

class Set :

    # Creates an empty instance. The constructor can accept an optional variable argument to which
    # a collection of initial values can be passed to initialize the set.
    def __init__( self, *initElements ) :
        self._theElements = list()

        for element in initElements :
            if element in self :
                continue
            else :
                self._theElements.append( element )

    # Returns the number of items in the set.
    def __len__( self ) :
        return len( self._theElements )

    # Determines if an element is in the set.
    def __contains__( self, element ) :
        return element in self._theElements

    # Adds a new unique element to the set.
    def add( self, element ) :
        if element not in self :
            self._theElements.append( element )

    # Removes an element from the set.
    def remove( self, element ) :
        assert element in self, "The element must be in the set."
        self._theElements.remove( element )

    # Determines if two sets are equal.
    def __eq__( self, setB ) :
        if len( self ) != len( setB ) :
            return False
        else :
            return self <= setB 

    # Determines if this set is a subset of setB
    def __le__( self, setB ) :
        for element in self :
            if element not in setB :
                return False

        return True

    # Creates a new set from the union of this set and setB.
    def __add__( self, setB ) :
        newSet = Set()
        newSet._theElements.extend( self._theElements )
        for element in setB :
            if element not in self :
                newSet._theElements.append( element )

        return newSet
    
    # Creates and returns a new set that is the intersection of this set and setB. The intersection
    # of sets A and B contains only those elements that are in both A and B. Neither set A nor set B
    # is modified by this operation.
    def __mul__( self, setB ) :
        newSet = Set()
        for element in self :
            if element in setB :
                newSet._theElements.append( element )

        return newSet

    # Creates and returns a new set that is the difference of this set and setB. The set difference, A - B,
    # contains only those elements that are in A but not in B. Neither set A nor set B is modified by this
    # operation.
    def __sub__( self, setB ) :
        newSet = Set()
        for element in self :
            if element not in setB :
                newSet._theElements.append( element )

        return newSet

    # Determines if the set is empty. Returns a boolen value.
    def isEmpty( self ) :
        return len( self._theElements ) == 0

    # Returns an iterator for traversing the list of items.
    def __iter__( self ) :
        return _SetIterator( self._theElements )

    
    # Given two sets, A and B, A is a proper subset of B, if A is a subset of B and A
    # does not equal B.
    def isProperSubset( self, setB ) :
        if not self <= setB :
            return False

        if self == setB :
            return False

        return True

    # Prints the elements of contained in the set, surrounded by curly braces.
    def __str__( self ) :
        return " {  %s } " % ( str( val ) for val in self._theElements )


class _SetIterator :

    def __init__( self, theSet ) :
        self._theSet = theSet
        self._curIndex = 0

    def __iter__( self ) :
        return self

    def __next__( self ) :
        if self._curIndex < len( self._theSet ) :
            item = self._theSet[ self._curIndex ]
            self._curIndex += 1

            return item

        else :
            raise StopIteration


mySet = Set( 150, 150, 75, 23, 86, 49 )
set2 = Set( 150, 75, 23 )
print( mySet )






