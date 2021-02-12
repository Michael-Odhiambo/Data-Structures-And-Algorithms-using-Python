
# Iterative version.

# Print the contents of a singly linked list in reverse order.
def printListRev( head ) :
    # Count the number of nodes in the list.
    numNodes = 0
    curNode = head

    while curNode is not None :
        curNode = curNode.next
        numNodes += 1

    # Iterate over the linked list multiple times. The first iteration
    # prints the last item, the second iteration prints the next to last
    # item, and so on.
    for i in range( numNodes ) :
        # The temporary pointer starts from the first node each time.
        curNode = head

        # Iterate one less time for iteration of the outer loop.
        for j in range( numNodes - i ) :
            curNode = curNode.next

        # Print the data in the node referenced by curNode.
        print( curNode.data )

# Recursive implementation.

def printInRev( head ) :
    if head is not None :
        printInRev( head.next )
        print( head.data )
