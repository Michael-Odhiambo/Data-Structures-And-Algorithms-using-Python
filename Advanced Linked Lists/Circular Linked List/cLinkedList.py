
class LinkedList :
    def __init__( self ) :
        self._tail = None
        self._count = 0

    def __len__( self ) :
        return self._count

    def __contains__( self, value ) :
        curNode = self._tail
        done = self._tail is None

        while not done :
            curNode = curNode.next
            if curNode.data == value :
                return True
            else :
                done = curNode is self._tail or curNode.data > value

        return False

    def traverse( self ) :
        curNode = self._tail
        done = self._tail is None

        while not done :
            curNode = curNode.next
            print( curNode.data )
            done = curNode is self._tail

    def add( self, value ) :
        newNode = _listNode( value )

        if self._tail is None :    # Empty list.
            self._tail = newNode
            newNode.next = newNode

        elif value < self._tail.next.data :  # Insert infront.
            newNode.next = self._tail.next
            self._tail.next = newNode

        elif value > self._tail.data :   # Insert at the back.
            newNode.next = self._tail.next
            self._tail.next = newNode
            self._tail = newNode

        else :   # Insert in the middle.
            # Position the two pointers.
            preNode = None
            curNode = self._tail
            done = self._tail is None

            while not done :
                preNode = curNode
                curNode = curNode.next
                done = curNode is self._tail or curNode.data > value

            # Adjust links to insert the node.
            newNode.next = curNode
            preNode.next = newNode


        # Update the count.
        self._count += 1

    def remove( self, value ) :
        assert value in self, " The value must be in the list. "

        preNode = None
        curNode = self._tail

        done = self._tail is None

        while not done :
            preNode = curNode
            curNode = curNode.next
            if curNode.data == value :
                node = curNode

                if curNode is self._tail :
                    if self._tail.next == self._tail :
                        self._tail = None

                    else :
                        preNode.next = curNode.next
                        self._tail = preNode


                else :
                    preNode.next = curNode.next

                self._count -= 1

                return node.data

            else :
                done = curNode is self._tail




# Storage class.
class _listNode :
    def __init__( self, data ) :
        self.data = data
        self.next = None

myList = LinkedList()
myList.add( 21 )
myList.add( 37 )
myList.add( 58 )
myList.add( 74 )
myList.add( 48 )
myList.traverse()
print()
myList.remove( 21 )
myList.traverse()
print()
myList.remove( 58 )
myList.traverse()
print()
myList.remove( 74 )
myList.traverse()
myList.remove( 37 )
myList.remove( 48 )
print()

myList.traverse()
