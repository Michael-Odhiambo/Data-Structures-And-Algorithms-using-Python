


class PriorityQueue :
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

    # Adds an item into the queue.
    def enqueue( self, item, priority ) :

        item = _QueueNode( item, priority )
        if self._head is None :
            self._head = item

        else :
            self._tail.next = item

        self._tail = item
        self._count += 1

    # Removes and returns the item with the highest priority in the queue.
    def dequeue( self ) :
        assert not self.isEmpty(), " Cannot dequeue from an empty Queue. "

        curNode = self._head
        preNode = None

        highestPriorityNode = curNode
        prevNode = None

        while curNode is not None :
            if curNode.priority < highestPriorityNode.priority :
                prevNode = preNode
                highestPriorityNode = curNode

            preNode = curNode
            curNode = curNode.next

        if highestPriorityNode is self._head :
            self._head = self._head.next

        else :
            prevNode.next = highestPriorityNode.next


        return highestPriorityNode.item


        


# Storage class.
class _QueueNode :
    def __init__( self, item, priority ) :
        self.item = item
        self.priority = priority
        self.next = None


Q = PriorityQueue()
Q.enqueue( "Purple", 5 )
Q.enqueue( "Black", 1 )
Q.enqueue( "Orange", 3 )
Q.enqueue( "White", 0 )
Q.enqueue( "Green", 1 )
Q.enqueue( "Yellow", 5 )

print( len( Q ) )

print( Q.dequeue() )
print( Q.dequeue() )
print( Q.dequeue() )
print( Q.dequeue() )
print( Q.dequeue() )
print( Q.dequeue() )

