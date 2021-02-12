# Merges two sorted lists to create and return a new sorted list.
def mergeSortedLists( listA, listB ) :
    # Create a new list and initialize the markers.
    newList = list()
    a = 0
    b = 0

    while a < len( listA ) and b < len( listB ) :
        if listA[a] < listB[b] :
            newList.append( listA[a] )
            a += 1

        else :
            newList.append( listB[b] )
            b += 1
    # If listA contains more items, add them to the new list.
    while a < len( listA ) :
        newList.append( listA[a] )
        a += 1

    # Or if listB contains more items, add them to the new list.
    while b < len( listB ) :
        newList.append( listB[b] )
        b += 1

    return newList

listA = [ 2, 8, 15, 23, 37 ]
listB = [ 4, 6, 15, 20 ]
newList = mergeSortedLists( listA, listB )
print( newList )
