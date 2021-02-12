
# Sorts a linked list using the technique of the insertion sort. A reference to the new ordered list is
# returned.

def lListInsertionSort( origList ) :
    # Make sure the list contains at least one node.
    if origList is None :
        return None

    # Iterate through the original list.
    newList = None
    while origList is not None :
        # Assign a temp reference to the first node.
        curNode = origList
        # Advance the original list reference to the next node.
        origList = origList.next
        # Unlink the first node and insert into the new ordered list.
        curNode.next = None
        newList = addToSortedList( newList, curNode )

    # Return the list reference of the new ordered list.
    return newList

# Given a head pointer, insert a value into a sorted linked list. Find the insertion point
# for the new value.
def addToSortedList( theList, theNode ) :
    preNode = None
    curNode = theList  # head.

    while curNode is not None and theNode.data > curNode.data :
        preNode = curNode
        curNode = curNode.next

    theNode.next = curNode

    # Link the new node into the list.
    if curNode is theList :  # head.
        theList = theNode

    else :
        preNode.next = theNode

    return theList

class Node :
    def __init__( self, data ) :
        self.data = data
        self.next = None

node1 = Node( 23 )
node2 = Node( 51 )
node3 = Node( 2 )
node4 = Node( 18 )
node5 = Node( 4 )
node6 = Node( 31 )

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

curNode = node1
while curNode is not None :
    print( curNode.data )
    curNode = curNode.next
print()

sortedList = lListInsertionSort( node1 )

curNode = sortedList
while curNode is not None :
    print( curNode.data )
    curNode = curNode.next