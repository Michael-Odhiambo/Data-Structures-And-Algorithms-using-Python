
# Implementation of the stack ADT using a singly linked list.
class Stack :
    # Creates an empty stack.
    def __init__( self ) :
        self._top = None
        self._size = 0

    # Returns True if the stack is empty and False otherwise.
    def isEmpty( self ) :
        return self._top is None

    # Returns the number of items in the stack.
    def __len__( self ) :
        return self._size

    # Returns the top item of the stack without removing it.
    def peek( self ) :
        assert not self.isEmpty(), "Cannot peek at an empty stack."
        return self._top.item

    # Removes and returns the top item in the stack.
    def pop( self ) :
        assert not self.isEmpty(), "Cannot pop from an empty stack."
        node = self._top
        self._top = self._top.next
        self._size -= 1
        return node.item

    # Pushes an item onto the top of the stack.
    def push( self, item ) :
        self._top = _StackNode( item, self._top )
        self._size += 1

# Private class for storing the stack nodes.
class _StackNode :
    def __init__( self, item, link ) :
        self.item = item
        self.next = link

myStack = Stack()

myStack.push( 1 )
myStack.push( 2 )
myStack.push( 3 )
myStack.push( 4 )
myStack.push( 5 )
print( len( myStack ) )
print( myStack.isEmpty() )
print( myStack.peek() )
    


    
