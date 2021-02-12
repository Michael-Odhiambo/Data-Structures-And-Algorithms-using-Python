
class Queue :
    def __init__( self ) :
        self._head = None
        self._size = 0

    def __len__( self ) :
        return self._size

    def isEmpty( self ) :
        return self._head is None

    def enqueue( self, item, priority ) :

        preNode = None
        curNode = self._head

        while curNode is not None and curNode.priority <= priority :
            preNode = curNode
            curNode = curNode.next

        newNode = _QueueNode( item, priority )
        newNode.next = curNode

        if curNode is self._head :
            self._head = newNode

        else :
            preNode.next = newNode

    def dequeue( self ) :
        assert not self.isEmpty(), " Cannot dequeue from an empty queue."
        node = self._head
        self._head = self._head.next

        return node.item



# Storage class.
class _QueueNode :
    def __init__( self, item, priority ) :
        self.item = item
        self.priority = priority
        self.next = None

Q = Queue()
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