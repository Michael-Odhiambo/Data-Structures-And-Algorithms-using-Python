
# Design and implements a function that reverses the order of items in a queue. Your solution may only
# use operations defined by the Queue ADT, but you are free to use other data structures if necessary.

from stack import Stack
from listQueue import Queue


def reverseQueue( theQueue ) :
    theStack = Stack()
    for i in range( len( theQueue ) ) :
        theStack.push( theQueue.dequeue() )

    for i in range( len( theStack ) ) :
        value = theStack.pop()
        theQueue.enqueue( value )

    return theQueue

myQueue = Queue()
myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)
myQueue.enqueue(4)
myQueue.enqueue(5)
myQueue.enqueue(6)

myQueue = reverseQueue( myQueue )

for i in range( len( myQueue ) ) :
    print( myQueue.dequeue() )

