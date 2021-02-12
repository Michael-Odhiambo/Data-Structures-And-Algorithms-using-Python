# Implement the Bag ADT from Chapter 1 to use a sorted list and the binary
# search algorithm. Evaluate the time complexities for each of the operations.

class Bag :
    # Creates an empty bag instance.
    def __init__( self, *initElements ) :
        self._items = list()

        for element in initElements :
            self.add( element )

    # Returns the number of items in the bag.
    def __len__( self ) :
        return len( self._items )

    # Helper method to find the index of an item in the bag.
    def _findPosition( self, item ) :
        low = 0
        high = len( self ) - 1

        while low <= high :
            mid = ( low + high ) // 2
            
            if self._items[ mid ] == item :
                return mid

            elif self._items[ mid ] < item :
                low = mid + 1
            
            else :
                high = mid - 1

        return low

    # Determines if the given item is in the list.
    def __contains__( self, item ) :
        index = self._findPosition( item )
        return index < len( self ) and self._items[ index ] == item

    # Add an item to the bag. The items is added at its proper position so that the sorted list
    # is maintained.
    def add( self, item ) :
        index = self._findPosition( item )
        self._items.insert( index, item )

    # Removes the given items from the bag.
    def remove( self, item ) :
        assert item in self._items, "The given item must be in the bag."
        index = self._findPosition( item )
        self._items.pop( index )

    def __iter__( self ) :
        return _BagIterator( self._items )


class _BagIterator :
    def __init__( self, theItems ) :
        self.items = theItems
        self._curIndex = 0

    def __iter__( self ) :
        return self

    def __next__( self ) :
        if self._curIndex < len( self.items ) :
            item = self.items[ self._curIndex ]
            self._curIndex += 1

            return item

        else :
            raise StopIteration

myBag = Bag( 2, 1, 5, 4, 6, 4 )
myBag.add( 100 )
myBag.remove( 2 )
for item in myBag :
    print( item )

print( "+++++++" )

print( len( myBag ) )

print( "+++++" )
print( 0 in myBag )



















