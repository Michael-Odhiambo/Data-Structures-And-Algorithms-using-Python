
class CountingBag :

    def __init__( self ) :
        self._theItems = dict()

    def __len__( self ) :
        return len( self._theItems )

    def __contains__( self, item ) :
        return item in self._theItems.keys()

    def add( self, item ) :

        if item in self._theItems.keys() :
            self._theItems[ item ] += 1

        else :
            self._theItems[ item ] = 1

    def numOf( self, item ) :
        assert item in self._theItems.keys(), "Item is not in the bag."
        
        return self._theItems[ item ]

    def __iter__( self ) :
        return _BagIterator( self._theItems )

    def remove( self, item ) :
        self._theItems.pop( item )


# Returns an iterator over the items in the Counting Bag.
class _BagIterator :
    
    def __init__( self , theItems ) :
        self._theItems = theItems
        self._curIndex = 0

    def __iter__( self ) :
        return self

    def __next__( self ) :
        if self._curIndex < len( self._theItems ) :
            keys = list( self._theItems.keys() )
            values = list( self._theItems.values() )

            key = keys[ self._curIndex ]
            value = values[ self._curIndex ]

            self._curIndex += 1
            
            return key, value

        else :
            raise StopIteration


