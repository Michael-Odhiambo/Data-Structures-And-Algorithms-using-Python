
from arrayADT import Array

# Implementation of the Map ADT using closed hashing and a probe with
# double hashing.

# Storage class for the hash table entries.
class _MapEntry :
    def __init__( self, key, value ) :
        self.key = key
        self.value = value

class HashMap :
    # Defines constants to represent the status of each table entry.
    UNUSED = None
    EMPTY = _MapEntry( None, None )

    # Creates an empty map instance.
    def __init__( self ) :
        self._hashTable = Array( 7 )
        self._count = 0
        self._loadFactor = len( self._hashTable ) - len( self._hashTable ) // 3

    # Finds the slot containing the key or where the key can be added.
    # forInsert indicates if the search is for an insertion, which locates
    # the slot into which the new key can be added.

    def _findSlot( self, key, forInsert ) :
        # Compute the home slot and step size.
        slot = self._hash1( key )
        step = self._hash2( key )

        # Probe for the key.
        M = len( self._hashTable )



        while self._hashTable[ slot ] is not HashMap.UNUSED :
            if forInsert and ( self._hashTable[ slot ] is HashMap.UNUSED or self._hashTable[ slot ] is HashMap.EMPTY ) :
                return slot

            elif not forInsert and ( self._hashTable[ slot ] is not HashMap.EMPTY and self._hashTable[ slot ].key == key ) :
                return slot

            else :
                slot = ( slot + step ) % M

        if forInsert and ( self._hashTable[ slot ] is HashMap.UNUSED or self._hashTable[ slot ] is HashMap.EMPTY ) :
            return slot

    def _rehash( self ) :
        # Create a new larger table.
        origTable = self._hashTable
        newSize = len( self._hashTable ) * 2 + 1
        self._hashTable = Array( newSize )

        # Modify the size attributes.
        self._count = 0
        self._loadFactor = newSize - newSize // 3

        # Add the keys from the original array to the new table.
        for entry in origTable :
            if entry is not HashMap.UNUSED and entry is not HashMap.EMPTY :
                slot = self._findSlot( entry.key, True )
                self._hashTable[ slot ] = entry
                self._count += 1

    # The main hash function for mapping keys to the table entries.
    def _hash1( self, key ) :
        return abs( hash( key ) ) % len( self._hashTable )

    # The second hash function used with double hashing probes.
    def _hash2( self, key ) :
        return 1 + abs( hash( key ) ) % ( len( self._hashTable ) - 2 )

    # Returns the value associated with the given key.
    def valueOf( self, key ) :
        slot = self._findSlot( key, False )
        assert slot is not None, "Invalid map key."
        return self._hashTable[ slot ].value

    # Adds a new entry to the map if the key does not exist. Otherwise, the new value
    # replaces the current value associated with the given key.
    def add( self, key, value ) :
        if key in self :
            slot = self._findSlot( key, False )
            self._hashTable[ slot ].value = value
            return False

        else :
            slot = self._findSlot( key, True )
            self._hashTable[ slot ] = _MapEntry( key, value )
            self._count += 1
            if self._count == self._loadFactor :
                self._rehash()
            return True

    def __contains__( self, key ) :
        slot = self._findSlot( key, False )
        return slot is not None

    def __len__( self ) :
        return self._count

    def __iter__( self ) :
        return _HashMapIterator( self._hashTable )

    def remove( self, key ) :
        assert key in self, "Invalid key entry."
        slot = self._findSlot( key, False )
        self._hashTable[ slot ] = _MapEntry( None, None )
        self._count -= 1


class _HashMapIterator :
    def __init__( self, theHashTable ) :
        self._theTable = theHashTable
        self._curBlock = 0
    def __iter__( self ) :
        return self

    def __next__( self ) :
        if self._curBlock < len( self._theTable ) :
            if self._theTable[ self._curBlock ] is not None :
                entry = self._theTable[ self._curBlock ].key
                self._curBlock += 1
                return entry

            else :
                self._curBlock += 1

        else :
            raise StopIteration









myHash = HashMap()

myHash.add( 103, "Michael" )
myHash.add( 101, "Allan" )
myHash.add( 155, "Odhiambo" )
myHash.add( 116, "Edwina" )
myHash.add( 200, "Software" )
print( len( myHash ) )
print()
myHash.remove( 116 )
print()
print( len( myHash ) )

print( len( myHash._hashTable) )
print( myHash._loadFactor )

for key in myHash :
    print( key )



