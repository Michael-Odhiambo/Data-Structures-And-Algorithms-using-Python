
import random

class GrabBag :

    def __init__( self ) :
        self._theItems = list()

    # Returns the number of items in the bag.
    def __len__( self ) :
        return len( self._theItems )

    # Determines if the given item is in the bag.
    def __contains__( self, item ) :
        return item in self._theItems

    # Adds a new item in the bag.
    def add( self, item ) :
        self._theItems.append( item )

    # Randomly removes an item from the bag.
    def grabItem( self ) :
        index = random.randint( 0, len( self._theItems) - 1 )
        return self._theItems[ index ]

    # Returns an iterator over the GrabBag.
    def __iter__( self ) :
        return _BagIterator( self._theItems )



class _BagIterator :
    def __init__( self, theList ) :
        self._theItems = theList
        self._curIndex = 0

    def __iter__( self ) :
        return self

    def __next__( self ) :
        if self._curIndex < len( self._theItems ) :
            item = self._theItems[ self._curIndex ]
            self._curIndex += 1

            return item

        else :
            raise StopIteration

