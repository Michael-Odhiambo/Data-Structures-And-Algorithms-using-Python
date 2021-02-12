
def mergeLists( listA, listB ) :

    # Initialize two index variables to be used with the two lists.
    a = 0
    b = 0

    newList = list()

    # Merge the two list together until one is emtpy.
    while a < len( listA ) and b < len( listB ) :
        if listA[a] < listB[b] :
            newList.append( listA[a] )
            a += 1

        else :
            newList.append( listB[b] )
            b += 1

    # If the list on the left contains more items, append them to the new list.
    while a < len( listA ) :
        newList.append( listA[ a ] )
        a += 1

    # Or if the right subsequence contains more items, append them to the new list.
    while b < len( listB ) :
        newList.append( listB[ b ] )
        b += 1

    return newList

# Sorts a Python list in ascending order using the merge sort algorithm.
def pythonMergeSort( theSeq ) :
    # Check the base case - the list contains a single item.
    if len( theSeq ) <= 1 :
        return theSeq

    else :
        # Compute the midpoint.
        mid = len( theSeq ) // 2
        # Split the list and perform the recursive step.
        leftHalf = pythonMergeSort( theSeq[:mid] )
        rightHalf = pythonMergeSort( theSeq[mid:] )

        # Merge the two orderd sublists.
        newList = mergeLists( leftHalf, rightHalf )
        return newList

mySequence = [ 10, 23, 51, 18, 4, 31, 13, 5 ]
print( pythonMergeSort( mySequence ) )

