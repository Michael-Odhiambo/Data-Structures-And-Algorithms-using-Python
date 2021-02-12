
# Implementation of the unbounded queue ADT using a Python list with new items appended to the end.


class PriorityQueue :
    # Creates a priority queue.
    def __init__( self ) :
        self._qList = list()

    # Returns True if the queue is empty.
    def isEmpty( self ) :
        return len( self ) == 0

    # Returns the length of the queue.
    def __len__( self ) :
        return len( self._qList )

    # Adds the given item item to the queue.
    def enqueue( self, item, priority ) :
        # Creates a new item of the storage class and appends it to the queue.
        item = _PriorityQEntry( item, priority )
        self._qList.append( item )

    # Removes and returns the first item in the queue.
    def dequeue( self ) :
        assert not self.isEmpty(), " Cannot dequeue from an empty queue. "

        # Find the entry with the highest priority.
        highest = 0
        for i in range( len( self ) ) :
            if self._qList[ i ].priority < self._qList[ highest ].priority :
                highest = i

        # Remove the item with the highest priority and return it.
        entry = self._qList.pop( highest )
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

