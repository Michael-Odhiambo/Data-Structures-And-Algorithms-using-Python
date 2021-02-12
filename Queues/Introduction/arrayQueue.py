
# An implementation of the Queue ADT using a circular array.
from arrayADT import Array

class Queue :
    # Creates a new queue instance.
    def __init__( self, maxSize ) :
        self._theArray = Array( maxSize )
        self._front = 0
        self._back = maxSize - 1
        self._count = 0

    # Returns True if the queue is empty.
    def isEmpty( self ) :
        return self._count == 0

    # Returns True if the queue is full.
    def isFull( self ) :
        return self._count == len( self._theArray )

    # Returns the number of items in the queue.
    def __len__( self ) :
        return self._count

    # Adds the given item to the queue.
    def enqueue( self, item ) :
        assert not self.isFull(), " Cannot enqueue to an empty queue. "
        maxSize = len( self._theArray )
        self._back = ( self._back + 1 ) % maxSize
        self._theArray[ self._back ] = item
        self._count += 1

    # Removes and returns the first item in the queue.
    def dequeue( self ) :
        assert not self.isEmpty(), " Cannot dequeue from an empty queue. "
        item = self._theArray[ self._front ]
        maxSize = len( self._theArray )
        self._front = ( self._front + 1 ) % maxSize
        self._count -= 1
        return item

myQueue = Queue( 10 )

for i in range( 10 ) :
    myQueue.enqueue( i )

for i in range( 10 ) :
    print( myQueue.dequeue() )
