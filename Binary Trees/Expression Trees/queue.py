
# Implementation of the Queue ADT using a linked list.
class Queue :
    # Creates an empty queue instance.
    def __init__( self ) :
        self._head = None
        self._tail = None
        self._count = 0

    # Returns True if the queue is empty.
    def isEmpty( self ) :
        return self._head is None

    # Returns the number of items in the queue.
    def __len__( self ) :
        return self._count

    # Adds the given item to the queue.
    def enqueue( self, item ) :
        node = _QueueNode( item )
        if self._head is None :
            self._head = node

        else :
            self._tail.next = node

        self._tail = node
        self._count += 1

    # Removes and returns the first item in the queue.
    def dequeue( self ) :
        assert not self.isEmpty(), " Cannot dequeue from an empty queue. "
        node = self._head
        if self._head is self._tail :
            self._head = None
            self._tail = None

        else :
            self._head = self._head.next

        self._count -= 1
        return node.item

class _QueueNode :
    def __init__( self, item ) :
        self.item = item
        self.next = None



