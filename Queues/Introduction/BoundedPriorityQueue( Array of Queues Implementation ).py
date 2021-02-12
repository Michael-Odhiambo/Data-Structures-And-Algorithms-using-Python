# Implementation of the bounded Priority Queue ADT using an array of queues in which the queues are
# implemented using a linked list.

from arrayADT import Array
from lListQueue import Queue

class BPriorityQueue :
    # Creates an empty bounded priority queue.
    def __init__( self, numLevels ) :
        self._qSize = 0
        self._qLevels = Array( numLevels )

        for i in range( numLevels ) :
            self._qLevels[i] = Queue()

    # Returns True if the queue is empty.
    def isEmpty( self ) :
        return len( self ) == 0

    # Returns the number of items in the queue.
    def __len__( self ) :
        return self._qSize

    # Adds the given item into the queue.
    def enqueue( self, item, priority ) :
        assert priority >= 0 and priority < len( self._qLevels ), " Invalid Priority level. "
        self._qLevels[ priority ].enqueue( item )
        self._qSize += 1

    # Removes and returns the first item in the queue.
    def dequeue( self ) :
        i = 0

        while i < len( self._qLevels ) and self._qLevels[i].isEmpty() :
            i += 1

        return self._qLevels[i].dequeue()


Q = BPriorityQueue( 6 )
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






