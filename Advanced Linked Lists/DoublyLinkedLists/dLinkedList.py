
class LinkedList :
    def __init__( self ) :
        self._head = None
        self._tail = None
        self._probe = None
        self._size = 0

    def __len__( self ) :
        return self._size

    # Adds an item to the list.
    def add( self, value ) :
        node = _listNode( value )

        if self._head is None :  # Empty list.
            self._head = node
            self._tail = node

        elif value < self._head.data :  # insert before head.
            node.next = self._head
            self._head.prev = node
            self._head = node

        elif value > self._tail.data :
            node.prev = self._tail
            self._tail.next = node
            self._tail = node

        else :  # Insert in the middle.
            curNode = self._head

            while curNode is not None and curNode.data < value :
                curNode = curNode.next

            node.next = curNode
            node.prev = curNode.prev
            curNode.prev.next = node
            curNode.prev = node

        self._size += 1

    # Probing a doubly linked list.
    # Given the head, tail and probe references, probe the list for a target. Make sure the list is not
    # empty.
    def __contains__( self, target ) :
        if self._head is None :
            return False

        # If probe is null, initialize it to the first node.
        if self._probe is None :
            self._probe = self._head

        # If the target comes before the probe node, we traverse backward, otherwise, traverse forward.
        if target < self._probe.data :
            while self._probe is not None and target <= self._probe.data :
                if target == self._probe.data :
                    return True
                else :
                    self._probe = self._probe.prev

        else :
            while self._probe is not None and target >= self._probe.data :
                if target == self._probe.data :
                    return True
                else :
                    self._probe = self._probe.next

        # If the target is not found in the list, return False.
        return False

    def forwardTraversal( self ) :
        curNode = self._head

        while curNode is not None :
            print( curNode.data )
            curNode = curNode.next

    def backwardTraversal( self ) :
        curNode = self._tail

        while curNode is not None :
            print( curNode.data )
            curNode = curNode.prev

    def remove( self ) :
        pass


# Storage class.
class _listNode :
    def __init__( self, data ) :
        self.data = data
        self.prev = None
        self.next = None

myList = LinkedList()
myList.add( 21 )
myList.add( 37 )
myList.add( 58 )
myList.add( 74 )
myList.add( 48 )
myList.forwardTraversal()
print()
print( len( myList ) )

print( 60 in myList )

