# Implement a new version of the Map ADT from Section 3.2 to use a sorted
# list and the binary search algorithm.

class Map :
    def __init__( self ) :
        self._theItems = list()

    def __len__( self ) :
        return len( self._theItems )

    # Helper method to find the given key in the map.
    def _findPosition( self, key ) :
        low = 0
        high = len( self ) - 1

        while low <= high :
            mid = ( low + high ) // 2
            if self._theItems[ mid ].key == key :
                return mid

            elif self._theItems[ mid ].key < key :
                low = mid + 1

            else :
                high = mid - 1

        return low

    # Determines if the given key is contained in the map.
    def __contains__( self, theKey ) :
        index = self._findPosition( theKey )
        return index < len( self ) and self._theItems[ index ].key == theKey

    # Mofifies the value if found else adds it to the map.
    def __setitem__( self, theKey, theValue ) :
        if theKey in self :
            index = self._findPosition( theKey )
            self._theItems[ index ].value = theValue

        else :
            index = self._findPosition( theKey )
            item = _MapElement( theKey, theValue )
            self._theItems.insert( index, item )

    # Gets the item associated with the given key.
    def __getitem__( self, theKey ) :
        if theKey in self :
            index = self._findPosition( theKey )
            return self._theItems[ index ].value
        

    # Removes the item associated with the given key.
    def remove( self, key ) :
        assert key in self, " The value must be in the map."
        index = self._findPosition( key )
        self._theItems.pop( index )


class _MapElement :
    def __init__( self, key, value ) :
        self.key = key
        self.value = value

myMap = Map()
myMap[10] = 1000
myMap[2] = 200
myMap[10] = 10000

for val in myMap._theItems :
    print( val.value )

print()

print( myMap[10] )