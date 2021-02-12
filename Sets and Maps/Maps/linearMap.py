

class Map :

    # Creates an empty map instance.
    def __init__( self ) :
        self._entryList = list()

    # Returns the number of entries in the map.
    def __len__( self ) :
        return len( self._entryList )

    # Determines if the map contains the given key.
    def __contains__( self, key ) :
        index = self._findPosition( key )
        return index is not None

    # Adds a new entry to the map if the key doesn't exist. Otherwise, the new value replaces
    # the current value associated with the key.
    def __setitem__( self, key, value ) :
        index = self._findPosition( key )
        if index is not None :  # if the key was found.
            self._entryList[index].value = value

            return False

        else :  # Otherwise add a new entry.
            entry = _MapEntry( key, value )
            self._entryList.append( entry )
            
            return True

    # Returns the value associated with the key.
    def __getitem__( self, key ) :
        index = self._findPosition( key )
        assert index is not None, "Invalid Map entry."
        return self._entryList[index].value

    # Removes the entry associated with the key.
    def remove( self, key ) :
        index = self._findPosition( key )
        assert index is not None, "Invalid Map entry."
        self._entryList.pop( index )

    # Returns an iterator for traversing the keys of the map.
    def __iter__( self ) :
        return _MapIterator( self._entryList )

    # Helper method used to find the index position of a category. If the key is not found,
    # None is returned.
    def _findPosition( self, key ) :
        # Iterate through the elements of the list.
        for i in range( len( self ) ) :
            # Is the key stored in the ith entry?
            if self._entryList[i].key == key :
                return i

            # When not found, return None.
        return None

    # Returns an array containing all of the keys stored in the map. The keys should not be
    # any particular ordering.
    def keyArray( self ) :
        keys = list()

        for val in self._entryList :
            keys.append( val.key )

        return keys


# Storage class for holding key/value pairs.
class _MapEntry :
    def __init__( self, key, value ) :
        self.key = key
        self.value = value

# Iterator for traversing the keys of the map.
class _MapIterator :
    def __init__( self, theList ) :
        self._theList = theList
        self._curIndex = 0

    def __iter__( self ) :
        return self

    def __next__( self ) :
        if self._curIndex < len( self._theList ) :
            key = self._theList[self._curIndex].key
            val = self._theList[self._curIndex].value
            self._curIndex += 1

            return key, val

        else :
            raise StopIteration


