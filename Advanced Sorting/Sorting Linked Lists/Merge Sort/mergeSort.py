
# Class for creating the node objects.
class _ListNode :
    def __init__( self, data ) :
        self.data = data
        self.next = None

# The function below sorts a linked list using merge sort. A new head reference is returned.
def lListMergeSort( theList ) :
    # If the list is empty( base case ); return None.
    if theList is None :
        return None

    # Split the list into two sublists of equal size.
    rightList = _splitLinkedList( theList )
    leftList = theList

    # Perform the same operation on the left half.
    leftList = lListMergeSort( leftList )

    # .. and the right half.
    rightList = lListMergeSort( rightList )

    # Merge the two ordered sublists.
    theList = _mergeLinkedLists( leftList, rightList )

    # Return the head pointer of the ordered sublist.
    return theList

# Splits a linked list at the midpoint to create two sublists. The head reference of the right sublist
# is returned. The left sublist is still referenced by the original head reference.
def _splitLinkedList( subList ) :
    # Assign a reference to the first and second nodes in the list.
    midPoint = subList
    curNode = midPoint.next

    # Iterate through the list until curNode falls off the end.
    while curNode is not None :
        # Advance curNode to the next node.
        curNode = curNode.next
        # If there are more nodes, advance curNode again and midPoint once.
        if curNode is not None :
            midPoint = midPoint.next
            curNode = curNode.next


    # Set rightList as the head pointer to the right sublist.
    rightList = midPoint.next

    # Unlink the right sublist from the left sublist
    midPoint.next = None

    return rightList

# Merges two sorted linked lists: returns the head reference for the new list.
def _mergeLinkedLists( subListA, subListB ) :
    # Create a dummy node and insert it at the front of the list.
    newList = _ListNode( None )
    newTail = newList

    # Append nodes to the new list until one is empty.
    while subListA is not None and subListB is not None :
        if subListA.data <= subListB.data :
            newTail.next = subListA
            subListA = subListA.next
        else :
            newTail.next = subListB
            subListB = subListB.next

        newTail = newTail.next
        newTail.next = None

    # If subList A contains more items, append them.
    if subListA is not None :
        newTail.next = subListA

    # ...or subListB.
    else :
        newTail.next = subListB

    # Return the new merged list, which begins with the first node after the dummy node.
    return newList.next


node1 = _ListNode( 23 )
node2 = _ListNode( 51 )
node3 = _ListNode( 2 )
node4 = _ListNode( 18 )
node5 = _ListNode( 4 )
node6 = _ListNode( 31 )

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

sortedList = lListMergeSort( node1 )

curNode = sortedList
while curNode is not None :
    print( curNode.data )
    curNode = curNode.next
