

class PriorityQueue :
    def __init__( self ) :
        self._qList = list()

    # Returns True if the queue is empty.
    def isEmpty( self ) :
        return len( self ) == 0

    # Returns the number of items in the queue.
    def __len__( self ) :
        return len( self._qList )

    # Helper method for finding the proper position of an item.
    def _findPosition( self, priority ) :
        low = 0
        high = len( self ) - 1

        while low <= high :
            mid = ( low + high ) // 2

            if self._qList[ mid ].priority == priority :
                return mid + 1

            elif self._qList[ mid ].priority < priority :
                low = mid + 1

            else :
                high = mid - 1

        return low

    # Adds an item to the queue.
    def enqueue( self, item, priority ) :
        item = _PriorityQEntry( item, priority )
        index = self._findPosition( priority )

        self._qList.insert( index, item )

    # Removes and returns the first item in the queue.
    def dequeue( self ) :
        assert not self.isEmpty(), " Cannot dequeue from an empty queue. "

        entry = self._qList.pop( 0 )
        return entry.item


# Storage class.
class _PriorityQEntry :
    def __init__( self, item, priority ) :
        self.item = item
        self.priority = priority

Q = PriorityQueue()
Q.enqueue( "Purple", 5 )
Q.enqueue( "Black", 1 )
Q.enqueue( "Orange", 3 )
Q.enqueue( "White", 0 )
Q.enqueue( "Green", 1 )
Q.enqueue( "Yellow", 5 )

print( Q.dequeue() )
print( Q.dequeue() )
print( Q.dequeue() )
print( Q.dequeue() )
print( Q.dequeue() )
print( Q.dequeue() )

